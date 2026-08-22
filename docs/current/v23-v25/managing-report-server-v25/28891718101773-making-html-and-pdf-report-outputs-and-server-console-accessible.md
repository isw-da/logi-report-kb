---
title: "Making HTML and PDF Report Outputs and Server Console Accessible"
id: 28891718101773
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891718101773-Making-HTML-and-PDF-Report-Outputs-and-Server-Console-Accessible
updated_at: 2026-02-26T02:13:26Z
source_host: docs-report.zendesk.com
---
# 
Making HTML and PDF Report Outputs and Server Console Accessible 

You can export reports to accessible HTML and PDF outputs and enable the accessible version of Report  Server for people who experience disabilities or have special needs, so they can access the reports using assistive tools. This topic describes how you can add accessibility to HTML outputs, export reports to accessible PDF files, and enable the accessible version of Report  Server. It also briefly introduces the functionality of the accessible version of Report Server.

This topic contains the following sections:

- Exporting Reports to Accessible PDF Files

- Making HTML Format Report Output Accessible

- Visiting the Accessible Version of Report Server

## 
Exporting Reports to Accessible PDF Files 

You can export reports to accessible PDF files,  by enabling the Accessible PDF option which is available on all PDF export UIs in Report, so that users of screen readers and those who have low vision can have their tagged PDF files read out aloud in appropriate language in the Adobe Acrobat software. The implementation standard is based on Web Content Accessibility Guidelines (WCAG) 2.0 (ISO/IEC 40500:2012) http://www.w3.org/TR/WCAG/and the PDF/UA (ISO 14289-1) standard http://www.iso.org/standard/64599.html.

Report supports these PDF tags: Document, Part, Sect, Div, P, H1, H2, H3, H4, H5, H6, Table, TR, TH, TD, Span, Link, and  Figure. When you select Accessible PDF to export a report to an accessible PDF, Report automatically adds appropriate tags to the report objects in the PDF output, according to their display sequence in the report structure tree in the Report Designer's Inspector. For example, Report adds the Document tag to the report body, the Part tag to a banded object in the report body, the Sect tag to a panel of the banded object, and the Div tag to a field in the banded panel. You can only customize the six heading tags using the Tag Name property for the following objects in Designer: DBFields, formula fields, parameter fields, summary fields, special fields, labels, and parameter controls.

## 
Making HTML Format Report Output Accessible

Report supports accessibility related HTML attributes and a built-in accessible Server Console for displaying reports in HTML. The implementation standard is based on HTML specification 4.01 http://www.w3.org/TR/WCAG10-HTML-TECHS/ and information on Section 508 Standards http://www.access-board.gov. 

When designing a report in Report Designer, you can add the accessibility related HTML attributes to the report elements in order to make the HTML format output more readable and accessible. You can find those attributes in the Accessibility category of the Report Inspector. 

To add accessibility to a report in the HTML format:

- Predefine necessary accessibility attributes when designing the report in Designer.

- Enable Section 508 compliant output when exporting the report to HTML format.
      In the HTML export UI, select Section 508 Compliant Output. If you only want to convert table/crosstab components into HTML data table in the HTML format report output, select Use HTML Data Table.

The preceding two options are available on all HTML export UIs in Report.

## 
Visiting the Accessible Version of Report Server

You can visit the accessible version of Report Server with simplified functionality to read reports by reader agent or other assistive tools. In the accessible version, Report Server displays reports  in the HTML format with accessibility attributes and displays table/crosstab components as HTML data tables.

You can use the option - Use Accessible Version - to set the accessible version of Report Server as the default portal UI. The default port for accessible version is 8888 which is also the default port for the Server Console in normal version. That is to say, the Use Accessible Version option controls switching between normal version and accessible version of Report Server UI when signing in to port 8888. By default, this option is unselected and you are directed to the Server Console in normal version. 

The server administrator can activate the accessible version for all users or for an individual user:

- 
For all users:
- On the system toolbar of the Server Console, navigate to Administration > Server Profile > Customize Server Preferences.

- Select the Advanced tab. 

- Select Use Accessible Version. 

- Select OK to apply the change.

- 
For an individual user:
- On the system toolbar of the Server Console, navigate to Administration > Security > User.

- Locate the wanted user ID, then select Preference for the user. 

- In the Preference dialog box, go to the Advanced tab. 

- Select Use Accessible Version.

- Select OK to save the change.

You can also enable the accessible version for yourself in the following way:

- On the Server Console, navigate to  My Profile > Customize Server Preferences on the system toolbar

- Select the Advanced tab.

- Select Use Accessible Version.

- Select OK to save the change.

After you have been enabled the access to Accessible Version, you will be directed to the accessible version after signing in next time. You can navigate through the server resource to view the target report, with the help of reader agent.

See the main options on the accessible version UI:

- 
Directory Path
The current directory where you have come to follow the server resource tree.

- 
Up to Higher Level Directory
Select to go to the parent level folder. 

- 
Up to Top Level Directory
Select to go to the default portal page.

- 
Leave Accessible Version
Select to go to the normal version of the Server Console with full functionalities. You'd better not leave the accessible version unless having others' help. Once you leave the accessible version, there is no way to return unless you re-sign in.

- 
Select User Directory
You can choose to open either the My Reports folder or the Public Reports folder.

- 
Catalog
The catalogs in the current directory.

- 
Report List
The folders and reports in the current directory. You can select the hyperlinks in the Name column to open them.
