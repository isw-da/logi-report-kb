---
title: "Exporting to PostScript"
id: 1500010099341
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099341-Exporting-to-PostScript
updated_at: 2021-07-23T19:16:11Z
---

# Exporting to PostScript

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099401-Exporting-to-XML)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099281-Exporting-to-Fax)

# Exporting to PostScript

This topic describes how you can export the result of a page or web report to a PostScript file.

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To PostScript**. Designer displays the [Export to PostScript dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058982-Export-to-PostScript-Dialog-Box).

   ![Export to PostScript dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848473751/expt2ps.gif)
3. Select the **Browse** button to specify the destination directory where to save the PostScript file and its file name. You can also type the location and file name manually in the **Directory** and **File Name** text boxes (make sure that the folder you specify does exist; otherwise, Designer displays an error message). If you do not type a name, Designer uses the report name as the PostScript file name by default.
4. If you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can make use of the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to change the order of the report tabs. If you do not type the name, Designer uses the report name as PostScript file name by default.
5. Select **No Margin** if you want to remove the margins in the PostScript output, which you set at report design time.
6. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the PostScript output. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
7. Select **OK** to start exporting.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When you export a report to a PostScript file, some objects in the output may be located imprecisely. You can print your report with PDF in order to get the accurate printed result. Therefore, you are recommended to export report to PDF rather than to PostScript.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099401-Exporting-to-XML)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099281-Exporting-to-Fax)
