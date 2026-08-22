---
title: "Exporting to PostScript"
id: 1500009589401
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589401-Exporting-to-PostScript
updated_at: 2021-07-24T05:54:41Z
---

# Exporting to PostScript

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589441-Exporting-to-XML)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568062-Exporting-to-Fax)

# Exporting to PostScript

To export the results of a report to a PostScript file, follow the steps below:

1. Open the report you want to export.
2. Select **File** > **Export**  > ****To** PostScript**. The [Export to PostScript](https://devnet.logianalytics.com/hc/en-us/articles/1500009586761-Export-to-PostScript-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893840279/expt2ps.gif)
3. Specify the directory where the export PostScript file will be saved. If the directory does not exist, an error message will be produced.
4. Enter the name for the exported file.
5. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839511/btn_mvup3.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839767/btn_mvdwn3.gif) to change the order or the report tabs.
6. Check **No Margin** if you want to remove the margins that have been set to the report at design time.
7. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported PostScript result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
8. When done, select **OK** to perform the export operation.

**Note:** When you export a report to a PostScript file, some objects in this report may be located imprecisely. You can print your report with PDF in order to get the accurate printed results. Therefore, you are recommended to export report to PDF rather than to PostScript.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589441-Exporting-to-XML)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568062-Exporting-to-Fax)
