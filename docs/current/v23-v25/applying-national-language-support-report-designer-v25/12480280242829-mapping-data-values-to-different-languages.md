---
title: "Mapping Data Values to Different Languages"
id: 12480280242829
section: "Applying National Language Support - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480280242829-Mapping-Data-Values-to-Different-Languages
updated_at: 2026-02-25T23:48:20Z
source_host: docs-report.zendesk.com
---
# 
Mapping Data Values to Different Languages

Using the Data Mapping Editor, you can create data mapping files to map data values of objects in a catalog to other languages. This topic introduces data mapping files and describes how you can create and apply them to display data values in the languages you want.

This topic contains the following sections:

- What Are Data Mapping Files?

- Creating a Data Mapping File

- Applying a Data Mapping File

## 
What Are Data Mapping Files?

A data mapping file is a property file that stores the target language information for objects in a catalog (DBFields, parameters, summaries, formulas, table/view/synonym columns, imported SQL columns, and so on). One data mapping file stores one language, and the name of the file is in the format FileName_language_country.properties. Designer uses the two-letter codes of the language and country as defined by ISO-639 and ISO-3166 in the mapping file name. For example, the German mapping file name is FileName_de_DE.properties. The lowercase "de" indicates the language is German, and the uppercase "DE" indicates the country is Germany. If all countries speaking German can use the same file, the file name can be just FileName_de.properties.

## 
Creating a Data Mapping File

To create a data mapping file, that is, to map the data values of objects in a catalog to a specific language, take the following steps:

- On the Catalog Manager toolbar, select Data Mapping Editor. Designer displays the Data Mapping Editor dialog box. 
    

- Select New to open the Create Data Mapping File dialog box.
    

- In the File Name text box, type the name of the mapping file. 

- Select the Language drop-down list and select to which language you want to map the data values in the catalog.

- Select OK. Designer then creates a property file  in the folder where the catalog file is.

- In the Data Mapping Editor dialog box, select Import Key.

- In the Import Key dialog box, select the objects the data values of which you want to map. Select OK to close the dialog box and return to the Data Mapping Editor dialog box.    

- Double-click cells in the Map to Value column to specify the mapping values for the imported objects according to the selected language.

- From the Import Key dialog box, you can only import part of the objects in a catalog. If you want to map values of other objects like summaries, select Add to add a mapping line and specify the value in the Current Value column and Map to Value column accordingly.

- Select OK to accept the changes and close the dialog box.

If you want to edit any existing data mapping file, in the Data Mapping Editor dialog box, select Load. In the Load Data Mapping File dialog box, select the data mapping file and select Open. Designer loads the information you have saved in the file in the Data Mapping Editor dialog box. Edit the values according to your requirements. 

## 
Applying a Data Mapping File

You can apply a data mapping file to the following objects:

- Objects in a catalog: table/view/synonym columns, aggregation objects, detail objects and group objects in business views, stored procedure columns, imported SQL columns, imported APE columns, UDS columns, HDS columns, formulas, summaries, and parameters.

- Objects in a report: DBFields, formulas, summaries, parameters, and special fields.

To apply a data mapping file to objects in a catalog

- Open the catalog.

- Select the node that represents the object to which you want to apply the data mapping file.

- In the Properties sheet, set the data mapping file name (without the locale part)  as value of the object's Data Mapping File property. For example, if the data mapping file is Product_de_DE.properties, type Product in the value cell.

To apply a data mapping file to objects in a report

- Open the report.

- In the Report Inspector, select the node that represents the object to which you want to apply the data mapping file.

- In the Properties sheet, set the data mapping file name (without the locale part) as value of the object's Data Mapping File property. For example, if the data mapping file is Product_de_DE.properties, type Product in the value cell.

The data mapping file cannot take effect now because there is no NLS property file for the report. You have to create a corresponding NLS property file for the report using the NLS Editor. See Creating NLS Property Files.

 When you apply a data mapping file to the same object both at catalog level and report level, the file specified at report level has higher priority. However, in the following two cases, if you want to apply a data mapping file to the object, you need to specify the file at report level. The data mapping file specified at catalog level cannot work under these two circumstances.

- When you use the object as the group-by field in a table or banded object and apply a special function or special group  to it.

- When you use the object as the category or series field in a chart and specify any text or mapping format for it.
