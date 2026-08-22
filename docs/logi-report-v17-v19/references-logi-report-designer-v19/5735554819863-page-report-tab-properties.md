---
title: "Page Report Tab Properties"
id: 5735554819863
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties
updated_at: 2022-11-02T08:18:47Z
---

# Page Report Tab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735585709847-Page-Report-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735546567191-Paragraph-Properties)

# Page Report Tab Properties

This topic describes the properties of a Page Report Tab object.

| Property Name | Description |
| --- | --- |
| General | |
| Default Format for Viewing Report | Specifies the default format to view the report tab on Server. Default is to adopt the format setting on Server. If you select a specific format, you can further configure the format options. Choose an option from the drop-down list.  * **<Server Setting>** Select to adopt the format setting on Server. * **Page Report** Select to view the report tab in Page Report Studio. Select the ellipsis Ellipsis button in the value cell to configure the format options in the [Page Report Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515048599-Page-Report-Option-Dialog-Box). * **HTML** Select to view the report tab in HTML. Select the ellipsis Ellipsis button in the value cell to configure the format options in the [HTML Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530096407-HTML-Option-Dialog-Box). * **PDF** Select to view the report tab in PDF. Select the ellipsis Ellipsis button in the value cell to configure the format options in the [PDF Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515042711-PDF-Option-Dialog-Box). * **Excel** Select to view the report tab in Excel. Select the ellipsis Ellipsis button in the value cell to configure the format options in the [Excel Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735529356567-Excel-Option-Dialog-Box). * **Text** Select to view the report tab in Text. Select the ellipsis Ellipsis button in the value cell to configure the format options in the [Text Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735531704087-Text-Option-Dialog-Box). * **RTF** Select to view the report tab in RTF. Select the ellipsis Ellipsis button in the value cell to configure the format options in the [RTF Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515297943-RTF-Option-Dialog-Box). * **XML** Select to view the report tab in XML. Select the ellipsis Ellipsis button in the value cell to configure the format options in the [XML Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735525274647-XML-Option-Dialog-Box). * **PostScript** Displays the report tab in PostScript. Select the ellipsis Ellipsis button in the value cell to configure the format options in the [PostScript Option dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530790679-PostScript-Option-Dialog-Box).   Data type: Enumeration  Note icon This property only controls direct running of the report tab on Server, but has no effect on advanced running or scheduled running of the report tab. |
| Instance Name | Designer displays this property when the page report tab uses query resources. It shows the instance name of the report tab and is read only. |
| Report Layout Type | Designer displays this property when the page report tab uses query resources. It shows the layout type of the report tab and is read only.  * **Flow Report** A regular flow layout report. * **Banded Report** A restricted flow layout report intended for Logi Report v7 compatibility only. |
| Result Buffer | |
| Result Buffer Size | Specifies the number of the report pages to store in the buffer. The default size 4 indicates Logi Report Engine allocates four pages of the report to the result buffer, and stores the other pages on disk. If you have enough memory, you can increase the result buffer size to store more pages of the report, so that you can get better performance. Data type: Integer |
| Data (available to query-based page report tab) | |
| [Automatic Cube Initialization](#ACI) | Specifies whether to enable automatic conversion of queries into business views at runtime for the report tab. When you set this property to "true", when users opening the report tab in Page Report Studio, Logi Report Engine automatically converts all the queries the data components in the report tab use to appropriate business views for analytic reporting purpose. If the conversion fails due to error or incomplete conditions, Logi Report Engine displays no warning message on UI but records the information into the log file.  When you set this property to "false", Logi Report Engine does not perform the conversion of queries to business views automatically when users open the report tab in Page Report Studio; instead, it converts the query a data component applies to a business view respectively when users perform an analytic reporting action on each data component, such as adding a field into the data component.  Data type: Boolean |
| Others | |
| After Init Parameter | Designer displays this property when the page report tab uses query resources. You can use it to implement the [Exit functions](https://devnet.logianalytics.com/hc/en-us/articles/5735563519639-Using-the-Exit-Functions). Specify an external application file (Java class file) that develops an action, Logi Report Engine then calls the action after you specify parameters when running the report tab. Data type: String |
| After Run | Designer displays this property when the page report tab uses query resources. You can use it to implement the [Exit functions](https://devnet.logianalytics.com/hc/en-us/articles/5735563519639-Using-the-Exit-Functions). Specify an external application file (Java class file) that develops an action, Logi Report Engine then calls the action immediately after it finishes running the report. Data type: String |
| Before Run | Designer displays this property when the page report tab uses query resources. You can use it to implement the [Exit functions](https://devnet.logianalytics.com/hc/en-us/articles/5735563519639-Using-the-Exit-Functions). Specify an external application file (Java class file) that develops an action, Logi Report Engine then calls the action at the point it is about to run the report tab. Data type: String |
| Click Priority | Specifies the priority of the actions to be triggered at runtime when users select certain objects that are bound with some actions in the report tab. Select the ellipsis Ellipsis button in the value cell to set the priority in the [Click Priority dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499978775-Click-Priority-Dialog-Box). Data type: String |
| This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.[Continuous Page Number with TOC](#ContinuousPageNumber) | Specifies whether to calculate pages for the Export Page Number and Export Total Page Number special fields in the report tab continuously when the report tab contains a TOC page panel. Data type: Boolean |
| Embedded Fonts | Specifies the True Type Fonts that you want to embed in the PDF output of the report tab, if you have used TTF in the report tab. You can select multiple fonts from the value drop-down list by pressing the Ctrl or Shift key. For more information, see [Delivering TTF in PDF](https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports#DeliverPDF). Data type: String |
| This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.Ignore TOC Anchor of Parent | Specifies whether to ignore the TOC Anchor property of objects that act as parent containers of other objects in the report tab, when generating Tables of Contents for the report tab. When you set this property to "true", Logi Report Engine generates a TOC entry for an object if its TOC Anchor property is "true", even when you do not include its parent object in the TOC. If you do not want to create TOC entries for those child objects when their parent objects are excluded, set this property to "false". Data type: Boolean |
| Import JavaScript | Designer displays this property when the page report tab uses query resources. You can use it to specify the name of a JavaScript file you develop to apply customized functions to the report tab in Page Report Studio, for example, test.js. You should save the JavaScript file in `<server_install_root>\public_html\javascript\dhtml`, and it will work together with API.js in the same folder, but with a higher priority if both of them contain the same functions. For example, you can create a JavaScript file that contains the following function:  `function promptMessage(message)     {     alert(message);     } window.promptMessage("test")`  Data type: String |
| No Temp File | Specifies whether to create temporary files for the report tab. You gain faster performance if you do not create the temporary files (true), while have better accuracy in data calculation with the temporary files (false). Data type: Boolean |
| On Parameter Value Change | Specifies the formulas for validating the parameter values in the report tab. After you specify the formulas, when users change the parameter values at runtime, Logi Report Engine passes the values to the formulas first for validation: if the values are valid, Logi Report Engine applies them to the parameters; otherwise, it displays the messages you define in the formulas. Choose the formulas from the drop-down list (to select multiple formulas, use the Ctrl or Shift key on the keyboard, then select outside the value cell to confirm). For example, for a String type parameter that requires a value of 4-7 characters, you can define a formula like this:  `if(length(@P_String) > 8 ) "The value is too long."  else if (length(@P_String) < 3 ) "The value is too short."   else ""`  Then, when users specify a string value of 9 characters to the parameter, Logi Report Engine displays the message "The value is too long.".  Data type: Object Array  Note icon When you define the formula, you need to make it return a blank string for valid parameter values. |
| Page Background | Specifies the background color of the report page. Choose a color from the drop-down list, or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Precision Sensitive | Designer displays this property when the page report tab uses query resources. You can use it to specify whether to enable [customized precision settings](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports#Precision) for the output of the report tab. If you do not care the report visual effect, leave the value of the property to "false" (the default behavior) to let Logi Report Engine deal with the precision. Logi Report Engine has better performance when precision insensitive than when sensitive. When you set this property to "true", Logi Report Engine applies the precision level you specify for each export format in the output. Data type: Boolean |
| This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.Push Down On-screen Filter | Specifies whether to push down the [on-screen filters](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports) in the report tab to execute the filters in the database at runtime. Data type: Boolean |
| Remove Extra Characters from First Line | Specifies whether to remove the quotation marks and commas from the first line of the report tab's Text and CSV outputs. Data type: Boolean |
| Show Subreport Header Footer | Specifies whether to show the page header and footer panels of the subreports in the report tab when the panels are visible in the subreports. Data type: Boolean |
| Style Group | Specifies the style group for the report tab. When you use the report tab as a subreport, choosing any style group from the drop-down list turns on the Style Group feature for the report tab, meaning, it inherits the style group from the primary report; choosing "none" or leaving this property blank turns off the Style Group feature for the report tab, meaning, it does not inherit style group from the primary report.  When you use the report tab as a linked report, if you select "Pass style group information down to linked report" while defining the link condition, the report tab inherits the style group from the primary report; if you do not select that option, it applies the style group that you specify for the property.  Data type: String |
| Suppress Object Space If Not Exported | Specifies whether to suppress the space for holding the objects in the output of the report tab, if you have specified to exclude them from exporting. Data type: Boolean |
| Work as Subreport | Specifies whether to use the report tab as a subreport only. If you set this property to "true", when users run the corresponding page report in Page Report Studio, they are not able to open the report tab from the Go To drop-down list or by switching tabs. |
| Excel | |
| Column Width List | Designer displays this property when the page report tab uses query resources. You can use it to specify the width of the columns beginning from the first column for the Excel output of the report tab. Use semicolon (;) to separate each width. If you do not want to specify the width for a certain column, omit the value, Logi Report Engine then applies the default value 8 for the column. For example, you can specify the column width like this:  12;8;15;10;9  The example specifies the width of the first 5 columns. For the other columns, they take the default width of Microsoft Excel sheet. 8 is the default column width in a Microsoft Excel sheet, and you can omit it, so you can also set the preceding example as:  12;;15;10;9  Data type: String  Note icon   * This property takes effect when you [export the report to Excel using Column Format](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel#Format) and set the report tab's Columned property to "true". * If the report tab contains a subreport, Logi Report Engine disables the Column Width List property of the subreport when generating the Excel output for the report tab. |
| [Columned](#Columned) | Specifies whether to turn on the properties related with exporting the report tab to a columned file, such as Excel and CSV. Data type: Boolean |
| Excel Buffer Size | Designer displays this property when the page report tab uses query resources. You can use it to specify the number of the report sheets to store in the buffer when exporting the report tab to Excel. The default size 1 indicates that Logi Report Engine allocates one sheet of the report to the result buffer, and stores the other sheets on disk. If you have enough memory, you can increase the Excel buffer size to store more sheets of the Excel output, so that you can get better performance. Data type: Integer  Note icon This property does not take effect if you export the report to Excel using Data Format. |
| Fast Pass | Designer displays this property when the page report tab uses query resources. If you set it to "true", users can get better performance when running the report tab to CSV in multiple threads on Server. Data type: Boolean  Note icon This property takes effect when you set the report tab's Columned property to "true". |
| Full Fill and Border | Specifies whether to apply background color and display border for empty cells in the Excel output of the report tab, using the format you have specified in the report template. Data type: Boolean  Note icon This property takes effect when you export the report tab to Excel using Report Format or Column Format; and if you use Column Format, you should set the report tab's Columned property to "false". |
| No Page Break for Column Format | Specifies whether to remove the page breaks on each individual sheet when you export the report tab to Excel using Column Format. Data type: Boolean |
| [No Page Break for Data Format](#NoPageBreak) | Specifies whether to remove the page breaks on each individual sheet when you export the report tab to Excel using Data Format. Data type: Boolean |
| [No Page Break for Report Format](#NoPageBreak) | Specifies whether to remove the page breaks on each individual sheet when you export the report tab to Excel using Report Format. Data type: Boolean |
| [Rows per Sheet](#RowsPerSheet) | Specifies the maximum number of rows in every worksheet in the Excel output of the report tab. Type an integer value to change the number.  * When you export the report tab to the Excel version of Excel 97-2003 Workbook (\*.xls), you can type a value that ranges from 0 to 65000. Logi Report Engine regards any value out of the range as 65000. * When you export the report tab to the Excel version of Excel Workbook (\*.xlsx), you can type a value that ranges from 0 to 1048000. Logi Report Engine regards any value out of the range as 1048000.   Data type: Integer |
| Sheet Name | Specifies the sheet name for the report tab in the Excel output. For a query-based report tab, if Logi Report Engine splits it into several sheets in the Excel output because of limited rows per sheet, it adds a postfix number to the sheets starting from the second one (SheetName, SheetName1, SheetName2, SheetName3...).  Data type: String  Note icon Excel does not support using the following characters in the sheet name: "|", ":", "/", "?", "\", "\*", "]", "[", and the single quotation mark (') as the last character either. If you use any one of them in the value of the property, Excel replaces it with "\_". |
| [Style Group for Export](#Export) (available to query-based page report tab) | |
| Excel Style Group | Specifies the style group for the Excel output of the report tab. If you do not specify a value for this property, Logi Report Engine applies the value of [Style Group](#StyleGroup) in the output. Data type: String |
| Fax Style Group | Specifies the style group for the fax output of the report tab. If you do not specify a value for this property, Logi Report Engine applies the value of [Style Group](#StyleGroup) in the output. Data type: String |
| HTML Style Group | Specifies the style group for the HTML output of the report tab. If you do not specify a value for this property, Logi Report Engine applies the value of [Style Group](#StyleGroup) in the output. Data type: String |
| Page Report Style Group | Specifies the style group for running the report tab in Page Report Studio. If you do not specify a value for this property, Logi Report Engine applies the value of [Style Group](#StyleGroup) to run the report tab. Data type: String |
| PDF Style Group | Specifies the style group for the PDF output of the report tab. If you do not specify a value here, Logi Report Engine applies the value of [Style Group](#StyleGroup) in the output. Data type: String |
| PS Style Group | Specifies the style group for the PostScript output of the report tab. If you do not specify a value for this property, Logi Report Engine applies the value of [Style Group](#StyleGroup) in the output. Data type: String |
| RST Style Group | Specifies the style group for the RST output of the report tab. If you do not specify a value for this property, Logi Report Engine applies the value of [Style Group](#StyleGroup) in the output. Data type: String |
| RTF Style Group | Specifies the style group for the RTF output of the report tab. If you do not specify a value for this property, Logi Report Engine applies the value of [Style Group](#StyleGroup) in the output. Data type: String |
| Text Style Group | Specifies the style group for the Text output of the report tab. If you do not specify a value here, Logi Report Engine applies the value of [Style Group](#StyleGroup) for the output. Data type: String |
| XML Style Group | Specifies the style group for the XML output of the report tab. If you do not specify a value for this property, Logi Report Engine applies the value of [Style Group](#StyleGroup) in the output. Data type: String |

## Automatic Cube Initialization

In order for users to perform analytic reporting actions on a query-based report component developed in Designer in Page Report Studio, Logi Report Engine needs to convert the component from query based to business view based.

**When the conversion is required**

The conversion is required when a user is trying to perform an analytic reporting action such as drilling through data on a crosstab that uses a query resource in Page Report Studio.

When the Automatic Cube Initialization property of a report tab is "true", Logi Report Engine automatically converts the queries the report tab uses to business views when a user opens the report tab in Page Report Studio.

**What makes the conversion successful**

The success of the conversion lies in the following aspects:

* There should be a business view using only the query that a data component applies as the data resource.
* All the fields in the data component have corresponding elements in the business view. For the mapping relationship, see [How to convert](#How).
* The cases described in [What cannot be converted](#cannot) should be avoided.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The report designer can create a complete and full function business view for the required query. In this way, Logi Report Engine is able to convert all fields in the query because there are always corresponding view elements in the complete business view. To create such a complete business view, create a group and a detail element for each DBField and formula, and create an aggregation for each summary.

**How to convert**

The following lists how Logi Report Engine converts each type of the fields in a query to the corresponding view element.

| If a query field is used as | Convert it to |
| --- | --- |
| Group-by field, crosstab column/row field, chart category/series field | Group object |
| Crosstab summaries | Aggregation object |
| Show Value in chart and is a summary | Aggregation object |
| Show Value in chart and is Number data type | Detail object |
| Static summary in the current or child group level, that is, the group-by field of the static summary is the same as the one used for the current group level or an ancestor group level | Aggregation object |
| Others and there is corresponding detail object in the business view | Detail object |
| Others and there isn't corresponding detail object in the business view | Group object |

**What cannot be converted**

The following shows the cases in a query-based data component that do not support conversion. The list supposes that all the involved query fields have their corresponding view elements in the business view based on the query:

* Static summary (except that used as Show Value of chart or in the current or child group level).
* Dynamic summary (except when the summary's group-by level is 0).
* Formula that references summaries.
* Page level formula.
* DBField or formula used as group-by field but the group has a special function.
* Parameter used as group-by field.
* Chart in a banded object that uses inherited dataset.
* Table, crosstab, or banded object that uses inherited dataset.
* Table, crosstab, chart, or banded object when one of its child components cannot be converted (the child components exclude blank components and those having already been converted).

## This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.Continuous Page Number with TOC

When you insert the Export Page Number or Export Total Page Number special field in the header/footer of the page panels in a report tab, if one of the page panels is a TOC page panel (you add a [table of contents](https://devnet.logianalytics.com/hc/en-us/articles/5735569955863-Adding-a-Table-of-Contents-in-a-Report) in the report tab), Logi Report Engine divides the pages into three portions: pages generated by page panels before the TOC page panel, the TOC pages generated by the TOC page panel, and pages generated by page panels after the TOC page panel. You can use this property to control whether you want to calculate page number for the special field in each portion differently (the default behavior when this property is "false"), or display continuous page number calculated from the first report page to the last with the TOC pages included.

For example, you have the following page panels in a report tab: two page panels before the TOC page panel and another two after it, and each of the page panel generates one page. Then you insert Export Page Number and Export Total Page Number in the header of all page panels.

![Page Panels](https://devnet.logianalytics.com/hc/article_attachments/9898475806103/prpty_rpt_pgrpttb1.gif)

When the Continuous Page Number with TOC property is "false" by default, the page number stops at the TOC page, page number for the TOC page is differently calculated from other pages, and then the page number starts all over again after the TOC page.

![Discontinuous Page Number](https://devnet.logianalytics.com/hc/article_attachments/9898458799255/prpty_rpt_pgrpttb2.gif)

When you set Continuous Page Number with TOC to "true", the number is calculated continuously from the very first report page to the last in the report.

![Continuous Page Number](https://devnet.logianalytics.com/hc/article_attachments/9898475836311/prpty_rpt_pgrpttb3.gif)

## Columned

After setting Columned to "true", you can predefine the coordinates for all objects in a report when exporting the report to a columned file such as [Excel](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel#Format) and [CSV](https://devnet.logianalytics.com/hc/en-us/articles/5735525405719-Exporting-Reports-to-Text#CSV), which helps improve Logi Report Engine's performance by saving the extra position calculating time during the export process. You can specify values of the following properties for each object to position them as you want in the output.

* Column Index, Row Index
* Column Number, Row Number. You can set the two properties for charts, images, and UDOs.
* Top Attach Column, Top Attach Row, Bottom Attach Column, and Bottom Attach Row. You can set the four properties for [drawing objects](https://devnet.logianalytics.com/hc/en-us/articles/5735554341911-Box-Properties#ExcelProperties).

Designer calculates the default values of these properties based on the position of each object in the report. Each time after you set Columned to "true" from "false", Designer recalculates the property values for all objects in the report and resets the values to the defaults (there is an exception: if both the Export to Excel and Export to CSV properties of an object are "false", Designer does not recalculate the values and instead preserves them as before).

## No Page Break

When you export a report to Excel without page breaks, the column headings appear just at the top of the Excel spreadsheet and are not repeated throughout the report (the split pages are technically merged within the Excel sheet); while, if the report breaks to a new sheet, the page header displays once again.

However, exporting a report to an Excel file without page breaks could bring the following results and limitations:

* In the Excel output, only one page header panel and one page footer panel in a banded object can display in each sheet. Only the first banded page header and the last banded page footer display in the output. As for tables, Logi Report Engine only exports the first table header and the last table footer.
* You cannot get a continuous table or banded object if the report contains other objects in horizontal locations. Logi Report Engine exports all split parts of a horizontal table vertically.
* Merging tables or crosstabs together extends the Excel sheet, which may cover other objects if they happen to be in the extended direction. Merging crosstabs together might extend the column/row index over the Excel sheet range, so you may lose the report part that is out of this range in the output.
* If a whole merged crosstab gets quite large, it might cause an out of memory error during the export process.

## Rows per Sheet

When you export a report to Excel, Logi Report Engine does not separate the rows in the same page and exports them to different worksheets, thus the number of rows it exports to a worksheet may be greater than the number you specify for the Rows per Sheet property. For example, when you set Rows per Sheet to 100, Logi Report Engine exports all content in the first page to the first worksheet, then it tests the number of rows the first page occupies in the first worksheet and determines where to export the next page.

* When the first page has less than 100 rows in the first worksheet, Logi Report Engine still exports the next page to the first worksheet even when the number of rows in the first page and the next is greater than 100.
* When the number of rows in the first page is equal to or more than 100, Logi Report Engine generates a new worksheet and exports the second page to the new worksheet.

## Style Group for Export

You can use the Style Group for Export properties to preset a style group to the report tab for each export format. The Style Group for Export properties have higher priority than the [Style Group](#StyleGroup) property. However, if you do not specify a style group for an export format, the report output of this format applies the value that you specify for the Style Group property by default.

The Style Group for Export properties take effect in the following cases:

* Export or preview the report in Designer.
* Export the report in Page Report Studio.
* Run and advanced run the report or schedule to publish it to version/disk/email/FTP on Server.

When you select the View tab to preview a report tab in Designer, Designer selects the value that you specify for the Style Group property in the Select Style Group dialog box by default. You can select another style group to apply to the report tab. In Designer view mode, if you further preview the view result in different formats or export it to different formats, the preview/output applies the style group of the view result, instead of the Style Group for Export property values.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735585709847-Page-Report-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735546567191-Paragraph-Properties)
