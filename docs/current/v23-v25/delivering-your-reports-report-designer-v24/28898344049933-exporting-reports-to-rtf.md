---
title: "Exporting Reports to RTF"
id: 28898344049933
section: "Delivering Your Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898344049933-Exporting-Reports-to-RTF
updated_at: 2024-09-30T09:13:14Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Exporting Reports to RTF

This topic describes how you can export a page or web report to a RTF file.

- Open the report that you want to export.

- Navigate to File > Export  >  To RTF. Designer displays the Export to RTF dialog box.
	

- By default, Designer saves the RTF file in the same folder and same name as the report file. You can type the destination directory and file name for the output in the Directory and File Name text boxes, or select Browse to specify the location and file name with File Explorer of your operating system. When the file name you specify does not contain the .rtf extension, Designer automatically adds the extension to the output file. If you want to use your preferred extension (or to have no extension) for the file name of the output, select Use Custom File Extension, then you can type your file name with any extension or no extension.

- When you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can select a report tab and select Move Up or Move Down to change the order of the report tabs.

- Select No Margin to remove the margins in the RTF output, which you set at report design time.

- Select Best Editing to apply the flow layout when exporting.

- Select Run Linked Report if you want to generate the reports that you link with the report (not including the detail reports) in the RTF output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

- Select OK to start exporting.

The following are some tips for you when exporting a report to RTF:

- Designer cannot export the Arc drawing object to a RTF file. 

- If you select Best Editing when export a report to RTF, the result can be edited easily, but the layout may be different from that you designed, because the Report RTF exporter cannot support some flow layout properties, such as Clear and Relative.

- In the Best Editing mode, one report just has one default tab which is in the last paragraph, so others are ignored.

- Microsoft Word Document limits the maximum page size in Word Print Layout to 22 inches. This may result in that when you export a report with many columns in the RTF format and then view it in Microsoft Word Document, the columns on the right get lost. If this happens, you can switch to Web Layout. If still not working, try a latest version of Microsoft Word Document.

Previous Topic  Next Topic
