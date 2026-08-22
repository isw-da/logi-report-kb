---
title: "Choose Data Dialog Box"
id: 5735565124375
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735565124375-Choose-Data-Dialog-Box
updated_at: 2022-11-02T04:14:24Z
---

# Choose Data Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513259415-Chart-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513226263-Choose-JDBC-Connection-Dialog-Box)

# Choose Data Dialog Box

You can use the Choose Data dialog box to specify the dataset you want to use for [a blank page report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#ChooseData) or for a [KPI](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC). This topic describes the options in the dialog box.

Designer displays the Choose Data dialog box when you do one of the following:

* In the [Select Component for Page Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544320151-Select-Component-for-Page-Report-Dialog-Box), select the Blank component and select OK.
* When creating a new page report tab, in the [Select Component for Page Report Tab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544328727-Select-Component-for-Page-Report-Tab-Dialog-Box), select the Blank component and select OK.
* Drag the KPI icon ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/9898533135639/icon_kpi.gif) from the Components panel to the destination in a web report or library component.

![Choose Data dialolg box - for choosing query resources](https://devnet.logianalytics.com/hc/article_attachments/9898533140631/chsdt.gif)

Designer displays these options:

**Data resource box**

This box lists the predefined data resources in the current catalog. Select one and Designer automatically creates a dataset based on it for the report tab or KPI.

* **<New XXX...>**/**<Add XXX...>**  
  Select to create or add a data resource of the same type in the catalog. Designer does not display this option when you use the dialog box for choosing KPI data in a library component.

**More Options**/**Less Options**

Select to show or hide the options for specifying the dataset you want to use. Designer does not display this pair of buttons when you use the dialog box for choosing KPI data in a library component.

* **New Dataset**  
  Select to create a dataset based on a data resource in the current catalog.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the page report.
  + **<New Dataset...>**  
    Select to create a dataset using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).
* **Current Dataset**  
  Designer disables this option because a page report tab cannot use inherited dataset.

**Edit**

Select to edit the specified query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box), ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")business view in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508168471-Business-View-Editor-Dialog-Box), or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box). Designer does not display this button when you use the dialog box for choosing KPI data in a library component.

**OK**

Select to apply the specified dataset to the report tab or KPI and close the dialog box.

**Cancel**

Select to quit choosing a dataset for the report tab or KPI and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513259415-Chart-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513226263-Choose-JDBC-Connection-Dialog-Box)
