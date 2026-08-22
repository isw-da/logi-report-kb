---
title: "Edit Hierarchical Data Source Dialog"
id: 1500009565322
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565322-Edit-Hierarchical-Data-Source-Dialog
updated_at: 2021-07-24T05:55:25Z
---

# Edit Hierarchical Data Source Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565302-Edit-Group-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565342-Edit-Line-Style-Dialog)

# Edit Hierarchical Data Source Dialog

The Edit Hierarchical Data Source dialog appears when you right-click a hierarchical data source and select Edit Hierarchical Data Source from the shortcut menu in the Catalog Manager. It helps you to [edit an HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog) in a catalog.

When the HDS you are to edit is a general HDS, this dialog displays [as follows](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893924759/edthds_gnrl.gif)

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

Applies all changes here and close the dialog.

**Cancel**

Does not retain changes and closes the dialog.

**Help**

Displays the help document about this feature.

When the HDS you are to edit is an XML HDS, this dialog displays [as follows](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889368471/edthds_xml.gif)

**XML URI**

Specifies the location of the external XML format data source. Can be a local path or a web url. Select Browse to find the file on the local disk.

**XSD URI**

Specifies the location of the schema file for the XML format data source. Can be a local path or a web url. Select Browse to find the file on the local disk.

**Root Name**

Indicates the HDS root, starting from which Logi JReport Designer imports the data.

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565302-Edit-Group-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565342-Edit-Line-Style-Dialog)
