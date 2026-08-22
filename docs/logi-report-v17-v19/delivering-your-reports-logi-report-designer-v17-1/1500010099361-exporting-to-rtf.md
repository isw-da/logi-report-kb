---
title: "Exporting to RTF"
id: 1500010099361
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099361-Exporting-to-RTF
updated_at: 2021-07-23T19:16:12Z
---

# Exporting to RTF

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099381-Exporting-to-Text)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099401-Exporting-to-XML)

# Exporting to RTF

This topic describes how you can export the result of a page or web report to a RTF file.

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To RTF**. Designer displays the [Export to RTF dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059022-Export-to-RTF-Dialog-Box).

   ![Export to RTF dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856876055/expt2rtf.gif)
3. Select the **Browse** button to specify the destination directory where to save the RTF and its file name. You can also type the location and file name manually in the **Directory** and **File Name** text boxes (make sure that the folder you specify does exist; otherwise, Designer displays an error message). If you do not type a name, Designer uses the report name as the RTF file name by default.
4. If you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can make use of the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to change the order of the report tabs.
5. Select the **No Margin** checkbox to remove the margins in the RTF output, which you set at report design time.
6. Select **Best Editing** to apply the flow layout when exporting.
7. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the RTF output. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
8. Select **OK** to start exporting.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* Designer cannot export the Arc drawing object to a RTF file.
* If you select Best Editing when export a report to RTF, the result can be edited easily, but the layout may be different from that you designed, because the Logi Report RTF exporter cannot support some flow layout properties, such as Clear and Relative.
* In the Best Editing mode, one report just has one default tab which is in the last paragraph, so others are ignored.
* Microsoft Word Document limits the maximum page size in Word Print Layout to 22 inches. This may result in that when you export a report with many columns in the RTF format and then view it in Microsoft Word Document, the columns on the right get lost. If this happens, you can switch to Web Layout. If still not working, try a latest version of Microsoft Word Document.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099381-Exporting-to-Text)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099401-Exporting-to-XML)
