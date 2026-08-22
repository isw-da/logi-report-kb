---
title: "Exporting Reports to Logi Report Result"
id: 12480208856461
section: "Delivering Your Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480208856461-Exporting-Reports-to-Logi-Report-Result
updated_at: 2026-02-25T23:48:29Z
source_host: docs-report.zendesk.com
---
# 
Exporting Reports to Logi Report Result

A Logi Report result file is Report's proprietary version of the report. You can open Logi Report result files on Server. This topic describes how you can export a page or web report to a Logi Report result file.

- Open the report that you want to export.

- Navigate to File > Export  > To Logi Report Result. Designer displays the Export to Logi Report Result dialog box.
    

- From the Save in drop-down list, specify where you want to save the result file.

- By default, Designer saves the result file in the same name as the report file with the .rst extension for a page report and .wst for a web report. You can type another name for the result file in the File name text box. When the file name you specify does not contain the .rst/.wst extension, Designer automatically adds the extension to the output file. If you want to use your preferred extension (or to have no extension) for the file name of the output, select Use Custom File Extension, then you can type your file name with any extension or no extension.

- When you are exporting a page report, in the report tab box, select the report tabs in the page report that you want to export.

- Select Zip if you want to export the report to a zip file.

- From the Precision Level drop-down list, specify the precision level with which  to export the report. The precision level you specify here has higher priority than the one defined in the Options dialog box.
     For a page report, to make the specified precision take effect, you need to make sure that the Precision Sensitive property of the selected page report tabs is "true".

- Select Run Linked Report if you want to generate the reports that you link with the report (not including the detail reports) in the result file. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

- Select OK to start exporting.
