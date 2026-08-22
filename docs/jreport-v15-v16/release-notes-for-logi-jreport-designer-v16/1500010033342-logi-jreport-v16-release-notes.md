---
title: "Logi JReport v16 Release Notes"
id: 1500010033342
section: "Release Notes for Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033342-Logi-JReport-v16-Release-Notes
updated_at: 2022-03-01T06:41:37Z
---

# Logi JReport v16 Release Notes

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068801-Logi-JReport-v16-Enhancements)

# Logi JReport v16 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Logi JReport v16 release.

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

## Feature Enhancements

| Item | Feature # | Description |
| --- | --- | --- |
| 1 | 19462 | Logi JReport Users now can quickly search and sort resources in the Catalog Browser and Business View Editor. |
| 2 | 19523 | A new option is provided in the Business View Editor that enables users to extract the year, quarter, month, week, or day from a timestamp field. |
| 3 | 19711 | Administrator can now fully control personal folder space usage. |
| 4 | 19823 | Email can now be sent to Roles and Groups in addition to users for scheduling. |
| 5 | 19872 | The JavaScript API now supports resource deployment and dynamic connections. |
| 6 | 19897 | Properties are now editable in Logi JReport Designer by default. |
| 7 | 71494 | The special field "Username" can now accept parameters from Stored Procedures. |
| 8 | 112944 | Exceptional criteria can now be applied to periodical scheduling. |
| 9 | 116717 & 147772 | Report templates can be automatically updated along with their metadata element name and property changes. |
| 10 | 117373 | Report bursting enhancements include dynamic email subject and comments. |
| 11 | 132060 | Parse button removed from SQL statement viewer in Query Editor because the parser no longer works with most databases. |
| 12 | 156225 | Link added for URL enhancements with on-screen filter. |
| 13 | 163235 | Added Summary function enhancements with distinctSum() support. |
| 14 | 164248 | Cascading Style Sheet (CSS) can now be applied to total cells and detail cells separately in crosstabs. |
| 15 | 173609 | Optional current or initial parameter values can now be passed to linked reports. |
| 16 | 178411 | The new special field "Record Number" is supported in Web Report. |
| 17 | 180042 | SVG images are now supported in XML data source for the URI scheme. |
| 18 | 185983 | LDAP support enhancements with optional full user retrieval from Active Directory and "everyone" role support. |
| 19 | 186164 | Security enhancements have been made with configurable JSP headers for Logi JReport Server JSPs and servlets. |
| 20 | 186496 | Dynamic font (font face, font size, etc.) can now be controlled by formula. |
| 21 | 186759 | Developers and end users now only need to connect to the server once, to deploy or download reports as many times as they need. |
| 22 | 187018 | Styles and formatting can be applied to individual elements in combo charts. |
| 23 | 187352 | Logi JReport now works with OpenJDK 12 and 13, and Oracle JDK 12. |
| 24 | 187839 | Users can now quickly search properties or preferences in Logi JReport Server. |
| 25 | 187849 | Browser cache now updates automatically when running on an upgraded server or a server with new patches. |
| 26 | 188091 | Performance enhancements have been made with optimized JavaScript loading mechanism. |
| 27 | 188887 | JDashboard is now hidden if a user is not licensed for it. |
| 28 | 189100 | Drawing Lines now have dynamic positioning and optional arrow ends. |
| 29 | 190779 | "Suppress" property is now supported on crosstab column and row headers. |
| 30 | 191217 | User Defined Object (UDO) enhancements now support rotate text, QR Codes, and optional barcode length optimization for Code 128 Symbology. |
| 31 | 193534 | Parameter values that have been set in the URL no longer appear on the Parameter tab of the Schedule page. |
| 32 | 193563 | Queries and subqueries are now automatically closed after their reporting task is completed. |

## Resolved Issues

| Item | Case # | Issue |
| --- | --- | --- |
| 1 | 70950 | Fixed the issue java.lang.ArrayIndexOutOfBoundsException when exporting a banded object to Excel. |
| 2 | 71494 | Fixed the problem of creating extra null parameters, instead of using existing ones from Stored Procedures. |
| 3 | 71510 | Fixed the problem of sharing a same filter to multiple banded objects instead of using their individual filters, if these banded objects were copied from one object. |
| 4 | 71667 | Fixed the Unknown Exception when configuring users' profiles to customize a library component's title bar. |
| 5 | 71781 | Fixed alignment issues caused by negative position values set to group footer. |
| 6 | 71822 | Fixed the configuring parameter options failure with Bind with Cascading Columns. |
| 7 | 71824 | Improved log system to include more detailed information about broken links, unmatched mapping names, etc. |
| 8 | 71899 | Fixed the failure of converting HTML tags in table cells when the property "Ignore HTML Tags" is set as false. |
| 9 | 80686 | Fixed the word-wrap failure on text objects when running reports on a specific environment (ThinkPad + Chrome versions V76 or V77). |
| 10 | 81328 | Fixed a problem in which BMP images failed to display in Blob format when retrieved from Oracle 12c.. |
| 11 | 81462 | Fixed problem where Arabic numbers could not be displayed in correct order in PDF reports. |
| 12 | 193536 | Improved neutralization of script-related HTML tags to prevent XSS and Path Traversal vulnerabilities. |
| 13 | 193732 | Fixed a problem in which reports failed to export to PDF, Excel, or other forms when a page break occurred on a record value or a label. |
| 14 | 193773 | Fixed the issue when a report is blank because report content is too large to fit in a table cell. |
| 15 | 193958 | Resolved the failure that occurred when synchronizing over 1000 groups from Active Directory Server to Logi JReport Server. |
| 16 | 194063 | Fixed a problem in which CSV files exported incorrectly to TEXT files. |
| 17 | 194468 | The method by which FTP connections are checked during scheduling was improved to prevent any cross-site request forgery (CSRF) vulnerabilities. |

## Known Issues

**Report data cut off in PDF due to PDF page size limitation**

When you export a report to PDF format, you will find that in the PDF result some data of the report are cut off if the report contains a large amount of data but its page mode was specified to be continuous page mode or its page size was set to be larger than 200 inches. This is due to a PDF limitation where the data displayed can be no larger than 200 inches in a single PDF page.

**Unsupported go-to action when using dynamic formulas on chart**

You will get exceptions when you perform the go-to action on a chart which uses a dynamic formula as its shown value and the formula contains group information. This is a limitation in the current version. It will be resolved in a future release.

[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068801-Logi-JReport-v16-Enhancements)
