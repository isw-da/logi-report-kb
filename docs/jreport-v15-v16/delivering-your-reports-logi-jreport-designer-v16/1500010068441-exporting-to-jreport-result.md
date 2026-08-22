---
title: "Exporting to JReport Result"
id: 1500010068441
section: "Delivering Your Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068441-Exporting-to-JReport-Result
updated_at: 2021-07-24T10:38:15Z
---

# Exporting to JReport Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033142-Exporting-to-Mail) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033122--Exporting-to-HTML)

# Exporting to JReport Result

A JReport result file is Logi JReport's proprietary version of the report result. JReport result files can be opened by Logi JReport Server.

To export the result of a report to a JReport result file, follow the steps below:

1. Open the report that is to be exported.
2. Select **File** > **Export**  > **To JReport Result**. The [Export to JReport Result](https://devnet.logianalytics.com/hc/en-us/articles/1500010030782-Export-to-Logi-JReport-Result-Dialog) dialog appears.

   ![Export to Logi JReport Result dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901164183/expt2rst.gif)
3. Type a name and specify a directory for the result file. A page report will be exported to a .rst file and a web report to a .wst file.
4. If you are exporting a page report, in the report tab box, select the report tabs in the page report you want to export.
5. If you want to export the report to a zip file, check the **Zip** option.
6. Specify the precision level with which you want to export the report from the Precision Level drop-down list. The precision level specified here has higher priority than [the one defined via the Options dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500010068401-Exporting-Report-Result#Precision).

   For a page report, to make the specified precision take effect, you need to make sure that the [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#PrecisionSensitive) property of the selected page report tabs is set to true.
7. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported result file. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
8. Select **OK** to start exporting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033142-Exporting-to-Mail) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033122--Exporting-to-HTML)
