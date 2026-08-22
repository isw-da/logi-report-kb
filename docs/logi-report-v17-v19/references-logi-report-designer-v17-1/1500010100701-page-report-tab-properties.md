---
title: "Page Report Tab Properties"
id: 1500010100701
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties
updated_at: 2021-07-23T19:16:38Z
---

# Page Report Tab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062282-Page-Report-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062302-Parameter-Control-Properties)

# Page Report Tab Properties

This topic lists the properties of a Page Report Tab object.

| Property Name | Description |
| --- | --- |
| General | |
| Default Format for Viewing Report | Specifies the default format with which to view the report tab on Server. The default value is to adopt the Server setting. If you select a specific format, you can select the ellipsis button Ellipsis button to further configure the format settings. After this property is configured, it will only control the directly-running result of the report tab on Server, but has no effect on the result of advanced running and schedule running.   * **<Server Setting>** - Adopts the format setting on Server. * **Page Report** - Displays the report tab in Page Report Studio. Select Ellipsis button in the value cell to configure the format settings in the [Page Report Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060062-Page-Report-Option-Dialog-Box). * **HTML** - Displays the report tab in HTML. Select Ellipsis button in the value cell to configure the format settings in the [HTML Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059542-HTML-Option-Dialog-Box). * **PDF** - Displays the report tab in PDF. Select Ellipsis button in the value cell to configure the format settings in the [PDF Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098181-PDF-Option-Dialog-Box). * **Excel** - Displays the report tab in Excel. Select Ellipsis button in the value cell to configure the format settings in the [Excel Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096601-Excel-Option-Dialog-Box). * **Text** - Displays the report tab in Text. Select Ellipsis button in the value cell to configure the format settings in the [Text Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060762-Text-Option-Dialog-Box). * **RTF** - Displays the report tab in RTF. Select Ellipsis button in the value cell to configure the format settings in the [RTF Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098521-RTF-Option-Dialog-Box). * **XML** - Displays the report tab in XML. Select Ellipsis button in the value cell to configure the format settings in the [XML Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060862-XML-Option-Dialog-Box). * **PostScript** - Displays the report tab in PostScript. Select Ellipsis button in the value cell to configure the format settings in the [PostScript Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098261-PostScript-Option-Dialog-Box).   Data type: Enumeration |
| Instance Name | Shows the instance name of the report tab. This property is read only and available for page reports created using query resources. |
| Report Layout Type | Displays the layout type of the report tab. This property is read only and available for page reports created using query resources.  * **Flow Report** - A regular flow layout report. * **Banded Report** - A restricted flow layout report, which is a layout intended for Logi Report Version 7 compatibility only. |
| Result Buffer | |
| [Result Buffer Size](#ResultBuffer) | Specifies the number of report result pages which will be stored in the buffer. Data type: Integer |
| Data (available for page reports created using query resources) | |
| [Automatic Cube Initialization](#ACI) | Specifies whether or not to enable the automatic cube conversion.  * **true** - If true, when opening the report tab in Page Report Studio, all the queries used by the data components in the report tab are converted to appropriate business views automatically for analytic reporting purpose. If the conversion fails due to error or incomplete conditions, no warning message will be shown on UI but the information will be recorded into the log file. * **false** - If false, the conversion of queries to business views will not be performed automatically when opening the report tab in Page Report Studio. Instead, when you are to perform an analytic reporting action like adding a field into a data component, the component's query will be converted to a business view in order for the action to work.   Data type: Boolean |
| Others | |
| After Init Parameter | This property is for the [Exit function](https://devnet.logianalytics.com/hc/en-us/articles/1500010093901-Using-the-Exit-Functions) usage. You can specify an external application file (Java class file) which develops an action. Logi Report calls the action after you specify parameters when running the report tab. This property is available for page report tabs created using query resources. Data type: String |
| After Run | This property is for the [Exit function](https://devnet.logianalytics.com/hc/en-us/articles/1500010093901-Using-the-Exit-Functions) usage. You can specify an external application file (Java class file) which develops an action. Logi Report Engine calls the action immediately after it finishes running the report result. This property is only available for query-based page report tabs.  Data type: String |
| Before Run | This property is for the [Exit function](https://devnet.logianalytics.com/hc/en-us/articles/1500010093901-Using-the-Exit-Functions) usage. You can specify an external application file (Java class file) which develops an action. Logi Report Engine calls the action at the point it is about to run the report tab. This property is only available for query-based page report tabs. Data type: String |
| Click Priority | Specifies the priority of the actions that will be triggered at runtime when you select on certain objects in the report tab which are bound with some actions. Select Ellipsis button in the value cell to set the priority in the [Click Priority dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095721-Click-Priority-Dialog-Box). Data type: String |
| Embedded Fonts | Specifies the True Type Fonts that have been used in the report tab so as to embed them if you want to export the report result to a PDF file. You can select multiple fonts by pressing the Ctrl or Shift key. For more information, see [Delivering TTF Result in PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500010101401-Applying-True-Type-Fonts-in-Reports#DeliverPDF).  Data type: String |
| [Import JavaScript](#ImportJavaScript) | Specifies the name of a JavaScript file you develop to apply customized functions in Page Report Studio, for example, user1.js. This property is available for page reports created using query resources. Your JavaScript file should be located in `<server_install_root>\public_html\javascript\dhtml`.  Data type: String |
| No Temp File | Specifies whether or not to create temporary files.  * **true** - Not to create temporary files. Gains faster engine performance. * **false** - To create temporary files. Gains better accuracy in calculating data.   Data type: Boolean |
| On Parameter Value Change | Specifies to use formulas to validate values of the parameters used by the report tab, then when the parameter values are changed at runtime, the values will be passed to the formulas first for validation. If the values are valid, they will be applied to the parameters; if not, you can make messages returned. Note that when you define the formula, you need to make it return a blank string for valid parameter values. Choose the required formulas from the drop-down list (to select multiple formulas, make user of the Ctrl or Shift keys on the keyboard, after selecting the formulas, select outside of the value cell to confirm). For example, for a string type parameter which requires a value that is of 4-7 characters, you can define a formula like this:  `if(length(@P_String) > 8 ) "The value is too long."  else if (length(@P_String) < 3 ) "The value is too short."   else ""`  Then, when a string value of 9 characters is specified to the parameter, you will be prompted with the "The value is too long." message.  Data type: Object Array |
| Page Background | Specifies the background color of the report page. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Precision Sensitive | Specifies whether to enable [customized precision settings](https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result#Precision) in the report result when exporting the report tab to different formats. If you do not care the report visual effect, leave the value of the property to be false as default and let Logi Report deal with the precision. Logi Report has better performance when precision insensitive than when sensitive. When the property is set to true, customized precision level for different export formats will be applied for exporting the report tab. This property is available for page reports created using query resources. Data type: Boolean |
| Show Subreport Header Footer | Specifies whether or not to show the page header and footer panels of subreports in the report tab.  * **true** - The page header and page footer panels of subreports in the report tab will be displayed when the panels are set to be visible in the subreports. * **false** - The page header and page footer panels of subreports in the report tab will not be displayed.   Data type: Boolean |
| Style Group | Specifies the style group for the report tab. When the report tab is used as a subreport, choosing any style group from the drop-down list turns on the Style Group feature for the report tab and it will inherit the style group of the primary report; choosing None or leaving this property empty turns off the Style Group feature for the report tab and it will not inherit style group from the primary report.  When the report tab is used as a linked report, if the option "Pass style group information down to linked report" is selected when defining the link condition, it will inherit the style group of the primary report; if unselected, it will take the style group specifed by the property.  Data type: String |
| Suppress Object Space If Not Exported | Specifies whether to suppress the space used for holding the objects in the exported report result when you have specified not to include them for exporting. Data type: Boolean |
| Excel | |
| Column Width List | Specifies the width of columns beginning from the first column for the exported Excel sheet. If you don't want to specify the width for a certain column, omit the value. Logi Report will then use the default value (8) for the column. This property is available for page reports created using query resources. Use semicolon (;) to separate each width, for example: 12;8;15;10;9  The example specifies the width of the first 5 columns. For the other columns, they take the default width of Microsoft Excel sheet.  8 indicates the default column width in Microsoft Excel sheet. It can be omitted. The above example can also be written as 12;;15;10;9  Data type: String  Note icon   * The Column Width List property takes effect only when you have set the report tab's [Columned](#Column) property to true and selected the Column Format option in the Export to Excel dialog box. * If the report tab contains a subreport, Designer disables the Column Width List property for the subreport when you export the report tab to Excel. |
| [Columned](#Columned) | If true, the engine performance will be improved when exporting the report tab to CSV and Excel. Only after the Columned property is set to true, it is meaningful to specify values to the following Excel properties of objects in the report tab, otherwise the specified values for these Excel properties cannot take effect.   * Column Index/Row Index * Column Number/Row Number. The properties are for chart platforms, images and UDOs. * Top Attach Column/Top Attach Row/Bottom Attach Column/Bottom Attach Row. The properties are for drawing objects.   Data type: Boolean |
| [Excel Buffer Size](#ExcelBuffer) | Specifies the number of report result sheets which will be stored in the buffer when exporting the report tab to Excel. This property is available for page reports created using query resources. Data type: Integer |
| Fast Pass | If true, the engine performance will be improved when running the report tab to CSV format in multiple threads on Server. This property is available for page reports created using query resources. To make fast pass work, the property Columned should be true.  Data type: Boolean |
| No Page Break | If true, there will be no page breaks on each individual sheet when exporting the report tab to Excel with the option Column Format selected in the Export to Excel dialog box. This means the column headings will appear just at the top of the Excel spreadsheet and will not be repeated throughout the report. If the report breaks to a new sheet then once again the page header will display. Data type: Boolean  Critical icon Exporting a report tab to an Excel file without page breaks means the split pages are technically merged within the Excel sheet, which could bring the following results and limitations:   * In the Excel output, only one page header panel and one page footer panel in a banded object will be displayed in each sheet. Only the first banded page header and the last banded page footer will be displayed in the exported result. As for tables, only the first table header and the last table footer will be exported. * You cannot get a continuous table or banded object if the report has other objects in horizontal locations. All split parts of a horizontal table will be exported vertically. * Merging tables or crosstabs together will extend the Excel sheet, which may cover other objects if they happen to be in the extended direction. When merging crosstabs together, the column/row index might be extended over the Excel sheet range, and the report part which is out of this range will get lost in the result file. * If a whole merged crosstab gets quite large, it might cause an out of memory error during the exporting process. |
| Rows per Sheet | Specifies the maximum number of rows for every worksheet when exporting the report tab to Excel. This property is available for page reports created using query resources. For the Excel version Excel 97-2003 Workbook (\*.xls), the value ranges from 0 to 65000. Any value out of the range will be considered as 65000. For the Excel version Excel Workbook (\*.xlsx), the value ranges from 0 to 1048000. Any value out of the range will be considered as 1048000.  When exporting a report to Excel, rows in the same page of the report cannot be separated and exported to different worksheets, thus the number of rows that is exported to a worksheet may be greater than the maximum number of rows that you set for the property Rows per Sheet. For example, if you set the value of Rows per Sheet to 100, all the contents of the first page will be exported to the first worksheet. After that, the rows of the first worksheet will be tested automatically by Designer. If the number of rows is less than 100, the Next Topic will still be exported to the first worksheet, even if the number of rows in the first page and the Next Topic is greater than 100; If the number of rows in the first page is equal to or more than 100, a new worksheet will be generated and the second page will be exported to the new worksheet.  Data type: Integer |
| Sheet Name | Specifies the sheet name for the report tab in the report's Excel output. If the report tab is split into several sheets in the Excel output because of limited rows per sheet, a postfix number will be added to the sheets starting from the second one (SheetName, SheetName1, SheetName2, SheetName3...). This property is available for page reports created using query resources. Data type: String  Note icon Excel does not support using the following characters in the sheet name: "|", ":", "/", "?", "\", "\*", "]", "[", and the single quotation mark (') as the last character in the sheet name. If you use any one of them in the value of the property, Excel replaces it by "\_". |
| [Style Group for Export](#Export) (available for page reports created using query resources) | |
| Excel Style Group | Pre-sets the style group for the Excel output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| Fax Style Group | Pre-sets the style group for the fax output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| HTML Style Group | Pre-sets the style group for the HTML output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| Page Report Style Group | Pre-sets the style group for running the report tab in Page Report Studio. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| PDF Style Group | Pre-sets the style group for the PDF output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| PS Style Group | Pre-sets the style group for the PostScript output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| RST Style Group | Pre-sets the style group for the RST output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| RTF Style Group | Pre-sets the style group for the RTF output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| Text Style Group | Pre-sets the style group for the Text output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| XML Style Group | Pre-sets the style group for the XML output of the report tab. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |

## Automatic Cube Initialization

In order for a query-based report component created in Designer, such as table, crosstab, chart, and banded object, to be able to perform analytic reporting actions on when you work with them in Page Report Studio, Logi Report needs to convert the component from query-based to business view-based.

**When the conversion is required**

The conversion is required when Page Report Studio end user is trying to perform an analytic reporting action such as drilling through data on a table, crosstab, chart, or banded object which is created based on a query.

When the property Automatic Cube Initialization is set to true, Logi Report will automatically convert the queries a report tab uses to business views when opening the report tab in Page Report Studio.

**What makes the conversion successful**

The success of the conversion lies in the following aspects:

* There should be a business view using only the query that a report component uses as the data resource.
* All the fields in the report component have corresponding elements in the business view. For the mapping relationship, see the section [How to convert](#How).
* The cases illustrated in [What cannot be converted](#cannot) should be avoided.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) The report designer can create a complete and full-function business view for the required query, in this way, all fields in the query are able to be converted since there are always corresponding view elements found in the complete business view. To create such a complete business view, create a group and a detail element for each DBField and formula, and create an aggregation for each summary.

**How to convert**

The following lists what types of fields in the query will be converted to what types of elements in the business view:

| When a query field is used as | It will be converted to |
| --- | --- |
| Group by field, crosstab column/row field, chart category/series field | Group element |
| Crosstab summaries | Aggregation element |
| Show Value in chart and is a summary | Aggregation element |
| Show Value in chart and is of Number type | Detail element |
| Static summary in the current or child group level, that is, the group by field of the static summary is the same as the one used for the current group level or an ancestor group level | Aggregation element |
| Others and there is corresponding detail element in the business view | Detail element |
| Others and there isn't corresponding detail element in the business view | Group element |

**What cannot be converted**

The following list shows the cases in a query-based component that do not support conversion. The list supposes that all the involved query fields have their corresponding view elements in the business view based on the query:

* Static summary (except that used as Show Value of chart or in the current or child group level).
* Dynamic summary (except when the summary's group-by level is 0).
* Formula that references summaries.
* Page level formula, that is, the formula calculated after the whole report finishes rendering.
* DBField or formula used as group-by field but the group has a special function.
* Parameter used as group-by field.
* Chart in a banded object that uses inherited dataset.
* Table, crosstab, or banded object whose dataset is inherited.
* Table, crosstab, chart, or banded object when one of its children components cannot be converted (the children components exclude blank components and those having already been converted).

## Result Buffer Size

The result buffer is used to store the result of one report in pages. Its default size 4 indicates 4 pages of the report result have been allocated to the result buffer. The other pages will be stored on disk. If you have enough memory, you can increase the result buffer size to store more pages of the report result. By doing this, you will achieve better performance.

## Import JavaScript

If you want to develop functions in your own JS file, you can use this property to support the control objects when viewing reports in Page Report Studio. Your own JS file should be located in `<server_install_root>\public_html\javascript\dhtml`, and it will work together with the API.js file in the same folder, but with a higher priority if both of them contain the same functions.

To use this property, simply set the property value to the name of your JS file.

For example, you have a JavaScript file named "user1.js" which contains the following function:

```
function promptMessage(message)  
    {  
    alert(message);  
    }  
window.promptMessage("test")
```

In this example, set the property to "user1.js" in order to apply functions defined in the file.

## Excel Buffer Size

The Excel buffer is used to store the report result in Excel buffer sheets when exporting the result in Excel. Its default size is 1, which indicates 1 sheet of the report result is allocated to the result buffer. The other sheets will be stored on disk. If you have enough memory, you can increase the Excel buffer size to store more sheets of the Excel output. By doing this, you will achieve better performance.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) The Excel Buffer Size property takes effect only when the Data Format option in the Export to Excel dialog box is not selected.

## Columned

Right after you set the property to true from false each time, Logi Report Engine recalculates the values of the following Excel properties of all objects in the report tab and reset the values to the defaults.

* Column Index/Row Index
* Column Number/Row Number. The properties are for chart platforms, images and UDOs.
* Top Attach Column/Top Attach Row/Bottom Attach Column/Bottom Attach Row. The properties are for drawing objects.

The default values are calculated based on the position of each object in the report tab. There is an exception: if both the Export to Excel and Export to CSV properties of an object are false, the values of these properties will not be recalculated and will be preserved as before.

The property controls two things when it is true:

* Use the columned method to export the report to Excel when the option Column Format in the corresponding export dialog box is selected.
* You can specify values for the Excel properties mentioned above of an object instead of using the default, so that they can be well-aligned in the Excel output. However if the Position property of an object is static, its Column Index and Row Index properties will not take affect when the report tab is exported to Excel.

When the property is false:

* The specified values for the above Excel properties of objects in the report tab are not applied when exporting to CSV or Excel.

## Style Group for Export

This is to pre-set a style group to the report tab for each export format. The style group specified for export formats has higher priority than that specified for the [Style Group](#StyleGroup) property. However, if you do not specify a style group for an export format, when you export the report to the format, it will take the value specified for the Style Group property by default.

The specified export style group applies in the following cases: when export or preview the report in Designer, export the report in Page Report Studio, and when run/advanced run the report or schedule to publish it to version/disk/e-mail/FTP on Server.

When viewing a report tab by selecting the View tab in Designer, the value specified for the Style Group property is selected by default in the Select Style Group dialog box but you can choose another style group to use in the dialog box. In the view mode, if you further preview the view result in different formats or export it to different formats, the preview/export result will take the style group of the view result, and the Style Group for Export property will not take effect.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062282-Page-Report-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062302-Parameter-Control-Properties)
