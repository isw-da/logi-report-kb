---
title: "Exporting to RTF"
id: 1500010068461
section: "Delivering Your Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068461-Exporting-to-RTF
updated_at: 2021-07-24T10:38:14Z
---

# Exporting to RTF

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068481-Exporting-to-Text) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033182-Exporting-to-XML)

# Exporting to RTF

This topic shows how to export the results of a report to a RTF format file.

1. Open the report you want to export.
2. Select **File** > **Export**  > **To RTF**. The [Export to RTF](https://devnet.logianalytics.com/hc/en-us/articles/1500010066021-Export-to-RTF-Dialog) dialog appears.

   ![Export to RTF dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901163927/expt2rtf.gif)
3. Select the **Browse** button to specify the destination directory where the exported RTF file will be placed and the name of the file. You can also input the location and file name manually in the Directory and File Name text boxes (make sure that the folder you specify does exist, otherwise an error message will be produced).
4. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404901163415/btn_mvup3.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404901163671/btn_mvdwn3.gif) to change the order of the report tabs.
5. Check the **No Margin** checkbox to remove the margins in the RTF result, which are set at report design time.
6. Check **Best Editing** to apply the flow layout when exporting.
7. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the RTF result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
8. Select **OK** to start exporting.

**Notes:**

* The Arc drawing object cannot be exported to a RTF file.
* If Best Editing is checked, the result can be edited easily, but the layout may be different from that you designed, because some flow layout properties will not be supported by Logi JReport RTF exporter, such as clear, relative and so on.
* In the Best Editing mode, one report just has one default tab which is in the last paragraph, so others will be ignored.
* Microsoft Word Document limits the maximum page size in Word Print Layout to 22 inches. This may result in that when you export a report with many columns in the RTF format and then view it in Microsoft Word Document the columns on the right get lost. If this happens you can switch to Web Layout. If still not working, try a latest version of Microsoft Word Document.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068481-Exporting-to-Text) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033182-Exporting-to-XML)
