---
title: "Filtering Datasets in a Report"
id: 28898608494093
section: "Manipulating Report Datasets - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898608494093-Filtering-Datasets-in-a-Report
updated_at: 2024-09-30T09:14:03Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Filtering Datasets in a Report

When you filter a dataset in a report, the filter conditions apply to all data components that use the dataset in the report. This topic describes how you can apply a filter to a dataset.

- Do one of the following to specify the dataset you want to filter:
- Navigate to Report > Manage Datasets, then in the Manage Datasets dialog box, select the dataset in the Dataset List box and select the Filter tab.

- When working with a page or web report, in the dialog box where you can select to use an existing dataset in the report (for example, the Bind Data dialog box, Choose Data dialog box, or the Data screen of the component wizard), select an existing dataset and select Edit, then in the Dataset Editor dialog box, select the Filter tab.

- When working with a page or web report, select a dataset from the dataset drop-down list of the Data panel or select a data component in the report to locate the dataset it applies in the Data panel, then select Dataset Filter on the toolbar of the panel. Designer displays the Dataset Filter dialog box for you to define the filter conditions.

- In the component wizard when working with a web report or business view-based page report, select the dataset you want to use for the data component in the Data screen and then select the  Dataset Filter screen.

- When working with a web report or business view-based page report, right-click a data component in the report and select Edit Dataset Filter from the shortcut menu. Designer displays the Edit Dataset Filter dialog box for you to define the filter conditions.

The following shows a sample dialog box.

- When the dataset is based on a business view, Designer displays the Filter drop-down list, which contains all predefined filters of the business view. You can select one from the drop-down list to apply to the dataset, or select User Defined in the list to define a new filter.

- Add the filter conditions. According to the data resource type from which the dataset is created, a business view or a query resource, the way to create a filter for the dataset varies.
- For a business view-based dataset, you can add filter condition for it in the same way as you add conditions for a predefined filter in the business view. Besides, you can use a local parameter as the value of a filter condition when editing the filter in the Dataset Filter or Edit Dataset Filter dialog box.

- 
To add filter conditions for a query-based dataset:         
- Select Add Condition to add a condition line.
            

- From the field drop-down list, select the field you want to filter. The field can be any DBField in the query resource, or a parameter or valid formula of these DBFields in the same catalog data source as the query resource.

- From the operator drop-down list, select the operator with which to compose the filter expression.

- Specify the value of how to filter the field

- Select the ellipsis to specify the value of how to filter the field in the Expressions dialog box or type the value in the value text box. You can also use the User Name special field or a parameter to filter the dataset dynamically. For the usage of parameters in filter conditions, see the example in Dynamically Filtering Queries.
            
- When you type the value, if multiple values are required, you should separate them with ","; if a value contains the character "," or "\", type the character as "\," or "\\".

- When the condition is based on a String field, you can apply an empty string as the value, by simply leaving the text box blank (value length=0).
     If you would like to filter space string (one or more spaces) and empty string, create a formula with the statement Trim(@Field) that transforms the spaces into empty string, then use the formula to replace the field itself in the condition.
    

- Repeat the preceding steps to define more condition lines and specify the logic relationship between the condition lines: "And" or "Or".

- To group some condition lines, select them and select Group, Designer then adds the selected condition lines  in one group and applies them as one line of filter expression (you can also group conditions and groups together).

- To take out any condition or group from a group, select it and select Ungroup.

- To adjust the priority of the condition lines, select it and select Up or Down.

- To delete a condition line, select it and select Delete.
            

 You cannot filter the following SQL type of data: Db.SQL_BINARY, Db.SQL_BLOB, Db.SQL_CLOB, Db.SQL_LONGVARCHAR, Db.SQL_LONGVARBINARY, Db.SQL_VARBINARY, and Db.SQL_OTHER.

Previous Topic  Next Topic
