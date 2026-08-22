---
title: "XML Connection Wizard Dialog Box"
id: 4405661750167
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661750167-XML-Connection-Wizard-Dialog-Box
updated_at: 2022-01-27T20:35:29Z
---

# XML Connection Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664593175-Windows-Media-Player-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661751191-XML-Option-Dialog-Box)

# XML Connection Wizard Dialog Box

You can use the XML Connection Wizard dialog box to [get data from an XML data source](https://devnet.logianalytics.com/hc/en-us/articles/4405661442711-Working-with-XML-Connections-in-a-Catalog#Set) in a catalog by importing XML schemas and transforming them to relational schemas. This topic describes the options in the dialog box.

Designer displays the XML Connection Wizard dialog box when you select XML and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661654807-New-Data-Source-Dialog-Box); or in the Catalog Manager, right-click a data source and select Add XML Connection from the shortcut menu, or right-click an existing XML connection and select Edit Connection from the shortcut menu.

The dialog box contains the following screens:

* [Import XML Schema Screen](#Import)
* [Modify Schema Properties Screen](#Modify)
* [Transform XML Schema Screen](#Transform)
* [Transformed Relational Schema Screen](#Transformed)
* [Add Table Screen](#Add)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish your work and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Import XML Schema Screen

Use this screen to specify the necessary information to import the XML schema.

![XML Connection Wizard - Import XML Schema](https://devnet.logianalytics.com/hc/article_attachments/4420394713623/xmlcnnctn_import.gif)

**Schema Type**

Select the type to import the XML schema: Import from XSD or Parse from an XML Instance.

**Schema Name**

Specify the schema file. You can select **Browse** to specify the schema file from your local disk or type the URI string of the file in the text box.

* **RESTful**  
  Designer enables this button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661694743-RESTful-Data-Source-Options-Dialog-Box) to define the RESTful options for the schema data.

**Starting Node**

Select the starting node, according to the root name in the XML source.

**Instance**

Specify the XML instance. You can select **Browse** to specify the instance file from your local disk or type the URI string of the file in the text box. The instance should match with the specified XSD schema.

* **RESTful**  
  Designer enables this button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661694743-RESTful-Data-Source-Options-Dialog-Box) to define the RESTful options for the instance data.

**Time Zone and Locale**

Select to open the [Time Zone and Locale Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664589207-Time-Zone-and-Locale-Options-Dialog-Box) to specify the default time zone and locale for the XML instance.

**Edit Format**

Select to open the Edit Format dialog box to specify the value formats of the referenced parameters and formulas.

* **Name**  
  This column shows the names of the parameters and formulas.
* **Format**  
  This column shows the value formats that you specify for the parameters and formulas.
* **OK**  
  Select to apply the changes and close the dialog box.
* **Cancel**  
  Select to close the dialog box without saving any changes.

**Refresh**

Designer displays this button when you use the dialog box for editing an existing XML connection. After you make changes in the dialog box and select the Refresh button, Designer reloads the XML schema information according to what you have changed.

Designer displays the following options when you select Import from XSD from the Schema Type drop-down list:

**URI**

Select to get instance data from URI.

**User Defined**

Select to get data from user-defined interface.

* **Class Name**  
  Specify the full name (including package name) of the class. You can select **Browse** to specify the class from your local disk or type the class name in the text box. You should have appended the class to the class path in the system environment.
* **The class implements**  
  This option shows the class name of the interface that the class implements after you specify the Class Name option.
* **Parameter**  
  Specify the parameter string for the user-defined data interface. The parameter string must match the format defined in the class.

**New Parameter**

Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661658135-New-Parameter-Dialog-Box) to create a parameter in the current catalog data source. You can then reference the parameter to dynamically specify a URI or user-defined interface that matches with the selected XSD schema at runtime.

**Validate with schema before fetching**

Select to validate if values in the XML instance is valid according to the W3C standard and the specified XSD schema.

## Modify Schema Properties Screen

Use this tab to specify properties of the XML schema.

![XML Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4420394713879/xmlcnnctn_modify.gif)

**Schema**

This box lists the corresponding schema structure of the root. ![](https://devnet.logianalytics.com/hc/article_attachments/4420394682903/btn_elmnt.gif)stands for elements, ![](https://devnet.logianalytics.com/hc/article_attachments/4420402353687/btn_atrbt.gif) stands for the attributes in the XML schema, and ![](https://devnet.logianalytics.com/hc/article_attachments/4420402354071/btn_elmntref.gif) stands for the references of elements.

**Properties**

This box lists properties and values of the properties for the selected element or attribute in the schema. For more information about the properties, see [XML Schema Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405664644503-XML-Schema-Properties).

## Transform XML Schema Screen

Use this screen to specify an XPath as the transforming start point. Designer then transforms all the elements and their attributes that match with the selected XPath to relational schema.

![XML Connection Wizard - Transform XML Schema](https://devnet.logianalytics.com/hc/article_attachments/4420394714263/xmlcnnctn_trnsfrm.gif)

## Transformed Relational Schema Screen

This screen lists the relational schema structure that Designer transforms from the XML schema. Select **Next** to confirm the transformation result and go into the Add Table screen.

![XML Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4420402387479/xmlcnnctn_trnsfrmd.gif)

## Add Table Screen

Use this screen to add tables that Designer transforms from the XML data source to the connection. Designer does not display the screen when you use the dialog box for editing an existing XML connection.

![XML Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4420402387991/xmlcnnctn_add.gif)

**Schema**

Select the schema in the XML data source to add tables from it.

**Tables**

This box lists the tables in the selected schema that Designer transforms from the XML data source, which you can add to the XMl connection.

**Added Tables**

This box lists the tables that you add to use in the XML connection.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif)**Add button**

Select to add the specified tables in the Tables box to use in the XML connection.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420394644119/btn_rmvarrow.gif)**Remove button**

Select to remove the specified table from the Added Tables box.

**Generate the default pre-join path**

Select to generate the default pre-join path for tables of the XML data source.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664593175-Windows-Media-Player-Parameter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661751191-XML-Option-Dialog-Box)
