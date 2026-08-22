---
title: "Properties of Page Report Tab"
id: 1500009591741
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab
updated_at: 2021-07-24T05:54:06Z
---

# Properties of Page Report Tab

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591701-Properties-of-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569782-Properties-of-Parameter-Control-in-Page-Report)

# Properties of Page Report Tab

The properties of a page report tab object are:

| Property Name | Description |
| --- | --- |
| General | |
| Default Format for Viewing Report | Specifies the default format with which to view the report tab on Logi JReport Server. The default value is to adopt the Logi JReport Server setting. If you select a specific format, you can select the button  beside to further configure the format settings. After this property is configured, it will only control the directly-running results of the report tab on Logi JReport Server, but has no effect on the results of advanced running and scheduled running.   * **<Server Setting>**  Adopts the format setting on Logi JReport Server. * **Page Report**  Specifies to display the report tab in Page Report Studio. Select  in the value cell to configure the format settings in the [Page Report Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009567022-Page-Report-Option-Dialog) dialog. * **HTML**  Specifies to display the report tab in HTML format. Select  in the value cell to configure the format settings in the [HTML Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009566362-HTML-Option-Dialog) dialog. * **PDF**  Specifies to display the report tab in PDF format. Select  in the value cell to configure the format settings in the [PDF Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009567002-PDF-Option-Dialog) dialog. * **Excel**  Specifies to display the report tab in Excel format. Select  in the value cell to configure the format settings in the [Excel Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009565462-Excel-Option-Dialog) dialog. * **Text**  Specifies to display the report tab in Text format. Select  in the value cell to configure the format settings in the [Text Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009589161-Text-Option-Dialog) dialog. * **RTF**  Specifies to display the report tab in RTF format. Select  in the value cell to configure the format settings in the [RTF Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009588481-RTF-Option-Dialog) dialog. * **XML**  Specifies to display the report tab in XML format. Select  in the value cell to configure the format settings in the [XML Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009567982-XML-Option-Dialog) dialog. * **PostScript**  Specifies to display the report tab in PostScript format. Select  in the value cell to configure the format settings in the [PostScript Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009588281-PostScript-Option-Dialog) dialog. * **Applet**  Specifies to display the report tab in Applet format. Select  in the value cell to configure the format settings in the [Applet Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009585681-Applet-Option-Dialog) dialog.   Data type: Enumeration |
| Instance Name | Shows the instance name of the report tab. This property is read only. |
| Report Layout Type | Displays the layout type of the report tab. This property is read only.  * **Flow Report** - A regular flow layout report. * **Banded Report** - A restricted flow layout report, which is a layout intended for Logi JReport Version 7 compatibility only. |
| Result Buffer | |
| [Result Buffer Size](#ResultBuffer) | Specifies the number of report results pages which will be stored in the buffer. Data type: Integer |
| Data | |
| [Automatic Cube Initialization](#ACI) | Specifies whether or not to enable the automatic cube conversion.  * **true** - If true, when opening the report tab in Page Report Studio, all the queries used by the data components in the report tab are converted to appropriate business views automatically for analytic reporting purpose. If the conversion fails due to error or incomplete conditions, no warning message will be shown on UI but the information will be recorded into the log file. * **false** - If false, the conversion of queries to business views will not be performed automatically when opening the report tab in Page Report Studio. Instead, when you are to perform an analytic reporting action like adding a field into a data component, the component's query will be converted to a business view in order for the action to work.   Data type: Boolean |
| Others | |
| [After Init Parameter](#callback_exit) | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called after you enter parameters in the pop-up parameter dialog when running the report tab. Data type: String |
| [After Run](#callback_exit) | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called immediately after Logi JReport Engine has finished running the report result. Data type: String |
| [Applet Height](#AppletSetting) | Specifies the applet height for running an exported applet in a web browser. Data type: Float |
| [Applet Width](#AppletSetting) | Specifies the applet width for running an exported applet in a web browser. Data type: Float |
| [Before Run](#callback_exit) | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called at the point Logi JReport Engine is about to run the report tab. Data type: String |
| Select Priority | Specifies the priority of the actions that will be triggered at runtime when you select on certain objects in the report tab which are bound with some actions. Select  in the value cell to set the priority in the [Select Priority](https://devnet.logianalytics.com/hc/en-us/articles/1500009585861-Select-Priority-Dialog) dialog. Data type: String |
| Embedded Fonts | Specifies the True Type Fonts that have been used in the report tab so as to embed them if you want to export the report results to a PDF file. You can select multiple fonts by pressing the Ctrl or Shift key. For more information, refer to [Delivering the Result in PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500009583001-True-Type-Fonts#DeliverPDF).  Data type: String |
| [Import JavaScript](#ImportJavaScript) | Specifies the name of a JavaScript file you develop to apply customized functions in Page Report Studio, for example, user1.js. Your JavaScript file should be located in `<server_install_root>\public_html\javascript\dhtml`.  Data type: String |
| No Temp File | Specifies whether or not to create temporary files.  * **true** - Not to create temporary files. Gains faster engine performance. * **false** - To create temporary files. Gains better accuracy in calculating data.   Data type: Boolean |
| On Parameter Value Change | Specifies to use formulas to validate values of the parameters used by the report tab, then when the parameter values are changed at runtime, the values will be passed to the formulas first for validation. If the values are valid, they will be applied to the parameters; if not, you can make messages returned. Note that when you define the formula, you need to make it return a blank string for valid parameter values. Choose the required formulas from the drop-down list (to select multiple formulas, make user of the Ctrl or Shift keys on the keyboard, after selecting the formulas, select outside of the value cell to confirm). For example, for a string type parameter which requires a value that is of 4-7 characters, you can define a formula like this:  `if(length(@P_String) > 8 ) "The value is too long."  else if (length(@P_String) < 3 ) "The value is too short."   else ""`  Then, when a string value of 9 characters is specified to the parameter, you will be prompted with the "The value is too long." message.  Data type: Object Array |
| Page Background | Specifies the background color of the report page. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Precision Sensitive | Specifies whether to enable [customized precision settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009589221-Exporting-Report-Results#Precision) in the report results when exporting the report tab to different formats. If you do not care the report visual effect, leave the value of the property to be false as default and let Logi JReport deal with the precision. Logi JReport has better performance when precision insensitive than when sensitive. When the property is set to true, customized precision level for different export formats will be applied for exporting the report tab. Data type: Boolean |
| Show Subreport Header Footer | Specifies whether or not to show the page header and footer panels of subreports in the report tab.  * **true** - The page header and page footer panels of subreports in the report tab will be displayed when the panels are set to be visible in the subreports. * **false** - The page header and page footer panels of subreports in the report tab will not be displayed.   Data type: Boolean |
| Style Group | Specifies the style group for the report tab. If the report tab is to be used as a subreport, choosing any style group from the drop-down list to turn on the style group feature for the report tab and it will inherit the style group of the primary report; choosing None or leaving this property empty to turn off the style group feature for the report tab and it will not inherit style group from the primary report.  If the report tab is to be used as a linked report, if the option "Pass style group information down to linked report" is check when defining the link condition, the linked report will inherit the style group of the primary report, if not checked, the linked report will take the style group specifed by the property.  Data type: String |
| Suppress Object Space If Not Exported | Specifies whether to suppress the space used for holding the object in the exported report result when you have specified not to include it for exporting. Data type: Boolean |
| Excel | |
| Column Width List | Specifies the width of columns beginning from the first column for the exported Excel sheet. The Columned property must be set to true for this property to take effect. Use semicolon (;) to separate each width, for example: 12;8;15;10;9  The example specifies the width of the first 5 columns. For the other columns, they take the default width of Microsoft Excel sheet.  8 indicates the default column width in Microsoft Excel sheet. It can be omitted. The above example can also be written as 12;;15;10;9  Data type: String |
| [Columned](#Columned) | If true, the engine performance will be improved when exporting the report tab to CSV or Excel format. Only after the Columned property is set to true, it is meaningful to specify values to the following Excel properties of objects in the report tab, otherwise the specified values for these Excel properties cannot take effect.   * Column Index/Row Index * Column Number/Row Number. The properties are for chart platforms, images and UDOs. * Top Attach Column/Top Attach Row/Bottom Attach Column/Bottom Attach Row. The properties are for drawing objects.   Data type: Boolean |
| [Excel Buffer Size](#ExcelBuffer) | Specifies the number of report results sheets which will be stored in the buffer when exporting the report tab to Excel. Data type: Integer |
| Fast Pass | If true, the engine performance will be improved when running the report tab to CSV format in multiple threads on Logi JReport Server. To make fast pass work, the property Columned should be true.  Data type: Boolean |
| No Page Break | If true, there will be no page breaks on each individual sheet when exporting the report tab to Excel with the option Column Format selected in the Export to Excel dialog. This means the column headings will appear just at the top of the Excel spreadsheet and will not be repeated throughout the report. If the report breaks to a new sheet then once again the page header will display. Data type: Boolean  **Note:** Exporting a report tab to an Excel file without page breaks means the split pages are technically merged within the Excel sheet, which could bring the following results and limitations:   * In the exported Excel format file, only one page header panel and one page footer panel in the banded object will be displayed in each sheet. Only the first banded page header and the last banded page footer will be displayed in the exported result. As for tables, only the first table header and the last table footer will be exported. * You cannot get a continuous table or banded object if the report has other objects in horizontal locations. All split parts of the horizontal table will be exported vertically. * Merging tables or crosstabs together will extend the Excel sheet, which may cover other objects if they happen to be in the extended direction. When merging crosstabs together, the column/row index might be extended over the Excel sheet range, and the report part which is out of this range will get lost in the result file. * If a whole merged crosstab gets quite large, it might cause an out of memory condition during the exporting process. |
| Rows per Sheet | Specifies the maximum number of rows for every worksheet when exporting the report tab to Excel. For the Excel version Excel 97-2003 Workbook (\*.xls), the value ranges from 0 to 65000. Any value out of the range will be considered as 65000. For the Excel version Excel Workbook (\*.xlsx), the value ranges from 0 to 1048000. Any value out of the range will be considered as 1048000.  Data type: Integer |
| Sheet Name | Specifies the sheet name for the report tab when exporting it to Excel. If the report tab is split into several sheets when exported to Excel because of limited rows per sheet, a postfix number will be added to the sheets starting from the second one (SheetName, SheetName1, SheetName2, SheetName3...). Data type: String  **Note:** The characters "|", ":", "/", "?", "\", "\*", "]", "[" cannot be displayed in the sheet name in Excel and the last character in the sheet name cannot be single quotation mark ('). If any one of them is used when you specify the property, it will be replaced by "\_" in Excel. |
| [Style Group for Export](#Export) | |
| Page Report Style Group | Pre-sets a style group for use when exporting the report tab to Page Report Result. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| Excel Style Group | Pre-sets a style group for use when exporting the report tab to Excel. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| Fax Style Group | Pre-sets a style group for use when exporting the report tab to Fax. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| HTML Style Group | Pre-sets a style group for use when exporting the report tab to HTML. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| PDF Style Group | Pre-sets a style group for use when exporting the report tab to PDF. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| PS Style Group | Pre-sets a style group for use when exporting the report tab to PostScript. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| RST Style Group | Pre-sets a style group for use when exporting the report tab to Logi JReport Result or Applet. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| RTF Style Group | Pre-sets a style group for use when exporting the report tab to RTF. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| Text Style Group | Pre-sets a style group for use when exporting the report tab to Text. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |
| XML Style Group | Pre-sets a style group for use when exporting the report tab to XML. If you do not specify a value here, the [Style Group](#StyleGroup) property value will be applied. Data type: String |

## Automatic Cube Initialization

In order for a query based report component created in Logi JReport Designer, such as table, crosstab, chart, and banded object, to be able to perform analytic reporting actions on when you work with them in Page Report Studio, Logi JReport needs to convert the component from query based to business view based.

**When the conversion is required**

The conversion is required when Page Report Studio end user is trying to perform an analytic reporting action such as drilling through data on a table, crosstab, chart, or banded object which is created based on a query.

When the property Automatic Cube Initialization is set to true, Logi JReport will automatically convert the queries a report tab uses to business views when opening the report tab in Page Report Studio.

**What makes the conversion successful**

The success of the conversion lies in the following aspects:

* There should be a business view using only the query that a report component uses as the data resource.
* All the fields in the report component have corresponding elements in the business view. For the mapping relationship, see the section [How to convert](#How).
* The cases illustrated in [What cannot be converted](#cannot) should be avoided.

**Tip:** The report designer can create a complete and full-function business view for the required query, in this way, all fields in the query are able to be converted since there are always corresponding view elements found in the complete business view. To create such a complete business view, create a group and a detail object for each DBField and formula, and create an aggregation for each summary.

**How to convert**

The following lists what types of fields in the query will be converted to what types of elements in the business view:

| When a query field is used as | It will be converted to |
| --- | --- |
| Group by field, crosstab column/row field, chart category/series field | Group element |
| Crosstab summaries | Aggregation element |
| Show Value in chart and is a summary | Aggregation element |
| Show Value in chart and is of Number type | Detail element |
| Others and there is corresponding detail object in the business view | Detail element |
| Others and there isn't corresponding detail object in the business view | Group element |

**What cannot be converted**

The following list shows the cases in a query based component that do not support conversion. The list supposes that all the involved query fields have their corresponding view elements in the business view based on the query:

* Static summary (except that used as Show Value of chart or in the current group by level).
* Dynamic summary (except when the summary's group by level is 0).
* Formula that references summaries.
* Page level formula, that is, the formula calculated after the whole report finishes rendering.
* DBField or formula used as group by field but the group has a special function.
* Parameter used as group by field.
* Chart in a banded object that uses inherited dataset.
* Table, crosstab, or banded object whose dataset is inherited.
* Table, crosstab, chart, or banded object when one of its children components cannot be converted (the children components exclude blank components and those having already been converted).

## Result Buffer

The result buffer is used to store the report results of one report in pages. Its default size 4 indicates 4 pages of a report results have been allocated to the result buffer. The other pages will be stored on disk. If you have enough memory, you can increase the result buffer size to store more pages of the report result. By doing this, you will achieve better performance.

## Applet Setting

Reports are developed in Logi JReport Designer and saved as.cls file. Report files and their associated resource files (.cat and.fml files) are published to Logi JReport Server for running reports in client/server mode. Once the report repository is properly set up, it can be accessed with any web browser or Page Report Studio. Also, you can choose to export the report results to a printer, a PDF file, a TXT file, and so on.

If the report results have been specified to be transferred and viewed in the applet format, you can change the display area by inputting the correct number in the Report Inspector. Alternatively, you can edit the applet file directly in a text editor.

* **Applet Height**: Refers to the height of an applet.
* **Applet Width**: Refers to the width of an applet.

See also [Exporting to Applet](https://devnet.logianalytics.com/hc/en-us/articles/1500009589241-Exporting-to-Applet) for more information about this format.

## Setup Callback or Exit Functions

During the running of a report, the display of the report is done by Logi JReport Engine. You have no control over this. However, Logi JReport functionality allows you to interact with this mechanism at 3 points:

* After the parameter has been initiated.
* At the point Logi JReport Engine is about to run the report. If you have parameters, the parameter at this stage will have been initiated, and you have given the parameter value.
* Immediately after Logi JReport Engine has run the report result.

At any or all of these three points you have the option of executing a class of your choice. Logi JReport has developed three [Exit functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009562522-Logi-JReport-Exit-Functions) for you: After Init Parameter, Before Run and After Run. These functions enable you to develop an action to be called before, after or during the process of running a report. Your applications will return true or false. For true, Logi JReport Engine will go on running. For false, Logi JReport Engine will stop at this point.

## Import JavaScript

If you want to develop functions in your own JS file, you can use this property to support the control objects when viewing reports in Page Report Studio. Your own JS file should be located in `<server_install_root>\public_html\javascript\dhtml`, and it will work together with the API.js file in the same folder, but with a higher priority if both of them contain the same functions.

To use this property, simply set the property value to the name of your JS file.

For example, you have a JavaScript file named "user1.js" which contains the following function:

|  |
| --- |
| ``` function promptMessage(message)   {   alert(message);   } window.promptMessage("test") ``` |

In this example, set the property to "user1.js" in order to apply functions defined in the file.

## Excel Buffer Size

The Excel buffer is used to store the report results in Excel buffer sheets when exporting the result in Excel format. Its default size is 1, which indicates 1 sheet of the report results is allocated to the result buffer. The other sheets will be stored on disk. If you have enough memory, you can increase the Excel buffer size to store more sheets of the Excel-format report result. By doing this, you will achieve better performance.

## Columned

Right after you set the property to true from false each time:

* Recalculate the values of the following Excel properties of all objects in the report and reset the values to the defaults.
  + Column Index/Row Index
  + Column Number/Row Number. The properties are for chart platforms, images and UDOs.
  + Top Attach Column/Top Attach Row/Bottom Attach Column/Bottom Attach Row. The properties are for drawing objects.

  The default values are calculated based on the position of each object in the report. There is an exception: if both the Export to Excel and Export to CSV properties of an object are false, the values of these properties will not be recalculated and will be preserved as before.

The property controls two things when it is true:

* Use the columned method to export the report to Excel when the option Column Format in the Export to Excel dialog is checked.
* You can specify values for the Excel properties mentioned above of an object instead of using the default.

When the property is false:

* The specified values for the above Excel properties of objects in the report are not applied when exporting to CSV or Excel.

## Style Group for Export

This is to pre-set a style group to the report for each export format. The style group specified for export formats has higher priority than that specified for the [Style Group](#StyleGroup) property in the Report Inspector. However, if you do not specify a style group for an export format, when you export the report to the format, it will take the value specified for the Style Group property.

The specified style group here is applied in the following cases: when export or preview the report in Logi JReport Designer, export the report in Page Report Studio, and when run/advanced run the report or schedule to publish it to version/disk/e-mail/FTP in Logi JReport Server.

When viewing a report by selecting the View tab in Logi JReport Designer, the value specified for the Style Group property is selected by default in the Select Style Group dialog but you can choose another style group you want to use in the dialog. In the view mode, if you further preview the view result in different formats or export it to different formats, the preview/export result will take the style group of the view result, and the Style Group for Export property will not take effect.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009591701-Properties-of-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569782-Properties-of-Parameter-Control-in-Page-Report)
