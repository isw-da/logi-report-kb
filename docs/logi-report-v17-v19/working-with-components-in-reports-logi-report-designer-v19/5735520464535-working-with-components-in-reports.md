---
title: "Working with Components in Reports"
id: 5735520464535
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735520464535-Working-with-Components-in-Reports
updated_at: 2022-11-02T04:12:37Z
---

# Working with Components in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569625367-Customizing-Field-Display-Names-for-Datasets-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type)

# Working with Components in Reports

Components are the objects that you can place in reports. Logi Report provides a full set of components that enable you to present and control the report data and presentation in a wide variety of ways. This topic introduces the usage of each component. It also briefly describes how Logi Report classifies the components and what data components are.

You can use the following components in Logi Report:

* [Chart](https://devnet.logianalytics.com/hc/en-us/articles/5735563831831-Working-with-Charts)
* [Table](https://devnet.logianalytics.com/hc/en-us/articles/5735512509719-Working-with-Tables)
* [Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/5735498924183-Working-with-Crosstabs)
* [Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects)
* [Map](https://devnet.logianalytics.com/hc/en-us/articles/5735499010967-Working-with-Maps)
* [KPI](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs)
* [Label](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels)
* [DBField](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields)
* [Parameter Field](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields)
* [Summary Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields)
* [Formula Field](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields)
* [Special Field](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields)
* [Tabular](https://devnet.logianalytics.com/hc/en-us/articles/5735564433175-Working-with-Tabulars)
* [Web Control](https://devnet.logianalytics.com/hc/en-us/articles/5735564487575-Working-with-Web-Controls)
* [Image](https://devnet.logianalytics.com/hc/en-us/articles/5735564305815-Working-with-Images)
* [Multimedia Object](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects)
* [Text Box](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes)
* [Subreport](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports)
* [Drawing Object](https://devnet.logianalytics.com/hc/en-us/articles/5735512413207-Working-with-Drawing-Objects)
* [UDO](https://devnet.logianalytics.com/hc/en-us/articles/5735507452311-Working-with-UDOs)
* [Barcode](https://devnet.logianalytics.com/hc/en-us/articles/5735498517911-Working-with-Barcodes)
* [Rank](https://devnet.logianalytics.com/hc/en-us/articles/5735564383767-Working-with-Ranks)

See [Component Placement in Different Report Type](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) about the components you can use in different report types, and the report areas where you can place them in a report.

## Component Categories

Logi Report classifies the components into the following categories:

* **Visual:** Chart, Map, KPI, and Rank
* **Grid:** Table, Crosstab, and Tabular
* **Basic:** Label, Text Box, Image, Subreport, and Banded Object
* **Data Field:** DBField, Formula Field, Summary Field, and Parameter Field
* **Web Control:** Filter Control, Parameter Control, Parameter Form Control, Navigation Control, Expand/Collapse Group, Radio Button, Checkbox, Drop-down List, List, Text Field, Password, Text Area, Button, Image Button, and Form
* **Special Field:** Print Date, Print Time, Fetch Date, Fetch Time, Record Number, and many more
* **Drawing Object:** Line, Arc, Box, Oval, and Round Box
* **Multimedia Object:** Applet, RealMedia, and Windows Media
* **Others:** UDO and Barcode

## Data Components

Some components must be bound with a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report) to display data, so Logi Report refers to them as data components or data containers. These components include Chart, Table, Crosstab, Banded Object, Geographic Map, and KPI. In page reports and ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")web reports, when two data containers in a parent-child relationship apply different datasets, you can use [data container links](https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report) to set up data relations between them.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) After you bind a dataset to the report body, Logi Report also regards the report body as a special data container. In this case, if you place a tabular directly inside the report body, the tabular applies the same dataset as the report body and becomes a data container too; if you place nested tabulars and the parent of the outermost tabular is the report body, all these tabulars apply dataset of the report body and turn to be data containers.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569625367-Customizing-Field-Display-Names-for-Datasets-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type)
