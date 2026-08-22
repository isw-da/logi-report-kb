---
title: "Working with Components in Reports"
id: 1500009583241
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports
updated_at: 2021-07-24T05:56:11Z
---

# Working with Components in Reports

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570882-Saving-a-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562922-Charts)

# Working with Components in Reports

Components are the objects that you can place in a report. Logi JReport provides a full set of components that allow you to present and control the report data and presentation in a wide variety of ways.

Components in Logi JReport can be classified as follows:

* **Visual**: chart, map, KPI, rank
* **Grid**: table, crosstab and tabular
* **Basic**: label, text box, image, subreport, banded object
* **Web controls**: filter control, parameter control, parameter form control, navigation control, radio button, check box, drop-down list, list, text field, password, text area, form, button, image button
* **Fields**: DBField, formula field, summary field, parameter field
* **Drawing objects**: line, arc, box, oval, round box
* **Special fields**: Print Date, Print Time, Fetch Date, Fetch Time, Record Number and many more
* **Others**: UDO, barcode, and multimedia objects (including Applet, Flash, RealMedia File and Windows Media File)

**Data components**

Some components can be bound with a dataset or inherit data from the dataset of their parents. These components are table, chart, crosstab, banded object, geographic map, and KPI component, and they are also referred to as data components or data containers.

In page reports that are created using query resources, you can set up link conditions between two data components which have a parent-child relationship. For details, see [Setting Up a Data Container Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009583301-Setting-Up-a-Data-Container-Link).

**Components supported for different report types**

You can use all of the above components except the KPI component in [page reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009570902-Page-Reports) created from query resources; while for page reports based on business views, [web reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports), and [library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009592681-Library-Components), only some of them.

In page reports based on business view, these components can be used: table, crosstab, 2-D chart, banded object, label, image, DBField, formula, summary, parameter, special field, drawing object, multimedia object, parameter control, parameter form control, filter control, and navigation control.

Components supported in web reports include: table, crosstab, 2-D chart, geographic map, KPI component, tabular, label, image, DBField, formula, summary, parameter, special field, multimedia object, parameter control, parameter form control, filter control, and navigation control.

In library components, the following can be used: table, crosstab, 2-D chart, KPI component, label, image, DBField, summary, formula, geographic map, parameter, special field, parameter control, parameter form control, filter control, navigation control, text field, checkbox, drop-down list, and list.

**Component placement**

Components can be placed within banded objects or some other components, as well as onto an empty area of a report. Logi JReport Designer indicates whether or not the target location is valid for the component.

The following tables lists the report areas that are valid targets for the various components, listed on the left. For components that are not supported in a report type, the corresponding cells are marked by "/".

|  | Report Layout Area | | | | | | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Page Report | | | | | | | | | | | | Web Report | | | | Library Component | | |
| Component | Report Body | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Text Box | Table Cell | Tabular Cell | Page Header/ Footer Panel | Table Cell | Tabular Cell | KPI Component | Page Header/ Footer Panel | Report Body | KPI Component | Table Cell |
| [Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009562922-Charts) | Y | Y | N | N | N | Y | Y | Y | N | N | Y | Y | N | Y | N | Y | Y | N | N |
| [Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009584261-Tables) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | Y | N | Y | Y | N | N |
| [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009563302-Crosstabs) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | Y | N | Y | Y | N | N |
| [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009562842-Banded-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / |
| [Map](https://devnet.logianalytics.com/hc/en-us/articles/1500009584061-Maps) | Y | Y | N | N | N | Y | Y | Y | N | N | Y | Y | N | Y | N | Y | Y | N | N |
| [KPI Component](https://devnet.logianalytics.com/hc/en-us/articles/1500009583981-KPI-Components) | / | / | / | / | / | / | / | / | / | / | / | / | N | Y | N | Y | Y | N | N |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584001-Labels) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500009583921-DBFields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009584201-Parameter-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y |
| [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009563602-Summary-Fields) | N | Y | N | N | N | Y | Y | Y | N | Y | N | N | Y | Y | Y | N | Y | Y | Y |
| [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009563362-Formula-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | Y |
| [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009584241-Special-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/1500009563742-Tabulars) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | N | N | N | N | / | / | / |
| [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/1500009563842-Web-Controls) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y | Y | N | N |
| [Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009583961-Images) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Multimedia Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009584181-Multimedia-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | N | Y | N | Y | / | / | / |
| [Text Box](https://devnet.logianalytics.com/hc/en-us/articles/1500009563762-Text-Boxes) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / |
| [Subreport](https://devnet.logianalytics.com/hc/en-us/articles/1500009563582-Subreports) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y | / | / | / | / | / | / | / |
| [Drawing Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009583941-Drawing-Objects) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | / | / | / | / | / | / | / |
| [UDO](https://devnet.logianalytics.com/hc/en-us/articles/1500009563782-UDOs) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | / | / | / | / | / | / | / |
| [Barcode](https://devnet.logianalytics.com/hc/en-us/articles/1500009562902-Barcodes) | Barcode and rank components can be inserted in a report layout area that is valid for the component on which the barcode or rank is based. For example, a rank component that represents a DBField is allowed in the report layout areas in which a DBField component is allowed. | | | | | | | | | | | | / | / | / | / | / | / | / |
| [Rank](https://devnet.logianalytics.com/hc/en-us/articles/1500009584221-Ranks) | / | / | / | / | / | / | / |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570882-Saving-a-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562922-Charts)
