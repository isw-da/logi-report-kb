---
title: "Logi Report v19.2 Release Notes"
id: 9898557594903
section: "Release Notes for Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9898557594903-Logi-Report-v19-2-Release-Notes
updated_at: 2023-02-01T03:17:41Z
---

# Logi Report v19.2 Release Notes

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements)

# Logi Report v19.2 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Logi Report v19.2. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [v19.2 Service Pack 3 Resolved Issues](#h_01GQVR3Y6HPQR27NHND5HWK2F2)
* [v19.2 Service Pack 2 Resolved Issues](#h_01GN97WYHB3GKMCCQQEWJPA62S)
* [v19.2 Service Pack 1 Resolved Issues](#h_01GJY3WB651R288ZTGTC1JW75Q)
* [v19.2 Feature Enhancements](#Feature)
* [v19.2 Resolved Issues](#Resolved)
* [Known Issues](#Known)

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

## v19.2 Service Pack 3 Resolved Issues (1/31/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Basic View of Page Report Studio | 02267822 | Page Report Studio no longer displays the Resource View and Toolbox panels when you run reports in the Basic View mode for the first time. |
| Color from DBField in Chart Conditional Fill | 02440354 | Designer now properly retrieves colors from the DBField you select to control the color setting of a chart conditional fill, when the chart is inside a banded object. |
| Display Page Reports | 02276235 | Report now displays proper data in your page report, when a formula references *\_\_currentfield* and applies in conditional formatting. |
| Invisible Column in Horizontal Table | 02415705 | After you set the Autofit property of a column in a horizontal table to "true", Report now does not display the column when the constant level formula you apply to control the column's Invisible property returns "true". |

## v19.2 Service Pack 2 Resolved Issues (12/30/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Exceptions with Cluster | None | You can now run reports in a Server cluster without getting NullPointerException and UnmarshalException error messages, when Cluster Memory Storage Number of Copies is less than the number of active servers in the cluster. |
| Formula Using "select-case" Statement | 02433713 | Designer now correctly parses formulas containing the "select-case" statement, without generating an InvocationTargetException error. |
| Order By Property on Web Report Crosstab | None | You can now use the Order By property of the column/row field in web report crosstabs to specify the field by which you want to sort the crosstab column/row header. |
| Page Report Studio Profile | 02267822 | Server now applies your v16.1 Page Report Studio profile properly. |
| Refresh Images in Linked Reports | 02423021 | Web Report Studio now displays images properly in linked reports in the Whole Window when you refresh the browser, even after the primary report session expires. |
| Run JavaScript API Demo | 02278416 | You can now run the JavaScript API demo and open page reports as expected after applying the patch JIP\_S\_1912\_sp2\_202211161159.jar. |
| Specify Parameter Values | None | You can now specify parameter values using jrs.param and jrd.param in the session variable and JavaScript API. |

## v19.2 Service Pack 1 Resolved Issues (11/30/2022)

| Title | Case # | Change Description |
| --- | --- | --- |
| Apply Server-Level Profile Properties After Upgrade | 02267822 | Server now applies your existing server-level profile properties for Page Report Studio properly, when you upgrade from v16.1. |
| Display Linked Web Reports Faster | 02279906 | Server now displays linked web reports faster, by calling getDynamicRscUsedStatus only once, removing unused on the fly formulas, and parsing and compiling on the fly formulas at the report level instead of the data component level. |
| Display Page Reports and Shortcut Menus Faster | 02278416 | Page Report Studio now displays page reports and shortcut menus faster, after you upgrade Server from v18.2. |
| Display Scheduled Report Tasks | 02275559 | Server now displays your scheduled report tasks on the My Tasks page, even if it cannot calculate the next run time of a periodically run schedule during the startup. |
| Execute Expressions When Data Cache Is Disabled | 02280893 | Logi Report now properly executes the expressions you create to control object properties, when you disable caching data for the datasets to which the corresponding data components apply (set the Cache property of the data components to "false"). |
| NLS Support in Renamed Reports | 02279356 | Renamed reports now support NLS when you save them in Web/Page Report Studio. |
| Node Pattern of Line Chart | 02394823 | After upgrading from v10 to v17.1 SP3 and later, Logi Report now properly applies the node pattern you have defined for a line chart. |
| Open Report in Designer | 02279390 | Designer now opens a report in a reasonable amount of time by compiling dynamic formulas of the same scope at the same time, instead of sequentially. |
| Open the Format Line Dialog Box | 02394823 | After upgrading Designer from v10 to v17.1 SP3 and later, you can now open the Format Line dialog box to edit the formatting of a line chart. |
| Print Page Header/Footer and Print Grid Lines | 02273214 | Server now prints page header/footer and grid lines in the Excel output as expected when you schedule report tasks via the API. |
| Report Style Group in Server Profile | None | You can now access the Report Style Group in the Common tab of both Web/Page Report Studio profiles, as changes you make in the Report Style Group affect both profiles. |
| Run Dashboards | 02265130 | Server now runs sample dashboards without displaying a ClassCastException error message, when you apply a custom JDashboard profile. |
| Run Reports | None | Server now runs reports of an earlier version without displaying a ClassCastException error message. |
| Select On-screen Filter Values in Linked Reports | 02275508 | You can now select values in on-screen filters when opening linked page reports in a new window, without getting a NullPointerException error message. |
| Session Variables | None | Session variables now work when you schedule report tasks via the web API. |
| Set Language in Run Report API | 02268240 | Server can now apply the Spanish language to the waiting screen correctly, when you set the "jrs.language" parameter in the run report API. |
| Switch Between Portrait and Landscape | 02386323 | You can now switch between Portrait and Landscape in the Page Properties dialog box in Page Report Studio, when the language you are using utilizes a comma (,) as a decimal point. |
| Value for the "currentfield" Variable | 02254842 | Logi Report now properly returns values to the "currentfield" variable, when you reference the variable in the formula for controlling the Foreground Color property of a data field and define a condition based on the variable in the conditional formatting of the field as well. |
| Value Synchronization Among Filter Controls | 02394870 | When you select a value in a filter control, Web Report Studio refreshes to display related filter control field values and dims unrelated filter control field values. |

## v19.2 Feature Enhancements (10/31/2022)

| Title | Description |
| --- | --- |
| [Create and Export Reports in Current Window](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements#NewWindow) | Server can now display reports in the current window, when creating reports, opening reports, and viewing exported outputs, by setting the new option Run and Export Report in the New Window in server preferences. |
| [Custom Page Layout for Different Report Outputs](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements#PageLayout) | You can now customize the page layout of your report for different outputs to display the outputs either in multiple pages or a single page, using Designer and Web/Page Report Studio. See [Specifying the Page Mode of a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#SpecifyMode). |
| [Customize Mappings Between Current Field and Corresponding Field in Link Filter](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements#FieldMapping) | You can now customize the mappings between the current field/category/series of the primary report and corresponding field of the linked report using fields of different names, to create more dynamic link filters between the two reports with the Current Field/Category/Series = Corresponding Field condition, when you link a report to another report in both Designer and Web Report Studio. See [Adding Links in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report#MapField). |
| Enhanced Logging | Logi Report updates the logging implementation to use the SLF4J (Simple Logging Facade for Java) solution, enabling you to migrate to another logging framework easily. See [Configuring the Logging System](https://devnet.logianalytics.com/hc/en-us/articles/5735516331543-Configuring-the-Logging-System). |
| [New Formula Functions to Get Group-by and Sort-by Columns](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements#Function) | You can now use the new built-in functions, *currentGroup()*, *currentGroupLevel()*, *getAllGroups()*, *getAllSortColumns()*, *getGroupBy()*, and *getSortBy()*, to get the group-by and sort-by columns of tables and banded objects in your reports, using both Designer and Web Report Studio. See [Appendix 1: Formula Functions.](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions#currentGroup) |
| [Remove Users' Shared Reports](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements#SharedReport) | Server administrators can now remove copies of reports that users have shared. See [Managing Users' Shared Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741463728407-Managing-User-Accounts#SharedReport) in the *Logi Report Server Guide*. |
| [Template Editor](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements#TemplateEditor) | Server now provides a template editor called Logi Report Studio. You can use it to edit page report templates. See the following links in the *Logi Report Server Guide*:  * [Enabling and Accessing Template Editor Logi Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/9905923782039-Enabling-and-Accessing-Template-Editor-Logi-Report-Studio) * [Working with Logi Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/9905923717783-Working-with-Logi-Report-Studio) * [Logi Report Studio Dialog Boxes](https://devnet.logianalytics.com/hc/en-us/articles/9905923105431-Logi-Report-Studio-Dialog-Boxes) |
| [Use LDAP Server and Triggers via Rest API](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements#API) | You can now configure your LDAP Server and manage triggers using the Rest API. See [Using JavaScript API to Embed Server Console and Reports in Your Applications](https://devnet.logianalytics.com/hc/en-us/articles/5741394606103-Using-JavaScript-API-to-Embed-Server-Console-and-Reports-in-Your-Applications-) in the *Logi Report Server Guide*. |
| [Use Text Box in Web Report and Business View-Based Page Report](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements#TextBox) | You can now insert text boxes in web reports and business view-based page reports, using Designer. Server now displays text boxes in Web Report Studio as it does in Page Report Studio. |
| Value Time Zone in Built-in Functions | You can now retain the time zone of Date/Time/DateTime field values in built-in functions by setting `CustomOffset=true&FunctionApplyOffset=true` in the URL of running reports. |

## v19.2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Aggregate On in Tables | 02100465 | Your aggregate report no longer overlaps the fields in the group footer when you aggregate on a table column in a group above table in Page Report Studio. |
| Allow Showing Unencrypted Value Property of Parameters | 02177645 | You can now save the Allow Showing Unencrypted Value property value of parameters into your .xml catalog. |
| Auto Fit Property in .xml Reports | 02134452 | Designer can now properly save property values into report templates after you edit the Auto Fit property of table columns in .xml reports. |
| Cached Reports Display | 02132979 | Server no longer displays reports multiple times in the Cached Reports list on the Server Console > Administration > Configuration > Cache > Report Cache page. |
| Call runReport API | 02093353 | Server now passes ParamDesc to the engine when calling the runReport API. |
| Change Default Profile | 02262757 | Server no longer changes the default profile for Web Report Studio, when you change the default profile for Page Report Studio in the Server Console > Administration > Server Profile > Customize Profile page. |
| Chart Legend Entry Labels with TTF | 02246933 | Logi Report now properly displays the chart legend entry labels when you apply TTF to the labels and set their Word Wrap property to "true". |
| Display Long Email Addresses When Scheduling to Email | 02122515 | Server now displays a long list of email addresses in the To box properly when you schedule report tasks to email. |
| Dynamic Formula Referencing Custom Aggregation | 02196180 | Designer no longer displays an error message when you preview a report containing a dynamic formula that references a custom aggregation, when the custom aggregation references another dynamic formula. |
| Edit .xml Report in Designer | 02178031 | Designer now automatically adds the ModeContainer tag into your .xml report template file if it is missing, to ensure you can edit the report. |
| Export Banded Page Report | 02074970 | You can now properly export a page report containing a banded object, when you have set the Convert HTML Tag property of a DBField in the banded object to "true". |
| Formulas After Upgrade | 02183104 | Report Customers upgrading from v14 to v19 can now return correct formula values when the formula references two functions as *func1() || func2()*. |
| Go to Detail with Automatic Cache | 02142069 | Server no longer displays the IllegalStateException error message, when you go to detail from bench charts in Web Report Studio, and if you enable Automatic Cache on Server. |
| Horizontal Alignment of DBField Content | 02247507 | Logi Report now properly displays the content of a DBField when you set its Horizontal Alignment property to "right". |
| Image Display in Web Report Studio | 02244744 | Web Report Studio now displays images in banded objects properly when you control the images using formulas. |
| Memory Leaks from SortGrpNodeEngine | 02190949 | Memory leaks are no longer created by SortGrpNodeEngine in Server. |
| Name Pattern in Dynamic Connections | 02158658 | Server now applies the Name Pattern property value in dynamic connections when running web reports using Advanced Run. |
| Object Formatting | 02197075 | Designer no longer removes the formatting you have specified for an object when you select the Up and Down buttons to move the object in the Report Inspector tree. |
| Object Order in the Report Inspector Tree | 02256389 | Designer now displays objects in the Report Inspector tree correctly according to their display sequence in a report, after you move the objects to back or front. |
| Open Formula Reports After Upgrade | 02121304 | You can now open reports created using v17.1 Update 1 that contain formulas, after upgrading Designer to v19 SP1. |
| Parameter Display | 02178031 | Logi Report no longer duplicates the same parameter in the Enter Parameter Values dialog box, when you customize the parameter display order and then change the parameter names to uppercase or lowercase. |
| Query Filter in QBE Format | 02137657 | Designer now correctly applies query filters you created using the QBE format, when the query contains columns that have the same name in the JSON file or database and the filter condition is based on one of the columns. |
| Refresh XML Connection in .xml Catalog | 02238519 | Designer now properly fetches columns from your XML data source in an .xml catalog, after you refresh the XML connection in the catalog and save the catalog. |
| Report Conversion | 02149005 | Server can now convert reports from v18.3 to v19.2 successfully without displaying the NullPointerException error message, when a dashboard has no versions. |
| RMI API | 02195435 | RemoteReportServerToolkit.getRemoteServerStatus(serverHost, serverPort) now returns proper values when Server is running or shut down, when connecting to a standalone Server by RMI. |
| Run Linked Reports | 02138124 | Web Report Studio now displays the proper linked report without displaying the "Uncaught TypeError" message, if a field value is null, when you select the Stock button. |
| Run Scheduled Tasks | 02138524 | You will now see performance improvements when running multiple threads in scheduled tasks. |
| Save As Using API Method | 02191826 | After upgrading to a version later than v18.3, you can now properly save a report as a new one using Design API method. |
| Script Files for MySQL | 02247332 | Server now provides appropriate script files for different MySQL versions in `<install_root>\script_files\create_new_tables`. |
| Scroll down Page Report to Next Page | 02243081 | Page Report Studio now displays the next page when you scroll down to the bottom, no matter whether the page report has a horizontal scrollbar. |
| Specify External dbconfig.xml via -D Parameters | 02146307 | You can now specify an external dbconfig.xml by adding -D parameters in an integrated environment. |
| Title in Accessible PDF | 02173191 | You can now see the correct Title property in PDF Document Properties when you export a report to an accessible PDF. |
| Update Report Description via Web API | 02248668 | Server no longer changes a report status when you update the report description using "PUT node" in the Web API. |
| Update Time of Scheduled Tasks via API | 02245732 | You can now update the time condition of scheduled report tasks using "PUT modifyScheduledTask" in the API. |
| Wrapped Field Content in Crosstab | 02185743 | Logi Report now properly displays the content of a field in a crosstab, when you set the Word Wrap property of the field to "true". |

## Known Issues

**Report data cut off in PDF due to PDF page size limitation**

When you export a report to PDF, you will find that in the PDF output, some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action when using dynamic formulas on chart**

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version.

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898540229783-Logi-Report-v19-2-Enhancements)
