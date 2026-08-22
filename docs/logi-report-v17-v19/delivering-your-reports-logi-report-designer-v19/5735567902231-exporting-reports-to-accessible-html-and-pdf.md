---
title: "Exporting Reports to Accessible HTML and PDF"
id: 5735567902231
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF
updated_at: 2022-11-02T07:57:49Z
---

# Exporting Reports to Accessible HTML and PDF

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735553344535-Exporting-Reports-to-Fax)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources)

# Exporting Reports to Accessible HTML and PDF

To help users who experience disabilities or have special needs use your reports, you can export the reports to both accessible HTML and PDF, so that they can read the reports with assistive tools. This topic describes how you can add accessibility to your HTML output and export your reports to accessible PDF. It also briefly introduces the accessible Server Console.

This topic contains the following sections:

* [Making HTML Output Accessible](#HTML)
* [Exporting Reports to Accessible PDF](#PDF)
  + [Adjusting the Reading Order of Report Objects in Accessible PDF](#Order)
* [The Accessible Server Console](#Server)

## Making HTML Output Accessible

Logi Report supports the accessibility HTML attributes and a built-in [accessible Server Console](#Server) for displaying reports in HTML. The implementation standard is based on HTML Specification 4.01 <http://www.w3.org/TR/WCAG10-HTML-TECHS/> and information on Section 508 Standards [http://www.section508.gov](http://www.section508.gov/) and [http://www.access-board.gov](http://www.access-board.gov/).

When designing a report in Designer, you can add these accessibility HTML attributes to the report objects to provide more readable and accessible HTML output.

**To add accessibility to a report in the HTML output**

1. Predefine the necessary accessibility attributes of the report objects when designing the report. When you select a report object in the design area, you can get these accessibility attributes in the [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735585381783-DBField-Properties#Accessibility) property group in the Properties sheet of the Report Inspector.

   ![Accessibility Properties](https://devnet.logianalytics.com/hc/article_attachments/9898477083543/frmt_acsbl_html.gif)
2. When exporting the report to HTML, select **Section 508 Compliant Output**. If you only want to convert table/crosstab components into HTML data table in the HTML output, select **Use HTML Data Table**. You can find these two options in all the HTML export UIs in Logi Report.

## Exporting Reports to Accessible PDF

You can also export your report to an accessible PDF by enabling the **Accessible PDF** option, which is available in all the PDF export UIs in Logi Report, so that users of screen readers and those who have low vision can have their tagged PDF read out aloud in appropriate language in the Adobe Acrobat software. The implementation standard is based on Web Content Accessibility Guidelines (WCAG) 2.0 (ISO/IEC 40500:2012) <http://www.w3.org/TR/WCAG/>and the PDF/UA (ISO 14289-1) <http://www.iso.org/standard/64599.html> standard.

Logi Report supports these PDF tags: Document, Part, Sect, Div, P, H1, H2, H3, H4, H5, H6, Table, TR, TH, TD, Span, Link, and Figure. When you select Accessible PDF to export a report to an accessible PDF, Logi Report automatically adds appropriate tags to the report objects in the PDF output, according to their display sequence in the report structure tree in the Report Inspector. For example, Logi Report adds the Document tag to the report body, the Part tag to a banded object in the report body, the Sect tag to a panel of the banded object, and the Div tag to a field in the banded panel. You can only customize the six heading tags using the [Tag Name](https://devnet.logianalytics.com/hc/en-us/articles/5735585381783-DBField-Properties#TagName) property for the following objects in Designer: DBFields, formula fields, parameter fields, summary fields, special fields, labels, and parameter controls.

### Adjusting the Reading Order of Report Objects in Accessible PDF

When you export a report to an accessible PDF, Logi Report exports the objects in the report according to their display sequence in the Report Inspector. When designing a report in Designer, you can adjust the object sequence to customize the order you want the screen reader to read them, by selecting an object and selecting **Up**![Up button](https://devnet.logianalytics.com/hc/article_attachments/9898404958359/btn_up.gif) or **Down**![Down button](https://devnet.logianalytics.com/hc/article_attachments/9898404966039/btn_down.gif) on the Report Inspector toolbar.

![Adjust Report Object Order for Accessible PDF](https://devnet.logianalytics.com/hc/article_attachments/9898460046615/frmt_acsbl_pdf.gif)

However, there are the following limitations:

* You can only move the objects the position of which are "absolute", and one object at a time.
* You can only adjust the order of the objects that are at the same layer in the report template, for example, the objects in the detail panel of a banded object.
* For the three main objects of a report, Report Body, TOC, and Datasets, you can only adjust the order of Report Body and TOC, and you cannot move the objects in the report body above the Page Panel object at the same layer.
* For the objects in the same tabular cell, you cannot move the objects that are contained in a paragraph.

## The Accessible Server Console

Server enables disabled users to visit the accessible version with simplified functionality to read reports by reader agent or other assistive tools. In the accessible version, Server displays reports in HTML with accessibility attributes, and outputs the table/crosstab components as HTML data tables. For more information, see Making HTML and PDF Report Outputs and Server Console Accessible in the *Logi Report Server Guide*.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735553344535-Exporting-Reports-to-Fax)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources)
