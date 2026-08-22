---
title: "Working with Components in Reports"
id: 1500010094261
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports
updated_at: 2021-07-23T19:14:35Z
---

# Working with Components in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101281-Managing-Page-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056822-Working-with-Charts)

# Working with Components in Reports

Components are the objects that you can place in a report. Logi Report provides a full set of components that enable you to present and control the report data and presentation in a wide variety of ways. This topic introduces the usage of each component.

## Component Categories

Logi Report classifies the components into the following categories:

* **Visual**: Chart, Map, KPI, and Rank
* **Grid**: Table, Crosstab, and Tabular
* **Basic**: Label, Text Box, Image, Subreport, and Banded Object
* **Web controls**: Filter Control, Parameter Control, Parameter Form Control, Navigation Control, Expand/Collapse Group, Radio Button, Checkbox, Drop-down List, List, Text Field, Password, Text Area, Button, Image Button, and Form
* **Fields**: DBField, Formula Field, Summary Field, and Parameter Field
* **Drawing objects**: Line, Arc, Box, Oval, and Round Box
* **Special fields**: Print Date, Print Time, Fetch Date, Fetch Time, Record Number, and many more
* **Others**: UDO, Barcode, and Multimedia Object (including Applet, Flash, RealMedia, and Windows Media)

## Data Components

You can bind datasets to some components or have them inherit data from the datasets of their parents. These components are Chart, Table, Crosstab, Banded Object, Geographic Map, and KPI. Logi Report refers to them as data components or data containers.

In page reports, you can set up link conditions between two data components which have a parent-child relationship. For more information, see [Setting Up Data Container Links in Banded Objects](https://devnet.logianalytics.com/hc/en-us/articles/1500010056782-Setting-Up-Data-Container-Links-in-Banded-Objects).

## Components Supported for Different Report Types

You can use all of the above components except KPI in page reports created from query resources; while for page reports based on business views, web reports, and library components, only some of them.

In page reports based on business view, you can use these components: Table, Crosstab, 2-D Chart, Banded Object, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, Drawing Object, Multimedia Object, Parameter Control, Parameter Form Control, Filter Control, and Navigation Control.

Components supported in web reports include: Table, Crosstab, 2-D Chart, Banded Object, Geographic Map, KPI, Tabular, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, Multimedia Object, and web controls excluding Expand/Collapse Group and Form.

In library components, you can use the following: Table, Crosstab, 2-D Chart, Geographic Map, KPI, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, and web controls excluding Expand/Collapse Group and Form.

## Component Placement

You can place components within banded objects or some other components, as well as in an empty area of a report. Designer indicates whether or not the target location is valid for the component.

The following table lists the report areas that are valid targets for the various components in each report type. For components that Designer does not support in a report type, you can see "/" in the corresponding cells.

|  | Page Report | | | | | | | | | | | | Web Report | | | | | | | | | | | Library Component | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Component | Report Body | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Text Box | Table Cell | Tabular Cell | Page Header/ Footer Panel | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | Tabular Cell | KPI | Page Header/ Footer Panel | Report Body | KPI | Table Cell |
| [Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010056822-Working-with-Charts) | Y | Y | N | N | N | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Table](https://devnet.logianalytics.com/hc/en-us/articles/1500010094921-Working-with-Tables) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010057162-Working-with-Crosstabs) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010094281-Working-with-Banded-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | / | / | / | / | / | / | / |
| [Map](https://devnet.logianalytics.com/hc/en-us/articles/1500010057282-Working-with-Maps) | Y | Y | N | N | N | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | N | Y | N | Y | Y | N | N |
| [KPI](https://devnet.logianalytics.com/hc/en-us/articles/1500010057242-Working-with-KPIs) | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | N | Y | N | Y | Y | N | N |
| [Label](https://devnet.logianalytics.com/hc/en-us/articles/1500010057262-Working-with-Labels) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010057382-Working-with-Parameter-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y |
| [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields) | N | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010094741-Working-with-Formula-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y |
| [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/1500010094961-Working-with-Tabulars) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | N | N | N | N | / | / | / |
| [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/1500010057502-Working-with-Web-Controls) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Image](https://devnet.logianalytics.com/hc/en-us/articles/1500010094761-Working-with-Images) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Multimedia Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010094821-Working-with-Multimedia-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | / | / | / |
| [Text Box](https://devnet.logianalytics.com/hc/en-us/articles/1500010094981-Working-with-Text-Boxes) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Subreport](https://devnet.logianalytics.com/hc/en-us/articles/1500010094861-Working-with-Subreports) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Drawing Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010057222-Working-with-Drawing-Objects) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [UDO](https://devnet.logianalytics.com/hc/en-us/articles/1500010057462-Working-with-UDOs) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Barcode](https://devnet.logianalytics.com/hc/en-us/articles/1500010094341-Working-with-Barcodes) | You can insert barcode and rank components in a report layout area that is valid for the component on which the barcode or rank is based. For example, a rank component that represents a DBField is allowed in the report layout areas in which a DBField component is allowed. | | | | | | | | | | | | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Rank](https://devnet.logianalytics.com/hc/en-us/articles/1500010094841-Working-with-Ranks) | / | / | / | / | / | / | / | / | / | / | / | / | / | / |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101281-Managing-Page-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010056822-Working-with-Charts)
