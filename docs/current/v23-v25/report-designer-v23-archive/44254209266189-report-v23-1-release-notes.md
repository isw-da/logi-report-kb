---
title: "Report v23.1 Release Notes"
id: 44254209266189
section: "Report Designer v23 (Archive)"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/44254209266189-Report-v23-1-Release-Notes
updated_at: 2026-03-16T01:09:20Z
source_host: docs-report.zendesk.com
---
# 
Report v23.1 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Report v23.1. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

- v23.1 Service Pack 3 Resolved Issues

- v23.1 Service Pack 2 Resolved Issues

- v23.1 Service Pack 1 Resolved Issues

- v23.1 Feature Enhancements

- v23.1 Resolved Issues

- Known Issues

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

## 
v23.1 Service Pack 3 Resolved Issues (4/28/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Display Columns of Parameters | None | Web Report Studio now properly displays columns of parameters, without exposing the bind columns while the report loads. |
| Display Linked Report From Pie Chart | 02560484 | Web Report Studo can now display the linked report after you select a pie chart, when the pie chart has only one value and the Angle Y property is set to 60. |
| Drag Library Components in Dashboards | 02559248 | You can now drag library components in dashboards, even if the templates of the library components have non-normal cases. |
| Merge Catalogs Using API | None | You can now successfully merge catalogs that contain user-defined formula functions (UDF) using an API. |
| Parameter Control Containing Boolean Parameter | None | Report now correctly displays a checkbox for the parameter control containing a Boolean parameter. |
| Rename Resources in Cluster | 02580168 | You can now access reports and catalogs from other clustered servers, after you rename them or their folders on a clustered server in a cluster. |
| Server Security Enhancements | None | We have enhanced the Report Server security. |
| Value Display in Pie Chart | 02576067 | Web Report Studio now displays the value of each pie slice on the slice as expected. |

## 
v23.1 Service Pack 2 Resolved Issues (3/30/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Bind Parameter with SQL Column | None | Designer now properly displays columns in the imported SQLs for you to bind with a parameter, if you have selected a query containing tables obtained from imported SQLs as the data source for the parameter. |
| Display Fields in Uppercase in Table Header | 02505891 | When viewing web reports in Web Report Studio or using the JavaScript API, Server now displays fields in uppercase in the table header as expected when you use formulas to return the uppercase of the fields, if there is no data in the table. |
| Distinct On Field of Aggregation Object | 02552002 | Designer now properly handles the Distinct On fields you specified for business view aggregation objects, when you save them into an .xml catalog file. |
| Filter Date Fields | 02491724 | You can now filter date fields using the Filter dialog box in Page Report Studio. |
| Password Synchronization in Cluster | 02510804 | You can now sign in to a clustered server without restarting it after you change your password on another clustered server. |
| Use Boolean-type Parameter to Control Another Parameter | 02484011 | You can now use a boolean-type parameter to refresh the value list of a bind column parameter in a parameter form control in Web Report Studio. |

## 
v23.1 Service Pack 1 Resolved Issues (2/28/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Change Parameter Values in Web Report Studio | None | Web Report Studio now displays proper chart data when you change parameter values in parameter controls. |
| Edit Reports via Wizard in Web Report Studio | 02480434 | You can now edit reports using the wizard in Web Report Studio, when filter sub-expressions reference parameters. |
| Replace Old Version for Publish and Schedule | 02487880 | Server now deletes old versions of reports as expected when you publish reports using the Designer or Server UI or schedule tasks via the API, with the archive policy of Replace Old Version. |
| Save Button in Business View Editor | None | Designer now enables the Save button in the Business View Editor dialog box, after you edit the union query for the business view and select OK in the Query Editor dialog box. |
| Union Query for Business View | None | Designer now properly generates the SQL statement for the BV query included in the union query of a business view when it contains incomplete join information, after you reopen the Query Editor dialog box for the BV query and select OK and then save the catalog. |

## 
v23.1 Feature Enhancements (1/31/2023)

| Title | Description |
| --- | --- |
| Background Color Transparency | When specifying the Background property for labels and fields in Designer and Web/Page Report Studio, you can now apply a transparent background color when customizing the color via dialog box or by typing an RGBA color value. See: Label Properties DBField Properties Formula Field Properties Parameter Field Properties Special Field Properties Summary Field Properties |
| Bar Chart Support in Report Studio | You can now create and update bar charts in the page report template editor Report Studio. See Working with Report Studio in the Report Server Guide. |
| Customize Chart Legend Entry Labels | You can now customize legend entry labels for values that meet specified conditions, when defining advanced single color conditional fill in a Bar, Bench, Line, Pie, or Donut chart. See: Applying Conditional Color Fills to Charts Edit Conditions and Label Dialog Box Label Editor Dialog Box |
| Customize Profile in REST/WEB API | Server now supports all Customize Profile properties in the REST/WEB API, including Common, Web Report Studio, Page Report Studio, and JDashboard properties. |
| Join Data with Branches for Business View | You can now join data for a business view by defining parent-child relationships between the tables the business view applies using the new Branch Editor. This new join approach enables you to get a different dataset for the business view, as compared to the dataset generated by using traditional joins. See Creating Branches for a Business View. |
| Manage Web Report Bookmarks | You can now manage bookmarks of web reports in the My Bookmarks folder on the Resources page of Server Console. Administrators can also manage other users' bookmarks. See the following topics in the Report Server Guide: Managing Web Report Bookmarks Managing Users' Web Report Bookmarks |
| Performance Improvement for Oracle Stored Procedures | The Oracle stored procedures you add into a catalog can now apply the setFetchSize property setting in the JdbcDriverConfig.properties file, resulting in improved performance. |
| Remove Duplicate Legend Entry Labels | You can now use a new property Show Duplicate Items on chart legend. Report sets it to "false" by default, to remove duplicate labels from the legend, so your reports look better when a chart applies conditional fill. |
| Run/Create Reports on Server Console in Same Window | If you clear the Create and Export Reports in New Window property in the Customize Server Preferences dialog box and run/create reports from the Server Console, Server now returns to the previous server page when you exit Web/Page Report Studio or cancel the report wizards. |
| Specify New Properties to Improve Report Appearance | You can now use more properties on the Text Box and some Web Control objects to enhance the look and feel of your reports. You can also specify these properties in the CSS styles you apply to the reports. See: Filter Control Properties Label Properties Multi-Value Container Properties Parameter Control Properties Parameter Form Control Properties Text Box Properties |
| Union Query for Business View | You can now create a union query for a business view when defining the business view either in Designer or using API, so each report applying the business view can have their own SQL query that is built dynamically at runtime. See Applying Union Query to a Business View. |

## 
v23.1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Apply Customized Server Profile to JavaScript Demo | 02436215 | Server now applies the new profile that you create on the Administration > Server Profile > Customized Profile > Web Report Studio tab, when you run web reports using the JavaScript demo. |
| Apply Filter Value to Linked Report | 02429477 | After you change the value in a filter control in a web report, Web Report Studio now displays the linked report in Excel with the correct filter value the second time you select the link, when you set jrs.result_file_name in the linked URL. |
| Basic View of Page Report Studio | 02267822 | Page Report Studio no longer displays the Resource View and Toolbox panels when you run reports in the Basic View mode for the first time. |
| Batch Tools in Designer | 02445752 | You can now properly run the batch tools included in the bin folder of Designer. |
| Bookmark Web Reports with Null Parameter Values | 02416660 | You can now bookmark web reports without getting a NullPointerException error message, when parameter values contain blank or Null strings. |
| Cluster Scheduler Lease | 02190949 | Server cluster scheduler lease now always works properly regardless of errors in the monitor thread. |
| Color from DBField in Chart Conditional Fill | 02440354 | Designer now properly retrieves colors from the DBField you select to control the color setting of a chart conditional fill, when the chart is inside a banded object. |
| Convert HTML Tag Property Controlled by Formula | 02275016 | Designer now correctly applies the Convert HTML Tag property of a DBField according to the return value of the formula you specify to control the property. |
| DBField Content | 02275016 | Designer now properly displays the content of a DBField across pages, when you set the field's Convert HTML Tag property to "true" and the content does not contain HTML tags. |
| Display Fields in Header | 02412856 | Report now displays proper field data in the header of all the pages in a report. |
| Display Page Reports | 02276235 | Report now displays proper data in your page report, when a formula references __currentfield and applies in conditional formatting. |
| Display Table Outer Border | 02244562 | Web Report Studio now displays the right outer border properly when you select a table, after you change the table from invisible to visible. |
| Display Values in Filter Controls for Multiple Components | 02417680 | Server now displays all field values in a text list filter control for all the components in a web report, when the components use different datasets but use the same business view. |
| Display/Export Print Time in Page Reports | 02417059 | Report now properly displays and exports the special field Print Time in page reports. |
| Dynamic Formula in Crosstab | 02426491 | Designer now properly generates the crosstab, when you add a dynamic formula used as Group on the column or row header of the crosstab. |
| Enhance Memory Usage | 02411875 | Server now manages memory more efficiently, for better performance. |
| Error Messages When Upgrade | 02273122 | Report no longer generates unnecessary log messages when you upgrade from v15.6 to v19.1 SP2. |
| Excel Output | 02244396 | Report now no longer duplicates the content of a field in the Excel output, when you export a report to Excel using Report Format. |
| Expression Controlled Property in Duplicated Data Container | 02178031 | When you copy a data container that has properties controlled by expressions and preview the report, Designer now removes the expressions that are invalid in the context of the duplicated data container and properly displays the report instead of producing an error message. |
| Formula for Comparison | 02439782 | Designer now displays expected report result, when you compare two strings using a formula in the report and one of the strings was created by adding a few strings. |
| Formula Name Containing "CF_" | 02455688 | Designer now properly parses normal formulas the names of which start with "CF_", rather than treating them as conditional formatting formulas. |
| Format Page on Demand | 02267206 | Server now clears Format Page on Demand in a user's Preference as expected when you clear it in Server Profile. |
| Invisible Column in Horizontal Table | 02415705 | After you set the Autofit property of a column in a horizontal table to "true", Report now does not display the column when the constant level formula you apply to control the column's Invisible property returns "true". |
| Object Layout | 02432596 | When objects at the bottom of a banded panel cannot completely display on the current page, they now no longer overlap with the objects placed under them on the next page, when you preview the report in Designer, run it in Web/Page Report Studio, or export it to PDF. |
| Open Report from Current Page Report with Parameters | 02438504 | Page Report Studio now passes parameter values successfully when you open another report from the current report, if parameter values contain spaces or special characters. |
| Parameter Display Order on Server | 02429194 | Server now displays parameters in the Enter Parameter Values dialog box in the order you defined using Designer, even when there are cascading parameters. |
| Performance of Getting Completed Tasks via Web API | 02432870 | Server now improves the performance of using the Web API to get thousands of completed scheduled tasks. |
| Publish to Server | 02241579 | Server can now display the server resource tree and publish your reports successfully when you publish to Server. |
| Remove Temporary Files | 02411698 | Report now removes temporary files as expected, after generating them when you export reports to Column Format XLSX Excel. |
| Report Session Timeout with Dashboard as Server Home Page | 02438635 | Server no longer displays an error message "The report session has expired", after you set a dashboard as the Server home page and restart Server. |
| Save and Run Page Reports as .xml | 02434292 | After you sort a banded object by a field in a page report and save the report in .xml format, Server now runs the new report successfully. |
| Schedule Tasks via Web API | 02419673 | Server now saves/updates multiple ReportEmails objects and applies the "useSMTPAccount" property of the successfulTaskEmails/failedTaskEmails objects in a scheduled task, when you submit the scheduled task through the web API. |
| Schedule to Email in PDF Attachment | 02417167 | Server now retains the "Generate charts and barcodes using vector graphics" selection for Attachment in PDF Format on the To E-mail tab, when you reenter the Schedule dialog box. |
| Schedule Weekly Tasks via REST API | 02448385 | You can now set the period value you want when you create weekly tasks for Server using the REST API. |
| Search in Select Field Dialog Box | 02415173 | The search bar now works properly in the Select Field dialog box for the Filter panel in Web Report Studio. |
| Update compile_tool.bat | 02421269 | Server now updates compile_tool.bat in \help\samples\APISecurity\SSO\compile_tool.zip to refer to jakarta.servlet.jsp-api-3.0.0.jar and jakarta.servlet-api-4.0.4.jar instead of servlet.jar. |
| Update Waiting Image | None | You can now update the loading status image of the waiting page for opening reports. |

## 
Known Issues

Report data cut off in PDF due to PDF page size limitation

When you export a report to PDF, some data of the report are cut off in the PDF output when the report contains a large amount of data, and you have applied continuous page mode to the report or set the page size to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

Unsupported go-to action when using dynamic formulas on chart

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula on the value axis and the formula contains group information.
