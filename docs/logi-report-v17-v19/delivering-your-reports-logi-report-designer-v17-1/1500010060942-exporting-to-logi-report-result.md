---
title: "Exporting to Logi Report Result"
id: 1500010060942
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060942-Exporting-to-Logi-Report-Result
updated_at: 2021-07-23T19:16:11Z
---

# Exporting to Logi Report Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060922-Exporting-to-Mail)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099301--Exporting-to-HTML)

# Exporting to Logi Report Result

A Logi Report result file is Logi Report's proprietary version of the report result. You can open Logi Report result files on Server. This topic describes how you can export a page or web report to a Logi Report result file.

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To Logi Report Result**. Designer displays the [Export to Logi Report Result dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059002-Export-to-Logi-Report-Result-Dialog-Box).

   ![Export to Logi Report Result dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856876439/expt2rst.gif)
3. Type a name and specify a directory for the result file. Designer exports a page report to a .rst file and a web report to a .wst file.
4. If you are exporting a page report, in the report tab box, select the report tabs in the page report that you want to export.
5. If you want to export the report to a zip file, select the **Zip** checkbox.
6. From the **Precision Level** drop-down list, specify the precision level with which to export the report. The precision level you specify here has higher priority than [the one defined in the Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result#Precision).

   For a page report, to make the specified precision take effect, you need to make sure that the [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#PrecisionSensitive) property of the selected page report tabs is true.
7. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the result file. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
8. Select **OK** to start exporting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060922-Exporting-to-Mail)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099301--Exporting-to-HTML)
