---
title: "Parameter Properties"
id: 1500009568922
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568922-Parameter-Properties
updated_at: 2021-07-24T05:54:24Z
---

# Parameter Properties

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590481-MongoDB-Element-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568942-Query-Properties)

# Parameter Properties

The properties of a parameter are as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Bind Column | Specifies the bind column of the parameter. Data type: String |
| Binding | Specifies the parameter which will be bound with the current one to sort the column controlled by the current parameter. Data type: String |
| Default Value Number | Specifies the parameter value that will be prompted by default at runtime. If it is set to 0, the first parameter value in the Value property will be prompted; if it is set to -1, the last parameter value in the Value property will be prompted. Data type: Integer |
| Description | Specifies the description of the parameter. Data type: String |
| Display Column | Specifies the display column of the parameter. Data type: String |
| Display Width | Specifies the display width of the parameter. Enter a numeric value to change the width. Data type: Float  **Notes:**   * If the Display Width value of a parameter is not set in the Catalog Manager, the parameter will be inserted in a report with the default width defined by Logi JReport. * Assume that you have set the Display Width of a parameter, and used the parameter while creating a new component with the report wizard, its width may be adjusted according to the paper size. |
| Distinct | Specifies whether or not the text of the parameter is to be distinct. Data type: Boolean |
| Get Value from API Only | Specifies whether the parameter values can be input via GUI or not. If true, the parameter values should only be obtained from API. If false, the parameter can be obtained from both GUI and API. Data type: Boolean |
| Hide Parameter When Single Value Returned | When a parameter is bound with a column, you can choose to hide the parameter at runtime when only a single value is returned for the parameter, and the returned single value will be used as default value of the parameter. Data type: Boolean |
| Import SQL | Specifies the statement of the imported SQL file, which is created manually. Data type: String |
| Maximum Value/Length | Specifies the maximum value allowed for this parameter, or the maximum length for a String type parameter. Data type: String |
| Minimum Value/Length | Specifies the minimum value allowed for this parameter, or the minimum length for a String type parameter. Data type: String |
| Name | Specifies the name of the parameter. Data type: String |
| Object Name | Specifies the name for the OOJDBC class that is related to the parameter. Data type: String |
| Object Parameter Name | Specifies the parameter name for the OOJDBC class. Data type: String |
| Operation | Specifies whether or not to check the minimum and maximum values that you specified for the parameter at runtime. If -1, it will not check; if 1, it will check at runtime. Data type: Integer |
| Prompt Text | Specifies the prompt text of the parameter, which is used for prompting users to provide the value of the parameter. Data type: String |
| Record Level Security | When a parameter is bound with a column, you can specify a RLS policy defined on the bind column in the data source to the parameter, then at runtime, the specified security identifier will see the records it is allowed to view in the parameter value drop-down list (to specify the security identifier, go to **File** > **Options** on the menu bar, in the General category of the Options dialog, specify the security identifier by the User Name option). Data type: String |
| Required | Specifies whether or not the parameter will be treated as a required one. Data type: Boolean |
| String Encoding | Specifies the encoding for the parameter. This property is available only when the parameter's data type is String. Data type: String |
| String Format | Specifies the user-defined format of the parameter value. This property works only when the parameter's data type is String. Data type: String |
| Treat Blank as Null | Specifies whether or not to treat blank data value as null when the parameter's data type is String. Data type: Boolean |
| Use Current Date-Time | Specifies whether or not to use the current system's date time as value of the parameter when the parameter's data type is Date, Time or DateTime. Data type: Boolean |
| Use Current Date-Time When Blank | Specifies whether or not to use the current system's date time as value of the parameter when the parameter's data type is Date, Time or DateTime, and the parameter value is blank. Data type: Boolean |
| [User Defined Format](#Format) | Specifies the user-defined format of the parameter value. Data type: String |
| Value List | Lists values of the parameter. This property is read only. |
| Value Type | Specifies the data type of the parameter. Choose an option from the drop-down list. Data type: Enumeration |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the parameter according to the contents. Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| Format | Specifies the display format of the parameter's value. The format varies with the parameter's data type and can be defined manually. Data type: String |
| Horizontal Alignment | Specifies the horizontal justification of the text in the parameter. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the parameter. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the parameter. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the parameter. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the parameter. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the parameter. Enter a numeric value to change the padding. Data type: Float |
| Geometry | |
| Height | Specifies the height of the parameter, which takes effect when the parameter is inserted into a report. Enter a numeric value to change the height. The default is 0 which means a proper height will be specified to the parameter by Logi JReport automatically. Data type: Float |
| Width | Specifies the width of the parameter, which takes effect when the parameter is inserted into a report. Enter a numeric value to change the width. The default is 0 which means a proper width will be specified to the parameter by Logi JReport automatically. Data type: Float |
| Color | |
| Background | Specifies the background color of the parameter. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the parameter. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border | |
| Border Color | Specifies the color of the border of the parameter. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the parameter. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the parameter. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the parameter. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether or not to draw two shadowed borders, beneath and to the right of the parameter. Data type: Boolean |
| Shadow Color | Specifies the color of the border shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the parameter. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color with which to draw a pattern to fill the parameter. Choose a color from the drop-down list or select Custom to customize a color. You can also enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** - No pattern will be applied to the parameter. * **50%** - The parameter will be filled in the specified color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the specified color. * **vertical** - The pattern will be made of vertical lines of the specified color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the specified color. * **diagonal** - The pattern will be made of slash lines of the specified color.   Data type: Enumeration |
| Others | |
| Data Mapping File | Specifies the data mapping file to the object [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500009589921-Applying-National-Language-Support).  * **<Auto>** - For a parameter bound with a single column or cascading columns, the data mapping file set for the display column is applied; for other parameters, no data mapping file is applied.   For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |

## User Defined Format

For example, you define a parameter of Date type and the following formats can be recognized: M/d/yy; MMM d, yyyy; MMMM d, yyyy; EEEE, MMMM d, yyyy. But if you want to enter a value like 1996.July.10, you should specify the user defined format as yyyy.MMMM.d. But remember it is the entering format, not the display format. To customize the display format, go to its [Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009591721-Properties-of-Parameter-Field-in-Page-Report#Format) property in Report Inspector, enter your customized display format as yyyy.MMMM.d. Then when you enter 1996.July.10, it will be displayed as 1996.July.10.

For details about how to define a user format for different types of parameters, refer to [User Defined Format for Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590281-User-Defined-Format-for-Parameters).

**Note:** The letters standing for year, month, and so on are case sensitive and should follow the standard of Java java.text.DateFormat, java.text.NumberFormat, and so on.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590481-MongoDB-Element-Properties)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568942-Query-Properties)
