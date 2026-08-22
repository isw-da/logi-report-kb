---
title: "Exporting to RTF"
id: 1500009589421
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589421-Exporting-to-RTF
updated_at: 2021-07-24T05:54:40Z
---

# Exporting to RTF

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568142-Exporting-to-Text)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589441-Exporting-to-XML)

# Exporting to RTF

To export the results of a report to an RTF format file, follow the steps below:

1. Open the report you want to export.
2. Select **File** > **Export**  > **To RTF**. The [Export to RTF](https://devnet.logianalytics.com/hc/en-us/articles/1500009565582-Export-to-RTF-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889309591/expt2rtf.gif)
3. Specify the directory and file name respectively in the Directory and File name text boxes. If you don't specify the name, Logi JReport will apply the report name as the default RTF file name.
4. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839511/btn_mvup3.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839767/btn_mvdwn3.gif) to change the order of the report tabs.
5. Check the **No Margin** checkbox to remove the margins that are originally set while you design the report.
6. Check **Best Editing** to apply the flow layout when exporting.
7. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported RTF result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
8. Select **OK**, and a file with the extension .rtf will be generated.

**Notes:**

* If Best Editing is checked, the results can be edited easily, but the layout may be different from that you designed, because some flow layout properties will not be supported by Logi JReport RTF exporter, such as clear, relative and so on.
* In the Best Editing mode, one report just has one default tab which is in the last paragraph, so others will be ignored.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568142-Exporting-to-Text)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589441-Exporting-to-XML)
