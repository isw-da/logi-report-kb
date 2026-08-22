---
title: "Working with Components in Reports"
id: 4405664365463
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports
updated_at: 2022-01-27T20:34:21Z
---

# Working with Components in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664693399-Managing-Page-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664369047-Working-with-Charts)

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
* **Others**: UDO, Barcode, and Multimedia Object (including Applet, RealMedia, and Windows Media)

## Data Components

You can bind datasets to some components or have them inherit data from the datasets of their parents. These components are Chart, Table, Crosstab, Banded Object, Geographic Map, and KPI. Logi Report refers to them as data components or data containers.

In page reports, you can set up link conditions between two data components which have a parent-child relationship. For more information, see [Setting Up Data Container Links in Banded Objects](https://devnet.logianalytics.com/hc/en-us/articles/4405664367511-Setting-Up-Data-Container-Links-in-Banded-Objects).

## Components Supported for Different Report Types

You can use all components except KPI in page reports that apply query resources; while for page reports using business views, web reports, and library components, only some of them.

In page reports based on business view, you can use these components: Table, Crosstab, 2-D Chart, Banded Object, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, Drawing Object, Multimedia Object, Parameter Control, Parameter Form Control, Filter Control, and Navigation Control.

Components supported in web reports include: Table, Crosstab, 2-D Chart, Banded Object, Geographic Map, KPI, Tabular, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, Multimedia Object, and web controls excluding Expand/Collapse Group and Form.

In library components, you can use the following: Table, Crosstab, 2-D Chart, Geographic Map, KPI, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, and web controls excluding Expand/Collapse Group and Form.

## Component Placement

You can place components within banded objects or some other components, and in an empty area of a report. Designer indicates whether the target location is valid for the component.

The following table lists the report areas that are valid targets for the various components in each report type. For components that Designer does not support in a report type, you can see "/" in the corresponding cells.

|  | Page Report | | | | | | | | | | | | Web Report | | | | | | | | | | | Library Component | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Component | Report Body | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Text Box | Table Cell | Tabular Cell | Page Header/ Footer Panel | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | Tabular Cell | KPI | Page Header/ Footer Panel | Report Body | KPI | Table Cell |
| [Chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664369047-Working-with-Charts) | Y | Y | N | N | N | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Table](https://devnet.logianalytics.com/hc/en-us/articles/4405664403351-Working-with-Tables) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/4405664392727-Working-with-Crosstabs) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/4405661345431-Working-with-Banded-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | / | / | / | / | / | / | / |
| [Map](https://devnet.logianalytics.com/hc/en-us/articles/4405661384599-Working-with-Maps) | Y | Y | N | N | N | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | N | Y | N | Y | Y | N | N |
| [KPI](https://devnet.logianalytics.com/hc/en-us/articles/4405661382551-Working-with-KPIs) | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | N | Y | N | Y | Y | N | N |
| [Label](https://devnet.logianalytics.com/hc/en-us/articles/4405661383575-Working-with-Labels) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [DBField](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/4405664399255-Working-with-Parameter-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y |
| [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/4405661398551-Working-with-Summary-Fields) | N | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/4405661380119-Working-with-Formula-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y |
| [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/4405661404695-Working-with-Tabulars) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | N | N | N | N | / | / | / |
| [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/4405661409815-Working-with-Web-Controls) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Image](https://devnet.logianalytics.com/hc/en-us/articles/4405661381143-Working-with-Images) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Multimedia Object](https://devnet.logianalytics.com/hc/en-us/articles/4405661390743-Working-with-Multimedia-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | / | / | / |
| [Text Box](https://devnet.logianalytics.com/hc/en-us/articles/4405664406679-Working-with-Text-Boxes) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Subreport](https://devnet.logianalytics.com/hc/en-us/articles/4405664401431-Working-with-Subreports) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Drawing Object](https://devnet.logianalytics.com/hc/en-us/articles/4405661379095-Working-with-Drawing-Objects) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [UDO](https://devnet.logianalytics.com/hc/en-us/articles/4405661407255-Working-with-UDOs) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Barcode](https://devnet.logianalytics.com/hc/en-us/articles/4405661349911-Working-with-Barcodes) | You can insert barcode and rank components in a report layout area that is valid for the component on which the barcode or rank is based. For example, you can insert a rank component that represents a DBField in the report layout areas in which a DBField component is allowed. | | | | | | | | | | | | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Rank](https://devnet.logianalytics.com/hc/en-us/articles/4405664400279-Working-with-Ranks) | / | / | / | / | / | / | / | / | / | / | / | / | / | / |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664693399-Managing-Page-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664369047-Working-with-Charts)
