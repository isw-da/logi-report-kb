---
title: "Report v26.2 Release Notes"
id: 47011446368781
section: "Release Notes for Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/47011446368781-Report-v26-2-Release-Notes
updated_at: 2026-07-31T14:01:35Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Report v26.2 Release Notes

This topic describes feature enhancements, resolved issues, and known issues of the Report v26.2 release, from June 30, 2026.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.

- v26.2 Service Pack 1 Resolved Issues

- Feature Enhancements

- v26.2 Resolved Issues

### Prerequisites

Version 26.1 includes changes to True Type Font (TTF) handling. If you are upgrading from version 23.4 or later, ensure all TTF files used in your existing reports are located in the %ReportHome%/fonts folder before rendering or delivering results. Without this one-time setup, you may experience unexpected font mismatching issues. Once the fonts are properly located, reports will render normally.

### Log4j and Log4Net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.

## 
v26.2 Service Pack 1 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Connection Pool Current Owner Column | None | A new Current Owner column has been added to the connection pool dialog, providing visibility into which user currently holds each connection. |
| Cache Cube Invalid Catalog Key Error | 05589440 | An 'Invalid catalog key' error that occurred when accessing Cache Cube paths has been resolved. Cache Cube operations now complete successfully without throwing catalog key errors. |
| Second Empty Page Generated in Reports | 05596361 | An issue where Logi Report v26 generated a second page with no data has been resolved. Reports now render with the correct number of pages without empty trailing pages. |
| Aggregate Reports Partial Data Loading Issue | 05515533 | Logi aggregate reports no longer display partial data requiring multiple toggles to load fully. Aggregate report data now loads completely on the initial render. |
| Boilerplate Corruption in Logi Report Server | 05586026 | An issue where the boilerplate in Logi Report Server was sometimes corrupted has been resolved. The boilerplate now renders consistently and correctly across all pages. |
| Form Control Drop-Down Search Not Working | 05594416 | The search feature in Form Control drop-down lists now functions correctly. Users can search and filter drop-down options as expected without encountering errors. |
| Report Filter Selected Value Display Issue | 05595507 | The selected value in report filters is now displayed correctly in the report output. Previously, the filter selection was not being reflected properly in the rendered report. |
| Scheduled FTP/SFTP CSV Export Issue | 05596009 | An issue with the FTP/SFTP CSV format when scheduling Logi Report exports has been resolved. Scheduled reports exported via FTP/SFTP now deliver CSV files correctly. |
| On New Page Behavior Change from v19 to v24 | 05586037 | The 'On New Page' behavior that changed between v19 and v24 has been corrected. The feature now behaves consistently with earlier versions as expected. |
| BF Section New Page Property Ignored in v26 | 05586494 | An issue where the 'must start on new page' property for BF sections was being ignored in v26 has been resolved. BF sections now correctly start on a new page as configured. |
| Repeating Headers and Transparent Report Issue in v26 | 05585384 | Reports generated in v26 no longer display repeating headers or show through-like transparent rendering. Headers now appear correctly without duplication or transparency artifacts. |

## 
Feature Enhancements

| Title | Description |
| --- | --- |
| Parameter Screen Submit Button Enhancement | The parameter screen now includes an enhanced Submit button, improving usability when users interact with report parameters before running a report. |
| HTML Tag Width Support | HTML tags now support the 'width:100%' property, allowing report content to dynamically fill the available container width for a more responsive layout. |
| Chart to Excel Export Control Flag | A new flag has been added to allow users to control whether charts are exported to Excel as chart objects or as images, resolving legend display issues during export. |
| Exclude Accounts from Simultaneous Login Restriction | Administrators can now exclude specific accounts from the 'Enable Multiple Users to Login Using the Same User Name' restriction, providing greater flexibility in managing user access policies. |
| Security and Vulnerability Improvements | Multiple security vulnerabilities have been identified and resolved as part of the Q2 security review, ensuring the application meets current security standards and reduces exposure to known risks. |
| Logi Report New UI Phase 3 | Phase 3 - Catalog Studio UI of the Logi Report modernization is now complete, delivering additional interface enhancements and refinements for a more consistent and intuitive user experience. |
| Logi Report New UI Phase 2 | Phase 2 of the Logi Report UI modernization introduces further visual and functional updates, building on the foundation established in Phase 1. |
| Logi Report New UI Phase 1 | Phase 1 - Page Studio UI of the Logi Report modernization delivers an updated interface with a refreshed look and feel, improving navigation and overall usability for end users. |
| CORS Header Configuration Enhancement | The method for setting CORS (Cross-Origin Resource Sharing) headers has been enhanced, giving administrators more control over cross-origin access policies for Logi Report Server. |
| Column Position Retained After Sort and Filter | The report view now retains the user's current column position after applying sorting or filtering, eliminating the need to scroll back to the relevant column after each operation. |
| Publish Reports to Server on Local Docker Container | Users can now publish reports from a local Logi Report Designer directly to a server running on a local Docker container, expanding deployment flexibility for on-premises environments. |
| Image URL Caching in Reports | Images loaded from URLs in reports can now be cached for reuse across records, reducing redundant network calls and improving report rendering performance. |
| Password-Protected Excel Export | Reports exported to Excel can now be protected with a password, supporting read-only access control for distributed Excel files. |
| Crosstab Wrap Direction Control | A new option has been added to control the wrap direction in crosstab reports, allowing users to define how content wraps when crosstab data exceeds available space. |
| REST API Enhancement | The Logi Report REST API has been enhanced with additional capabilities, improving integration options and providing greater programmatic control over report operations. |
| Row Limiting in Full Data Mode | A new row limiting option is now available in Full Data Mode with Complete Export, allowing users to cap the number of rows returned during a full data export. |
| Scheduler Task Cancellation and Log Enhancements | Scheduler jobs can now be configured to automatically cancel the next run when a report returns no data. Additionally, the completed logs view has been enhanced for improved visibility into job execution history. |
| Supported Database Versions Documentation Update | The documentation for supported database versions has been updated to reflect the latest compatibility information, ensuring users have accurate and current reference material for database configuration. |
| Composer Source Translation to BV | Composer source content can now be translated to BV (Business View), enabling seamless migration and reuse of existing Composer report definitions within the BV environment. |
| Catalog Link Settings Saved on Publish | Catalog link settings are now saved correctly when publishing the latest reports or library components to an existing folder, ensuring consistent catalog references are maintained across publish operations. |
| Enhanced attribute Block gap | The Block Gap property can now be controlled by setting a negative value to move the newly split crosstab layout to a new page. |
| Dynamic Resources in Template Editor Mode | Dynamic resources including formulas, parameters, aggregations, and functions are now supported in template editor mode, enabling more flexible and powerful report template design directly within the editor. |

## 
v26.2 Resolved Issues

| Title | Case # | Change Description |
| --- | --- | --- |
| Repeat Content Layout Issue | 05579750 | The Tabular layout is now handled correctly when the height of a Tabular cell is greater than the page height and the 'Repeat Content' property is set to true. |
| Customize Server Preference Page Access Issue | 05571494 | Users can no longer access the preferences page in My Tasks, Resources, and other areas when the 'Allow users to modify preferences from user console' setting is unchecked by the administrator. |
| SSL Certificate Issue in Logi Report Designer | 05525643 | SSL certificate validation in Logi Report Designer now functions correctly, resolving connection errors that occurred when accessing secure server URLs. |
| Logi Report Server Configuration Error | 05510941 | A NullPointerException error that occurred when editing banded object positions in the template editor and returning to Page Studio has been resolved. |
