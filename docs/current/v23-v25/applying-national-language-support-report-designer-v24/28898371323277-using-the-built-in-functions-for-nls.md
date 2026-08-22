---
title: "Using the Built-in Functions for NLS"
id: 28898371323277
section: "Applying National Language Support - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898371323277-Using-the-Built-in-Functions-for-NLS
updated_at: 2024-09-30T09:12:02Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Using the Built-in Functions for NLS

Report provides two built-in Translate functions for applying NLS to the formula result. This topic introduces the two functions briefly and presents an example to show the usage of the functions.

This topic contains the following sections:

- The Translate Functions

- Example: Calling the Translate Functions in a Formula

## 
The Translate Functions

You can call the following Translate functions in formulas to display the formula result in another language.

- 
Translate(String a)
This function searches for the NLS translation of the current field values in the bound data mapping file.

- 
Translate(String a, String b)
This function accesses the corresponding data mapping file dynamically according to the language you select from the language drop-down list on the NLS language toolbar and searches for the NLS translation of "String b" in it.

## 
Example: Calling the Translate Functions in a Formula

This example shows how you can call a Translate function in a formula to display the formula result in Chinese.

- Navigate to Home > Open to open the page report List of Customer Contact Cards.cls in the catalog file SampleReports.cat saved in <install_root>\Demo\Reports\SampleReports.

- Select the View tab to preview the report. 

- Select the Design tab to return to design mode. 

- Navigate to View > Language > NLS Editor.

- In the NLS Editor dialog box, select Add above the Language box.

- In the Add Language dialog box, select Chinese (China) from the Available Languages list and select OK to add it to the Language box of the NLS Editor dialog box.
    

-  Select OK in the NLS Editor dialog box.

- Open the Catalog Manager and select Data Mapping Editor on its toolbar.

- In the Data Mapping Editor dialog box, select New.

- In the Create Data Mapping File dialog box, type DataMapping in the File Name text box and select Chinese (China) from the Language drop-down list. Select OK to go back to the Data Mapping Editor dialog box.
    

- Select Import Key.

- In the Import Key dialog box, select the City and State fields in the Customers table and select OK.
    

- In the Data Mapping Editor dialog box, double-click cells in the Map to Value column to specify the mapping values for the two fields in Chinese. Select OK.

- Navigate to the Data Source 1 > jdbc connection > Tables > Customers node in the Catalog Manager, select the City column, select Show Properties to expand the Properties sheet on the right, then select DataMapping from the Data Mapping File property value drop-down list.

- Repeat the preceding step to set the Data Mapping File property of the State column in the same table to DataMapping.

- Select Save Catalog on the Catalog Manager toolbar to save the changes.

- Right-click the CustomerCityStateZip formula field in the report and select Edit from the shortcut menu. The formula expression is:
    

- Edit the formula to Translate(@City) + ", " + Translate(@State) + "  " + Translate(@"Postal Code"), then select Save on the toolbar to save the formula. Close the Formula Editor dialog box.
    

If you have not set the data mapping file of the two table columns, you can also edit the formula as follows to apply the NLS feature:

Translate("DataMapping", @City)+ ", " +Translate("DataMapping", @State) + "  " + Translate("DataMapping", @"Postal Code").

To completely display the Chinese characters in the report, next we need to edit the font properties for the CustomerCityStateZip formula field.

- Select CustomerCityStateZip in the report again, then set its Font Face property to  SimSun and Font Size property to 12 in the Report Inspector.
  

- Save the report. 
  

- Navigate to View > Language > Chinese (China).

- Preview the report again. Designer displays the formula result in Chinese.

- When you call either of the two Translate functions in a formula, you should not use the formula to perform further calculation unless you can make sure it is correct.

- When a formula references a parameter and the parameter's Allow Multiple Values property is "true", the two Translate functions are not available in the Formula Editor dialog box. In this case, if you want to apply NLS in the formula result, you can bind the data mapping file to the formula directly.

- You can also call the two Translate functions in formulas on Server, but they take effect only when the bound data mapping file exists on Server. Moreover, only when you have applied the data mapping file  in Designer, you can publish it to Server together with the object it is bound to.

Previous Topic  Next Topic
