---
title: "JSON Connection Wizard Dialog Box"
id: 28898139314829
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898139314829-JSON-Connection-Wizard-Dialog-Box
updated_at: 2024-09-30T09:08:03Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
JSON Connection Wizard Dialog Box

You can use the JSON Connection Wizard dialog box to get data from a JSON data source in a catalog. This topic describes the options in the dialog box.
    

 Designer displays the JSON Connection Wizard dialog box when you select JSON and select OK in the New Data Source dialog box; or in the Catalog Manager, right-click a data source and select New JSON Connection from the shortcut menu, or right-click an existing JSON connection and select Edit Connection from the shortcut menu.

The dialog box contains the following screens:

- Extract JSON Schema Screen

- Modify Schema Properties Screen

- Transformed Relational Schema Screen

- Add Table Screen

Designer displays these buttons in all the screens:

Back

Select to go back to the previous screen.

Next

Select to go to the next screen.

Finish

Select to finish your work and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
Extract JSON Schema Screen

Use this screen to specify the information to extract the JSON schema.

Schema Source

Select the source to extract the JSON schema: Extract Schema from Sample Data or Extract Schema from Instance Data.

Designer displays different options in the Extract JSON Schema screen to specify the schema according to the schema source you select.

- 
When you select the Schema Source option of "Extract Schema from Sample Data", Designer displays these options:
    Sample Data

Specify the sample data file from which to extract the JSON schema. You can select Browse to specify the sample data file from your local disk or type the URI string of the file in the text box.

- 
RESTful
Designer enables this button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the RESTful Data Source Options dialog box to define RESTful options for the sample data.

URI

Select to get instance data from URI.

- 
Instance
Specify the JSON instance file. You can select Browse to specify the instance file from your local disk or type the URI string of the file in the text box.      
- 
New parameter button
Select to open the New Parameter dialog box to create a parameter in the current catalog data source and reference it in the URI string to dynamically specify the instance.

- 
RESTful
Select to open the RESTful Data Source Options dialog box to define RESTful options for the instance data.

User Defined

Select to get instance data from user-defined interface.

- 
Class Name
Specify the full name (including package name) of the class. You can select Browse to specify the class file from your local disk or  type the class name with package name in the text box. You need to append the class to the class path in the system environment.

- 
The class implements
After you fill in the Class Name text box, Designer displays the class name of the interface that the class implements here.

- 
Parameter
Specify the parameter string for the user-defined data interface. The parameter string must match the format defined in the class.

Paginated

Select to get paginated instance data from a REST Web Service.

- 
User Name
Specify the user name for remote data authentication.

- 
Password
Specify the password for remote data authentication.

- 
Main Formula
Select the main formula that defines   how you want to fetch the pagination data.
- 
New Formula
Select to open the Formula Editor dialog box to compose the formula.

- 
Edit button
Select to edit the specified formula.

- 
Delete button
Select to delete the specified formula.

- 
When you select the Schema Source option of "Extract Schema from Instance Data", Designer displays these options:  
    Instance

Specify the JSON instance file. You can select Browse to select the instance file or type the URI string of the file in the text box.

- 
RESTful
Designer enables this button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the RESTful Data Source Options dialog box to define RESTful options for the instance data.

Edit Format

Select to open the Edit Format dialog box to specify the value formats of the referenced parameters and formulas.

- 
Name
This column shows the names of the parameters and formulas.

- 
Format
This column shows the value formats that you specify for the parameters and formulas.

- 
OK
Select to apply the changes and close the dialog box.

- 
Cancel
Select to close the dialog box without saving any changes.

Refresh

Designer displays this button when you use the dialog box for editing an existing JSON connection. After you make changes in the dialog box and select the Refresh button, Designer reloads the JSON schema information according to what you have changed.

## 
Modify Schema Properties Screen

Use this screen to specify properties of the JSON schema.

Schema

This box lists the corresponding schema structure of the root.  stands for elements.

Properties

This box lists properties and values of the properties for the selected element in the schema.

## 
Transformed Relational Schema Screen

This screen displays the relational tables Designer builds based on the transformed relational schema structure.

## 
Add Table Screen

Use this screen to add tables that Designer transforms from the JSON data source to the connection. Designer does not display the screen when you use the dialog box for editing an existing JSON connection. 

Tables

This box lists the tables that Designer transforms from the JSON data source.

Added Tables

This box lists the tables that you  add to use in the JSON connection.

Add button

Select to add the specified tables in the Tables box to the JSON connection.

Remove button

Select to remove the specified tables from the Added Tables box.

Previous Topic  Next Topic
