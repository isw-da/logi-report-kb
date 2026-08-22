---
title: "Mapping Data Values to Different Languages"
id: 1500009590001
section: "Applying National Language Support - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590001-Mapping-Data-Values-to-Different-Languages
updated_at: 2021-07-24T05:54:31Z
---

# Mapping Data Values to Different Languages

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568522-NLS-at-Report-Level)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568562-Creating-NLS-Property-Files)

# Mapping Data Values to Different Languages

With the [Data Mapping Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009565102-Data-Mapping-Editor-Dialog), you can create data mapping files to map data values of resources in a catalog to a specific language as you like. A data mapping file is a property file used to store the target language information for resources in a catalog (DBFields, parameters, summaries, formulas, table/view/synonym columns, imported SQL columns and so on). One data mapping file stores one language, and the name of the file is in the format "FileName\_language\_locale.properties". The abbreviations of the language and locale are used in the mapping file name. For example, the German mapping file name will be like this: FileName\_de\_DE.properties. The lower case "de" indicates the language is German, the upper case "DE" indicates the region is Germany. If all German regions can use the same file then the file name can be just FileName\_de.properties.

Below is a list of the sections covered in this topic:

> * [Creating a Data Mapping File](#Create)
> * [Editing a Data Mapping File](#Edit)
> * [Applying a Data Mapping File](#Apply)

## Creating a Data Mapping File

To create a data mapping file, that is to map the data values of resources in a catalog to a specific language, follow the steps below:

1. On the Catalog Manager toolbar, select the **Data Mapping Editor**  button to display the [Data Mapping Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009565102-Data-Mapping-Editor-Dialog).

   ![Data Mapping Editor](https://devnet.logianalytics.com/hc/article_attachments/4404889304343/dtmpedtr.gif)
2. Select the **New** button and the [Create Data Mapping File](https://devnet.logianalytics.com/hc/en-us/articles/1500009586061-Create-Data-Mapping-File-Dialog) dialog appears.

   ![Create Data Mapping File dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893831191/crtdtmpfile.gif)
3. In the File Name field, specify the name of the mapping file.
4. Select the **Language** drop-down list and select to which language the data values in the catalog will be mapped.
5. Select **OK**, and a property file will then be created in the folder where the catalog file is.
6. In the Data Mapping Editor, select the **Import Key** button to import the resources with the data values you want to map from the Import Key dialog.

   ![Import Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893831447/nls_rpt_map.gif)
7. Double-click cells in the Map to Value column to specify the mapping values for the imported resources according to the selected language. Use the quick search toolbar to locate the desired values in the value list if needed.
8. From the Import Key dialog, you can only import part of the resources in a catalog. If you want to map values of other resources like summaries, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a mapping line and specify the value in the Current Value column and Map to Value column accordingly.
9. When done, select **OK** to accept the changes and close the dialog.

## Editing a Data Mapping File

**To edit an existing data mapping file:**

1. In the Data Mapping Editor, select the **Load** button.
2. In the Load Data Mapping File dialog, select the data mapping file you want to edit and select **Open**.
3. Information that has been saved in the file is then loaded in the Data Mapping Editor. You can import/add more values to map, or delete some by selecting ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif).
4. When done, select **OK** to finish editing.

## Applying a Data Mapping File

A data mapping file can be applied to the following objects:

* Objects in a catalog: table/view/synonym columns, aggregation objects, detail objects and group objects in business views, stored procedure columns, imported SQL columns, UDS columns, HDS columns, formulas, summaries and parameters.
* Objects in a report: DBFields, formulas, summaries, parameters and special fields.

**To apply a data mapping file to objects in a catalog:**

1. Make sure that the option Forbid editing data object properties in the Catalog category of the Options dialog is unchecked so that the object property values in the Catalog Manager can be changed.
2. Open the catalog and select the node that represents the object to which you want to apply the data mapping file.
3. In the Properties sheet, set the data mapping file name (without the language and locale part) of the object as the value of the property Data Mapping File. For example, if the data mapping file name is Category\_de\_DE.properties, set the property value as Category.

**To apply a data mapping file to objects in a report:**

1. Open the report, then in Report Inspector, select the node that represents the object to which you want to apply the data mapping file.
2. In the Properties sheet, set the data mapping file name (without the language and locale part) of the object as the value of the property Data Mapping File. For example, if the data mapping file name is Category\_de\_DE.properties, set the property value as Category.

   The data mapping file cannot take effect now because there is no NLS property file for the report. You have to create a corresponding NLS property file for the report using the NLS Editor. For details, see [Creating NLS Property Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009568562-Creating-NLS-Property-Files).

**Note:** When the same object is applied with a data mapping file both at the catalog level and report level, the file specified at the report level for the object has the higher priority. However, in the following two cases, if you want to apply a data mapping file to the object, you need to specify the file at the report level. The data mapping file specified at the catalog level cannot work under these two circumstances.

* When the object is used as group by field in a table or banded object and a special function or special group is applied to it.
* When the object is added as the category or series field in a chart and any text or mapping format is specified for it.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568522-NLS-at-Report-Level)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568562-Creating-NLS-Property-Files)
