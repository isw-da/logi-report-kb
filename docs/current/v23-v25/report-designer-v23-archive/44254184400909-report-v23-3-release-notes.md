---
title: "Report v23.3 Release Notes"
id: 44254184400909
section: "Report Designer v23 (Archive)"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/44254184400909-Report-v23-3-Release-Notes
updated_at: 2026-03-16T01:09:17Z
source_host: docs-report.zendesk.com
---
# 
Report v23.3 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of Report v23.3. Subsequent updates are listed chronologically, most recent first.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

- v23.3 Service Pack 3 Resolved Issues

- v23.3 Service Pack 2 Resolved Issues

- v23.3 Service Pack 1 Resolved Issues

- v23.3 Feature Enhancements

- v23.3 Resolved Issues

- Known Issues

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

## 
v23.3 Service Pack 3 Resolved Issues (10/31/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Apply First N to Time/DateTime Fields | None | Web Report Studio now displays proper data when you apply the First N filter to Time/DateTime fields, if your server profile time zone is different from the JVM time zone. |
| Create Web Reports with Parameters | 03543828 | Web Report Studio now works as expected when you create a new report and specify a greater start date than the end date in the Enter Parameter Values dialog box. |
| Date Values in Filter Panel and Filter Controls | None | Web Report Studio now displays proper date values in the Filter panel and filter controls, when your server profile time zone is different from the JVM time zone. |
| Default Parameter Values in Available Value Lists | None | Server can now get the default parameter values from the available value lists in the Enter Parameter Values dialog box, when the parameters bind with Time/DateTime fields and your server profile time zone differs from the JVM time zone. |
| Display Parameter Values of DateTime Expressions | 03568689 | Server now displays proper parameter values of DateTime expressions in the value list for web reports, when the JVM time zone is different from the time zone you set in your server profile. |
| Drop-Down Value Lists for Bind Column Parameters | None | Web Report Studio still shows drop-down value lists for bind column parameters in all parameter UIs, when you set both "Allow Type-in of Value" and "-DNoValueListForDateTime" to "true". |
| Expression Value for Date/Time Parameters | None | Web Report Studio now shows the calculated values of expressions for Date/Time parameters in the input boxes and as tips in all parameter UIs, when you set the system variable -DNoValueListForDateTime to "true". |
| Expression Value for Date/Time/DateTime Parameters | None | For Date/Time/DateTime type parameters, Server now shows the calculated values of expressions: In the drop-down value lists of parameter (form) controls in Web Report Studio. In the input boxes when you edit the expression values. As the tips for the expression values. |
| Expression Value in Parameter UI | None | Web Report Studio now displays proper values of Date type expressions in the parameter UI and the default value of a DateTime type expression the same as the selected value in the calendar, when the JVM time zone is related to a Daylight Saving Time and different from the OS time zone. |
| Filter Time/DateTime Fields | None | Web Report Studio now displays proper data when you filter a Time or DateTime field using the shortcut menu or a filter control, if you enable Push Down On-screen Filter Values and your server profile time zone is different from the JVM time zone. |
| Filter with Time Values | None | Web Report Studio now displays the proper data when you filter with a time value. |
| Group-By Field Values of Date Type | None | Web Report Studio now displays the proper date values of group-by fields of the Date type, when your server profile time zone is different from the JVM time zone. |
| No Drop-Down Value Lists for Type-In Parameters | None | Web Report Studio now only displays the current values without drop-down value lists of type-in parameters of the Date/Time/DateTime type, when you set the system variable -DNoValueListForDateTime to "true". |
| Parameter Value Calculated by Expression | None | When you use an expression to specify the value for a Date/Time/DateTime parameter, Report now displays the date/time calculated by the expression in the parameter's value list rather than the expression for better user experience. |
| Parameter Values in Parameter Settings Dialog Box | 03568597 | Server now displays the proper values of parameters in the Parameter Settings dialog box, when the parameters are referenced by session variables. |
| Resize Tables with Dataset as All Resources in Business View | None | You can now resize tables and do other actions in Web Report Studio without getting an exception, when you set the dataset type to "All Resources in Business View". |
| Run Scheduled Email Tasks | 03312553 | Server now sends reports to valid recipients and no longer runs scheduled email tasks repeatedly, if the mail sender is invalid. |
| Specify Parameter Values | None | Web Report Studio now displays the parameter values of Date/Time/DateTime type parameters as you specify, if you don't set the parameters' User Defined Format and the JVM time zone is different from that in the Server Profile. |
| Time Zone in Filter Dialog Box | 03543671 | Server now displays date fields in the filter dialog box using the same time zone as in the report. |
| Time/DateTime Values in "Go To" Filter Panel | None | Web Report Studio now displays the proper Time/DateTime values in the "Go To" Filter panel, when your server profile time zone is different from the JVM time zone. |
| Value Time Zone in Parameter (Form) Controls | None | Server now displays values of type-in DateTime parameters using the server profile Timezone in parameter (form) controls in PDF outputs and values of Date type bind column parameters using the JVM time zone in parameter (form) controls in Web/Page Report Studio, when your server profile time zone differs from the JVM time zone. |
| Verification Message for Page Report Dataset Filter | 03543828 | Server now displays the proper verification error message when you specify the wrong parameter values for the dataset filter in the page report wizard. |

## 
v23.3 Service Pack 2 Resolved Issues (9/30/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Apply Web Report Studio Profile | None | Server now applies your Web Report Studio profile as expected when opening web reports in Web Report Studio, if you set the jrs.profile property in the session variable. |
| Duplicate Tabular Report | 03384664 | You can now successfully duplicate reports from a report that contains a tabular in Designer. |
| Dynamic Formula Used as Aggregation in Crosstab | 03395120 | Designer now no longer marks a dynamic formula that is used as Aggregation invalid when you open the Crosstab Wizard dialog box to edit a crosstab. |
| Export Crosstab to Excel in Column Format | 03453604 | Report now correctly displays a crosstab in the Excel output, when you set the Suppressed property of some fields in the crosstab to "true" and export to Excel in the Column Format. |
| Hide Enter Parameter Values Dialog Box | None | Server no longer displays the Enter Parameter Values dialog box for a report, when you specify to not show the dialog box, and if your saved default parameter values do not contain the value of the parameter whose "Get Value from API Only" property is enabled. |
| Run Linked Reports on Different Clustered Servers | 03471881 | Server now runs primary reports and linked reports on different nodes in a cluster at about the same speed. |
| Run Reports Without Edit Permission | 03426831 | Server now runs reports without displaying an Access Denied error message, when you set Default Mode for Web Report Studio to Edit Mode and Default View for Page Report Studio to Interactive View, and if you do not have the Edit permission on web reports. |
| Run Subreport | 03459983 | You can now successfully run a report containing a subreport that is in a banded panel in the primary report, when the content of the subreport and a field in the same banded panel spans pages. |
| Run Web Reports with Parameters | 03439306 | Server now runs web reports without displaying a NullPointerException error message, even if a parameter's value list is empty. |

## 
v23.3 Service Pack 1 Resolved Issues (8/31/2023)

| Title | Case # | Change Description |
| --- | --- | --- |
| Auto Fit Property on Horizontal Table | 02864215 | Report now properly adjusts the width of columns in a horizontal table according to content in the columns, when you set the Auto Fit property of any column to "true". |
| Data Container Link Using JSON Primary and Foreign Keys | 03316332 | Report now correctly sets up data container links based on the primary and foreign keys in a JSON data source. |
| Data Label of Chart Using Constant Interval | None | Report now properly displays the data labels on the category axis of a chart when you apply a constant interval to the axis and specify to truncate the data labels. |
| Date Time Parameter Value Display | 03288604 | Server now displays the calculated date time values of parameters instead of expressions when you create and run web reports, if you define the parameters as expressions and set their Allow Type-in of Value property to "false". |
| Display Line Charts in Web Report Studio | 03396163 | Web Report Studio now runs reports as expected without displaying an Error in Adaptor message, when you use single color with condition in line charts, and if you use a formula as the value of a Boolean type chart property. |
| Display Web Report Studio Dialogs | 02855465 | Web Report Studio now displays the complete dialog boxes when you embed Web Report Studio into your application, and if the default dialog boxes are bigger than the application window. |
| Embedded TTF in PDF Output | 03313052 | You can now add the -Dlogireport.pdf.UsePdfFontAscent option to Report's startup file to use the float ascent value in the PDF font for embedded TTFs in your PDF output. |
| Filter Time Field on Column Header | 03337048 | Web Report Studio now displays the proper time values when you filter on column headers. |
| Frequently Rerun Web Reports with Pie Charts | 03392174 | Web Report Studio now refreshes reports with pie charts as expected without displaying Uncaught TypeError messages, when you resize the browser window many times within a short time. |
| HTML Tags in Group-by Field Values | 03311525 | Report now properly parses the HTML tag elements in the values of a group-by field when you set the field's Convert HTML Tag property to "true". |
| Launch Report Installer with JDK 11.0.20 or Above | None | You can now launch the installer for Report earlier than v23.3.1 with JDK 11.0.20 or above when getting the "Could not find or load main class com.zerog.lax.LAX" error message, by running the following command: ~$ export _JAVA_OPTIONS=-Djdk.util.zip.disableZip64ExtraFieldValidation=true ~$ ./report_installation_file_name LAX_VM "/path/to/jdk-11.0.20/bin/java" Or ~$ export JAVA_TOOL_OPTIONS=-Djdk.util.zip.disableZip64ExtraFieldValidation=true ~$ ./report_installation_file_name LAX_VM "/path/to/jdk-11.0.20/bin/java" |
| Library Component Configuration Panel Binding No Data | 03305992 | JDashboard no longer displays a Check DataContainer Error message if the configuration panel of library component binds no data. |
| No Business View Available | 03305992 | Page Report Studio now lowers error messages to the Warning level, when it cannot find an appropriate business view. |
| Parameter Applying the  Value | 03291290 | After upgrading from v13 to v18 and later, Designer now no longer displays a NullPointerException when you preview a parameter report, when the parameter is a type-in parameter and applies the  value. |
| Parameter Bound with Imported SQL Column | None | Report now properly retrieves values for a parameter that is bound with an imported SQL column, when the imported SQL statement references another parameter. |
| Read Font Roboto | 03287261 | Server can now read the font Roboto when you export page reports to PDF/HTML on Linux if you specify the font in the HTML tag. |
| Return reportname() in Web Report Studio | 03287775 | Web Report Studio now displays the report name as expected when you create reports, and if you use a formula to return reportname(). |
| Run Scheduled Email Tasks | 03312553 | Server now displays an error message instead of endless run when running scheduled email tasks, if the email sender is not specified. |
| Save Parameter Values as Default on Server | 03287763 | Server now applies parameter values you save as the default on the Server Console, when other parameters are specified in session variables. |
| Use Formula to Control Properties of BV Data Component | 03230347 | You can now use formulas to control properties of data components in a business view-based report when you do not bind data to the report body, if you have added the formulas in the data components. |
| Use Today as Default for Parameters | None | Server now displays today's date time in the Enter Parameter Values dialog box as expected, when Use Today as Default is selected for a parameter, and if Server and client use different time zones. |

## 
v23.3 Feature Enhancements

| Title | Description |
| --- | --- |
| Catalog Studio License and Profile | You now need a Catalog Studio license to use Catalog Studio on Server. You can allow users to edit catalogs in the public folders by granting them Edit permission. You can also customize the Catalog Studio user interface using Catalog Studio Profile on the Server Console or via the JavaScript API. |
| Control Error and Status Messages in JavaScript API | You can utilize callback functions in the JavaScript API to control error, warning, and status messages from applications out of Report. |
| Enhance Export Capabilities with More Options | You can now set these new options: Overflow to Next Cell, Retain Formatted Values, and Generate Excel Formula to enhance the Excel output of your reports, and specify tag order of the report objects when exporting your reports to accessible PDF, in Template Object Order or Page Coordinate Order. |
| Key File and Username/Password for SFTP Schedule | You can now use the combination of an SSH key file and username/password to sign into your SFTP server, via the Server Console or Web API. |
| Save UDO into XML Report Template | When you save a page report containing user-defined objects (UDO) in XML format, Designer can now save the UDOs into the report template along with other report objects. |
| Support More Chart Types in Page Report Template Editor | You can now create and update area, pie, donut, and bench charts and customize their properties in the Inspector panel. You can change a chart type by selecting one in the Components panel. More properties are added to bar charts. |
| Timeout Control for Running Scheduled Tasks | Server administrators can now customize the timeout for running scheduled tasks and publishing to Email/FTP. |

## 
v23.3 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Abnormal Login Page in Integration Environment | 02793483 | Server no longer displays an abnormal login page when the request you forward to run reports does not contain correct login information in an integration environment. |
| Apply Style List in JDashboard | 03064215 | JDashboard now displays the style list as expected in the Edit mode, when you select Apply Style on the shortcut menu of a library component. |
| Barcode in PDF Output | 03017054 | Report now clearly generates barcodes using images in your PDF output. |
| Convert Subreports | 03287152 | Server now converts subreports together with primary reports when you use Administration > Other > Converting, and if the subreports need to be converted. |
| Crosstab Header Alignment | 03290873 | Page Report Studio now displays crosstab headers in the proper position. |
| Crosstab Values | 03067285 | Report now correctly calculates the aggregations and totals in a crosstab, when you set the Suppress property of its innermost aggregate field to "true". |
| Display Data Field as SVG Image | 03065702 | Report now properly displays a data field as image, when you use the SVG decode type for the image data. |
| Display Sort Icon in Summary Columns | 02855963 | Web Report Studio now displays the sort icon in the summary column headers of a summary table, when you set the Sortable property of the columns to "true". |
| Display Toolbar Buttons in Web Report Studio | None | After an administrator applies a new Web Report Studio profile as the default one, Web Report Studio now displays the toolbar buttons as expected when you resign into Server. |
| Dropdown Button Border for Parameters | 02855542 | Web Report Studio now displays the borders of dropdown buttons for multivalued parameters. |
| Enable Customize Properties | 03076760 | Server now retains the status of the Enable Customize Properties option, when you change a date parameter value while running web reports. |
| Field Display | 03209115 | Report now properly displays the content of a field when you set both its Auto Fit and Word Wrap properties to "true" and specified a non-zero value to its Maximum Width property. |
| Export to PDF | 03071471 | Web Report Studio now exports reports with parameters to PDF as expected without displaying the NullPointerException error message. |
| Formula Applying the join() Function | 03283007 | A formula that applies the join() built-in function can now return correct value. |
| Global Variable Reference in Banded Object | 03067285 | Report now correctly returns value to a formula that references another formula in which you specify a global variable, when you use this formula in a banded object. |
| Go to Second Page in Page Report | 03067564 | Page Report Studio no longer displays the TypeError message when you navigate to the second page. |
| Height of Banded Object Panels | 02850558 | Designer now properly changes the height of a banded object's panels, when you insert a vertical banded object into the banded object and then resize the panels. |
| Import Business Views Using Catalog Doctor | 02150834 | You can now import the business views in a catalog to another catalog using the Catalog Doctor. |
| Insert Page Panel | 03289853 | Designer now properly adds a blank page next to the current page when you insert a page panel. |
| Large Image in Field Value | 02851576 | When the value of a field references an image using the  tag and you set the field's Convert HTML Tag property to "true", Report now displays the image in a new page when the image is too large. |
| Paged Values for Query Filter | 03064934 | Web Report Studio now displays 500 values per page in the Select Values dialog box to enhance its performance, when you select More in the value list of the Query Filter dialog box. |
| Parameter Availability for Parameter (Form) Control | None | When you set the Get Value from API Only property of a parameter to "true", Designer and Page Report Studio now no longer display the parameter and all other parameters if the parameter is in a cascading group when you add a parameter control or parameter form control, while Web Report Studio does not display the parameter and its higher-level cascading parameters if any. |
| Parameter Expressions Returning Same Value | 02449834 | When the default value for one of the parameters in a report applies the dateadd('d', -1, firstdayofmonth(today())) expression and another applies dateadd('d', -1, firstdayofquarter(today())), Designer now properly displays the Enter Parameter Values dialog box when the two expressions return the same value. |
| Publish Catalogs and Reports from Designer | 03064985 | Server no longer displays catalogs and reports as folders after you publish them from Designer. |
| Reference Table Configuration | 03060469 | You can now configure the reference table to monitor resource references in your catalog, when any of the resources contains incomplete information in the template. |
| Restore Backup Realm DB in Cluster | 02854949 | Server can now restore your backup v14 realm DB in a cluster. |
| Run Bursting Reports in Cluster | 03065122 | Server now sends emails to all recipients as defined when running bursting reports in a cluster. |
| Run Page Reports via Servlet URL Forward | 02793483 | You can now run reports in Page Report Studio by forwarding the servlet URL in an integrated environment without getting a 404 error message. |
| Run Scheduled Bursting Tasks to FTP | 03209298 | Server can now run scheduled bursting tasks to FTP without displaying a ClassCastException error message. |
| Run Scheduled Tasks | 03045772 | Server now runs scheduled tasks without displaying the Array Index Out Of Range error message, when you use TTF in reports. |
| Same Pages and Table Rows as in PDF | None | Web Report Studio now displays the same number of pages and table rows as in the PDF output. |
| Save New Dashboards via API | 02581640 | You can now save your new dashboards after you insert or delete components via the API, when your network runs slowly. |
| Scroll Bars in the Select Folder Dialog Box | 01999109 | Designer now properly displays scroll bars in the Select Folder dialog box for you to select the target location on Server to publish your resources, when you changed the resolution of your laptop to a value other than 100%. |
| Submit FTP Schedule Tasks via URL | 02823344 | Server can now submit FTP schedule tasks via URL without displaying a NullPointerException error message, when the jrs.ftp_text_file_suffix property is not included in the URL. |
| Type-in Parameter Without Default Value | 02851521 | You can now successfully preview a parameter report in Designer, when you defined the parameter as a type-in parameter without any default value. |
| Update Parameter Values | 03063628 | Server can now refresh and display the values of other parameters when you update a parameter value for a page report. |

## 
Known Issues

Report data cut off in PDF due to PDF page size limitation

When you export a report to PDF, some data of the report are cut off in the PDF output when the report contains a large amount of data, and you have applied continuous page mode to the report or set the page size to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

Unsupported go-to action when using dynamic formulas on chart

You get exceptions when you perform the go-to action on a chart that uses a dynamic formula on the value axis and the formula contains group information.
