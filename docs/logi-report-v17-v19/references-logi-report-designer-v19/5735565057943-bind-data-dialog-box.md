---
title: "Bind Data Dialog Box"
id: 5735565057943
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735565057943-Bind-Data-Dialog-Box
updated_at: 2022-11-02T08:20:19Z
---

# Bind Data Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513176343-Barcode-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513195031-Bursting-Dialog-Box)

# Bind Data Dialog Box

You can use the Bind Data dialog box to [bind a dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#BindData) to the report body. This topic describes the options in the dialog box.

Designer displays the Bind Data dialog box when you do one of the following:

* Navigate to Report > Bind Data.
* Right-click any blank area in the report body and select Bind Data from the shortcut menu.
* Select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/7933662747415/btn_fmla.gif) to specify a formula to return value to some page properties for a page report tab in the General tab of the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box) or via the [Page Panel object](https://devnet.logianalytics.com/hc/en-us/articles/5735533484311-Page-Panel-Properties) in the Report Inspector, or to![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/7933688209431/___newv19.1.png "New for version 19.1.")some Excel properties of a page report tab or web report, but you have not bound a dataset to the report body, then select OK in the message box.

Designer provides you with different options in the dialog box for binding data to a [page/web report](#Report) or a [library component](#LC).

## For Binding Data to a Page/Web Report

![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933690155799/bddt.gif)

Designer displays these options:

**New Dataset**

Select to create a dataset based on a data resource in the current catalog. The data resource box on the right lists the predefined data resources in the catalog. Select the data resource you want to bind to the report body. Designer then automatically creates a dataset based on the specified data resource in the report.

* **<New XXX...>**/**<Add XXX...>**  
  Select to create or add a data resource of the same type in the catalog.

**Existing Dataset**

Select to use a dataset from the ones that you have created in the report.

* **<New Dataset...>**  
  Select to create a dataset using the [New Dataset dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735566804375-New-Dataset-Dialog-Box).

**Current Dataset**

Designer disables this option because the report body cannot use inherited dataset.

**Less Options**/**More Options**

Select to hide or show the dataset selection panel to choose a dataset to bind to the report body.

**Edit**

Select to modify the specified query in the [Query Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552449687-Query-Editor-Dialog-Box), ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/7933646501655/___newv19.png "New for version 19.")business view in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508168471-Business-View-Editor-Dialog-Box), or dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529002007-Dataset-Editor-Dialog-Box).

**OK**

Select to bind the specified dataset to the report body and close the dialog box.

**Cancel**

Select to quit binding data to the report body and close the dialog box.

**Help**

Select to view information about the dialog box.

## For Binding Data to a Library Component

![Bind Data dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933690165015/bddt_bv.gif)

Designer displays these options:

**Available data resources**

This box lists the predefined business views in the current catalog. Select the business view you want to bind to the report body. Designer then automatically creates a dataset based on the specified business view in the library component.

**OK**

Select to bind the specified dataset to the report body and close the dialog box.

**Cancel**

Select to quit binding data to the report body and close the dialog box.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735513176343-Barcode-Expert-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513195031-Bursting-Dialog-Box)
