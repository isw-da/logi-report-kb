---
title: "Parameter Properties"
id: 4405664635159
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664635159-Parameter-Properties
updated_at: 2022-01-27T20:36:17Z
---

# Parameter Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664633367-MongoDB-Element-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664637207-Query-Properties)

# Parameter Properties

This topic describes the properties of a [Parameter object](https://devnet.logianalytics.com/hc/en-us/articles/4405661800215-Working-with-Parameters) in a catalog.

| Property Name | Description |
| --- | --- |
| General | |
| Allow Showing Unencrypted Value | Specifies whether to display the "Hide Parameter Value" option in the UI for specifying the parameter value to allow users to view the unencrypted values of the parameter after the values are encrypted. Data type: Boolean |
| Bind Column | Specifies the bind column of the parameter. Data type: String |
| Binding | Specifies the parameter to bind with the current parameter to sort the column controlled by the current parameter. Data type: String |
| Default Value Number | Specifies the default parameter value you want to prompt to users. Set the property value to 0 when you want to prompt the first parameter value that you specify for the parameter; set the property value to -1 to prompt the last parameter value. Data type: Integer |
| Description | Specifies the description of the object. Data type: String |
| Display Column | Specifies the display column of the parameter. Data type: String |
| Display Width | Specifies the display width of the object, which takes effect when you insert the object into reports. Type a numeric value to change the width. If you do not set the display width, Designer applies a default width to it automatically. Data type: Float  Note icon After you set the Display Width property of an object and use the object while creating a data component with wizard, Designer may adjust its width according to the paper size. |
| Distinct | Specifies whether to display identical values only once in the UI for specifying the parameter value. Data type: Boolean |
| Encrypt Parameter Value | Specifies whether to encrypt values of the parameter in the UI where the parameter is used or required (excluding parameter control and parameter form control) and in log files. However, when you bind the parameter with a column or set its [Allow Multiple Values](https://devnet.logianalytics.com/hc/en-us/articles/4405664612887-Creating-Parameters-in-a-Catalog#AllowMultipleValues) property to "true", Logi Report Engine only encrypts its values in log files. Note icon When writing the value of a formula or string that references an encrypted parameter to log, Logi Report Engine may not encrypt the parameter value.  Data type: Boolean |
| Get Value from API Only | Specifies whether the parameter values can only be specified using API. When this property is "true", users should obtain parameter values only from API and there is no parameter dialog box available in any Designer or Server UI for inputting values. Users need to provide values of the parameter by API such as URLs, coding, and sessions; otherwise, Logi Report Engine applies the default value of the parameter.  When this property is "false", the parameter values can be obtained from both GUI and API.  When a member of a cascading parameter group can get values from API only, it means that all the higher level members shall get values from API only. This also applies to parameters on which other parameters depend. When several parameters share values in JDashboard, if any of them can get values from API only, they will share the values from API.  Data type: Boolean |
| Hide Parameter When Single Value Returned | Specifies whether to hide the parameter when only a single value is returned to it. When you bind a parameter with a column, you can specify to hide the parameter if only a single value is returned to it at runtime. Logi Report Engine then applies the returned single value as the default value of the parameter. This can be very useful for security. For example, you can use a parameter bound with a DBField such as UserID and if there is one to one mapping of UserID to the Server users, then a query for a parameter such as *Select UserID FROM Employees WHERE UserID = @username* would just return a single value and thus you can use it as a filter for any other queries you create.  Data type: Boolean |
| Import SQL | Specifies the SQL statement for retrieving values of the bound column and display column for the parameter. You can use the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields#UserName)" in the SQL statement as *@username*. Data type: String  Note icon Once you edit the SQL statement, the later changes to the Bind Column and Display Column properties cannot take effect unless you remove the SQL lines or bind column to the parameter all over again using dialog box. |
| Maximum Value/Length | Specifies the maximum value allowed for the parameter, or the maximum length for a String type parameter. Data type: String |
| Minimum Value/Length | Specifies the minimum value allowed for the parameter, or the minimum length for a String type parameter. Data type: String |
| Name | Specifies the mapped name of the object in the catalog. Data type: String |
| Object Name | Specifies the name of the OOJDBC class related to the parameter. Data type: String |
| Object Parameter Name | Specifies the parameter name for the OOJDBC class. Data type: String |
| Operation | Specifies whether to check the minimum and maximum values users provide to the parameter. If you want to perform the check, set the property value to -1; otherwise, set it to 1. Data type: Integer |
| Prompt Text | Specifies the text for prompting users to provide value for the parameter. To help users avoid typing a value out of range, you can add the value range to the end of the prompt text, for example, "Type a customer ID (1~100):"; to help users avoid typing a value in a wrong pattern, you can add the value pattern to the end of the prompt text, for example, "Type an order date (MMM-dd-yy):". |
| Record Level Security | Specifies the record level security to apply to the parameter. If you bind a parameter with a column, you can specify a RLS policy defined on the bound column to the parameter, then at runtime, the specified security identifier only sees the records it is allowed to view in the parameter value drop-down list. See [Applying RLS to a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/4405661801239-Parameter-Application-Cases#RLS) for an example.  Data type: String |
| Required | Specifies whether the parameter is a required parameter. A required parameter must be fulfilled, meaning, users must supply a value to the parameter before they can run the report. If you set the option to "false", the parameter is an optional parameter. The value of an optional parameter can be blank, which means users can either type a value, or leave it as it is. In the dialog box for specifying the parameter value, Logi Report marks the prompt text of a required parameter with the "\*" symbol.  Data type: Boolean  Critical icon If a parameter is optional and you do not expect it to take effect in the report, when specifying the parameter value, you should clear the content in the value text box. Any value left in the text box functions in the report. |
| String Encoding | Specifies the encoding for values of the parameter when the parameter is String data type. Data type: String |
| String Format | Specifies the user-defined format for values of the parameter when the parameter is String data type. Data type: String |
| Treat Blank as Null | Specifies whether to treat blank value as null for the parameter when the parameter is String data type. Data type: Boolean |
| [Use Current Date-Time](https://devnet.logianalytics.com/hc/en-us/articles/4405664612887-Creating-Parameters-in-a-Catalog#CurrentDateTime) | Specifies whether to use the current system's date time as value of the parameter when the parameter is Date, Time, or DateTime data type. Data type: Boolean |
| [Use Current Date-Time When Blank](https://devnet.logianalytics.com/hc/en-us/articles/4405664612887-Creating-Parameters-in-a-Catalog#CurrentDateTime) | Specifies whether to use the current system's date time as value of the parameter when the parameter is Date, Time, or DateTime data type, and the parameter value is blank. Data type: Boolean |
| [User Defined Format](https://devnet.logianalytics.com/hc/en-us/articles/4405664612887-Creating-Parameters-in-a-Catalog#UDF) | Specifies the user-defined format for values of the parameter. For certain types of parameters, the value format Logi Report provides may not satisfy your requirement. In this case, you can define your own preferred format. Once you define the value format, any value supplied to the parameter should be in accordance with this format; otherwise, there is an error message.  Data type: String |
| Value List | Shows values of the parameter. This property is read only. |
| Value Type | Specifies the data type of the parameter. Choose an option from the drop-down list. Data type: Enumeration |
| Text Format | |
| Auto Fit | Specifies whether to automatically adjust the width and height of the object according to its content. Data type: Boolean |
| Auto Scale in Number | Designer displays this property when the object is Number data type. You can use it to specify whether to automatically scale values of the object that fall into the two ranges:  * When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12). * When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.   The option "auto" means that the property setting follows that of the parent data component when you use the object in a report.  Data type: Boolean |
| Bold | Specifies whether to apply bold formatting to the text in the object. Data type: Boolean |
| Font Face | Specifies the font face of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text in the object. Type an integer value to change the size. Data type: Integer |
| Format | Specifies the format in which you want to display values of the object in the report. Choose an option from the drop-down list or type the format by yourself. Data type: String  Note icon If the object is BigDecimal data type, to avoid precision loss, you should specify a prefix JRD when setting the format. |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to italicize the text in the object. Data type: Boolean |
| Strikethrough | Specifies whether to draw a line through the text in the object. Data type: Boolean |
| Underline | Specifies whether to add a horizontal line under the text in the object. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text according to the width of the object. Data type: Boolean |
| Padding | |
| Bottom Padding | Specifies the space between the content in the object and the bottom border of the object. Type a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the content in the object and the left border of the object. Type a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the content in the object and the right border of the object. Type a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the content in the object and the top border of the object. Type a numeric value to change the padding. Data type: Float |
| Geometry | |
| Height | Specifies the height of the object, which takes effect when you insert the object into reports. If you do not set the height, Designer assigns a proper height to the object automatically. Data type: Float |
| Width | Specifies the width of the object, which takes effect when you insert the object into reports. If you do not set the width, Designer assigns a proper width to the object automatically. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color for the border of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style for the bottom border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style for the left border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style for the right border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to add a drop shadow effect to the border. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style for the top border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** Select if you do not want to apply a pattern to the object. * **50%** Select to fill the object using 50%-transparency of the specified pattern color. * **horizontal** Select to fill the object with horizontal lines using the specified pattern color. * **vertical** Select to fill the object with vertical lines using the specified pattern color. * **grid** Select to fill the object with grids using the specified pattern color. * **diagonal** Select to fill the object with diagonal lines using the specified pattern color.   Data type: String |
| Others | |
| Data Mapping File | Specifies the data mapping file to apply to the parameter [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/4405661798039-Mapping-Data-Values-to-Different-Languages).  * **<Auto>** - When you select this option, if the parameter is bound with a single column or cascading columns, Logi Report Engine applies the data mapping file that you specify for its display column to the parameter; otherwise, it applies no data mapping file to the parameter.   For example, if the data mapping file name is Category\_de\_DE.properties, set the value as "Category" (without the locale part).  Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664633367-MongoDB-Element-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664637207-Query-Properties)
