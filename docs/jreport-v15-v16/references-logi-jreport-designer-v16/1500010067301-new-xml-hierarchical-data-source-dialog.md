---
title: "New XML Hierarchical Data Source Dialog"
id: 1500010067301
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067301-New-XML-Hierarchical-Data-Source-Dialog
updated_at: 2021-07-24T10:38:33Z
---

# New XML Hierarchical Data Source Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067281-New-View-Element-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031762-NLS-Editor-Dialog)

# New XML Hierarchical Data Source Dialog

The New XML Hierarchical Data Source dialog helps you to [import an XML HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010064221-Adding-Hierarchical-Data-Sources-to-a-Catalog#Import) into a catalog. It appears when you right-click a data source and select New XML Hierarchical Data Source from the shortcut menu in the Catalog Manager.

![New XML Hierarchical Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901192087/nwxmlhds.gif)

The following are details about options in the dialog:

**XML URI**

Specifies the location of the external XML format data source. Can be a local path or a web URL. Select Browse to find the file on the local disk.

**XSD URI**

Specifies the location of the schema file for the XML format data source. Can be a local path or a web URL. Select Browse to find the file on the local disk.

**Root Name**

Indicates the hierarchical data source root, starting from which Logi JReport Designer imports the data.

**Structure**

Shows the structure of the hierarchical data source.

**Columns**

Specifies settings for the columns.

* **Element**  
   Displays the field name in the selected node of table.
* **Selected**  
   Specifies whether to import the field into the catalog.
* **Format**  
   Specifies the format in which the field value is to be displayed in the report result. Varies for different types of data, and can be manually defined.
* **Type**  
   Specifies the data type of the column.
* **Precision**  
   Displays the default value for each SQL type automatically. Select the cell and modify the value if necessary.
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010067281-New-View-Element-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031762-NLS-Editor-Dialog)
