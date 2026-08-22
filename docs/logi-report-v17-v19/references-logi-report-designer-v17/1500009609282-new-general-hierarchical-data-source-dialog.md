---
title: "New General Hierarchical Data Source Dialog"
id: 1500009609282
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009609282-New-General-Hierarchical-Data-Source-Dialog
updated_at: 2021-07-24T16:04:20Z
---

# New General Hierarchical Data Source Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609222-New-Data-Source-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632681-New-Parameter-Dialog)

# New General Hierarchical Data Source Dialog

The New General Hierarchical Data Source dialog helps you to [add a general HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009629501-Adding-Hierarchical-Data-Sources-to-a-Catalog#General) into a catalog. It appears when you right-click a data source node and select New General Hierarchical Data Source from the shortcut menu the Catalog Manager.

![New General Hierarchical Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904250519/nwhds.gif)

The following are details about options in the dialog:

**Class Name**

Specifies the name of the entrance class that implements the HDS APIs. The class should be in the class path in the system environment.

**Parameter**

Specifies the parameter string that is required by the class, if any. The parameter string must match the format defined in the HDS class.

**Structure**

Shows the structure of the hierarchical data source.

**Columns**

Specifies the column settings.

* **Element**  
   Displays the column name in the selected node of table.
* **Selected**  
   Specifies whether to import the column into the catalog.
* **Format**  
   Specifies the format in which the column values are to be displayed in the report result. Varies for different types of data, and can be manually defined.
* **Type**  
   Specifies the data type of the column.
* **Precision**  
   Displays the default value for each SQL type automatically. You can select the cell and modify the value.
* **Scale**  
   Specifies the decimal place.
* **Nullable**  
   Specifies whether the field is nullable. You have three options to choose: Nullable, No Nulls and Nullable Unknown.
* **Currency**  
   Specifies whether to use the Currency type for this field or not.
* **Array**  
   Specifies whether to use the Array type for this field or not.

**Load Tree**

Analyzes and loads data tree from the external data source file. The structure is shown in the Structure box after you select this button.

**OK**

Applies all changes here and closes the dialog.

**Cancel**

Does not retain changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609222-New-Data-Source-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632681-New-Parameter-Dialog)
