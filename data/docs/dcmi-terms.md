# DCMI Metadata Terms (text extract)

Source: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ (CC BY 4.0)

DCMI: DCMI Metadata Terms

Dublin Core

Open menu

DCMI-2026 Conference

###

Bluesky

Twitter

YouTube

GitHub

RSS Feed

Close menu

About DCMI

Themes

Members

Governing Board

Usage Board

Directorate

DCMI 2026 Conference

Bluesky

Twitter

YouTube

GitHub

RSS Feed

Go to...

Home

Dublin Core™

DCMI Specifications

Skip to main content

# DCMI Metadata Terms

This document is an up-to-date specification of all metadata terms maintained by the Dublin Core Metadata Initiative, including properties, vocabulary encoding schemes, syntax encoding schemes, and classes.

Creator
DCMI Usage Board

Identifier
http://dublincore.org/specifications/dublin-core/dcmi-terms/2020-01-20/

Date Issued
2020-01-20

Latest Version

https://www.dublincore.org/specifications/dublin-core/dcmi-terms/

Version History

https://www.dublincore.org/specifications/dublin-core/dcmi-terms/release_history/

Document Status

DCMI Recommendation

##

## Index of Terms

### Properties in /terms/ namespace

abstract

accessRights

accrualMethod

accrualPeriodicity

accrualPolicy

alternative

audience

available

bibliographicCitation

conformsTo

contributor

coverage

created

creator

date

dateAccepted

dateCopyrighted

dateSubmitted

description

educationLevel

extent

format

hasFormat

hasPart

hasVersion

identifier

instructionalMethod

isFormatOf

isPartOf

isReferencedBy

isReplacedBy

isRequiredBy

issued

isVersionOf

language

license

mediator

medium

modified

provenance

publisher

references

relation

replaces

requires

rights

rightsHolder

source

spatial

subject

tableOfContents

temporal

title

type

valid

### Properties in /elements/1.1/ namespace

contributor

coverage

creator

date

description

format

identifier

language

publisher

relation

rights

source

subject

title

type

### Vocabulary Encoding Schemes

DCMIType

DDC

IMT

LCC

LCSH

MESH

NLM

TGN

UDC

### Syntax Encoding Schemes

Box

ISO3166

ISO639-2

ISO639-3

Period

Point

RFC1766

RFC3066

RFC4646

RFC5646

URI

W3CDTF

### Classes

Agent

AgentClass

BibliographicResource

FileFormat

Frequency

Jurisdiction

LicenseDocument

LinguisticSystem

Location

LocationPeriodOrJurisdiction

MediaType

MediaTypeOrExtent

MethodOfAccrual

MethodOfInstruction

PeriodOfTime

PhysicalMedium

PhysicalResource

Policy

ProvenanceStatement

RightsStatement

SizeOrDuration

Standard

### DCMI Type Vocabulary

Collection

Dataset

Event

Image

InteractiveResource

MovingImage

PhysicalObject

Service

Software

Sound

StillImage

Text

### Terms for vocabulary description

domainIncludes

memberOf

rangeIncludes

VocabularyEncodingScheme

##
Section 1: Introduction and Definitions

This document is an up-to-date, authoritative specification of all metadata terms maintained by the Dublin Core™ Metadata Initiative. Included are the fifteen terms of the Dublin Core™ Metadata Element Set (also known as "the Dublin Core") plus several dozen properties, classes, datatypes, and vocabulary encoding schemes. The "Dublin Core" plus these extension vocabularies are collectively referred to as "DCMI metadata terms" ("Dublin Core terms" for short). These terms are intended to be used in combination with metadata terms from other, compatible vocabularies in the context of application profiles.

DCMI metadata terms are expressed in RDF vocabularies for use in Linked Data. Creators of non-RDF metadata can use the terms in contexts such as XML, JSON, UML, or relational databases by disregarding both the global identifier and the formal implications of the RDF-specific aspects of term definitions. Such users can take domain, range, subproperty, and subclass relations as usage suggestions and focus on the natural-language text of definitions, usage notes, and examples.

Each term is identified with a Uniform Resource Identifier (URI), a global identifier usable in Linked Data. Term URIs resolve to the (DCMI Metadata Terms) document when selected in a browser or, when referenced programmatically by RDF applications, to one of four RDF schemas. The scope of each RDF schema corresponds to a "DCMI namespace", or set of DCMI metadata terms that are identified using a common base URI, as enumerated in the DCMI Namespace Policy. In Linked Data, the URIs for DCMI namespaces are often declared as prefixes in order to make data, queries, and schemas more concise and readable.

The four DCMI namespaces are:

http://purl.org/dc/elements/1.1/ The /elements/1.1/ namespace was created in 2000 for the RDF representation of the fifteen-element Dublin Core and has been widely used in data for more than twenty years. This namespace corresponds to the original scope of ISO 15836, which was published first in 2003 and last revised in 2017 as ISO 15836-1:2017 [ISO 15836-1:2017.

http://purl.org/dc/terms/ The /terms/ namespace was originally created in 2001 for identifying new terms coined outside of the original fifteen-element Dublin Core. In 2008, in the context of defining formal semantic constraints for DCMI metadata terms in support of RDF applications, the original fifteen elements themselves were mirrored in the /terms/ namespace. As a result, there exists both a dc:date (http://purl.org/dc/elements/1.1/date) with no formal range and a corresponding dcterms:date (http://purl.org/dc/terms/date) with a formal range of "literal". While these distinctions are significant for creators of RDF applications, most users can safely treat the fifteen parallel properties as equivalent. The most useful properties and classes of DCMI Metadata Terms have now been published as ISO 15836-2:2019 [ISO 15836-2:2019]. While the /elements/1.1/ namespace will be supported indefinitely, DCMI gently encourages use of the /terms/ namespace.

http://purl.org/dc/dcmitype/ The /dcmitype/ namespace was created in 2001 for the DCMI Type Vocabulary, which defines classes for basic types of thing that can be described using DCMI metadata terms.

http://purl.org/dc/dcam/ The /dcam/ namespace was created in 2008 for terms used in the description of DCMI metadata terms.

Each term is specified with the following minimal set of attributes:

Minimal Attributes

Name
A token appended to the URI of a DCMI namespace to create the URI of the term.

Label
The human-readable label assigned to the term.

URI
The Uniform Resource Identifier used to uniquely identify a term.

Definition
A statement that represents the concept and essential nature of the term.

Type of Term
The type of term: property, class, datatype, or vocabulary encoding scheme.

Where applicable, the following attributes provide additional information about a term:

Additional Attributes

Comment
Additional information about the term or its application.

See
Authoritative documentation related to the term.

Subproperty Of
A property of which the described term is a sub-property.

Superclass Of
A class of which the described term is a super-class.

Subclass Of
A class of which the described term is a sub-class.

Domain
A class of which a resource described by the term is an instance.

Domain Includes
A suggested class for subjects of this property.

Range
A class of which a value described by the term is an instance.

Range Includes
A suggested class for values of this property.

Member Of
An enumerated set of resources (Vocabulary Encoding Scheme) of which the term is a member.

Instance Of
A class of which the described term is an instance.

Equivalent Property
A property to which the described term is equivalent.

#### References

References

[ISO 15836-1:2017]

https://www.iso.org/standard/71339.html

[ISO 15836-2:2019]

https://www.iso.org/standard/71341.html

[NAMESPACE]

http://dublincore.org/specifications/dublin-core/dcmi-namespace/

##
Section 2: Properties in the /terms/ namespace

###
abstract

Property

More details →

URI

http://purl.org/dc/terms/abstract

Label
Abstract

Definition
A summary of the resource.

Subproperty of

Description

(http://purl.org/dc/elements/1.1/description)

Description

(http://purl.org/dc/terms/description)

###
accessRights

Property

More details →

URI

http://purl.org/dc/terms/accessRights

Label
Access Rights

Definition
Information about who access the resource or an indication of its security status.

Comment
Access Rights may include information regarding access or restrictions based on privacy, security, or other policies.

Range Includes

http://purl.org/dc/terms/RightsStatement

Subproperty of

Rights

(http://purl.org/dc/elements/1.1/rights)

Rights

(http://purl.org/dc/terms/rights)

###
accrualMethod

Property

More details →

URI

http://purl.org/dc/terms/accrualMethod

Label
Accrual Method

Definition
The method by which items are added to a collection.

Comment
Recommended practice is to use a value from the Collection Description Accrual Method Vocabulary [DCMI-ACCRUALMETHOD].

Range Includes

http://purl.org/dc/terms/MethodOfAccrual

Has Domain
http://purl.org/dc/dcmitype/Collection

###
accrualPeriodicity

Property

More details →

URI

http://purl.org/dc/terms/accrualPeriodicity

Label
Accrual Periodicity

Definition
The frequency with which items are added to a collection.

Comment
Recommended practice is to use a value from the Collection Description Frequency Vocabulary [DCMI-COLLFREQ].

Range Includes

http://purl.org/dc/terms/Frequency

Has Domain
http://purl.org/dc/dcmitype/Collection

###
accrualPolicy

Property

More details →

URI

http://purl.org/dc/terms/accrualPolicy

Label
Accrual Policy

Definition
The policy governing the addition of items to a collection.

Comment
Recommended practice is to use a value from the Collection Description Accrual Policy Vocabulary [DCMI-ACCRUALPOLICY].

Range Includes

http://purl.org/dc/terms/Policy

Has Domain
http://purl.org/dc/dcmitype/Collection

###
alternative

Property

More details →

URI

http://purl.org/dc/terms/alternative

Label
Alternative Title

Definition
An alternative name for the resource.

Comment
The distinction between titles and alternative titles is application-specific.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Title

(http://purl.org/dc/elements/1.1/title)

Title

(http://purl.org/dc/terms/title)

###
audience

Property

More details →

URI

http://purl.org/dc/terms/audience

Label
Audience

Definition
A class of agents for whom the resource is intended or useful.

Comment
Recommended practice is to use this property with non-literal values from a vocabulary of audience types.

Range Includes

http://purl.org/dc/terms/AgentClass

###
available

Property

More details →

URI

http://purl.org/dc/terms/available

Label
Date Available

Definition
Date that the resource became or will become available.

Comment
Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

Date

(http://purl.org/dc/terms/date)

###
bibliographicCitation

Property

More details →

URI

http://purl.org/dc/terms/bibliographicCitation

Label
Bibliographic Citation

Definition
A bibliographic reference for the resource.

Comment
Recommended practice is to include sufficient bibliographic detail to identify the resource as unambiguously as possible.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Identifier

(http://purl.org/dc/elements/1.1/identifier)

Identifier

(http://purl.org/dc/terms/identifier)

###
conformsTo

Property

More details →

URI

http://purl.org/dc/terms/conformsTo

Label
Conforms To

Definition
An established standard to which the described resource conforms.

Range Includes

http://purl.org/dc/terms/Standard

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
contributor

Property

More details →

URI

http://purl.org/dc/terms/contributor

Label
Contributor

Definition
An entity responsible for making contributions to the resource.

Comment
The guidelines for using names of persons or organizations as creators apply to contributors.

Range Includes

http://purl.org/dc/terms/Agent

Subproperty of

Contributor

(http://purl.org/dc/elements/1.1/contributor)

###
coverage

Property

More details →

URI

http://purl.org/dc/terms/coverage

Label
Coverage

Definition
The spatial or temporal topic of the resource, spatial applicability of the resource, or jurisdiction under which the resource is relevant.

Comment
Spatial topic and spatial applicability may be a named place or a location specified by its geographic coordinates. Temporal topic may be a named period, date, or date range. A jurisdiction may be a named administrative entity or a geographic place to which the resource applies. Recommended practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names [TGN]. Where appropriate, named places or time periods may be used in preference to numeric identifiers such as sets of coordinates or date ranges. Because coverage is so broadly defined, it is preferable to use the more specific subproperties Temporal Coverage and Spatial Coverage.

Range Includes

http://purl.org/dc/terms/Location

http://purl.org/dc/terms/Period

http://purl.org/dc/terms/Jurisdiction

Subproperty of

Coverage

(http://purl.org/dc/elements/1.1/coverage)

###
created

Property

More details →

URI

http://purl.org/dc/terms/created

Label
Date Created

Definition
Date of creation of the resource.

Comment
Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

Date

(http://purl.org/dc/terms/date)

###
creator

Property

More details →

URI

http://purl.org/dc/terms/creator

Label
Creator

Definition
An entity responsible for making the resource.

Comment
Recommended practice is to identify the creator with a URI. If this is not possible or feasible, a literal value that identifies the creator may be provided.

Range Includes

http://purl.org/dc/terms/Agent

Equivalent Property

http://xmlns.com/foaf/0.1/maker

Subproperty of

Creator

(http://purl.org/dc/elements/1.1/creator)

Contributor

(http://purl.org/dc/terms/contributor)

###
date

Property

More details →

URI

http://purl.org/dc/terms/date

Label
Date

Definition
A point or period of time associated with an event in the lifecycle of the resource.

Comment
Date may be used to express temporal information at any level of granularity. Recommended practice is to express the date, date/time, or period of time according to ISO 8601-1 [ISO 8601-1] or a published profile of the ISO standard, such as the W3C Note on Date and Time Formats [W3CDTF] or the Extended Date/Time Format Specification [EDTF]. If the full date is unknown, month and year (YYYY-MM) or just year (YYYY) may be used. Date ranges may be specified using ISO 8601 period of time specification in which start and end dates are separated by a '/' (slash) character. Either the start or end date may be missing.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

###
dateAccepted

Property

More details →

URI

http://purl.org/dc/terms/dateAccepted

Label
Date Accepted

Definition
Date of acceptance of the resource.

Comment
Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty. Examples of resources to which a date of acceptance may be relevant are a thesis (accepted by a university department) or an article (accepted by a journal).

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

Date

(http://purl.org/dc/terms/date)

###
dateCopyrighted

Property

More details →

URI

http://purl.org/dc/terms/dateCopyrighted

Label
Date Copyrighted

Definition
Date of copyright of the resource.

Comment
Typically a year. Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

Date

(http://purl.org/dc/terms/date)

###
dateSubmitted

Property

More details →

URI

http://purl.org/dc/terms/dateSubmitted

Label
Date Submitted

Definition
Date of submission of the resource.

Comment
Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty. Examples of resources to which a 'Date Submitted' may be relevant include a thesis (submitted to a university department) or an article (submitted to a journal).

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

Date

(http://purl.org/dc/terms/date)

###
description

Property

More details →

URI

http://purl.org/dc/terms/description

Label
Description

Definition
An account of the resource.

Comment
Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.

Subproperty of

Description

(http://purl.org/dc/elements/1.1/description)

###
educationLevel

Property

More details →

URI

http://purl.org/dc/terms/educationLevel

Label
Audience Education Level

Definition
A class of agents, defined in terms of progression through an educational or training context, for which the described resource is intended.

Range Includes

http://purl.org/dc/terms/AgentClass

Subproperty of

Audience

(http://purl.org/dc/terms/audience)

###
extent

Property

More details →

URI

http://purl.org/dc/terms/extent

Label
Extent

Definition
The size or duration of the resource.

Comment
Recommended practice is to specify the file size in megabytes and duration in ISO 8601 format.

Range Includes

http://purl.org/dc/terms/SizeOrDuration

Subproperty of

Format

(http://purl.org/dc/elements/1.1/format)

Format

(http://purl.org/dc/terms/format)

###
format

Property

More details →

URI

http://purl.org/dc/terms/format

Label
Format

Definition
The file format, physical medium, or dimensions of the resource.

Comment
Recommended practice is to use a controlled vocabulary where available. For example, for file formats one could use the list of Internet Media Types [MIME]. Examples of dimensions include size and duration.

Range Includes

http://purl.org/dc/terms/MediaType

http://purl.org/dc/terms/Extent

Subproperty of

Format

(http://purl.org/dc/elements/1.1/format)

###
hasFormat

Property

More details →

URI

http://purl.org/dc/terms/hasFormat

Label
Has Format

Definition
A related resource that is substantially the same as the pre-existing described resource, but in another format.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Is Format Of.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
hasPart

Property

More details →

URI

http://purl.org/dc/terms/hasPart

Label
Has Part

Definition
A related resource that is included either physically or logically in the described resource.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Is Part Of.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
hasVersion

Property

More details →

URI

http://purl.org/dc/terms/hasVersion

Label
Has Version

Definition
A related resource that is a version, edition, or adaptation of the described resource.

Comment
Changes in version imply substantive changes in content rather than differences in format. This property is intended to be used with non-literal values. This property is an inverse property of Is Version Of.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
identifier

Property

More details →

URI

http://purl.org/dc/terms/identifier

Label
Identifier

Definition
An unambiguous reference to the resource within a given context.

Comment
Recommended practice is to identify the resource by means of a string conforming to an identification system. Examples include International Standard Book Number (ISBN), Digital Object Identifier (DOI), and Uniform Resource Name (URN). Persistent identifiers should be provided as HTTP URIs.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Identifier

(http://purl.org/dc/elements/1.1/identifier)

###
instructionalMethod

Property

More details →

URI

http://purl.org/dc/terms/instructionalMethod

Label
Instructional Method

Definition
A process, used to engender knowledge, attitudes and skills, that the described resource is designed to support.

Comment
Instructional Method typically includes ways of presenting instructional materials or conducting instructional activities, patterns of learner-to-learner and learner-to-instructor interactions, and mechanisms by which group and individual levels of learning are measured. Instructional methods include all aspects of the instruction and learning processes from planning and implementation through evaluation and feedback.

Range Includes

http://purl.org/dc/terms/MethodOfInstruction

###
isFormatOf

Property

More details →

URI

http://purl.org/dc/terms/isFormatOf

Label
Is Format Of

Definition
A pre-existing related resource that is substantially the same as the described resource, but in another format.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Has Format.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
isPartOf

Property

More details →

URI

http://purl.org/dc/terms/isPartOf

Label
Is Part Of

Definition
A related resource in which the described resource is physically or logically included.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Has Part.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
isReferencedBy

Property

More details →

URI

http://purl.org/dc/terms/isReferencedBy

Label
Is Referenced By

Definition
A related resource that references, cites, or otherwise points to the described resource.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of References.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
isReplacedBy

Property

More details →

URI

http://purl.org/dc/terms/isReplacedBy

Label
Is Replaced By

Definition
A related resource that supplants, displaces, or supersedes the described resource.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Replaces.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
isRequiredBy

Property

More details →

URI

http://purl.org/dc/terms/isRequiredBy

Label
Is Required By

Definition
A related resource that requires the described resource to support its function, delivery, or coherence.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Requires.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
issued

Property

More details →

URI

http://purl.org/dc/terms/issued

Label
Date Issued

Definition
Date of formal issuance of the resource.

Comment
Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

Date

(http://purl.org/dc/terms/date)

###
isVersionOf

Property

More details →

URI

http://purl.org/dc/terms/isVersionOf

Label
Is Version Of

Definition
A related resource of which the described resource is a version, edition, or adaptation.

Comment
Changes in version imply substantive changes in content rather than differences in format. This property is intended to be used with non-literal values. This property is an inverse property of Has Version.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
language

Property

More details →

URI

http://purl.org/dc/terms/language

Label
Language

Definition
A language of the resource.

Comment
Recommended practice is to use either a non-literal value representing a language from a controlled vocabulary such as ISO 639-2 or ISO 639-3, or a literal value consisting of an IETF Best Current Practice 47 [IETF-BCP47] language tag.

Range Includes

http://purl.org/dc/terms/LinguisticSystem

Subproperty of

Language

(http://purl.org/dc/elements/1.1/language)

###
license

Property

More details →

URI

http://purl.org/dc/terms/license

Label
License

Definition
A legal document giving official permission to do something with the resource.

Comment
Recommended practice is to identify the license document with a URI. If this is not possible or feasible, a literal value that identifies the license may be provided.

Range Includes

http://purl.org/dc/terms/LicenseDocument

Subproperty of

Rights

(http://purl.org/dc/elements/1.1/rights)

Rights

(http://purl.org/dc/terms/rights)

###
mediator

Property

More details →

URI

http://purl.org/dc/terms/mediator

Label
Mediator

Definition
An entity that mediates access to the resource.

Comment
In an educational context, a mediator might be a parent, teacher, teaching assistant, or care-giver.

Range Includes

http://purl.org/dc/terms/AgentClass

Subproperty of

Audience

(http://purl.org/dc/terms/audience)

###
medium

Property

More details →

URI

http://purl.org/dc/terms/medium

Label
Medium

Definition
The material or physical carrier of the resource.

Range Includes

http://purl.org/dc/terms/PhysicalMedium

Domain Includes

http://purl.org/dc/terms/PhysicalResource

Subproperty of

Format

(http://purl.org/dc/elements/1.1/format)

Format

(http://purl.org/dc/terms/format)

###
modified

Property

More details →

URI

http://purl.org/dc/terms/modified

Label
Date Modified

Definition
Date on which the resource was changed.

Comment
Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

Date

(http://purl.org/dc/terms/date)

###
provenance

Property

More details →

URI

http://purl.org/dc/terms/provenance

Label
Provenance

Definition
A statement of any changes in ownership and custody of the resource since its creation that are significant for its authenticity, integrity, and interpretation.

Comment
The statement may include a description of any changes successive custodians made to the resource.

Range Includes

http://purl.org/dc/terms/ProvenanceStatement

###
publisher

Property

More details →

URI

http://purl.org/dc/terms/publisher

Label
Publisher

Definition
An entity responsible for making the resource available.

Range Includes

http://purl.org/dc/terms/Agent

Subproperty of

Publisher

(http://purl.org/dc/elements/1.1/publisher)

###
references

Property

More details →

URI

http://purl.org/dc/terms/references

Label
References

Definition
A related resource that is referenced, cited, or otherwise pointed to by the described resource.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Is Referenced By.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
relation

Property

More details →

URI

http://purl.org/dc/terms/relation

Label
Relation

Definition
A related resource.

Comment
Recommended practice is to identify the related resource by means of a URI. If this is not possible or feasible, a string conforming to a formal identification system may be provided.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

###
replaces

Property

More details →

URI

http://purl.org/dc/terms/replaces

Label
Replaces

Definition
A related resource that is supplanted, displaced, or superseded by the described resource.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Is Replaced By.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
requires

Property

More details →

URI

http://purl.org/dc/terms/requires

Label
Requires

Definition
A related resource that is required by the described resource to support its function, delivery, or coherence.

Comment
This property is intended to be used with non-literal values. This property is an inverse property of Is Required By.

Subproperty of

Relation

(http://purl.org/dc/elements/1.1/relation)

Relation

(http://purl.org/dc/terms/relation)

###
rights

Property

More details →

URI

http://purl.org/dc/terms/rights

Label
Rights

Definition
Information about rights held in and over the resource.

Comment
Typically, rights information includes a statement about various property rights associated with the resource, including intellectual property rights. Recommended practice is to refer to a rights statement with a URI. If this is not possible or feasible, a literal value (name, label, or short text) may be provided.

Range Includes

http://purl.org/dc/terms/RightsStatement

Subproperty of

Rights

(http://purl.org/dc/elements/1.1/rights)

###
rightsHolder

Property

More details →

URI

http://purl.org/dc/terms/rightsHolder

Label
Rights Holder

Definition
A person or organization owning or managing rights over the resource.

Comment
Recommended practice is to refer to the rights holder with a URI. If this is not possible or feasible, a literal value that identifies the rights holder may be provided.

Range Includes

http://purl.org/dc/terms/Agent

###
source

Property

More details →

URI

http://purl.org/dc/terms/source

Label
Source

Definition
A related resource from which the described resource is derived.

Comment
This property is intended to be used with non-literal values. The described resource may be derived from the related resource in whole or in part. Best practice is to identify the related resource by means of a URI or a string conforming to a formal identification system.

Subproperty of

Source

(http://purl.org/dc/elements/1.1/source)

Relation

(http://purl.org/dc/terms/relation)

###
spatial

Property

More details →

URI

http://purl.org/dc/terms/spatial

Label
Spatial Coverage

Definition
Spatial characteristics of the resource.

Range Includes

http://purl.org/dc/terms/Location

Subproperty of

Coverage

(http://purl.org/dc/elements/1.1/coverage)

Coverage

(http://purl.org/dc/terms/coverage)

###
subject

Property

More details →

URI

http://purl.org/dc/terms/subject

Label
Subject

Definition
A topic of the resource.

Comment
Recommended practice is to refer to the subject with a URI. If this is not possible or feasible, a literal value that identifies the subject may be provided. Both should preferably refer to a subject in a controlled vocabulary.

Subproperty of

Subject

(http://purl.org/dc/elements/1.1/subject)

###
tableOfContents

Property

More details →

URI

http://purl.org/dc/terms/tableOfContents

Label
Table Of Contents

Definition
A list of subunits of the resource.

Subproperty of

Description

(http://purl.org/dc/elements/1.1/description)

Description

(http://purl.org/dc/terms/description)

###
temporal

Property

More details →

URI

http://purl.org/dc/terms/temporal

Label
Temporal Coverage

Definition
Temporal characteristics of the resource.

Range Includes

http://purl.org/dc/terms/PeriodOfTime

Subproperty of

Coverage

(http://purl.org/dc/elements/1.1/coverage)

Coverage

(http://purl.org/dc/terms/coverage)

###
title

Property

More details →

URI

http://purl.org/dc/terms/title

Label
Title

Definition
A name given to the resource.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Title

(http://purl.org/dc/elements/1.1/title)

###
type

Property

More details →

URI

http://purl.org/dc/terms/type

Label
Type

Definition
The nature or genre of the resource.

Comment
Recommended practice is to use a controlled vocabulary such as the DCMI Type Vocabulary [DCMI-TYPE]. To describe the file format, physical medium, or dimensions of the resource, use the property Format.

Subproperty of

Type

(http://purl.org/dc/elements/1.1/type)

###
valid

Property

More details →

URI

http://purl.org/dc/terms/valid

Label
Date Valid

Definition
Date (often a range) of validity of a resource.

Comment
Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty.

Has Range
http://www.w3.org/2000/01/rdf-schema#Literal

Subproperty of

Date

(http://purl.org/dc/elements/1.1/date)

Date

(http://purl.org/dc/terms/date)

##
Section 3: Properties in the /elements/1.1/ namespace

###
contributor

Property

More details →

URI

http://purl.org/dc/elements/1.1/contributor

Label
Contributor

Definition
An entity responsible for making contributions to the resource.

Comment
The guidelines for using names of persons or organizations as creators also apply to contributors. Typically, the name of a Contributor should be used to indicate the entity.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
coverage

Property

More details →

URI

http://purl.org/dc/elements/1.1/coverage

Label
Coverage

Definition
The spatial or temporal topic of the resource, spatial applicability of the resource, or jurisdiction under which the resource is relevant.

Comment
Spatial topic and spatial applicability may be a named place or a location specified by its geographic coordinates. Temporal topic may be a named period, date, or date range. A jurisdiction may be a named administrative entity or a geographic place to which the resource applies. Recommended practice is to use a controlled vocabulary such as the Getty Thesaurus of Geographic Names [TGN]. Where appropriate, named places or time periods may be used in preference to numeric identifiers such as sets of coordinates or date ranges.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
creator

Property

More details →

URI

http://purl.org/dc/elements/1.1/creator

Label
Creator

Definition
An entity primarily responsible for making the resource.

Comment
Examples of a Creator include a person, an organization, or a service. Typically, the name of a Creator should be used to indicate the entity.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
date

Property

More details →

URI

http://purl.org/dc/elements/1.1/date

Label
Date

Definition
A point or period of time associated with an event in the lifecycle of the resource.

Comment
Date may be used to express temporal information at any level of granularity. Recommended practice is to express the date, date/time, or period of time according to ISO 8601-1 [ISO 8601-1] or a published profile of the ISO standard, such as the W3C Note on Date and Time Formats [W3CDTF] or the Extended Date/Time Format Specification [EDTF]. If the full date is unknown, month and year (YYYY-MM) or just year (YYYY) may be used. Date ranges may be specified using ISO 8601 period of time specification in which start and end dates are separated by a '/' (slash) character. Either the start or end date may be missing.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
description

Property

More details →

URI

http://purl.org/dc/elements/1.1/description

Label
Description

Definition
An account of the resource.

Comment
Description may include but is not limited to: an abstract, a table of contents, a graphical representation, or a free-text account of the resource.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
format

Property

More details →

URI

http://purl.org/dc/elements/1.1/format

Label
Format

Definition
The file format, physical medium, or dimensions of the resource.

Comment
Recommended practice is to use a controlled vocabulary where available. For example, for file formats one could use the list of Internet Media Types [MIME].

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
identifier

Property

More details →

URI

http://purl.org/dc/elements/1.1/identifier

Label
Identifier

Definition
An unambiguous reference to the resource within a given context.

Comment
Recommended practice is to identify the resource by means of a string conforming to an identification system.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
language

Property

More details →

URI

http://purl.org/dc/elements/1.1/language

Label
Language

Definition
A language of the resource.

Comment
Recommended practice is to use either a non-literal value representing a language from a controlled vocabulary such as ISO 639-2 or ISO 639-3, or a literal value consisting of an IETF Best Current Practice 47 [IETF-BCP47] language tag.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
publisher

Property

More details →

URI

http://purl.org/dc/elements/1.1/publisher

Label
Publisher

Definition
An entity responsible for making the resource available.

Comment
Examples of a Publisher include a person, an organization, or a service. Typically, the name of a Publisher should be used to indicate the entity.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
relation

Property

More details →

URI

http://purl.org/dc/elements/1.1/relation

Label
Relation

Definition
A related resource.

Comment
Recommended practice is to identify the related resource by means of a URI. If this is not possible or feasible, a string conforming to a formal identification system may be provided.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
rights

Property

More details →

URI

http://purl.org/dc/elements/1.1/rights

Label
Rights

Definition
Information about rights held in and over the resource.

Comment
Typically, rights information includes a statement about various property rights associated with the resource, including intellectual property rights.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
source

Property

More details →

URI

http://purl.org/dc/elements/1.1/source

Label
Source

Definition
A related resource from which the described resource is derived.

Comment
The described resource may be derived from the related resource in whole or in part. Recommended best practice is to identify the related resource by means of a string conforming to a formal identification system.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
subject

Property

More details →

URI

http://purl.org/dc/elements/1.1/subject

Label
Subject

Definition
The topic of the resource.

Comment
Typically, the subject will be represented using keywords, key phrases, or classification codes. Recommended best practice is to use a controlled vocabulary.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
title

Property

More details →

URI

http://purl.org/dc/elements/1.1/title

Label
Title

Definition
A name given to the resource.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

###
type

Property

More details →

URI

http://purl.org/dc/elements/1.1/type

Label
Type

Definition
The nature or genre of the resource.

Comment
Recommended practice is to use a controlled vocabulary such as the DCMI Type Vocabulary [DCMI-TYPE]. To describe the file format, physical medium, or dimensions of the resource, use the Format element.

Note
A second property with the same name as this property has been declared in the dcterms: namespace. See the Introduction to the document DCMI Metadata Terms for an explanation.

##
Section 4: Vocabulary Encoding Schemes

###
DCMIType

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/DCMIType

Label
DCMI Type Vocabulary

Definition
The set of classes specified by the DCMI Type Vocabulary, used to categorize the nature or genre of the resource.

See

http://purl.org/dc/dcmitype/

###
DDC

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/DDC

Label
DDC

Definition
The set of conceptual resources specified by the Dewey Decimal Classification.

See

http://www.oclc.org/dewey/

###
IMT

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/IMT

Label
IMT

Definition
The set of media types specified by the Internet Assigned Numbers Authority.

See

http://www.iana.org/assignments/media-types/

###
LCC

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/LCC

Label
LCC

Definition
The set of conceptual resources specified by the Library of Congress Classification.

See

http://lcweb.loc.gov/catdir/cpso/lcco/lcco.html

###
LCSH

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/LCSH

Label
LCSH

Definition
The set of labeled concepts specified by the Library of Congress Subject Headings.

###
MESH

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/MESH

Label
MeSH

Definition
The set of labeled concepts specified by the Medical Subject Headings.

See

http://www.nlm.nih.gov/mesh/meshhome.html

###
NLM

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/NLM

Label
NLM

Definition
The set of conceptual resources specified by the National Library of Medicine Classification.

See

http://wwwcf.nlm.nih.gov/class/

###
TGN

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/TGN

Label
TGN

Definition
The set of places specified by the Getty Thesaurus of Geographic Names.

See

http://www.getty.edu/research/tools/vocabulary/tgn/index.html

###
UDC

Vocabulary Encoding Scheme

More details →

URI

http://purl.org/dc/terms/UDC

Label
UDC

Definition
The set of conceptual resources specified by the Universal Decimal Classification.

See

http://www.udcc.org/

##
Section 5: Syntax Encoding Schemes

###
Box

Datatype

More details →

URI

http://purl.org/dc/terms/Box

Label
DCMI Box

Definition
The set of regions in space defined by their geographic coordinates according to the DCMI Box Encoding Scheme.

See

https://www.dublincore.org/specifications/dublin-core/dcmi-box/

###
ISO3166

Datatype

More details →

URI

http://purl.org/dc/terms/ISO3166

Label
ISO 3166

Definition
The set of codes listed in ISO 3166-1 for the representation of names of countries.

See

https://www.iso.org/obp/ui/#search

###
ISO639-2

Datatype

More details →

URI

http://purl.org/dc/terms/ISO639-2

Label
ISO 639-2

Definition
The three-letter alphabetic codes listed in ISO639-2 for the representation of names of languages.

See

http://lcweb.loc.gov/standards/iso639-2/langhome.html

###
ISO639-3

Datatype

More details →

URI

http://purl.org/dc/terms/ISO639-3

Label
ISO 639-3

Definition
The set of three-letter codes listed in ISO 639-3 for the representation of names of languages.

See

http://www.sil.org/iso639-3/

###
Period

Datatype

More details →

URI

http://purl.org/dc/terms/Period

Label
DCMI Period

Definition
The set of time intervals defined by their limits according to the DCMI Period Encoding Scheme.

See

https://www.dublincore.org/specifications/dublin-core/dcmi-period/

###
Point

Datatype

More details →

URI

http://purl.org/dc/terms/Point

Label
DCMI Point

Definition
The set of points in space defined by their geographic coordinates according to the DCMI Point Encoding Scheme.

See

https://www.dublincore.org/specifications/dublin-core/dcmi-point/

###
RFC1766

Datatype

More details →

URI

http://purl.org/dc/terms/RFC1766

Label
RFC 1766

Definition
The set of tags, constructed according to RFC 1766, for the identification of languages.

See

http://www.ietf.org/rfc/rfc1766.txt

###
RFC3066

Datatype

More details →

URI

http://purl.org/dc/terms/RFC3066

Label
RFC 3066

Definition
The set of tags constructed according to RFC 3066 for the identification of languages.

Comment
RFC 3066 has been obsoleted by RFC 4646.

See

http://www.ietf.org/rfc/rfc3066.txt

###
RFC4646

Datatype

More details →

URI

http://purl.org/dc/terms/RFC4646

Label
RFC 4646

Definition
The set of tags constructed according to RFC 4646 for the identification of languages.

Comment
RFC 4646 obsoletes RFC 3066.

See

http://www.ietf.org/rfc/rfc4646.txt

###
RFC5646

Datatype

More details →

URI

http://purl.org/dc/terms/RFC5646

Label
RFC 5646

Definition
The set of tags constructed according to RFC 5646 for the identification of languages.

Comment
RFC 5646 obsoletes RFC 4646.

See

http://www.ietf.org/rfc/rfc5646.txt

###
URI

Datatype

More details →

URI

http://purl.org/dc/terms/URI

Label
URI

Definition
The set of identifiers constructed according to the generic syntax for Uniform Resource Identifiers as specified by the Internet Engineering Task Force.

See

http://www.ietf.org/rfc/rfc3986.txt

###
W3CDTF

Datatype

More details →

URI

http://purl.org/dc/terms/W3CDTF

Label
W3C-DTF

Definition
The set of dates and times constructed according to the W3C Date and Time Formats Specification.

See

http://www.w3.org/TR/NOTE-datetime

##
Section 6: Classes

###
Agent

Class

More details →

URI

http://purl.org/dc/terms/Agent

Label
Agent

Definition
A resource that acts or has the power to act.

Instance Of

http://purl.org/dc/terms/AgentClass

###
AgentClass

Class

More details →

URI

http://purl.org/dc/terms/AgentClass

Label
Agent Class

Definition
A group of agents.

Subclass of

http://www.w3.org/2000/01/rdf-schema#Class

###
BibliographicResource

Class

More details →

URI

http://purl.org/dc/terms/BibliographicResource

Label
Bibliographic Resource

Definition
A book, article, or other documentary resource.

###
FileFormat

Class

More details →

URI

http://purl.org/dc/terms/FileFormat

Label
File Format

Definition
A digital resource format.

Subclass of

http://purl.org/dc/terms/MediaType

###
Frequency

Class

More details →

URI

http://purl.org/dc/terms/Frequency

Label
Frequency

Definition
A rate at which something recurs.

###
Jurisdiction

Class

More details →

URI

http://purl.org/dc/terms/Jurisdiction

Label
Jurisdiction

Definition
The extent or range of judicial, law enforcement, or other authority.

Subclass of

http://purl.org/dc/terms/LocationPeriodOrJurisdiction

###
LicenseDocument

Class

More details →

URI

http://purl.org/dc/terms/LicenseDocument

Label
License Document

Definition
A legal document giving official permission to do something with a resource.

Subclass of

http://purl.org/dc/terms/RightsStatement

###
LinguisticSystem

Class

More details →

URI

http://purl.org/dc/terms/LinguisticSystem

Label
Linguistic System

Definition
A system of signs, symbols, sounds, gestures, or rules used in communication.

Comment
Written, spoken, sign, and computer languages are linguistic systems.

###
Location

Class

More details →

URI

http://purl.org/dc/terms/Location

Label
Location

Definition
A spatial region or named place.

Subclass of

http://purl.org/dc/terms/LocationPeriodOrJurisdiction

###
LocationPeriodOrJurisdiction

Class

More details →

URI

http://purl.org/dc/terms/LocationPeriodOrJurisdiction

Label
Location, Period, or Jurisdiction

Definition
A location, period of time, or jurisdiction.

###
MediaType

Class

More details →

URI

http://purl.org/dc/terms/MediaType

Label
Media Type

Definition
A file format or physical medium.

Subclass of

http://purl.org/dc/terms/MediaTypeOrExtent

###
MediaTypeOrExtent

Class

More details →

URI

http://purl.org/dc/terms/MediaTypeOrExtent

Label
Media Type or Extent

Definition
A media type or extent.

###
MethodOfAccrual

Class

More details →

URI

http://purl.org/dc/terms/MethodOfAccrual

Label
Method of Accrual

Definition
A method by which resources are added to a collection.

###
MethodOfInstruction

Class

More details →

URI

http://purl.org/dc/terms/MethodOfInstruction

Label
Method of Instruction

Definition
A process that is used to engender knowledge, attitudes, and skills.

###
PeriodOfTime

Class

More details →

URI

http://purl.org/dc/terms/PeriodOfTime

Label
Period of Time

Definition
An interval of time that is named or defined by its start and end dates.

Subclass of

http://purl.org/dc/terms/LocationPeriodOrJurisdiction

###
PhysicalMedium

Class

More details →

URI

http://purl.org/dc/terms/PhysicalMedium

Label
Physical Medium

Definition
A physical material or carrier.

Comment
Examples include paper, canvas, or DVD.

Subclass of

http://purl.org/dc/terms/MediaType

###
PhysicalResource

Class

More details →

URI

http://purl.org/dc/terms/PhysicalResource

Label
Physical Resource

Definition
A material thing.

###
Policy

Class

More details →

URI

http://purl.org/dc/terms/Policy

Label
Policy

Definition
A plan or course of action by an authority, intended to influence and determine decisions, actions, and other matters.

###
ProvenanceStatement

Class

More details →

URI

http://purl.org/dc/terms/ProvenanceStatement

Label
Provenance Statement

Definition
Any changes in ownership and custody of a resource since its creation that are significant for its authenticity, integrity, and interpretation.

###
RightsStatement

Class

More details →

URI

http://purl.org/dc/terms/RightsStatement

Label
Rights Statement

Definition
A statement about the intellectual property rights (IPR) held in or over a resource, a legal document giving official permission to do something with a resource, or a statement about access rights.

###
SizeOrDuration

Class

More details →

URI

http://purl.org/dc/terms/SizeOrDuration

Label
Size or Duration

Definition
A dimension or extent, or a time taken to play or execute.

Comment
Examples include a number of pages, a specification of length, width, and breadth, or a period in hours, minutes, and seconds.

Subclass of

http://purl.org/dc/terms/MediaTypeOrExtent

###
Standard

Class

More details →

URI

http://purl.org/dc/terms/Standard

Label
Standard

Definition
A reference point against which other things can be evaluated or compared.

##
Section 7: DCMI Type Vocabulary

###
Collection

Class

More details →

URI

http://purl.org/dc/dcmitype/Collection

Label
Collection

Definition
An aggregation of resources.

Comment
A collection is described as a group; its parts may also be separately described.

Member Of

http://purl.org/dc/terms/DCMIType

###
Dataset

Class

More details →

URI

http://purl.org/dc/dcmitype/Dataset

Label
Dataset

Definition
Data encoded in a defined structure.

Comment
Examples include lists, tables, and databases. A dataset may be useful for direct machine processing.

Member Of

http://purl.org/dc/terms/DCMIType

###
Event

Class

More details →

URI

http://purl.org/dc/dcmitype/Event

Label
Event

Definition
A non-persistent, time-based occurrence.

Comment
Metadata for an event provides descriptive information that is the basis for discovery of the purpose, location, duration, and responsible agents associated with an event. Examples include an exhibition, webcast, conference, workshop, open day, performance, battle, trial, wedding, tea party, conflagration.

Member Of

http://purl.org/dc/terms/DCMIType

###
Image

Class

More details →

URI

http://purl.org/dc/dcmitype/Image

Label
Image

Definition
A visual representation other than text.

Comment
Examples include images and photographs of physical objects, paintings, prints, drawings, other images and graphics, animations and moving pictures, film, diagrams, maps, musical notation. Note that Image may include both electronic and physical representations.

Member Of

http://purl.org/dc/terms/DCMIType

###
InteractiveResource

Class

More details →

URI

http://purl.org/dc/dcmitype/InteractiveResource

Label
Interactive Resource

Definition
A resource requiring interaction from the user to be understood, executed, or experienced.

Comment
Examples include forms on Web pages, applets, multimedia learning objects, chat services, or virtual reality environments.

Member Of

http://purl.org/dc/terms/DCMIType

###
MovingImage

Class

More details →

URI

http://purl.org/dc/dcmitype/MovingImage

Label
Moving Image

Definition
A series of visual representations imparting an impression of motion when shown in succession.

Comment
Examples include animations, movies, television programs, videos, zoetropes, or visual output from a simulation. Instances of the type Moving Image must also be describable as instances of the broader type Image.

Member Of

http://purl.org/dc/terms/DCMIType

Subclass of

http://purl.org/dc/dcmitype/Image

###
PhysicalObject

Class

More details →

URI

http://purl.org/dc/dcmitype/PhysicalObject

Label
Physical Object

Definition
An inanimate, three-dimensional object or substance.

Comment
Note that digital representations of, or surrogates for, these objects should use Image, Text or one of the other types.

Member Of

http://purl.org/dc/terms/DCMIType

###
Service

Class

More details →

URI

http://purl.org/dc/dcmitype/Service

Label
Service

Definition
A system that provides one or more functions.

Comment
Examples include a photocopying service, a banking service, an authentication service, interlibrary loans, a Z39.50 or Web server.

Member Of

http://purl.org/dc/terms/DCMIType

###
Software

Class

More details →

URI

http://purl.org/dc/dcmitype/Software

Label
Software

Definition
A computer program in source or compiled form.

Comment
Examples include a C source file, MS-Windows .exe executable, or Perl script.

Member Of

http://purl.org/dc/terms/DCMIType

###
Sound

Class

More details →

URI

http://purl.org/dc/dcmitype/Sound

Label
Sound

Definition
A resource primarily intended to be heard.

Comment
Examples include a music playback file format, an audio compact disc, and recorded speech or sounds.

Member Of

http://purl.org/dc/terms/DCMIType

###
StillImage

Class

More details →

URI

http://purl.org/dc/dcmitype/StillImage

Label
Still Image

Definition
A static visual representation.

Comment
Examples include paintings, drawings, graphic designs, plans and maps. Recommended best practice is to assign the type Text to images of textual materials. Instances of the type Still Image must also be describable as instances of the broader type Image.

Member Of

http://purl.org/dc/terms/DCMIType

Subclass of

http://purl.org/dc/dcmitype/Image

###
Text

Class

More details →

URI

http://purl.org/dc/dcmitype/Text

Label
Text

Definition
A resource consisting primarily of words for reading.

Comment
Examples include books, letters, dissertations, poems, newspapers, articles, archives of mailing lists. Note that facsimiles or images of texts are still of the genre Text.

Member Of

http://purl.org/dc/terms/DCMIType

##
Section 8: Terms for vocabulary description

###
domainIncludes

Property

More details →

URI

http://purl.org/dc/dcam/domainIncludes

Label
Domain Includes

Definition
A suggested class for subjects of this property.

###
memberOf

Property

More details →

URI

http://purl.org/dc/dcam/memberOf

Label
Member Of

Definition
A relationship between a resource and a vocabulary encoding scheme which indicates that the resource is a member of a set.

Has Range
http://purl.org/dc/dcam/VocabularyEncodingScheme

See

https://www.dublincore.org/specifications/dublin-core/abstract-model/2007-06-04/

###
rangeIncludes

Property

More details →

URI

http://purl.org/dc/dcam/rangeIncludes

Label
Range Includes

Definition
A suggested class for values of this property.

###
VocabularyEncodingScheme

Class

More details →

URI

http://purl.org/dc/dcam/VocabularyEncodingScheme

Label
Vocabulary Encoding Scheme

Definition
An enumerated set of resources.

See

https://www.dublincore.org/specifications/dublin-core/abstract-model/2007-06-04/

##
Section 9: Bibliography

[DCMI-ACCRUALMETHOD] Collection Description Accrual Method Vocabulary. URL: https://dublincore.org/groups/collections/accrual-method/
[DCMI-ACCRUALPOLICY] Collection Description Accrual Policy Vocabulary. URL: https://dublincore.org/groups/collections/accrual-policy/
[DCMI-COLLFREQ] Collection Description Frequency Vocabulary. URL: https://dublincore.org/groups/collections/frequency/
[DCMI-TYPE] DCMI Type Vocabulary. URL: https://dublincore.org/documents/dcmi-type-vocabulary/
[EDTF] Extended Date/Time Format Specification. URL: http://www.loc.gov/standards/datetime/
[IETF-BCP47] Best Current Practice 47: Tags for Identifying Languages. URL: https://tools.ietf.org/html/bcp47
[ISO8601-1] ISO 8601-1, Date and time — Representations for information interchange — Part 1: Basic rules. URL: https://www.iso.org/iso-8601-date-and-time-format.html
[MIME] Internet Media Types. URL: https://www.iana.org/assignments/media-types/media-types.xhtml
[TGN] Getty Thesaurus of Geographic Names. URL: https://www.getty.edu/research/tools/vocabulary/tgn/index.html
[W3CDTF] W3C Note on Date and Time Formats. URL: https://www.w3.org/TR/NOTE-datetime

##

###

###

###

###