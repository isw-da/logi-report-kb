---
title: "Add Parameter Dialog Box Properties"
id: 5741428253975
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741428253975-Add-Parameter-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:12Z
---

# Add Parameter Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741443886487-Add-Aggregation-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741443918871-Aggregate-On-Dialog-Box-Properties)

# Add Parameter Dialog Box Properties

You can use the Add Parameter dialog box to [add a local parameter](https://devnet.logianalytics.com/hc/en-us/articles/5741476426263-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-#Param) to a report. This topic describes the properties in the dialog box.

Server displays the dialog box when you select the **Toggle to Parameter** button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/9905575308823/btn_dshbrd_prm.gif) in the [Edit Dataset Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985329714327-Edit-Dataset-Filter-Dialog-Box-Properties) or [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741449994391-Filter-Dialog-Box-Properties), select the triangle button on the left, and then select **<Add Parameter…>**.

![Add Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905634053783/addprm.gif)

**Name**

Specify the name of the parameter.

**Value Setting**

Select the parameter type.

* **Type-in Parameter**  
  Select if you want to predefine parameter values by typing manually.
* **Bind with Single Column**  
  Select if you want to bind the parameter with a DBField. Server retrieves the DBField values as the parameter values.
* **Bind with Cascading Columns**  
  Select if you want to create a group of cascading parameters to filter parameters with parameters in an easy way.

**Value Type**

Select the data type of the parameter when it is a type-in parameter.

**Values**

The section after **Value Type** varies with **Value Setting**.

* **For Type-in Parameter**
  + **Value List**  
    Server lists the parameter values you predefined.
  + **Prompt Values** [format hint]   
    Predefine the parameter values. The [format hint] shows what the predefined values should look like.

    All the prompt values must be of the same data type as the **Value Type**.

    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add button**  
      Select to add a value line. Click the value line and type a value. If the parameter is of Date, DateTime, or Time type, you can also select the **Calendar** icon ![](https://devnet.logianalytics.com/hc/article_attachments/9905617212951/btn_clndr.gif) to set a date and time value using the calendar.
    - ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**  
      Select to remove the selected value.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) **Move Up button**  
      Select to move the selected value higher in the list.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**  
      Select to move the selected value lower in the list.
* **For Bind with Single Column**
  + **Source**  
    Select the business view in the current data source that retrieves data to the parameter.
  + **Bind Column**  
    Select the group or detail object in the selected business view that you want to bind with the parameter.
  + **Display Column**  
    Select the group or detail object in the selected business view whose values you want to display as the parameter values.
* **For Bind with Cascading Columns**
  + **Source**  
    Select the business view in the current data source that retrieves data to the parameter.
  + **Value List**  
    Define a group of cascading parameters.
    - ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add button**  
      Select to add a new parameter.
    - ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**  
      Select to remove the selected parameter.
    - ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) **Move Up button**  
      Select to move the selected parameter higher in the list. The higher the position is, the higher the parameter level is. The higher-level parameter values control the lower-level parameter values.
    - ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**  
      Select to move the selected parameter lower in the list.
    - **Bind Column**  
      Select the group or detail object in the selected business view you want to bind with the parameter.
    - **Display Column**  
      Select the group or detail object in the selected business view whose values you want to display as the parameter values.
    - **Parameter**  
      Select if you want to create a parameter based on a pair of Bind Column and Display Column in a line. The parameter becomes a member of the cascading parameter group. Logi Report creates all parameters in the cascading group as independent parameters.

      By default, the name of a cascading parameter is *[Parameter Name]-[Bind Column name]*.

**Options**

Specify the properties of the parameter, which vary with **Value Setting**.

* **Prompt Text**  
  Type the text for prompting users to provide the parameter value.

  **Tips:**

  + To help users avoid typing a value out of range, you can add the value range to the end of the prompt text. For example, "Type a customer ID (1~100):".
  + To help users avoid typing a value in a wrong pattern, you can add the value pattern to the end of the prompt text. For example, "Type an order date (MMM-dd-yy):".
* **Minimum Value/Length**  
  Specify the minimum value of the parameter. If the parameter value type is String, this property name is Minimum Length, which means that you can set the minimum length of the string.
* **Maximum Value/Length**  
  Specify the maximum value of the parameter. If the parameter value type is String, this property name is Maximum Length, which means that you can set the maximum length of the string.
* **String Encoding**  
  Specify the encoding for the parameter values. This property is available when the parameter's data type is String.
* **User Defined Format**  
  You can define your preferred format when Logi Report value formats cannot meet your requirement. Once you define the value format, all the values supplied for the parameter at runtime should be based on it, otherwise you will get an error message.

  Pay attention to the following when using user defined formats for parameter values:

  + The date and time formats should follow the [JDK standard](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).
  + The user defined format shows different appearance under different locale, and you need input values according to the display format. For example, under the Spanish or French locale, **####.##** displays as **#0,##**, and you should follow **#0,##** to input values.
  + The user defined format only controls the format of the input values, which does not mean that the display values are in the same format. To change the display format of a parameter, you need to specify the [Format](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#Format) property of this parameter in the Inspector panel.
  + Decimal number format syntax:

    | Symbol | Meaning | Notes |
    | --- | --- | --- |
    | 0 | A digit |  |
    | \* | A digit. Zero shows as a star. | Cannot mix 0, \*, and \_ in the same format. |
    | \_ | A digit. Zero shows as a space. | Cannot mix 0, \*, and \_ in the same format. |
    | # | A digit. Zero shows as blank. | The actual number might be much larger than the format provided. |
    | . | Placeholder for decimal separator. It might be a comma in some locales. |  |
    | , | Placeholder for grouping delimiter. It might be a period in some locales. | Show the interval to be used. |
    | ; | Separate formats | Positive and negative. |
    | - | If there is no explicit negative sign, - is prefixed. | "#,##0.00" -> "#,##0.00;(#,##0.00)" |
    | % | Divide by 100 and show as a percentage |  |
    | X | You can use any other characters in the prefix or suffix. |  |
  + String format syntax:

    | Symbol | Meaning | Example |
    | --- | --- | --- |
    | % | Any string of zero or more characters. | WHERE title LIKE '%computer%' finds all book titles with the word 'computer' anywhere in the book title. |
    | \_ (underscore) | Any single character. | WHERE au\_fname LIKE '\_ean' finds all four-letter first names that end with ean (such as Dean and Sean). |
    | [ ] | Any single character within the specified range ([a-f]) or set ([abcdef]). | WHERE au\_lname LIKE '[C-P]arsen' finds author last names ending with arsen and beginning with any single character between C and P, for example Carsen, Larsen, and Karsen. |
    | [^] | Any single character not within the specified range ([^a-f]) or set ([^abcdef]). | WHERE au\_lname LIKE 'de[^l]%' finds all author last names beginning with de and where the following letter is not l. |
* **Required**  
   Select **true** if you want to treat the parameter as a required parameter. You must supply a value for a required parameter before a report run. When it is false, Server treats the parameter as an optional parameter. You can leave an optional parameter blank.

  In the dialog box for specifying the parameter value, Server marks the prompt text of a required parameter with an asterisk (\*).

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If the parameter is optional, and you do not expect it to take effect in your report, when specifying the parameter value, clear the contents in the value text box. Any value in the value text box will function in reports.
* **Hide Parameter When Single Value Returned**  
  You see this property when the parameter is bound with a column. Select **true** if you do not want to specify the parameter value at runtime when it has only one value. Server uses the only value as the default value of the parameter.
* **Allow Multiple Values**  
   Select **true** if if you want to specify multiple parameter values for the parameter.
* **Enable the "All Values" Option**  
  Server activates this property when the **Allow Multiple Values** property is true. Its default value is true, which displays **All Values** in the dialog box for specifying multiple values for the parameter.
* **Treat Blank as Null**  
   This property is available only when the parameter's data type is String. Select **true** if you want the parameter value which is empty to be null instead of "".
* **Use Current Date-Time**   
  This property is available only when the parameter's data type is Date, Time, or DateTime. Select **true** if you want to use the current date time in your system as the parameter value.
* **Use Current Date-Time When Blank**  
  This property is available only when the parameter's data type is Date, Time, or DateTime.
  Select **true** if you want to use the current date time in your system as the parameter value when the value is blank.

  If the parameter value type is Date, Time, or DateTime, you can choose whether to get the parameter value dynamically from the system date time by enabling one of the two properties - **Use Current Date-Time** or **Use Current Date-Time When Blank**. However, you need to make sure your system's DateTime format is **yyyy-MM-dd H:mm:ss** as it is the only format Logi Report supports. Otherwise, you need to make use of the User Defined Parameter Format feature. Also, if you enable one of the two properties, you need to provide the parameter's prompt value according to the data type of your parameter.

  + When the data type of the parameter is Date, you can specify the value according to the format **yyyy-MM-dd**.
    - yyyy-01-01: Year will change dynamically.
    - 2007-MM-01: Month will change dynamically.
    - 2007-01-dd: Date will change dynamically.
    - yyyy-MM-01: Year and month will change dynamically.
    - yyyy-01-dd: Year and date will change dynamically.
    - yyyy-MM-dd: Year, month, and date will change dynamically.
    - 2007-MM-dd: Month and date will change dynamically.
  + When the data type of the parameter is Time, you can specify the value according to the format **H:mm:ss**.
    - H:00:00: Hour will change dynamically.
    - 12:mm:00: Minute will change dynamically.
    - 12:00:ss: Second will change dynamically.
    - H:mm:00: Hour and minute will change dynamically.
    - 12:mm:ss: Minute and second will change dynamically.
    - H:00:ss: Hour and second will change dynamically.
    - H:mm:ss: Hour, minute, and second will change dynamically.
  + When the data type of the parameter is DateTime, specify the value in a combination of the preceding two formats.
* **Sort**  
   Server displays this property if you bind the parameter with a column. You can use it to sort the parameter values.
  + **Ascend**  
     Select to sort the parameter values in ascending order.
  + **Descend**  
     Select to sort the parameter values in descending order.
  + **No Sort**  
     Select to display the parameter values in their original order as in the database.
  + **Sort By**  
     Select to open the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741457687831-Custom-Sort-Dialog-Box-Properties) if you want to sort the parameter values by sorting the values of other fields.
* **Distinct**  
   Select **true** if you want repeated values to display only once in the UI for specifying the parameter value.
* **Allow Type-in of Value**  
   Select **true** if you want to type values in addition to selecting values when specifying the parameter value. Server enables this property for **Type-in Parameter** by default.
* **When Out of Value Range**  
   Specify how you want to respond if the typed value is out of the predefined value list when the **Allow Type-in of Value** property is true.
  + **Adopt directly**  
     Select if you want to use the typed value directly.
  + **Use default**  
     Select if you want to use the default value that you defined when creating the parameter.
  + **Warn**  
     Select if you want to display a warning message saying that "Value xxx is out of the available value list".

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) For a multi-valued parameter, if one of the input values is not in the value list, Server treats the whole input result as out of range.
* **Get Value from API Only**  
   Select **true** if you only want to specify the parameter value by API such as URLs, coding, and sessions. In this case, Logi Report does not display any parameter dialog boxes for specifying values.

  When it is false, you can specify the parameter value using both UI and API.

  If a member of a cascading parameter group can only get values from API, all the higher-level members shall get values from API only. This also applies to parameters on which other parameters depend. If in JDashboard several parameters share values, when any of them can only get values from API, they will share the values from API.
* **On Parameter Value Change**  
  Select a formula from the value list that defines an action you want to call when the parameter value changes. You call the action before the other actions defined in the report or library component. It can work as a parameter value validation rule.
* **Encrypt Parameter Value**  
   Select **true** if you want to encrypt the parameter value in the UI where the parameter displays (excluding parameter control and parameter form control) and in log files. However, when the parameter is bound with a column or when its [Allow Multiple Values](#AllowMultipleValues) property is true, Server only encrypts its values in log files.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) When writing the value of a formula or string that references a parameter to log, Server might not encrypt the parameter value.
* **Allow Showing Unencrypted Value**  
   Server activates this property when **Encrypt Parameter Value** is true. Set it to true if you want to display **Hide Parameter Value** in the UI of specifying the parameter value so that you can view the encrypted parameter values when needed.

**OK**

Select to add a parameter in the report and exit the dialog box.

**Cancel**

Select to close the dialog box without adding a parameter.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif) **Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif) **Close button**

Select to close the dialog box without adding a parameter.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741443886487-Add-Aggregation-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741443918871-Aggregate-On-Dialog-Box-Properties)
