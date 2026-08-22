---
title: "Report v23.4 Release Notes"
id: 44254222444685
section: "Report Designer v23 (Archive)"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/44254222444685-Report-v23-4-Release-Notes
updated_at: 2026-03-16T01:09:15Z
source_host: docs-report.zendesk.com
---
# 
Report v23.4 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Report v23.4. Subsequent updates are listed chronologically, most recent first. 

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

- v23.4 Service Pack 3 Resolved Issues

- v23.4 Service Pack 2 Resolved Issues

- v23.4 Service Pack 1 Resolved Issues

- v23.4 Feature Enhancements

- v23.4 Resolved Issues

- Known Issues

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

## 
v23.4 Service Pack 3 Resolved Issues (1/31/2024)

| Title | Case # | Change Description |
| --- | --- | --- |
| Banded Object with Multiple BPF After Upgrade | 04456578 | After upgrading from v15.6 to v23.3, Report now no longer overlaps the banded page footer (BPF) panels in your banded object. |
| Business View Based on Query and Imported SQL | 04502013 | Report now applies query-level parameter filters as expected, when you change a parameter value from All Values to some values, and if the report's business view combines an imported SQL statement and a query that wraps another imported SQL statement. |
| Call Stored Procedures Only Once | 04496410 | Server now calls stored procedures only once when you change cascading parameter values, or when the parameters sent by the front end to the engine don't follow the order of Stored Procedures' dependencies, if you create cascading parameters based on stored procedures and adjust the parameters order in your report. |
| Convert HTML Tag | 04481586 | Report now properly parses the  tags within a  tag in the content of your report objects, when you specify the Convert HTML Tag property to "true". |
| Data of Crosstab as Subreport | 04490270 | When you add a crosstab contained in a banded object as a subreport in another banded object in the primary report, Report now completely displays data of the crosstab in the primary report if the crosstab spans on several pages. |
| Delete Tabular Cells | 04487417 | Web Report Studio now removes the cell content only when you delete a tabular cell. |
| Display Date Type Parameter Values | 04453056 | Report now displays proper date type parameter values in reports in Designer, Web/Page Report Studio, and PDF, when the parameter values are within Daylight Saving Time while the OS date time is not, if you enable "Automatically adjust clock for Daylight Saving Time". |
| Display Scheduled Tasks | 04461952 | Server now displays all your scheduled tasks. |
| Has Border Property of Crosstab After Upgrade | 04456529 | Designer now retains the "true" value for the Has Border property of your crosstabs when you upgrade from v17 and earlier to v23.4 SP3. |
| Hyphen in Email Addresses | 04484189 | Server now supports the hyphen signs (-) in email addresses in the Schedule's Notification tab. |
| Insert Parameter Form Control | None | You can now always select the parameters you need and select OK in the Insert Parameter Form Control dialog box to create a parameter form control in your report. |
| JRotator in PDF Output | 04477758 | You can now get the same look for the JRotator object in your PDF output as when you preview it in Designer, when you select to generate charts and barcodes using vector graphics for the PDF. |
| Maximum Length Property of Chart in .xml Report | 03767760 | After you edit the Maximum Length property of a chart in an .xml report, Designer now correctly saves the property value into the report template when you save the report. |
| Open Export Dialog Box in JDashboard | 04478663 | JDashboard no longer displays an unknown service exception when you open the Export dialog box. |
| Open Linked Reports with Basic View Only | 04141597 | Page Report Studio no longer displays the Interactive View option when you open linked reports, as in the primary report. |
| Run Web Reports | 04485515 | You can now run reports in Web Report Studio without getting an Uncaught TypeError, when you set an expression as the Invisible property value to hide objects when there is no record. |
| Run Web Reports with Data Container Link | 04410141 | Web Report Studio now runs your report without displaying the ArrayIndexOutOfBoundsException error message, when you have set up the data container link between a table and its parent banded object. |
| Save Parameter Values as Default | 04497098 | You can now change parameter values and save them as the default in the Parameter Settings dialog box without getting a NullPointerException error message. |
| Search Parameter Values | 04148155 | Web Report Studio now displays search results as expected in the Enter Values dialog box, which you open from the Parameters panel or Enter Parameter Values dialog box. |
| Table Without Header in Accessible PDF After Upgrade | 04480433 | After upgrading from v15.6 to v23.3, Designer now properly adds a blank  tag for a table in your accessible PDF output when the table does not contain the table header row. |
| Time Zone in Advanced Run | 04393537 | Server now applies the JVM time zone to Datetime parameter values when you advanced run reports, if you don't set the default time zone in the server preference. |
| View Reports when Downloading Server Reports | 04121812 | You can now view reports as expected while navigating the server folder, when you download reports from Server in Designer. |
| Zoom Setting in JavaScript API | 04489758 | You can now use the URL parameter "jrd_zoom" to set the zoom percentage when opening page reports via the JavaScript API. |

## 
v23.4 Service Pack 2 Resolved Issues (12/30/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Add KPI to Web Report Using Existing Dataset | 03670192 | When you add a KPI component to a web report and apply an existing dataset in the web report that contains filter criterion to the KPI, Designer now no longer removes the filter criterion from the dataset. |
| Alternating Row Colors in Tables | 03928310 | Page Report Studio no longer applies alternating row colors to the summary row in tables, when you set Include Header and Footer to "false". |
| Convert HTML Tags | 03626661 | When you set the Convert HTML Tags property of a field to "true", Report can now properly parses the tags in the field content if the content contains the  tag and there isn't a  tag next to . |
| Copy Email Addresses when Scheduling | 03631057 | You can now copy email addresses when scheduling report tasks without getting an invalid email address error message. |
| Date Values in Excel Output | 03670618 | Server now displays the proper dates in the Excel output when the JVM time zone is EST. |
| Deliver Message on Bubble Chart | 03624583 | You can now use the bubbles in bubble charts to send and receive messages correctly. By default, current field and current value mean the bubble radius. |
| Display Date in Calendar | 03816959 | Web Report Studio now displays the proper date in the calendar when you select a calendar icon. |
| Display of Nested Banded Objects | 03635080 | When you insert a banded object into another banded object and set the On New Page property of a panel in the child banded object to "true", Designer now does not start the child banded panel on a new page if the current page is blank. |
| Display Receive Message Dialog Box | 03624583 | Designer can now display the Receive Message dialog box. |
| External Authorization with Case Insensitivity | 03613868 | Server can now get a JUser by calling getInsensitiveJUser(String submitter, String realmName, String userName) on jet.server.api.admin.SecurityAdminService with insensitive user name. |
| Filter for Same-Name Datasets | 03639074 | When two datasets in a page report have the same name, Designer now retains the filter criterion on each dataset after you edit the data component applying either of the two datasets. |
| Fully Display Button Text | 03626243 | After you publish web reports from v23.3, Web Report Studio now displays the Generate button fully as expected when you run the web reports for the first time. |
| Open Links in New Tab | 03928120 | Page Report Studio now displays the linked URL in a new tab when you select a link, regardless of whether it is a conditional link, if you set the link target to . |
| Overflow of Group Header Rows | 03928120 | The shading on the group header rows no longer overflows in Page Report Studio, when you zoom in or out on your report. |
| Preview Report Containing Field Displayed as Barcode | 03625709 | You can now correctly preview a report without Designer endlessly increasing the report pages, when you display a field in the report as Barcode and set the Convert HTML Tag property of the field to "true". |
| Run Page Reports | 03656968 | After upgrading from v13, Report now runs page reports without getting stack overflow, even if a query and a parameter have the same name. |
| Run Reports via HTTPS | 03471891 | You can now run reports using HTTPS when working with JRClient. |
| Run Scheduled Tasks Periodically | 03624598 | After you upgrade from v23.1.2, Server now runs scheduled report tasks periodically as expected when the reports use cascading parameters. |
| Save Catalog Containing Invalid Custom Measure | 03667621 | Designer now no longer adds a NullPointerException in log when you save a catalog containing a custom measure that references nonexistent business view element, instead, Designer displays a warning message at the time when you check the syntax of the custom measure. |
| Save Web Report in XML Using API | None | You can now save web reports in XML (.wls.xml) using API. |
| Tips in Line Charts | 03621357 | Web Report Studio now displays tip information as expected when you hover over data points in line charts. |
| Trigger Links on Bubble Charts | 03624583 | You can now trigger links on bubble charts in Web Report Studio and JDashboard. |
| Zoom Charts | 03621368 | Web Report Studio now displays the same result as Designer does when you zoom charts. |

## 
v23.4 Service Pack 1 Resolved Issues (11/30/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Access Scheduled Tasks of Organization Users | None | System admin can now see all scheduled public report tasks of organization users. |
| Align Barcodes to Right | 03555546 | After you publish page reports to a remote server, Server can now align barcodes to the right as expected in HTML output on Windows and in RTF and HTML outputs on Linux. |
| Get Scheduled Tasks via Web API | None | Server now includes the submitter in the returned content when you use the Web API - GET/myTasks/scheduled/list and GET/myTasks/scheduled/list/page - to get scheduled tasks. |
| Link to URL | 03570781 | Page Report Studio now displays the corresponding URL when you select a link, if the link contains ():=[]'. |
| Options for Embedding Fonts in PDF Output | 03521846 | You can now map fonts to TTF and embed specific TTF into your PDF output by adding the -Dlogireport.pdf.MapToTTF and -Dlogireport.pdf.EmbeddedFonts options to Server or Designer's startup file. |
| Preview and Export Report When Convert to HTML Enabled | 03621564 | You can now successfully preview and export a report in Designer, when you set the Convert HTML Tag property of a field in the report to "true" and the field does not contain real content after converting, for example, the field's content is: . |
| Publish Catalogs from Designer to Server | 03589944 | Designer now works as expected without hanging for a long time, when you publish catalogs from Designer to Server within an application server. |
| Relative Position in Page Report Studio | 03595983 | Page Report Studio now displays relative besides static and absolute in the default value list for the Position option, when the current position is relative. However, relative is no longer available in the value list after you apply static or absolute and reopen the dialog box. |
| Save Report to Another Catalog | 03596173 | When you save a report to another catalog, Designer now properly merges the resources the report applies into the target catalog. |
| Time Zone in Chart Tips | 03608665 | Web Report Studio now displays tips in the chart graph with the same time zone as that for the Date/Time labels on the X axis. |

## 
v23.4 Feature Enhancements (10/31/2023)

| Title | Description |
| --- | --- |
| Cache Data of Cascading Parameters | You can now specify whether you want to cache data of cascading parameters at both application level and parameter level to improve performance. See： Options Dialog Box Creating Parameters in a Catalog |
| Customizable Default Format for Boolean Data | You can now specify the default format for Boolean data by setting the Boolean Format property of a JDBC connection as True/False, T/F, or 1/0 according to your database system. |
| Define Catalog Object Security | You can now assign the four user permissions on the catalog objects in Catalog Studio: Create Children, Visible, Edit, and Delete. |
| Escape Formula for CSV | To mitigate vulnerability of your CSV output, Report now provides the new option - Escape Formula for CSV and enables it by default, allowing Report to add a tab character in the front of the content in any cell when the content begins with one of the following characters: "=", "+", "-", and "@". |
| Export to PDF/A Compliant Document | You can now export your report to a PDF/A compliant document and add attachments to the PDF. See Adding PDF Attachment to a Report. |
| More Components and Features in Page Report Template Editor | In the page report template editor, you can now insert special fields, images, page panels, TOC page panel, page breaks, and Expand/Collapse Group web controls into your report template, set their properties, drag components across page panels, and turn on the pageless layout mode by clearing the Page Layout property. |

## 
v23.4 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Add Group Column in Summary Table | 03323574 | After you hide a group column in a summary table and then add a new group column to the table via the Table Wizard dialog box, Designer now no longer hides the newly added group column and correctly displays data of the new column. |
| Apply First N to Time/DateTime Fields | None | Web Report Studio now displays proper data when you apply the First N filter to Time/DateTime fields, if your server profile time zone is different from the JVM time zone. |
| Buttons Applying the Property Web Action | 03296697 | You can now successfully add several buttons and apply the Property web action to all the buttons in a report. |
| Close Page Reports | 03325541 | Server now closes reports in Page Report Studio as expected when your user session expires. Server cancels page report running without displaying a NullPointerException error message. |
| Create Web Reports via URL | 03516950 | You can now create web reports through URL when the URL contains the jrd_datasources parameter. |
| Create Web Reports with Parameters | 03543828 | Web Report Studio now works as expected when you create a new report and specify a greater start date than the end date in the Enter Parameter Values dialog box. |
| DateTime Values on Chart X Axis | 03542127 | Web Report Studio now displays DateTime values on chart X axis as expected when the Server Profile and JVM time zone are different from the OS time zone. |
| Date Values in Filter Panel and Filter Controls | None | Web Report Studio now displays proper date values in the Filter panel and filter controls, when your server profile time zone is different from the JVM time zone. |
| Default Parameter Values in Available Value Lists | None | Server can now get the default parameter values from the available value lists in the Enter Parameter Values dialog box, when the parameters bind with Time/DateTime fields and your server profile time zone differs from the JVM time zone. |
| Display Chart Tips | 03542549 | Web/Page Report Studio now displays chart tips on the left when there is not enough space on the right. |
| Display Completed Tasks | 03383266 | Server now displays a large number of completed tasks faster in the My Tasks > Completed page. |
| Display Crosstabs in Library Components | None | Server now displays crosstabs in library components as expected, when the crosstabs contain no data or have data exceptions. |
| Display Parameter Form Control Values | 03439306 | After you export your report and refresh it, Report now displays the proper values of parameter form controls and the footer as expected instead of "0". |
| Display Parameter Values of DateTime Expressions | 03568689 | Server now displays proper parameter values of DateTime expressions in the value list for web reports, when the JVM time zone is different from the time zone you set in your server profile. |
| Display Permission UI in Cluster | None | Server now displays the permission UI as expected after you restart clustered servers several times, when the number of nodes to share memory is less than the number of nodes in your cluster. |
| Enhance Query Filter Performance with Large Data | 03064934 | Web Report Studio now enhances the performance of the Query Filter dialog box involving a large number of data as follows: No longer displays the Page Unresponsive error message when loading the filter data. Displays the result as expected when you search for a value. Displays the Select Values dialog box as expected when you select the "in" operator and select More in the value list. |
| Export Reports to Excel | 03463883 | Report now exports reports to Excel without displaying an ArrayIndexOutOfBoundsException error message, when your report template has more than 127 group levels. |
| Export to Excel When Convert to HTML Is Enabled | 03370127 | Designer now no longer displays the ClassCastException when you export a report to Excel, if you set the Convert HTML Tag property of a field in the report to "true". |
| Export to .xls Excel File | 03370127 | Report now no longer loses any data in your Excel output, when you export the report to an .xls Excel file. |
| Expression Value for Date/Time/DateTime Parameters | None | For Date/Time/DateTime type parameters, Server now shows the calculated values of expressions: In the drop-down value lists of parameter (form) controls in Web Report Studio. In the input boxes when you edit the expression values. As the tips for the expression values. |
| Expression Value in Parameter UI | None | Web Report Studio now displays proper values of Date type expressions in the parameter UI and the default value of a DateTime type expression the same as the selected value in the calendar, when the JVM time zone is related to a Daylight Saving Time and different from the OS time zone. |
| Field Padding After Converting HTML Tags | 03502583 | Report now properly applies the padding you specified to a DBField after converting the HTML tags in the content of the field, when you set the Convert HTML Tag property of the field to "true". |
| Filter Time/DateTime Fields | None | Web Report Studio now displays proper data when you filter a Time or DateTime field using the shortcut menu or a filter control, if you enable Push Down On-screen Filter Values and your server profile time zone is different from the JVM time zone. |
| Filter with Time Values | None | Web Report Studio now displays the proper data when you filter with a time value. |
| Formula Calling UDF | 03551369 | Report now properly parses the user defined functions (UDF) you define and returns correct values to the formulas calling the UDFs. |
| Group-By Field Values of Date Type | None | Web Report Studio now displays the proper date values of group-by fields of the Date type, when your server profile time zone is different from the JVM time zone. |
| Next Run Time for Scheduled Tasks | 03567887 | Server can now run scheduled tasks once every two or more weeks and show the next run time as expected. |
| Open .xls Excel Output File | 03370127 | You can now successfully open the .xls Excel output file exported from Report, when the Excel file contains a large amount of rich text cells. |
| Parameter Value Calculated by Expression | None | When you use an expression to specify the value for a Date/Time/DateTime parameter, Report now displays the date/time calculated by the expression in the parameter's value list rather than the expression for better user experience. |
| Parameter Values in Parameter Settings Dialog Box | 03568597 | Server now displays the proper values of parameters in the Parameter Settings dialog box, when the parameters are referenced by session variables. |
| Parameter Values When Applying Daylight Saving Time | 03355975 | Report now correctly displays data in your report that contains DateTime parameters, when your operating system applies daylight saving time. |
| Performance Enhancement with Multiple Subreports | None | Server now enhances the engine performance when your report contains multiple subreports and a subreport further contains a subreport. |
| Preview Parameter Report in Designer | 03369696 | Designer now properly displays the Enter Parameter Values dialog box when you preview a parameter report, if you referenced the parameter in the JSON data source the report applies and bound the parameter with a column in the same JSON data source. |
| Proper Text Display Within  Tags | 03521846 | Page Report Studio now displays text without extra spaces when the text contains double  tags. Text in bold no longer covers other text within a  tag in PDF outputs. |
| Publish Reports to Server in Designer | 03468771 | You can now publish catalogs and reports to Server in Designer, when folder names in the target server path contain spaces. |
| Remove Illegal Email Addresses from Scheduled Tasks | 03467467 | You can now remove illegal email addresses when updating scheduled email tasks. |
| Remove Unavailable File Reference | 03428312 | Report no longer references %JAVAHOME%\lib\tools.jar that is not available since JDK 9 in the additional classpath in setenv.bat when your Designer is installed using JDK 9 or later. |
| Repeated DSException in Engine Log | 03305992 | Report no longer displays the error message "DSException: The cursor is already closed" many times in engine.log. |
| Resize Bookmark Setting Dialog Box | 03594351 | You can now resize the Bookmark Setting dialog box along with the table within it and the table columns in the dialog box as expected in Web Report Studio. |
| Resize Tables with Dataset as All Resources in Business View | None | You can now resize tables and do other actions in Web Report Studio without getting an exception, when you set the dataset type to "All Resources in Business View". |
| Run Bursting Reports to Email | 03465948 | Server now sends bursting reports to valid email addresses, when the recipient field contains a Null value which is an invalid email address. |
| Run getScheduledTasks in Web API | 03425298 | Server now runs getScheduledTasks in the Web API without displaying a NullPointerException error message, when you do not set the logonType. |
| Run Reports in Page Report Studio with Incomplete Preference | None | After upgrading from V16, Server can now run reports in Page Report Studio in an integrated environment, even if your common server preference setting is incomplete. |
| Run Reports via HTTPS URL | 03471891 | You can now run reports using the HTTPS URL when the Server port is not specified. |
| Run Scheduled Email Tasks | 03312553 | Server now sends reports to valid recipients and no longer runs scheduled email tasks repeatedly, if the mail sender is invalid. |
| run.jsp | 03542031 | Server run.jsp can now handle the parameters originally sent to tryView.jsp, including non-string parameters you set in the session. |
| Search Parameter Values | 03463454 | In the Enter Parameter dialog box, you can now click and write in the whole extended search area when a parameter value is long. |
| Specify Parameter Values | None | Web Report Studio now displays the parameter values of Date/Time/DateTime type parameters as you specify, if you don't set the parameters' User Defined Format and the JVM time zone is different from that in the Server Profile. |
| Time Zone in Filter Dialog Box | 03543671 | Server now displays date fields in the filter dialog box using the same time zone as in the report. |
| Time/DateTime Values in "Go To" Filter Panel | None | Web Report Studio now displays the proper Time/DateTime values in the "Go To" Filter panel, when your server profile time zone is different from the JVM time zone. |
| TTF in PDF Output | 03466206 | Report now correctly displays the True Type Font in your PDF report output, when the TTF applies PostScript outlines. |
| Value Time Zone in Parameter (Form) Controls | None | Server now displays values of type-in DateTime parameters using the server profile Timezone in parameter (form) controls in PDF outputs and values of Date type bind column parameters using the JVM time zone in parameter (form) controls in Web/Page Report Studio, when your server profile time zone differs from the JVM time zone. |
| Verification Message for Page Report Dataset Filter | 03543828 | Server now displays the proper verification error message when you specify the wrong parameter values for the dataset filter in the page report wizard. |

## 
Known Issues

Report data cut off in PDF due to PDF page size limitation

When you export a report to PDF, some data of the report are cut off in the PDF output when the report contains a large amount of data, and you have applied continuous page mode to the report or set the page size to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

Unsupported go-to action when using dynamic formulas on chart

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula on the value axis and the formula contains group information.
