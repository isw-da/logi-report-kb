---
title: "Creating Parameters in a Catalog"
id: 1500009611502
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog
updated_at: 2021-07-24T16:03:50Z
---

# Creating Parameters in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases)

# Creating Parameters in a Catalog

This topic introduces creating parameters in a catalog. In a report that uses business view as the data source, you can also create [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Param) to use in the report specifically.

This topic includes the following sections:

* [Predefining Parameters in a Catalog](#Predefine)
* [Creating Parameters in a Catalog When Needed](#Create)
* [Setting the Parameter Options](#Options)
  + [User Defined Format for Parameters](#UDF)

See also [Parameter Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009606382-Parameter-Fields) for how to work with parameters as component in a report.

## Predefining Parameters in a Catalog

You can predefine parameters in a catalog so as to use them directly in reports.

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, expand the data source in which to create the parameter, then:
   * Select the **Parameters** node or any existing parameter in the data source and select **New Parameter**  on the Catalog Manager toolbar.
   * Right-click the **Parameters** node in the data source and select **New Parameter**  on the shortcut menu.

   The [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009632681-New-Parameter-Dialog) dialog appears.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911652503/nwprm.gif)
3. In the Name text box, type a name for the parameter. Since parameters and DBFields share the same name space, you might want to preface parameters with the letter "p" such as pStartDate.
4. Select a parameter type from the Value Setting drop-down list: Type-in Parameter, Bind with Single Column or Bind with Cascading Columns.
5. In the value section, specify the parameter values as required. The section varies with the type you select from the Value Setting drop-down list.
   * **For Type-in Parameter**
     1. Specify the data type of the parameter value from the Value Type drop-down list.
     2. If you want to provide end users with some values, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a value line, select on the new line and then type in a value of the specified data type.

        If the parameter is of Date, DateTime, or Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404904203031/btn_clndr.gif) to [specify the value](https://devnet.logianalytics.com/hc/en-us/articles/1500009634541-Specifying-Parameter-Values#Date). For a parameter of the Parameters type, the value should be one or more parameter names in the format *@ParameterName* or *@ParameterName1,@ParameterName2* (see [Controlling Multiple Parameters in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#Control) for an example about this value type).
     3. Repeat the above step to add more values.

        To adjust the order of the values, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif); to remove any unwanted value, select it in the list and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).
     4. To make a value the default selected value for the parameter, select it from the list.
   * **For Bind with Single Column**

     ![Bind with Single Column](https://devnet.logianalytics.com/hc/article_attachments/4404911652759/prmtr_crt_bind.gif)

     1. From the Source drop-down list, select the required data source type: Tables and Views (including synonyms), Stored Procedures, Imported SQLs, or User Defined, then all DBFields in the current catalog data source of this type will be available for retrieving values for the parameter.
     2. Select the field to be bound with the parameter from the Bind Column drop-down list. At runtime, end users will see a list containing all the values in this field. For example State would show a list of states the users can choose from.
     3. If you want the values of another field to be displayed for the end users to choose from, select that field from the Display Column drop-down list.

        Logi Report provides a mechanism that links each value of the display field with the exact value of the bound field for a parameter, thus when you select a value of the display field, the value of the bound field is actually sent to the query and filters the query result. This can help you bind the parameter to a DBField in order to provide a list of values for end users to select at runtime which probably makes more sense. The selected value of the bound field will be used as the parameter value. For example, it might be confusing if you provide a list of customer ID numbers for users to select at runtime, since the ID numbers would probably mean nothing to them. In cases like this, it is better for you to display values of other fields, which would make more sense. For this case, you might prefer to display customer names instead of ID numbers. When the report end users select a customer name from the list, its ID number is passed to the query as the parameter value so that the search criteria can be fulfilled.
   * **For Bind with Cascading Columns**

     ![Bind with Cascading Columns](https://devnet.logianalytics.com/hc/article_attachments/4404911653015/prmtr_crt_cscd.gif)

     1. From the Data Source drop-down list, select the required data source from which to retrieve values for the parameter: a table, view, synonym, stored procedure, imported SQL, or user defined data source.
     2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to add a parameter row.
     3. Select in the Bind Column cell and select a field from the drop-down list to bind to the parameter.
     4. If you want the values of another field to be displayed for end users to choose from, select in the Display Column cell and then select that field from the drop-down list.
     5. Select in the Parameter cell to create the parameter. A name for the parameter will then be automatically added by Logi Report.
     6. Repeat steps b to e to create more parameters. Make sure that the selected Bind Column fields are of a cascading hierarchy. In this way, a group of cascading parameters are created. For example, the parameter group could first be by Country followed by State and then by City. [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#FilterParam) for an example.

        To adjust the order of the parameters, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif); to remove any unwanted parameter from the cascading group, select it and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).
6. In the Options box, set [options](#Options) for the parameter according to your requirements.
7. Select **OK** to create the parameter.

**Notes:**

* When you create a parameter in a catalog data source that contains only XML connections, the parameter type Bind with Cascading Columns is not supported.
* If a parameter is added in a catalog data source that contains only MongoDB connections, only tables and user defined data sources can be used to bind with the parameter.

## Creating Parameters in a Catalog When Needed

Besides predefining parameters in a catalog via the Catalog Manager, Logi Report Designer also provides you quick access to create parameters in a catalog from the UI where a parameter list is available, for example in the Resources box of the report wizard. In this parameter list, the <New Parameter...> item is provided on the top. By selecting the item, you can create any parameters you want with the New Parameter dialog, which are then added into the current catalog.

## Setting the Parameter Options

Logi Report provides you with many properties to customize a parameter according to how the parameter will be used. For example, you can specify whether a parameter is a required parameter, define the prompting text which can be a guidance for the report end users to provide a meaningful value.

The following table lists the properties available for customizing a parameter in the parameter dialog. More properties can be accessed in the Catalog Manager [Properties sheet](https://devnet.logianalytics.com/hc/en-us/articles/1500009634841-Parameter-Properties).

| Option Name | Description |
| --- | --- |
| Prompt Text | Specifies the text for prompting users to provide the value of the parameter. **Tips**:   * To help users avoid typing a value out of range, you can add the value range to the end of the prompt text. For example, "Type a customer ID (1~100):". * To help users avoid typing a value in a wrong pattern, you can add the value pattern to the end of the prompt text. For example, "Type an order date (MMM-dd-yy):". |
| Minimum Value/Length | Specifies the minimum value allowed for the parameter. If the parameter value type is String, this option is defined as Minimum Length, which means that you can set the minimum allowed length of the string. |
| Maximum Value/Length | Specifies the maximum value allowed for the parameter. If the parameter value type is String, this option is defined as Maximum Length, which means that you can set the maximum allowed length of the string. |
| String Encoding | Specifies the encoding for the parameter. Available only when the parameter's data type is defined as String. |
| [User Defined Format](#UDF) | For certain types of parameters, the value format supplied by Logi Report may not satisfy your requirement. In this case, you can define your own preferred format. When you have defined the value format, all the values supplied for the parameter at runtime should be based on it, otherwise there will be an error message. |
| Required | Specifies whether or not the parameter will be treated as a required one. A required parameter must be fulfilled, which means that you must supply a value for the parameter before the report can be run. When the property is false, the parameter will be treated as an optional parameter. An optional parameter can be left blank, which means you can either type a value, or leave it as it is. In the dialog for specifying the parameter value, the prompt text of a required parameter will be marked with a \* sign.  **Note**: If the parameter is optional and you do not expect it to take effect in your report, when specifying the parameter value, clear the content in the value text box. Any value left in the field will function in reports. |
| Hide Parameter When Single Value Returned | When a parameter is bound with a column, you can choose to hide the parameter at runtime when only a single value is returned for the parameter, and the returned single value will be used as default value of the parameter. This can be very useful for security. For example, you could use a parameter bound with a DBField such as UserID and if there is one to one mapping of UserID to the Logi Report login users, then a query for a parameter such as *Select UserID FROM Employees WHERE UserID = @username* would just return a single value and thus could be used as a filter for any other queries you create. |
| Allow Multiple Values | Enables multiple values to be selected for the parameter. Multi-valued parameters can be used in dataset filters, query filters, imported SQLs, and subreport/link report conditions. A multi-valued parameter can also be displayed in a report by using the [join()](https://devnet.logianalytics.com/hc/en-us/articles/1500009605182-Appendix-1-Formula-Functions#join) function. |
| Enable the "All Values" Option | Available when **Allow Multiple Values** is true. Its default value is true which will display the "All Values" option in the dialog for specifying multiple values for the parameter. |
| Scope of All Values | Available when **Enable the "All Values" Option** is true. It defines the meaning of the "All Values" option. Logi Report has two ways to get all values of a parameter. One is to get all values in the database, which is fast but has strict requirements on the parameter; the other is to get all available values as provided in the UI for specifying the parameter values.   * **Auto**  Specifies to let Logi Report decide whether to use all values in database or all available values according to the parameter condition and performance. By default Auto is selected and this is recommended unless the result is not what you expected. * **All Values in Database**  Specifies to use all the values in the database for the parameter, namely the reference of the parameter will be ignored. In this way, you may get more values than the available values provided by Logi Report.   If the parameter allows type-in values, "All" means all possible values of the parameter data type. * **All Available Values**  Specifies to use all the available values for the parameter. |
| Treat Blank as Null | Available when the parameter's data type is String. If it is true, the parameter value will be null; if false, the default parameter value is "". |
| Use Current Date-Time | Available when the parameter's data type is Date, Time or DateTime. If it is true, the current date time in your system will be used as value of the parameter. |
| Use Current Date-Time When Blank | Available when the parameter's data type is Date, Time or DateTime. If it is true, when the value of the parameter is blank, the current date time in your system will be used as value of the parameter. If you want to get parameter value dynamically from the system's date time, you need to make sure your system's DateTime format is set to yyyy-MM-dd H:mm:ss as it is the only format Logi Report supports; otherwise, you need to make use of the User Defined Parameter Format feature. Also, if one of the two options is enabled, you need to provide the parameter's prompt value according to the data type of your parameter.   * When the data type of the parameter is Date, you can specify the value according to the format yyyy-MM-dd.   + yyyy-01-01: Year will be dynamically changed.   + 2007-MM-01: Month will be dynamically changed.   + 2007-01-dd: Date will be dynamically changed.   + yyyy-MM-01: Year and month will be dynamically changed.   + yyyy-01-dd: Year and date will be dynamically changed.   + yyyy-MM-dd: Year, month, and date will be dynamically changed.   + 2007-MM-dd: Month and date will be dynamically changed. * When the data type of the parameter is Time, you can specify the value according to the format H:mm:ss.   + H:00:00: Hour will be dynamically changed.   + 12:mm:00: Minute will be dynamically changed.   + 12:00:ss: Second will be dynamically changed.   + H:mm:00: Hour and minute will be dynamically changed.   + 12:mm:ss: Minute and second will be dynamically changed.   + H:00:ss: Hour and second will be dynamically changed.   + H:mm:ss: Hour, minute and second will be dynamically changed. * When the data type of the parameter is DateTime, specify the value in a combination of the above. |
| Record Level Security | When a parameter is bound with a column, you can specify a RLS policy defined on the bound column to the parameter, then at runtime the specified security identifier will see the records it is allowed to view in the parameter value drop-down list. See [Applying RLS to a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#RLS) for an example. |
| Sort | Specifies how to sort values of cascading parameters.  * **Ascend**  Sorts parameter values in an ascending order. * **Descend**  Sorts parameter values in a descending order. * **No Sort**  The parameter values are displayed in the original order as in database. * **Sort By**  Sorts parameter values by sorting other fields in the same data source as the cascading group. When Sort By is selected, the [Sort By](https://devnet.logianalytics.com/hc/en-us/articles/1500009633621-Sort-By-Dialog) dialog will be displayed for specifying fields and their sorting orders. |
| Distinct | If set to true, in the UI for specifying the parameter value, identical values will appear only once and no duplicate values will be listed. |
| Import SQL | Displays the SQL statement for retrieving values of the bound column and display column. You can edit the statement. To do this, select in the value cell, then select Choose button and edit the statement in the Import SQL dialog. **Notes**:   * If you have made changes to the SQL statement, the later changes for Bind Column and Display Column will not take effect unless you remove the SQL lines or bind the parameter all over again. To remove the SQL lines, select Choose button in the value cell and clear the content in the Import SQL dialog. * The special field User Name can also be used in the SQL statement as *@username*. |
| Allow Type-in of Value | Specifies whether to enable typing values in addition to selecting values when specifying the parameter value at runtime. The property is enabled for Type-in Parameter by default. |
| When Out of Value Range | Specifies how Logi Report will respond if the typed value is out of the predefined value list. The property is enabled only when the option Allow Type-in of Value is set to true. There are three solutions as follows:   * **Adopt directly**  The typed value will be used directly. * **Use default**  The default value defined when creating the parameter will be used. * **Warn**  Displays a warning message telling that "Value xxx is out of the available value list".   **Note**: For a multi-valued parameter, if one of the input values is not in the value list, the whole input result will be treated as out of range. |
| Get Value from API Only | Specifies whether the parameter values can only be specified using API. If true, the parameter values should only be obtained from API and there will be no parameter dialogs available on any Logi Report Designer or Server UI for inputting values. Users will have to give the values of the parameter by API such as URLs, coding, and sessions, otherwise the default value will be used.  If false, the parameter can be obtained from both GUI and API.  If a member of a cascading parameter group is set to get values from API only, it means that all the higher level members shall get values from API only. This also applies to parameters on which other parameters depend. If in JDashboard several parameters share values, when any of them is set to get values from API only, they will share the values from API. |
| On Parameter Value Change | Specifies to define an action that will be called when the parameter value changes. Choose a formula from the drop-down list to develop an action, which will be called before the other actions defined in the report or library component. It can work as a parameter value validation rule. |
| Encrypt Parameter Value | Specifies whether to encrypt the values of the parameter in the UI where the parameter is used or required (excluding parameter control and parameter form control) and in log files. However, when the parameter is bound with a column or when its [Allow Multiple Values](#AllowMultipleValues) is true, its values will only be encrypted in log files. **Note**: When writing the value of a formula or string that references a parameter to log, the parameter value may not be encrypted. |
| Allow Showing Unencrypted Value | The option is enabled when Encrypt Parameter Value is true. It specifies whether to display the option Hide Parameter Value in the UI for specifying the parameter value to allow end users to view the unencrypted values of the parameter after the values are encrypted. |

### User Defined Format for Parameters

You should pay attention to the following when using user defined formats for parameter values:

* The date and time formats should follow the [JDK standard](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).
* The user defined format will show different appearance under different locale, and you need to specify values according to the displayed format. For example, under the Spanish or French locale, ####.## will be displayed as #0,## and you should follow #0,## to type in values.
* The user defined format only limits the format of the input value, which does not mean that the display value will be in the same format. To change the display format of a parameter, you will need to specify the [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009635661-Parameter-Field-Properties#Format) property of this parameter in the Report Inspector.
* Decimal number format syntax:  

  | Symbol | Meaning | Notes |
  | --- | --- | --- |
  | 0 | A digit |  |
  | \* | A digit, zero shows as a star | Can't mix 0, \*, and \_ in same format |
  | \_ | A digit, zero shows as a space | Can't mix 0, \*, and \_ in same format |
  | # | A digit, zero shows as blank | The actual number may be much larger than the format provided |
  | . | Placeholder for decimal separator, it may be a comma in some locales. |  |
  | , | Placeholder for grouping delimiter, it may be a period in some locales. | Shows the interval to be used |
  | ; | Separates formats | positive and negative. |
  | - | If there is no explicit negative sign, - is prefixed | "#,##0.00" -> "#,##0.00;(#,##0.00)" |
  | % | Divides by 100 and shows as a percentage |  |
  | X | Any other characters can be used in the prefix or suffix |  |
* String format syntax:  

  | Symbol | Meaning | Example |
  | --- | --- | --- |
  | % | Any string of zero or more characters. | WHERE title LIKE '%computer%' finds all book titles with the word 'computer' anywhere in the book title. |
  | \_ (underscore) | Any single character. | WHERE au\_fname LIKE '\_ean' finds all four-letter first names that end with ean (Dean, Sean, and so on). |
  | [ ] | Any single character within the specified range ([a-f]) or set ([abcdef]). | WHERE au\_lname LIKE '[C-P]arsen' finds author last names ending with arsen and beginning with any single character between C and P, for example Carsen, Larsen, Karsen, and so on. |
  | [^] | Any single character not within the specified range ([^a-f]) or set ([^abcdef]). | WHERE au\_lname LIKE 'de[^l]%' finds all author last names beginning with de and where the following letter is not l. |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases)
