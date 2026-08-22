---
title: "Edit Hierarchical Data Source Dialog"
id: 1500009630741
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630741-Edit-Hierarchical-Data-Source-Dialog
updated_at: 2021-07-24T16:04:47Z
---

# Edit Hierarchical Data Source Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630721-Edit-Group-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607922-Edit-Line-Style-Dialog)

# Edit Hierarchical Data Source Dialog

The Edit Hierarchical Data Source dialog helps you to [edit an HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009629501-Adding-Hierarchical-Data-Sources-to-a-Catalog) in a catalog. It appears when you right-click a hierarchical data source and select Edit Hierarchical Data Source from the shortcut menu in the Catalog Manager.

The dialog varies according to the type of the HDS, [general HDS](#General) or [XML HDS](#XML).

---

When the HDS you are to edit is a general HDS, this dialog displays as follows:

![Edit Hierarchical Data Source dialog for general HDS](https://devnet.logianalytics.com/hc/article_attachments/4404904349335/edthds_gnrl.gif)

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
   Specifies the precision of the column's values. The default value comes from data source metadata and it specifies the column's largest number of digits. The larger the precision is, the more memory it might take, however, the more accurate values you will get.
* **Scale**  
   Specifies the number of digits to the right of the decimal point for the column's values.
* **Nullable**  
   Specifies whether the column is nullable. You have three options to choose: Nullable, No Nulls and Nullable Unknown.
* **Currency**  
   Specifies whether to use the Currency type for this column or not
* **Array**  
   Specifies whether to use the Array type for this column or not.

**Load Tree**

Parses and loads data tree from the external data source file. The structure is shown in the Structure box after you select this button.

**OK**

Applies all changes here and close the dialog.

**Cancel**

Does not retain changes and closes the dialog.

**Help**

Displays the help document about this feature.

---

When the HDS you are to edit is an XML HDS, the dialog displays as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4404904349847/edthds_xml.gif)

**XML URI**

Specifies the location of the external XML format data source. Can be a local path or a web url. Select Browse to find the file on the local disk.

**XSD URI**

Specifies the location of the schema file for the XML format data source. Can be a local path or a web url. Select Browse to find the file on the local disk.

**Root Name**

Indicates the HDS root, starting from which Logi Report Designer imports the data.

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
   Specifies the precision of the column's values. The larger the precision is, the more memory it might take, however, the more accurate values you will get.
* **Scale**  
   Specifies the number of digits to the right of the decimal point for the column's values.
* **Nullable**  
   Specifies whether the column is nullable. You have three options to choose: Nullable, No Nulls and Nullable Unknown.
* **Currency**  
   Specifies whether to use the Currency type for this column or not
* **Array**  
   Specifies whether to use the Array type for this column or not.

**Load Tree**

Parses and loads data tree from the external data source file. The structure is shown in the Structure box after you select this button.

**OK**

Applies all changes here and closes the dialog.

**Cancel**

Does not retain changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630721-Edit-Group-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009607922-Edit-Line-Style-Dialog)
