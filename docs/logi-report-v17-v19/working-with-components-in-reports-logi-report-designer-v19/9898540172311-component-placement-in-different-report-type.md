---
title: "Component Placement in Different Report Type"
id: 9898540172311
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type
updated_at: 2022-11-02T08:20:10Z
---

# Component Placement in Different Report Type

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520464535-Working-with-Components-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563831831-Working-with-Charts)

# Component Placement in Different Report Type

The components you can use vary with the report type: page report (query-based or business view-based), web report, or library component. In a report, you can place components within banded objects or some other components, in the page headers and footers, and in an empty area in the report body. When you insert a component, Designer indicates whether the target location is valid for the component. This topic describes the components you can use in different report types, and uses tables to show the report areas in each report type that are valid locations for different components.

* [Components in Query-Based Page Report](#QueryCLS)
* [Components in Business View-Based Page Report](#BVCLS)
* [Components in Web Report](#WLS)
* [Components in Library Component](#LC)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The following tables show whether you can place a component type in different report areas generally. You may find Designer does not allow adding some specific components of a type to a location. For example, you see "Y" for Web Control in all the banded panel columns in the page report tables, but you can insert the Expand/Collapse Group web control in Banded Page Header Panel (BPH) only.

## Components in Query-Based Page Report

As Designer indicates in the Insert ribbon, you can use all components except KPI in page reports that apply query resources.

|  | Report Body | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | Tabular Cell | Text Box | Page Header/ Footer Panel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [DBField](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields) | N | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N |
| [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Label](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Text Box](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes) | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| [Image](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Table](https://devnet.logianalytics.com/hc/en-us/articles/5735512509719-Working-with-Tables) | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/5735498924183-Working-with-Crosstabs) | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| [Chart](https://devnet.logianalytics.com/hc/en-us/articles/5735563831831-Working-with-Charts) | Y | Y | N | N | N | Y | Y | Y | N | Y | N | Y |
| [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/5735564433175-Working-with-Tabulars) | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| [Subreport](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports) | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | N | Y |
| [UDO](https://devnet.logianalytics.com/hc/en-us/articles/5735507452311-Working-with-UDOs) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N |
| [Map](https://devnet.logianalytics.com/hc/en-us/articles/5735499010967-Working-with-Maps) | Y | Y | N | N | N | Y | Y | Y | N | Y | N | Y |
| [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Drawing Object](https://devnet.logianalytics.com/hc/en-us/articles/5735512413207-Working-with-Drawing-Objects) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N | N |
| [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/5735564487575-Working-with-Web-Controls) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Multimedia Object](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y | Y |
| [Barcode](https://devnet.logianalytics.com/hc/en-us/articles/5735498517911-Working-with-Barcodes) | You can insert barcode and rank components in a report area that is valid for the component on which the barcode or rank is based. For example, you can insert a rank component that represents a DBField in the report areas in which a DBField component is allowed. | | | | | | | | | | | |
| [Rank](https://devnet.logianalytics.com/hc/en-us/articles/5735564383767-Working-with-Ranks) |

## Components in Business View-Based Page Report

You can use the following components in business view-based page reports: DBField, Formula Field, Summary Field, Parameter Field, Label, ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")Text Box, Image, Table, Crosstab, 2-D Chart, Banded Object, Subreport, Special Field, Drawing Object, Web Control (advanced web controls and Form only), and Multimedia Object.

|  | Report Body | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Text Box | Page Header/ Footer Panel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [DBField](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields) | N | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Label](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Text Box](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| [Image](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Table](https://devnet.logianalytics.com/hc/en-us/articles/5735512509719-Working-with-Tables) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/5735498924183-Working-with-Crosstabs) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| [Chart](https://devnet.logianalytics.com/hc/en-us/articles/5735563831831-Working-with-Charts) | Y | Y | N | N | N | Y | Y | Y | N | N | Y |
| [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| [Subreport](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports) | Y | Y | Y | Y | Y | Y | Y | Y | N | N | Y |
| [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Drawing Object](https://devnet.logianalytics.com/hc/en-us/articles/5735512413207-Working-with-Drawing-Objects) | N | Y | Y | Y | Y | Y | Y | Y | N | N | N |
| [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/5735564487575-Working-with-Web-Controls) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Multimedia Object](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects) | Y | Y | Y | Y | Y | Y | Y | Y | N | Y | Y |

## Components in Web Report

You can use the following components in web reports: DBField, Formula Field, Summary Field, Parameter Field, Label, ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")Text Box, Image, Table, Crosstab, 2-D Chart, Banded Object, KPI, Tabular, Map (Geographic Map only), Special Field, Drawing Object (Line only), Web Control (excluding Expand/Collapse Group and Form), and Multimedia Object.

|  | Banded Header Panel (BH) | Banded Page Header Panel (BPH) | Banded Detail Panel (DT) | Banded Page Footer Panel (BPF) | Banded Footer Panel (BF) | Banded Group Header Panel (GH) | Banded Group Footer Panel (GF) | Table Cell | Tabular Cell | This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Text Box | KPI | Page Header/ Footer Panel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [DBField](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N |
| [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N |
| [Label](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Text Box](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes) | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| [Image](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| [Table](https://devnet.logianalytics.com/hc/en-us/articles/5735512509719-Working-with-Tables) | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/5735498924183-Working-with-Crosstabs) | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| [Chart](https://devnet.logianalytics.com/hc/en-us/articles/5735563831831-Working-with-Charts) | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| [KPI](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs) | N | N | N | N | N | N | N | N | Y | N | N | Y |
| [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/5735564433175-Working-with-Tabulars) | N | N | N | N | N | N | N | N | N | N | N | N |
| [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects) | N | N | N | N | N | N | N | N | Y | N | N | Y |
| [Geographic Map](https://devnet.logianalytics.com/hc/en-us/articles/5735499019543-Using-Geographic-Maps) | N | N | N | N | N | N | N | N | Y | N | N | Y |
| [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields) | Y | Y | Y | Y | Y | Y | Y | Y | Y | N | N | N |
| [Drawing Object](https://devnet.logianalytics.com/hc/en-us/articles/5735512413207-Working-with-Drawing-Objects) | Y | Y | Y | Y | Y | Y | Y | N | N | N | N | N |
| [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/5735564487575-Working-with-Web-Controls) | Y | Y | Y | Y | Y | Y | Y | N | Y | N | N | Y |
| [Multimedia Object](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects) | Y | Y | Y | Y | Y | Y | Y | N | Y | Y | N | Y |

## Components in Library Component

You can use the following components in library components: DBField, Formula Field, Summary Field, Parameter Field, Label, Image, Table, Crosstab, 2-D Chart, KPI, Map (Geographic Map only), Special Field, and Web Control (excluding Expand/Collapse Group and Form).

|  | Body | Table Cell | KPI |
| --- | --- | --- | --- |
| [DBField](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields) | Y | Y | Y |
| [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields) | Y | Y | Y |
| [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields) | Y | Y | Y |
| [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields) | Y | Y | N |
| [Label](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels) | Y | Y | Y |
| [Image](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images) | Y | Y | Y |
| [Table](https://devnet.logianalytics.com/hc/en-us/articles/5735512509719-Working-with-Tables) | Y | N | N |
| [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/5735498924183-Working-with-Crosstabs) | Y | N | N |
| [Chart](https://devnet.logianalytics.com/hc/en-us/articles/5735563831831-Working-with-Charts) | Y | N | N |
| [KPI](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs) | Y | N | N |
| [Geographic Map](https://devnet.logianalytics.com/hc/en-us/articles/5735499019543-Using-Geographic-Maps) | Y | N | N |
| [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields) | Y | Y | N |
| [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/5735564487575-Working-with-Web-Controls) | Y | N | N |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735520464535-Working-with-Components-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563831831-Working-with-Charts)
