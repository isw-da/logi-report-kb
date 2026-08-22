---
title: "Exporting Reports to PostScript"
id: 5735531904791
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735531904791-Exporting-Reports-to-PostScript
updated_at: 2022-11-02T07:57:54Z
---

# Exporting Reports to PostScript

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735516111511-Exporting-Reports-to-XML)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735553344535-Exporting-Reports-to-Fax)

# Exporting Reports to PostScript

This topic describes how you can export a page or web report to a PostScript file.

1. Open the report that you want to export.
2. Navigate to **File** > **Export** > **To PostScript**. Designer displays the [Export to PostScript dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513975319-Export-to-PostScript-Dialog-Box).

   ![Export to PostScript dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898459873943/expt2ps.gif)
3. By default, Designer saves the PostScript file in the same folder and same name as the report file. You can type the destination directory and file name for the output in the **Directory** and **File Name** text boxes, or select **Browse** to specify the location and file name with File Explorer of your operating system. When the file name you specify does not contain the .ps extension, Designer automatically adds the extension to the output file. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")If you want to use your preferred extension (or to have no extension) for the file name of the output, select **Use Custom File Extension**, then you can type your file name with any extension or no extension.
4. When you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can select a report tab and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to change the order of the report tabs. If you do not type the name, Designer uses the report name as PostScript file name by default.
5. Select **No Margin** if you want to remove the margins in the PostScript output, which you set at report design time.
6. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the PostScript output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
7. Select **OK** to start exporting.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When you export a report to a PostScript file, some objects in the output may be located imprecisely. You can print your report with PDF in order to get the accurate printed result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735516111511-Exporting-Reports-to-XML)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735553344535-Exporting-Reports-to-Fax)
