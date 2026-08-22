---
title: "Exporting to Logi JReport Result"
id: 1500009568122
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568122-Exporting-to-Logi-JReport-Result
updated_at: 2021-07-24T05:54:39Z
---

# Exporting to Logi JReport Result

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568102-Exporting-to-Mail)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568082-Exporting-to-HTML)

# Exporting to Logi JReport Result

A Logi JReport result file is Logi JReport's proprietary version of the report results. Logi JReport result files can be opened by Logi JReport Server.

**To export the results of a report to Logi JReport result:**

1. Open the report that is to be exported.
2. Select **File** > **Export**  > **To****Logi JReport Result**. The [Export to Logi JReport Result](https://devnet.logianalytics.com/hc/en-us/articles/1500009586781-Export-to-Logi-JReport-Result-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893840023/expt2rst.gif)
3. Type a name and specify a directory for the result file. A page report will be exported to a .rst file and a web report to a .wst file.
4. If you are exporting a page report, in the report tab box, select the report tabs in the page report you want to export.
5. If you want to export the report to a zip file, check the **Zip** option.
6. Specify the precision level with which you want to export the report from the Precision Level drop-down list. The precision level specified here has higher priority than the one defined via the [Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog#Export) dialog.

   For a page report, to make the specified precision take effect, you need to make sure that the [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#PrecisionSensitive) property of the selected page report tabs is set to true.
7. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported result file. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
8. Select **OK**, and the result file will then be generated in the specified directory.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568102-Exporting-to-Mail)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568082-Exporting-to-HTML)
