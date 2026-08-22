---
title: "Logi Report v18.3 Enhancements"
id: 4420461816983
section: "Release Notes for Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4420461816983-Logi-Report-v18-3-Enhancements
updated_at: 2022-01-27T07:58:15Z
---

# Logi Report v18.3 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4420453757847-Logi-Report-v18-3-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411822430231-Logi-Report-v18-2-Release-Notes)

# Logi Report v18.3 Enhancements

This topic introduces the significant features of Logi Report v18.3.

* [User Experience & Usability Improvements](#UX)
* [Pixel-Perfect Formatting](#Format)
* [Enhanced Operational Reporting Capabilities](#Reporting)
* [Platform Enhancements and Optimizations](#Platform)

## User Experience & Usability Improvements

* You can now customize the text format of the subreport links in Excel output when you export the subreport in separate sheet, to make these links more easily recognizable inside the primary report.

  ![Customizable Subreport Index in Excel Output](https://devnet.logianalytics.com/hc/article_attachments/4420453756567/subreport-index-format.jpg)
* Logi Report enhances dynamic formulas by enabling report designers to create local parameters directly via the Formula Editor dialog box to reference in the formulas in Designer, and enabling end users to reference local and global parameters in the formulas in both Web Report Studio and Page Report Studio.

  ![Dynamic Formula Reference Parameter](https://devnet.logianalytics.com/hc/article_attachments/4420447435415/dynamic-formula.jpg)

## Pixel-Perfect Formatting

* Designer now provides the Invisible property for page panels in query-based page reports, and you can use formulas to dynamically display or hide the content inside page panels according to different user scenarios with continued page numbers in the reports.

  ![Dynamic Page Panel Visibility](https://devnet.logianalytics.com/hc/article_attachments/4420453756823/page-panel-visibility.jpg)
* You can now use four new formula functions: *currentUsedHeight()*, *currentUsedWidth()*, *totalAvailableHeight()*, and *totalAvailableWidth()*, for calculating report space dynamically. These functions can help extend the capability of multipage and pixel perfect reporting at runtime, when used for the Fill Whole Page, On New Page, Invisible, and Suppress properties of banded objects and tables.

  ![New Formula Functions for Space Calculation](https://devnet.logianalytics.com/hc/article_attachments/4420447435671/space-formula-functions.jpg)

## Enhanced Operational Reporting Capabilities

You can now add a Table of Contents in a page report or web report, use the TOC Page Number special field to display page numbers for the TOC differently than your report pages, and specify properties for the TOC Container object to customize format of the TOC entries. With the TOC, you can easily navigate to the report content you want when previewing the report in Designer and in the report outputs.

![TOC in Report](https://devnet.logianalytics.com/hc/article_attachments/4420461816471/toc-in-report.jpg)

## Platform Enhancements and Optimizations

* Logi Report upgrades the support for some third-party packages to newer versions.
* Logi Report now supports Oracle JDK 17 and OpenJDK 17, in addition to Oracle JDK 8, 9, 11, and 12, and OpenJDK 8, 11, 12, 13, 14, 15, and 16.
* You can now use REST API to publish resources from the Server computer to Server and from one Server to another, besides from the local drive to Server, as you do on the Server Console.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4420453757847-Logi-Report-v18-3-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4411822430231-Logi-Report-v18-2-Release-Notes)
