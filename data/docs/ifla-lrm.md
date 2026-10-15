# IFLA Library Reference Model (text extract)

Source: https://repository.ifla.org/handle/20.500.14598/40 (CC BY 4.0)

 
 
 
 
 
 
 
 
 
 
 
Pat Riva, Patrick Le Bœuf, and Maja Žumer 
 
Consolidation Editorial Group 
of the IFLA FRBR Review Group 
 
 
 
 
Definition of a conceptual reference model to provide a framework for the 
analysis of non-administrative metadata relating to library resources 
 
 
 
 
 
 
August 2017 
Revised after world-wide review 
Endorsed by the IFLA Professional Committee 
 
 
As amended and corrected through 
December 2017 
 
 
 
 
 
 
 
 Pat Riva, Patrick Le Bœuf, and Maja Žumer, 2017 
IFLA Library Reference Model 
 
A Conceptual Model for 
Bibliographic Information 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
© 2017 by Pat Riva, Patrick Le Bœuf, Maja Žumer. This work is licensed under the Creative Commons 
Attribution 4.0 International (CC BY 4.0) license. To view a copy of this license, visit: 
http://creativecommons.org/licenses/by/4.0  
 
IFLA 
P.O. Box 95312 
2509 CH Den Haag 
Netherlands 
 
www.ifla.org   

IFLA LRM (2017-12) 
 
 
3 
 
Table of Contents 
Table of Contents ................................................................................................................................................... 3 
 Introduction .................................................................................................................................. 5 
1.1 Background .............................................................................................................................................. 5 
1.2 Contributors ............................................................................................................................................ 6 
 Methodology ................................................................................................................................. 9 
2.1 Scope and Objectives ............................................................................................................................. 9 
2.2 Conceptual Model as the Basis for Implementation ....................................................................... 10 
2.3 Process of Consolidation of the FR Family of Conceptual Models ............................................. 11 
2.4 Relationship to Other Models ............................................................................................................ 12 
 Users and User Tasks ................................................................................................................ 15 
3.1 User Population Considered ............................................................................................................... 15 
3.2 User Tasks Summary ............................................................................................................................ 15 
3.3 User Tasks Definitions ........................................................................................................................ 16 
 Model Definition........................................................................................................................ 17 
4.1 Entities ................................................................................................................................................... 18 
4.1.1 Introduction ................................................................................................................................ 18 
4.1.2 Class or “isA” Hierarchy for Entities...................................................................................... 18 
4.1.3 Entities Detailed Definition ..................................................................................................... 19 
4.2 Attributes ............................................................................................................................................... 37 
4.2.1 Introduction ................................................................................................................................ 37 
4.2.2 Hierarchy Structure for Attributes .......................................................................................... 37 
4.2.3 Remarks on the Attributes of the Entity Res ........................................................................ 39 
4.2.4 Attributes Detailed Definition ................................................................................................. 39 
4.2.5 Index to Attributes .................................................................................................................... 59 
4.3 Relationships ......................................................................................................................................... 61 
4.3.1 Introduction ................................................................................................................................ 61 
4.3.2 Hierarchy Structure for Relationships .................................................................................... 62 
4.3.3 Relationships Detailed Definition ........................................................................................... 64 
4.3.4 Relationships Ordered by Domain.......................................................................................... 79 
 Model Overview ......................................................................................................................... 83 
5.1 Entity-Relationship Diagrams ............................................................................................................. 83 
5.2 Constraints between Entities and Alignments ................................................................................. 87 
5.3 Modelling of Online Distribution ...................................................................................................... 87 
5.4 Nomens in a Library Context ............................................................................................................. 88 
5.5 Modelling of Bibliographic Identities ................................................................................................ 89 

IFLA LRM (2017-12) 
 
 
4 
 
5.6 Representative Expression Attributes ............................................................................................... 91 
5.7 Modelling of Aggregates ...................................................................................................................... 93 
5.8 Modelling of Serials .............................................................................................................................. 94 
 Alignment of User Tasks with the Entities, Attributes and Relationships ........................ 97 
6.1 Use Cases Illustrating the User Tasks ................................................................................................ 97 
 Glossary of Modelling Terminology ..................................................................................... 100 
 Conceptual Models Consulted ............................................................................................... 101 
 
  

IFLA LRM (2017-12) 
 
 
5 
 
 Introduction 
1.1 Background 
Since the initial publication of the Functional Requirements for Bibliographic Records (FRBR) in 1998, the FR 
family of conceptual models grew to include three separate models for specific aspects of the 
bibliographic universe. In addition to FRBR for bibliographic data, the FR family of conceptual models 
included the Functional Requirements for Authority Data (FRAD) and the Functional Requirements for Subject 
Authority Data (FRSAD). 
 
These models were prepared independently over many years by different working groups: 
 FRBR was the final report of the IFLA Study Group on the Functional Requirements for 
Bibliographic Records. The Study Group was constituted in 1992, and the report was approved 
by the Standing Committee of the Section on Cataloguing on September 5, 1997. 
 FRAD was the outcome of the IFLA Working Group on Functional Requirements and 
Numbering of Authority Records (FRANAR). FRANAR was established in April 1999 by the 
Division of Bibliographic Control and the Universal Bibliographic Control and International 
MARC Programme (UBCIM). The report was approved by the Standing Committees of the 
Cataloguing Section and the Classification and Indexing Section in March 2009. 
 FRSAD was the report of the IFLA Working Group on the Functional Requirements for 
Subject Authority Records (FRSAR), which was formed in 2005. The report was approved by 
the Standing Committee of the IFLA Section on Classification and Indexing in June 2010. 
 
Section 3.2.2 of the FRBR Final report, concerning the definition of the entity expression, was amended as 
a result of the adoption of the recommendation of the Working Group on the Expression Entity 
(2003-2007). Additionally, the Working Group on Aggregates, established by the FRBR Review Group 
in 2005, was tasked to consider the modelling of various types of aggregates. Its recommendations were 
adopted by the FRBR Review Group in August 2011, in San Juan, Puerto Rico, and its final report was 
submitted in September 2011. 
 
Starting in 2003, the FRBR Review Group has held joint meetings with the group within the 
International Council of Museums (ICOM) Committee on Documentation (CIDOC) responsible for 
maintaining the museum community’s internationally agreed-upon conceptual model, the CIDOC 
Conceptual Reference Model (CIDOC CRM). This joint work resulted in the development of a 
formulation using the same object-oriented modelling framework as the CIDOC CRM, of the FRBR 
model and the approval of this model as an official extension of the CIDOC CRM. This reformulation 
of FRBR, known as FRBROO (FRBR object-oriented), was first approved in 2009 as version 1.0 which 
corresponded directly to the original FRBR model. With the subsequent publication of the FRAD and 
FRSAD models, FRBROO was expanded to include the entities, attributes and relationships from the 
FRAD and FRSAD models, starting with FRBROO version 2.0. 
 
Inevitably the three FR models, although all created in an entity-relationship modelling framework, 
adopted different points of view and differing solutions for common issues. Even though all three 
models are needed in a complete bibliographic system, attempting to adopt the three models in a single 
system required solving complex issues in an ad hoc manner with little guidance from the models. Even 
as FRAD and FRSAD were being finalized in 2009 and 2010, it became clear that it would be necessary 
to combine or consolidate the FR family into a single coherent model to clarify the understanding of 
the overall model and remove barriers to its adoption. 
 

IFLA LRM (2017-12) 
 
 
6 
 
The FRBR Review Group worked actively towards a consolidated model starting in 2010, in a series of 
working meetings held in conjunction with IFLA conferences and at an additional mid-year meeting in 
April 2012 during which the user task consolidation was first drafted. In 2013 in Singapore, the FRBR 
Review Group constituted a Consolidation Editorial Group (CEG) to focus on the detailed 
reassessment of attributes and relationships, and the drafting of this model definition document. The 
CEG (at times with other FRBR Review Group members or invited experts) held five multi-day 
meetings, as well as discussing progress in detail with the FRBR Review Group as a whole during a 
working meeting in 2014 in Lyon, France and another in 2015 in Cape Town, South Africa. 
 
A World-Wide Review of the FRBR-Library Reference Model was conducted from February 28 to May 
1, 2016. The CEG held another meeting on May 19-23, 2016 to consider the responses and update the 
draft model. The FRBR Review Group considered that draft at a working meeting in 2016 in 
Columbus, Ohio, USA. At the 2016 meeting, the model was renamed the IFLA Library Reference 
Model (IFLA LRM). 
 
The resulting model definition was approved by the FRBR Review Group (November 2016), and then 
made available to the Standing Committees of the Sections on Cataloguing and Subject Analysis & 
Access, as well as to the ISBD Review Group, for comment in December 2016. The final document 
was approved by the IFLA Committee on Standards and endorsed by the IFLA Professional 
Committee on August 18, 2017. 
1.2 Contributors 
The Consolidation Editorial Group had the principal responsibility for drafting this IFLA LRM model 
definition document. All members of the FRBR Review Group and liaisons during the consolidation 
project, and during the lead-up to the formal consolidation project, made considerable contributions 
during working meetings and through written responses. Members of the CIDOC CRM Special 
Interest Group (CIDOC CRM SIG) who participated in the development of FRBROO version 2.4 
(which was taking place during the same time-frame) raised issues and provided significant reflections. 
 
Consolidation Editorial Group 
Pat Riva, chair (Canada) 
Patrick Le Bœuf (France) 
Maja Žumer (Slovenia) 
 
FRBR Review Group 
Marie Balíková, corresponding member, 2013- 
María Violeta Bertolini, 2015-2016 
Anders Cato, 2006-2009 
Rajesh Chandrakar, 2009-2013 
Alan Danskin, 2005-2009 
Barbora Drobíková, 2015- 
Gordon Dunsire, 2009- 
Elena Escolano Rodríguez, 2011-2015, corresponding member, 2015- 
Agnese Galeffi, 2015- 
Massimo Gentili-Tedeschi, 2015- 
Ben Gu, 2015- 
Patrick Le Bœuf, 2013- 
Françoise Leresche, 2007-2015 
Filiberto Felipe Martínez-Arellano, 2011-2013 
Tanja Merčun, 2013- 
Anke Meyer-Hess, 2013- 

IFLA LRM (2017-12) 
 
 
7 
 
Eeva Murtomaa, 2007-2011, corresponding member, 2011- 
Chris Oliver, chair 2013- 
Ed O’Neill, 2003-2007, and chair Working Group on Aggregates, 2005-2011 
Glenn Patton, 2003-2009 
Pat Riva, chair 2005-2013 
Miriam Säfström, 2009-2014 
Athena Salaba, 2013- 
Barbara Tillett, 2003-2011 
Maja Žumer, 2005-2013 
 
ISBD Review Group liaisons: 
Mirna Willer, 2011-2015 
Françoise Leresche, 2015- 
 
ISSN Network liaisons: 
François-Xavier Pelegrin, 2012-2014 
Clément Oury, 2015- 
 
The following invited experts and past FRBR Review Group members participated in key consolidation 
working meetings: 
Anders Cato, 2010 
Massimo Gentili-Tedeschi, 2013-2014 
Dorothy McGarry, 2011 
Glenn Patton, 2009-2011 
Miriam Säfström, 2016 
Jay Weitz, 2014, 2016 
 
The following CIDOC CRM SIG members were particularly involved in the development of FRBROO 
version 2.4: 
Trond Aalberg 
Chryssoula Bekiari 
Martin Doerr, chair of CIDOC CRM SIG 
Øyvind Eide 
Mika Nyman 
Christian-Emil Ore 
Richard Smiraglia 
Stephen Stead 
 
 
  

IFLA LRM (2017-12) 
 
 
8 
 
  

IFLA LRM (2017-12) 
 
 9 
 Methodology 
2.1 Scope and Objectives 
The IFLA Library Reference Model aims to be a high-level conceptual reference model 
developed within an enhanced entity-relationship modelling framework. The model covers 
bibliographic data as understood in a broad, general sense. In terms of general approach and 
methodology, the modelling process that resulted in the IFLA LRM model adopted the 
approach taken in the original FRBR study, where it was described as follows: 
 
“The study uses an entity analysis technique that begins by isolating the entities 
that are the key objects of interest to users of bibliographic records. The study 
then identifies the characteristics or attributes associated with each entity and 
the relationships between entities that are most important to users in 
formulating bibliographic searches, interpreting responses to those searches, 
and “navigating” the universe of entities described in bibliographic records. The 
model developed in the study is comprehensive in scope but not exhaustive in 
terms of the entities, attributes, and relationships that it defines. The model 
operates at the conceptual level; it does not carry the analysis to the level that 
would be required for a fully developed data model.” (FRBR, p. 4) 
 
The IFLA LRM model aims to make explicit general principles governing the logical structure of 
bibliographic information, without making presuppositions about how that data might be stored 
in any particular system or application. As a result, the model does not make a distinction 
between data traditionally stored in bibliographic or holdings records and data traditionally 
stored in name or subject authority records. For the purposes of the model, all of this data is 
included under the term bibliographic information and as such is within the scope of the model. 
 
IFLA LRM takes its functional scope from the user tasks (see Chapter 3), these are defined from 
the point of view of the end-user and the end-user’s needs. As a result, administrative metadata 
used by libraries and bibliographic agencies solely for their internal functions is deemed out of 
scope of the model. 
 
The model considers bibliographic information pertinent to all types of resources generally of 
interest to libraries; however, the model seeks to reveal the commonalities and underlying 
structure of bibliographic resources. The model selected terms and created definitions so that 
they may be applicable in a generic way to all types of resources, or to all relevant entities. In 
consequence, data elements that are viewed as specialized or are specific to certain types of 
resources, are generally not represented in the model. Nevertheless, a few significant expression 
attributes specific to resources of certain types (such as the attributes language, cartographic scale, 
key, medium of performance) are included. This shows how the model can accommodate such 
expansion, as well as being relevant for the illustration of the application of the work attribute 
representative expression attribute. The model is comprehensive at the conceptual level, but only 
indicative in terms of the attributes and relationships that are defined. 
 
  

IFLA LRM (2017-12) 
 
 10 
2.2 Conceptual Model as the Basis for Implementation 
The conceptual model as declared in IFLA LRM is a high-level conceptual model and as such is 
intended as a guide or basis on which to formulate cataloguing rules and implement 
bibliographic systems. Any practical application will need to determine an appropriate level of 
precision, requiring either expansion within the context of the model, or possibly some 
omissions. However, for an implementation to be viewed as a faithful implementation of the 
model, the basic structure of the entities and the relationships among them (including the 
cardinality constraints), and the attachment of those attributes implemented, needs to be 
respected. 
 
Although the structural relationships between the entities work, expression, manifestation, and item 
are core to the model, the attributes and the other relationships declared in the model are not 
required for implementation. Should some attributes or relationships be omitted as unneeded in 
a particular application, the resulting system can still be considered an implementation of IFLA 
LRM. It is possible for a compatible implementation to omit one of the entities declared in IFLA 
LRM. For example, the entity item may be unneeded in a national bibliography that does not 
provide any item-level information. In that case, none of the attributes defined for the item entity, 
and none of the relationships involving the item entity, can be implemented. Similarly, if the 
existence of a given work is reflected in a given catalogue just because the library which produces 
that catalogue holds copies of studies about that work, but no copy of any edition of that work, 
there is no need to implement the structural relationships from work to item for that instance of 
the entity work. 
 
IFLA LRM provides a number of mechanisms that permit the expansions that are likely to be 
needed in any actual implementation. The definition of a category attribute for the entity res 
permits implementations to create, for any of the entities, those subclasses that might be useful. 
Additional specialized attributes can be added for any or all entities, following the patterns 
provided, to cover, for example, particular resource types or to provide more details about agents. 
Other attributes, such as the manifestation statement, are intended to be sub-typed according to the 
provisions of the cataloguing rules applied by the bibliographic agency. Many relationships are 
defined at a general level, again with the intention that implementations would define pertinent 
refinements. The model provides a structure and the guidance needed so that implementations 
can introduce detail in a consistent and coherent way, fitting it into the basic structure of the 
model. 
 
Definitions of certain key elements in IFLA LRM are intended to be compatible with the 
operationalization of the model through a variety of cataloguing codes. One case is the work 
attribute representative expression attribute, which records the values of those expression attributes 
considered essential in characterizing the work, without predetermining the criteria that may be 
used in making this determination in a particular cataloguing code. 
 
A wide range of decisions made in cataloguing rules can be accommodated by the model. For 
example, the exact criteria that delimit instances of the work entity are not governed by the 
model. As a result, the model does not prescribe the level of adaptation required so that a given 
expression based on an existing expression should be regarded as just another expression of the same 
work, rather than as an expression of a distinct work. However, for the practical purpose of 
illustrating the model, examples are used which reflect generally accepted existing practice as to 
where these boundaries lie. For example, all translations of a given text are traditionally 
collocated, in library catalogues, under the same preferred title, which is an indication that in the 
implicit conceptualization of librarians, all translations are viewed as expressions of the same work; 

IFLA LRM (2017-12) 
 
 11 
rights societies have a very different concept of “work”, and regard each translation as a distinct 
“work”. At a conceptual level, the model accommodates both approaches equally, and is 
agnostic as to what “should” be done; but as this document is addressed to the community of 
librarians, it occasionally introduces the example of translations as expressions, since that example 
is assumed to be easily understood by its intended readers. 
2.3 Process of Consolidation of the FR Family of Conceptual Models 
The model consolidation task was more than a simple editorial process to fit the three models in 
the FR family (FRBR, FRAD, FRSAD) together. Since the three models differed significantly in 
their scopes and points of view, as well as in the solutions adopted to certain common issues, 
choices had to be made in order to ensure the internal consistency of the conceptualization that 
underlies the model. It was essential to adopt a consistent point of view at the outset, so as to 
have a principled basis on which to resolve the differences between the models. Maintaining a 
consistent viewpoint, or making an ontological commitment, requires that, at certain crucial 
points, only a single option among the conceivable alternatives can be considered compatible 
with the model. Developing a consistent, consolidated model required taking a fresh look at all 
the models, which also offered an opportunity to incorporate insights gained since their initial 
publications through user research and experience in working with the models. 
 
For each element in the model (user tasks, entities, attributes, relationships), the existing FRBR, 
FRAD, and FRSAD definitions were examined in parallel, seeking to align them based on their 
intended meanings, and then to develop generalizations. User tasks were examined first, as this 
provided a focus and functional scope for the rest of the modelling decisions. Entities were the 
next element examined, then relationships and attributes alternately. The modelling of entities, 
attributes and relationships was accomplished through several iterations, as each pass revealed 
simplifications and refinements which then needed to be applied consistently throughout the 
model. Finally, all definitions, scope notes and examples were drafted and the full model 
definition checked for consistency and completeness. 
 
A major criterion for the retention or establishment of an entity was that it had to be needed as 
the domain or range of at least one significant relationship or had to have at least one relevant 
attribute that could not logically be generalized to a superclass of the entity. An important factor 
in the assessment of relationships and attributes was to determine whether they could be 
generalized, including whether they could be declared at a higher level using a superclass entity. 
Entities were added if they could then be used to streamline the model by permitting the 
reduction of relationships or attributes. 
 
While entities, and the relationships between them, provide the structure of the model, attributes 
are what gives flesh to the description of an instance of an entity. Whether an attribute is 
“monovalued” or “multivalued” (that is, whether the corresponding data element is considered 
repeatable or non-repeatable) is not prescribed by the model. 
 
There are basically two ways to represent an attribute in an actual implementation: 
 an attribute can be represented as a mere literal (a string, a number…): this is what OWL 
(Web Ontology Language) regards as “datatype properties”; 
 an attribute can be represented as a Uniform Resource Identifier (URI) pointing to an 
external source (a referential or normative document of any kind, such as an authority 
file, or a list of coded values), in which case it could have been modelled as a relationship 
rather than as a mere attribute, but the model is meant to remain agnostic as to the way it 
is to be implemented: this is what OWL regards as “object properties”. 

IFLA LRM (2017-12) 
 
 12 
Some attributes can be represented either way, some can only be represented as literals; for those 
that can only be represented as URIs, the preference was to model them as relationships. 
 
IFLA LRM is presented as a concise model definition document, principally consisting of 
formatted tables and diagrams. Previous experience in creating IFLA vocabularies for the FR 
family of conceptual models indicated that a highly structured document will, for example, make 
the task of specifying namespaces for use with linked open data applications easier and reduce 
the potential for ambiguity. The context has changed since the FRBR model was originally 
developed, and new needs have emerged, particularly in terms of reuse of data in semantic web 
applications, making this consideration an integral part of the initial planning of presentation of 
the model definition. 
 
The definition of the IFLA LRM model presented in the current document is fully self-
contained. No other document is required to follow the model. Specifically, the model definition 
documents of the three previous models are superseded. 
2.4 Relationship to Other Models 
In the same time-period as the IFLA Library Reference Model was being developed, a parallel 
process was taking place in the object-oriented definition of FRBR. FRBROO version 1.0 (first 
published in 2009) expressed the original FRBR model as an extension of the CIDOC 
Conceptual Reference Model (CIDOC CRM) for museum information. It was expanded to 
include the entities, attributes and relationships declared in FRAD and FRSAD, resulting in 
FRBROO version 2.4 (approved in 2016). The modelling exercise behind that expansion informed 
the work of consolidation being undertaken in the entity-relationship formalism of the model, 
but did not predetermine any of the decisions taken in the definition of the IFLA LRM model. 
IFLA LRM aims to be a very general high-level model; it includes less detail compared to 
FRBROO, which seeks to be comparable in terms of generality with CIDOC CRM. 
 
IFLA LRM, as its name indicates, remains a model issuing from the library community for 
library data. It does not presume to constrain other heritage communities in their 
conceptualization of the data relevant to their respective communities. Cross-community 
dialogue in the development of multi-domain ontologies is of great interest, and has potential for 
improved service to users. Establishing a single, consistent model of the library domain, such as 
IFLA LRM, provides a favourable and necessary prerequisite for any joint activity to develop any 
future common model. 
 
IFLA LRM issues from, but is distinct from, the three previous models in the FR family of 
conceptual models, FRBR, FRAD, and FRSAD. To facilitate the transition between the three 
previous models and IFLA LRM, an overview of the major differences along with detailed 
transition mappings have been produced as a separate companion document issued in 2017 
under the title: Transition mappings : user tasks, entities, attributes, and relationships in FRBR, FRAD, and 
FRSAD mapped to their equivalents in the IFLA Library Reference Model. These mappings cover every 
user task, entity, attribute, and relationship defined in FRBR, FRAD, and FRSAD. Starting from 
an alignment of the respective FRBR, FRAD, and FRSAD elements, the transition mappings 
document the resulting disposition of those elements in IFLA LRM. Elements may have been: 
retained (possibly under a different name, or with a generalized definition), merged, generalized, 
modelled differently, or deprecated (deemed out of scope, or otherwise not appropriate for the 
level of the model—for example, some of the elements deprecated as being too granular might 
be implemented in an expansion). A frequent example of a difference in modelling is the case of 

IFLA LRM (2017-12) 
 
 13 
many former attributes, which in IFLA LRM have been modelled as relationships to the entities 
place and time-span.  
 
The Transition mappings is a one-time companion document; these mappings are not needed for 
an understanding of IFLA LRM itself. Their main purpose is to assist in the transition of an 
existing application to IFLA LRM. The mappings are also of interest to anyone following the 
development over time of the IFLA conceptual models. The Transition mappings document will 
not be maintained to reflect any future development of the IFLA LRM model. 
 
 
  

IFLA LRM (2017-12) 
 
 14 
  

IFLA LRM (2017-12) 
 
 15 
 Users and User Tasks 
3.1 User Population Considered 
In framing the user tasks that provide focus for the model, the needs of a wide range of users of 
bibliographic and authority data were considered. The data may be used by readers, students, 
researchers and other types of end-users, by library staff, by other actors in the information 
chain, including publishers, distributors, vendors, etc. Many of the uses made of the data by 
these groups of people can be viewed as specific use cases of the five generic user tasks defined 
in Table 3.2 (section 3.3) below. 
 
The model is primarily concerned with the data and functionality required by end-users (and 
intermediaries working on behalf of end-users) to meet their information needs. Library staff and 
others responsible for the creation and maintenance of the data often use the same data as end-
users to carry out similar tasks in the course of their duties; these tasks are also in scope of the 
model. However, administrative and rights metadata is also needed for the management of 
bibliographic and authority data to enable it to meet user needs. While this data and its 
associated administrative tasks are vital to the provision of service, these tasks are not in the 
scope or orientation of the model. Rights metadata is only in scope insofar as it relates to the 
user’s ability to carry out the obtain task. 
3.2 User Tasks Summary 
The five generic user tasks described in this chapter serve as a statement of the model’s 
functional scope and confirm its outward orientation to the end-user’s needs. The user tasks are 
phrased from the point of view of supporting the user’s ability to carry them out. In the 
description of the tasks, the term “resource” is used very broadly. It includes instances of any of 
the entities defined in the model, as well as actual library resources. This recognizes that library 
resources are what is most relevant from the end-user point of view. 
 
Breaking the information seeking process down into the five generic tasks is intended to draw 
out each of the basic aspects of this process. Although the tasks are listed here in a particular 
order, there is no intention to imply that these are all obligatory steps in an ideal information 
seeking process. In reality information seeking is iterative and may move in a tangent at any 
stage. Some user tasks may happen essentially simultaneously in the user’s mind (identify and select, 
for example). In particular, explore is a separate dimension from the other tasks: in some cases 
providing starting points for further information seeking processes, and in others allowing 
browsing without any particular information goal. 
 
Table 3.1    User Tasks Summary 
Find To bring together information about one or more resources of interest by searching on any relevant 
criteria 
Identify To clearly understand the nature of the resources found and to distinguish between similar resources 
Select To determine the suitability of the resources found, and to be enabled to either accept or reject 
specific resources 
Obtain To access the content of the resource 
Explore To discover resources using the relationships between them and thus place the resources in a context 

IFLA LRM (2017-12) 
 
 16 
3.3 User Tasks Definitions 
Table 3.2    Definitions of User Tasks 
Task Definition Comment 
Find To bring together 
information 
about one or 
more resources 
of interest by 
searching on any 
relevant criteria 
The find task is about searching. The user’s goal is to bring together 
one or more instances of entities as the result of a search. The user 
may search using an attribute or relationship of an entity, or any 
combination of attributes and/or relationships. 
 
To facilitate this task, the information system seeks to enable 
effective searching by offering appropriate search elements or 
functionality. 
Identify To clearly 
understand the 
nature of the 
resources found 
and to distinguish 
between similar 
resources 
The user’s goal in the identify task is to confirm that the instance of 
the entity described corresponds to the instance sought, or to 
distinguish between two or more instances with similar 
characteristics. In “unknown item” searches, the user also seeks to 
recognize the basic characteristics of the resources presented. 
 
To facilitate this task, the information system seeks to clearly 
describe the resources it covers. The description should be 
recognizable to the user and easily interpreted. 
Select To determine the 
suitability of the 
resources found, 
and to be enabled 
to either accept 
or reject specific 
resources 
The select task is about reacting to possible options. The user’s goal is 
to make choices, from among the resources presented, about which of 
them to pursue further. The user’s secondary requirements or 
limitations may involve aspects of content, intended audience, etc. 
 
To facilitate this task, the information system needs to allow/support 
relevance judgements by providing sufficient appropriate 
information about the resources found to allow the user to make this 
determination and act on it. 
Obtain To access the 
content of the 
resource 
The user’s goal in the obtain task is to move from consulting a 
surrogate to actually interacting with the library resources selected. 
 
To fulfill this task, the information system needs to either provide 
direct links to online information, or location information for physical 
resources, as well as any instructions and access information required 
to complete the transaction or any restrictions on access. 
Explore To discover 
resources using 
the relationships 
between them 
and thus place 
the resources in a 
context 
The explore task is the most open-ended of the user tasks. The user 
may be browsing, relating one resource to another, making 
unexpected connections, or getting familiar with the resources 
available for future use. The explore task acknowledges the 
importance of serendipity in information seeking. 
 
To facilitate this task the information system seeks to support 
discovery by making relationships explicit, by providing contextual 
information and navigation functionality. 
 
  

IFLA LRM (2017-12) 
 
 17 
 Model Definition 
The formal model definition presented in this chapter covers the three elements used in entity-
relationship models: 
 entities, the classes which are the focus of interest, described in section 4.1; 
 attributes, the data which characterizes instances of entities, described in section 4.2; 
 relationships, the properties which link instances of entities, described in section 4.3. 
 
In entity-relationship models, the entities define the framework of the model and function as 
nodes, while relationships connect entities to each other. Attributes depend on entities and 
provide information about the entities. Figure 4.1 illustrates the functionality of these modelling 
elements using the options for modelling terms associated with res: either as entities or as 
attributes. The first model (the one adopted in LRM) shows that a single res may be related to 
two distinct instances of a nomen entity by appellation relationships, and all the entities have 
attribute values. The lower model shows the alternative of treating nomens as attributes of the res 
entity. In this case, values of the “name” attribute cannot have attributes in turn, and no 
relationships can be declared between these terms and any other entities in the model. 
 
Figure 4.1    Alternative Entity-Relationship Models for Nomens 
Every element in the model is numbered for unambiguous reference. The numbering 
convention adopted is the prefix “LRM-”, a letter corresponding to the type of element 
(E = entity; A = attribute; R = relationship) and a sequential number. For attributes, the number 
of the entity for which the attribute is defined is inserted prior to the letter “A” (meaning 
attribute) and the sequential number of the attribute, the sequential numbering restarts under 
each entity. Each entity, attribute and relationship is also given a brief name. While these names 
were chosen with the intention of conveying the spirit of the corresponding entity, attribute or 
relationship, it is impossible for a brief term or phrase to fully capture the meanings of the 
elements within the model. Before applying an aspect of the model, it is important to always 
become familiar with the definition and full scope notes of the entity, attribute or relationship. 
RES 
NOMEN  
 1 
Language 
 = 
English 
Scheme 
 = 
xxx authority file 
... 
Attribute  
 1 
Attribute  
 2 
Attribute  
 3 
Attribute  
 4 
... 
NOMEN  
 2 
Language 
 = 
Russian 
Script 
= 
cyrillic 
Scheme 
 = 
yyy authority file 
... 
RES 
Attribute  
 1 
Attribute  
 2 
Attribute  
 3 
Attribute  
 4 
Name 
= 
NOMEN 
 1 
Name 
= 
NOMEN 
 2 
... 

IFLA LRM (2017-12) 
 
 18 
4.1 Entities 
4.1.1 Introduction 
The entities defined in the model are those identified as the key objects of interest to users of 
library information systems. These entities are defined in general, inclusive, terms so as to draw 
out the most relevant features required to fulfill user needs. Entities serve as domains and ranges 
of the relationships highlighted in the model. Attributes defined for each entity serve to further 
define its characteristics. 
 
An entity is an abstract class of conceptual objects; there are many instances of each entity which 
are described in bibliographic, holdings or authority data. One entity may be declared a 
superclass of other entities which then have a subclass relationship to it. Any instance of a 
subclass entity is also an instance of the superclass. This forms part of the structure of enhanced 
entity-relationship models and can be expressed as “is a” (or isA). For example, the entity person 
is a subclass of the entity agent, this can be expressed as: person isA agent. Since all persons are agents, 
any relationship or attribute that applies to the entity agent also applies to the entity person, 
without needing to be explicitly declared for the entity person. The reverse direction does not 
hold; relationships or attributes explicitly defined for subclass entities do not apply to the whole 
superclass. Thus, for example, the entity person has a relationship to the entity place such as “is 
place of birth of”, this relationship does not hold for those agents which are collective agents. 
 
Constraints may operate between different entities. In general, other than those entities related 
by isA hierarchies, the entities declared in the model are disjoint. Disjoint entities can have no 
instance that is simultaneously an instance of more than one of these entities. This means, for 
example, that something cannot be both an instance of the person entity and an instance of the 
collective agent entity. However, something is by nature both an instance of the collective agent entity 
and an instance of the agent entity. Similarly, something cannot be both an instance of the 
manifestation entity (an abstract entity which is a set) and an instance of the item entity (a concrete 
entity). 
 
4.1.2 Class or “isA” Hierarchy for Entities 
Table 4.1 below shows in tabular form the superclass and subclass relationships defined between 
the entities in Table 4.2 (section 4.1.3). The model includes a single top-level entity (res), shown 
in the first column of the table; all other entities are direct or indirect subclasses of res. The eight 
entities that are direct subclasses of res are shown in the second column: work, expression, 
manifestation, item, agent, nomen, place, time-span. The third column shows the two entities that are 
subclasses of the entity agent: person and collective agent. 
 
  

IFLA LRM (2017-12) 
 
 19 
Table 4.1    Entity Hierarchy 
Top Level Second Level Third Level 
LRM-E1  Res   
-- LRM-E2  Work  
-- LRM-E3  Expression  
-- LRM-E4  Manifestation  
-- LRM-E5  Item  
-- LRM-E6  Agent  
-- -- LRM-E7  Person 
-- -- LRM-E8  Collective Agent 
-- LRM-E9  Nomen  
-- LRM-E10  Place  
-- LRM-E11  Time-span  
 
 
4.1.3 Entities Detailed Definition 
Each entity declared in the model is described in Table 4.2 below. Entities are numbered 
sequentially from LRM-E1 to LRM-E11. Following the number, first the name of each entity is 
given, then a brief definition, and a statement of relevant constraints, all in the same row. A 
longer scope note and a selection of examples of instances of that entity are in subsequent table 
rows. To fully understand the intent of each entity, and the kinds of instances that belong to it, it 
is important to consult the definition and the full scope note. The names of the entities are to 
some extent arbitrary, they are intended to serve as shorthand to refer to the entities in the 
sections on attributes and relationships that follow. The name of an entity viewed alone is not 
intended to convey the full meaning behind the entity. 
 
In considering the examples of all the entities other than the entity nomen, it is important to bear 
in mind that instances of entities need to be referred to by a nomen associated with that instance, 
but it is the instance itself which is the example, not the nomen. When necessary to highlight the 
distinction between a res and a nomen representing the res, a description of the instance of the res 
entity is given in curly braces ({ }), while a term representing an instance of the nomen entity is 
given in single quotes (' '). Additionally, where the distinction is necessary, straight double quotes 
(" ") indicate a value of the nomen string attribute of an instance of the nomen entity. 
 
  

IFLA LRM (2017-12) 
 
 20 
Table 4.2    Entities 
ID Name Definition Constraints 
LRM-E1 Res Any entity in the universe of 
discourse 
 
 Scope notes Res (“thing” in Latin) is the top entity in the model. Res includes 
both material or physical things and concepts. Everything 
considered relevant to the bibliographic universe, which is the 
universe of discourse in this case, is included. Res is a superclass 
of all the other entities that are explicitly defined, as well as of 
any other entities not specifically labelled. 
 Examples  {Homer’s Odyssey} [ancient Greek work] 
 {Henry Gray’s Anatomy of the human body} [medical 
work written in the 19th century by Henry Gray] 
 {Codex Sinaiticus} [manuscript containing, among 
others, the Christian Bible in Greek] 
 {Henry Gray} [person, physician, author of medical 
works] 
 {Agatha Christie} [person, author of detective novels] 
 {Miss Jane Marple} [character in numerous Agatha 
Christie novels and stories] 
 {Lassie} [fictional female dog of the Rough Collie breed, 
title character in the novel Lassie come-home by Eric 
Knight, first published in 1940, and appearing in 
numerous film and television spin-offs] 
 {Pal} [lived June 4, 1940-June 1958, a male dog of the 
Rough Collie breed who portrayed the character Lassie 
on film from 1943 to 1954 (several of Pal’s male 
descendants portrayed Lassie in subsequent films and 
television shows)] 
 {Lassie} [female Collie crossbreed dog, living in Lyme 
Regis, UK, who on January 1, 1915 rescued a sailor 
presumed dead, considered the inspiration for the 
character Lassie] 
 {the International Federation of Library Associations and 
Institutions} [an association] 
 {the Romanov family} [the Russian imperial family] 
 {Italian-Canadians} [a group of people who are not a 
collective agent] 
 {Job} [the Biblical figure] 
 {Horus} [the ancient Egyptian deity] 
 {graduates of Queen’s University between 1980-1990} 
[a group of people who are not a collective agent] 
 {anatomy} [a concept] 
 {the Tibetan script} [writing system used for the Tibetan 
language 
 {Eiffel Tower} [a man-made built structure] 
 {console table created by Giovanni Battista Piranesi in 

IFLA LRM (2017-12) 
 
 21 
Table 4.2    Entities 
1769 held by the Rijksmuseum, object number 
BK-1971-14} [a specific object] 
 {Paris, France} [a city] 
 {Atlantis} [a legendary continent] 
 {Earthsea} [a fictional world, the setting of Ursula K. 
Le Guin’s Earthsea trilogy] 
 {the 1920s} [a time-span] 
 {the Battle of Hastings} [an event] 
 {horses} [a species of mammal] 
 {the racehorse Seabiscuit} [a specific, named animal] 
ID Name Definition Constraints 
LRM-E2 Work The intellectual or artistic content 
of a distinct creation 
Superclass: res 
The entities work, 
expression, manifestation, 
item are disjoint 
 Scope notes A work is an abstract entity that permits the grouping of 
expressions that are considered functional equivalents or near 
equivalents. A work is a conceptual object, no single material 
object can be identified as the work. 
 
The essence of the work is the constellation of concepts and 
ideas that form the shared content of what we define to be 
expressions of the same work. A work is perceived through the 
identification of the commonality of content between and among 
various expressions. However, similarity of factual or thematic 
content alone is not enough to group several expressions as 
realizing the same instance of work. For example, two textbooks 
both presenting an introduction to calculus, or two oil paintings 
of the same view (even if painted by the same artist), would be 
considered distinct works if independent intellectual or artistic 
effort was involved in their creation. 
 
In the case of aggregating works and serial works, the essence of 
the work is the concept or plan for the selection, assembly and 
ordering of the expressions of other works to be embodied in the 
resulting aggregate manifestation. 
 
A work comes into existence simultaneously with the creation of 
its first expression, no work can exist without there being (or 
there having been at some point in the past) at least one 
expression of the work. 
 
A work can be recognized retrospectively from an examination 
of the individual realizations or expressions of the work. The 
work consists of the intellectual or artistic creation that lies 
behind all the various expressions of the work. As a result, the 
content identified with an instance of work can evolve as new 

IFLA LRM (2017-12) 
 
 22 
Table 4.2    Entities 
expressions of it are created. 
 
Bibliographic and cultural conventions play a crucial role in 
determining the exact boundaries between similar instances of 
works. User needs are the basis for determining whether 
instances of expression are considered to belong to the same 
instance of work. When the majority of users, for most general 
purposes, would regard the expression instances as being 
intellectually equivalent, then these expressions are considered 
to be expressions of the same work. 
 
Generally, when a significant degree of independent intellectual 
or artistic effort is involved in the production of an expression, 
the result is viewed as a new work with a transformation 
relationship to the source work. Thus paraphrases, rewritings, 
adaptations for children, parodies, musical variations on a theme 
and free transcriptions of a musical composition are usually 
considered to represent new works. Similarly, adaptations of a 
work from one literary or art form to another (e.g., 
dramatizations, adaptations from one medium of the graphic arts 
to another, etc.) are considered to represent new works. 
Abstracts, digests and summaries are also considered to 
represent new works. 
 Examples  {Homer’s Odyssey} 
 {Henry Gray’s Anatomy of the human body} 
 {Agatha Christie’s They do it with mirrors} 
 {Laura Hillenbrand’s Seabiscuit: an American legend} 
 {Eric Knight’s Lassie come-home} 
 {Lassie come home} [film, first release 1943] 
 {Ursula K. Le Guin’s The Earthsea trilogy} 
 {Ursula K. Le Guin’s The tombs of Atuan} [a novel 
which is part of the Earthsea trilogy] 
 {René Goscinny and Albert Uderzo’s Astérix le Gaulois} 
[a collaboratively created work in which Goscinny wrote 
the text and Uderzo created the drawings] 
 {Johann Sebastian Bach’s The art of the fugue} 
 {Wolfgang Amadeus Mozart’s Piano sonata KV 281 in 
B flat major} 
 {Wolfgang Amadeus Mozart’s Rondo KV 494} 
 {Johannes Brahms’s String quartet Op. 51 n. 1 in 
C minor} 
 {IFLA Journal} 
 {IFLA series on bibliographic control} [a monographic 
series, an aggregating work] 
 {François Truffault’s Jules et Jim} 
 {Microsoft Excel} 
 {The Dewey Decimal Classification (DDC)} 

IFLA LRM (2017-12) 
 
 23 
Table 4.2    Entities 
 {WebDewey} [software for displaying and searching the 
DDC, created by Pansoft GmbH] 
 {The Ordnance Survey’s 1:50 000 Landranger series} 
 {Auguste Rodin’s The thinker} 
 {Raoul Dufy’s Racecourse in Epsom} 
 {Barnett Newman’s Voice of fire} 
 {I want to hold your hand} [a song by John Lennon and 
Paul McCartney] 
ID Name Definition Constraints 
LRM-E3 Expression A distinct combination of signs 
conveying intellectual or artistic 
content 
Superclass: res 
The entities work, 
expression, manifestation, 
item are disjoint 
 Scope notes An expression is a distinct combination of signs of any form or 
nature (including visual, aural or gestural signs) intended to 
convey intellectual or artistic content and identifiable as such. 
The term “sign” is intended here in the meaning used in 
semiotics. An expression is an abstract entity distinct from the 
carriers used to record it. 
 
An expression is the specific intellectual or artistic form that a 
work takes each time it is “realized”. Expression encompasses, 
for example, the specific words, sentences, paragraphs, etc. that 
result from the realization of a work in the form of a text, or the 
particular sounds, phrasing, etc. resulting from the realization of 
a musical work. The boundaries of the entity expression are 
defined, however, so as to exclude incidental aspects of physical 
form, such as typeface and page layout for a text, unless, due to 
the nature of the work, these are integral to the intellectual or 
artistic realization of the work as such. 
 
An expression comes into existence simultaneously with the 
creation of its first manifestation, no expression can exist 
without there being (or there having been at some point in the 
past) at least one manifestation. 
 
The process of abstraction leading to the identification of the 
entity expression indicates that the intellectual or artistic content 
embodied in one manifestation is in fact the same, or 
substantially the same, as that embodied in another 
manifestation even though the physical embodiment may differ 
and differing attributes of the manifestations may obscure the 
fact that the content is similar in both. 
 
On a practical level, the degree to which bibliographic 
distinctions are made between variant expressions of a work will 
depend to some extent on the nature of the work itself, on the 

IFLA LRM (2017-12) 
 
 24 
Table 4.2    Entities 
anticipated needs of users and on what the cataloguer can 
reasonably be expected to recognize from the instance of the 
manifestation being described. 
 
Variations within substantially the same expression (e.g., slight 
variations that can be noticed between two states of the same 
edition in the case of hand press production) would be ignored in 
most applications. However, for some applications of the model 
(e.g., comprehensive databases of early printed texts, complete 
listings of the states of prints), each variation may be viewed as 
a different expression. 
 
Inasmuch as the form of expression is an inherent characteristic 
of the expression, any change in form (e.g., from written 
notation to spoken word) results in a new expression. Similarly, 
changes in the intellectual conventions or instruments that are 
employed to express a work (e.g., translation of a textual work 
from one language to another) result in the production of a new 
expression. If a text is revised or modified, the resulting 
expression is considered to be a new expression of the work. 
Minor changes, such as corrections of spelling and punctuation, 
etc., may be considered as variations within the same expression. 
 
When an expression of a work is accompanied by 
augmentations, such as illustrations, notes, glosses, etc. that are 
not integral to the intellectual or artistic realization of the work, 
such augmentations are considered to be separate expressions of 
their own separate work(s). Such augmentations may, or may 
not, be considered significant enough to warrant distinct 
bibliographic identification. 
(Further discussion of aggregates resulting from augmentation 
is found in section 5.7, Modelling of Aggregates.) 
 Examples  The English translation by Robert Fagles of Homer’s 
Odyssey, copyright 1996 
 The English translation by Richmond Lattimore of 
Homer’s Odyssey, copyright 1965 
 English text of Agatha Christie’s They do it with mirrors, 
original copyright 1952 [same English text also 
published under the title Murder with mirrors] 
 Large scale version realized by the fonderie Alexis 
Rudier in 1904 of Auguste Rodin’s The thinker [Rodin’s 
first version in 1880 is approximately 70 cm in height; 
this 1904 version is 180 cm in height] 
 Dewey Decimal Classification, 23rd edition (DDC23) 
[English edition] 
 Classification décimale de Dewey, 23e édition [French 
translation of DDC23] 

IFLA LRM (2017-12) 
 
 25 
Table 4.2    Entities 
 V ocal score of Giuseppe Verdi’s Macbeth 
 A recording of a specific performance by the Amadeus 
Quartet and Hephzibah Menuhin on piano of Franz 
Schubert’s Trout quintet 
 The musical notation of John Lennon and Paul 
McCartney’s song I want to hold your hand 
ID Name Definition Constraints 
LRM-E4 Manifestation A set of all carriers that are 
assumed to share the same 
characteristics as to intellectual or 
artistic content and aspects of 
physical form. That set is defined 
by both the overall content and the 
production plan for its carrier or 
carriers 
Superclass: res 
The entities work, 
expression, manifestation, 
item are disjoint 
 Scope notes A manifestation results from the capture of one or more 
expressions onto a carrier or set of carriers. As an entity, 
manifestation represents the common characteristics shared by 
those carriers, in respect to both intellectual or artistic content 
and physical form. 
 
A manifestation is recognized from the common characteristics 
exhibited by the items resulting from the same production 
process. The specification of the production process is an 
intrinsic part of the manifestation. The production may be 
explicitly planned so as to take place over time, as, for example, 
in printing on demand. The production plan may involve aspects 
that are not under the direct control of the producer, such as the 
specific digital storage media onto which an online file is 
downloaded by different end-users. Whatever storage media is 
used, the downloaded files are instances of the same 
manifestation as the online file. 
 
Production processes cover the range from formal industrial 
processes to artisanal or artistic processes. A production process 
may result in a set of multiple items that are interchangeable for 
most purposes. The manifestation can be defined by the specific 
properties and attributes that any item belonging to that 
manifestation should portray. 
 
In other cases, such as for holograph manuscripts, many 
artisanal or artistic productions or reproductions for preservation 
purposes, the intention is that the production process result in a 
single, unique item. The manifestation in this case is the 
singleton set (a set with a single member) that captures the idea 
of the item in question. 
 

IFLA LRM (2017-12) 
 
 26 
Table 4.2    Entities 
The boundaries between one manifestation and another are 
drawn on the basis of both intellectual or artistic content and 
physical form. When the production process involves changes in 
physical form, the resulting product is considered a new 
manifestation. Changes in physical form include changes 
affecting display characteristics that are incidental to the 
conception of the work (e.g., a change in typeface, size of font, 
page layout, etc.), changes in physical medium (e.g., a change 
from paper to microfilm as the medium of conveyance), and 
changes in the container (e.g., a change from cassette to 
cartridge as the container for a tape). Where the production 
process involves a publisher, producer, distributor, etc., and there 
are changes signalled in the product that are related to 
publication, marketing, etc. (e.g., a change in publisher, 
repackaging, etc.), the resulting product may be considered a 
new manifestation. Whenever the production process involves 
modifications, additions, deletions, etc. (other than minor 
changes to spelling, punctuation, etc.) that affect the intellectual 
or artistic content, the result is a new expression of the work 
which is embodied in a new manifestation. On a practical level, 
the degree to which distinctions between manifestations are 
accounted for in catalogues will depend to some extent on the 
anticipated needs of users and on the differences that the 
cataloguer can reasonably be expected to recognize. Certain 
minor variations or differences in packaging may not be 
considered bibliographically significant and will not warrant the 
recognition of a new manifestation. 
 
Changes that occur deliberately or inadvertently during the 
production process that affect the items result, strictly speaking, 
in a new manifestation of the same expression. A manifestation 
resulting from such a change may be identified as a particular 
“state” or “issue” of the publication. 
 
Changes that occur to an individual item after the production 
process is complete (damage, wear and tear, the loss of a page, 
repairs, rebinding into multiple volumes, etc.) are not considered 
to result in a new manifestation. That item is simply considered 
to be an exemplar of the manifestation that no longer fully 
reflects the original production plan. 
 
However, when multiple items from different manifestations are 
physically combined or joined (books or pamphlets bound 
together, audio tapes spliced together, etc.) the result is a new 
singleton manifestation.  
 Examples  The Odyssey of Homer / translated with an introduction 
by Richmond Lattimore, first Harper Colophon edition 
published in the Perennial library series, in New York by 

IFLA LRM (2017-12) 
 
 27 
Table 4.2    Entities 
Harper & Row in 1967, ISBN 0-06-090479-8 
[manifestation containing the complete text of Richmond 
Lattimore’s English translation of the Greek poem] 
 Homer. The Odyssey / translated by Robert Fagles, 
Penguin Classics, Deluxe edition published in New York 
by Penguin Books in 1997, ISBN 0-670-82162-4 
[manifestation containing the complete text of Robert 
Fagles’ English translation of the Greek poem] 
 Vieux-Québec / textes de Guy Robert ; gravures d’Albert 
Rousseau published in Montréal by Editions du Songe 
and Iconia in 1982 [manifestation of a collaborative work 
consisting of text and engravings] 
 Seabiscuit: an American legend / Laura Hillenbrand 
published in New York by Random House in 2001, 
ISBN 978-0-375-50291-0 [manifestation of the story of 
the racehorse Seabiscuit] 
 They do it with mirrors / Agatha Christie published in the 
UK by William Collins & Sons in 1952 [a manifestation 
of a detective novel] 
 Murder with mirrors / Agatha Christie published in the 
US by Dodd, Mead & Co. in 1952 [another manifestation 
of the same detective novel, published in a different 
country with a different title] 
 The Oxford book of short stories / chosen by V .S. 
Pritchett published in New York by Oxford University 
Press in 1981, ISBN 0-19-214116-3 [an aggregate 
manifestation embodying both an aggregating expression 
which is the intellectual work of the compiler, V .S. 
Pritchett, and the selected expressions of 41 short stories 
by various authors] 
 Voice of fire, acrylic on canvas, painted by Barnett 
Newman in 1967 [singleton manifestation] 
 Codex Sinaiticus, original manuscript [singleton 
manifestation] 
ID Name Definition Constraints 
LRM-E5 Item An object or objects carrying signs 
intended to convey intellectual or 
artistic content 
Superclass: res 
The entities work, 
expression, manifestation, 
item are disjoint 
 Scope notes In terms of intellectual or artistic content and physical form, an 
item exemplifying a manifestation normally reflects all the 
characteristics that define the manifestation itself. 
 
An item is in many instances a single physical object, but in 
other cases, an item may consist of multiple physical pieces or 
objects. An item may be a part of a larger physical object, for 
example, when a file is stored on a disc which also contains 

IFLA LRM (2017-12) 
 
 28 
Table 4.2    Entities 
other files, the portion of the disc holding the file is the physical 
carrier or item. 
 Examples  The manuscript known as the Codex Sinaiticus 
 The manuscript known as the Book of Kells 
 Bronze cast realized by the fonderie Alexis Rudier in 
1904 of Auguste Rodin’s The thinker held at the Musée 
Rodin in Paris, France since 1922, ID number S. 1295 
 Numbered copy 4 (of a limited edition of 50) of Vieux-
Québec / textes de Guy Robert ; gravures d’Albert 
Rousseau published in 1982 in Montréal by Editions du 
Songe and Iconia 
 Voice of fire, acrylic on canvas, painted by Barnett 
Newman in 1967, owned by the National Gallery of 
Canada since 1989 
 Library of Congress Copy 2 of Homer. The Odyssey / 
translated by Robert Fagles, Penguin Classics, Deluxe 
edition published in New York by Penguin Books in 
1997, ISBN 0-670-82162-4 
 Peter Jackson’s personal copy of The lord of the rings. 
The two towers, Special extended DVD edition, 
published in 2003, ISBN 0-7806-4404-2 [a 4-disc set 
with 2 booklets] 
 The ebook Pop Culture by Richard Memeteau, published 
by Zones in 2014 and distributed by Editis in EPUB2 
format, ISBN 978-2-35522-085-2, received by the 
National Library of France through digital legal deposit 
on 1st February 2016 to which the legal deposit number 
DLN-20160201-6 has been assigned. In the catalogue, 
this item is identified with a unique number: 
LNUM20553886 
ID Name Definition Constraints 
LRM-E6 Agent An entity capable of deliberate 
actions, of being granted rights, and 
of being held accountable for its 
actions 
Superclass: res 
Subclasses: person, 
collective agent 
 Scope notes The entity agent is a superclass strictly equivalent to the union 
of the entities person and collective agent. It is defined to reduce 
redundancy in the model by providing a single entity to serve as 
the domain or range of certain relationships that apply to all 
specific types of agents. 
 
Being an agent requires having, or having had, the potential of 
intentional relationships with instances of entities of 
bibliographic interest (works, expressions, manifestations, 
items), whether that specific agent has ever done so or not. 
Human beings are directly or indirectly the motive force behind 

IFLA LRM (2017-12) 
 
 29 
Table 4.2    Entities 
all such actions taken by all agents. 
 
Automatons (such as, weather recording devices, software 
translation programs, etc.), sometimes referred to as 
technological agents, are in this model viewed as tools used and 
set up by an actual agent. 
 Examples  {Margaret Atwood} 
 {Hans Christian Andersen} 
 {Queen Victoria} 
 {the Borromeo family} 
 {BBC Symphony Orchestra} 
 {Symposium on Glaucoma} 
ID Name Definition Constraints 
LRM-E7 Person An individual human being Superclass: agent 
The entities person and 
collective agent are disjoint 
 Scope notes The entity person is restricted to real persons who live or are 
assumed to have lived. 
 
Strict proof of the existence of a person is not required, as long 
as there is a general acceptance of their probable historicity. 
However, figures generally considered fictional (for example, 
Kermit the Frog), literary (for example, Miss Jane Marple) or 
purely legendary (for example, the wizard Merlin) are not 
instances of the entity person. 
 Examples  {Pythagoras} 
 {Marco Polo} 
 {Homer} 
 {Henry Gray} 
 {Agatha Christie} 
 {Richmond Lattimore} 
 {Robert Fagles} 
 {John I of France, King of France and Navarre} [King 
from his birth on November 15, 1316 to his death five 
days later on November 20] 
 {Johann Sebastian Bach} 
 {Raoul Dufy} 
 {the person referred to through the real name 'Charles 
Dodgson' and the pseudonym 'Lewis Carroll'} [author 
and mathematician] 
ID Name Definition Constraints 
LRM-E8 Collective 
Agent 
A gathering or organization of 
persons bearing a particular name 
and capable of acting as a unit 
Superclass: agent 
The entities person and 
collective agent are disjoint 

IFLA LRM (2017-12) 
 
 30 
Table 4.2    Entities 
 Scope notes The entity collective agent designates a wide range of named 
groups of persons that bear a particular name and have the 
potential of acting together as a unit. In addition to families, 
commercial or corporate entities and other legally registered 
bodies, the entity collective agent includes organizations and 
associations, musical, artistic or performing groups, 
governments, and any of their sub-units. The membership of 
many types of collective agents will continue to evolve over 
time. 
 
Occasional groups and groups that are constituted as meetings, 
conferences, congresses, expeditions, exhibitions, festivals, fairs, 
etc., also fall under the definition of collective agent as long as 
they are identified by a particular name and can act as a unit. 
 
Joint pseudonyms or collective pseudonyms are nomens that 
refer to instances of the collective agent entity as the agent 
behind the identity consists of two or more persons bearing a 
particular name and acting as a unit, despite having chosen to be 
identified by a name culturally associated with individual 
persons. 
(Further discussion of individual, collective or joint pseudonyms 
is found in section 5.5, Modelling of Bibliographic Identities.) 
 
A gathering of people is considered a collective agent only when 
it exhibits organizational characteristics that permit them to 
perform actions that reflect agency with respect to instances of 
entities of bibliographic interest (such as approving a report, 
publishing the proceedings of a conference). These collective 
actions may be performed by representatives selected by the 
whole, rather than by all individual members acting together. 
Groups of persons that do not qualify as agents (for example, 
national, religious, cultural or ethnic groups, such as Italian-
Canadians, or gatherings referred to by a general descriptive 
term instead of a particular name) are not instances of the entity 
collective agent. 
 
The essential distinction between a collective agent and a 
gathering of people which is not an instance of the entity 
collective agent, is that the name used by the instance of the 
entity must be a specific name and not just a generic description 
for the gathering. 
 
Families and corporate bodies are specific types of collective 
agents that may be relevant in a particular bibliographic 
application. 
 Examples  {the International Federation of Library Associations and 
Institutions} [an association] 

IFLA LRM (2017-12) 
 
 31 
Table 4.2    Entities 
 {81st World Library and Information Conference, held 
15-21 August 2015 in Cape Town, South Africa} [a 
conference] 
 {Bibliothèque nationale de France} [the national library 
of France] 
 {Friends of the Library} [the “Friends” organization at 
North Carolina State University] 
 {Pansoft GmbH} [a company] 
 {the musical group referred to as 'The Beatles'} 
 {City of Ottawa} [a municipal government] 
 {Canada} [the nation, not the physical territory] 
 {the office of Prime Minister of Canada, held 
successively by individual incumbents} 
 {the Franciscan Order} [a monastic order] 
 {the parish of St. Paul’s Cathedral in London, United 
Kingdom} [an administrative subdivision of a diocese] 
 {the royal house of the Medici} 
 {the Bach family of musicians} 
 {the publishing company referred to as 'Random House'} 
 {the group of 20th century French mathematicians 
publishing under the collective pseudonym 'Nicolas 
Bourbaki', and also known as the 'Association des 
collaborateurs de Nicolas Bourbaki'} 
 {the two cousins who used the joint pseudonym 'Ellery 
Queen' when publishing together in the field of detective 
fiction, and who were also known separately under the 
names 'Frederic Dannay' and 'Manfred Bennington Lee'} 
 {the two women who published together using the joint 
pseudonym 'Virginia Rosslyn', and who never published 
under their real names 'Isabelle A. Rivenbark' and 'Claire 
D. Luna'} 
ID Name Definition Constraints 
LRM-E9 Nomen An association between an entity 
and a designation that refers to it 
Superclass: res 
 Scope notes A nomen associates whatever appellation (i.e., combination of 
signs) is used to refer to an instance of any entity found in the 
bibliographic universe with that entity. Any entity referred to in 
the universe of discourse is named through at least one nomen. 
 
An arbitrary combination of signs or symbols cannot be 
regarded as an appellation or designation until it is associated 
with something in some context. In that sense, the nomen entity 
can be understood as the reification of a relationship between an 
instance of res and a string. The string itself does not constitute 
an instance of the nomen entity but is modelled as the value of 
the nomen string attribute of an instance of the nomen entity. 

IFLA LRM (2017-12) 
 
 32 
Table 4.2    Entities 
Two instances of the nomen entity can have perfectly identical 
values for their nomen string attribute and yet remain distinct, as 
long as they either refer to distinct instances of the res entity, or 
have distinct values for one or more of their other attributes 
(while referring to the same instance of the res entity). 
 
A nomen associates a combination of signs with an instance of 
an entity on the basis of a cultural or linguistic convention: by 
associating a nomen string with a res, the nomen establishes a 
meaning that is not inherent in the nomen string itself. 
Depending on context of use, nomens having identical values for 
their nomen string attribute can involve instances of different 
entities in the real world even within the same language 
(polysemy and homonymy). Conversely, the same instance of an 
entity can be referred to through any number of nomens 
(synonymy). In the controlled environment of a bibliographic 
information system, though, synonymy is avoided and the 
nomen string attribute values of nomens would generally be 
disambiguated, so that each nomen string is associated with only 
one instance of the res entity within the specific scheme. 
 
The identity of a nomen is determined by the combination of the 
res it involves, the choice and order of the symbols used within 
its nomen string attribute, and the values of all of its other 
attributes. Variation in the symbols used (such as transliteration 
into another script) or variation in their ordering usually results 
in a different nomen, but variation in the visual representation of 
the symbols present in the nomen string attribute value (such as 
different fonts that may be used to present alpha-numeric or 
character strings) does not result in a different nomen string. 
 
Nomens are assigned and associated with instances of entities 
either formally (such as by bibliographic agencies) or informally 
through common usage. When nomens are assigned formally, 
the construction of the nomen string attribute value may follow 
predetermined rules. 
 
A nomen string attribute value may consist of components or 
parts. In this case, the corresponding nomen can be viewed as 
being derived from two or more pre-existing nomens, and this 
derivation process may be governed by rules (for example, the 
ordering of name-title access points for works, the citation order 
in a faceted classification scheme, or the order of subdivisions in 
a subject heading system). For example, a new nomen for a 
person may be derived by combining a pre-existing nomen for 
that person and a nomen for the time-span of that person’s 
lifetime; similarly, a new nomen for a work may be derived by 
combining a nomen for a person who authored that work, and a 

IFLA LRM (2017-12) 
 
 33 
Table 4.2    Entities 
pre-existing nomen for that work. 
 Examples Nomens for a person: 
 'Agatha Christie' as a way of referring to {the person 
Dame Agatha Christie, Lady Mallowan} 
 'Agatha Mary Clarissa Miller' as a way of referring to 
{the person Dame Agatha Christie, Lady Mallowan} 
 'Lady Mallowan' as a way of referring to {the person 
Dame Agatha Christie, Lady Mallowan} 
 'Mary Westmacott' as a way of referring to {the person 
Dame Agatha Christie, Lady Mallowan} 
 'Christie, Agatha, 1890-1976' as a way of referring to 
{the person Dame Agatha Christie, Lady Mallowan} 
[preferred access point according to RDA for her 
detective novels and stories] 
 'Westmacott, Mary, 1890-1976' as a way of referring to 
{the person Dame Agatha Christie, Lady Mallowan} 
[preferred access point according to RDA for her 
romance novels] 
Nomens for an international organization in several languages: 
 'United Nations' as a way of referring to {the collective 
agent United Nations} in English 
 'Nations Unies' as a way of referring to {the collective 
agent United Nations} in French 
 'Nazioni Unite' as a way of referring to {the collective 
agent United Nations} in Italian 
 'Vereinigte Nationen' as a way of referring to {the 
collective agent United Nations} in German 
Nomens for a work: 
 'Christie, Agatha, 1890-1976. Murder with mirrors' as a 
way of referring to {the work Murder with mirrors by 
Agatha Christie} [preferred access point in the 
LC/NACO authority file] 
 'Christie, Agatha, 1890-1976. They do it with mirrors' as 
a way of referring to {the work Murder with mirrors by 
Agatha Christie} [variant access point in the LC/NACO 
authority file] 
Nomens for musical works: 
 'Brahms, Johannes, 1883-1897. Quartets, violins (2), 
viola, cello, no. 1, op. 51, no. 1, C minor' as a way of 
referring to {Johannes Brahms’s work String Quartet 
No. 1} [preferred access point according to RDA in the 
LC/NACO authority file] 
 'Brahms, Johannes, 1883-1897. Quartets, strings, no. 1, 
op. 51, no. 1, C minor' as a way of referring to {Johannes 
Brahms’s work String Quartet No. 1} [variant access 
point in the LC/NACO authority file] 
 'Schubert, Franz, 1797-1828. Sonatas, piano, D. 959, 

IFLA LRM (2017-12) 
 
 34 
Table 4.2    Entities 
A major' as a way of referring to {Franz Schubert’s work 
Piano Sonata D. 959} [preferred access point according 
to RDA in the LC/NACO authority file] 
 'Schubert, Franz, 1797-1828. Sonates. Piano. D 959. La 
majeur' as a way of referring to {Franz Schubert’s work 
Piano Sonata D. 959} [preferred access point in the BnF 
authority file] 
Nomens for the one day time-span 2015-03-01: 
 'March 1, 2015' as a way of referring, in English and 
within the Gregorian calendar scheme, to the time-span 
that elapsed between zero o’clock on the 1st of March 
2015 and midnight on the 1st of March 2015 
 '1 marzo 2015' as a way of referring, in Italian and within 
the Gregorian calendar scheme, to the time-span that 
elapsed between zero o’clock on the 1st of March 2015 
and midnight on the 1st of March 2015 
 '01/03/2015' as a way of referring, in the 
DD/MM/YYYY notation convention and within the 
Gregorian calendar scheme, to the time-span that elapsed 
between zero o’clock on the 1st of March 2015 and 
midnight on the 1st of March 2015 
 '10 Adar 5775' as a way of referring, in Romanized 
Hebrew and within the Jewish calendar scheme, to the 
time-span that elapsed between nightfall on the 28th of 
February 2015 and nightfall on the 1st of March 2015 
 '1936 Phalguna 10' as a way of referring, in Romanized 
Hindi and within the Indian civil calendar scheme, to the 
time-span that elapsed between zero o’clock on the 1st of 
March 2015 and midnight on the 1st of March 2015 
Nomens for a subject concept: 
 'Music' as a way of referring to music in LCSH [valid 
term in LCSH] 
 '780' as a way of referring to music in the DDC 
[classification number for the topic {music} in DDC] 
 'Music' as a way of referring to music in LCGFT [valid 
genre term in LCGFT] 
Nomens in the form of identifiers: 
 '978-0-375-50291-0' within the ISBN scheme [ISBN for 
the manifestation: Seabiscuit: an American legend / 
Laura Hillenbrand published in 2001 by Random House] 
 '0000 0001 2102 2127' within the ISNI scheme [ISNI for 
the identity {Agatha Christie}] 
 '0000 0003 6613 0900' within the ISNI scheme [ISNI for 
the identity {Mary Westmacott}] 
Nomens and the notions of polysemy and homonymy: 
 'Lusitania' as a way of referring to the ancient Roman 
province that corresponds to current Portugal and part of 

IFLA LRM (2017-12) 
 
 35 
Table 4.2    Entities 
current Spain in the Iberian Peninsula 
 'Lusitania' as a way of referring to the British luxury liner 
that was sunk by a German submarine in the North 
Atlantic on May 7, 1915 
 'Verve' as a way of referring to {the record label Verve} 
 'Verve' as a way of referring to {the periodical Verve} 
 'Verve' as a way of referring to {the rock music band 
Verve} 
 'Verve' as a way of referring to {the notion of vivacious 
eloquence} in the English language 
 'Verve' as a way of referring to {the notion of vivacious 
eloquence} in the French language 
ID Name Definition Constraints 
LRM-E10 Place A given extent of space  Superclass: res 
 Scope notes The entity place, as relevant in a bibliographic context, is a 
cultural construction; it is the human identification of a 
geographic area or extent of space. Places are usually identified 
through a physical object (a geographical feature or a man-made 
object), or due to their relevance with regards to a particular 
agent (geopolitical entities such as countries, cities), or as the 
location of an event. The place as an extent of space is distinct 
from any governing bodies that exercise jurisdiction in that 
territory. The government responsible for a territory is a 
collective agent. Places can be contemporary or historical, on 
Earth or extra-terrestrial. Imaginary, legendary or fictional 
places are not instances of the place entity. 
 
A place can have fuzzy boundaries. The boundaries of a place 
can change over time (such as a city that absorbs adjacent 
suburbs) without changing the identity of the place for 
bibliographic purposes. 
 
As it can be a moving frame of reference, the entity place is not 
necessarily identified by its geospatial coordinates alone. 
 Examples  {Montréal (Québec)} [area culturally identified as a 
place although the central city has absorbed adjacent 
towns throughout its history] 
 {Lutèce} 
 {Clonmacnoise} [area where the ruins of the destroyed 
monastery of Clonmacnoise are still to be seen] 
 {Greenland} 
 {Italy} 
 {Africa} 
 {St. Lawrence River} 
 {Lake Huron} 
 {Mars} 

IFLA LRM (2017-12) 
 
 36 
Table 4.2    Entities 
ID Entity Definition Constraints 
LRM-E11 Time-span A temporal extent having a 
beginning, an end and a duration 
Superclass: res 
 Scope notes A time-span is a period of time that can be identified by 
specifying its beginning and end. The resulting duration can be 
associated with actions or occurrences that happened during that 
period of time. Even a very precise time-span has a measurable 
duration, however brief it may be. 
 
In library implementations, the instances of time-span 
considered useful in bibliographic or authority data are often 
expressed in years (year of birth of a person, year of death of a 
person, year a corporate body ceased to exist, year of publication 
of a manifestation), even though the associated event took place 
during only a portion of the year. 
 
The information available to the cataloguer, or the inherent 
characteristics of the time-span being identified, will be reflected 
in the degree of precision used in recording of a temporal extent. 
For example, '14th century' may be sufficiently precise in 
recording the beginning of the Renaissance, while a decade may 
be more appropriate when identifying the beginning of a musical 
style. 
 
Dates serve as the appellations or nomens for time-spans in 
different calendar or time-keeping systems. Time-spans can also 
be referred to by more general terms, such as for ages, 
geological eras, or epochs. 
 Examples  {the period of time beginning on 1st January 2015, 
ending on 31 December 2015, and having a duration of 
one year} [may be referred to as '2015 A.D.' (using Anno 
Domini) or as '2015 CE' (using common era)} 
 {2015-03-01} [time-span of a day expressed in the 
Gregorian calendar in YYYY-MM-DD format] 
 {20120808094025.0} [time-span of one-tenth of a 
second expressed in YYYYMMDDHHMMSS.S format] 
 {Twentieth Century} 
 {Ordovician Period} [time-span lasting from 488.3 to 
443.7 million years before present] 
 {488.3 million years before present} [time-span of the 
beginning of the Ordovician period] 
 {Ming Dynasty} 
 {Bronze Age} [a time-span although the exact time 
covered will vary depending on location] 
 {Age of Enlightenment} 
 
  

IFLA LRM (2017-12) 
 
 37 
4.2 Attributes 
4.2.1 Introduction 
Attributes characterize specific instances of an entity. None of the attributes defined in the 
model are required for any given instance of an entity, but attributes may be recorded if 
applicable and easily ascertainable, when the data is considered relevant to the purpose of the 
application. The conceptual model defines and describes the content of the attribute, but each 
application needs to provide details on the method for recording the data. Data for an attribute 
may be recorded in accordance with a controlled list or vocabulary, or as a natural language 
literal in a language and script preferred by the agency recording the data. Given instances of 
entities may have several values for a particular attribute, either simultaneously or over time. 
Such attributes are termed multivalued. 
 
The attributes presented under each entity are representative and are not in any way to be 
considered an exhaustive listing of attributes that might be determined to be useful in a particular 
application. An application can define additional attributes to record additional relevant data or 
to record data at a greater level of granularity than is illustrated. Certain attributes that are 
important to the model or are frequently relevant in bibliographic systems are included here. 
However, the listing of an attribute in the model is not intended in any way to imply that these 
attributes are required for any application. 
 
Only the entities declared in section 4.1.3 (Entities Detailed Definition) have attributes defined 
for them in the model. The entity collective agent does not have any defined attributes. Entity 
subclassing results in attribute sub-types. For example, as the entities person and collective agent are 
subclasses of the entity agent, all attributes defined for the agent entity can also be applied to the 
person or collective agent entities, and do not need to be explicitly defined for those entities. 
However, the reverse does not hold. Attributes specifically defined for the entity person cannot be 
extended to the superclass entity agent. 
 
4.2.2 Hierarchy Structure for Attributes 
Table 4.3 below summarizes in a concise tabular form the attributes defined in the model. 
Following the entity hierarchy structure (shown in full in Table 4.1 in section 4.1.2), attributes 
may also feature hierarchy. In particular, the category attribute of the entity res is sub-typed to 
provide category attributes for certain subclass entities of res. These are the only attributes defined 
at the lower level in the model, and are given in the fourth column of the table. All the other 
attributes are at the same level and are given in the third column. In an expansion of the model, 
additional lower-level attributes may be defined. In this table, the third level entity person is 
shown in the same column as the second level entities (the entity collective agent is not shown, as it 
does not have any defined attributes). The full definitions of all the attributes are given in 
Table 4.4 (Attributes) in section 4.2.4. 
 
 
  

IFLA LRM (2017-12) 
 
 38 
Table 4.3    Attribute Hierarchy 
Entity Top Level Entity Lower Levels Attribute Top Level Attribute Lower Level 
LRM-E1  Res  LRM-E1-A1  Category  
-- LRM-E2  Work -- LRM-E2-A1  Category 
-- LRM-E3  Expression -- LRM-E3-A1  Category 
-- LRM-E4  Manifestation -- LRM-E4-A1  Category 
of carrier 
-- LRM-E9  Nomen -- LRM-E9-A1  Category 
-- LRM-E10  Place -- LRM-E10-A1  Category 
LRM-E1  Res  LRM-E1-A2  Note  
-- LRM-E2  Work LRM-E2-A2  Representative 
expression attribute 
 
-- LRM-E3  Expression LRM-E3-A2  Extent  
-- LRM-E3  Expression LRM-E3-A3  Intended audience  
-- LRM-E3  Expression LRM-E3-A4  Use rights  
-- LRM-E3  Expression LRM-E3-A5  Cartographic scale  
-- LRM-E3  Expression LRM-E3-A6  Language  
-- LRM-E3  Expression LRM-E3-A7  Key  
-- LRM-E3  Expression LRM-E3-A8  Medium of performance  
-- LRM-E4  Manifestation LRM-E4-A2  Extent  
-- LRM-E4  Manifestation LRM-E4-A3  Intended audience  
-- LRM-E4  Manifestation LRM-E4-A4  Manifestation statement  
-- LRM-E4  Manifestation LRM-E4-A5  Access conditions  
-- LRM-E4  Manifestation LRM-E4-A6  Use rights  
-- LRM-E5  Item LRM-E5-A1  Location  
-- LRM-E5  Item LRM-E5-A2  Use rights  
-- LRM-E6  Agent LRM-E6-A1  Contact information  
-- LRM-E6  Agent LRM-E6-A2  Field of activity  
-- LRM-E6  Agent LRM-E6-A3  Language  
-- --        LRM-E7  Person LRM-E7-A1  Profession / Occupation  
-- LRM-E9  Nomen LRM-E9-A2  Nomen string  
-- LRM-E9  Nomen LRM-E9-A3  Scheme  
-- LRM-E9  Nomen LRM-E9-A4  Intended audience  
-- LRM-E9  Nomen LRM-E9-A5  Context of use  
-- LRM-E9  Nomen LRM-E9-A6  Reference source  
-- LRM-E9  Nomen LRM-E9-A7  Language  
-- LRM-E9  Nomen LRM-E9-A8  Script  
-- LRM-E9  Nomen LRM-E9-A9  Script conversion  
-- LRM-E10  Place LRM-E10-A2  Location  
-- LRM-E11  Time-span LRM-E11-A1  Beginning  
-- LRM-E11 Time-span LRM-E11-A2  Ending  
 

IFLA LRM (2017-12) 
 
 39 
4.2.3 Remarks on the Attributes of the Entity Res 
Category attribute: As the category attribute is declared for the entity res, it automatically can be sub-
typed to apply to any entity. Due to the significant use cases for categorization of certain entities, 
some entity-specific sub-types of the general category attribute are declared in the model and given 
their own attribute numbers. This does not imply that the general category attribute cannot be 
sub-typed under the other entities, if considered useful by an application. Category attributes serve 
to sub-type or sub-categorize the entity according to a typology or categorization scheme 
relevant to a particular application. Several independent types of categorizations may be applied 
to an entity in a particular implementation. Depending on the needs of the implementation, the 
entity types defined through the use of the category attribute can function as specific entities that 
are subclasses of the entity in question. This mechanism serves to extend the model with specific 
details. The examples given are not intended to be interpreted as proposing controlled 
vocabularies for these means of categorization, as any established controlled vocabulary can be 
adopted. 
 
Note attribute: Declared for the entity res, the note attribute can be sub-typed to apply to any 
entity. Notes permit the association of information relating to an instance of an entity with that 
entity. The note attribute can be implemented to accommodate information which is stored as 
free-text instead of as a specific structured attribute or relationship. 
 
4.2.4 Attributes Detailed Definition 
Each attribute declared in the model is described in Table 4.4 below. The attributes are grouped 
by the entity to which each attribute is attached. The entities are presented in the order that 
follows their presentation in Table 4.2 (Entities) in section 4.1.3. Attributes are numbered 
sequentially within each entity; for example, the attributes of the entity expression (numbered 
LRM-E3 in Table 4.2) are numbered from LRM-E3-A1 to LRM-E1-A8. The order of 
presentation of attributes within each entity is as follows: the category attribute (if specifically 
declared for the entity) is listed first, then attributes are listed by logical grouping, then in 
alphabetical order. For each attribute, the columns of the first row in the table present, after the 
number and the entity, a brief name of the attribute, followed by a brief definition. A longer 
scope note, if needed, and a selection of examples of that attribute, are given in subsequent table 
rows. To fully understand an attribute, it is important to consult the definition and the full scope 
note. The name of an attribute viewed alone is not intended to convey the full meaning behind 
the attribute. 
 
As this model is meant to remain extremely generic, this Table focuses on those attributes that 
can serve to describe any type of instance of a given entity. However, some more specific 
attributes are also provided. As a model emanating from and intended to be used by the library 
community, the significance and utility of attributes pertaining to texts, such as the language 
attribute, or music, such as the medium of performance attribute, is recognized. These more specific 
attributes are listed, for the entity expression, after the more generic ones, and are introduced by a 
statement which indicates that they do not apply to all types of instances of the entity to which 
they are attached. 
 
Most attributes are multivalued, although Table 4.4 does not explicitly state which are and which 
are not. For example, multiple independent categorization schemes may be applied to works; 
however, when categorized with respect to termination intention, the respective definitions 
dictate that an instance of a work cannot be both a monograph and a serial at the same time. 
 

IFLA LRM (2017-12) 
 
 40 
In most cases when an attribute can be represented either as a literal or as a URI, the examples 
provide illustrations of both possibilities (although no effort is made for completeness). A 
majority of the examples are taken from actual databases, or from existing authoritative 
documentation (such as the UNIMARC Manual), using versions in force as of 2015. 
Occasionally, some examples are taken from sources external to libraries, in order to show that 
this model, although focusing on library applications, is not meant to limit itself to the library 
community. Although many examples are given in various MARC formats (namely MARC 21, 
UNIMARC, and INTERMARC), this model is developed very much with semantic web 
technologies in mind, and it is hoped that in the future, an update of this document will provide 
RDF examples as well. In the MARC examples, the following display conventions have been 
adopted: the field tag is shown preceding the indicators and subfield contents; a value of 'blank' 
in an indicator is shown with the hash mark (#); display spaces are shown both before and after 
subfield codes. 
 
To distinguish between an instance of the entity nomen and the value of the nomen string attribute 
for a given instance of nomen, the following notation convention is adopted: single quotes (' ') 
indicate an instance of the nomen entity, while straight double quotes (" ") indicate a value of the 
nomen string attribute of an instance of the nomen entity. 
 
Table 4.4    Attributes 
ID Entity Attribute Definition 
LRM-E1-A1 RES Category A type to which the res belongs 
 Scope notes  
 Examples  object 
 work 
 concept 
 event 
 family 
 corporate body 
ID Entity Attribute Definition 
LRM-E1-A2 RES Note Any kind of information about a res 
that is not recorded through the use of 
specific attributes and/or relationships 
 Scope notes  
 Examples  Imprint stamped on verso of t.p. [general note 
on a manifestation] 
 Fourth manned mission in the Apollo program. 
[part of general note on an object, namely the 
Apollo 10 spacecraft, in the Library of Congress 
Authorities] 
 Surgery performed on an outpatient basis. May 
be hospital-based or performed in an office or 
surgicenter. [general note on a concept] 
 Deacidified copy. [general note on an item] 
 317 ## $a Inscription on the title page in 
sixteenth century hand, ‘Iohannes Wagge me 

IFLA LRM (2017-12) 
 
 41 
Table 4.4    Attributes 
iure tenet’ $5 DB/S-5-KK.555 [note on 
ownership history of an item as expressed in a 
UNIMARC field] 
ID Entity Attribute Definition 
LRM-E2-A1 WORK Category A type to which the work belongs 
 Scope notes The category attribute can characterize a given work 
with regard to various categorizations: 
- categorization as to termination intention, 
- categorization as to creative domain, 
- categorization as to form / genre, 
- etc. 
 Examples Categorization as to termination intention: 
 monograph 
 serial 
Categorization as to creative domain: 
 literature 
 music 
 fine arts 
Categorization as to form / genre: 
 novel 
 play 
 poem 
 essay 
 symphony 
 concerto 
 sonata 
 fnk [UNIMARC code for: funk] 
 sou [UNIMARC code for: soul music] 
 drawing 
 painting 
 photograph 
ID Entity Attribute Definition 
LRM-E2-A2 WORK Representative 
expression 
attribute 
An attribute which is deemed essential 
in characterizing the work and whose 
values are taken from a representative 
or canonical expression of the work 
 Scope notes Generally, the representative expression attribute will 
be typed and the types chosen will vary depending on 
the context of use (as given by the cataloguing rules, 
the nature of catalogue, or the category of work). Each 
of the attributes chosen may itself be multivalued. The 
values of these attributes are inferred either from 
particular expressions considered to best represent the 
work, or from characteristics abstracted from a more or 

IFLA LRM (2017-12) 
 
 42 
Table 4.4    Attributes 
less nebulous network of similar expressions. There is 
no requirement to precisely identify an expression or 
expressions which serves as source for the values of the 
representative expression attributes, nor does that 
expression need to be recorded in the case where it is 
identified.  
(For additional discussion of the function of this 
attribute in the model, see section 5.6, Representative 
Expression Attributes.) 
 Examples For textual works: 
 Language: English 
 Intended audience: children 
For musical works: 
 Key: B flat minor 
 Medium of performance: violin 
For cartographic works: 
 Cartographic scale: 1:10,000 
 Projection: Albers equal-area conic projection 
For moving image works: 
 Aspect ratio: 16:9 
 Colourization: hand-colouring 
For art works: 
 Medium of execution: sculpture 
ID Entity Attribute Definition 
LRM-E3-A1 EXPRESSION Category A type to which the expression belongs 
 Scope notes The category attribute can characterize a given 
expression with regard to various categorizations: 
- content type, 
- state of development, 
- format of notated music, 
- etc. 
 Examples Content type, expressed in natural language, in English: 
 written notation 
 musical notation 
 recorded sound 
Content type, expressed as English language terms 
from the ISBD Content Form controlled vocabulary: 
 dataset 
 image 
 music 
 text 
Content type, expressed as URI from the ISBD Content 
Form controlled vocabulary: 
 http://iflastandards.info/ns/isbd/terms/contentfor
m/T1001 

IFLA LRM (2017-12) 
 
 43 
Table 4.4    Attributes 
 http://iflastandards.info/ns/isbd/terms/contentfor
m/T1002 
 http://iflastandards.info/ns/isbd/terms/contentfor
m/T1004 
 http://iflastandards.info/ns/isbd/terms/contentfor
m/T1009 
Categorization as to state of development expressed in 
natural language, in English: 
 draft 
 final 
Categorization (applicable to content type of notated 
music) as to format of notated music, expressed in 
natural language, in English: 
 vocal score 
 piano conductor part 
 etc. 
Categorization (applicable to content type of notated 
music) as to musical notation used, expressed in natural 
language, in English: 
 graphic notation 
 neumatic notation 
 etc. 
ID Entity Attribute Definition 
LRM-E3-A2 EXPRESSION Extent A quantification of the extent of the 
expression 
 Scope notes The value of the extent attribute consists of three 
elements: 
- a type of extent (e.g., length of text, envisioned 
duration of performance of musical notation, actual 
duration of recorded performance, etc.), 
- a number, 
- and a measurement unit (words, minutes, etc.). 
 
The type of extent and the measurement unit may be 
given implicitly. The level of precision used in 
recording the quantification of the extent may vary. 
 Examples  approximately 8 minutes [performance time 
stated in natural language, in English, on a 
musical score] 
 306 ## ‡a 002052 ‡a 000415 ‡a 000956 
‡a 003406 [durations encoded in a MARC 21 
field] 
ID Entity Attribute Definition 
LRM-E3-A3 EXPRESSION Intended 
audience 
A class of users for which the 
expression is intended 

IFLA LRM (2017-12) 
 
 44 
Table 4.4    Attributes 
 Scope notes The intended audience attribute can characterize a 
given expression by indicating groups of end-users for 
which expressions with those features are deemed 
particularly appropriate: 
- categorization as to age group, 
- categorization as to sensory impairment, 
- categorization as to educational level, 
- categorization as to occupational group, 
- etc. 
 Examples Categorization as to age group: 
 children 
 young adults 
 adults 
Categorization as to sensory impairment: 
 users able to read braille 
 users needing a visual description 
 users needing closed captioning 
Categorization as to educational level: 
 primary 
 secondary 
ID Entity Attribute Definition 
LRM-E3-A4 EXPRESSION Use rights A class of use restrictions to which the 
expression is submitted 
 Scope notes  
 Examples  Reproduction is submitted to authorization. 
[rights expressed in natural language, in 
English] 
 The play can be read or performed anywhere, 
by any number of people. Anyone who wishes 
to do it should contact the author’s agent [...], 
who will license performances free of charge 
provided that no admission fee is charged and 
that a collection is taken at each performance 
for Medical Aid for Palestinians [...]. 
[performing rights attached to Caryl Churchill’s 
play Seven Jewish children, expressed in natural 
language, in English] 
  Attributes applicable only to specific types of 
expression  
ID Entity Attribute Definition 
LRM-E3-A5 EXPRESSION Cartographic 
scale 
A ratio of distances in a cartographic 
expression to the actual distances they 
represent 

IFLA LRM (2017-12) 
 
 45 
Table 4.4    Attributes 
 Scope notes The cartographic scale attribute is specific to 
expressions of cartographic works. 
 
The cartographic scale attribute may apply to 
horizontal, vertical, angular, and/or other distances 
represented in the expression. 
 Examples  Scale 1 : 10,000 [cartographic scale expressed 
in natural language, in English] 
 034 1# ‡a a ‡b 100000 [cartographic scale 
expressed in normalized form in a MARC 21 
field] 
ID Entity Attribute Definition 
LRM-E3-A6 EXPRESSION Language A language used in the expression 
 Scope notes The language attribute is specific to expressions 
consisting solely or partially of linguistic signs (either 
sonic or in notated form). 
 
The language attribute of the expression may include a 
number of languages, each pertaining to an individual 
component of the expression. 
 Examples  it [language Italian expressed as an ISO 639-1 
code] 
 bre [language Breton expressed as an ISO 
639-2 code] 
 Slovene [language expressed as an English 
natural term] 
 Slovenian [alternative name for a language 
expressed as an English natural term] 
 http://id.loc.gov/vocabulary/iso639-1/zu 
[language Zulu expressed as a URI] 
ID Entity Attribute Definition 
LRM-E3-A7 EXPRESSION Key A pitch structure (musical scale, 
ecclesiastic mode, raga, maqam, etc.), 
that characterizes the expression 
 Scope notes The key attribute is specific to expressions of musical 
works. 
 
The term “key” is broadly defined to encompass 
various musical traditions. This attribute is not 
restricted to Western art music. 
 Examples  C major [key expressed in natural language, in 
English] 
 128 […] $d dm [key of D minor expressed as a 

IFLA LRM (2017-12) 
 
 46 
Table 4.4    Attributes 
code in a UNIMARC subfield] 
 Hypolydian mode [mode expressed in natural 
language, in English] 
 8th ecclesiastical mode [mode expressed in 
natural language, in English] 
 Bayati [maqam expressed in natural language, 
in English] 
 بياتي [maqam expressed in natural language, in 
Arabic] 
ID Entity Attribute Definition 
LRM-E3-A8 EXPRESSION Medium of 
performance 
A combination of performing tools 
(voices, instruments, ensembles, etc.) 
stated, intended, or actually used in the 
expression 
 Scope notes The medium of performance attribute is specific to 
expressions of musical works. 
 
The value of the medium of performance attribute 
includes at least one unit consisting of: 
- a number (implicit through the use of a singular noun, 
or explicitly stated), 
- and a type of performing tool (which may include: 
types of human voice tessitura, types of individual 
instruments, types of ensembles, etc.). 
 Examples  flute, oboe, glass harmonica, viola, cello 
[medium of performance expressed in natural 
language, in English; number of performers 
(1 per instrument) is implicit through the use of 
singular nouns] 
 flutes (2), oboes (2), clarinets (2), horn, bassoon 
[medium of performance expressed in natural 
language, in English; number of performers is 
either implicit (when it equals 1) or explicitly 
stated (2)] 
 clarinet or viola [medium of performance 
expressed in natural language, in English, 
including an alternative] 
 382 0# ‡a trumpet ‡n 2 ‡a trombone ‡n 2 ‡s 4 
[medium of performance expressed in a 
MARC 21 field] 
 146 0# $a b $c 01svl#### $c 01kpf#### $i 002a 
[medium of performance of instrumental music, 
violin and piano, two performers expressed as 
codes in a UNIMARC field] 
 http://id.loc.gov/authorities/performanceMediu
ms/mp2013015841 [medium of performance of 

IFLA LRM (2017-12) 
 
 47 
Table 4.4    Attributes 
solo vocal ensemble expressed as a URI] 
 <perfMedium><performer><instrV oice>violin<
/instrV oice></performer><performer><instrV oi
ce>viola</instrV oice></performer><performer
><instrV oice>violoncello</instrV oice></perfor
mer></perfMedium> [medium of performance 
expressed in the MEI (Music Encoding 
Initiative) schema] 
ID Entity Attribute Definition 
LRM-E4-A1 MANIFESTATION Category of 
carrier 
A type of material to which all physical 
carriers of the manifestation are 
assumed to belong 
 Scope notes The category of carrier attribute can characterize a 
given manifestation with regard to various 
categorizations: 
- categorization as to general type of carrier (e.g., 
sheet), 
- categorization as to physical material employed in 
manufacturing the carriers (e.g., plastic), 
- categorization as to the physical material that is 
applied to the base material of the carriers (e.g., oil 
paint), 
- categorization as to the means used to record notation, 
sound, or images in the production of a manifestation 
(e.g., analogue), 
- etc. 
 
The carrier for a manifestation consisting of multiple 
physical components may include more than one form 
(e.g., a filmstrip with an accompanying booklet, a 
separate sound disc carrying the sound track for a film, 
etc.). 
 Examples Categorization as to general type of carrier, expressed 
in natural language, in English: 
 sound cassette 
 videodisc 
 microfilm cartridge 
 transparency 
Categorization as to physical material employed in 
manufacturing the carriers: 
 paper 
 wood 
 plastic 
 metal 
 
 

IFLA LRM (2017-12) 
 
 48 
Table 4.4    Attributes 
Categorization as to the physical material that is 
applied to the base material of the carriers: 
 oil paint [applied to canvas] 
 chemical emulsion [applied to a film base] 
Categorization as to the means used to record notation, 
sound, or images in the production of a manifestation: 
 analogue 
 acoustic 
 electric 
 digital 
 optical 
ID Entity Attribute Definition 
LRM-E4-A2 MANIFESTATION Extent A quantification of the extent observed 
on a physical carrier of the 
manifestation and assumed to be 
observable on all other physical 
carriers of the manifestation as well 
 Scope notes The value of the extent attribute consists of three 
elements: 
- a type of extent (e.g., numbering of physical units, 
height, width, diameter, etc.), 
- a number, 
- and a measurement unit (e.g., volumes, pages, sheets, 
discs, reels, etc.; cm, inches, etc.; Mb/Megabytes; etc.). 
 
The type of extent and the measurement unit may be 
given implicitly. The level of precision used in 
recording the quantification of the extent may vary. 
 Examples  300 ## $a 301 p., [8] p. of plates [number of 
pages, recorded according to AACR2 and 
expressed in a MARC 21 subfield] 
 215 ## $a 1 score (vi, 63 p.) $d 20 cm $a 16 
parts $d 32 cm $e 1 booklet [number of pages, 
and their height; number of parts, and their 
height; and number of accompanying material 
elements, expressed in various subfields of a 
UNIMARC field] 
 4 3/4 in. [diameter, expressed in natural 
language, in English] 
ID Entity Attribute Definition 
LRM-E4-A3 MANIFESTATION 
 
 
 
Intended 
audience 
A class of users for which the physical 
carriers of the manifestation are 
intended 

IFLA LRM (2017-12) 
 
 49 
Table 4.4    Attributes 
 Scope notes The intended audience attribute can characterize a 
given manifestation by indicating groups of end-users 
for which manifestations with those features are 
deemed particularly appropriate: 
- categorization as to sensory impairment (visual 
impairment, hearing impairment, etc.), 
- categorization as to specialized carriers for specific 
audiences (young children, etc.), 
- etc. 
 Examples Categorization as to sensory impairment: 
 users able to read regular print 
 users needing large print 
 users needing easy-to-read fonts for dyslexics 
Categorization as to specific audiences: 
 board books for young children 
 bath books for young children 
ID Entity Attribute Definition 
LRM-E4-A4 MANIFESTATION Manifestation 
statement 
A statement appearing in exemplars of 
the manifestation and deemed to be 
significant for users to understand how 
the resource represents itself 
 Scope notes The manifestation statement attribute is a statement that 
is usually transcribed from a source or sources present 
in exemplars of a manifestation. Transcription 
conventions are codified by each implementation. 
 
A manifestation is likely to be characterized by 
multiple statements of different types. In most 
implementations, these statements would likely be 
typed at a level of granularity considered appropriate 
for user needs. For example, the manifestation 
statement attribute may include transcribed elements 
such as: publication statement (as a whole), or 
alternatively, place of publication statement + publisher 
name statement + date of publication statement (as 
three individual statements). 
 Examples  우리말의 수수께끼 : 역사 속으로 떠나는 
우리말 여행 / 박영준...[등]지음 [complete 
ISBD area 1] 
 Edinburgi : venundantur apud M. R. Freebairn, 
J. Paton et G. Brown, 1716 [complete 
publication statement] 
 Edinburgi [place of publication statement] 
 venundantur apud M. R. Freebairn, J. Paton et 

IFLA LRM (2017-12) 
 
 50 
Table 4.4    Attributes 
G. Brown [publisher name statement] 
 1716 [date of publication statement] 
 De l’imprimerie des aristocrates, chez Pluton, 
aux portes de l’Enfer : et se trouve chez la garde 
bréviaire de l’abbé Maury, Marie Margot, rue 
Troussevache [complete publication statement, 
including reference to a fictitious place of 
publication (“at Pluto’s, at the gates of Hell”), 
and lacking a date of publication statement] 
 4th revised ed. [edition statement, following 
ISBD transcription conventions] 
 4th revised edition [edition statement, following 
RDA transcription conventions] 
 (Miscellaneous report / Geological survey of 
Canada = Rapport divers / Commission 
géologique du Canada) [complete ISBD area 6] 
ID Entity Attribute Definition 
LRM-E4-A5 MANIFESTATION Access 
conditions 
Information as to how any of the 
carriers of the manifestation are likely 
to be obtained 
 Scope notes The access conditions attribute includes: 
- System requirements, 
- Mode of access, 
- etc. 
 Examples  538 ## ‡a System requirements: IBM 360 and 
370; 9K bytes of internal memory; OS SVS and 
OSMVS. [system requirements expressed in a 
MARC 21 field] 
 538 ## ‡a Blu-ray 3D: requires Blu-ray player; 
3D version requirements: full HD TV , 
compatible 3D glasses, Blu-ray 3D Player or 
PS3, and high speed HDMI cable. [system 
requirements for a video disc expressed in a 
MARC 21 field] 
 538 ## ‡a PSP (PlayStation portable); region 1; 
wi-fi compatible. [system requirements for a 
video game expressed in a MARC 21 field] 
ID Entity Attribute Definition 
LRM-E4-A6 MANIFESTATION Use rights A class of use and/or access restrictions 
to which all carriers of the 
manifestation are assumed to be 
submitted 
 Scope notes The use rights attribute includes: 
- Terms of availability, 

IFLA LRM (2017-12) 
 
 51 
Table 4.4    Attributes 
- Access restrictions, 
- etc. 
 
The use rights may be granted directly by the publisher, 
or be imposed by the publisher as transmitted via the 
library’s contracted rights or license agreement. This is 
often the case for rights associated with digital objects. 
 Examples  Freely available to members of the Club. [rights 
expressed in natural language, in English] 
 Restricted to institutions with a subscription. 
[rights expressed in natural language, in 
English] 
ID Entity Attribute Definition 
LRM-E5-A1 ITEM Location The collection and/or institution in 
which the item is held, stored, or made 
available for access 
 Scope notes This information can be specified at whatever level of 
precision is required in order to guide end-users in 
obtaining the item. 
 Examples  252 ## $a DLC $b Manuscript Division 
$c James Madison Memorial Building, 1st & 
Independence Ave., S.E., Washington, DC USA 
$f 4016 [location as expressed in a UNIMARC 
field] 
 852 01 $a ViBlbV $b Main Lib $b MRR $k Ref 
$h HF5531.A1 $i N4273 [location as expressed 
in a MARC 21 field] 
ID Entity Attribute Definition 
LRM-E5-A2 ITEM Use rights A class of use and/or access restrictions 
to which the item is submitted 
 Scope notes  
 Examples  Film restricted to classroom use. [rights 
expressed in natural language, in English] 
 In-library use only. [rights associated with a 
copy housed in a reference collection, expressed 
in natural language, in English] 
ID Entity Attribute Definition 
LRM-E6-A1 AGENT Contact 
information 
Information useful for communicating 
with or getting in contact with the 
agent 
 Scope notes 
 
 

IFLA LRM (2017-12) 
 
 52 
Table 4.4    Attributes 
 Examples  P.O. Box 95312, 2509 La Haye. Contact : 
31.70.3140884. Télécopie : 31.70.3834827. 
Adresse électronique : IFLA@ifla.org [contact 
information for the collective agent IFLA, 
expressed in natural language, in French] 
ID Entity Attribute Definition 
LRM-E6-A2 AGENT Field of 
activity 
A field of endeavour, area of expertise, 
etc., in which the agent is engaged or 
was engaged 
 Scope notes  
 Examples  780 [field of activity, music, expressed as a 
Dewey classification number] 
 journalisme [field of activity, journalism, 
expressed as a RAMEAU term] 
 art history [field of activity expressed as a Getty 
Art and Architecture Thesaurus (AAT) term] 
ID Entity Attribute Definition 
LRM-E6-A3 AGENT Language A language used by the agent when 
creating an expression 
 Scope notes A given agent can use more than one language, 
simultaneously or over time. 
 
The type of use of a given language can be specified 
(e.g., use of the English language for the creation of 
original content, use of the English language as source 
language of translations, etc.). 
 Examples  041 ## $a eng $a fre […] [languages English 
and French used by Samuel Beckett for the 
creation of original content, expressed as codes 
in INTERMARC subfields] 
 041 ## […] $t eng $t fre [languages English 
and French used by Samuel Beckett as source 
languages of translation, expressed as codes in 
INTERMARC subfields] 
 http://id.loc.gov/vocabulary/iso639-1/zu 
[language Zulu expressed as a URI] 
ID Entity Attribute Definition 
LRM-E7-A1 PERSON Profession / 
Occupation 
A profession or occupation in which 
the person works or worked 
 Scope notes  
 Examples  librarian [a profession expressed in natural 
language, in English] 

IFLA LRM (2017-12) 
 
 53 
Table 4.4    Attributes 
 COLLECTIVE 
AGENT 
No attributes restricted to this entity, see agent for 
relevant attributes 
ID Entity Attribute Definition 
LRM-E9-A1 NOMEN Category A type to which the nomen belongs 
 Scope notes Nomens may be categorized in terms of: 
- the type of thing named (personal name, work title, 
etc.), 
- the source in which the nomen is attested (spine title, 
running title), 
- the function of the nomen (identifier, controlled 
access point, classification notation, etc.). 
 Examples  http://id.loc.gov/vocabulary/identifiers/isbn-a 
[category (more specifically, a kind of 
identifier), expressed as a URI] 
 controlled access point [category, expressed in 
natural language, in English] 
 personal name [category, expressed in natural 
language, in English] 
 spine title [category, expressed in natural 
language, in English] 
 running title [category, expressed in natural 
language, in English] 
 key title [category (more specifically, a kind of 
identifier), expressed in natural language, in 
English] 
 pseudonym [category, expressed in natural 
language, in English] 
 married name [category, expressed in natural 
language, in English] 
ID Entity Attribute Definition 
LRM-E9-A2 NOMEN Nomen string The combination of signs that forms an 
appellation associated with an entity 
through the nomen 
 Scope notes The string involved in a nomen can be expressed as a 
notation in any form, such as a combination of signs 
within a writing system, chemical structure symbols, 
mathematical notation, or by any other kind of sign, 
such as sounds, etc. 
 
A nomen is more than the mere string of signs that 
constitutes the appellation associated with a thing 
through the nomen. Without any contextualization, the 
value of the nomen string attribute is a mere literal, 
potentially attached to anything in the world, as 

IFLA LRM (2017-12) 
 
 54 
Table 4.4    Attributes 
opposed to the nomen itself, which as a result of the 
appellation relationship is attached to one and only one 
instance of res. For example, the nomen 'John Smith' is 
the appellation of one and only one John Smith in the 
world, while the value of the nomen string attribute that 
reads "John Smith" in the Latin alphabet is the same for 
all the different things in the world that happen to be 
named 'John Smith'. 
(See also the Scope Notes for the appellation 
relationship, LRM-R13.) 
  Examples  the string of Latin alphabetic characters 
"Agatha Christie" [which may appear in a 
context where it serves to refer to the person 
{Agatha Christie}] 
 the string of Latin alphabetic characters "The 
postman always rings twice" [which may 
appear, for instance, in a context where it serves 
to refer to a novel by James M. Cain] 
 the string of Latin alphabetic characters "IFLA" 
[which may appear in a context where it serves 
to refer to the collective agent {International 
Federation of Library Associations and 
Institutions}, but may also appear as the value 
of the nomen string attribute for a distinct 
nomen that refers to another collective agent, 
the {International Federation of Landscape 
Architects}] 
 the string of Latin alphabetic characters 
"poison", which as a mere string has no 
language, and which constitutes both the value 
of the nomen string attribute for the English 
nomen 'poison', and the value of the nomen 
string attribute for the French nomen 'poison' 
 the string of alphabetic characters "Gift", which 
as a mere string has no language, and which 
constitutes both the value of the nomen string 
attribute for the English nomen 'Gift' attached to 
the concept {gift}, and the value of the nomen 
string attribute for the German nomen 'Gift' 
attached to the concept {poison} 
 the string of articulated sounds recorded on the 
web page 
<http://dictionary.cambridge.org/pronunciation/
english/hamlet> for the word 'hamlet' (a 
common noun) in British pronunciation 
 the string of articulated sounds recorded on both 
the web page 

IFLA LRM (2017-12) 
 
 55 
Table 4.4    Attributes 
<http://dictionary.cambridge.org/pronunciation/
english/serial> for the word 'serial' in British 
pronunciation, and the web page 
<http://dictionary.cambridge.org/pronunciation/
english/cereal> for the word 'cereal' in British 
pronunciation 
 the string of digits "20150601", which 
constitutes the value of the nomen string 
attribute of at least two distinct nomens: a 
normalized date (a nomen for a time-span), and 
an ISSN (without of its central hyphen) (a 
nomen for a work) 
 the string of digits "300", which constitutes the 
value of the nomen string attribute of at least 
five distinct nomens: a non-normalized date 
(nomen for a time-span), a title (nomen for a 
work), a Dewey Decimal Classification number 
(nomen for a res), a hotel room number (nomen 
for a res), a MARC 21 field code (nomen for a 
res) 
ID Entity Attribute Definition 
LRM-E9-A3 NOMEN Scheme The scheme in which the nomen is 
established 
 Scope notes The scheme attribute includes: 
- value encoding schemes (subject heading lists, 
thesauri, classification systems, name authority lists, 
etc.) 
- and syntax encoding schemes (standards for encoding 
dates, etc.). 
 
When the same value of one of the other nomen 
attributes (such as intended audience, language, script) 
is applicable to all the nomens in a particular scheme, 
the value can be implemented at the scheme level. 
 Examples 
 
 
 
 
 
 
 
 
 
 
 
 http://id.loc.gov/authorities/performanceMediu
ms [value encoding scheme for medium of 
performance expressed as a URI] 
 http://id.loc.gov/authorities/classification [value 
encoding scheme for the Library of Congress 
Classification expressed as a URI] 
 ISO 8601 [syntax encoding scheme for dates 
and times] 

IFLA LRM (2017-12) 
 
 56 
Table 4.4    Attributes 
ID Entity Attribute Definition 
LRM-E9-A4 NOMEN Intended 
audience 
A class of users for which the nomen is 
considered appropriate or preferred 
 Scope notes Indicating the intended audience for a nomen can serve 
as a basis for a mechanism that selects a nomen from a 
cluster of equivalent nomens, for use in a particular 
context. For example, an international multi-lingual 
authority file can indicate the intended audience for 
each nomen by recording the language in which the 
nomen is a preferred form. 
 Examples  sj [intended audience of children, expressed as a 
code used as a prefix in all Library of Congress 
children’s subject headings] 
 chi [intended audience of Chinese speakers, 
expressed as a MARC 21 language code] 
ID Entity Attribute Definition 
LRM-E9-A5 NOMEN Context of use Information as to the context(s) in 
which a nomen is used by the agent 
who is referred to through it 
 Scope notes The context of use attribute includes domains 
associated with a nomen used by an agent. 
 Examples  literary works [context of use expressed in 
natural language, in English] 
 critical works [context of use expressed in 
natural language, in English] 
 works on mathematics [context of use expressed 
in natural language, in English] 
 detective novels [context of use expressed in 
natural language, in English] 
ID Entity Attribute Definition 
LRM-E9-A6 NOMEN Reference 
source 
A source in which there is evidence for 
the use of the nomen 
 Scope notes 
 
 
 
 
 
 
 
 
 
 
A reference source attests to the existence of a linkage 
between a designation and the instance of the entity res 
that it serves to identify. It may clarify the validity and 
scope of the nomen. 
 
A reference source attribute value may refer to: 
- biographical dictionaries, encyclopedias, etc., 
- other schemes, 
- any publications, 
- etc. 

IFLA LRM (2017-12) 
 
 57 
Table 4.4    Attributes 
 Examples  670 ## |a Adamson, J. Groucho, Harpo, Chico, 
and sometimes Zeppo, [1973] [reference source 
expressed in a MARC 21 field; the reference 
source is a publication about the collective 
agent identified through the nomen 'Marx 
Brothers'] 
 670 ## |a nuc89-22212: Her RLIN II processing 
for UC online catalog input, 1984 |b (hdg. on 
WU rept.: Coyle, Karen; usage: Karen Coyle) 
[reference source expressed in a MARC 21 
field; the reference source is a publication by 
the person identified through the nomen 'Coyle, 
Karen'] 
 810 ## $a Les clowns et la tradition clownesque 
/ P. R. Lévy, 1991 [reference source expressed 
in a UNIMARC field; the reference source is a 
publication about the res identified by the 
nomen 'Clowns'] 
 810 ## $a Oxford dictionary of national 
biography [reference source expressed in a 
UNIMARC field; the reference source is a 
biographical dictionary] 
 810 ## $a LCSH, 1988-03 [reference source 
expressed in a UNIMARC field; the reference 
source is another scheme, distinct from the 
scheme in which the nomen appears] 
ID Entity Attribute Definition 
LRM-E9-A7 NOMEN Language The language in which the nomen is 
attested 
 Scope notes The language attribute may be viewed as recording a 
scheme of a particular type (that is, a natural human 
language) in which a nomen may be considered valid. 
Viewed in this way, the language attribute may be 
implemented as a sub-type of the scheme attribute. 
 Examples  http://id.loc.gov/vocabulary/iso639-1/zu 
[language Zulu expressed as a URI] 
ID Entity Attribute Definition 
LRM-E9-A8 NOMEN Script The script in which the nomen is 
notated 
 Scope notes The script attribute allows the identification of the 
writing system used to provide a notation for the 
nomen. The writing system consists of the full range of 
the conventions used. Writing systems may be 
alphabetic, syllabic, ideographic, etc., or some 
combination of these. 

IFLA LRM (2017-12) 
 
 58 
Table 4.4    Attributes 
 
The script does not, however, include aspects such as 
the choice of font or other incidental display 
characteristics (for example, point size, colour) which 
do not encode any features which result in differences 
in the interpretation of the written symbols. 
 Examples  Tibetan [script expressed in natural language, in 
English] 
 Tibt [script expressed as a code in the ISO 
15924 standard] 
 t [script expressed as a code used in 
INTERMARC format] 
ID Entity Attribute Definition 
LRM-E9-A9 NOMEN Script 
conversion 
The rule, system, or standard that was 
used to create a nomen that is derived 
on the basis of another, distinct nomen 
notated in another, distinct script 
 Scope notes A script conversion attribute value may refer to: 
- transliterations,  
- script conversions that cannot be reversed,  
- etc. 
 Examples  ISO 9 [script conversion from Cyrillic alphabet 
to Latin alphabet] 
 Wade-Giles [script conversion from Chinese 
script to Latin alphabet] 
ID Entity Attribute Definition 
LRM-E10-A1 PLACE Category A type to which the place belongs 
 Scope notes  
 Examples  town [category expressed in natural language, 
in English] 
 country [category expressed in natural 
language, in English] 
 continent [category expressed in natural 
language, in English] 
ID Entity Attribute Definition 
LRM-E10-A2 PLACE Location A delimitation of the physical territory 
of the place 
 Scope notes The level of precision used can vary according to the 
context. 
 Examples  123 ## $d E1444300 $e E1482200 $f S0403900 
$g S0433900 [location expressed as codes in a 
UNIMARC field] 

IFLA LRM (2017-12) 
 
 59 
Table 4.4    Attributes 
ID Entity Attribute Definition 
LRM-E11-A1 TIME-SPAN Beginning A value for the time at which the time-
span started, expressed in a precise 
way in an authoritative external system 
to allow temporal positioning of events 
 Scope notes The level of precision used can vary according to the 
context. 
 Examples  19850412T101530 [beginning expressed 
according to the ISO 8601 standard] 
 488.3 million years before present [beginning of 
the Ordovician period, a geological period] 
ID Entity Attribute Definition 
LRM-E11-A2 TIME-SPAN Ending A value for the time at which the time-
span ended, expressed in a precise way 
in an authoritative external system to 
allow temporal positioning of events 
 Scope notes The level of precision used can vary according to the 
context. 
 Examples  19860513T112536 [ending expressed according 
to the ISO 8601 standard] 
 443.7 million years before present [ending of 
the Ordovician period, a geological period] 
 
 
4.2.5 Index to Attributes 
Table 4.5 below is an index to the attributes defined in Table 4.4 (Attributes) in section 4.2.4. In 
Table 4.5 the attributes are sorted alphabetically by the name of the attribute. In the cases where 
the same name appears for attributes of different entities, the secondary sort is by the entity ID. 
 
Table 4.5 Index by Attribute Name 
Attribute Name Attribute ID Entity ID Entity 
Access conditions LRM-E4-A5 LRM-E4 Manifestation 
Beginning LRM-E11-A1 LRM-E11 Time-span 
Cartographic scale LRM-E3-A5 LRM-E3 Expression 
Category LRM-E1-A1 LRM-E1 Res 
Category LRM-E2-A1 LRM-E2 Work 
Category LRM-E3-A1 LRM-E3 Expression 
Category LRM-E9-A1 LRM-E9 Nomen 
Category LRM-E10-A1 LRM-E10 Place 

IFLA LRM (2017-12) 
 
 60 
Table 4.5 Index by Attribute Name 
Attribute Name Attribute ID Entity ID Entity 
Category of carrier LRM-E4-A1 LRM-E4 Manifestation 
Contact information LRM-E6-A1 LRM-E6 Agent 
Context of use LRM-E9-A5 LRM-E9 Nomen 
Ending LRM-E11-A2 LRM-E11 Time-span 
Extent LRM-E3-A2 LRM-E3 Expression 
Extent LRM-E4-A2 LRM-E4 Manifestation 
Field of activity LRM-E6-A2 LRM-E6 Agent 
Intended audience LRM-E3-A3 LRM-E3 Expression 
Intended audience LRM-E4-A3 LRM-E4 Manifestation 
Intended audience LRM-E9-A4 LRM-E9 Nomen 
Key LRM-E3-A7 LRM-E3 Expression 
Language LRM-E3-A6 LRM-E3 Expression 
Language LRM-E6-A3 LRM-E6 Agent 
Language LRM-E9-A7 LRM-E9 Nomen 
Location LRM-E5-A1 LRM-E5 Item 
Location LRM-E10-A2 LRM-E10 Place 
Manifestation statement LRM-E4-A4 LRM-E4 Manifestation 
Medium of performance LRM-E3-A8 LRM-E3 Expression 
Nomen string LRM-E9-A2 LRM-E9 Nomen 
Note LRM-E1-A2 LRM-E1 Res 
Profession / Occupation LRM-E7-A1 LRM-E7 Person 
Reference source LRM-E9-A6 LRM-E9 Nomen 
Representative expression attribute LRM-E2-A2 LRM-E2 Work 
Scheme LRM-E9-A3 LRM-E9 Nomen 
Script LRM-E9-A8 LRM-E9 Nomen 
Script conversion LRM-E9-A9 LRM-E9 Nomen 
Use rights LRM-E3-A4 LRM-E3 Expression 
Use rights LRM-E4-A6 LRM-E4 Manifestation 
Use rights LRM-E5-A2 LRM-E5 Item 
 
 
  

IFLA LRM (2017-12) 
 
 61 
4.3 Relationships 
4.3.1 Introduction 
Relationships are an essential part of the bibliographic universe: they connect instances of 
entities and provide context for them. In the IFLA LRM model, the relationships are declared in 
a general, abstract way and thus enable implementers to include additional details in a consistent 
and coherent way by introducing additional refinements. 
 
The first relationship in Table 4.7 in section 4.3.3 (res ‘is associated with’ res) is the top-level, 
general relationship. All other relationships declared in the model are specific refinements of this 
relationship which add to the semantic content of the specific association between particular 
domain and range entities, and specify stricter constraints where this is meaningful. Any 
additional relationships needed by a particular implementation can be defined as refinements of 
the additional relationships defined in the model, or of the top relationship. In the context of a 
subject thesaurus, the specific thesaural relationships between res that serve as subjects would be 
defined as refinements of the top relationship. 
 
The relationships between works, expressions, manifestations, and items are the core of the model. 
Implementing other relationships is encouraged, since they enable exploration and discovery and 
are very important for end-users. 
 
The relationships declared in the model can serve as building blocks for “compound” or multi-
step relationships. Traversing two or more relationships is referred to as a “path”. For example, 
the link between a work and a term used to represent its subject is provided by a two-step path 
which also accounts for the role of the entity res. 
 (LRM-R12) WORK ‘has as subject’ RES + 
 (LRM-R13) RES ‘has appellation’ NOMEN 
 
When a particular path is frequently required in a particular application, it can be implemented as 
a single relationship which serves as a shortcut for the more developed path. The intermediate 
node(s) or entities become implicit. One shortcut is sufficiently important that it is declared in 
the model: 
 (LRM-R15) NOMEN ‘is equivalent to’ NOMEN 
is the same as the following pair of relationships: 
 (LRM-R13i) NOMEN1 ‘is appellation of’ RES + 
 (LRM-R13) RES ‘has appellation’ NOMEN2 
 
The entity subclass/superclass structure (the “isA” hierarchy) can also be used in a path to 
restrict the domain or range entities in a relationship. The pair of statements: 
 (isA)  PERSON isA AGENT + 
 (LRM-R5i) AGENT ‘created’ WORK 
imply the shortcut relationship: 
   PERSON ‘created’ WORK 
This latter specific relationship can be implemented directly if it is considered desirable. 
 
Multi-step paths can make use of both the “isA” hierarchy and the relationships declared in the 
model. This is the case in the path linking a work to a nomen associated by one agent (such as a 
bibliographic agency) with the agent responsible for creating the work. 
 
 

IFLA LRM (2017-12) 
 
 62 
 (LRM-R5) WORK ‘was created by’ AGENT1 + 
 (isA)  AGENT1 isA RES + 
 (LRM-R13) RES ‘has appellation’ NOMEN + 
 (LRM-R14i) NOMEN ‘was assigned by’ AGENT2 
 
The relationships are declared on the entity level. It is important to note that while relationships 
are declared between entities, in reality they are established and exist between instances. 
 
Only the entities declared in section 4.1.3 serve as domains or ranges of relationships defined in 
the model. The entity person does not appear explicitly in any of the relationships defined. All 
refinements of relationships that require the entity person are created using the entity hierarchy 
mechanism described above. 
 
 
4.3.2 Hierarchy Structure for Relationships 
Table 4.6 below summarizes in a concise tabular form the relationships defined in the model. 
Following the entity hierarchy structure (shown in full in Table 4.1 in section 4.1.2), relationships 
may also feature hierarchy. All relationships are refinements of the top-level relationship 
(LRM-R1), which is given in the first row of the first column. All the other relationships defined 
in the model are at the same level and are given in the second column. In an expansion of the 
model, additional second level relationships, as well as relationships at still lower hierarchy levels, 
may be defined. To make the listing more compact, only the relationship names are given, the 
inverse names are omitted. The inverse names and full definitions of all the relationships are 
given in Table 4.7 (Relationships) in section 4.3.3. 
 
 

IFLA LRM (2017-12) 
 
 63 
Table 4.6 Relationship Hierarchy 
Top Level Second Level 
LRM-R1  RES is associated with RES  
-- LRM-R2 WORK is realized through EXPRESSION 
-- LRM-R3 EXPRESSION is embodied in MANIFESTA TION 
-- LRM-R4 MANIFESTATION is exemplified by ITEM 
-- LRM-R5 WORK was created by AGENT 
-- LRM-R6 EXPRESSION was created by AGENT 
-- LRM-R7 MANIFESTATION was created by AGENT 
-- LRM-R8 MANIFESTATION was manufactured by AGENT 
-- LRM-R9 MANIFESTATION is distributed by AGENT 
-- LRM-R10 ITEM is owned by AGENT 
-- LRM-R11 ITEM was modified by AGENT 
-- LRM-R12 WORK has as subject RES 
-- LRM-R13 RES has appellation NOMEN 
-- LRM-R14 AGENT assigned NOMEN 
-- LRM-R15 NOMEN is equivalent to NOMEN 
-- LRM-R16 NOMEN has part NOMEN 
-- LRM-R17 NOMEN is derivation of NOMEN 
-- LRM-R18 WORK has part WORK 
-- LRM-R19 WORK precedes WORK 
-- LRM-R20 WORK accompanies / complements WORK 
-- LRM-R21 WORK is inspiration for WORK 
-- LRM-R22 WORK is a transformation of WORK 
-- LRM-R23 EXPRESSION has part EXPRESSION 
-- LRM-R24 EXPRESSION is derivation of EXPRESSION 
-- LRM-R25 EXPRESSION was aggregated by EXPRESSION 
-- LRM-R26 MANIFESTATION has part MANIFESTATION 
-- LRM-R27 MANIFESTATION has reproduction MANIFESTATION 
-- LRM-R28 ITEM has reproduction MANIFESTATION 
-- LRM-R29 MANIFESTATION has alternate MANIFESTA TION 
-- LRM-R30 AGENT is member of COLLECTIVE AGENT 
-- LRM-R31 COLLECTIVE AGENT has part COLLECTIVE AGENT 
-- LRM-R32 COLLECTIVE AGENT precedes COLLECTIVE AGENT 
-- LRM-R33 RES has association with PLACE 
-- LRM-R34 PLACE has part PLACE 
-- LRM-R35 RES has association with TIME-SPAN 
-- LRM-R36 TIME-SPAN has part TIME-SPAN 
  

IFLA LRM (2017-12) 
 
 64 
4.3.3 Relationships Detailed Definition 
Each relationship declared in the model is described in Table 4.7 below. Relationships are 
numbered sequentially from LRM-R1 to LRM-R36. Inverse (reciprocal) relationships can be 
referred to by the number of the relationship plus the suffix “i”. 
 
For each relationship, the columns of the first row in the table present, after the number, the 
domain (source) entity for the relationship, the name of the relationship, the name of the inverse 
(or reciprocal) relationship, the range (target) entity for the relationship, and the cardinality. The 
definition of the relationship, any scope notes, and a selection of examples of instances of that 
relationship are presented in subsequent table rows. 
 
In the inverse relationships the entity from the Range column serves as the domain, the entity 
from the Domain column serves as the range, and the inverse name of the relationship is used. 
For example, the relationships represented by the second entry of the table should be read as: 
 (LRM-R2) WORK ‘is realized through’ EXPRESSION 
 (LRM-R2i) EXPRESSION ‘realizes’ WORK   (inverse reading) 
 
Relationships are recursive when the same entity serves as both domain and range, and are 
called symmetric when the relationship name is the same as the inverse name. In addition to the 
top relationship (res ‘is associated with’ res), the nomen-equivalence (nomen ‘is equivalent to’ 
nomen) and the manifestation-alternate (manifestation ‘has alternate’ manifestation) relationships are 
both recursive and symmetric. The ‘has part/is part of’ relationships are an example of 
relationships that are recursive without also being symmetric. 
 
Relationships that express states or ongoing activities are named in the present tense (such as ‘is 
associated with’, ‘is member of’, ‘is subject of’), while relationships that express actions that were 
logically completed in the past are named in the past tense (such as ‘was created by’, ‘created’, 
‘was assigned by’). 
 
Cardinality specifies the number of instances of the domain and range entities that may be 
connected by the specific relationship. The cardinality 1 to M (M meaning many) for the ‘is 
realized through’ relationship, for example, means that each work has one or more expressions that 
realize it and that each expression realizes exactly one work. Similarly, in the ‘is exemplified by’ 
relationship, each item is an exemplar of a single manifestation, while each manifestation is 
exemplified by one or more items. The cardinality M to M for the work ‘was created by’ agent 
relationship, for example, means that any agent may create many works and a work may be the 
result of creative contributions from several agents. 
 
 
Table 4.7 Relationships 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R1 Res is associated with is associated 
with 
Res M to M 
 Definition This relationship links two res that have an association of any kind 
 Scope notes This is a general relationship valid for all entities in the bibliographic 
universe. In general, specific refinements would be defined to carry 
more precise semantics. 

IFLA LRM (2017-12) 
 
 65 
Table 4.7 Relationships 
 Examples  Topic to topic, e.g.: {Quantum theory} is associated with 
{Thermodynamics} 
 Work to work, e.g.: the work titled Through the Looking-Glass 
and What Alice Found There is associated with the work titled 
Alice’s Adventures in Wonderland 
 Topic to work, e.g.: the character Alice is associated with the 
work titled Alice’s Adventures in Wonderland 
 Person to collective agent, e.g.: Nathaniel Hawthorne is 
associated with the Phi Beta Kappa Society 
 Person to time-span, e.g.: Emily Dickinson is associated with 
the time-span from 1830 (the year she was born) to 1886 (the 
year she died) 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R2 Work is realized through realizes Expression 1 to M 
 Definition This relationship links a work with any of the expressions which convey 
the same intellectual or artistic content 
 Scope notes The logical connection between work and expression, as reflected in the 
model through this relationship, serves as the basis both for identifying 
the work represented by an individual expression and for ensuring that 
all expressions of a work are linked to the work. Indirectly the 
relationships between a work and the various expressions of that work 
also serve to establish a “sibling” relationship between the various 
expressions of the work. 
 Examples  The work known as Eine kleine Nachtmusik is realized through 
the musical notation found in the editions of Eine kleine 
Nachtmusik from 1989 by Bärenreiter, ISBN 3-370-00301-5, 
and by VEB Deutscher Verlag für Musik, ISBN 3-370-00301-5, 
and in the undated edition by Breitkopf & Härtel, plate number 
4956 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R3 Expression is embodied in embodies Manifestation M to M 
 Definition This relationship links an expression with a manifestation in which the 
expression appears 
 Scope notes A manifestation may embody one or more expressions and any 
expression may be embodied in one or more manifestations. This logical 
connection serves as the basis both for identifying the specific 
expression or expressions of a work or works embodied in an individual 
manifestation and for ensuring that all manifestations of the same 
expression are linked back to that expression.  
 Examples 
 
 
 
 
 
 
 The musical notation of Hans Günter Heumann’s piano 
arrangement of Mozart’s Eine kleine Nachtmusik is embodied in 
the 1996 publication by Henry Lemoine identified by plate 
number 26336HL 

IFLA LRM (2017-12) 
 
 66 
Table 4.7 Relationships 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R4 Manifestation is exemplified by exemplifies Item 1 to M 
 Definition This relationship connects a manifestation with any item that reflects the 
characteristics of that manifestation 
 Scope notes The logical connection serves as the basis both for identifying the 
manifestation exemplified by an individual item and for ensuring that all 
items of the same manifestation are linked to that manifestation. 
Indirectly the relationships between a manifestation and the various 
items exemplifying that manifestation also serve to establish a “sibling” 
relationship between the various items of a manifestation. 
 Examples  The publication by Bärenreiter in 1989 containing a facsimile of 
Mozart’s autograph manuscript of the work known as Eine 
kleine Nachtmusik is exemplified by the exemplar held by the 
Music Department of the National Library of France, shelf 
number VMA-991(2,26) 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R5 Work was created by created Agent M to M 
 Definition This relationship links a work to an agent responsible for the creation of 
the intellectual or artistic content 
 Scope notes The logical connection between a work and a related agent serves as the 
basis both for identifying an agent responsible for an individual work 
and for ensuring that all works by a particular agent are linked to that 
agent. 
 Examples  The literary work known as Hamlet was created by William 
Shakespeare 
 The musical work known as Eine kleine Nachtmusik was created 
by Wolfgang Amadeus Mozart 
 The musical work known as Communication breakdown was 
created by Page, Jones and Bonham (members of the musical 
group Led Zeppelin) 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R6 Expression  was created by created Agent M to M 
 Definition This relationship links an expression to an agent responsible for the 
realization of a work 
 Scope notes This relationship applies both to the creation of the original expression 
and any subsequent modifications such as translations, revisions and 
performances. An agent responsible for the intellectual or artistic content 
of a work is responsible for the conception of the work as an abstract 
entity; an agent responsible for the expression of the work is responsible 
for the specifics of the intellectual or artistic realization or execution of 
the expression. The logical connection between an expression and a 
related agent serves as the basis both for identifying an agent 
responsible for an individual expression and for ensuring that all 
expressions realized by an agent are linked to that agent. 

IFLA LRM (2017-12) 
 
 67 
Table 4.7 Relationships 
 Examples  Majda Stanovnik created the Slovenian text titled Medved Pu, 
which is a Slovenian translation of A. A. Milne’s Winnie the 
Pooh 
 The Helsinki Philharmonic Orchestra, conducted by Okko 
Kamu, created the performed expression of Jean Sibelius’s 
Finlandia Op. 26 issued on a recording identified by ISRC 
FIFIN8800300 
 Matthew Cameron created the musical notation of the piano 
arrangement of Mozart’s Eine kleine Nachtmusik which was 
originally published in 2006 and first performed by Cyprien 
Katsaris 
 The musical group Led Zeppelin created the performed 
expression of the musical work known as Communication 
breakdown released in 1969 on their self-titled album Led 
Zeppelin on the Atlantic label, catalogue number 588171 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R7 Manifestation was created by created Agent M to M 
 Definition This relationship links a manifestation to an agent responsible for 
creating the manifestation 
 Scope notes For a manifestation, the notion of creation broadly includes the 
publication process for published manifestations. The logical connection 
between a manifestation and a related agent serves as the basis both for 
identifying an agent responsible for creating a manifestation and for 
ensuring that all manifestations created by an agent are linked to that 
agent. 
 Examples  Brill created the 2014 publication of Muḥsin Mahdī’s critical 
edition of the literary work known as The thousand and one 
nights 
 The monastery of Lindisfarne created the overall content and 
layout of the Lindisfarne Gospels 
 Streamline Records created the publication of Lady Gaga’s 
sound recording titled Poker face: remixes, UPC 602517965393 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R8 Manifestation was manufactured 
by 
manufactured Agent M to M 
 Definition This relationship links a manifestation to an agent responsible for the 
fabrication, production or manufacture of the items of that manifestation 
 Scope notes The manifestation may be manufactured or produced through industrial 
processes or through artisanal methods. 
 Examples 
 
 
 
 
 
 
 The 2013 publication by the Historical Society of Western 
Pennsylvania titled The Civil War in Pennsylvania was 
manufactured by the printing company named Heeter 
(Canonsburg, Pa.) 
 The monastery of Lindisfarne manufactured the manuscript 
known as the Lindisfarne Gospels 

IFLA LRM (2017-12) 
 
 68 
Table 4.7 Relationships 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R9 Manifestation is distributed by distributes Agent M to M 
 Definition This relationship links a manifestation to an agent responsible for 
making items of that manifestation available 
 Scope notes The items can be made available through the traditional distribution 
processes for physical items, or by making electronic items available for 
download, streaming, etc. 
 Examples  The 2001 publication of Cai Hua’s A Society without Fathers or 
Husbands: the Na of China, published by Zone Books (New 
York), is distributed by the MIT Press (Cambridge, Mass.) 
 The Canadian Broadcasting Corporation (CBC) distributes the 
episodes of the radio show Podcast playlist by making the files 
available for downloading at 
http://www.cbc.ca/radio/podcasts/podcast-playlist/ or for 
streaming at http://www.cbc.ca/radio/podcastplaylist 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R10 Item is owned by owns Agent M to M 
 Definition This relationship links an item to an agent that is or was the owner or 
custodian of that item 
 Scope notes The logical connection between an item and a related agent could serve 
as the basis both for identifying an agent that owned or had 
custodianship of an item and for ensuring that all items owned by, or in 
the custodianship of, a particular agent are linked to that agent. 
 Examples  The exemplar with shelf number VMA-991(2,26) of the 
publication by Bärenreiter in 1989 containing a facsimile of 
Mozart’s autograph manuscript of the work known as Eine 
kleine Nachtmusik is owned by the Music Department of the 
National Library of France 
 The exemplar VM2-457 of the publication by Le Clerc in 1765 
of Jean-Jacques Rousseau’s Le devin du village is owned by 
Marie-Antoinette 
 The National Library of France owns the digital item of the 
ebook Pop Culture by Richard Memeteau, published by Zones 
in 2014 and distributed by Editis in EPUB2 format, 
ISBN 978-2-35522-085-2, received through digital legal deposit 
on 1st February 2016 to which the legal deposit number 
DLN-20160201-6 has been assigned. In the catalogue, this item 
is identified with a unique number: LNUM20553886 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R11 Item was modified by modified Agent M to M 
 Definition This relationship links an item to an agent that made changes to this 
particular item without creating a new manifestation 
 Scope notes 
 
 
Examples include adding annotations, adding an ex-libris, removing 
pages, rebinding, restoration. 

IFLA LRM (2017-12) 
 
 69 
Table 4.7 Relationships 
 Examples  The autograph manuscript of Jean-Paul Sartre’s La nausée was 
modified by bookbinder Monique Mathieu 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R12 Work has as subject is subject of Res M to M 
 Definition This relationship links a work to its topic(s) 
 Scope notes The logical connection between a work and a related subject entity 
serves as the basis both for identifying the subject of an individual work 
and for ensuring that all works relevant to a given subject are linked to 
that subject. 
 Examples  {black holes} is subject of Stephen Hawking’s A Brief history of 
time 
 Anne Hart’s The life and times of Miss Jane Marple has as 
subject {Miss Jane Marple, a character in numerous Agatha 
Christie novels and stories} [a work of literary criticism] 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R13 Res has appellation is appellation of Nomen 1 to M 
 Definition This relationship links an entity with a sign or combination of signs or 
symbols through which that entity is referred to within a given scheme 
or context 
 Scope notes The consequence of the definition of nomen as the association between 
something and a designation that refers to it, is that each nomen is 
uniquely associated with a single res within a given scheme (which can 
extend from a specific local system to a natural language, through a 
shared authority file). The resulting cardinality of the appellation 
relationship is that while a single res may have many nomens, each 
nomen is the appellation of a single res. The fact that two instances of 
nomen may have the same value for their nomen string attribute does not 
modify this cardinality, and does not imply that such instances of nomen 
are actually one and the same instance of nomen associated with more 
than one instance of res, even if the scheme in question is a natural 
language. The nomen string "Gift" may be used to refer either to a 
present or to a poison, according to whether it is the nomen string value 
for a nomen within the English language or for a nomen in the German 
language: although the string nomen values look the same, we do have 
here two distinct instances of nomen for two distinct instances of res. 
 
Although in theory, one instance of nomen (a subclass of res) could be 
associated to another instance of nomen via the appellation relationship 
(resulting in a nomen for another nomen), in practice the general case 
would not be provided for in implementations. Structurally, in a system 
implementation where instances of the entity nomen are assigned an 
internal identifier (also a nomen of a specific type) this relationship 
would be implicit in the system design. An example of this situation 
could be found in a linked data implementation which assigns a URI 
(nomen) to instances of nomen of other types. 
 Examples  {the author of one of the earliest known grammars of Sanskrit, 
known as Ashtadhyayi} has appellation 'Pāṇini' 

IFLA LRM (2017-12) 
 
 70 
Table 4.7 Relationships 
 {the concept of infinity} has appellation '∞' 
 {black holes} has appellation 'trous noirs' 
 {black holes} has appellation 'črne luknje' 
 {black holes} has appellation '黑洞' 
 {International Federation of Library Associations and 
Institutions} has appellation 'IFLA' [IFLA nomen1] 
 {International Federation of Landscape Architects} has 
appellation 'IFLA' [IFLA nomen2, a distinct instance of the 
entity nomen from IFLA nomen1] 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R14 Agent assigned was assigned by Nomen 1 to M 
 Definition This relationship links an agent with a particular nomen that was 
assigned by this agent 
 Scope notes In the bibliographic context, nomen assignment is applied to the creation 
of subject terms, controlled access points, identifiers, etc. 
 Examples  ISBN agency assigned '0-553-10953-7' to the 1998 publication 
of Stephen Hawking’s A Brief history of time 
 Call number 'QB981 .H377 1998' was assigned to the 1998 
publication of Stephen Hawking’s A Brief history of time by the 
Library of Congress 
 The term 'proton' was assigned by Ernest Rutherford to the 
hydrogen nucleus in 1920 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R15 Nomen is equivalent to is equivalent to Nomen M to M 
 Definition This is the relationship between two nomens which are appellations of 
the same res 
 Scope notes This is a shortcut of a fully developed path:  
NOMEN1 is appellation of RES + RES has appellation NOMEN2 
 
The nomens related by this relationship are functionally equivalent in 
meaning (assigned to the same res), but as they retain their own values 
in any attributes that are recorded for them, they are not interchangeable 
as far as usage is concerned. The equivalent nomens may differ as to 
crucial attributes such as scheme, language or context of use. 
 
This equivalence relationship relates instances of nomens, and not the 
values of the nomen string attributes for these nomens. Thus, even 
though it may seem counter-intuitive, two nomens that refer to different 
res, even if recorded with the same literal string, will not be equivalent. 
 Examples  'USA' is equivalent to 'United States of America' 
 'Анна Павловна (Матвеевна) Павлова' is equivalent to 'Anna 
Pavlovna (Matveyevna) Pavlova' 
 'Bill Clinton' is equivalent to 'William Jefferson Clinton' 
 'Norma Jeane Mortenson' is equivalent to 'Marilyn Monroe' [as 
nomens for the person] 
 'τὰ βιβλία' is equivalent to 'The Bible' 

IFLA LRM (2017-12) 
 
 71 
Table 4.7 Relationships 
 'Schubert, Franz, 1797-1828. Sonatas, piano, D. 959, A major' is 
equivalent to 'Schubert, Franz, 1797-1828. Sonates. Piano. 
D 959. La majeur' [the preferred heading according to RDA for 
an English language cataloguing agency represents the same 
musical work as the preferred heading established for a French 
language cataloguing agency] 
 'Santa Claus' is equivalent to 'Saint Nick' 
 'Music' is equivalent to '780' [the classification number '780' is a 
valid number in the Dewey Decimal Classification representing 
the same concept as the term 'Music' assigned in the Library of 
Congress Subject Headings] 
 'Christie, Agatha, 1890-1976' is equivalent to '0000 0001 2102 
2127' [ISNI for the public identity {Agatha Christie}, distinct 
from the public identity {Mary Westmacott}] 
 'International Federation of Library Associations and 
Institutions' is equivalent to 'IFLA' [IFLA nomen1] 
 'International Federation of Landscape Architects' is equivalent 
to 'IFLA' [IFLA nomen2, a distinct instance of the entity nomen 
from IFLA nomen1; IFLA nomen2 is not equivalent to IFLA 
nomen1] 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R16 Nomen has part is part of Nomen M to M 
 Definition This relationship indicates that one nomen is constructed using another 
nomen as a component 
 Scope notes The whole-part relationship for nomens is essential in handling the 
attributes of components of nomens constructed using pre-existing 
nomens, as such attributes as language may differ between the parts of a 
compound nomen. 
 Examples  'Shakespeare' is part of 'William Shakespeare' 
 'Measles' is part of 'Measles/epidemiology' 
 'Twelfth Night, or What You Will' has part 'Twelfth Night' 
 'Schubert, Franz, 1797-1828. Sonatas, piano, D. 959, A major' 
has part 'Schubert, Franz, 1797-1828' 
 'Italy. Ministero degli affari esteri' has part 'Italy' 
 '1830-1886' is part of 'Dickinson, Emily, 1830-1886' 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R17 Nomen is derivation of has derivation Nomen M to 1 
 Definition This relationship indicates that one nomen was used as the basis for 
another nomen, both of which are appellations of the same res 
 Scope notes A nomen may be derived from another due to formal modifications in 
the notation used (such as transliteration) or cultural or linguistic 
conventions (creation of abbreviated or shortened or variant forms). 
 Examples  'USA' is derivation of 'United States of America' 
 'Анна Павловна (Матвеевна) Павлова' has derivation 'Anna 
Pavlovna (Matveyevna) Pavlova' 
 'Bill Clinton' is derivation of 'William Jefferson Clinton' 

IFLA LRM (2017-12) 
 
 72 
Table 4.7 Relationships 
 'Schubert, Franz, 1797-1828. Sonatas, piano, D. 959, A major' is 
derivation of 'Sonata in la maggiore op. postuma, D. 959' 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R18 Work has part is part of Work M to M 
 Definition This is the relationship between two works, where the content of one is a 
component of the other 
 Scope notes This applies when the component-to-whole relationship is an inherent 
aspect of the works and holds for all the expressions and manifestations 
of the larger work and of its component works, whether the expression or 
manifestation comprises the full larger work or just one or more (but not 
all) of the component works. Examples include movements of concertos, 
poems within poetry cycles, multipart novels, triptychs. 
 Examples  A wizard of Earthsea is part of the Earthsea trilogy by Ursula K. 
Le Guin 
 Richard Wagner’s Der Ring des Nibelungen has part Richard 
Wagner’s Götterdämmerung 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R19 Work  precedes succeeds Work M to M 
 Definition This is the relationship of two works where the content of the second is a 
logical continuation of the first 
 Scope notes The relationship is about a sequence of ideas and should not be confused 
with the time of creation of the respective works. 
 
As this relationship concerns the logical continuation of the content of 
the respective works, it does not apply to those serial works that 
transform over time (via major title changes, changes in media type, 
etc.) yet maintain a continuity in their form or numbering schemes. See 
the work-transformation relationship, LRM-R22, to express the 
relationship between one aggregating or serial work and another that 
modifies and continues it. 
 Examples  Margaret Mitchell’s Gone With the Wind precedes both 
Alexandra Ripley’s Scarlett and Donald McCaig’s Rhett 
Butler’s People 
 Margaret Mitchell’s Gone With the Wind succeeds Donald 
McCaig’s Ruth’s Journey 
 The TV series Better Call Saul! precedes the TV series Breaking 
Bad 
 A wizard of Earthsea precedes The tombs of Atuan, which 
precedes The farthest shore, all in the Earthsea trilogy by Ursula 
K. Le Guin 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R20 Work 
 
 
 
accompanies / 
complements 
is accompanied 
/ complemented 
by 
Work M to M 

IFLA LRM (2017-12) 
 
 73 
Table 4.7 Relationships 
 Definition This is the relationship between two works which are independent, but 
can also be used in conjunction with each other as complements or 
companions 
 Scope notes The two works may be adding value to each other (in this case the 
relationship is symmetrical); in other cases one of the works is 
considered secondary. 
 Examples  Leigh Lowe’s Prima Latina: an introduction to Christian Latin. 
Teacher manual accompanies / complements Leigh Lowe’s 
Prima Latina: an introduction to Christian Latin. Student book 
 Eric Gill’s set of illustrations for the Song of Songs accompanies 
/ complements the Song of Songs in the 1931 publication by the 
Cranach Press 
 Wole Soyinka’s foreword to the Universal declaration of human 
rights accompanies / complements the Universal declaration of 
human rights in the 1994 publication by African Book Builders 
 The periodical Applied economics quarterly. Supplement 
(ISSN 1612-2127) accompanies / complements the periodical 
Applied economics quarterly (ISSN 1611-6607) 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R21 Work is inspiration for is inspired by Work M to M 
 Definition This is the relationship between two works where the content of the first 
served as the source of ideas for the second 
 Scope notes  
 Examples  The musical West Side Story is inspired by the play Romeo and 
Juliet 
 The painting Plan for a City Gate in Kiev by Viktor Hartmann is 
inspiration for the musical piece The Great Gate of Kiev from 
Pictures at an Exhibition by Modest Mussorgsky 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R22 Work is a transformation 
of 
was 
transformed 
into 
Work M to 1 
 Definition This relationship indicates that a new work was created by changing the 
scope or editorial policy (as in a serial or aggregating work), the genre or 
literary form (dramatization, novelization), target audience (adaptation 
for children), or style (paraphrase, imitation, parody) of a previous work 
 Scope notes Some transformations may be considered as being only inspired by a 
previous work. 
 Examples  Mary Lamb’s Cymbeline, from Charles and Mary Lamb’s Tales 
from Shakespeare, is a transformation of William Shakespeare’s 
Cymbeline 
 Seth Grahame-Smith’s Pride and prejudice and zombies is a 
transformation of Jane Austen’s Pride and prejudice 
 The periodical entitled Le Patriote de Saône-et-Loire 
(ISSN 1959-9935) was transformed into the new periodical 
entitled Le Démocrate de Saône-et-Loire (ISSN 1959-9943) 

IFLA LRM (2017-12) 
 
 74 
Table 4.7 Relationships 
after the former was suppressed by censorship in 1850 [a 
definitive replacement] 
 The separate periodicals entitled Animal research 
(ISSN 1627-3583), Animal science (ISSN 1357-7298), and 
Reproduction nutrition development (ISSN 0926-5287) were 
transformed into the periodical entitled Animal 
(ISSN 1751-7311) [a merger] 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R23 Expression has part is part of Expression M to M 
 Definition This is a relationship between two expressions where one is a 
component of the other 
 Scope notes This applies when the component-to-whole relationship is an inherent 
aspect of the works and holds for all the expressions and manifestations 
of the larger work and of its component works, whether the expression or 
manifestation comprises the full larger work or just one or more (but not 
all) of the component works. 
 Examples  The music notation of Franz Schubert’s Ave Maria Op. 52, 
No. 6 is part of the music notation of Franz Schubert’s Sieben 
Gesänge aus Walter Scott’s Fräulein vom See Op. 52 
 The audio recording of Dante Alighieri's La divina commedia 
read by Enrico de Negri has part the audio recording of Dante 
Alighieri's La divina commedia, Inferno read by Enrico de Negri 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R24 Expression is derivation of has derivation Expression M to 1 
 Definition This relationship indicates that of two expressions of the same work, the 
second was used as the source for the other 
 Scope notes In many cases, the exact source of, for example, a translation, 
adaptation, revision, or arrangement is not known. If it is, it may be an 
interesting aspect for the end-user. The derivation relationship may be 
refined to provide more detailed information about the nature of the 
transformation. 
 Examples 
 
 
 
 The French translation of Y ukio Mishima’s 天人五衰 published 
as “L’ange en décomposition” is a derivation of the English 
translation of Yukio Mishima’s 天人五衰 published as “The 
decay of the angel” 
 The 1965 recording of a performance of Anton Bruckner’s 
Symphony No. 2 in C minor by the Toronto Symphony Orchestra 
directed by Herman Scherchen is a derivation of the particular 
score of Anton Bruckner’s Symphony No. 2 in C minor found in 
the 1892 edition (Doblinger) supervised by Cyrill Hynais with 
revisions by Bruckner 
 The French translation of Wong’s essentials of pediatric nursing 
published as Soins infirmiers : pédiatrie by Chenelière 
éducation (Montréal, Québec), ©2012, is a derivation of the 8th 
English edition, appearing in the manifestation published by 
Mosby/Elsevier (St. Louis, Missouri), ©2009 

IFLA LRM (2017-12) 
 
 75 
Table 4.7 Relationships 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R25 Expression was aggregated by aggregated Expression M to M 
 Definition This relationship indicates that a specific expression of a work was 
chosen as part of the plan of an aggregating expression 
 Scope notes An aggregating expression will select multiple specific expressions of 
other works so that they can be embodied together in an aggregate 
manifestation. An expression may be chosen by multiple aggregating 
expressions. 
 
This is a shortcut of the relationships illustrated in Figure 5.7, the 
general model for aggregates. 
EXPRESSION1 is embodied in MANIFESTATION (aggregate) + 
MANIFESTATION (aggregate) embodies (aggregating) EXPRESSION 
 
Unlike the whole-part relationship between expressions, the expressions 
selected to appear together in the aggregate manifestation do not become 
components of the aggregating expression. Furthermore, the relationship 
between these expressions is not an inherent feature of the works that 
these expressions realize, and thus is does not hold in other expressions 
of those works. 
 Examples  The English text of Edgar Allan Poe’s “The fall of the House of 
Usher” was aggregated by the aggregating expression that 
produced the aggregate manifestation “The Oxford book of 
short stories” chosen by V .S. Pritchett 
 The aggregating expression that produces the monographic 
series “IFLA series on bibliographic control” aggregated the 
English text of “ISBD : International standard bibliographic 
description”, consolidated edition 2011 
 The aggregating expression that produces the monographic 
series “Povremena izdanja Hrvatskoga knjižničarskog društva. 
Novi niz” aggregated the 2014 Croatian text of “ISBD : 
International standard bibliographic description”, consolidated 
edition 2011 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R26 Manifestation has part is part of  Manifestation M to M 
 Definition This is a relationship between two manifestations where one is a 
component of the other 
 Scope notes In some cases the components of a manifestation are based on physical 
considerations relating to the carrier in which the manifestation is 
intended to be issued (for example, a recording is too long to fit on a 
single disc and is issued in a two-disc boxed set). An alternate 
manifestation on another carrier may not display the same components. 
 
However, in the case when the component-to-whole relationship is an 
inherent aspect of the works it holds for all the expressions and 
manifestations of the larger work and of its component works, whether 
the expression or manifestation comprises the full larger work or just one 
or more (but not all) of the component works. 

IFLA LRM (2017-12) 
 
 76 
Table 4.7 Relationships 
 Examples  The Bolchazy-Carducci Publishers publication of Latin for the 
new millennium by Milena Minkova et al. has part the 
Bolchazy-Carducci Publishers publication of volume 5, 
“Level 2: Student text”, ISBN 978-0-86516-563-2, of Latin for 
the new millennium by Milena Minkova et al. 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R27 Manifestation has reproduction is reproduction 
of 
Manifestation 1 to M 
 Definition This is the relationship between two manifestations providing the end-
user with exactly the same content and where an earlier manifestation 
has provided a source for the creation of a subsequent manifestation, 
such as facsimiles, reproductions, reprints, and reissues 
 Scope notes Generally, for reprints and reissues no specific item of the source 
manifestation is singled out as the source of the reproduction. 
Furthermore, in these cases, although a particular item may have been 
used as a source of reproduction, this item should be considered to 
represent the source manifestation as a whole. The process of 
reproduction always results in a new manifestation, even when only a 
single item was produced from that manifestation. 
 Examples  The 1873 publication of Daniel Wilson’s Caliban: the missing 
link by Macmillan has reproduction the 2014 publication of 
Daniel Wilson’s Caliban: the missing link by Cambridge 
University press as a facsimile edition 
 The 2007 reprint edition of Hubert Reeve’s Malicorne: 
réflexions d’un observateur de la nature published by Éditions 
du Seuil as number 179 in the series Points. Science 
(ISBN 978-2-02-096760-0) is reproduction of the 1990 edition 
of Hubert Reeve’s Malicorne: réflexions d’un observateur de la 
nature published by Éditions du Seuil in the series Science 
ouverte (ISBN 2-02-012644-3) 
 The 1990 edition of Hubert Reeve’s Malicorne: réflexions d’un 
observateur de la nature published by Éditions du Seuil in the 
series Science ouverte (ISBN 2-02-012644-3) has reproduction 
the 1991 edition published by France loisirs 
(ISBN 2-7242-6486-X) 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R28 Item has reproduction is reproduction 
of 
Manifestation 1 to M 
 Definition This is the relationship between an item of one manifestation and 
another manifestation providing the end-user with exactly the same 
content and where a specific item has provided a source for the creation 
of a subsequent manifestation 
 Scope notes In this case, the particular item used as a source of reproduction is 
significant, either by its provenance or due to item-specific 
characteristics such as annotations or ownership markings. The process 
of reproduction always results in a new manifestation, even when only a 
single item was produced from that manifestation. 

IFLA LRM (2017-12) 
 
 77 
Table 4.7 Relationships 
 Examples  The 2015 publication of Harry Partch’s Two studies on ancient 
Greek scales by Schott is reproduction of the holograph 
manuscript of Harry Partch’s Two studies on ancient Greek 
scales 
 The Canadian Pacific Railway’s 1913 settlers’ guide : 
information concerning Manitoba, Saskatchewan and Alberta, 
originally published in Montreal in 1913, has reproduction on 
microfiche issued by the Canadian Institute for Historical 
Microreproductions in 2000, which was filmed from a copy of 
the original publication held by the Glenbow Museum Library, 
Calgary 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R29 Manifestation has alternate has alternate Manifestation M to M 
 Definition This relationship involves manifestations that effectively serve as 
alternatives for each other 
 Scope notes Typical cases are when a publication, sound recording, video, etc., is 
issued in more than one format or when it is released simultaneously by 
different publishers in different countries. 
 Examples  The LP release of the punk rock band the Soviettes’ album titled 
“LP III” has alternate the CD release of the punk rock band the 
Soviettes’ album titled “LP III” 
 Agatha Christie’s The Sittaford Mystery published in 1931 in the 
UK by William Collins & Sons has alternate the simultaneous 
US edition published as The Murder at Hazelmoor by Dodd, 
Mead & Co. 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R30 Agent is member of has member Collective 
Agent 
M to M 
 Definition This a relationship between an agent and a collective agent that the 
agent joined as a member 
 Scope notes A person may explicitly join an organization or association. A person 
may implicitly become a member of a family by birth, adoption, 
marriage, etc. 
 
A collective agent may join another collective agent as a member. 
 Examples  The king of England Henry VIII is member of the House of 
Tudor 
 Pearl Buck is member of Phi Beta Kappa 
 IFLA has member the National Library of China 
 Prime Ministers of Canada has member Pierre Elliot Trudeau 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R31 Collective 
Agent  
has part is part of Collective 
Agent 
M to M 
 Definition This is a relationship between two collective agents where one is a 
component of the other 

IFLA LRM (2017-12) 
 
 78 
Table 4.7 Relationships 
 Scope notes  
 Examples  The IFLA Cataloguing Section is part of IFLA 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R32 Collective 
Agent  
precedes succeeds Collective 
Agent  
M to M 
 Definition This is a relationship between two collective agents where the first was 
transformed into the second 
 Scope notes A single instance of this relationship can record a simple transformation 
of a single collective agent into a single successor. Multiple instances of 
this relationship can be used together to capture the more complex 
mergers and splits that can occur between and among collective agents. 
 Examples  National Library of Canada precedes Library and Archives 
Canada 
 National Archives of Canada precedes Library and Archives 
Canada 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R33 Res has association with is associated 
with 
Place M to M 
 Definition This relationship links any entity with a given extent of space 
 Scope notes In most implementations this relationship would be refined to reflect the 
exact nature of the association, for example, place of work conception or 
creation, place of expression creation (e.g., place of musical 
performance), place of publication or manufacture, current or former 
location of an item, and location of an agent.  
 Examples  Emily Dickinson has association with Amherst, Mass. [the town 
where she was born] 
 Zone Books has association with New York City [the city where 
this publisher is located] 
 Gone With the Wind has association with Atlanta, Georgia [the 
city which provides the setting for the narrative] 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R34 Place has part is part of Place M to M 
 Definition This is a relationship between two places where one is a component of 
the other 
 Scope notes  
 Examples  California is part of USA 
 Dolomites is part of Alps 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R35 Res has association with is associated 
with 
Time-span M to M 
 Definition This relationship links any entity with a temporal extent 

IFLA LRM (2017-12) 
 
 79 
Table 4.7 Relationships 
 Scope notes In most implementations this relationship would be refined to reflect the 
exact nature of the association, for example, time of work conception or 
creation, time of expression creation (e.g., date/time of musical 
performance), time of publication or manufacture, period of ownership 
of an item, date of birth of a person, time of validity of the nomen for a 
particular res. 
 Examples  The 1998 publication of Stephen Hawking’s A Brief history of 
time has association with 1998 
 The Phi Beta Kappa Society has association with December 5, 
1776, when it was founded 
 The term 'Happenings (Art)' has association with the date/time 
20151205060018.0, when this term became the valid LCSH 
heading due to the corresponding authority record being 
updated, replacing the term 'Happening (Art)' 
 Emily Dickinson has association with the time-span from 1830 
to 1886 
 The recording of the live performance of the song 
Communication Breakdown by Led Zeppelin in Paris at the 
Olympia on October 10, 1969 has association with the 
time-span of October 10, 1969 
ID Domain Relationship name Inverse name Range Cardinality 
LRM-R36 Time-span has part is part of Time-span M to M 
 Definition This is a relationship between two time-spans where one is a component 
of the other 
 Scope notes  
 Examples  The 1930s is part of the 20th century 
 
 
4.3.4 Relationships Ordered by Domain 
Table 4.8 below is an ordering of the relationships defined in Table 4.7 (Relationships) in section 
4.3.3, according to the entity that is the domain of the relationship. All relationships, as well as all 
inverse relationships for those relationships that are not symmetric, are listed in Table 4.8. The 
inverse relationships are those for which the ID number of the relationship (Rel ID column) 
includes the “i” suffix. For each relationship given in the table, the relationship name, the inverse 
name, the entities that are the domain and the range, and all the respective IDs are given in a 
single row.  
 
In Table 4.8 the relationships are sorted by the entity that is functioning as the domain of the 
relationship. The entities are sorted, using the ID of Domain column, according to the order 
that follows their presentation in Table 4.2 (Entities) in section 4.1.3. Within the same entity 
functioning as domain, the relationships are sorted alphabetically by the relationship name 
column. Finally, in the cases where the same relationship name appears for multiple relationships 
with the same entity as domain, the secondary sort is by the entity that is the range of the 
relationship, using the ID of Range column. 
 

IFLA LRM (2017-12) 
 
 80 
Table 4.8 Relationships by Entity functioning as the Domain 
Rel ID 
ID of 
Domain Domain Relationship name Inverse name 
ID of 
Range Range 
LRM-R13 LRM-E1 Res has appellation is appellation of LRM-E9 Nomen 
LRM-R33 LRM-E1 Res has association with is associated with LRM-E10 Place 
LRM-R35 LRM-E1 Res has association with is associated with LRM-E11 Time-span 
LRM-R1 LRM-E1 Res is associated with is associated with LRM-E1 Res 
LRM-R12i LRM-E1 Res is subject of has as subject LRM-E2 Work 
LRM-R20 LRM-E2 Work 
accompanies / 
complements 
is accompanied / 
complemented by LRM-E2 Work 
LRM-R12 LRM-E2 Work has as subject is subject of LRM-E1 Res 
LRM-R18 LRM-E2 Work has part is part of LRM-E2 Work 
LRM-R22 LRM-E2 Work is a transformation of was transformed into LRM-E2 Work 
LRM-R20i LRM-E2 Work 
is accompanied / 
complemented by 
accompanies / 
complements LRM-E2 Work 
LRM-R21 LRM-E2 Work is inspiration for is inspired by LRM-E2 Work 
LRM-R21i LRM-E2 Work is inspired by is inspiration for LRM-E2 Work 
LRM-R18i LRM-E2 Work is part of has part LRM-E2 Work 
LRM-R2 LRM-E2 Work is realized through realizes LRM-E3 Expression 
LRM-R19 LRM-E2 Work  precedes succeeds LRM-E2 Work 
LRM-R19i LRM-E2 Work succeeds precedes LRM-E2 Work  
LRM-R5 LRM-E2 Work was created by created LRM-E6 Agent 
LRM-R22i LRM-E2 Work was transformed into is a transformation of LRM-E2 Work 
LRM-R25i LRM-E3 Expression aggregated was aggregated by LRM-E3 Expression 
LRM-R24i LRM-E3 Expression has derivation is derivation of LRM-E3 Expression 
LRM-R23 LRM-E3 Expression has part is part of LRM-E3 Expression 
LRM-R24 LRM-E3 Expression is derivation of has derivation LRM-E3 Expression 
LRM-R3 LRM-E3 Expression is embodied in embodies LRM-E4 Manifestation 
LRM-R23i LRM-E3 Expression is part of has part LRM-E3 Expression 
LRM-R2i LRM-E3 Expression realizes is realized through LRM-E2 Work 
LRM-R25 LRM-E3 Expression was aggregated by aggregated LRM-E3 Expression 
LRM-R6 LRM-E3 Expression  was created by created LRM-E6 Agent 
LRM-R3i LRM-E4 Manifestation embodies is embodied in LRM-E3 Expression 
LRM-R29 LRM-E4 Manifestation has alternate has alternate LRM-E4 Manifestation 
LRM-R26 LRM-E4 Manifestation has part is part of  LRM-E4 Manifestation 
LRM-R27 LRM-E4 Manifestation has reproduction is reproduction of LRM-E4 Manifestation 
LRM-R9 LRM-E4 Manifestation is distributed by distributes LRM-E6 Agent 
LRM-R4 LRM-E4 Manifestation is exemplified by exemplifies LRM-E5 Item 
LRM-R26i LRM-E4 Manifestation is part of  has part LRM-E4 Manifestation 
LRM-R27i LRM-E4 Manifestation is reproduction of has reproduction LRM-E4 Manifestation 
LRM-R28i LRM-E4 Manifestation is reproduction of has reproduction LRM-E5 Item 
LRM-R7 LRM-E4 Manifestation was created by created LRM-E6 Agent 
LRM-R8 LRM-E4 Manifestation was manufactured by manufactured LRM-E6 Agent 
LRM-R4i LRM-E5 Item exemplifies is exemplified by LRM-E4 Manifestation 
LRM-R28 LRM-E5 Item has reproduction is reproduction of LRM-E4 Manifestation 
LRM-R10 LRM-E5 Item is owned by owns LRM-E6 Agent 

IFLA LRM (2017-12) 
 
 81 
Table 4.8 Relationships by Entity functioning as the Domain 
Rel ID 
ID of 
Domain Domain Relationship name Inverse name 
ID of 
Range Range 
LRM-R11 LRM-E5 Item was modified by modified LRM-E6 Agent 
LRM-R14 LRM-E6 Agent assigned was assigned by LRM-E9 Nomen 
LRM-R5i LRM-E6 Agent created was created by LRM-E2 Work 
LRM-R6i LRM-E6 Agent created was created by LRM-E3 Expression  
LRM-R7i LRM-E6 Agent created was created by LRM-E4 Manifestation 
LRM-R9i LRM-E6 Agent distributes is distributed by LRM-E4 Manifestation 
LRM-R30 LRM-E6 Agent is member of has member LRM-E8 
Collective 
Agent 
LRM-R8i LRM-E6 Agent manufactured was manufactured by LRM-E4 Manifestation 
LRM-R11i LRM-E6 Agent modified was modified by LRM-E5 Item 
LRM-R10i LRM-E6 Agent owns is owned by LRM-E5 Item 
LRM-R30i LRM-E8 
Collective 
Agent has member is member of LRM-E6 Agent 
LRM-R31 LRM-E8 
Collective 
Agent  has part is part of LRM-E8 
Collective 
Agent 
LRM-R31i LRM-E8 
Collective 
Agent is part of has part LRM-E8 
Collective 
Agent  
LRM-R32 LRM-E8 
Collective 
Agent  precedes succeeds LRM-E8 
Collective 
Agent  
LRM-R32i LRM-E8 
Collective 
Agent  succeeds precedes LRM-E8 
Collective 
Agent  
LRM-R17i LRM-E9 Nomen has derivation is derivation of LRM-E9 Nomen 
LRM-R16 LRM-E9 Nomen has part is part of LRM-E9 Nomen 
LRM-R13i LRM-E9 Nomen is appellation of has appellation LRM-E1 Res 
LRM-R17 LRM-E9 Nomen is derivation of has derivation LRM-E9 Nomen 
LRM-R15 LRM-E9 Nomen is equivalent to is equivalent to LRM-E9 Nomen 
LRM-R16i LRM-E9 Nomen is part of has part LRM-E9 Nomen 
LRM-R14i LRM-E9 Nomen was assigned by assigned LRM-E6 Agent 
LRM-R34 LRM-E10 Place has part is part of LRM-E10 Place 
LRM-R33i LRM-E10 Place is associated with has association with LRM-E1 Res 
LRM-R34i LRM-E10 Place is part of has part LRM-E10 Place 
LRM-R36 LRM-E11 Time-span has part is part of LRM-E11 Time-span 
LRM-R35i LRM-E11 Time-span is associated with has association with LRM-E1 Res 
LRM-R36i LRM-E11 Time-span is part of has part LRM-E11 Time-span 
 
 
  

IFLA LRM (2017-12) 
 
 82 
  

IFLA LRM (2017-12) 
 
 83 
 Model Overview 
5.1 Entity-Relationship Diagrams 
The entities and the significant relationships between them can be summarized in a series of 
entity-relationship diagrams. Attributes do not appear in these diagrams, each attribute is simply 
a characteristic associated with the relevant entity. 
 
Conventions used in the entity-relationship diagrams: 
 A rectangle is used for each entity, these serve as nodes which are connected by 
relationships. The name of the entity is written in all capitals within the rectangle. 
 A line (arrow) represents the relationship (or relationships) which hold between the 
entities. The name (or names) of the relationships are written in lower case by the line 
(first the relationship name, then the inverse name underneath it). 
 When a relationship is recursive (the same entity is both the domain and the range), the 
arrow is shown as a loop at one of the corners of the entity rectangle. The name of the 
relationship is written within the loop. 
 When illustrated, the “isA” hierarchy which links subclass entities to their superclass 
entity, is shown with a dotted line. 
 The cardinality of a relationship is indicated by the arrowheads: 
◦ a single-headed arrow indicates that the cardinality for that entity is “one (1)” 
◦ a double-headed arrow indicates that the cardinality for that entity is “many (M)”. 
 
Figure 5.1    Relationships between Work, Expression, Manifestation, and Item 
 
WORK
EXPRESSION
MANIFESTATION
ITEM
is realized through
realizes
is embodied in
embodies
is exemplified by
exemplifies
 
 

IFLA LRM (2017-12) 
 
 84 
Relationships LRM-R2 to LRM-R4 are shown in Figure 5.1. These relationships indicate that a 
work may be realized through one or more than one expression; an expression, on the other hand, 
realizes one and only one work. An expression may be embodied in one or more than one 
manifestation; likewise, a manifestation may embody one or more than one expression. A manifestation, 
in turn, may be exemplified by one or more than one item; but an item may exemplify one and 
only one manifestation. 
 
 
Figure 5.2    Responsibility Relationships between Agents and Works, Expressions, Manifestations, 
and Items 
 
WORK
EXPRESSION
MANIFESTATION
ITEM
AGENT
was created by
created
was created by
created
was created by
created
was manufactured by
manufactured
is distributed by
distributes
is owned by
owns
was modified by
modified
 
Relationships LRM-R5 to LRM-R11 are shown in Figure 5.2. These relationships all hold 
between the entity agent (or by extension either of its subclasses) and works, expressions, 
manifestations, and items. These relationships capture responsibility for the processes of creation, 
manufacture, distribution, ownership or modification. All these relationships are many-to-many, 
indicating that any number of agents may be involved in any number of specific instances of any 
of these processes. 
 

IFLA LRM (2017-12) 
 
 85 
Figure 5.3    Subject Relationship 
WORK RES
has as subject
is subject of
 
Relationship LRM-R12 is depicted in Figure 5.3. This relationship links works to the res which are 
the subject of the works. Any res (and so by extension any other entity, as all entities are 
subclasses of the entity res) may be the subject of one or more works; works may have one or 
more res as their subject. 
 
Figure 5.4    Appellation Relationship 
has part
RES NOMEN
has apellation
is appellation of
 
Relationship LRM-R13 is depicted in Figure 5.4. This relationship links a res to its nomens. Any res 
(and so by extension any other entity, as all entities are subclasses of the entity res) may be known 
by one or more nomens. Each nomen is the appellation of a single res. (For the application of this 
relationship to the modelling of bibliographic identities, see section 5.5.) Relationship LRM-R16, 
which states that nomens may have parts which are themselves nomens, is also illustrated. 
 
Figure 5.5    Relationships among Agents 
AGENT
PERSON
COLLECTIVE
AGENT
isA
isA
has part
precedes
is member of
 

IFLA LRM (2017-12) 
 
 86 
Relationships LRM-R30 to LRM-R32 are shown in Figure 5.5. The membership relationship 
holds between a collective agent and any agent (person or another collective agent). A collective agent may 
have one or more members, and an agent may be a member of one or more collective agents. 
Collective agents may have one or more parts which are themselves collective agents, and collective agents 
may precede and succeed each other over time. To these relationships is added an indication of 
the “isA” hierarchy between the entity agent and its subclasses person and collective agent. 
 
Figure 5.6    Overview of  Relationships 
RES
WORK
EXPRESSION
MANIFESTATION
ITEM
AGENT
PLACE
TIME-SPAN
NOMEN
PERSON
COLLECTIVE
AGENT
is subject of
is realized through
is embodied in
is exemplified by
created
created
created
manufactured
distributes
owns
modified
isA
isA
was assigned by
is appellation of
is associated with
is associated with
is associated with
has part
precedes
accompanies
is inspiration for
is transformation of
has part
is derivation of
has part
is derivation of
has part
has reproduction
has alternate
has part
precedes
has part
has part
is member of
has reproduction
 
 
The final overview diagram, Figure 5.6, shows all the relationships depicted in figures 5.1 
through 5.5 along with all other relationships defined in the model. The shortcuts are not 
illustrated. To streamline the presentation, the “isA” hierarchical structure that connects all 
entities to the entity res is omitted, and only the relationship names that correspond to the 
direction illustrated are given. Unlike the preceding diagrams, the cardinality of relationships is 
not indicated; rather the single arrowheads correspond to the direction of the relationship whose 
name is given. 
 
The diagram illustrates that a res may be associated with other res (LRM-R1), as well as with 
instances of place (LRM-R33) and time-span (LRM-R35). The entities place and time-span may be 
composed of parts which are themselves respectively places (LRM-R34) and time-spans 
(LRM-R36). Nomens are assigned by an agent (LRM-R14), and may be derived from other nomens 
(LRM-R17) as well as being composed of parts which are themselves nomens (LRM-R16). 
 
Works may be related to other works in several ways: as component parts, as logical predecessors 
or successors, by accompanying or complementing each other, by serving as inspiration for other 
works, or by being transformed into new works (LRM-R18 to LRM-R22). Similarly, expressions of a 
work can be derived into new expressions (LRM-R24) and may have expressions as component parts 
(LRM-R23); manifestations may be related as reproductions (LRM-R27) or as alternates 
(LRM-R29), and may also have manifestations as component parts (LRM-R26). Items may be 
related to manifestations as the source for a reproduction (LRM-R28). 

IFLA LRM (2017-12) 
 
 87 
5.2 Constraints between Entities and Alignments 
IFLA LRM declares that, other than those entities related by the “isA” hierarchies, the entities in 
the model are disjoint. Disjointness is a strong constraint and means that the disjoint entities can 
have no instance that is simultaneously an instance of more than one of these entities. 
 
Some of the consequences of disjointness are seldom disputed, such as that something cannot be 
both an instance of the person entity and an instance of the collective agent entity. It takes a little 
more thought to realize that something cannot be both an instance of the manifestation entity (an 
abstract entity which is a set) and an instance of the item entity (a concrete entity). While only one 
physical object may exist, it is viewed according to distinct aspects as to whether its manifestation 
nature is being considered, or whether its item aspects are in focus. 
 
Further, if someone says that “Hamlet is a work”, and someone else says that “Hamlet is an 
expression”, it does not imply that Hamlet is simultaneously both a work and an expression, as 
opponents to the notion of disjointness of the work, expression, manifestation, and item entities 
might argue: it simply means that these two individuals have distinct aspects of Hamlet in mind, 
but refer to these distinct aspects using nomens which have the same nomen string. This issue is 
better solved by examining the relationships that are implemented in actual databases than by 
eliminating disjointness altogether: it is these relationships that denote, in a very practical way, 
either a work or an expression, rather than metaphysical discussions about what Hamlet “is” in the 
absolute. 
 
In practice, if there is a need to align two data sources that hold contradictory views about 
something that is identified through a given URI, it is possible to extrapolate the existence of 
implicit, additional entities that can serve as gateways between those contradictory views. For 
example, if a library catalogue claims that a French translation of Hamlet is an expression, and a 
database produced by a rights society claims that the same French translation of Hamlet, 
identified by the same URI, is a work, both views can be reconciled by assuming that the “thing” 
identified by that URI is neither a work nor an expression, but a “textual creation”, that is, the 
combination of linguistic symbols and concepts, and that the library catalogue only accounts for 
the linguistic symbols of which that textual creation consists, while the rights society’s database 
only envisions the concepts involved in the translation process. An expansion of the IFLA LRM 
model, aiming at allowing these two data sources to be merged, could be developed, by declaring 
an additional entity: textual creation, and two additional relationships: textual creation has conceptual 
content work, and textual creation has symbolic content expression. 
 
5.3 Modelling of Online Distribution 
Production processes form an intrinsic part of a manifestation. In the case of manifestations that are 
intended to be distributed online, such as downloadable files or streaming media, the production 
process consists of a specification of actions that will take place once triggered by an action by 
the end-user. 
 
As a result, the production plan will involve aspects that are not fully specified as they are not 
under the direct control of the producer, such as the specific digital storage media onto which an 
online file is downloaded by different end-users. Whatever storage media is used, the 
downloaded files are instances of the same manifestation as the online file. This is the case also for 
printing on demand, where the producer cannot control, for example, the colour of paper that 
the end-user will use to make the printout. 

IFLA LRM (2017-12) 
 
 88 
 
These processes, strictly speaking, result in variant states in a manifestation, and even in very 
slightly variant expressions, when digital rights management software modifies the file as it is being 
downloaded to the end-user’s device. 
 
When it comes to digital publishing, the acquisition process is not so much associated with the 
production of physical items, as with the duplication of the content of the manifestation (possibly 
with alterations, e.g., the addition of a file or metadata stating specific rights and identifying the 
acquirer of a “digital item” – in that case, strictly speaking, the whole process would be 
considered to result in the creation of a new, distinct manifestation). However, it would be 
impractical, and not meet user needs, to regard all “digital items” as distinct singleton 
manifestations. 
 
If there is a need, in a given implementation, to identify and describe specific “digital items” as 
such, an extension to the basic IFLA LRM model could be developed. Such an extension could 
account for the specific characteristics of digital objects, by defining a digital item entity at an 
intermediate level between the manifestation and item entities. In such an extension, item is entirely 
a physical entity, while digital item is basically a file or a package of files that contains the overall 
content of a manifestation and that may be altered (during the acquisition process or afterwards), 
by the addition of particular statements of rights and ownership, further annotations, 
degradations of the octet stream, etc. 
 
5.4 Nomens in a Library Context 
In a library context, the nomens for persons, collective agents (such as families and corporate bodies), 
or places have been traditionally referred to as names, the nomens for works, expressions, and 
manifestations as titles, while the nomens for res used in a subject context are variously referred to as 
terms, descriptors, subject headings, and classification notation. 
 
An identifier is a type of nomen that is intended to have persistence and uniqueness within a 
specific domain of application, such as identifiers for publications of a specific type, or identifiers 
for persons, so that instances of that entity can be specifically identified and referred to 
unambiguously. What distinguishes an identifier from other nomens is that the nomen string 
attribute value of an identifier cannot be identical with the nomen string attribute value of any 
other nomen, within a given system (of course, other nomens, outside that system, may happen to 
have the same nomen string attribute value). Identifiers are generally assigned by authorized 
assignment agencies according to agreed-upon rules. Instances of assignment agencies include, 
but are not limited to, registration agencies for ISO identifiers, national governments for 
identifiers for citizens and residents. The scope of an identifier system may be broad (such as 
URI) or highly specialized (catalogue numbers for the works of a specific composer). 
 
In library information systems, controlled access points are a type of nomen that has traditionally 
been assigned to be used to provide collocation for persons, collective agents (that is, families and 
corporate bodies), works, and expressions, as well as for additional entities used as objects of the has 
as subject relationship. 
 
Controlled access points are nomens constructed according to the relevant rules in the 
bibliographic system. They can take the form of names, titles, terms, codes, etc., as specified by 
the relevant construction rules. 
 

IFLA LRM (2017-12) 
 
 89 
In many knowledge organization systems, controlled access points can be designated as one of 
two sub-types: 
 
a) preferred or authorized access points 
b) variant access points. 
 
Preferred or authorized access points uniquely identify an instance of an entity within a catalogue 
or database and thus also serve as identifiers, while variant access points may or may not be 
uniquely associated (one-to-one) with a specific instance of an entity, depending on the 
construction rules applied. 
 
In current library practice, name authority records are generally created for each bibliographically 
significant cluster of nomens that refer to the same instance of an entity, and record both the 
nomen string representing the preferred form of the access point (a nomen) and the nomen strings 
corresponding to any variant access points or identifiers (additional nomens). Although an 
authority record controls nomens, as a shortcut information about the instance of an entity 
referred to by the nomens is generally recorded in the same authority record along with 
information about the nomens, blurring the distinction between the entities res and nomen. The 
modelling of all categories of authority records used in current library practice is quite complex 
and outside the scope of the model. 
 
5.5 Modelling of Bibliographic Identities 
The modelling of bibliographic identities (or personas) in IFLA LRM makes use of the nomen 
entity and the ‘has appellation’ relationship. The ‘has appellation’ relationship is one-to-many and 
holds between instances of any entity and the various nomens used for that instance. Instances of 
all entities have multiple appellation relationships to different nomens. The different nomens for the 
same instance of an entity will likely differ in the values held for one or more of the nomen 
attributes (such as, language, script, scheme, etc.). 
 
In particular, persons (defined as: an individual human being) generally have multiple nomens; the 
use of each nomen may be governed by many factors, including the preference for certain nomens 
in specific contexts. The context of use attribute of a nomen is used to record those aspects of this 
context that are deemed relevant in making the distinction between bibliographic identities that 
are recognized as distinct in a particular bibliographic environment. The relevant context may be 
simple to describe explicitly, or it may be inferred from multiple characteristics. In a simple 
situation, the context of use can relate a nomen (or nomens) as being used by a person when publishing 
literary works, while another cluster of nomens may be identified as those used by the same person 
when publishing scientific works. In a more complex case, the context of use may need to 
distinguish between nomens used by a person in writing a series of novels about one imaginary 
world, and the other nomens used by that person when writing another series of novels about a 
different imaginary world. 
 
In the model, a bibliographic identity is a cluster of nomens used by a person in the same 
bibliographically significant context or contexts. Which kinds of differences in context of use 
trigger the recognition, and consequent specific handling, of distinct bibliographic identities, 
depend on the cataloguing rules or knowledge organization system. For example, multiple 
pseudonyms for the same person may require multiple preferred access points in the cataloguing 
rules, but only a single classification number. 
 

IFLA LRM (2017-12) 
 
 90 
According to some current cataloguing rules, name authority records are generally created for 
each distinct bibliographically significant nomen cluster or identity, and information about the 
instance of an entity referred to through the nomens is generally also recorded in the authority 
record. When multiple, distinct nomen clusters are known to be related to the same underlying 
instance of an entity, current practice may permit linking the authority records for those clusters 
that are in the same authority file. 
 
The bibliographic identities formed by nomen clusters are a type of res, and have enough 
persistence to be assigned nomens, such as the International Standard Name Identifier (ISNI) 
which is a nomen (of type identifier) assigned to public identities. An ISNI, a preferred access 
point and several variant access points may all be nomens of the same bibliographic identity, and 
so are equivalent nomens for that identity (res). 
 
EXAMPLE 
A real person uses two distinct nomen clusters in different contexts of use; each of these clusters 
includes three nomens. As this difference in context of use is significant in the particular cataloguing 
code, within each cluster the cataloguing rules have designated one nomen in the form of an 
access point as the preferred form, and the other access point as a variant. Each cluster may be 
recorded in a different authority record and the two records may be linked to draw out their 
relationship to the same person. 
 
Person 1: Nomen 1: Context (detective fiction), Category (preferred form of access point) 
  Nomen 2: Context (detective fiction), Category (variant form of access point) 
  Nomen 3: Context (detective fiction), Category (identifier of type ISNI) 
 
  Nomen 4: Context (romance novels), Category (preferred form of access point) 
  Nomen 5: Context (romance novels), Category (variant form of access point) 
  Nomen 6: Context (romance novels), Category (identifier of type ISNI) 
 
In some real-life situations, the cataloguer may not know whether one cluster of nomens is used 
by the same person as another distinct cluster of nomens. Furthermore, the cataloguer may not 
know (and has no need to know) whether any of these nomens is a form of the person’s real, legal 
name or not. The lack of fuller knowledge means that the full set of possible relationships 
between these nomen clusters cannot be recorded, but otherwise does not affect the provision of 
access to resources. In some cases, all the cataloguer may know with certainty is that a nomen 
appears in a manifestation statement that attributes responsibility for some aspect of a work or 
expression. The wording of the statement may be consistent with the assumption that the agent is a 
person or may give another impression. The cataloguer’s real-world knowledge will lead to the 
conclusion that since an expression of a work exists, then some actual agent (or several agents) was 
responsible for its creation, no matter how little information about those agents is available. 
 
In any implementation, cataloguing rules need to operationalize the handling of persons and their 
nomen clusters. Generally, cataloguing rules make the default assumption that each nomen cluster 
used in a consistent context of use is the appellation of a single person, and then make provisions for 
adding appropriate relationships among the bibliographic identities when this turns out not to be 
the case. These other cases include the use in different contexts of multiple bibliographic 
identities by the same person (real name and pseudonym or multiple pseudonyms). Conversely, a 
single nomen cluster formulated according to a pattern culturally associated with individual persons 
may actually identify a collective agent consisting of multiple persons (joint pseudonyms). 
 

IFLA LRM (2017-12) 
 
 91 
5.6 Representative Expression Attributes 
In a strict formal sense, within the model all the expressions of a work are equal as realizations of 
the work. However, research with end-users indicates that they consider certain characteristics as 
inherent in works and that expressions that reflect those characteristics can be felt to best represent 
the intention of the creators of that work. The perceived “distance” between a given expression 
and the image of the “ideal” expression is often of interest and may be used as a selection criterion 
for expressions. For many purposes, end-users seek out expressions that display “original” 
characteristics and are particularly interested in manifestations of these expressions. 
 
In many situations the representative or “canonical” characteristics are easily identified as those 
portrayed in the first or original expression of the work, which is in turn embodied in the first 
manifestation of the work. Other expressions can, if the full history of the work is known, be seen as 
taking shape from a network of derivations or transformations starting from an original 
expression. Other situations are not as clear-cut. Textual works initially issued simultaneously in 
two or more languages, none of which is identified as the original language (such as government 
documents of multilingual countries or publications of multinational organizations) could either 
be considered to have multiple “original” languages, or either not to have a single “original” 
language at all. Similarly, musical works with alternative instrumentation could be considered to 
have multiple “original” values for the medium of performance attribute. In some cases, the 
derivation history of the expressions of a work is sufficiently complex that the expression features 
considered “canonical” by current users in identifying the work were not actually those present in 
an original expression. 
 
End-users intuitively understand that William Shakespeare’s Hamlet is linked to the English 
language and that its literary form is a play. Users will consider that derived expressions, such as 
abridgements or translations, are distinct expressions of the work that are more distant from the 
“original” expression than full-length English language editions. This judgement is based on 
cultural knowledge and assumptions about what the early expressions of the play were like, even 
though few end-users have been directly exposed to early manifestations of these expressions. 
 
Similarly with musical works, through cultural knowledge end-users consider Franz Schubert’s 
piano sonata D. 959 in A major to be a work for piano in the form of a sonata, without making 
reference to specific scores or recorded performances. Rather, many scores and recorded 
performances are viewed as equally reflecting these canonical or representative attributes. 
 
This sort of extrapolation of characteristics significant in identifying a work occurs even when all 
early expressions and manifestations are lost, such as with classical texts originally passed down 
orally. End-users still consider Homer’s Odyssey to be linked to the Classical Greek language and 
that it is a narrative poem, even though the earliest extant versions are considerably later than the 
original creation, and even though the evidence for Homer as an individual creator has been 
questioned. Some characteristics can be inferred even for lost works with no extant expressions or 
manifestations, as long as some other evidence exists. 
 
Since end-users perceive certain characteristics as pertaining to, or being inherent in, the work 
itself, these characteristics are useful as a means of describing and identifying the work. The 
values of these expression attributes can be notionally “transferred” to the work and used in work 
identification, although strictly speaking these attributes concern expression characteristics and not 
work characteristics. 
 

IFLA LRM (2017-12) 
 
 92 
In the model, the work attribute representative expression attribute records the values of those 
attributes that are imputed to the work level through this mental process. This attribute is defined 
in the model as a pragmatic way to “park” information under the work, and in this way avoid the 
need to record the information in association with any specific expression. When the actual 
representative expressions may not otherwise be needed in the database as no manifestations of 
those expressions are represented, this streamlining is particularly convenient. 
 
For any expression of the work, the values held by the same attributes at the expression level permits 
a rough measure of the “distance” between a given expression and expressions that would be 
perceived as representative or “canonical”. Many expressions of a work may, in fact, match the 
values of the representative expression attributes and so form a network or cluster of canonical 
expressions. As the work attributes are distinct from the source expression attributes, there is no 
contradiction in having expressions of the work that hold values for these attributes different from 
those recorded as representative expression attributes. 
 
The model provides the container for these significant attributes by declaring a single, 
multivalued attribute for the work. However, an implementation would need to specify which 
attributes are considered significant for the identification of works and provide appropriate sub-
types for the attribute representative expression attribute. The sub-types might be defined differently 
depending on the value of the category of work attribute. For example, for primarily textual works, 
the expression attribute language might be chosen. For cartographic works, the expression attribute 
cartographic scale may be significant, but not language. Many expression attributes have the potential 
to be adopted as representative expression attributes for some categories of work. For example, the 
attributes intended audience, cartographic scale, language, key, medium of performance, as defined in the 
model, could plausibly be used. 
 
To reduce data entry, a cataloguing module can implement “automatic” promotion to 
representative expression attribute for relevant expression attributes in the vast majority of cases where 
new works are realized through a single manifestation of a single expression. This would also 
frequently (but not always) be the case with art works. 
 
The model does not prescribe the criteria that are to be applied in making the determination of 
representativity for the values of any given expression attribute; this is operationalized by the 
relevant cataloguing practice. Whether a characteristic is displayed by the original expression of the 
work will often be a component of this decision-making process, as will solutions for those cases 
where there is no clear original, or the original has not been preserved, or the cataloguer does 
not have enough information to know. These operational criteria may involve judgement of the 
appropriateness of certain expression characteristics for the end-user population, such as arbitrarily 
selecting among several equally “original” expressions, the one that is in the language of the 
catalogue. 
 
EXAMPLE 
Work: was created by: Louise Penny 
 has title (work): Still life  
 language (representative expression attribute): English 
 category of work: Novel 
 
Expression 1 (matches the representative expression attributes): 
 has language: English 
 has title: Still life 
 was created by: Louise Penny 

IFLA LRM (2017-12) 
 
 93 
Expression 2 (does not match the representative expression attribute language): 
 has language: French 
 has title: Nature morte 
 was created by (translator): Michel Saint-Germain 
 
5.7 Modelling of Aggregates 
An aggregate is defined as a manifestation embodying multiple expressions. Three distinct types of 
aggregates exist:  
 
 Aggregate Collections of Expressions 
Collections are sets of multiple independently created expressions which are ‘published’ 
together in a single manifestation. Collections include selections, anthologies, monographic 
series, issues of serials and other similar groups of resources. Examples include journal 
issues (aggregates of articles), multiple novels published together in a single volume, 
books with independently written chapters, compilations on CDs (aggregates of 
individual songs), and various collected/selected works. A distinctive characteristic of 
collections is that the individual works are usually similar in type and/or genre such as a 
collection of novels by a particular author, songs by a particular artist, or an anthology of 
a genre of poetry. However, in other cases, they also may be what appears to be a 
random collection of expressions. 
 
 Aggregates Resulting from Augmentation 
Aggregates resulting from augmentation are distinct from collections in that they typically 
consist of a single independent work that has been supplemented with one or more 
dependent works. Such aggregates occur when an expression is supplemented with 
additional material that is not integral to the original work and does not significantly 
change the original expression. Forewords, introductions, illustrations, notes, etc. are 
examples of augmenting works, as are full scores with added reduction for piano. The 
augmenting material may or may not be considered significant enough to warrant distinct 
bibliographic identification. 
 
 Aggregates of Parallel Expressions 
Manifestations may embody multiple, parallel expressions of the same work. A single 
manifestation containing expressions of the work in multiple languages is a common form of 
this type of aggregate. They are commonly used to publish manuals and official 
documents for multilingual environments. Parallel expressions are also common on the 
web where users are provided access to equivalent material in their choice of languages. 
Other examples include publishing a text in its original language with a translation, or a 
DVD containing a motion picture with a choice of spoken languages and subtitle 
languages. 
 
Manifestations may contain multiple expressions as indicated by the many-to-many relationship 
between expressions and manifestations. This is the only many-to-many relationship among the 
WEMI entities. A manifestation can embody multiple expressions and an expression can be embodied 
in multiple manifestations. By contrast, an expression can only realize a single work and an item can 
only exemplify a single manifestation. 
 
Modelling an aggregate simply as an embodiment of discrete expressions may fail to recognize the 
creative effort of the aggregator or editor. The process of aggregating the expressions is itself an 

IFLA LRM (2017-12) 
 
 94 
intellectual or artistic effort and therefore meets the criteria for a work. In this sense the 
aggregation happens on the expression level, because only expressions can be combined (or 
aggregated). In the process of combining the expressions and thus, consequently, creating the 
aggregate manifestation, the aggregator creates an aggregating work. This type of work has also been 
referred to as the glue, binding, or the mortar that transforms a set of individual expressions into 
an aggregate. This effort may be relatively minor—two existing novels published together—or it 
may represent a major effort resulting in an aggregate that is significantly more than a sum of its 
parts (for example an anthology). The essence of the aggregating work is the selection and 
arrangement criteria. It does not contain the aggregated works themselves and the whole-part 
relationship is not applicable. An aggregate should not be confused with works which were 
created with parts, such as multipart novels. 
 
The modelling of aggregates as a manifestation embodying multiple expressions is simple and 
straightforward; works and expressions are treated identically regardless of their form of publication 
or the physical manifestation in which they are embodied. An expression may be published alone or 
it may be embodied in a manifestation with other expressions. This general model is illustrated in 
Figure 5.7. 
 
Although every aggregate manifestation also embodies an expression of the aggregating work, these 
expressions may, or may not, be considered significant enough to warrant distinct bibliographic 
identification. The model, however, is flexible, permitting the aggregating work to be described at 
any time. If the aggregating work was not initially identified, it can be described later, if appropriate. 
In the same way, a previously undescribed augmentation (for example, a preface) can be 
described when considered significant, for example, when it is republished as an essay. 
 
Figure 5.7    General Model for Aggregates 
 
 
5.8 Modelling of Serials 
Serials are complex constructs that combine whole/part relationships and aggregation 
relationships: 
 the complete serial manifestation has a whole/part relationship to its individual issues 
published over time (even though there are serials that happen to have only one issue 
released); 
 and each individual issue is an aggregate of articles (even though there are serials that can 
occasionally have issues consisting of only one article). 
 
  
  
  
  
  
  
Aggregating 
Expression 
  
  
  
  
  
Aggregate 
Manifestation 
   
  
is embodied in 
  
The Works 
 
Aggregating Work 
Expressions 
is embodied in 
is realized through 
is realized through 

IFLA LRM (2017-12) 
 
 95 
Each issue of a serial constitutes an aggregate manifestation according to the IFLA LRM definition 
of aggregate as a manifestation embodying multiple expressions as each issue embodies expressions of 
multiple works, as well as an expression of an aggregating work which provides the plan for the 
aggregation of that issue. On the other hand, the manifestation constituting the complete serial as a 
whole is issued in a sequence of parts over time, in a whole/part relationship at the manifestation 
level (LRM-R26). In the case of a serially-issued sequence of aggregate manifestations, the 
corresponding aggregating work is termed a serial work. In the model, the term serial work is 
restricted to this specific type of aggregating work; this usage differs from common library usage in 
which the term “serial work” is used interchangeably with the term “serial” to refer to the 
resulting sequence of aggregate manifestations. The serial work gives rise to the sequence of 
aggregating works resulting in the individual issues through the work-inspiration relationship (LRM-
R21). Despite their differences, these aggregating works are each inspired by the overall editorial 
policy, scope and style of the serial work. However, the serial work does not have a whole/part 
relationship at the work level to the issues. 
 
The description of serial works is particularly difficult to model, because it does not limit itself to 
a description of the past, but is also intended to allow end-users to make assumptions about 
what the behaviour of a serial work will be, at least in the near future. The “thing” described may 
have changed dramatically in the past, and may do so even more dramatically in the future. 
 
Since the work entity is defined, in IFLA LRM, as one “that permits the identification of the 
commonality of content between and among various expressions”, a serial work can be modelled as 
a particular case of the work entity, although the notion of “commonality of content” is not to be 
understood in the same sense as for monographs. Each issue of a serial aggregates distinct 
articles, and it is therefore not possible to claim that the same ideas are common to the various 
expressions embodied in the manifestations of all the issues that make up a serial, while it is possible 
to claim that the same ideas are common to the English text of Romeo and Juliet and an Italian 
translation of it. Rather, the “commonality of content” that defines a serial work resides in both 
the publisher’s and the editor’s intention to convey the feeling to end-users that all individual 
issues do belong to an identifiable whole, and in the collection of editorial concepts (a title, an 
overall topic, a recognizable layout, a regular frequency, etc.) that will help to convey that feeling. 
 
Such a constellation of editorial concepts can evolve over time without the serial work losing its 
identity. The same can be said of monographic works, for that matter: for example, the concepts 
expressed in the sixth edition of Darwin’s On the Origin of Species are not quite the same as those 
expressed in the first edition of that same work. 
 
Consider the case of a serial issued with distinct regional “editions” (for example The Wall Street 
journal which is issued in Eastern and Western editions). The use of the term “edition” gives the 
impression that this case is analogous with monograph edition statements which frequently 
indicate two expressions of the same work. However, for a serial work, whose essence is the 
editorial concepts that guide the production of the issues that comprise the resulting aggregate 
manifestation, the differences between regional editions are sufficient to result in two distinct, 
albeit related, serial works. It is far more satisfactory to regard any serial as a distinct instance of 
the work entity, and to acknowledge the existence of specific relationships (e.g., “is a sibling local 
edition of”) among instances of the serial work entity. In this high-level model, however, not all 
specific relationships that may hold between serial works are listed. Applications which need a 
more detailed model for serials are invited to either adopt a specific conceptual model for serials, 
such as PRESSOO, or declare, as refinements of the high-level work-transformation relationship 
(LRM-R22), their own set of specific relationships among serial works, according to the overall 
philosophy of the IFLA LRM model. 

IFLA LRM (2017-12) 
 
 96 
 
It ensues that any serial work can be said to have only one expression and only one manifestation. All 
relationships between serials can be modelled as work-to-work relationships, even in cases where 
all the issues of a given serial that have been published so far aggregate translations of articles 
that are themselves aggregated in the issues of another serial: it would be tempting to say that the 
text of the former serial is a “translation” of the text of the latter, and that both are, therefore, 
according to the cataloguing rules that currently prevail in the library world, “expressions” of one 
and the same “work”. However, as it is impossible to predict that this relationship will hold in 
the future, it would be wrong to model these two serials as mere expressions of one work, and it is 
ontologically more accurate to regard them as completely distinct works. Similarly, when a serial is 
released in the form of printed issues and another serial is released as PDF files made available 
online, and when a thorough examination of all the issues of both serials that have been released 
so far reveals that the content of the PDF files is rigorously identical with the content of the 
printed issues, it would be tempting to model these two serials as two manifestations of one 
expression of one work. But once again, it is impossible to affirm that the serial issued on paper 
will be coextensive in time with the online serial, and that this relationship will hold in the long 
term. 
 
However, it remains possible to expand the IFLA LRM model by defining additional entities that 
comprise, say, the paper edition of a journal and its edition on the web; all linguistic editions of a 
journal that is published in more than one language as separate editions; all local editions of a 
journal, etc., according to the needs that have to be met in a given implementation of the model. 
An ISSN can therefore be said to identify an individual serial work, while an ISSN-L can be said 
to identify a particular case of such an additional entity when, at the time of cataloguing, a given 
serial is simultaneously released in printed form and as PDF files. 
 
  

IFLA LRM (2017-12) 
 
 97 
 Alignment of User Tasks with the 
Entities, Attributes and Relationships 
6.1 Use Cases Illustrating the User Tasks 
Each of the five generic user tasks defined in sections 3.2 and 3.3 is a generalization of many 
specific tasks likely to be carried out by users of library data and library databases. The use cases 
presented in Table 6.1 below illustrate a range of these specific tasks. The use cases make the link 
between the end-users’ activity and the model by framing the end-user’s information seeking in 
terms of the entities, attributes and relationships defined in the model. These use cases are 
illustrative of the range of user queries and show how the elements of the model are used to 
fulfill the user tasks. The use cases given here are by no means exhaustive; many variants or 
combinations would normally be encountered in a real-life situation. 
 
Table 6.1 Use Cases for User Tasks 
Task Use Cases 
Find To find all manifestations of expressions of a work 
- by searching using a title associated with the work or one of its expressions or 
manifestations 
 
To find all expressions of a work that 
- are written in a given language 
 
To find resources that have a relationship to a given agent 
- search using a personal name of a composer to find musical works composed by 
the person 
- search using a personal name to find works or expressions including illustrations 
by that person 
- search using a corporate body name to find reports issued by that collective 
agent 
 
To find out, discover or confirm, the extent of coverage of the database 
- search for a person by a nomen known to the user, to confirm whether the 
database contains a record for the person 
 
To find resources having an association with a particular place or time-span 
- search using a place name to find manifestations published in that place 
- search using a date range and a place to find works that originated in a place 
during a time-span 
 
To find resources embodying works that are in a subject relationship to a given res 
(or set of res) 
- search using a nomen (for the given res) that is used in the Library of Congress 
Subject Headings 
- search using a nomen (for the given res) that is established in the Dewey 
Decimal Classification 

IFLA LRM (2017-12) 
 
 98 
Table 6.1 Use Cases for User Tasks 
Task Use Cases 
- search using a personal or corporate or place name as established in the 
authority file 
Identify To identify, or recognize, among the results of a search 
- resources that embody a manifestation of the work sought, even though the title 
of those manifestations differs from the work title as searched by the user 
- resources that embody a manifestation of the work sought, even though other 
works by different creators bear a title similar to the work title as searched by the 
user 
- a personal name that corresponds to the person sought by the user, even though 
other people are identified by similar names 
- a personal name that corresponds to the person sought by the user, even though 
other names exist for that person, used in the same or in different contexts 
- a place name that corresponds to the place sought by the user, even though the 
place is known by names in more than one language 
 
To identify, among the results of a search, those resources intended for a specific 
audience or purpose 
- recognize that a resource, although it concerns the subject of interest, is intended 
for young children and not university students 
- recognize that a resource, although it embodies a musical work of interest, is a 
notated expression and not recorded sound 
 
To identify 
- a subject term that corresponds to the res sought, even though the term searched 
by the user has homonyms in natural language 
- a classification number that corresponds to the res sought 
Select To select, from among the resources identified, manifestations of the work or 
works sought that 
- include the most relevant additional content (such as, including original and 
translated expressions of a play in the same manifestation) 
- include a secondary contribution by a particular agent (such as, translation by a 
particular translator, critical notes or introduction by a particular scholar) 
- are in the most convenient physical format for the user’s present purpose (such 
as, easy to carry pocket book for leisure reading, compact water-resistant city map 
for travel) 
- are in a medium that can be used by the user (such as, an audio book, in braille 
or in large print, DVD or Blu-ray) 
- are available in the user’s location (a copy is present in the user’s local library 
and is not presently borrowed) 
- are available for the type of use the user intends (such as, a copy that can be 
used outside of the library exists, public performance rights are associated with a 
copy of a video so that the user can show it in a classroom setting) 
 
To select, from among the resources identified through a subject search, those 
resources that seem the most relevant 
- due to the aspects or facets or approach to the subject described 

IFLA LRM (2017-12) 
 
 99 
Table 6.1 Use Cases for User Tasks 
Task Use Cases 
- due to the language of the content 
- due to the intended audience (for example, to select introductory texts for 
undergraduate use, but instead select popularizations for recreational reading) 
- due to the date of creation of the content (for example, to select recently written 
works for an information need for state-of-the-art current information, but instead 
select works created in the 1800s (regardless of the date of publication of the 
manifestation) if the information need is to understand how the subject was 
perceived at that time) 
Obtain To obtain a resource by: 
- linking to or downloading an online resource using the link found in the library 
catalogue 
- physically borrowing an item determined to be available from a local library 
- receiving an item through interlibrary loan from a more distant library or 
supplier 
- purchasing an item from a vendor or supplier using the citation information 
verified through the library catalogue or national bibliography 
 
To obtain information about an entity itself from the information recorded in 
authority data 
- obtain date and location of birth and death of a person from the authority data 
- confirm the country in which a city is located 
Explore To explore relationships in order to understand the structure of a subject domain 
and its terminology 
- browse the concepts presented as being narrower than a starting subject 
 
To explore the relationships between different instances of an entity 
- follow the derivation relationships between a progenitor work and other works 
based on it or adapted from it 
- browse the works and expressions associated with a given agent and the roles 
played by that agent in their creation or realization 
 
To understand the relationships between various nomens for an instance of an 
entity 
- examine the variant names for a topical subject within a subject vocabulary 
- survey the variant names used by a specific person in different contexts of use 
(such as name used in religion; official name) 
- view the names used by an international corporate body in different languages 
- explore correlations between nomens for the same instance of an entity in 
different controlled vocabularies (such as finding a classification number that 
corresponds to a subject heading or term) 
 
 
  

IFLA LRM (2017-12) 
 
 100 
 Glossary of Modelling Terminology 
Attribute A type of data which characterizes specific instances of an entity 
Cardinality Specification of the number of instances of the domain and range entities that 
may be connected by the specific relationship 
Disjoint Entirely non-overlapping sets. Disjoint entities can have no instance that is 
simultaneously an instance of more than one of these entities 
Domain The source entity, or departure point, for a relationship 
Enhanced 
entity-
relationship 
model 
Entity-relationship model that incorporates the notion of inheritance of 
attributes and relationships from an entity to all the entities that are subsumed 
in it 
Entity An abstract class of conceptual objects, representing the key objects of interest 
in the model 
Instance A specific exemplar of an entity 
Inverse The logical complement of a relationship, which traverses from the range to 
the domain 
Multivalued Attributes that can have more than one value for a specific instance of an 
entity 
Path Traversing two or more relationships in sequence 
Property An attribute or relationship of an entity 
Range The target entity, or arrival point, for a relationship 
Reciprocal see Inverse 
Recursive A relationship for which the same entity serves as both domain and range 
Reification Process through which a relationship is modelled as an entity, so that it can in 
turn have its own attributes and relationships 
Relationship A connection between instances of entities 
Shortcut A single relationship which serves to represent a more developed path 
consisting of two or more relationships 
Subclass An entity, all of whose instances are also instances of a larger, superordinate 
entity 
Symmetric A relationship for which the relationship name is the same as the name of the 
inverse relationship 
Universe of 
discourse 
Everything considered relevant in the domain that is being modelled 
 
  

IFLA LRM (2017-12) 
 
 101 
 Conceptual Models Consulted 
(Aggregates WG) Final report of the Working Group on Aggregates / chair, Ed O’Neill. September 12, 
2011. Available at: http://www.ifla.org/files/assets/cataloguing/frbrrg/AggregatesFinalReport.pdf 
(accessed 2017-08-01) 
 
(CIDOC CRM 6.2.2) Definition of the CIDOC Conceptual Reference Model / produced by the 
ICOM/CIDOC Documentation Standards Group, continued by the CIDOC CRM Special Interest 
Group ; current main editors: Patrick Le Bœuf, Martin Doerr, Christian Emil Ore, Stephen Stead. 
Version 6.2.2. January 2017. Available at: http://www.cidoc-crm.org/sites/default/files/2017-01-
25%23CIDOC%20CRM_v6.2.2_esIP.pdf (accessed 2017-08-01) 
 
(FRBROO 2.4) Definition of FRBRoo : a conceptual model for bibliographic information in object-
oriented formalism / International Working Group on FRBR and CIDOC CRM Harmonisation ; editors: 
Chryssoula Bekiari, Martin Doerr, Patrick Le Bœuf, Pat Riva. Version 2.4. November 2015. Available at: 
http://www.ifla.org/files/assets/cataloguing/FRBRoo/frbroo_v_2.4.pdf (accessed 2017-08-01) and as 
FRBR : object-oriented definition and mapping from FRBRER, FRAD and FRSAD, at: 
http://www.cidoc-crm.org/frbroo/sites/default/files/FRBRoo_V2.4.pdf (accessed 2017-08-01) 
 
(FRAD) Functional requirements for authority data : a conceptual model / edited by Glenn E. Patton, 
IFLA Working Group on Functional Requirements and Numbering of Authority Records (FRANAR). 
München : K.G. Saur, 2009. (IFLA series on bibliographic control ; vol. 34). As amended and corrected 
through July 2013. Available at: http://www.ifla.org/files/assets/cataloguing/frad/frad_2013.pdf 
(accessed 2017-08-01) 
 
(FRBR) Functional requirements for bibliographic records : final report / IFLA Study Group on the 
Functional Requirements for Bibliographic Records. München : K.G. Saur, 1998. (UBCIM publications ; 
new series, vol. 19). As amended and corrected through February 2009. Available at: 
http://www.ifla.org/files/assets/cataloguing/frbr/frbr_2008.pdf (accessed 2017-08-01) 
 
(FRSAD) Functional requirements for subject authority data (FRSAD) : a conceptual model / edited by 
Marcia Lei Zeng, Maja Žumer and Athena Salaba. München : De Gruyter Saur, 2011. (IFLA series on 
bibliographic control ; vol. 43). Available at: http://www.ifla.org/files/assets/classification-and-
indexing/functional-requirements-for-subject-authority-data/frsad-final-report.pdf (accessed 2017-08-01). 
Errata for section 5.4.2, October 2011, available at: 
http://www.ifla.org/files/assets/cataloguing/frsad/FRSADerrata2011.pdf (accessed 2017-08-01) 
 
(PRESSOO) PRESSOO : extension of CIDOC CRM and FRBROO for the modelling of bibliographic 
information pertaining to continuing resources / editor: Patrick Le Bœuf. Version 1.2. January 2016. 
Available at: http://www.ifla.org/files/assets/cataloguing/PRESSoo/pressoo_v1.2.pdf and at: 
http://www.cidoc-crm.org/pressoo/sites/default/files/pressoo_v1.2.pdf (accessed 2017-08-01) 
 
Transition mappings : user tasks, entities, attributes, and relationships in FRBR, FRAD, and FRSAD 
mapped to their equivalents in the IFLA Library Reference Model / Pat Riva, Patrick Le Bœuf and Maja 
Žumer. 2017. Available at: https://www.ifla.org/publications/node/11412 (accessed 2017-08-01) 
 