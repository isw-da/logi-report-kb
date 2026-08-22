---
title: "Parameter Properties"
id: 1500009634841
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634841-Parameter-Properties
updated_at: 2021-07-24T16:03:45Z
---

# Parameter Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611702-MongoDB-Element-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634861-Query-Properties)

# Parameter Properties

This topic lists the properties of a Parameter object in a catalog.

| Property Name | Description |
| --- | --- |
| General | |
| Allow Showing Unencrypted Value | The property is enabled when [Encrypt Parameter Value](#Encrypt) is true. It specifies whether to display the option Hide Parameter Value in the UI for specifying the parameter value to allow end users to view the unencrypted values of the parameter after the values are encrypted. Data type: Boolean |
| Bind Column | Specifies the bind column of the parameter. Data type: String |
| Binding | Specifies the parameter which will be bound with the current one to sort the column controlled by the current parameter. Data type: String |
| Default Value Number | Specifies the parameter value that will be prompted by default at runtime. If it is set to 0, the first parameter value in the Value property will be prompted; if it is set to -1, the last parameter value in the Value property will be prompted. Data type: Integer |
| Description | Specifies the description of the parameter. Data type: String |
| Display Column | Specifies the display column of the parameter. Data type: String |
| Display Width | Specifies the display width of the parameter. Type a numeric value to change the width. Data type: Float  **Notes:**   * If the Display Width value of a parameter is not set in the Catalog Manager, the parameter will be inserted in a report with the default width defined by Logi Report. * Assume that you have set the Display Width of a parameter, and used the parameter while creating a new component with the report wizard, its width may be adjusted according to the paper size. |
| Distinct | If set to true, in the UI for specifying the parameter value, identical values will appear only once and no duplicate values will be listed. Data type: Boolean |
| Encrypt Parameter Value | Specifies whether to encrypt the values of the parameter In the UI where the parameter is used or required (excluding parameter control and parameter form control) and in log files. However, when the parameter is bound with a column or when its [Allow Multiple Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog#AllowMultipleValues) property is true, its values will only be encrypted in log files. **Note**: When writing the value of a formula or string that references a parameter to log, the parameter value may not be encrypted.  Data type: Boolean |
| Get Value from API Only | Specifies whether the parameter values can only be specified using API. If true, the parameter values should only be obtained from API and there will be no parameter dialogs available on any Logi Report Designer or Server UI for inputting values. Users will have to give the values of the parameter by API such as URLs, coding, and sessions, otherwise the default value will be used.  If false, the parameter can be obtained from both UI and API.  If a member of a cascading parameter group is set to get values from API only, it means that all the higher level members shall get values from API only. This also applies to parameters on which other parameters depend. If in JDashboard several parameters share values, when any of them is set to get values from API only, they will share the values from API.  Data type: Boolean |
| Hide Parameter When Single Value Returned | When a parameter is bound with a column, you can choose to hide the parameter at runtime when only a single value is returned for the parameter, and the returned single value will be used as default value of the parameter. Data type: Boolean |
| Import SQL | Displays the SQL statement for retrieving values of the bound column and display column for the parameter. You can edit the statement. Data type: String  **Notes**:   * If you have made changes to the SQL statement, the later changes for Bind Column and Display Column of the parameter will not take effect unless you remove the SQL lines or bind the parameter all over again. * The special field User Name can also be used in the SQL statement as *@username*. |
| Maximum Value/Length | Specifies the maximum value allowed for this parameter, or the maximum length for a String type parameter. Data type: String |
| Minimum Value/Length | Specifies the minimum value allowed for this parameter, or the minimum length for a String type parameter. Data type: String |
| Name | Specifies the name of the parameter. Data type: String |
| Object Name | Specifies the name for the OOJDBC class that is related to the parameter. Data type: String |
| Object Parameter Name | Specifies the parameter name for the OOJDBC class. Data type: String |
| Operation | Specifies whether or not to check the minimum and maximum values that you specified for the parameter at runtime. If -1, it will not check; if 1, it will check at runtime. Data type: Integer |
| Prompt Text | Specifies the text for prompting users to provide the value of the parameter. Data type: String  **Tips**:   * To help users avoid typing a value out of range, you can add the value range to the end of the prompt text. For example, "Type a customer ID (1~100):". * To help users avoid typing a value in a wrong pattern, you can add the value pattern to the end of the prompt text. For example, "Type an order date (MMM-dd-yy):". |
| Record Level Security | When a parameter is bound with a column, you can specify a RLS policy defined on the bound column to the parameter, then at runtime the specified security identifier will see the records it is allowed to view in the parameter value drop-down list. See [Applying RLS to parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611482-Parameter-Application-Cases#RLS) for an example. Data type: String |
| Required | Specifies whether or not the parameter will be treated as a required one. A required parameter must be fulfilled, which means that you must provide a value for the parameter before the report can be run. When the property is false, the parameter will be treated as an optional parameter. An optional parameter can be left blank, which means you can either type a value, or leave it as it is. In the dialog for specifying the parameter value, the prompt text of a required parameter will be marked with a \* sign.  Data type: Boolean  **Note**: If the parameter is optional and you do not expect it to take effect in your report, in the UI for specifying the parameter value, clear the content in the value text box. Any value left in the field will function in reports. |
| String Encoding | Specifies the encoding for the parameter when the parameter's data type is String. Data type: String |
| String Format | Specifies the user defined format of the parameter value when the parameter's data type is String. Data type: String |
| Treat Blank as Null | Specifies whether or not to treat blank data value as null when the parameter's data type is String. Data type: Boolean |
| [Use Current Date-Time](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog#CurrentDateTime) | Specifies whether or not to use the current system's date time as value of the parameter when the parameter's data type is Date, Time or DateTime. Data type: Boolean |
| [Use Current Date-Time When Blank](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog#CurrentDateTime) | Specifies whether or not to use the current system's date time as value of the parameter when the parameter's data type is Date, Time or DateTime, and the parameter value is blank. Data type: Boolean |
| [User Defined Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog#UDF) | For certain types of parameters, the value format supplied by Logi Report may not satisfy your requirement. In this case, you can define your own preferred format. When you have defined the value format, all the values supplied for the parameter at runtime should be based on it, otherwise there will be an error message. Data type: String  **Notes**:   * The letters standing for year, month, and so on are case sensitive and should follow the standard of Java java.text.DateFormat, java.text.NumberFormat, and so on. * The user defined format will show different appearance under different locale, and you need to specify values according to the displayed format. For example, under the Spanish or French locale, ####.## will be displayed as #0,## and you should follow #0,## to type in values. * The user defined format only limits the format of the input value, which does not mean that the display value will be in the same format. To change the display format of a parameter, you will need to specify the [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009635661-Parameter-Field-Properties#Format) property of this parameter in the Report Inspector. |
| Value List | Lists values of the parameter. This property is read only. |
| Value Type | Specifies the data type of the parameter. Choose an option from the drop-down list. Data type: Enumeration |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the parameter according to the contents. Data type: Boolean |
| Auto Scale in Number | The property is available when the parameter is of the Number data type. It specifies whether to automatically scale the parameter values that fall into the two ranges:  * When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale values.   The option "auto" means that the property setting follows that of the parent data container when the parameter is added in a report.  Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Type an integer value to change the size. Data type: Integer |
| [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009635341-DBField-Properties#Format) | Specifies the display format of the parameter's value. The format varies with the parameter's data type and can be defined manually. Data type: String |
| Horizontal Alignment | Specifies the horizontal justification of the text in the parameter. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the parameter. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the parameter. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the parameter. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the parameter. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the parameter. Type a numeric value to change the padding. Data type: Float |
| Geometry | |
| Height | Specifies the height of the parameter, which takes effect when the parameter is inserted into a report. Type a numeric value to change the height. The default is 0 which means a proper height will be specified to the parameter by Logi Report automatically. Data type: Float |
| Width | Specifies the width of the parameter, which takes effect when the parameter is inserted into a report. Type a numeric value to change the width. The default is 0 which means a proper width will be specified to the parameter by Logi Report automatically. Data type: Float |
| Color | |
| Background | Specifies the background color of the parameter. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the parameter. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the parameter. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the parameter. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the parameter. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the parameter. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether or not to draw two shadowed borders, beneath and to the right of the parameter. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the parameter. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color with which to draw a pattern to fill the parameter. Choose a color from the drop-down list or select Custom to customize a color. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Pattern Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009635341-DBField-Properties#PatternStyle) | Specifies the style of the pattern. Choose an option from the drop-down list. Data type: Enumeration |
| Others | |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500009611362-Applying-National-Language-Support).  * **<Auto>** - For a parameter bound with a single column or cascading columns, the data mapping file set for the display column is applied; for other parameters, no data mapping file is applied.   For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611702-MongoDB-Element-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634861-Query-Properties)
