---
title: "Bind Data Dialog Box"
id: 1500010058062
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058062-Bind-Data-Dialog-Box
updated_at: 2021-07-23T19:15:04Z
---

# Bind Data Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058082-Barcode-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058102-Bursting-Dialog-Box)

# Marks content and feature updates for Logi Report v17.1. New feature new content.Bind Data Dialog Box

You can use the Bind Data dialog box to [bind a data resource](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#BindData) to the report body. This topic describes the options in the dialog box.

Designer displays the Bind Data dialog box when you select Report > Bind Data, or right-click any blank area in the report body and select Bind Data from the shortcut menu, and provides different options in the dialog box for binding a [business view](#BV) or a [query resource](#Query).

## For Binding a Business View

![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848419607/bddt_bv.gif)

You see the following options in the dialog box:

**Available data resources**

The box lists all the predefined business views in the current catalog. Select the business view you want.

**OK**

Select to bind the specified business view to the report body and close the dialog box.

**Cancel**

Select to cancel the binding of a business view to the report body and close the dialog box.

**Help**

Select to view information about the dialog box.

## For Binding a Query Resource

![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856839191/bddt.gif)

You see the following options in the dialog box:

**Data resource box**

The box lists all the predefined data resources in the current catalog. Select the data resource you want to bind to the report body. Designer then automatically creates a dataset based on the selected data resource in the current page report.

**Less Options**/**More Options**

Select to show or hide the dataset selection panel to choose a dataset to bind to the report body.

* **New Dataset**  
  Select to create a dataset based on the current catalog data resources. When you select a query, Designer enables the Edit button at the bottom and you can select the button to edit the query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098321-Query-Editor-Dialog-Box).
* **Existing Dataset**  
  Select to use a dataset from the ones that you have created in the current page report. You can select the Edit button to edit the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select <New Dataset...> to create a dataset in the page report using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098001-New-Dataset-Dialog-Box).

* **Current Dataset**  
  Designer disables the option because the report body cannot use inherited dataset.

**OK**

Select to bind the specified data resource to the report body and close the dialog box.

**Cancel**

Select to cancel the binding of a data resource to the report body and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058082-Barcode-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058102-Bursting-Dialog-Box)
