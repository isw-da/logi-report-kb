---
title: "Working with Components in Reports\n\t\t"
id: 1500010063261
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063261-Working-with-Components-in-Reports
updated_at: 2021-07-24T10:39:31Z
---

# Working with Components in Reports
		

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070881-Managing-Page-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028702-Charts)

# Working with Components in Reports

Components are the objects that you can place in a report. Logi JReport provides a full set of components that allow you to present and control the report data and presentation in a wide variety of ways.

Components in Logi JReport can be classified as follows:

* **Visual**: Chart, Map, KPI, Rank
* **Grid**: Table, Crosstab and Tabular
* **Basic**: Label, Text Box, Image, Subreport, Banded Object
* **Web controls**: Filter Control, Parameter Control, Parameter Form Control, Navigation Control, Expand/Collapse Group, Radio Button, Checkbox, Drop-down List, List, Text Field, Password, Text Area, Button, Image Button, Form
* **Fields**: DBField, Formula Field, Summary Field, Parameter Field
* **Drawing objects**: Line, Arc, Box, Oval, Round Box
* **Special fields**: Print Date, Print Time, Fetch Date, Fetch Time, Record Number and many more
* **Others**: UDO, Barcode and Multimedia Object (including Applet, Flash, RealMedia and Windows Media)

## Data Components

Some components can be bound with a dataset or inherit data from the dataset of their parents. These components are Chart, Table, Crosstab, Banded Object, Geographic Map, and KPI. They are also referred to as data components or data containers.

In page reports you can set up link conditions between two data components which have a parent-child relationship. For details, see [Setting Up Data Container Links in Banded Objects](https://devnet.logianalytics.com/hc/en-us/articles/1500010028662-Setting-Up-Data-Container-Links-in-Banded-Objects).

## Components Supported for Different Report Types

You can use all of the above components except KPI in page reports created from query resources; while for page reports based on business views, web reports, and library components, only some of them.

In page reports based on business view, these components can be used: Table, Crosstab, 2-D Chart, Banded Object, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, Drawing Object, Multimedia Object, Parameter Control, Parameter Form Control, Filter Control, and Navigation Control.

Components supported in web reports include: Table, Crosstab, 2-D Chart, Banded Object, Geographic Map, KPI, Tabular, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, Multimedia Object, and web controls excluding Expand/Collapse Group and Form.

In library components, the following can be used: Table, Crosstab, 2-D Chart, Geographic Map, KPI, Label, Image, DBField, Formula Field, Summary Field, Parameter Field, Special Field, and web controls excluding Expand/Collapse Group and Form.

## Component Placement

Components can be placed within banded objects or some other components, as well as onto an empty area of a report. Logi JReport Designer indicates whether or not the target location is valid for the component.

The following tables lists the report areas that are valid targets for the various components in each report type. For components that are not supported in a report type, the corresponding cells are marked by "/".

|  | Page Report | | | | | | | | | | | | Web Report | | | | | | | | | | | Library Component | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Component | Report Body | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Text Box | Table Cell | Tabular Cell | Page Header/ Footer Panel | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | Tabular Cell | KPI | Page Header/ Footer Panel | Report Body | KPI | Table Cell |
| [Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010028702-Charts) | Y | Y | N | N | N | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Table](https://devnet.logianalytics.com/hc/en-us/articles/1500010063901-Tables) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500010063681-Crosstabs) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010063281-Banded-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | / | / | / | / | / | / | / |
| [Map](https://devnet.logianalytics.com/hc/en-us/articles/1500010063821-Maps) | Y | Y | N | N | N | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | N | Y | N | Y | Y | N | N |
| [KPI](https://devnet.logianalytics.com/hc/en-us/articles/1500010029082-KPIs) | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | / | N | Y | N | Y | Y | N | N |
| [Label](https://devnet.logianalytics.com/hc/en-us/articles/1500010029102-Labels) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500010063761-DBFields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010029182-Parameter-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y |
| [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010029262-Summary-Fields-) | N | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010063801-Formula-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010029242-Special-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y |
| [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/1500010029322-Tabulars) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | N | N | N | N | N | N | N | N | N | N | / | / | / |
| [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/1500010029362-Web-Controls) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Image](https://devnet.logianalytics.com/hc/en-us/articles/1500010029062-Images) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Multimedia Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010029162-Multimedia-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | / | / | / |
| [Text Box](https://devnet.logianalytics.com/hc/en-us/articles/1500010063961-Text-Boxes) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Subreport](https://devnet.logianalytics.com/hc/en-us/articles/1500010029222-Subreports) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Drawing Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010063781-Drawing-Objects) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [UDO](https://devnet.logianalytics.com/hc/en-us/articles/1500010063981-UDOs) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Barcode](https://devnet.logianalytics.com/hc/en-us/articles/1500010028682-Barcodes) | Barcode and rank components can be inserted in a report layout area that is valid for the component on which the barcode or rank is based. For example, a rank component that represents a DBField is allowed in the report layout areas in which a DBField component is allowed. | | | | | | | | | | | | / | / | / | / | / | / | / | / | / | / | / | / | / | / |
| [Rank](https://devnet.logianalytics.com/hc/en-us/articles/1500010029202-Ranks) | / | / | / | / | / | / | / | / | / | / | / | / | / | / |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070881-Managing-Page-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028702-Charts)
