---
title: "Edit Hierarchical Data Source Dialog Box"
id: 1500010096281
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096281-Edit-Hierarchical-Data-Source-Dialog-Box
updated_at: 2021-07-23T19:15:17Z
---

# Edit Hierarchical Data Source Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058762-Edit-Group-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096321-Edit-Line-Style-Dialog-Box)

# Edit Hierarchical Data Source Dialog Box

You can use the Edit Hierarchical Data Source dialog box to [edit an HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010095101-Adding-Hierarchical-Data-Sources-to-a-Catalog) in a catalog. This topic describes the options in the dialog box.

Designer displays the Edit Hierarchical Data Source dialog box when you right-click a hierarchical data source and select Edit Hierarchical Data Source from the shortcut menu in the Catalog Manager, and provides different options in the dialog box according to the type of the HDS: [general HDS](#General) or [XML HDS](#XML).

---

For a general HDS, Designer displays the following options in the dialog box:

![Edit Hierarchical Data Source dialog box for general HDS](https://devnet.logianalytics.com/hc/article_attachments/4404856976407/edthds_gnrl.gif)

**Class Name**

The option shows the name of the entrance class that implements the HDS APIs.

**Parameter**

Specify the parameter string that is required by the class, if any. The parameter string must match the format defined in the HDS class.

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

---

For an XML HDS, Designer displays the following options in the dialog box:

![](https://devnet.logianalytics.com/hc/article_attachments/4404848584983/edthds_xml.gif)

**XML URI**

The option shows the location of the external XML data source, which can be a local path or a web URL.

**XSD URI**

The option shows the location of the schema file for the XML data source, which can be a local path or a web URL.

**Root Name**

The option shows the HDS root, starting from which Designer imports the data.

**Structure**

The box shows the structure of the hierarchical data source.

**[Columns](#Columns)**

You can specify the column settings in this box.

**Load Tree**

Select to parse and load data tree from the external data source file. Designer displays the structure in the Structure box after you select this button.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058762-Edit-Group-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096321-Edit-Line-Style-Dialog-Box)
