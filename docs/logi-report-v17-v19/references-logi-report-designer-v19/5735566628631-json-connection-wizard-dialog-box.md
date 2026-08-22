---
title: "JSON Connection Wizard Dialog Box"
id: 5735566628631
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735566628631-JSON-Connection-Wizard-Dialog-Box
updated_at: 2022-11-02T04:39:38Z
---

# JSON Connection Wizard Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735551861527-Join-Options-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514748567-KPI-Chart-Wizard-Dialog-Box)

# JSON Connection Wizard Dialog Box

You can use the JSON Connection Wizard dialog box to [get data from a JSON data source](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog#Set) in a catalog. This topic describes the options in the dialog box.

Designer displays the JSON Connection Wizard dialog box when you select JSON and select OK in the [New Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530467735-New-Data-Source-Dialog-Box); or in the Catalog Manager, right-click a data source and select New JSON Connection from the shortcut menu, or right-click an existing JSON connection and select Edit Connection from the shortcut menu.

The dialog box contains the following screens:

* [Extract JSON Schema Screen](#Extract)
* [Modify Schema Properties Screen](#Modify)
* [Transformed Relational Schema Screen](#Transformed)
* [Add Table Screen](#Add)

Designer displays these buttons in all the screens:

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

## Extract JSON Schema Screen

Use this screen to specify the information to extract the JSON schema.

![JSON Connection Wizard - Extract JSON Schema](https://devnet.logianalytics.com/hc/article_attachments/9898478968855/jsoncnctn_extrt.gif)

**Schema Source**

Select the source to extract the JSON schema: [Extract Schema from Sample Data](#Sample) or [Extract Schema from Instance Data](#Instance).

Designer displays different options in the Extract JSON Schema screen to specify the schema according to the schema source you select.

* When you select the Schema Source option of "Extract Schema from Sample Data", Designer displays these options:

  **Sample Data**

  Specify the sample data file from which to extract the JSON schema. You can select **Browse** to specify the sample data file from your local disk or type the URI string of the file in the text box.

  + **RESTful**  
    Designer enables this button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567159831-RESTful-Data-Source-Options-Dialog-Box) to define RESTful options for the sample data.

  **URI**

  Select to get instance data from URI.

  + **Instance**  
    Specify the JSON instance file. You can select **Browse** to specify the instance file from your local disk or type the URI string of the file in the text box.
    - ![New Parameter button](https://devnet.logianalytics.com/hc/article_attachments/9898478152855/btn_nwparam.gif)**New parameter button**  
      Select to open the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box) to create a parameter in the current catalog data source and reference it in the URI string to dynamically specify the instance.
    - **RESTful**  
      Select to open the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567159831-RESTful-Data-Source-Options-Dialog-Box) to define RESTful options for the instance data.

  **User Defined**

  Select to get instance data from user-defined interface.

  + **Class Name**  
    Specify the full name (including package name) of the class. You can select **Browse** to specify the class file from your local disk or type the class name with package name in the text box. You need to append the class to the class path in the system environment.
  + **The class implements**  
    After you fill in the Class Name text box, Designer displays the class name of the interface that the class implements here.
  + **Parameter**  
    Specify the parameter string for the user-defined data interface. The parameter string must match the format defined in the class.

  ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")**Paginated**

  Select to get paginated instance data from a REST Web Service.

  + **User Name**  
    Specify the user name for remote data authentication.
  + **Password**  
    Specify the password for remote data authentication.
  + **Main Formula**  
    Select the main formula that defines how you want to fetch the pagination data.
    - **New Formula**  
      Select to open the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565964055-Formula-Editor-Dialog-Box) to compose the formula.
    - ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898405043607/btn_edit1.gif)**Edit button**  
      Select to edit the specified formula.
    - ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9898477280279/btn_delete.gif)**Delete button**  
      Select to delete the specified formula.
* When you select the Schema Source option of "Extract Schema from Instance Data", Designer displays these options:

  **Instance**

  Specify the JSON instance file. You can select **Browse** to select the instance file or type the URI string of the file in the text box.

  + **RESTful**  
    Designer enables this button when the specified URI string begins with the "http://" or "https://" protocol. Select it to open the [RESTful Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567159831-RESTful-Data-Source-Options-Dialog-Box) to define RESTful options for the instance data.

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

Designer displays this button when you use the dialog box for editing an existing JSON connection. After you make changes in the dialog box and select the Refresh button, Designer reloads the JSON schema information according to what you have changed.

## Modify Schema Properties Screen

Use this screen to specify properties of the JSON schema.

![JSON Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/9898461870359/jsoncnctn_mdfy.gif)

**Schema**

This box lists the corresponding schema structure of the root. ![](https://devnet.logianalytics.com/hc/article_attachments/9898458858647/btn_elmnt.gif)stands for elements.

**Properties**

This box lists properties and values of the properties for the selected element in the schema.

## Transformed Relational Schema Screen

This screen displays the relational tables Designer builds based on the transformed relational schema structure.

![JSON Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/9898478980631/jsoncnctn_trnsfrmd.gif)

## Add Table Screen

Use this screen to add tables that Designer transforms from the JSON data source to the connection. Designer does not display the screen when you use the dialog box for editing an existing JSON connection.

![JSON Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/9898461898519/jsoncnctn_adtbl.gif)

**Tables**

This box lists the tables that Designer transforms from the JSON data source.

**Added Tables**

This box lists the tables that you add to use in the JSON connection.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif)**Add button**

Select to add the specified tables in the Tables box to the JSON connection.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9898422552599/btn_rmvarrow.gif)**Remove button**

Select to remove the specified tables from the Added Tables box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735551861527-Join-Options-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735514748567-KPI-Chart-Wizard-Dialog-Box)
