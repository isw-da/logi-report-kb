---
title: "Example: Creating an NLS Report"
id: 45190619902733
section: "Applying National Language Support - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190619902733-Example-Creating-an-NLS-Report
updated_at: 2026-04-30T15:15:19Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Example: Creating an NLS Report

This topic presents an example to show how you can make an English report display in Chinese. 

This example contains the following tasks:

- Task 1: Create an NLS property file 

- Task 2: Create a data mapping file

- Task 3: Publish the report to Server

- Task 4: Apply NLS to the report at runtime

Task 1: Create an NLS property file

- Navigate to File > Open to open the web report Sales Detail Report.wls in the catalog file SampleReports.cat in <install_root>\Demo\Reports\SampleReports.

- Select the node Filter Control representing the filter control PRODUCT TYPE in the Report Inspector and set the Map Name property to true. Select the nodes Filter Control 1 and Filter Control 2 representing the filter controls CATEGORY and PRODUCT NAME respectively in the Report Inspector, and you can find their Map Name property is false.
     When you set the Map Name property of a filter control to "true", its title, namely, the value of its Text property is the same as the bound field's Name property in the Catalog Manager and you cannot change it, and its type in the NLS Editor dialog box is "Metadata"; otherwise, its  Text property in the Report Inspector is editable, and its type in the NLS Editor dialog box is "Title".

- Navigate to View > Language > NLS Editor. Designer displays the NLS Editor dialog box.

- Select Add above the Language box.

- In the Add Language dialog box, select Chinese (China) from the Available Languages list and select OK to add the language and return to the NLS Editor dialog box.

- In the Display tab, Designer lists the scope and types of the objects in the report and the items you need to translate in the Scope, Type, and Key columns. You can see that only the type of the filter controls CATEGORY and PRODUCT NAME is "Title".
    

- Specify all the corresponding target language text in the Translate in Chinese column and select OK.
    

Task 2: Create a data mapping file

- On the Catalog Manager toolbar, select the Data Mapping Editor. Designer displays the Data Mapping Editor dialog box.

- Select New, then in the Create Data Mapping File dialog box, type DataMapping in the File Name text box, select Chinese (China) from the Language drop-down list and select OK  to return to the Data Mapping Editor dialog box.
    

- Select Import Key.

- In the Import Key dialog box, select the following fields the report uses one by one: Country and Region in the Customers table; Category, Product Name, and Product Type Name (the Product Type field in the report) in the Products table. Select OK.
    

- Double-click cells in the Map to Value column to specify the mapping values for the imported fields to Chinese. Select OK.
    

- In the Catalog Manager, select Show Properties on the toolbar to display the Properties sheet.

- Select the Category field in the Products table, then find its Data Mapping File property and select DataMapping as the value.

- Repeat the preceding step to set the Data Mapping File property of the fields Product Name and Product Type Name to DataMapping. 

- Select Save Catalog on the Catalog Manager toolbar to save the changes.

- In the design area, select the chart legend and the Region field in the crosstab and set their Data Mapping File property to DataMapping in the Report Inspector too.
    

- Save the report.

You may notice that you can specify the Data Mapping File property in both the Catalog Manager and the Report Inspector, meaning, you can specify the data mapping file of a field a report uses at both the catalog level and report level. When you specify the property at both levels, the data mapping file you set in the Report Inspector has higher priority.

Task 3: Publish the report to Server

By now, you have finished creating the NLS property file and the corresponding data mapping file and applied them to Sales Detail Report.wls. Publish the report and the catalog it uses to Server. See Publishing Resources Remotely.

Task 4: Apply NLS to the report at runtime

- Sign in to the Server Console.

- In the Start Page, select  My Profile under the Manage category. Server displays the My Profile > Customize Server Preferences page.

- Switch to the Advanced tab, select Yes for the Enable NLS option and select Chinese (China) from the Default Language drop-down list. Select OK.
    

- Access the Resources page of the  Server Console.

- Locate the web report Sales Detail Report.wls you published and run it in Web Report Studio. The report displays in Chinese.

- Select Edit Mode from the mode drop-down menu on the Web Report Studio toolbar.

- Select the chart or the crosstab, Web Report Studio then displays the business view it uses in the Resources panel. You can see all resources in the resource tree  display as you translated for the metadata objects in the NLS Editor in Designer.
