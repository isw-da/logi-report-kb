---
title: "JSON Connection Wizard Dialog"
id: 1500009587721
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587721-JSON-Connection-Wizard-Dialog
updated_at: 2021-07-24T05:55:05Z
---

# JSON Connection Wizard Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566602-Join-Options-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566622-Library-Component-Setting-Dialog)

# JSON Connection Wizard Dialog

The JSON Connection Wizard appears when you select JSON and select OK in the [New Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009587961-New-Data-Source-Dialog) dialog, or in the Catalog Manager right-click a data source and select New JSON Connection from the shortcut menu or right-click an existing [JSON connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009585121-Setting-Up-a-JSON-Connection) and select Edit Connection from the shortcut menu. It helps you to import an XML schema and transform it to a relational schema for future use, and consists of the following screens:

* [Extract JSON Schema](#Extract)
* [Modify Schema Properties](#Modify)
* [Transformed Relational Schema](#Transformed)
* [Add Table](#Add)

**Back**

Goes back to the previous screen.

**Next**

Goes to the next screen.

**Finish**

Finishes confirming to transform a JSON schema to a relational schema.

**Cancel**

Does not retain changes and closes this wizard.

**Help**

Displays the help document about this feature.

## Extract JSON Schema

Specifies the necessary information to extract JSON schema. [See the screen](javascript:%20void(null)).

![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4404889332119/jsoncnctn_extrt.gif)

**Schema Source**

Specifies the source to extract JSON schema: [Extract Schema from Sample Data](#Sample) or [Extract Schema from Instance Data](#Instance). Options on the screen differ with the schema source.

* When Extract Schema from Sample Data is selected, the following options are available:

  **Sample Data**

  Specifies the sample file by selecting the Browse button or inputting the URI string directly in the text box. In the URI string, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname".

  + **RESTful**  
     The button is activated when the specified URI string begins with `http://` or `https://` protocol. Selecting it opens the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588461-RESTful-Data-Source-Options-Dialog) dialog, in which you can define the RESTful options for the sample data.

  **URI**

  Specifies to get instance data from URI.

  + **Instance**  
     Specifies the JSON instance by selecting the Browse button or inputting the URI string directly in the text box. It should match with the JSON schema defined in the specified sample data file. In the URI string, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname".
    - **RESTful**  
       The button is activated when the specified URI string begins with `http://` or `https://` protocol. Selecting it opens the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588461-RESTful-Data-Source-Options-Dialog) dialog, in which you can define the RESTful options for the instance data.

  **User Defined**

  Specifies to get instance data from user defined interface.

  + **Class Name**  
     Specifies the full name (including package name) of the class by selecting the Browse button or inputting the class name directly in the text box. The class should be appended to the class path in the system environment.
  + **The class implements**  
     After filling in the Class Name field, the class name of the interface that the class implements will be displayed here.
  + **Parameter**  
     Specifies the parameter string for the user defined data interface. The parameter string must match the format defined in the class. In the parameter string, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname".

  **New Parameter**

  Opens the [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog) dialog to create a parameter in the current catalog data source. You can then reference the parameter to dynamically specify a JSON instance or user defined interface that matches with the selected JSON schema at runtime.
* When Extract Schema from Instance Data is selected, the following options are available:

  **Instance**

  Specifies the JSON instance by selecting the Browse button or input the URI string directly in the text box. In the URI string, you can reference parameters and constant level formulas in the current catalog data source and the special field User Name in the format "@fieldname".

  + **RESTful**  
     The button is activated when the specified URI string begins with `http://` or `https://` protocol. Selecting it opens the [RESTful Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588461-RESTful-Data-Source-Options-Dialog) dialog, in which you can define the RESTful options for the instance data.

**Refresh**

Enabled only when you edit an existing JSON connection. Once you make some change in the wizard and select the Refresh button, the JSON schema information will be reloaded according to what you have changed.

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

## Modify Schema Properties

Specifies properties of the JSON schema. [See the screen](javascript:%20void(null)).

![JSON Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404893869975/jsoncnctn_mdfy.gif)

**Schema**

Lists the corresponding schema structure of the root. ![](https://devnet.logianalytics.com/hc/article_attachments/4404893844759/btn_elmnt.gif)stands for elements, ![](https://devnet.logianalytics.com/hc/article_attachments/4404889311383/btn_atrbt.gif)stands for the attributes in the XML schema and ![](https://devnet.logianalytics.com/hc/article_attachments/4404889311639/btn_elmntref.gif) stands for the references of elements.

**Properties**

Lists all the properties of the selected elements and attributes in the schema.

* **Name**  
   Displays names of properties of the selected elements or attributes.
* **Value**  
   Specifies values of properties for the selected elements or attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4404889311895/xmlcnnctn_trnsfrm.gif)

## Transformed Relational Schema

This screen lists the transformed relational schema structure. It helps you to select Next to confirm the transformation results and go into the Add Table screen. [See the screen](javascript:%20void(null)).

**Transformed Tables**

Shows tables transformed from JSON schema.

![JSON Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404889332375/jsoncnctn_trnsfrmd.gif)

## Add Table

Adds tables that are transformed from the relational schema to the connection. This screen is not available when you edit an existing JSON connection. [See the screen](javascript:%20void(null)).

![JSON Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404893870231/jsoncnctn_adtbl.gif)

**Tables**

Lists the tables transformed from the JSON schema.

**Added Tables**

Lists the tables that you have added from the relational schema.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)

Adds the selected tables.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)

Removes the selected tables from the Added Tables box.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566602-Join-Options-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566622-Library-Component-Setting-Dialog)
