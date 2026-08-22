---
title: "New General Hierarchical Data Source Dialog Box"
id: 5735543777943
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735543777943-New-General-Hierarchical-Data-Source-Dialog-Box
updated_at: 2022-11-02T07:53:11Z
---

# New General Hierarchical Data Source Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735530467735-New-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box)

# New General Hierarchical Data Source Dialog Box

You can use the New General Hierarchical Data Source dialog box to [add a general HDS](https://devnet.logianalytics.com/hc/en-us/articles/5735499355159-Adding-Hierarchical-Data-Sources-to-a-Catalog#General) in the current catalog. This topic describes the options in the dialog box.

Designer displays the New General Hierarchical Data Source dialog box when you right-click a data source node and select New General Hierarchical Data Source from the shortcut menu in the Catalog Manager.

![New General Hierarchical Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898478537367/nwhds.gif)

Designer displays these options:

**Class Name**

Specify the name of the entrance class that implements the HDS APIs. The class should be in the class path in the system environment. Select **Browse** to specify the class.

**Parameter**

Specify the parameter string that is required by the class, if any. The parameter string must match the format defined in the HDS class.

**Structure**

This box shows the structure of the hierarchical data source.

**Columns**

You can specify the column settings in this box.

* **Element**  
  This column shows the names of the columns in the selected node of table.
* **Selected**  
  Specify whether to import the column into the catalog.
* **Format**  
  Specify the format to display the column values in reports. It varies for different data types, and you can manually define the format.
* **Type**  
  Specify the data type of the column.
* **Precision**  
  Specify the precision of the column's values. The default value comes from data source metadata and it specifies the column's largest number of digits. The larger the precision is, the more memory it might take, while the more accurate values you get.
* **Scale**  
  Specify the number of digits to the right of the decimal point for the column's values.
* **Nullable**  
  Specify whether the column is nullable. You have three options to choose: Nullable, No Nulls, and Nullable Unknown.
* **Currency**  
  Specify whether to use the Currency data type for this column.
* **Array**  
  Specify whether to use the Array data type for this column.

**Load Tree**

Select to parse and load data tree from the external data source file. Designer displays the structure in the Structure box after you select this button.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735530467735-New-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box)
