---
title: "Exporting Reports to Accessible HTML and PDF"
id: 4405664594583
section: "Delivering Your Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF
updated_at: 2022-01-27T20:34:43Z
---

# Exporting Reports to Accessible HTML and PDF

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661755031-Exporting-to-Fax)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661923607-Publishing-and-Downloading-Resources)

# Exporting Reports to Accessible HTML and PDF

To help users who experience disabilities or have special needs use your reports, you can export the reports to both accessible HTML and PDF, so that they can read the reports with assistive tools. This topic describes how you can add accessibility to your HTML output and export your reports to accessible PDF. It also briefly introduces the accessible Server Console.

This topic contains the following sections:

* [Making HTML Output Accessible](#HTML)
* [Exporting Reports to Accessible PDF](#PDF)
* [Adjusting the Reading Order of Report Objects in Accessible PDF](#Order)
* [The Accessible Server Console](#Server)

## Making HTML Output Accessible

Logi Report supports the accessibility HTML attributes and a built-in accessible Server Console for displaying reports in HTML. The implementation standard is based on HTML Specification 4.01 <http://www.w3.org/TR/WCAG10-HTML-TECHS/> and information on Section 508 Standards: [http://www.section508.gov](http://www.section508.gov/) and [http://www.access-board.gov](http://www.access-board.gov/).

When designing a report in Designer, you can add these accessibility HTML attributes to the report objects to provide more readable and accessible HTML output.

**To add accessibility to a report in the HTML output**

1. Predefine the necessary accessibility attributes of the report objects when designing the report.

   When you select a report object in the design area, you can get these accessibility attributes in the Accessibility property group in the Properties sheet of the Report Inspector. For more information about the accessibility attributes of each report object, see [Report Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties).
2. Enable Section 508 compliant output when exporting the report to HTML.

   In the HTML export UI, select **Section 508 Compliant Output**. If you only want to convert table/crosstab components into HTML data table in the HTML output, select **Use HTML Data Table**.

   Logi Report provides the two options in all the HTML export UIs.

## Exporting Reports to Accessible PDF

You can also export your report to an accessible PDF by enabling the **Accessible PDF** option, which is available in all the PDF export UIs in Logi Report, so that users of screen readers and those who have low vision can have their tagged PDF read out aloud in appropriate language in the Adobe Acrobat software. The implementation standard is based on Web Content Accessibility Guidelines (WCAG) 2.0 (ISO/IEC 40500:2012) <http://www.w3.org/TR/WCAG/>and the PDF/UA (ISO 14289-1) <http://www.iso.org/standard/64599.html> standard.

### Adjusting the Reading Order of Report Objects in Accessible PDF

When you export a report to an accessible PDF, Logi Report Engine exports the objects in the report according to their display sequence in the report structure tree in the Report Inspector. When designing a report in Designer, you can adjust the object sequence to customize the order you want the screen reader to read them, by selecting an object and selecting **Up**![Up button](https://devnet.logianalytics.com/hc/article_attachments/4420550817815/btn_up.gif) or **Down**![Down button](https://devnet.logianalytics.com/hc/article_attachments/4420550818199/btn_down.gif) on the Report Inspector toolbar.

![Adjust Report Object Order for Accessible PDF](https://devnet.logianalytics.com/hc/article_attachments/4420556121751/frmt_acsbl_pdf.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg)

* You can only move the objects the position of which are "absolute", and one object at a time.
* You can only adjust the order of the objects that are at the same layer in the report template, for example, the objects in the detail panel of a banded object.
* For the three main objects of a report, Report Body, TOC, and Datasets, you can only adjust the order of Report Body and TOC, and you cannot move the objects in the report body above the Page Panel object at the same layer.
* For the objects in the same tabular cell, you cannot move the objects that are contained in a paragraph.

## The Accessible Server Console

Server enables the disabled users to visit the accessible version with simplified functionality to read reports by reader agent or other assistive tools. In the accessible version, Server displays reports in HTML with accessibility attributes, and outputs the table/crosstab components as HTML data tables. For more information, see Making HTML and PDF Report Outputs and Server Console Accessible in the *Logi Report Server Guide*.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661755031-Exporting-to-Fax)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661923607-Publishing-and-Downloading-Resources)
