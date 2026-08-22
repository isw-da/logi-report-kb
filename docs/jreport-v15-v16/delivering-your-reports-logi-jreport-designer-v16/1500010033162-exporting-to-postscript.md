---
title: "Exporting to PostScript"
id: 1500010033162
section: "Delivering Your Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033162-Exporting-to-PostScript
updated_at: 2021-07-24T10:38:15Z
---

# Exporting to PostScript

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033182-Exporting-to-XML) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033102-Exporting-to-Fax)

# Exporting to PostScript

This topic introduces how to export the results of a report to a PostScript file.

1. Open the report you want to export.
2. Select **File** > **Export**  > ****To** PostScript**. The [Export to PostScript](https://devnet.logianalytics.com/hc/en-us/articles/1500010066001-Export-to-PostScript-Dialog) dialog appears.

   ![Export to PostScript dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901164439/expt2ps.gif)
3. Select the **Browse** button to specify the destination directory where the exported PostScript file will be placed and the name of the file. You can also input the location and file name manually in the Directory and File Name text boxes (make sure that the folder you specify does exist, otherwise an error message will be produced).
4. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404901163415/btn_mvup3.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404901163671/btn_mvdwn3.gif) to change the order of the report tabs.
5. Check **No Margin** if you want to remove the margins in the exported PostScript result, which are set at report design time.
6. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported PostScript result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
7. Select **OK** to start exporting.

**Note:** When you export a report to a PostScript file, some objects in this report may be located imprecisely. You can print your report with PDF in order to get the accurate printed result. Therefore, you are recommended to export report to PDF rather than to PostScript.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033182-Exporting-to-XML) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033102-Exporting-to-Fax)
