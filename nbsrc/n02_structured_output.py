TITLE = "02 · Structured output you can validate"
CELLS = [
    ("md", """# 02 · Structured output you can validate ⏱️ 25 minutes

Free text is for people. Catalogues want fields. This notebook makes the model fill a schema, then checks every answer,
because a small model will confidently invent a value when the card is silent.

**What you'll learn**
1. Define the shape of the answer as a Pydantic model and hand its JSON schema to the model
2. Validate what comes back, and what grammar-enforced output does and does not guarantee
3. See the model invent a missing field, and add a rule that catches it
4. Run twenty catalogue cards in a batch and measure against a gold file"""),
    ("md", "## 02.01 Configuration"),
    ("code", """import os
os.environ.setdefault("WORKSHOP_TIER", "16gb")
from workshop.config import load_settings
settings = load_settings(); MODEL = settings.model
print("Model:", MODEL)"""),
    ("md", """## 02.02 The shape of a record

Every free-text field is a bounded string: `max_length` travels into the schema, and a small model with an open-ended string can run away.
An empty string means "the card does not say". `Literal` restricts the language code to a fixed list. The fields follow the order of
the card itself: creator, title, imprint (place : publisher, year), identifier. The description strings travel into the schema the
model sees, so write them as instructions.

Why not `Optional[str]` with `null`? We tried, in October 2026: at temperature 0 the 8B answered `null` for every optional field in
turn and then poured the whole imprint line into the first free-text field, sometimes repeating it until the window filled.
Schema design is prompt design."""),
    ("code", """from typing import Literal
from pydantic import BaseModel, Field

class Record(BaseModel):
    title: str = Field(max_length=200, description="Title proper as written on the card: the part before any ' : ' subtitle, without statement of responsibility")
    creators: list[str] = Field(max_length=6, description="Persons or bodies responsible, as written, surname first")
    place: str = Field(max_length=60, description="Place of publication, the part before the colon in the imprint line; empty string if the imprint has no place. Never guess it from the publisher")
    publisher: str = Field(max_length=100, description="Publisher name only, the part between the colon and the comma in the imprint line; empty string if absent")
    date: str = Field(max_length=20, description="Year of publication as written, for example 1774; empty string if the card says o.J. or s.d. or gives no year")
    language: Literal["de", "en", "fr", "it", "es", "ja", "other"] = Field(description="Language of the work")
    identifier: str = Field(max_length=60, description="ISBN or DOI if the card has one, digits and hyphens only (no 'ISBN' or 'doi:' prefix); empty string if none")

import json
print(json.dumps(Record.model_json_schema(), indent=1)[:900], "...")"""),
    ("md", """## 02.03 One card, one record

`format=Record.model_json_schema()` makes Ollama constrain the output to the schema (grammar-enforced decoding).
`Record.model_validate_json` then parses it. Temperature 0 for extraction, and a hard ceiling of 300 output tokens so a runaway answer cannot eat the session."""),
    ("code", """from pathlib import Path
from workshop.llm import chat

INSTRUCTIONS = ("Extract the bibliographic record from this catalogue card into the JSON schema. A card has these lines: "
                "the creator (surname first); the title; the imprint as 'Place : Publisher, year'; the extent; sometimes an identifier. "
                "Copy each value as written into its own field. Use an empty string for a field the card does not state; "
                "never guess a place or year.")

def extract(card_text: str, model: str = MODEL) -> Record:
    response = chat(
        [{"role": "user", "content": f"{INSTRUCTIONS}\\n\\nCard:\\n{card_text}"}],
        model=model, format=Record.model_json_schema(), options={"num_predict": 300},
    )
    return Record.model_validate_json(response.message.content)

card = Path("data/cards/card-01.txt").read_text(encoding="utf-8")
print(card)
print(extract(card).model_dump())"""),
    ("md", """## 02.04 What is enforced, and what is not

The grammar guarantees the JSON is well formed and the keys and types match. It does not guarantee the *values* are true.
Try a card with a deliberately missing place of publication."""),
    ("code", """card3 = Path("data/cards/card-03.txt").read_text(encoding="utf-8")
print(card3)
rec3 = extract(card3)
print(rec3.model_dump())
print("place should be empty; the model said:", repr(rec3.place))"""),
    ("md", """In the October 2026 tests both Apertus builds filled the missing French place with the publisher's name. Valid JSON,
wrong fact. Validation rules have to encode what you know about the data."""),
    ("code", """from pydantic import ValidationError, model_validator

class CheckedRecord(Record):
    @model_validator(mode="after")
    def place_is_not_publisher(self):
        if self.place and self.publisher and self.place.strip().lower() == self.publisher.strip().lower():
            raise ValueError("place equals publisher; the card probably has no place")
        return self

def extract_checked(card_text: str, model: str = MODEL, retries: int = 1) -> CheckedRecord:
    messages = [{"role": "user", "content": f"{INSTRUCTIONS}\\n\\nCard:\\n{card_text}"}]
    last_error: ValidationError | None = None
    for attempt in range(retries + 1):
        response = chat(messages, model=model, format=CheckedRecord.model_json_schema(), options={"num_predict": 300})
        try:
            return CheckedRecord.model_validate_json(response.message.content)
        except ValidationError as err:
            last_error = err
            print(f"attempt {attempt + 1}: validation failed: {err.errors()[0]['msg']}")
            messages += [{"role": "assistant", "content": response.message.content},
                         {"role": "user", "content": f"The record failed validation: {err.errors()[0]['msg']}. Fix it and return the JSON again. Use an empty string where the card is silent."}]
    raise last_error

print(extract_checked(card3).model_dump())"""),
    ("md", """## 02.05 A batch of twenty, measured

Run every card, write a CSV, and compare with the gold file. The score tells you how much human review the field needs."""),
    ("code", """import csv, json
gold = {g["file"]: g for g in json.loads(Path("data/cards/cards-gold.json").read_text(encoding="utf-8"))}
rows, correct, total = [], 0, 0
for path in sorted(Path("data/cards").glob("card-*.txt")):
    rec = extract(path.read_text(encoding="utf-8"))
    rows.append({"file": path.name, **rec.model_dump()})
    g = gold[path.name]
    for field in ("title", "date", "place", "publisher", "language", "identifier"):
        total += 1
        correct += (str(getattr(rec, field) or "").strip().lower() == str(g[field] or "").strip().lower())
Path("runs").mkdir(exist_ok=True)
with open("runs/cards-extracted.csv", "w", newline="", encoding="utf-8") as fh:
    writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); writer.writeheader(); writer.writerows(rows)
print(f"{len(rows)} cards, field accuracy {correct}/{total} = {correct/total:.0%}; wrote runs/cards-extracted.csv")"""),
    ("md", """Which fields fail most? This is where a human reviewer should look first."""),
    ("code", """from collections import Counter
misses = Counter()
for row in rows:
    g = gold[row["file"]]
    for field in ("title", "date", "place", "publisher", "language", "identifier"):
        if str(row[field] or "").strip().lower() != str(g[field] or "").strip().lower():
            misses[field] += 1
print(misses.most_common())"""),
    ("md", """Title and language are where the 8B slips most. It copies the subtitle after " : " although the description asks for the title
proper, and it guesses the language of a French or Italian book as English from the imprint. A field description is a hint, not
a guarantee; that is what the gold file and a human reviewer are for."""),
    ("md", """## 02.06 Exercises

🖥️ **GUI:** paste the text of `data/cards/card-03.txt` into the Ollama app together with the `INSTRUCTIONS` text from 02.03 and
the field list from 02.02, and see whether the model invents a place of publication.

🔧 **Run and change:** add a field `pages: str = Field(default="", max_length=40, ...)` with a description, re-run 02.03 on card-02. Did the model copy "375 S."?

🔧 **Run and change:** change `INSTRUCTIONS` to ask for the title in English translation. Is that extraction or invention?

🚀 **Stretch:** add `confidence: float = Field(description="0 to 1")`. Run five cards and compare the confidence values with
the actual errors in 02.05. Small models fill this field without meaning; a real confidence needs a second check, not a number.

🚀 **Stretch:** the same extraction through the OpenAI client. Create the client as in 01.06
(`from openai import OpenAI; oa = OpenAI(base_url=f"{settings.host}/v1", api_key="ollama")`); then
`oa.chat.completions.parse(model=MODEL, messages=..., response_format=Record)` returns `completion.choices[0].message.parsed`."""),
    ("md", """## ✅ Checkpoint

- A Pydantic model defined the answer shape; Ollama enforced the structure; Pydantic validated it
- You saw a well-formed, wrong value and wrote a rule that catches it, with a retry that feeds the error back
- You measured field accuracy on twenty cards and know which fields need a human

Next: `03_vocabulary_search.ipynb`."""),
]
