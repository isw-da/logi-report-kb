---
title: "Page Report Tab Properties"
id: 28898548533901
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898548533901-Page-Report-Tab-Properties
updated_at: 2024-09-30T09:09:33Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Page Report Tab Properties

This topic describes the properties of a Page Report Tab object.

| Property Name | Description |
| --- | --- |
| General |  |
| Default Format for Viewing Report | Specifies the default format to view the report tab on Server. Default is to adopt the format setting on Server. If you select a specific format, you can further configure the format options. Choose an option from the drop-down list.  Select to adopt the format setting on Server. Page Report Select to view the report tab in Page Report Studio. Select the ellipsis in the value cell to configure the format options in the Page Report Option dialog box. HTML Select to view the report tab in HTML. Select the ellipsis in the value cell to configure the format options in the HTML Option dialog box. PDF Select to view the report tab in PDF. Select the ellipsis in the value cell to configure the format options in the PDF Option dialog box. Excel Select to view the report tab in Excel. Select the ellipsis in the value cell to configure the format options in the Excel Option dialog box. Text Select to view the report tab in Text. Select the ellipsis in the value cell to configure the format options in the Text Option dialog box. RTF Select to view the report tab in RTF. Select the ellipsis in the value cell to configure the format options in the RTF Option dialog box. XML Select to view the report tab in XML. Select the ellipsis in the value cell to configure the format options in the XML Option dialog box. PostScript Displays the report tab in PostScript. Select the ellipsis in the value cell to configure the format options in the PostScript Option dialog box. Data type: Enumeration This property only controls direct running of the report tab on Server, but has no effect on advanced running or scheduled running of the report tab. |
| Instance Name | Designer displays this property when the page report tab uses query resources. It shows the instance name of the report tab and is read only. |
| Report Layout Type | Designer displays this property when the page report tab uses query resources. It shows the layout type of the report tab and is read only. Flow Report A regular flow layout report. Banded Report A restricted flow layout report intended for Report v7 compatibility only. |
| Result Buffer |  |
| Result Buffer Size | Specifies the number of the report pages to store in the buffer. The default size 4 indicates Report Engine allocates four pages of the report to the result buffer, and stores the other pages on disk. If you have enough memory, you can increase the result buffer size to store more pages of the report, so that you can get better performance. Data type: Integer |
| Data (available to query-based page report tab) |  |
| Automatic Cube Initialization | Specifies whether to enable automatic conversion of queries into business views at runtime for the report tab. When you set this property to "true", when users opening the report tab in Page Report Studio, Report Engine automatically converts all the queries the data components in the report tab use to appropriate business views for analytic reporting purpose. If the conversion fails due to error or incomplete conditions, Report Engine displays no warning message on UI but records the information into the log file. When you set this property to "false", Report Engine does not perform the conversion of queries to business views automatically when users open the report tab in Page Report Studio; instead, it converts the query a data component applies to a business view respectively when users perform an analytic reporting action on each data component, such as adding a field into the data component. Data type: Boolean |
| Others |  |
| After Init Parameter | Designer displays this property when the page report tab uses query resources. You can use it to implement the Exit functions. Specify an external application file (Java class file) that develops an action, Report Engine then calls the action after you specify parameters when running the report tab. Data type: String |
| After Run | Designer displays this property when the page report tab uses query resources. You can use it to implement the Exit functions. Specify an external application file (Java class file) that develops an action, Report Engine then calls the action immediately after it finishes running the report. Data type: String |
| Before Run | Designer displays this property when the page report tab uses query resources. You can use it to implement the Exit functions. Specify an external application file (Java class file) that develops an action, Report Engine then calls the action at the point it is about to run the report tab. Data type: String |
| Click Priority | Specifies the priority of the actions to be triggered at runtime when users select certain objects that are bound with some actions in the report tab. Select the ellipsis in the value cell to set the priority in the Click Priority dialog box. Data type: String |
| Continuous Page Number with TOC | Specifies whether to calculate pages for the Export Page Number and Export Total Page Number special fields in the report tab continuously when the report tab contains a TOC page panel. Data type: Boolean |
| Embedded Fonts | Specifies the True Type Fonts that you want to embed in the PDF output of the report tab, if you have used TTF in the report tab. You can select multiple fonts from the value drop-down list by pressing the Ctrl or Shift key. For more information, see Delivering TTF in PDF. Data type: String |
| Ignore TOC Anchor of Parent | Specifies whether to ignore the TOC Anchor property of objects that act as parent containers of other objects in the report tab, when generating Tables of Contents for the report tab. When you set this property to "true", Report Engine generates a TOC entry for an object if its TOC Anchor property is "true", even when you do not include its parent object in the TOC. If you do not want to create TOC entries for those child objects when their parent objects are excluded, set this property to "false". Data type: Boolean |
| Import JavaScript | Designer displays this property when the page report tab uses query resources. You can use it to specify the name of a JavaScript file you develop to apply customized functions to the report tab in Page Report Studio, for example, test.js. You should save the JavaScript file in \public_html\javascript\dhtml, and it will work together with API.js in the same folder, but with a higher priority if both of them contain the same functions.For example, you can create a JavaScript file that contains the following function: function promptMessage(message) { alert(message); } window.promptMessage("test") Data type: String |
| No Temp File | Specifies whether to create temporary files for the report tab. You gain faster performance if you do not create the temporary files (true), while have better accuracy in data calculation with the temporary files (false). Data type: Boolean |
| On Parameter Value Change | Specifies the formulas for validating the parameter values in the report tab. After you specify the formulas, when users change the parameter values at runtime, Report Engine passes the values to the formulas first for validation: if the values are valid, Report Engine applies them to the parameters; otherwise, it displays the messages you define in the formulas. Choose the formulas from the drop-down list (to select multiple formulas, use the Ctrl or Shift key on the keyboard, then select outside the value cell to confirm). For example, for a String type parameter that requires a value of 4-7 characters, you can define a formula like this: if(length(@P_String) > 8 ) "The value is too long." else if (length(@P_String) Automatic Cube Initialization

In order for users to perform analytic reporting actions on a query-based report component developed in Designer in Page Report Studio, Report Engine needs to convert the component from query based to business view based.

When the conversion is required

The conversion is required when a user is trying to perform an analytic reporting action such as drilling through data on a crosstab that uses a query resource in Page Report Studio.

When the Automatic Cube Initialization property of a report tab is "true", Report Engine automatically converts the queries the report tab uses to business views when a user opens the report tab in Page Report Studio.

What makes the conversion successful

The success of the conversion lies in the following aspects: 

- There should be a business view using only the query that a data component applies as the data resource.

- All the fields in the data component have corresponding elements in the business view. For the mapping relationship, see How to convert. 

- The cases described in What cannot be converted should be avoided. 

 The report designer can create a complete and full function business view for the required query. In this way, Report Engine is able to convert all fields in the query  because there are always corresponding view elements in the complete business view. To create such a complete business view, create a group and a detail element for each DBField and formula, and create an aggregation for each summary.

How to convert

The following lists how Report Engine converts each type of the fields in a query to the corresponding view element.

| If a query field is used as | Convert it to |
| --- | --- |
| Group-by field, crosstab column/row field, chart category/series field | Group object |
| Crosstab summaries | Aggregation object |
| Show Value in chart and is a summary | Aggregation object |
| Show Value in chart and is Number data type | Detail object |
| Static summary in the current or child group level, that is, the group-by field of the static summary is the same as the one used for the current group level or an ancestor group level | Aggregation object |
| Others and there is corresponding detail object in the business view | Detail object |
| Others and there isn't corresponding detail object in the business view | Group object |

What cannot be converted

The following shows the cases in a query-based data component that do not support conversion. The list supposes that all the involved query fields have their corresponding view elements in the business view based on the query:

- Static summary (except that used as Show Value of chart or in the current or child group level).

- Dynamic summary (except when the summary's group-by level is 0).

- Formula that references summaries.

- Page level formula.

- DBField or formula used as group-by field but the group has a special function.

- Parameter used as group-by field.

- Chart in a banded object that uses inherited dataset.

- Table, crosstab, or banded object that uses inherited dataset.

- Table, crosstab, chart, or banded object when one of its child components cannot be converted (the child components exclude blank components and those having already been converted).

## 
Continuous Page Number with TOC

When you insert the Export Page Number or Export Total Page Number special field in the header/footer of the page panels in a report tab, if one of the page panels is a TOC page panel (you add a table of contents in the report tab), Report Engine divides the pages into three portions: pages generated by page panels before the TOC page panel, the TOC pages generated by the TOC page panel, and pages generated by page panels after the TOC page panel. You can use this property to control whether you want to calculate page number for the special field in each portion differently (the default behavior when this property is "false"), or display continuous page number calculated from the first report page to the last with the TOC pages included.

For example, you have the following page panels in a report tab: two page panels before the TOC page panel and another two after it, and each of the page panel generates one page. Then you insert Export Page Number and Export Total Page Number in the header of all page panels. 

When the Continuous Page Number with TOC property is "false" by default, the page number stops at the TOC page, page number for the TOC page is differently calculated from other pages, and then the page number starts all over again after the TOC page.

When you set Continuous Page Number with TOC to "true", the number is calculated continuously from the very first report page to the last in the report.

## 
Columned

After setting Columned  to "true",  you can predefine the coordinates for all objects in a report when exporting the report to a columned file such as Excel and CSV, which helps improve Report Engine's performance by saving the extra position calculating time during the export process. You can specify values of the following properties for each object to position them as you want in the output.

- Column Index, Row Index 

- Column Number, Row Number. You can set the two properties for charts, images, and UDOs. 

- Top Attach Column, Top Attach Row, Bottom Attach Column, and Bottom Attach Row. You can set the four properties for drawing objects.

Designer calculates the default values of these properties based on the position of each object in the report. Each time after you set Columned to "true" from "false", Designer recalculates the property values for all objects in the report and resets the values to the defaults (there is an exception: if both the Export to Excel and Export to CSV properties of an object are "false", Designer does not recalculate the values and instead preserves them as before).     

## 
No Page Break

When you export a report to Excel without page breaks, the column headings appear just at the top of the Excel spreadsheet and are not repeated throughout the report (the split pages are technically merged within the Excel sheet); while, if the report breaks to a new sheet, the page header displays once again.

However, exporting a report to an Excel file without page breaks could bring the following results and limitations:

- In the Excel output, only one page header panel and one page footer panel in a banded object can display in each sheet. Only the first banded page header and the last banded page footer  display in the output. As for tables, Report Engine only exports the first table header and the last table footer. 

- You cannot get a continuous table or banded object if the report contains other objects in horizontal locations. Report Engine exports all split parts of a horizontal table vertically. 

- Merging tables or crosstabs together extends the Excel sheet, which may cover other objects if they happen to be in the extended direction. Merging crosstabs together might extend the column/row index over the Excel sheet range, so you may lose the report part that is out of this range in the output. 

- If a whole merged crosstab gets quite large, it might cause an out of memory error during the export process. 

## 
Rows per Sheet

When you export a report to Excel, Report Engine does not separate the rows in the same page and exports them to different worksheets, thus the number of rows it exports to a worksheet may be greater than the number you specify for the Rows per Sheet property. For example, when you set Rows per Sheet to 100, Report Engine exports all content in the first page to the first worksheet, then it tests the number of rows the first page occupies in the first worksheet and determines where to export the next page.

- When the first page has less than 100 rows in the first worksheet, Report Engine still exports the next page to the first worksheet even when the number of rows in the first page and the next is greater than 100.

- When the number of rows in the first page is equal to or more than 100, Report Engine generates a new worksheet and exports the second page to the new worksheet.

## 
Style Group for Export

You can use the Style Group for Export properties  to preset a style group to the report tab for each export format. The Style Group for Export properties have higher priority than the Style Group property. However, if you do not specify a style group for an export format, the report output of this format applies the value that you specify for the Style Group property by default.

The Style Group for Export properties take effect in the following cases:

- Export or preview the report in Designer.

- Export the report in Page Report Studio.

- Run and advanced run the report or schedule to publish it to version/disk/email/FTP on Server.

When you select the View tab to preview a report tab  in Designer, Designer selects the value that you specify for the Style Group property in the Select Style Group dialog box by default. You can select another style group to apply to the report tab. In Designer view mode, if you further preview the view result in different formats or export it to different formats, the preview/output applies the style group of the view result, instead of the Style Group for Export property values.

Previous Topic  Next Topic
