---
title: "Exporting Reports to Accessible HTML and PDF"
id: 1500010099241
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099241-Exporting-Reports-to-Accessible-HTML-and-PDF
updated_at: 2021-07-23T19:16:09Z
---

# Exporting Reports to Accessible HTML and PDF

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099281-Exporting-to-Fax)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources)

# Exporting Reports to Accessible HTML and PDF

To help users who experience disabilities or have special needs use your reports, you can export the reports to both accessible HTML and PDF outputs, so that they can read the reports with assistive tools. This topic describes how you can add accessibility to your HTML outputs and export your reports to accessible PDF. It also briefly introduces the functionality of the accessible Server version.

This topic contains the following sections:

* [Making HTML Outputs Accessible](#HTML)
* [Exporting Reports to Accessible PDF](#PDF)
* [The Accessible Server Version](#Server)

## Making HTML Outputs Accessible

Logi Report supports accessibility related HTML attributes and a built-in accessible Server Console for displaying the report result in HTML. The implementation standard is based on HTML specification 4.01 <http://www.w3.org/TR/WCAG10-HTML-TECHS/> and information on Section 508 Standards: [http://www.section508.gov](http://www.section508.gov/) and [http://www.access-board.gov](http://www.access-board.gov/).

When designing a report in Designer, you can add the accessibility related HTML attributes to the report objects in order to make the HTML outputs more readable and accessible. You can find these attributes in the Accessibility property group of the Report Inspector.

**To add accessibility to a report in the HTML output:**

1. Predefine necessary accessibility attributes when designing the report.

   When you select a report object in the design area, you can get the corresponding accessibility attributes in the Report Inspector. For more information about the accessibility attributes for each report object, see [Report Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties).
2. Enable Section 508 compliant output when exporting the report to HTML.

   In the HTML export UI, select the option **Section 508 Compliant Output**. If you only want to convert table/crosstab components into HTML data table in the HTML output, select the option **Use HTML Data Table**.

   Logi Report provides the above two options in all the HTML export UIs.

## Exporting Reports to Accessible PDF

Logi Report also supports exporting the report result to an accessible PDF by enabling the **Accessible PDF** option, which is available in all the PDF export UIs in Logi Report, so that users of screen readers and those who have low vision can have their tagged PDF read out aloud in appropriate language in the Adobe Acrobat software. The implementation standard is based on Web Content Accessibility Guidelines (WCAG) 2.0 (ISO/IEC 40500:2012) <http://www.w3.org/TR/WCAG/>and the PDF/UA (ISO 14289-1) <http://www.iso.org/standard/64599.html> standard.

## The Accessible Server Version

Server enables the disabled users to visit the accessible version with simplified functionality to read reports by reader agent or other assistive tools. In the accessible version, Server displays reports in HTML with accessibility attributes, and outputs the table/crosstab components as HTML data tables.

For more information about how to enable the accessible Server version, see Making HTML and PDF Report Results and Server Console Accessible in the *Logi Report Server Guide*.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099281-Exporting-to-Fax)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources)
