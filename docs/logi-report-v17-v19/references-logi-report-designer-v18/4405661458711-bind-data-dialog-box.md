---
title: "Bind Data Dialog Box"
id: 4405661458711
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661458711-Bind-Data-Dialog-Box
updated_at: 2022-01-27T20:38:21Z
---

# Bind Data Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661461911-Barcode-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664430615-Bursting-Dialog-Box)

# Bind Data Dialog Box

You can use the Bind Data dialog box to [bind a data resource](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#BindData) to the report body. This topic describes the options in the dialog box.

Designer displays the Bind Data dialog box when you do one of the following:

* Navigate to Report > Bind Data.
* Right-click any blank area in the report body and select Bind Data from the shortcut menu.
* Select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) to edit some page properties using a formula for a page report tab in the General tab of the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box) or via the [Page Panel object](https://devnet.logianalytics.com/hc/en-us/articles/4405661878807-Page-Panel-Properties) in the Report Inspector, ![This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.](https://devnet.logianalytics.com/hc/article_attachments/4420542050071/___newv18.3.jpg "New for version 18.3.")or to edit the Sheet Name property of a page report tab or web report, but you have not bound a data resource to the report body, then select OK in the message box.

Designer provides you with different options in the dialog box for binding a [business view](#BV) or a [query resource](#Query).

## For Binding a Business View

![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542081943/bddt_bv.gif)

You see the following options in the dialog box:

**Available data resources**

This box lists all the predefined business views in the current catalog. Select the business view you want.

**OK**

Select to bind the specified business view to the report body and close the dialog box.

**Cancel**

Select to quit binding data to the report body and close the dialog box.

**Help**

Select to view information about the dialog box.

## For Binding a Query Resource

![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550834327/bddt.gif)

You see the following options in the dialog box:

**Data resource box**

This box lists all the predefined data resources in the current catalog. Select the data resource you want to bind to the report body. Designer then automatically creates a dataset based on the specified data resource in the current page report.

**Less Options**/**More Options**

Select to show or hide the dataset selection panel to choose a dataset to bind to the report body.

* **New Dataset**  
  Select to create a dataset based on a data resource in the current catalog. If you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661685015-Query-Editor-Dialog-Box). You can also select the first item under a resource node to add or create a data resource of the type in the catalog and use it to create the dataset.
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select **Edit** to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), or select **<New Dataset...>** to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661656087-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer disables this option because the report body cannot use inherited dataset.

**OK**

Select to bind the specified dataset to the report body and close the dialog box.

**Cancel**

Select to quit binding data to the report body and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661461911-Barcode-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664430615-Bursting-Dialog-Box)
