---
title: "Exporting to Logi Report Result"
id: 4405664598551
section: "Delivering Your Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664598551-Exporting-to-Logi-Report-Result
updated_at: 2022-01-27T20:34:45Z
---

# Exporting to Logi Report Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664597271-Exporting-to-Mail)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664596375--Exporting-to-HTML)

# Exporting to Logi Report Result

A Logi Report result file is Logi Report's proprietary version of the report. You can open Logi Report result files on Server. This topic describes how you can export a page or web report to a Logi Report result file.

1. Open the report that you want to export.
2. Navigate to **File** > **Export**  > **To Logi Report Result**. Designer displays the [Export to Logi Report Result dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664478487-Export-to-Logi-Report-Result-Dialog-Box).

   ![Export to Logi Report Result dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550853655/expt2rst.gif)
3. Type a name and specify a directory for the result file. Designer exports a page report to a .rst file and a web report to a .wst file.
4. If you are exporting a page report, in the report tab box, select the report tabs in the page report that you want to export.
5. Select **Zip** if you want to export the report to a zip file.
6. From the **Precision Level** drop-down list, specify the precision level with which to export the report. The precision level you specify here has higher priority than [the one defined in the Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664595479-Exporting-Reports#Precision).

   For a page report, to make the specified precision take effect, you need to make sure that the [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#PrecisionSensitive) property of the selected page report tabs is "true".
7. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the result file. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
8. Select **OK** to start exporting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664597271-Exporting-to-Mail)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664596375--Exporting-to-HTML)
