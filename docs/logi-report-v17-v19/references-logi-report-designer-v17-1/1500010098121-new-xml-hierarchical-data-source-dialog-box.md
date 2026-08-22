---
title: "New XML Hierarchical Data Source Dialog Box"
id: 1500010098121
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098121-New-XML-Hierarchical-Data-Source-Dialog-Box
updated_at: 2021-07-23T19:15:48Z
---

# New XML Hierarchical Data Source Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098101-New-View-Element-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059882-NLS-Editor-Dialog-Box)

# New XML Hierarchical Data Source Dialog Box

You can use the New XML Hierarchical Data Source dialog box to [import an XML HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010095101-Adding-Hierarchical-Data-Sources-to-a-Catalog#Import) into the current catalog. This topic describes the options in the dialog box.

Designer displays the New XML Hierarchical Data Source dialog box when you right-click a data source and select New XML Hierarchical Data Source from the shortcut menu in the Catalog Manager.

![New XML Hierarchical Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856906135/nwxmlhds.gif)

You see the following options in the dialog box:

**XML URI**

Specify the location of the external XML data source. It can be a local path or a web URL. Select the Browse button to find the file on the local disk.

**XSD URI**

Specify the location of the schema file for the XML data source. It can be a local path or a web URL. Select the Browse button to find the file on the local disk.

**Root Name**

The option shows the HDS root, starting from which Designer imports the data.

**Structure**

The box shows the structure of the hierarchical data source.

**Columns**

You can specify the column settings in this box.

* **Element**  
  The column shows the names of the columns in the selected node of table.
* **Selected**  
  Specify whether to import the column into the catalog.
* **Format**  
  Specify the format in which to display the column values in the report result. It varies for different data types, and you can manually define the format.
* **Type**  
  Specify the data type of the column.
* **Precision**  
  Specify the precision of the column's values. The default value comes from data source metadata and it specifies the column's largest number of digits. The larger the precision is, the more memory it might take; however, the more accurate values you will get.
* **Scale**  
  Specify the number of digits to the right of the decimal point for the column's values.
* **Nullable**  
  Specify whether the column is nullable. You have three options to choose: Nullable, No Nulls, and Nullable Unknown.
* **Currency**  
  Specify whether to use the Currency type for this column or not
* **Array**  
  Specify whether to use the Array type for this column or not.

**Load Tree**

Select to parse and load data tree from the external data source file. Designer displays the structure in the Structure box after you select this button.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098101-New-View-Element-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059882-NLS-Editor-Dialog-Box)
