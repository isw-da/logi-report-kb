---
title: "Creating Parameters in a Catalog"
id: 5735516481047
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735516481047-Creating-Parameters-in-a-Catalog
updated_at: 2022-11-02T08:07:51Z
---

# Creating Parameters in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525858199-Parameter-Application-Cases)

# Creating Parameters in a Catalog

You can create different types of parameters in a catalog. When you create parameters, you can add prompting text to guide users on how to use them. You can also include a default value or multiple values for users to select without binding with a database table. You can use the parameters defined in a catalog in multiple reports and edit them at any time. In a report that uses business view as the data source, you can also create [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Param) to use in the report specifically. This topic introduces the types of the parameters Logi Report supports and describes how you can create parameters in a catalog and customize the parameter options.

This topic contains the following sections:

* [Parameter Types](#Type)
* [Predefining Parameters in a Catalog](#Predefine)
* [Creating Parameters in a Catalog on Demand](#Create)
* [Setting the Parameter Options](#Options)
  + [User-Defined Format for Parameters](#UDF)

See also [Parameter Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields) for how to work with parameters as component in a report.

## Parameter Types

You can create parameters of the following types in Logi Report:

* **Type-in Parameter**  
  Users can type in value of the parameter at runtime. When the parameter is a date or time value, users can select the date from a calendar widget.
* **Bind with Single Column**  
  Logi Report Engine returns the available list of the parameter values based on a query to the database.
* **Bind with Cascading Columns**  
  Logi Report Engine filters the parameter values from the database based on previously specified values of the cascading group.
* **Bind with Single Column Combined with Type-in**  
  Users can select a value or type their own value, often used for wildcard selections.
* **Multivalued Parameter**  
  Users can select more than one value for the parameter. You can define any of the preceding types as a multivalued parameter.

## Predefining Parameters in a Catalog

You can predefine parameters in a catalog, so you can use them directly when designing reports.

1. [Open the catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, expand the data source to which you want to create the parameter, then do either of the following:
   * Select the **Parameters** node or any existing parameter in the data source and select **New Parameter**  on the Catalog Manager toolbar.
   * Right-click the **Parameters** node in the data source and select **New Parameter** on the shortcut menu.

   Designer displays the [New Parameter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552101271-New-Parameter-Dialog-Box).

   ![New Parameter dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898476079127/nwprm.gif)
3. In the **Name** text box, type a name for the parameter. Since parameters and DBFields share the same name space, you might want to preface parameters with the letter "p" such as "pStartDate".
4. Select a parameter type from the **Value Setting** drop-down list: Type-in Parameter, Bind with Single Column, or Bind with Cascading Columns.
5. In the value section, specify the parameter values. The section varies with the type you select from the Value Setting drop-down list.
   * **For Type-in Parameter**
     1. Specify the data type of the parameter value from the **Value Type** drop-down list.
     2. If you want to provide users with some values, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a value line, then select in the new line and type a value of the specified data type. When the parameter is Date, Time, or DateTime data type, you can also select the **calendar**![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/9898458896919/btn_clndr.gif) to [specify the value](https://devnet.logianalytics.com/hc/en-us/articles/5735525892247-Specifying-Parameter-Values#Date). For a parameter of the Parameters type, the value should be one or more parameter names in the format *@ParameterName* or *@ParameterName1,@ParameterName2*. See [Controlling Multiple Parameters in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735525858199-Parameter-Application-Cases#Control) for an example about this value type.
     3. Repeat the preceding step to add more values.
     4. You can adjust the order of the values using **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif). To delete any unwanted value, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
     5. To set a value as the default selected value for the parameter, select it from the list.
   * **For Bind with Single Column**

     ![Bind with Single Column](https://devnet.logianalytics.com/hc/article_attachments/9898476088215/prmtr_crt_bind.gif)

     1. From the **Data Source** drop-down list, select the data source from which to retrieve values for the parameter: a table, view, synonym, user-defined data source, stored procedure, imported SQL, query, or imported APE (available only when the catalog data source contains a MongoDB connection and you have imported APEs via this connection) in the same catalog data source as the parameter. However, when you are creating the parameter in a catalog data source that contains only MongoDB connections, Designer displays tables, user-defined data sources, and imported APEs if there are any in the drop-down list only.
     2. Select the DBField you want to bind with the parameter from the **Bind Column** drop-down list. At runtime, users will see a list containing all the values in this DBField. For example, "State" would show a list of states the users can choose from.
     3. If you want to display the values of another DBField for users to choose from, select that DBField from the **Display Column** drop-down list.

        Logi Report provides a mechanism that links each value of the display field with the exact value of the bound field for a parameter, thus when you select a value of the display field, Logi Report Engine sends the value of the bound field to the query to filter the query result. This can help you bind the parameter to a DBField to provide a list of values for users to select at runtime. Logi Report Engine applies the selected value of the bound field as the parameter value. For example, it might be confusing if you provide a list of customer IDs for users to select at runtime, since the IDs would probably mean nothing to them. In cases like this, it is better for you to display values of other fields, for example, you might prefer to display customer names instead of IDs. When users select a customer name from the list, Logi Report Engine passes the customer's ID to the query as the parameter value to fulfill the search criteria.
   * **For Bind with Cascading Columns**

     ![Bind with Cascading Columns](https://devnet.logianalytics.com/hc/article_attachments/9898476097303/prmtr_crt_cscd.gif)

     1. From the **Data Source** drop-down list, select the data source from which to retrieve values for the parameter: a table, view, synonym, user-defined data source, stored procedure, imported SQL, query, or imported APE (available only when the catalog data source contains a MongoDB connection and you have imported APEs via this connection) in the same catalog data source as the parameter. However, when you are creating the parameter in a catalog data source that contains only MongoDB connections, Designer displays tables, user-defined data sources, and imported APEs if there are any in the drop-down list only.
     2. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add a parameter line.
     3. Select in the **Bind Column** cell and select a DBField from the drop-down list to bind to the parameter.
     4. If you want to display the values of another DBField for users to choose from, select in the **Display Column** cell and then select that DBField from the drop-down list.
     5. Select in the **Parameter** cell to create the parameter. Designer automatically adds a name for the parameter. Designer creates all parameters in the cascading group as independent parameters and names them in the format: *[The name specified as parameter name]-[Bind Column name]*.
     6. Repeat steps "b" to "e" to create more parameters. Make sure that the selected Bind Column fields are of a cascading hierarchy. In this way, you can create a group of cascading parameters. For example, the parameter group could first be by Country, followed by State, and then by City. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/5735525858199-Parameter-Application-Cases#FilterParam) for an example.
     7. You can adjust the order of the parameters in the cascading group by selecting a parameter and then selecting **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif). To delete a parameter from the cascading group, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif).
6. In the **Options** box, specify [options](#Options) for the parameter according to your requirements.
7. Select **OK** to create the parameter.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* When you create a Bind with Single Column, or Bind with Cascading Columns parameter, Designer does not list the queries that are not based on any table, view, or synonym in the Data Source drop-down list.
* The Bind with Cascading Columns feature is only useful when the default SQL generated by Logi Report Engine returns the correct values for the bound parameters. When you need more complex SQL, you must use Bind With Single Column, and manually specify the SQL to reference the higher level parameter in each lower level. For example, you may have State and City, the City parameter can reference the State parameter such as "SELECT City FROM Customers WHERE Customers.State = @State".
* You cannot use the Bind with Cascading Columns parameter type, when you create a parameter in a catalog data source that contains only XML connections.

## Creating Parameters in a Catalog on Demand

Besides predefining parameters in a catalog via the Catalog Manager, Designer also provides you quick access to create parameters in a catalog from the UI where a parameter list is available, for example in the Resources box of the component wizard. In this parameter list, you can find the option **<New Parameter...>** on the top. Select the option and you can create a parameter in the catalog and use it for the current scenario.

## Setting the Parameter Options

Logi Report provides you with many properties to customize a parameter according to how you would like to use the parameter. For example, you can specify whether a parameter is a required parameter, define the prompting text which can be a guidance for users to provide a meaningful value.

The following table lists the properties Designer provides for customizing a parameter in the parameter dialog box. You can get more properties in the Catalog Manager [Properties sheet](https://devnet.logianalytics.com/hc/en-us/articles/5735545728919-Parameter-Properties).

| Option Name | Description |
| --- | --- |
| Prompt Text | Specifies the text for prompting users to provide value for the parameter. To help users avoid typing a value out of range, you can add the value range to the end of the prompt text, for example, "Type a customer ID (1~100):"; to help users avoid typing a value in a wrong pattern, you can add the value pattern to the end of the prompt text, for example, "Type an order date (MMM-dd-yy):". |
| Minimum Value/Length | Specifies the minimum value allowed for this parameter, or the minimum length for a String type parameter. |
| Maximum Value/Length | Specifies the maximum value allowed for this parameter, or the maximum length for a String type parameter. |
| String Encoding | Designer displays this option when the parameter is String data type. You can use it to specify the encoding for values the parameter. |
| [User Defined Format](#UDF) | Specifies the user-defined format for values of the parameter. For certain types of parameters, the value format Logi Report provides may not satisfy your requirement. In this case, you can define your own preferred format. Once you define the value format, any value supplied to the parameter should be in accordance with this format; otherwise, there is an error message. |
| Required | Specifies whether the parameter is a required parameter. A required parameter must be fulfilled, meaning, users must supply a value for the parameter before they can run the report. When you set this option to "false", the parameter is an optional parameter. The value of an optional parameter can be blank, which means users can either type a value, or leave it as it is. In the dialog box for specifying the parameter value, Logi Report marks the prompt text of a required parameter with the "\*" symbol.  Critical icon If a parameter is optional and you do not expect it to take effect in the report, when specifying the parameter value, you should clear the content in the value text box. Any value left in the text box functions in the report. |
| Hide Parameter When Single Value Returned | Specifies whether to hide the parameter when only a single value is returned to it. When you bind a parameter with a column, you can specify to hide the parameter if only a single value is returned to it at runtime. Logi Report Engine then applies the returned single value as the default value of the parameter. This can be very useful for security. For example, you can use a parameter bound with a DBField such as UserID and if there is one to one mapping of UserID to the Server users, then a query for a parameter such as *Select UserID FROM Employees WHERE UserID = @username* would just return a single value and thus you can use it as a filter for any other queries you create. |
| Allow Multiple Values | Specifies whether to enable users to select multiple values for the parameter. You can use multivalued parameters in dataset filters, query filters, imported SQLs, and subreport/link report conditions. You can also display a multivalued parameter in a report by using the [join()](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions#join) function. |
| Enable the "All Values" Option | Designer enables this option when you set Allow Multiple Values to "true". Its default value is "true", which displays the "All Values" option in the dialog box for specifying multiple values for the parameter. |
| Scope of All Values | Designer enables this option when you set Enable the "All Values" Option to "true". You can use it to specify the meaning of the "All Values" option. Logi Report Engine has two ways to get all values of a parameter. One is to get all values in the database, which is fast but has strict requirements on the parameter; the other is to get all available values as provided in the UI for specifying the parameter values.   * **Auto** Select to let Logi Report Engine decide whether to use all values in the database or all available values according to the parameter condition and performance. "Auto" is the default value of this option, and you should use this value, unless the result is not what you expect. * **All Values in Database** Select to use all the values in the database for the parameter, namely, the reference of the parameter will be ignored. In this way, you may get more values than the available values provided by Logi Report Engine. If the parameter allows type-in values, "All" means all possible values of the parameter data type. * **All Available Values** Select to use all the available values for the parameter. |
| Treat Blank as Null | Designer displays this option when the parameter is String data type. When you set it to "true", the parameter value is null; if "false", the default parameter value is "". |
| [Use Current Date-Time](#CurrentDateTime) | Designer displays this option when the parameter is Date, Time, or DateTime data type. When you set it to "true", Logi Report Engine applies the current date time in your system as value of the parameter. |
| [Use Current Date-Time When Blank](#CurrentDateTime) | Designer displays this option when the parameter is Date, Time, or DateTime data type. When you set it to "true", if the value of the parameter is blank, Logi Report Engine applies the current date time in your system as value of the parameter. |
| Record Level Security | Specifies the record level security to apply to the parameter. When you bind a parameter with a column, you can specify a RLS policy defined on the bound column to the parameter, then at runtime, the specified security identifier only sees the records it is allowed to view in the parameter's value drop-down list. See [Applying RLS to a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735525858199-Parameter-Application-Cases#RLS). |
| Sort | Designer displays this option when you bind the parameter with a column. You can use it to specify how to sort values of the parameter.  * **Ascend** Select to sort the parameter values in an ascending order. * **Descend** Select to sort the parameter values in a descending order. * **No Sort** Select to display the parameter values in their original order as in the database. * **Sort By** Select to open the [Sort By dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567412631-Sort-By-Dialog-Box) to select the fields by which to sort the parameter values. Designer then sorts the parameter values by sorting the values of the specified fields. |
| Distinct | Specifies whether to display identical values only once in the UI for specifying the parameter value. |
| Import SQL | Specifies the SQL statement for retrieving values of the bound column and display column for the parameter. To edit the SQL statement, select in the value cell, then select the **ellipsis**Ellipsis button and edit the statement in the Import SQL dialog box. You can use the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields#UserName)" in the SQL statement as *@username*. Note icon Once you edit the SQL statement, the later changes for Bind Column and Display Column of the parameter cannot take effect unless you remove the SQL lines or bind the parameter all over again (to remove the SQL lines, open the Import SQL dialog box again and clear the content). |
| Allow Type-in of Value | Specifies whether to enable typing values in addition to selecting values when specifying the parameter value. Designer enables this option for Type-in Parameter by default. |
| When Out of Value Range | Designer enables this option only when you set Allow Type-in of Value to "true". You can use it to specify how you want Logi Report Engine to respond if the provided parameter value is out of the predefined value list. There are three solutions:   * **Adopt directly** Select to apply the specified value directly. * **Use default** Select to apply the default value that you define when creating the parameter. * **Warn** Select to display a warning message saying that "Value xxx is out of the available value list".   Note icon For a multivalued parameter, if one of the specified values is not in the value list, Logi Report Engine treats the whole input result as out of range. |
| Get Value from API Only | Specifies whether the parameter values can only be specified using API. When you set this option to "true", users should obtain parameter values only from API and there is no parameter dialog box available in any Designer or Server UI for specifying values. Users need to provide values of the parameter by API such as URLs, coding, and sessions; otherwise, Logi Report Engine applies the default value of the parameter.  When you set this option to "false", the parameter values can be obtained from both GUI and API.  When a member of a cascading parameter group can get values from API only, it means that all the higher level members shall get values from API only. This also applies to parameters on which other parameters depend. When several parameters share values in JDashboard, if any of them can get values from API only, they will share the values from API. |
| On Parameter Value Change | Specifies the action to be called when the parameter value changes. Choose a formula from the drop-down list to develop an action, which Logi Report Engine calls before the other actions defined in the report. It can work as a parameter value validation rule. |
| Encrypt Parameter Value | Specifies whether to encrypt values of the parameter in the UI where the parameter is used or required (excluding parameter control and parameter form control) and in log files. However, when you bind the parameter with a column or set its [Allow Multiple Values](#AllowMultipleValues) to "true", Logi Report Engine only encrypts its values in log files.  Note icon When writing the value of a formula or string that references an encrypted parameter to log, Logi Report Engine may not encrypt the parameter value. |
| Allow Showing Unencrypted Value | Designer enables this option when you set Encrypt Parameter Value to "true". You can use it to specify whether to display the "Hide Parameter Value" option in the UI for specifying the parameter value to allow users to view the unencrypted values of the parameter after the values are encrypted. |

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When you want to get parameter value dynamically from the system's date time, you need to make sure that you select "yyyy-MM-dd H:mm:ss" as the DateTime format of your system, because it is the only format Logi Report supports; otherwise, you need to use the [User-Defined Parameter Format](#UDF) feature. Also, if you enable one of the two options, Use Current Date-Time and Use Current Date-Time When Blank, you need to provide the parameter's prompt value according to the data type of your parameter.

* When the parameter is Date data type, you can specify the value according to the format "yyyy-MM-dd".
  + yyyy-01-01: Year is dynamically changed.
  + 2007-MM-01: Month is dynamically changed.
  + 2007-01-dd: Date is dynamically changed.
  + yyyy-MM-01: Year and month are dynamically changed.
  + yyyy-01-dd: Year and date are dynamically changed.
  + yyyy-MM-dd: Year, month, and date are dynamically changed.
  + 2007-MM-dd: Month and date are dynamically changed.
* When the parameter is Time data type, you can specify the value according to the format "H:mm:ss".
  + H:00:00: Hour is dynamically changed.
  + 12:mm:00: Minute is dynamically changed.
  + 12:00:ss: Second is dynamically changed.
  + H:mm:00: Hour and minute are dynamically changed.
  + 12:mm:ss: Minute and second are dynamically changed.
  + H:00:ss: Hour and second are dynamically changed.
  + H:mm:ss: Hour, minute, and second are dynamically changed.
* When the parameter is DateTime data type, specify the value in a combination of the preceding formats.

### User-Defined Format for Parameters

You should pay attention to the following when using user-defined formats for parameter values.

* The date and time formats should follow the [JDK standard](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).
* The user-defined format shows different appearance under different locale, and you need to specify values according to the displayed format. For example, under the Spanish or French locale, "####.##" displays as "#0,##" and you should follow "#0,##" to type values.
* The user-defined format only limits the format of the input value, which does not mean that the display value is in the same format. To change the display format of a parameter, you need to specify the [Format](https://devnet.logianalytics.com/hc/en-us/articles/5735533553303-Parameter-Field-Properties#Format) property of this parameter in the Report Inspector.

The following tables show the format syntax for decimal numbers and strings.

**Decimal Number Format Syntax**

| Symbol | Meaning | Notes |
| --- | --- | --- |
| 0 | A digit. |  |
| \* | A digit, zero shows as a star. | Cannot mix 0, "\*", and "\_" in the same format. |
| \_ | A digit, zero shows as a space. | Cannot mix 0, "\*", and "\_" in the same format. |
| # | A digit, zero shows as blank. | The actual number may be much larger than the provided format. |
| . | Placeholder for decimal separator, it may be a comma in some locales. |  |
| , | Placeholder for grouping delimiter. It may be a period in some locales. | Shows the interval to be used. |
| ; | Separates formats. | Positive and negative. |
| - | If there is no explicit negative sign, "-" is prefixed. | "#,##0.00" -> "#,##0.00;(#,##0.00)" |
| % | Divides by 100 and shows as a percentage. |  |
| X | Any other characters can be used in the prefix or suffix. |  |

**String Format Syntax**

| Symbol | Meaning | Example |
| --- | --- | --- |
| % | Any string of zero or more characters. | WHERE title LIKE "%computer%" finds all book titles with the word "computer" anywhere in the book title. |
| \_ (underscore) | Any single character. | WHERE au\_fname LIKE "\_ean" finds all four-letter first names that end with "ean" (Dean, Sean, and so on). |
| [ ] | Any single character within the specified range ([a-f]) or set ([abcdef]). | WHERE au\_lname LIKE "[C-P]arsen" finds author last names ending with "arsen" and beginning with any single character between "C" and "P", for example Carsen, Larsen, and Karsen. |
| [^] | Any single character not within the specified range ([^a-f]) or set ([^abcdef]). | WHERE au\_lname LIKE "de[^l]%" finds all author last names beginning with "de" and where the following letter is not "l". |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525858199-Parameter-Application-Cases)
