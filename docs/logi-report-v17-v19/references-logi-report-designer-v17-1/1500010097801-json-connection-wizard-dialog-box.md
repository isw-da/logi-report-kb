---
title: "JSON Connection Wizard Dialog Box"
id: 1500010097801
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097801-JSON-Connection-Wizard-Dialog-Box
updated_at: 2021-07-23T19:15:41Z
---

# JSON Connection Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097781-Join-Options-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097821-KPI-Chart-Wizard-Dialog-Box)

# JSON Connection Wizard Dialog Box

You can use the JSON Connection Wizard dialog box to [get data from a JSON data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010057762-Working-with-JSON-Connections-in-a-Catalog#Set) to use in a catalog. This topic describes the options in the dialog box.

Designer displays the JSON Connection Wizard dialog box when you select JSON and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059982-New-Data-Source-Dialog-Box), or in the Catalog Manager, right-click a data source and select New JSON Connection from the shortcut menu, or right-click an existing JSON connection and select Edit Connection from the shortcut menu.

The dialog box contains the following screens:

* [Extract JSON Schema Screen](#Extract)
* [Modify Schema Properties Screen](#Modify)
* [Transformed Relational Schema Screen](#Transformed)
* [Add Table Screen](#Add)

You see these buttons in all the screens:

**Back**

Select to go back to the previous screen.

**Next**

Select to go to the next screen.

**Finish**

Select to finish transforming a JSON schema to a relational schema.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Extract JSON Schema

Use this screen to specify the necessary information to extract the JSON schema.

![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/4404848514839/jsoncnctn_extrt.gif)

**Schema Source**

Select the source to extract the JSON schema: [Extract Schema from Sample Data](#Sample) or [Extract Schema from Instance Data](#Instance).

Designer displays different options in the Extract JSON Schema screen to specify the schema according to the schema source you select.

* If you select the Schema Source option of "Extract Schema from Sample Data", you see the following options:

  **Sample Data**

  Specify the sample data file from which to extract the JSON schema. You can type the URI string of the sample data file in the text box or select the Browse button to select the file.

  + **RESTful**  
    Designer enables the button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098501-RESTful-Data-Source-Options-Dialog-Box) to define the RESTful options for the sample data.

  **URI**

  Select to get instance data from URI.

  + **Instance**  
    Specify the JSON instance file. You can type the URI string in the text box or select the Browse button to select the instance file. The instance should match with the JSON schema defined in the specified sample data file.
    - **RESTful**  
      Designer enables the button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098501-RESTful-Data-Source-Options-Dialog-Box) to define the RESTful options for the instance data.

  **User Defined**

  Select to get instance data from user-defined interface.

  + **Class Name**  
    Specify the full name (including package name) of the class. You can input the class name with package name in the text box or select the Browse button to select the class file. You need to append the class to the class path in the system environment.
  + **The class implements**  
    After you fill in the Class Name text box, Designer displays the class name of the interface that the class implements here.
  + **Parameter**  
    Specify the parameter string for the user-defined data interface. The parameter string must match the format defined in the class.

  **New Parameter**

  Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098041-New-Parameter-Dialog-Box) to create a parameter in the current catalog data source. You can then reference the parameter to dynamically specify a JSON instance or user-defined interface that matches with the selected JSON schema at runtime.
* If you select the Schema Source option of "Extract Schema from Instance Data", you see the following options:

  **Instance**

  Specify the JSON instance file. You can type the URI string of the instance file in the text box or select the Browse button to select the file.

  + **RESTful**  
    Designer enables the button when the specified URI string begins with the "http://" or "https://" protocol. Select it to optn the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098501-RESTful-Data-Source-Options-Dialog-Box) to define the RESTful options for the instance data.

**Refresh**

Designer enables the button when you use the dialog box for editing an existing JSON connection. After you make changes in the dialog box and select the Refresh button, Designer reloads the JSON schema information according to what you have changed.

**Edit Format**

Select to open the Edit Format dialog box to specify the value formats of the referenced parameters and formulas.

* **Name**  
  The column shows the names of the parameters and formulas.
* **Format**  
  The column shows the value formats that you specify for the parameters and formulas.
* **OK**  
  Select to apply the changes and close the dialog box.
* **Cancel**  
  Select to close the dialog box without saving any changes.

## Modify Schema Properties

Use this screen to specify the properties of the JSON schema.

![JSON Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404848515223/jsoncnctn_mdfy.gif)

**Schema**

The box lists the corresponding schema structure of the root. ![](https://devnet.logianalytics.com/hc/article_attachments/4404856879895/btn_elmnt.gif)stands for elements.

**Properties**

The box lists all the properties of the selected element in the schema.

* **Name**  
  The column shows the names of the properties for the selected element.
* **Value**  
  The column shows the values that you specify for the properties of the selected element.

## Transformed Relational Schema

This screen lists the relational tables that Designer builds based on the transformed relational schema structure. Select Next to confirm the transformation result and go to the Add Table screen.

![JSON Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404848515479/jsoncnctn_trnsfrmd.gif)

## Add Table Screen

Use this screen to add tables that Designer transforms from the relational schema to the JSON connection. Designer does not display the screen when you use the dialog box for editing an existing JSON connection.

![JSON Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404856915863/jsoncnctn_adtbl.gif)

**Tables**

The box lists the tables that Designer transforms from the JSON schema.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif)**Add button**

Select to add the specified table to use in the JSON connection.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif)**Remove button**

Select to remove the specified table from the Added Tables box.

**Added Tables**

The box lists the tables that you select to add to use in the JSON connection.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097781-Join-Options-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097821-KPI-Chart-Wizard-Dialog-Box)
