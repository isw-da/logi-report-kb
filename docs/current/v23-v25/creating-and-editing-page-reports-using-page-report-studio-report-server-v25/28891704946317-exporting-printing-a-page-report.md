---
title: "Exporting/Printing a Page Report"
id: 28891704946317
section: "Creating and Editing Page Reports Using Page Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891704946317-Exporting-Printing-a-Page-Report
updated_at: 2026-02-26T02:13:37Z
source_host: docs-report.zendesk.com
---
# 
Exporting/Printing a Page Report 

When you are satisfied with a report, you may want to export it to other formats or print it. This topic describes how you can export and print a page report.

This topic contains the following sections:

- Exporting a Page Report

- Printing a Page Report

## 
Exporting a Page Report

 You can export a report as a result version or as a local file to other formats. However, if the report you are going to export is linked to another report, in the exported report the link will no longer be available.

- Select Menu > File > Export, or the Export button  on the toolbar to display the Export dialog box.
    

- In the File Name field, specify the name of the exported report file.

- Specify the destination of the report:
    
- 
View Report Result: Select to directly open the report in the web browser if the format is supported by a plug-in of the web browser; otherwise Server will prompt you to save the report file.

- 
Save to File System: Select if you want the web browser to prompt you to save the report file to a specified folder. You need to provide a name for the report file in the File Name field.

- 
Save to Version System: Select to save the report as a result version in Report Server's versioning system.

- In the Select Report Tabs box, select the report tabs you want to export. Server will export the selected report tabs in the list order. You can change the order of the report tabs by selecting  or .

- From the Select Format drop-down list, select the format in which you want to export the report: HTML, PDF, Excel, Text, RTF, XML, PostScript, or Page Report Result.

- To specify the additional setting of the selected format, select  More Options.

- From the Style Group drop-down list, select the style group you want to apply to the exported report output. If the page report is created in Report Designer, when you specify the <No Style> item, the style group property predefined for specific export format in Report Designer will apply to export the report to that format.

- Set the other properties for the selected format as you want.

- Select OK to confirm.

Tip: Before exporting a report, you can customize the page properties for each exported output. For more information, see Setting up the report page.

## 
Printing a Page Report

You can print the current page report to a PDF or HTML file.

- Select Menu > File > Printable Version, or the Printable Version button  on the toolbar. Server displays the Printable Version dialog box.
    

- Specify whether to print the current report tab or multiple report tabs in the current report.

- Select the format in which you want to print the report: PDF or HTML.

- When you only want to print the current report tab, specify the range of the pages in the report tab that you want to print.
    
- 
All
          If the option is selected, all pages in the current report tab will be printed.

- 
Current Page
        If the option is selected, only the current page of the report tab will be printed.

- 
Pages
        If the option is selected, you can define the pages in the current report tab that you want to print. Separate the page numbers and/or page ranges by commas.

When you want to print multiple report tabs in the current report, select the report tabs you want and adjust the printing order of the report tabs by selecting  and .

- Select Apply. Server opens the PDF or HTML output file in an associated program with which you can print it to a printer.
