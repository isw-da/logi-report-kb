---
title: "Exporting Reports to Accessible HTML and PDF"
id: 45190617271821
section: "Delivering Your Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190617271821-Exporting-Reports-to-Accessible-HTML-and-PDF
updated_at: 2026-04-30T15:15:06Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Exporting Reports to Accessible HTML and PDF

To help users who experience disabilities or have special needs use your reports, you can export the reports to both accessible HTML and PDF, so that they can read the reports with assistive tools. This topic describes how you can add accessibility to your HTML output and export your reports to accessible PDF. It also briefly introduces the accessible Server Console.

This topic contains the following sections:

- Making HTML Output Accessible

- 
Exporting Reports to Accessible PDF- Adjusting the Template Object Order  in  Accessible PDF

- The Accessible Server Console

## 
Making HTML Output Accessible

Report supports the accessibility HTML attributes and a built-in accessible Server Console for displaying reports in HTML. The implementation standard is based on HTML Specification 4.01 and information on Section 508 Standards (www.section508.gov and www.access-board.gov).

When designing a report in Designer, you can add these accessibility HTML attributes to the report objects to provide more readable and accessible HTML output.

To add accessibility to a report in the HTML output

- Predefine the necessary accessibility attributes of the report objects when designing the report. When you select a report object in the design area, you can get these accessibility attributes in the Accessibility property group in the Properties sheet of the Report Inspector.
				

- When exporting the report to HTML, select Section 508 Compliant Output. If you only want to convert table/crosstab components into HTML data table in the HTML output, select Use HTML Data Table. You can find these two options  in all the HTML export UIs in Report.
			    

 

## 
Exporting Reports to Accessible PDF

You can also export your report to an accessible PDF by enabling the Accessible PDF option, which is available in all the PDF export UIs in Report, so that users of screen readers and those who have low vision can have their tagged PDF read out aloud in appropriate language in the Adobe Acrobat software.  The implementation standard is based on Web Content Accessibility Guidelines (WCAG) 2.0 (ISO/IEC 40500:2012) and the PDF/UA (ISO 14289-1) standard.

Report supports these PDF tags: Document,  Part, Sect, Div, P, H1, H2, H3, H4, H5, H6, Table, TR, TH, TD, Span, Link, and  Figure. When you export a report to an accessible PDF, Report automatically adds appropriate tags to the report objects in the PDF output. For example, Report adds the Document tag to the report body, the Part tag to a banded object in the report body, the Sect tag to a panel of the banded object, and the Div tag to a field in the banded panel. You can only customize the six heading tags using the Tag Name property for the following objects in Designer: DBFields, formula fields, parameter fields, summary fields, special fields, labels, and parameter controls.

In the PDF export UIs, you can select the Setting button to specify in which order you want Report to add tags to the report objects in the accessible PDF.

- 
Template Object Order
Select to add tags to the report objects according to their order in the report template, which is determined by their display sequence in the report structure tree in the Report Inspector of Designer.

- 
Page Coordinate Order
Select to add tags to the report objects according to their coordinate on the report pages. Report tags the object with the smallest Y value on each page first, and when two objects have the same Y value,  the object with smaller X value first. When the difference between the Y values of two objects is less than 40 (0.5 point), Report considers them having the same Y value.

### 
Adjusting the Template Object Order in  Accessible PDF

When designing a report in Designer, you can adjust the display sequence of the report objects in  the Report Inspector to specify their order in the report template, so when you apply Template Object Order to the accessible PDF of the report, Report adds tags to the report objects according to this sequence. 

To adjust the display sequence of the report objects in  the report structure tree,  select an object and select Up or Down on the Report Inspector toolbar. 

However, there are the following limitations:

- You can only move the objects the position of which are "absolute", and one object at a time.

- You can only adjust the order of the objects that are at the same layer in the report template, for example, the objects in the detail panel of a banded object.

- For the three main objects of a report, Report Body, TOC, and Datasets, you can only adjust the order of Report Body and TOC, and you cannot move the objects in the report body above the Page Panel object at the same layer.

- For the objects in the same tabular cell, you cannot move the objects that are contained in a paragraph.

## 
The Accessible Server Console

Server enables disabled users to visit the accessible version with simplified functionality to read reports by reader agent or other assistive tools. In the accessible version,  Server displays reports in HTML with accessibility attributes, and outputs the table/crosstab components as HTML data tables. For more information, see Making HTML and PDF Report Outputs and Server Console Accessible in the Report Server Guide.
