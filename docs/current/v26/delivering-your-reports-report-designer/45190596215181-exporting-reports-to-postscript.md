---
title: "Exporting Reports to PostScript"
id: 45190596215181
section: "Delivering Your Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190596215181-Exporting-Reports-to-PostScript
updated_at: 2026-04-30T15:15:08Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Exporting Reports to PostScript

This topic describes how you can export a page or web report to a PostScript file.

- Open the report that you want to export.

- Navigate to File > Export > To PostScript. Designer displays the Export to PostScript dialog box.
	

- By default, Designer saves the PostScript file in the same folder and same name as the report file. You can type the destination directory and file name for the output in the Directory and File Name text boxes, or select Browse to specify the location and file name with File Explorer of your operating system. When the file name you specify does not contain the .ps extension, Designer automatically adds the extension to the output file. If you want to use your preferred extension (or to have no extension) for the file name of the output, select Use Custom File Extension, then you can type your file name with any extension or no extension.

- When you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can select a report tab and select Move Up or Move Down to change the order of the report tabs.  If you do not type the name, Designer uses the report name as PostScript file name by default.

- Select No Margin if you want to remove the margins in the PostScript output, which you set at report design time.

- Select Run Linked Report if you want to generate the reports that you link with the report (not including the detail reports) in the PostScript output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

- Select OK to start exporting.

 When you export a report to a PostScript file, some objects in the output may be located imprecisely. You can print your report with PDF in order to get the accurate printed result.
