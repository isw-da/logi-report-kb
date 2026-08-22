---
title: "XML Connection Wizard Dialog"
id: 1500009567962
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009567962-XML-Connection-Wizard-Dialog
updated_at: 2021-07-24T05:54:43Z
---

# XML Connection Wizard Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567942-Windows-Media-Player-Parameter-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567982-XML-Option-Dialog)

# XML Connection Wizard Dialog

The XML Connection Wizard appears when you select XML and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009587961-New-Data-Source-Dialog) dialog, or in the Catalog Manager right-click a data source and select Add XML Connection from the shortcut menu or right-click an existing [XML connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009585441-Setting-Up-an-XML-Connection) and select Edit Connection from the shortcut menu. It helps you to import an XML schema and transform it to a relational schema for future use, and consists of the following screens:

* [Import XML Schema](#Import)
* [Modify Schema Properties](#Modify)
* [Transform XML Schema](#Transform)
* [Transformed Relational Schema](#Transformed)
* [Add Table](#Add)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes confirming to transform an XML schema to a relational schema.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Import XML Schema

Specifies the necessary information to import XML schema. [See the screen](javascript:%20void(null)).

![XML Connection Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404893844247/xmlcnnctn_import.gif)

**Schema Type**

Specifies the type to import XML schema: Import from XSD or Parse from an XML Instance.

**Schema Name**

Specifies the schema file by selecting the Browse button or inputting the URI string directly in the text box. In the URI string, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname".

* **RESTful**  
   The button is activated when the specified URI string begins with `http://` or `https://` protocol. Selecting it opens the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588461-RESTful-Data-Source-Options-Dialog) dialog, in which you can define the RESTful options for the schema data.

**Starting Node**

Specifies the starting node, according to the root name in the XML source.

**Instance**

Specifies the XML instance by selecting the Browse button or input the URI string directly in the text box. It should match with the selected XSD schema. In the URI string, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname".

* **RESTful**  
   The button is activated when the specified URI string begins with `http://` or `https://` protocol. Selecting it opens the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588461-RESTful-Data-Source-Options-Dialog) dialog, in which you can define the RESTful options for the instance data.

**Time Zone and Locale**

Opens the [Time Zone and Locale Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009567782-Time-Zone-and-Locale-Options-Dialog) dialog to specify the default time zone and locale for the XML instance.

The following options are available only when you select Import from XSD from the Schema Type drop-down list.

* **URI**  
   Specifies to get instance data from URI.
* **User Defined**  
   Specifies to get data from user defined interface.
  + **Class Name**  
     Specifies the full name (including package name) of the class by selecting the Browse button or inputting the class name directly in the text box. The class should be appended to the class path in the system environment.
  + **The class implements**  
     After filling in the Class Name field, the class name of the interface that the class implements will be displayed here.
  + **Parameter**  
     Specifies the parameter string for the user defined data interface. The parameter string must match the format defined in the class. In the parameter string, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname".
* **New Parameter**  
   Opens the [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog) dialog to create a parameter in the current catalog data source. You can then reference the parameter to dynamically specify a URI or user defined interface that matches with the selected XSD schema at runtime.
* **Validate with schema before fetching**  
   If selected, Logi JReport Designer will validate whether or not values in the XML instance is valid according to the W3C standard and the specified XSD schema. If not, a message - Invalid Value will pop up.

**Edit Format**

Opens the Edit Format dialog to specify the value formats of the referenced parameters and formulas.

* **Name**  
   Displays names of the parameters and formulas.
* **Format**  
   Specifies the value formats of the parameters and formulas.

* **OK**  
   Accepts changes and closes the dialog.
* **Cancel**  
   Does not retain changes and closes the dialog.

**Refresh**

Available only when you edit an existing XML connection. Once you make some change in the wizard and select the Refresh button, the XML schema information will be reloaded according to what you have changed.

## Modify Schema Properties

Specifies properties of the XML schema. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893844503/xmlcnnctn_modify.gif)

**Schema**

Lists the corresponding schema structure of the root. ![](https://devnet.logianalytics.com/hc/article_attachments/4404893844759/btn_elmnt.gif)stands for elements, ![](https://devnet.logianalytics.com/hc/article_attachments/4404889311383/btn_atrbt.gif)stands for the attributes in the XML schema and ![](https://devnet.logianalytics.com/hc/article_attachments/4404889311639/btn_elmntref.gif) stands for the references of elements.

**Properties**

Lists all the properties of the selected elements and attributes in the schema.

* **Name**  
   Displays names of properties of the selected elements or attributes.
* **Value**  
   Specifies values of properties for the selected elements or attributes.

**Note:** When the property Data Type is specified as Date, Time or DateTime, you can specify the Format Pattern for them to make values of the data type displayed in the required format. For details about these properties, see [Supplementing information for the XML schema](https://devnet.logianalytics.com/hc/en-us/articles/1500009564382-Importing-an-XML-Schema#XMLSchema).

## Transform XML Schema

This screen allows you to specify an XPath as a transforming start point. All the elements matching with the selected XPath and their attributes will be transformed to the relational schema. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889311895/xmlcnnctn_trnsfrm.gif)

## Transformed Relational Schema

This screen lists the transformed relational schema structure. It helps you to select Next to confirm the transformation results and go into the Add Table screen. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889312151/xmlcnnctn_trnsfrmd.gif)

## Add Table

Adds tables that are transformed from the relational schema to the connection. This screen is not available when you edit an existing XML connection. [See the screen](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893845015/xmlcnnctn_add.gif)

**Schema**

Lists the schemas in the database for you to select.

**Tables**

Lists the tables transformed from the XML schema.

**Added Tables**

Lists the tables that you have added from the relational schema.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected tables.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)

Removes the selected tables from the Added Tables box.

**Generate the default pre-join path**

Specifies whether or not to generate the default pre-join path for tables of the XML data source.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567942-Windows-Media-Player-Parameter-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567982-XML-Option-Dialog)
