---
title: "Mapping Data Values to Different Languages"
id: 1500009634461
section: "Applying National Language Support - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634461-Mapping-Data-Values-to-Different-Languages
updated_at: 2021-07-24T16:03:51Z
---

# Mapping Data Values to Different Languages

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611382-NLS-at-Report-Level) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611442-Creating-NLS-Property-Files)

# Mapping Data Values to Different Languages

Using the Data Mapping Editor, you can create data mapping files to map data values of resources in a catalog to a specific language as you like.

A data mapping file is a property file used to store the target language information for resources in a catalog (DBFields, parameters, summaries, formulas, table/view/synonym columns, imported SQL columns, and so on). One data mapping file stores one language, and the name of the file is in the format "FileName\_language\_locale.properties". The abbreviations of the language and locale are used in the mapping file name. For example, the German mapping file name will be like this: FileName\_de\_DE.properties. The lower case "de" indicates the language is German, the upper case "DE" indicates the region is Germany. If all German regions can use the same file then the file name can be just FileName\_de.properties.

This topic includes the following sections:

> * [Creating a Data Mapping File](#Create)
> * [Applying a Data Mapping File](#Apply)

## Creating a Data Mapping File

To create a data mapping file, that is to map the data values of resources in a catalog to a specific language, follow the steps below:

1. On the Catalog Manager toolbar, select the **Data Mapping Editor**  button. The [Data Mapping Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607702-Data-Mapping-Editor-Dialog) appears.

   ![Data Mapping Editor](https://devnet.logianalytics.com/hc/article_attachments/4404911660311/dtmpedtr.gif)
2. Select the **New** button and the [Create Data Mapping File](https://devnet.logianalytics.com/hc/en-us/articles/1500009607542-Create-Data-Mapping-File-Dialog) dialog appears.

   ![Create Data Mapping File dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904217495/crtdtmpfile.gif)
3. In the File Name field, specify the name of the mapping file.
4. Select the **Language** drop-down list and select to which language the data values in the catalog will be mapped.
5. Select **OK**, and a property file will then be created in the folder where the catalog file is.
6. In the Data Mapping Editor, select the **Import Key** button to import the resources with the data values you want to map from the Import Key dialog.

   ![Import Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911660567/nls_rpt_map.gif)
7. Double-click cells in the Map to Value column to specify the mapping values for the imported resources according to the selected language.
8. From the Import Key dialog, you can only import part of the resources in a catalog. If you want to map values of other resources like summaries, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a mapping line and specify the value in the Current Value column and Map to Value column accordingly.
9. When done, select **OK** to accept the changes and close the dialog.

If you want to edit any existing data mapping file, in the Data Mapping Editor, select the **Load** button,in the Load Data Mapping File dialog select the data mapping file and select **Open**. Information that has been saved in the file is then loaded in the Data Mapping Editor. Edit the values as required.

## Applying a Data Mapping File

A data mapping file can be applied to the following objects:

* Objects in a catalog: table/view/synonym columns, aggregation objects, detail objects and group objects in business views, stored procedure columns, imported SQL columns, imported APE columns, UDS columns, HDS columns, formulas, summaries and parameters.
* Objects in a report: DBFields, formulas, summaries, parameters and special fields.

**To apply a data mapping file to objects in a catalog:**

1. Open the catalog and select the node that represents the object to which you want to apply the data mapping file.
2. In the Properties sheet, set the data mapping file name (without the language and locale part) of the object as the value of the property Data Mapping File. For example, if the data mapping file name is Category\_de\_DE.properties, set the property value as Category.

**To apply a data mapping file to objects in a report:**

1. Open the report, then in Report Inspector, select the node that represents the object to which you want to apply the data mapping file.
2. In the Properties sheet, set the data mapping file name (without the language and locale part) of the object as the value of the property Data Mapping File. For example, if the data mapping file name is Category\_de\_DE.properties, set the property value as Category.

   The data mapping file cannot take effect now because there is no NLS property file for the report. You have to create a corresponding NLS property file for the report using the NLS Editor. For details, see [Creating NLS Property Files](https://devnet.logianalytics.com/hc/en-us/articles/1500009611442-Creating-NLS-Property-Files).

**Note:** When the same object is applied with a data mapping file both at the catalog level and report level, the file specified at the report level for the object has the higher priority. However, in the following two cases, if you want to apply a data mapping file to the object, you need to specify the file at the report level. The data mapping file specified at the catalog level cannot work under these two circumstances.

* When the object is used as group-by field in a table or banded object and a special function or special group is applied to it.
* When the object is added as the category or series field in a chart and any text or mapping format is specified for it.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611382-NLS-at-Report-Level) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611442-Creating-NLS-Property-Files)
