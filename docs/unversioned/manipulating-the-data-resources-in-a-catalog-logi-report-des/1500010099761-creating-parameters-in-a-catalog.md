---
title: "Creating Parameters in a Catalog"
id: 1500010099761
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog
updated_at: 2021-07-23T19:16:18Z
---

# Creating Parameters in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases)

# Creating Parameters in a Catalog

You can create different types of parameters in a catalog. When you create parameters, you can add prompting text to guide the report users on how to use them. You can also include a default value or multiple values for the report users to select without binding with a database table. You can use the parameters defined in a catalog in multiple reports, and edit them at any time. In a report that uses business view as the data source, you can also create [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param) to use in the report specifically. This topic introduces the types of the parameters Logi Report supports, and describes how you can create parameters in a catalog and customize the parameter options.

This topic contains the following sections:

* [Parameter Types](#Type)
* [Predefining Parameters in a Catalog](#Predefine)
* [Creating Parameters in a Catalog When Needed](#Create)
* [Setting the Parameter Options](#Options)
  + [User-Defined Format for Parameters](#UDF)

See also [Parameter Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010057382-Working-with-Parameter-Fields) for how to work with parameters as component in a report.

## Parameter Types

You can create parameters of the following types in Logi Report:

* **Type-in Parameter**  
  The report users can type in value of the parameter at runtime. When the parameter is a date or time value, the report users can select the date from a calendar widget.
* **Bind with Single Column**  
  Logi Report Engine returns the available list of the parameter values based on a query to the database.
* **Bind with Cascading Columns**  
  Logi Report Engine filters the values shown to the report users from the DBMS based on previously entered parameters.
* **Bind with Single Column combined with Type-in**  
  The report users can select a value or type their own value, often used for wildcard selections.
* **Multi-valued Parameter**  
  The report users can select more than one value for the parameter. You can define any of the above types as a multi-valued parameter.

## Predefining Parameters in a Catalog

You can predefine parameters in a catalog so as to use them directly in reports.

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, expand the data source in which to create the parameter, then:
   * Select the **Parameters** node or any existing parameter in the data source and select **New Parameter**  on the Catalog Manager toolbar.
   * Right-click the **Parameters** node in the data source and select **New Parameter**  on the shortcut menu.

   Designer displays the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098041-New-Parameter-Dialog-Box).

   ![New Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848447255/nwprm.gif)
3. In the **Name** text box, type a name for the parameter. Since parameters and DBFields share the same name space, you might want to preface parameters with the letter "p" such as "pStartDate".
4. Select a parameter type from the **Value Setting** drop-down list: **Type-in Parameter**, **Bind with Single Column**, or **Bind with Cascading Columns**.
5. In the value section, specify the parameter values. The section varies with the type you select from the Value Setting drop-down list.
   * **For Type-in Parameter**
     1. Specify the data type of the parameter value from the **Value Type** drop-down list.
     2. If you want to provide the report users with some values, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a value line, then select in the new line and type a value of the specified data type.

        If the parameter is of the Date, Time, or DateTime data type, you can also select the **calendar** button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to [specify the value](https://devnet.logianalytics.com/hc/en-us/articles/1500010061282-Specifying-Parameter-Values#Date). For a parameter of the Parameters type, the value should be one or more parameter names in the format *@ParameterName* or *@ParameterName1,@ParameterName2* (see [Controlling Multiple Parameters in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#Control) for an example about this value type).
     3. Repeat the above step to add more values.

        To adjust the order of the values, make use of the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons; to delete any unwanted value, select it in the list and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).
     4. To make a value the default selected value for the parameter, select it from the list.
   * **For Bind with Single Column**

     ![Bind with Single Column](https://devnet.logianalytics.com/hc/article_attachments/4404848447511/prmtr_crt_bind.gif)

     1. From the **Source** drop-down list, select the required data source type: **Tables and Views** (including synonyms), **Stored Procedures**, **Imported SQLs**, or **User Defined**, Designer then displays all DBFields in the current catalog data source of this type for retrieving values for the parameter. However, when you are creating the parameter in a catalog data source that contains only MongoDB connections, Designer only displays the Tables and User Defined type in the drop-down list.
     2. Select the field you want to bind with the parameter from the **Bind Column** drop-down list. At runtime, the report users will see a list containing all the values in this field. For example, "State" would show a list of states the users can choose from.
     3. If you want to display the values of another field for the report users to choose from, select that field from the **Display Column** drop-down list.

        Logi Report provides a mechanism that links each value of the display field with the exact value of the bound field for a parameter, thus when you select a value of the display field, Logi Report Engine sends the value of the bound field to the query to filter the query result. This can help you bind the parameter to a DBField in order to provide a list of values for the report users to select at runtime, which probably makes more sense. Logi Report Engine applies the selected value of the bound field as the parameter value. For example, it might be confusing if you provide a list of customer IDs for users to select at runtime, since the IDs would probably mean nothing to them. In cases like this, it is better for you to display values of other fields, for example, you might prefer to display customer names instead of IDs. When the report users select a customer name from the list, Logi Report Engine passes the customer's ID to the query as the parameter value so as to fulfill the search criteria.
   * **For Bind with Cascading Columns**

     ![Bind with Cascading Columns](https://devnet.logianalytics.com/hc/article_attachments/4404856856855/prmtr_crt_cscd.gif)

     1. From the **Data Source** drop-down list, select the required data source from which to retrieve values for the parameter: a table, view, synonym, stored procedure, imported SQL, or user-defined data source in the same catalog data source as the parameter. However, when you are creating the parameter in a catalog data source that contains only MongoDB connections, Designer only displays tables and user-defined data sources in the drop-down list.
     2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) to add a parameter row.
     3. Select in the **Bind Column** cell and select a field from the drop-down list to bind to the parameter.
     4. If you want to display the values of another field for the report users to choose from, select in the **Display Column** cell and then select that field from the drop-down list.
     5. Select in the **Parameter** cell to create the parameter. Designer automatically adds a name for the parameter. Designer creates all parameters in the cascading group as independent parameters and names them in the format: *[The name specified as parameter name]-[Bind Column name]*.
     6. Repeat steps "b" to "e" to create more parameters. Make sure that the selected Bind Column fields are of a cascading hierarchy. In this way, you can create a group of cascading parameters. For example, the parameter group could first be by Country, followed by State, and then by City. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#FilterParam) for an example.

        To adjust the order of the parameters, make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif); to delete any unwanted parameter from the cascading group, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).

     ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) The Bind with Cascading Columns feature is only useful when the default SQL generated by Logi Report Engine returns the correct values for the bound parameters. When you need more complex SQL, you must use Bind With Single Column and manually specify the SQL to reference the higher level parameter in each lower level. For example, you may have State and City, the City parameter can reference the State parameter such as "SELECT City FROM Customers WHERE Customers.State = @State".
6. In the **Options** box, set [options](#Options) for the parameter according to your requirements.
7. Select **OK** to create the parameter.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you create a parameter in a catalog data source that contains only XML connections, the parameter type Bind with Cascading Columns is not supported; while when you create a parameter in a catalog data source that contains only MongoDB connections, you can only bind tables and user-defined data sources with the parameter.

## Creating Parameters in a Catalog When Needed

Besides predefining parameters in a catalog via the Catalog Manager, Designer also provides you quick access to create parameters in a catalog from the UI where a parameter list is available, for example in the Resources box of the report wizard. In this parameter list, you can fine the item **<New Parameter...>** on the top. By selecting the item, you can create any parameters you want with the New Parameter dialog box, which Designer automatically adds into the current catalog.

## Setting the Parameter Options

Logi Report provides you with many properties to customize a parameter according to how you would like to use the parameter. For example, you can specify whether a parameter is a required parameter, define the prompting text which can be a guidance for the report users to provide a meaningful value.

The following table lists the properties Designer provides for customizing a parameter in the parameter dialog box. You can get more properties in the Catalog Manager [Properties sheet](https://devnet.logianalytics.com/hc/en-us/articles/1500010061522-Parameter-Properties).

| Option Name | Description |
| --- | --- |
| Prompt Text | Specifies the text for prompting the report users to provide the value of the parameter. By default, if you do not specify the prompting text, the report users only see the parameter names. Note icon   * To help users avoid typing a value out of range, you can add the value range to the end of the prompt text, for example, "Type a customer ID (1~100):". * To help users avoid typing a value in a wrong pattern, you can add the value pattern to the end of the prompt text, for example, "Type an order date (MMM-dd-yy):". |
| Minimum Value/Length | Specifies the minimum value allowed for the parameter. If the parameter's value type is String, this option is Minimum Length, and you can set the minimum allowed length of the string. |
| Maximum Value/Length | Specifies the maximum value allowed for the parameter. If the parameter's value type is String, this option is Maximum Length, and you can set the maximum allowed length of the string. |
| String Encoding | Designer displays the option when the parameter's data type is String. You can use it to specify the encoding for the parameter. |
| [User Defined Format](#UDF) | For certain types of parameters, the value format supplied by Logi Report may not satisfy your requirement. In this case, you can define your own preferred format. Once you define the value format, all the values supplied for the parameter at runtime should be based on it; otherwise, there is an error message. |
| Required | Specifies whether or not to treat the parameter as a required one. A required parameter must be fulfilled, meaning the report users must supply a value for the parameter before they can run the report. When you set the option to "false", the parameter is an optional parameter. An optional parameter can be left blank, which means the report users can either type a value, or leave it as it is. In the dialog box for specifying the parameter value, Logi Report marks the prompt text of a required parameter with the "\*" symbol.  Critical icon If a parameter is optional and you do not expect it to take effect in your report, when specifying the parameter value, you should clear the content in the value text box. Any value left in the text box functions in the report. |
| Hide Parameter When Single Value Returned | When a parameter is bound with a column, you can hide the parameter at runtime when only a single value is returned for the parameter. Logi Report Engine then applies the returned single value as the default value of the parameter. This can be very useful for security. For example, you could use a parameter bound with a DBField such as UserID and if there is one to one mapping of UserID to the Logi Report Server login users, then a query for a parameter such as *Select UserID FROM Employees WHERE UserID = @username* would just return a single value and thus could be used as a filter for any other queries you create. |
| Allow Multiple Values | Enables the report users to select multiple values for the parameter. You can use multi-valued parameters in dataset filters, query filters, imported SQLs, and subreport/link report conditions. You can also display a multi-valued parameter in a report by using the [join()](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions#join) function. |
| Enable the "All Values" Option | Designer enables the option only when you set Allow Multiple Values to "true". Its default value is "true", which displays the "All Values" option in the dialog box for specifying multiple values for the parameter. |
| Scope of All Values | Designer enables the option only when you set Enable the "All Values" Option to "true". You can use it to specify the meaning of the "All Values" option. Logi Report Engine has two ways to get all values of a parameter. One is to get all values in the database, which is fast but has strict requirements on the parameter; the other is to get all available values as provided in the UI for specifying the parameter values.   * **Auto** Select to let Logi Report Engine decide whether to use all values in the database or all available values according to the parameter condition and performance. "Auto" is the default value of this option, and this is recommended unless the result is not what you expected. * **All Values in Database** Select to use all the values in the database for the parameter, namely, the reference of the parameter will be ignored. In this way, you may get more values than the available values provided by Logi Report Engine.   If the parameter allows type-in values, "All" means all possible values of the parameter data type. * **All Available Values** Select to use all the available values for the parameter. |
| Treat Blank as Null | Designer displays the option when the parameter's data type is String. If you set it to true, the parameter value is null; if false, the default parameter value is "". |
| Use Current Date-Time | Designer displays the option when the parameter's data type is Date, Time, or DateTime. If you set it to "true", Logi Report Engine applies the current date time in your system as value of the parameter. |
| Use Current Date-Time When Blank | Designer displays the option when the parameter's data type is Date, Time, or DateTime. If you set it to "true", when the value of the parameter is blank, Logi Report Engine applies the current date time in your system as value of the parameter. If you want to get parameter value dynamically from the system's date time, you need to make sure your system's DateTime format is set to "yyyy-MM-dd H:mm:ss", because it is the only format Logi Report supports; otherwise, you need to make use of the User-Defined Parameter Format feature. Also, if one of the two options is enabled, you need to provide the parameter's prompt value according to the data type of your parameter.   * When the data type of the parameter is Date, you can specify the value according to the format "yyyy-MM-dd".   + yyyy-01-01: Year is dynamically changed.   + 2007-MM-01: Month is dynamically changed.   + 2007-01-dd: Date is dynamically changed.   + yyyy-MM-01: Year and month are dynamically changed.   + yyyy-01-dd: Year and date are dynamically changed.   + yyyy-MM-dd: Year, month, and date are dynamically changed.   + 2007-MM-dd: Month and date are dynamically changed. * When the data type of the parameter is Time, you can specify the value according to the format "H:mm:ss".   + H:00:00: Hour is dynamically changed.   + 12:mm:00: Minute is dynamically changed.   + 12:00:ss: Second is dynamically changed.   + H:mm:00: Hour and minute are dynamically changed.   + 12:mm:ss: Minute and second are dynamically changed.   + H:00:ss: Hour and second are dynamically changed.   + H:mm:ss: Hour, minute, and second are dynamically changed. * When the data type of the parameter is DateTime, specify the value in a combination of the above. |
| Record Level Security | When a parameter is bound with a column, you can specify a RLS policy defined on the bound column to the parameter, then at runtime, the specified security identifier only sees the records it is allowed to view in the parameter value drop-down list. See [Applying RLS to a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#RLS) for an example. |
| Sort | Specifies how to sort values of cascading parameters.  * **Ascend** Select to sort the parameter values in an ascending order. * **Descend** Select to sort the parameter values in a descending order. * **No Sort** Select to display the parameter values in their original order as in the database. * **Sort By** Select to sort the parameter values by sorting other fields in the same data source as the cascading group. When you select Sort By, Designer displays the [Sort By](https://devnet.logianalytics.com/hc/en-us/articles/1500010098801-Sort-By-Dialog-Box) dialog for you to specify the fields and their sorting orders. |
| Distinct | If you set the option to "true", in the UI for specifying the parameter value, Logi Report Engine displays the identical values only once and does not list any duplicate values. |
| Import SQL | Specifies the SQL statement for retrieving values of the bound column and display column. To edit the SQL statement, select in the value cell, then select the ellipsis button Ellipsis button and edit the statement in the Import SQL dialog box. Note icon   * Once you edit the SQL statement, the later changes for Bind Column and Display Column cannot take effect unless you remove the SQL lines or bind the parameter all over again. To remove the SQL lines, select Ellipsis button in the value cell and clear the content in the Import SQL dialog box. * You can also use the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields#UserName)" in the SQL statement as *@username*. |
| Allow Type-in of Value | Specifies whether to enable typing values in addition to selecting values when specifying the parameter value. Designer enables the option for Type-in Parameter by default. |
| When Out of Value Range | Designer enables the option only when you set Allow Type-in of Value to "true". You can use it to specify how you want Logi Report Engine to respond if the typed parameter value is out of the predefined value list. There are three solutions as follows:   * **Adopt directly** Select to apply the typed value directly. * **Use default** Select to apply the default value that you define when creating the parameter. * **Warn** Select to display a warning message telling that "Value xxx is out of the available value list".   Note icon For a multi-valued parameter, if one of the input values is not in the value list, Logi Report Engine treats the whole input result as out of range. |
| Get Value from API Only | Specifies whether the parameter values can only be specified using API. If true, the report users should obtain parameter values only from API and there is no parameter dialog boxes available on any Designer or Server UI for inputting values. The report users have to give the values of the parameter by API such as URLs, coding, and sessions; otherwise. Logi Report Engine applies the default value of the parameter.  If false, the parameter can be obtained from both GUI and API.  If a member of a cascading parameter group can get values from API only, it means that all the higher level members shall get values from API only. This also applies to parameters on which other parameters depend. If several parameters share values in JDashboard, when any of them can get values from API only, they will share the values from API. |
| On Parameter Value Change | Specifies the action to be called when the parameter value changes. Choose a formula from the drop-down list to develop an action, which Logi Report Engine calls before the other actions defined in the report. It can work as a parameter value validation rule. |
| Encrypt Parameter Value | Specifies whether to encrypt the values of the parameter in the UI where the parameter is used or required (excluding parameter control and parameter form control) and in log files. However, when the parameter is bound with a column or when its [Allow Multiple Values](#AllowMultipleValues) is true, Logi Report Engine only encrypts its values in log files. Note icon When writing the value of a formula or string that references a encrypted parameter to log, Logi Report Engine may not encrypt the parameter value. |
| Allow Showing Unencrypted Value | Designer enables the option only when you set Encrypt Parameter Value to true. You can use it to specify whether to display the "Hide Parameter Value" option in the UI for specifying the parameter value to allow the report users to view the unencrypted values of the parameter after the values are encrypted. |

### User-Defined Format for Parameters

You should pay attention to the following when using user-defined formats for parameter values:

* The date and time formats should follow the [JDK standard](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).
* The user-defined format shows different appearance under different locale, and you need to specify values according to the displayed format. For example, under the Spanish or French locale, "####.##" displays as "#0,##" and you should follow "#0,##" to type in values.
* The user-defined format only limits the format of the input value, which does not mean that the display value is in the same format. To change the display format of a parameter, you need to specify the [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010100721-Parameter-Field-Properties#Format) property of this parameter in the Report Inspector.
* Decimal number format syntax:  

  | Symbol | Meaning | Notes |
  | --- | --- | --- |
  | 0 | A digit. |  |
  | \* | A digit, zero shows as a star. | Cannot mix 0, "\*", and "\_" in same format. |
  | \_ | A digit, zero shows as a space. | Cannot mix 0, "\*", and "\_" in same format. |
  | # | A digit, zero shows as blank. | The actual number may be much larger than the format provided. |
  | . | Placeholder for decimal separator, it may be a comma in some locales. |  |
  | , | Placeholder for grouping delimiter. It may be a period in some locales. | Shows the interval to be used. |
  | ; | Separates formats. | Positive and negative. |
  | - | If there is no explicit negative sign, "-" is prefixed. | "#,##0.00" -> "#,##0.00;(#,##0.00)" |
  | % | Divides by 100 and shows as a percentage. |  |
  | X | Any other characters can be used in the prefix or suffix. |  |
* String format syntax:  

  | Symbol | Meaning | Example |
  | --- | --- | --- |
  | % | Any string of zero or more characters. | WHERE title LIKE "%computer%" finds all book titles with the word "computer" anywhere in the book title. |
  | \_ (underscore) | Any single character. | WHERE au\_fname LIKE "\_ean" finds all four-letter first names that end with "ean" (Dean, Sean, and so on). |
  | [ ] | Any single character within the specified range ([a-f]) or set ([abcdef]). | WHERE au\_lname LIKE "[C-P]arsen" finds author last names ending with "arsen" and beginning with any single character between "C" and "P", for example Carsen, Larsen, and Karsen. |
  | [^] | Any single character not within the specified range ([^a-f]) or set ([^abcdef]). | WHERE au\_lname LIKE "de[^l]%" finds all author last names beginning with "de" and where the following letter is not "l". |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases)
