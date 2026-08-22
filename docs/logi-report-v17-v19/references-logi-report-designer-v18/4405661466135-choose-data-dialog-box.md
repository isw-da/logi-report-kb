---
title: "Choose Data Dialog Box"
id: 4405661466135
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661466135-Choose-Data-Dialog-Box
updated_at: 2022-01-27T20:38:10Z
---

# Choose Data Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661468695-Chart-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411769082647-Choose-JDBC-Connection-Dialog-Box)

# Choose Data Dialog Box

You can use the Choose Data dialog box to choose data for a report tab or KPI. This topic describes the options in the dialog box.

Designer displays different options in the dialog box for choosing a [business view](#BV) or a [query resource](#Query).

## For Choosing a Business View

When you open the Choose Data dialog box via one of the following methods, you use it to choose a business view to bind to the [blank page report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#Tab) or [KPI](https://devnet.logianalytics.com/hc/en-us/articles/4405661382551-Working-with-KPIs).

* In the [Select Component for Page Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664570647-Select-Component-for-Page-Report-Dialog-Box), select Create Using Business View, select the Blank component, and then select OK.
* When creating a new report tab in a business view-based page report, in the [Select Component for Page Report Tab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661705367-Select-Component-for-Page-Report-Tab-Dialog-Box), select the Blank component and select OK.
* Drag the KPI icon ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/4420402536343/icon_kpi.gif) from the Components panel to the destination in an open web report or library component.

![Choose Data dialog box - for choosing business views](https://devnet.logianalytics.com/hc/article_attachments/4420402536599/chsdt-bv.gif)

You see the following options in the dialog box:

**Business view box**

This box lists all the predefined business views in the current catalog. Select the business view you want.

**OK**

Select to bind the specified business view to the target and close the dialog box.

**Cancel**

Select to quit binding a business view to the target and close the dialog box.

**Help**

Select to view information about the dialog box.

## For Choosing a Query Resource

When you open the Choose Data dialog box via one of the following methods, you use it to choose the dataset for [the blank page report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#Tab).

* In the [Select Component for Page Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664570647-Select-Component-for-Page-Report-Dialog-Box), select the Blank component and select OK.
* When creating a new report tab in a query-based page report, in the [Select Component for Page Report Tab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661705367-Select-Component-for-Page-Report-Tab-Dialog-Box), select the Blank component and select OK.

![Choose Data dialolg box - for choosing query resources](https://devnet.logianalytics.com/hc/article_attachments/4420410602647/chsdt.gif)

You see the following options in the dialog box:

**Data resource box**

This box lists all the predefined data resources in the current catalog. Select one and Designer creates a dataset based on it automatically for the report tab.

**More Options**/**Less Options**

Select to show or hide the dataset selection panel to choose a dataset for the report tab.

* **New Dataset**  
  Select to create a dataset based on a data resource in the current catalog. If you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661685015-Query-Editor-Dialog-Box). You can also select the first item under a resource node to add or create a data resource of the type in the catalog and use it to create the dataset.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select **Edit** to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), or select **<New Dataset...>** to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661656087-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer disables this option because a page report tab cannot use inherited dataset.

**Edit**

Select to edit the specified query or dataset.

**OK**

Select to apply the specified dataset to the report tab and close the dialog box.

**Cancel**

Select to quit choosing a dataset for the report tab and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661468695-Chart-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411769082647-Choose-JDBC-Connection-Dialog-Box)
