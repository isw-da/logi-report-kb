---
title: "New Parameter Dialog"
id: 1500009566822
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog
updated_at: 2021-07-24T05:55:00Z
---

# New Parameter Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588001-New-General-Hierarchical-Data-Source-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566842-New-Summary-Dialog)

# New Parameter Dialog

The New Parameter dialog appears when you do any of the following:

* Right-click the Parameters node in the Catalog Manager and select New Parameter from the shortcut menu.
* In the Data panel of the main window, select <New Parameter…> in the Local Parameters node.
* Right-click a data component created using a business view and select Format Filter from the shortcut menu. In the [Edit Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009565242-Edit-Filter-Dialog) dialog, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to the value text field, then in the Values dialog, select <New Parameter…> in the Local Parameters node.

It helps you to [create parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter) in a catalog, or create local parameters to use in the current report or library component.

The following are details about options in the dialog. [See the dialog](javascript:%20void(null)).

![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893825559/nwprm.gif)

**Name**

Specifies the name of the parameter.

**Value Setting**

Specifies the parameter type.

* **Type-in Parameter**  
   If selected, you can predefine parameter values by typing manually.
* **Bind with Single Column**  
   If selected, the parameter will be bound with a DBField. The values of the DBField will be retrieved as the parameter values at runtime.
* **Bind with Cascading Columns**  
   If selected, you can create a group of cascading parameters so as to achieve the function of filtering parameters with parameters in a simple way. Not available when the parameter is in a catalog data source that contains only XML connections.

**Value Type**

Specifies the data type of the parameter.

**Values**

The section after Value Type varies with the type you select from the Value Setting drop-down list.

* **For Type-in Parameter**
  + **Value List**  
     Lists the predefined parameter values.
  + **Prompt Values** [format hint]  
     Predefines the parameter values. The [format hint] shows what the predefined values should look like.

    There can be more than one prompt value. All the prompt values must be of the same type as specified in the Value Type field.

    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
       Adds a new prompt value to the list. Double-click in the value line to edit the value. If the parameter is of Date, DateTime, or Time type, you can also select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404889299735/btn_clndr.gif) to set a date and time value in the [Calendar](https://devnet.logianalytics.com/hc/en-us/articles/1500009564742-Calendar-Dialog) dialog.
    - ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
       Removes the selected prompt value.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
       Adjusts the display sequence of selected value by moving it up a step.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
       Adjusts the display sequence of selected value by moving it down a step.
* **For Bind with Single Column**  
  Logi JReport provides such a mechanism that links each field value of Display Column with the exact value of Bind Column. When you select the field value from Display Column, the field value of Bind Column is actually sent to the query and filters the query result. It helps you to bind the parameter to a DBField (column) in order to provide a list of DBField values for users to select at runtime. The selected value of the bound DBField will be used as the parameter value. Additionally, instead of displaying the values of the bound one, you can also choose to display values of other DBField, which probably makes more sense to the report end users. For example, it might be confusing if you provide a list of customer ID numbers for users to select at runtime, since the ID numbers could probably mean nothing to them. In cases like this, it is wise for you to display values of other fields, which could probably make more sense. For this case, you might prefer to display customer names instead of ID numbers. When the report end users select a customer name from the list, its ID number is passed to the query as the parameter value so that the search criteria can be fulfilled. So, before the report with a parameter bound to a DBField is processed, a query statement will be executed first to retrieve the values of the bound field and display field.
  + **Source**  
     Specifies the source type from which to retrieve the columns which can be used to bind with the parameter. The available source types are: Tables and Views (including synonyms), Stored Procedures, Imported SQLs, and User Defined. However, when the parameter is in a catalog data source that contains only MongoDB connections, only Tables and User Defined are available in the Source drop-down list.
  + **Bind Column**  
     Specifies the DBField to be bound with the parameter.
  + **Display Column**  
     When viewing a report which contains the parameter, the field values related to the column name you selected in the drop-down list of Display Column will be displayed in the Enter Parameter Values dialog at runtime.
* **For Bind with Cascading Columns**
  + **Data Source**  
     Specifies the data source from which to retrieve the columns which can be used to bind with the parameters. The available data sources are tables, views, synonyms, stored procedures, imported SQLs, and user defined data sources in the catalog data source in which the parameter is. However, when the parameter is in a catalog data source that contains only MongoDB connections, only tables and user defined data sources are available.
  + **Value List**  
     Defines a group of cascading parameters.
    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
       Adds a new parameter.
    - ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
       Removes the selected parameter.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
       Adjusts the parameter level by moving it up a step. The higher the position is, the higher the level is. The lower level field values are controlled by the higher level field values.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
       Adjusts the parameter level by moving it down a step.
    - **Bind Column**  
       Specifies the DBField to be bound with the parameter.
    - **Display Column**  
       When viewing a report which contains the parameter, the field values related to the column name you selected in the drop-down list of Display Column will be displayed in the Enter Parameter Values dialog at runtime.
    - **Parameter**  
       Specifies whether to set a group of Bind Column and Display Column as a parameter which will become a member of the cascading parameter group. All parameters in the cascading group will be created as independent parameters in the catalog after you finish the dialog.

      The parameter name is provided by Logi JReport automatically, and the format is *[The name specified as parameter name]-[Bind Column name]*.

**Options**

Specifies options for the parameter. The options vary with the type you select from the Value Setting drop-down list.

* **Prompt Text**  
   Specifies the text for prompting users to provide the value of the parameter.

  **Tips**:

  + To help users avoid typing a value out of range, you can add the value range to the end of the prompt text. For example, "Type a customer ID (1~100):".
  + To help users avoid typing a value in a wrong pattern, you can add the value pattern to the end of the prompt text. For example, "Type an order date (MMM-dd-yy):".
* **Minimum Value/Length**  
   Specifies the minimum value allowed for the parameter. If the parameter value type is String, this option is defined as Minimum Length, which means that you can set the minimum allowed length of the string.
* **Maximum Value/Length**  
   Specifies the maximum value allowed for the parameter. If the parameter value type is String, this option is defined as Maximum Length, which means that you can set the maximum allowed length of the string.
* **String Encoding**  
   Specifies the encoding for the parameter. Available only when the parameter's data type is defined as String.
* **User Defined Format**  
   For certain types of parameters, the value format supplied by Logi JReport may not satisfy your requirement. In this case, you can define your own preferred format. When you have defined the value format, all the values you supply at runtime should be based on it. Otherwise there will be an error message. For details, see [User Defined Format for Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590281-User-Defined-Format-for-Parameters).

  **Notes**:

  + The letters that stand for the user defined format should follow the JDK standard. In addition, the user defined format only limits the format of the input value, which does not mean that the display value will be in the same format. To change the display format, you will need to specify the Format property of this parameter in the Report Inspector.
  + The user defined format will show different appearance under different locale, and you need input values according to the displayed format. For example, under the Spanish or French locale, ####.## will be displayed as #0,## and you should follow #0,## to input values.
* **Required**  
   If set to true, the parameter will be treated as a required parameter. A required parameter must be fulfilled, which means that you must supply a value in the Enter Parameter Values dialog before the report can be run. If set to false, the parameter will be treated as an optional parameter. An optional parameter can be left blank, which means you can either type a value, or leave it as it is.

  In the Enter Parameters Value dialog, the prompt text of a required parameter will be marked with a \* sign.

  **Note**: If the parameter is optional and you do not expect it to take effect in your report, in the Enter Parameter Values dialog, clear the content in the value field. Otherwise, any value left in the field will function in reports.
* **Hide Parameter When Single Value Returned**  
   Specifies to hide the parameter at runtime when only a single value is returned for the parameter. The returned single value will be used as default value of the parameter.
* **Allow Multiple Values**  
   Enables multiple parameter values to be selected. To allow users to select more than one value of a parameter, report designer needs to set the Allow Multiple Values option to true when creating the parameter. Then when users run reports with the parameter, they are able to make use of the [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009565442-Enter-Values-Dialog) dialog to specify multiple values of the parameter. Multi-valued parameters are supported in dataset filters, query filters, imported SQL files, and subreport/link report conditions. A multi-valued parameter can be displayed in a report by using the [join()](https://devnet.logianalytics.com/hc/en-us/articles/1500009568262-String-Functions#join) function.
* **Enable the "All" Option**  
   When Allow Multiple Values is true, this option is activated and its default value is true which will display the All checkbox in the Enter Values dialog. At report runtime, when users select the All checkbox the parameter value result is all the values that match the parameter data type.
* **Treat Blank as Null**  
   Available only when the parameter's data type is defined as String. If it is true, the parameter value will be null; if false, the default parameter value is "".
* **Use Current Date-Time**  
   If set to true, the current date time in your system will be used as value of the parameter. Available only when the parameter's data type is defined as Date, Time or DateTime.
* **Use Current Date-Time When Blank**  
   If set to true, when the value of the parameter is blank, the current date time in your system will be used as value of the parameter. Available only when the parameter's data type is defined as Date, Time or DateTime.

  If the type of the parameter is set to Date, Time or DateTime, you can choose whether to get parameter value dynamically from the system's date time by enabling one of the above options - Use Current or Use Current When Blank. However, if you want to use this feature, you need to make sure your system's DateTime format is set to yyyy-MM-dd H:mm:ss as it is the only format Logi JReport supports; otherwise, you need to make use of the User Defined Parameter Format feature. Also, if one of the two options is enabled, you need to provide the parameter's prompt value according to the data type of your parameter.

  + When the data type of the parameter is Date, you can specify the value according to the format yyyy-MM-dd.
    - yyyy-01-01: Year will be dynamically changed.
    - 2007-MM-01: Month will be dynamically changed.
    - 2007-01-dd: Date will be dynamically changed.
    - yyyy-MM-01: Year and month will be dynamically changed.
    - yyyy-01-dd: Year and date will be dynamically changed.
    - yyyy-MM-dd: Year, month, and date will be dynamically changed.
    - 2007-MM-dd: Month and date will be dynamically changed.
  + When the data type of the parameter is Time, you can specify the value according to the format H:mm:ss.
    - H:00:00: Hour will be dynamically changed.
    - 12:mm:00: Minute will be dynamically changed.
    - 12:00:ss: Second will be dynamically changed.
    - H:mm:00: Hour and minute will be dynamically changed.
    - 12:mm:ss: Minute and second will be dynamically changed.
    - H:00:ss: Hour and second will be dynamically changed.
    - H:mm:ss: Hour, minute and second will be dynamically changed.
  + When the data type of the parameter is DateTime, specify the value in a combination of the above.
* **Record Level Security**  
   Specifies the RLS policy defined on the bound column in the data source to the parameter. For details, refer to [Applying RLS to a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590061-Applying-RLS-to-a-Parameter).
* **Sort**  
   Specifies how to sort values of cascading parameters.
  + **Ascend**  
     Sorts parameter values in an ascending order.
  + **Descend**  
     Sorts parameter values in a descending order.
  + **No Sort**  
     The parameter values are displayed in the original order as in database.
  + **Sort By**  
     Sorts parameter values by sorting other fields in the same data source as the cascading group. When Sort By is selected, the [Sort By](https://devnet.logianalytics.com/hc/en-us/articles/1500009567662-Sort-By-Dialog) dialog will be displayed for specifying fields and their sorting orders.
* **Distinct**  
  If set to true, when viewing a report that contains the parameter, in the Enter Parameter Values dialog, identical values will appear only once and no duplicate values will be listed.
* **Import SQL**  
   Displays the SQL statement for retrieving values of the bound column and display column. You can edit the statement if required. To do this, select in the value cell, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) and edit the statement in the Import SQL dialog.

  **Notes**:

  + If you have made changes to the SQL statement, the later changes for Bind Column and Display Column will not take effect unless you remove the SQL lines or bind the parameter all over again. To remove the SQL lines, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell and clear the content in the Import SQL dialog.
  + The special field User Name can also be used in the SQL statement as *@username* (to specify the user name, go to **File** > **Options**, in the General category of the Options dialog, set the User Name option).
* **Allow Type-in of Value**  
   Specifies whether to enable typing values besides selecting values when setting parameter values. The property is enabled for Type-in Parameter by default.
* **When Out of Value Range**  
   Specifies how Logi JReport will respond if the typed value is out of the predefined value list. The property is enabled only when the option Allow Type-in of Value is set to true.

  There are three solutions as follows:

  + **Adopt directly**  
     The typed value will be used directly.
  + **Use default**  
     The default value defined when creating the parameter will be used.
  + **Warn**  
     Displays a warning message telling that "Value xxx is out of the available value list".

  **Note**: For a multi-value parameter, if one of the input values is not in the value list, the whole input result will be treated as out of range.
* **Get Value from API Only**  
   Specifies whether the parameter values can be input via GUI or not.

  If true, the parameter values should only be obtained from API and there will be no parameter dialogs available on any Logi JReport Designer or Server GUI for inputting values. Users will have to give the values of the parameter by API such as URLs, coding, and sessions, otherwise the default value will be used.

  If false, the parameter can be obtained from both GUI and API.

  If a member of a cascading parameter group is set to get values from API only, it means that all the higher level members shall get values from API only. This also applies to parameters that some other parameters depend on. If in JDashboard several parameters share values, when any of them is set to get values from API only, they will share the values from API.
* **On Parameter Value Change**  
   Specifies to define an action that will be called when the parameter value changes. Choose a formula from the drop-down list to develop an action, which will be called before the other actions defined in the report or library component. It can work as a parameter value validation rule.

**OK**

Applies all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009588001-New-General-Hierarchical-Data-Source-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566842-New-Summary-Dialog)
