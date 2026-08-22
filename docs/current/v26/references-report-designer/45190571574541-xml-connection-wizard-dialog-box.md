---
title: "XML Connection Wizard Dialog Box"
id: 45190571574541
section: "References - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190571574541-XML-Connection-Wizard-Dialog-Box
updated_at: 2026-04-30T15:14:36Z
source_host: logi-report-v26.insightsoftware.com
---
# 
XML Connection Wizard Dialog Box

You can use the XML Connection Wizard dialog box to get data from an XML data source in a catalog. This topic describes the options in the dialog box.
    

Designer displays the XML Connection Wizard dialog box when you select XML and select OK in the New Data Source dialog box; or in the Catalog Manager, right-click a data source and select Add XML Connection from the shortcut menu, or right-click an existing XML connection and select Edit Connection from the shortcut menu.

The dialog box contains the following screens:

- Import XML Schema Screen

- Modify Schema Properties Screen

- Transform XML Schema Screen

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
Import XML Schema Screen

Use this screen to specify the information to import the XML schema.

Schema Type

Select the source to import the XML schema: Import from XSD or Parse from an XML Instance.

Schema Name

Specify the schema file. You can select Browse to specify the schema file from your local disk or type the URI string of the file in the text box.

- 
RESTful
Designer enables this button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the RESTful Data Source Options dialog box to define the RESTful options for the schema data.

Starting Node 

Select the starting node, according to the root name in the XML instance.

Instance

Specify the XML instance. You can select Browse to specify the instance file from your local disk or type the URI string of the file in the text box. The instance should match with the specified XSD schema.

- 
RESTful
Designer enables this button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the RESTful Data Source Options dialog box to define the RESTful options for the instance data.

Time Zone and Locale

Select to open the Time Zone and Locale Options dialog box to specify the default time zone and locale for the XML instance.

Edit Format

Select to open the Edit Format dialog box to specify value formats of the referenced parameters and formulas.

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

Designer displays this button when you use the dialog box for editing an existing XML connection. After you make changes in the dialog box and select the Refresh button, Designer reloads the XML schema information according to what you have changed.

Designer displays the following options when you select Import from XSD from the Schema Type drop-down list:

URI

Select to get instance data from URI.

User Defined

Select to get data from user-defined interface.
    

- 
Class Name
Specify the full name (including package name) of the class. You can select Browse to specify the class from your local disk or type the class name in the text box. You should have appended the class  to the class path in the system environment.

- 
The class implements
This option shows the class name of the interface that the class implements after you specify the Class Name option.

- 
Parameter
Specify the parameter string for the user-defined data interface. The parameter string must match the format defined in the class. 

New Parameter

Select to open the New Parameter dialog box to create a parameter in the current catalog data source. You can then reference the parameter to dynamically specify a URI or user-defined interface that matches with the selected XSD schema at runtime.

Validate with schema before fetching

Select to validate if values in the XML instance is valid according to the W3C standard and the specified XSD schema.

 

## 
Modify Schema Properties Screen

Use this tab to specify properties of the XML schema.

Schema

This box lists the corresponding schema structure of the root. stands for elements,  stands for the attributes in the XML schema, and  stands for the references of elements.

Properties

This box lists properties and values of the properties for the selected element or attribute in the schema.

 

## 
Transform XML Schema Screen

Use this screen to specify an XPath as the transforming start point. Designer then transforms all the elements and their attributes that match with the selected XPath  to relational schema.

 

## 
Transformed Relational Schema Screen

This screen displays the relational schema structure Designer transforms from the XML schema.

 

## 
Add Table Screen

Use this screen to add tables that Designer transforms from the XML data source to the connection. Designer does not display the screen when you use the dialog box for editing an existing XML connection.

Schema

Select the schema in the XML data source to add tables from it.

Tables

This box lists the tables in the selected schema that Designer transforms from the XML data source.

Added Tables

This box lists the tables that you add to use in the XML connection.

Add button

Select to add the specified tables in the Tables box to the XML connection.

Remove button

Select to remove the specified table from the Added Tables box.

Generate the default pre-join path

Select to generate the default pre-join path for tables of the XML data source.
