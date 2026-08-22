---
title: "Exporting Reports to Logi Report Result"
id: 5735525374615
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735525374615-Exporting-Reports-to-Logi-Report-Result
updated_at: 2022-11-02T07:57:55Z
---

# Exporting Reports to Logi Report Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735531881623-Exporting-Reports-to-Mail)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML)

# Exporting Reports to Logi Report Result

A Logi Report result file is Logi Report's proprietary version of the report. You can open Logi Report result files on Server. This topic describes how you can export a page or web report to a Logi Report result file.

1. Open the report that you want to export.
2. Navigate to **File** > **Export**  > **To Logi Report Result**. Designer displays the [Export to Logi Report Result dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565857815-Export-to-Logi-Report-Result-Dialog-Box).

   ![Export to Logi Report Result dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898459854743/expt2rst.gif)
3. From the **Save in** drop-down list, specify where you want to save the result file.
4. By default, Designer saves the result file in the same name as the report file with the .rst extension for a page report and .wst for a web report. You can type another name for the result file in the **File name** text box. When the file name you specify does not contain the .rst/.wst extension, Designer automatically adds the extension to the output file. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")If you want to use your preferred extension (or to have no extension) for the file name of the output, select **Use Custom File Extension**, then you can type your file name with any extension or no extension.
5. When you are exporting a page report, in the report tab box, select the report tabs in the page report that you want to export.
6. Select **Zip** if you want to export the report to a zip file.
7. From the **Precision Level** drop-down list, specify the precision level with which to export the report. The precision level you specify here has higher priority than [the one defined in the Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports#Precision).

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) For a page report, to make the specified precision take effect, you need to make sure that the [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#PrecisionSensitive) property of the selected page report tabs is "true".
8. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the result file. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
9. Select **OK** to start exporting.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735531881623-Exporting-Reports-to-Mail)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML)
