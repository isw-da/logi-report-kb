---
title: "Logi Report v18.2 Enhancements"
id: 4411830858775
section: "Release Notes for Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4411830858775-Logi-Report-v18-2-Enhancements
updated_at: 2022-01-27T07:58:16Z
---

# Logi Report v18.2 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4411822430231-Logi-Report-v18-2-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683905815-Logi-Report-v18-1-Release-Notes)

# Logi Report v18.2 Enhancements

This topic introduces the significant features of Logi Report v18.2.

* [User Experience & Usability Improvements](#UX)
* [Pixel-Perfect Formatting](#Format)
* [Enhanced Operational Reporting Capabilities](#Reporting)

## User Experience & Usability Improvements

* Logi Report Designer now applies a new color theme to the Start Page and main frame top banner, providing you with an enhanced and modern look.

  ![Designer in New Theme](https://devnet.logianalytics.com/hc/article_attachments/4420453374999/designer-new-theme.jpg)
* You can now use the new properties No Page Break for Data Format and No Page Break for Report Format to remove the page breaks on each individual sheet in Excel output, when you export a report to Excel using Data Format and Report Format, in addition to Column Format.

  ![Excel Output With and Without Page Breaks](https://devnet.logianalytics.com/hc/article_attachments/4420453375383/no-page-break.jpg)
* You can now change the property values in server.properties in an integrated Logi Report Server after you upgrade to v18.2, by creating the install.server.properties file and adding properties and their new values in it.

## Pixel-Perfect Formatting

* You can now reduce the width of fields, labels, and table/crosstab columns when the associated contents are not as wide as the objects, to get an improved autofit display, by using the Reduce Width When Autofit property in Logi Report Server or the Reduce Width When Auto Fit property in Logi Report Designer. The property is available in these places:
  + The Inspector panel in Designer and Web Report Studio
  + The shortcut menu and properties dialog of an object in Web/Page Report Studio

  ![Reduce Width When Autofit](https://devnet.logianalytics.com/hc/article_attachments/4420453375767/autofit-reduce-width.png)

## Enhanced Operational Reporting Capabilities

* You can now call a set of functions in your formulas to convert Currency, Number, Date, DateTime, and Time data to strings based on specified locales.

  ![Locale Formula Functions](https://devnet.logianalytics.com/hc/article_attachments/4420461444503/locale-formulas.jpg)
* You can now use the Format Locale property to display the appropriate values of data fields and special fields for a country or region.

  ![Format Locale](https://devnet.logianalytics.com/hc/article_attachments/4420447038103/format-locale.png)
* You can now use an Office 365 email server in Logi Report for scheduling to email and emailing system notifications of task success/failure. When there are invalid email addresses, Server can still send emails to the valid addresses successfully, while displaying a message about the failure of sending emails to the exact invalid addresses.

  ![Office 365 SMTP Server](https://devnet.logianalytics.com/hc/article_attachments/4420453376663/office365.png)
* Logi Report now supports OpenJDK 15 and 16, in addition to OpenJDK 8, 11, 12, 13, and 14.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4411822430231-Logi-Report-v18-2-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683905815-Logi-Report-v18-1-Release-Notes)
