---
title: "Exporting Reports"
id: 5735544904599
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735544904599-Exporting-Reports
updated_at: 2022-11-02T07:57:50Z
---

# Exporting Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735531983767-Printing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735531881623-Exporting-Reports-to-Mail)

# Exporting Reports

This topic introduces how you can export page and web reports to different formats. It also describes the two useful configuration methods for customizing the page settings and layout precision of each export format.

You can export a page or web report to the following file formats:

* [Mail](https://devnet.logianalytics.com/hc/en-us/articles/5735531881623-Exporting-Reports-to-Mail)
* [Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/5735525374615-Exporting-Reports-to-Logi-Report-Result)
* [HTML](https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML)
* [PDF](https://devnet.logianalytics.com/hc/en-us/articles/5735531895447-Exporting-Reports-to-PDF)
* [Excel](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel)
* [Text](https://devnet.logianalytics.com/hc/en-us/articles/5735525405719-Exporting-Reports-to-Text)
* [RTF](https://devnet.logianalytics.com/hc/en-us/articles/5735531933591-Exporting-Reports-to-RTF)
* [XML](https://devnet.logianalytics.com/hc/en-us/articles/5735516111511-Exporting-Reports-to-XML)
* [PostScript](https://devnet.logianalytics.com/hc/en-us/articles/5735531904791-Exporting-Reports-to-PostScript)
* [Fax](https://devnet.logianalytics.com/hc/en-us/articles/5735553344535-Exporting-Reports-to-Fax)

## Customizing Page Settings for Report Outputs

Before exporting a report, you can customize the page settings for the output of each export format. For a library component, the page settings take effect when users export the library component in JDashbaord.

1. Navigate to **File** > **Page Setup**. Designer displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552285079-Page-Setup-Dialog-Box).
2. Select the **Export** tab.

   ![Page Setup dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/9898460005783/pgstup_expt19.2.gif)
3. Select a format from the **Export To** drop-down list.
4. ![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898423002391/___newv19.2.png "New for version 19.2.")By default, Designer applies [pagination mode](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Mode) to the output of the format for a page report tab or web report. Clear **Page Layout** if you want to apply continuous mode, so the output displays in a single page.
5. Designer enables the page options when you do not clear Page Layout and automatically applies the [page settings that you define in the General tab](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages#Setting) of the dialog box to the output of the format. You can clear **Auto** and specify different page settings for the output.
6. Select other formats to customize the page layout and page settings of the output.
7. Select **OK** to accept the settings.

When you clear the Auto option for an export format and select OK in the Page Setup dialog box, Designer adds a corresponding [export page setting object](https://devnet.logianalytics.com/hc/en-us/articles/5735533514391-Export-Page-Setting-Object-Properties) to the report structure tree in the Report Inspector. You can edit the page properties for the output of the export format there too. When you select the Auto option for this export format and select OK in the dialog box again, Designer removes its export page setting object automatically from the report structure tree.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Server also applies the page layout and page settings you specify for any export format when users advanced run and schedule to run the page report tab or web report in this format at runtime.

## Customizing the Layout Precision for Report Outputs

You can customize the layout precision to apply when exporting reports in Designer. However for page reports, the customized precision can take effect only in report tabs whose [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#PrecisionSensitive) property is "true".

1. Navigate to **File** > **Options**.
2. In the Options dialog box, select **Export to** in the **Category** box.
3. Select the **Layout Precision**. Designer displays the Advanced Export Settings dialog box.

   ![Advanced Export Settings dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898460014103/advexptsting.gif)
4. Select **Customize for each format**. By default, Designer selects **Optimize for speed over visual effect**, meaning, Designer decides the precision level which is oriented towards speed more than visualization.
5. Select **System Default Settings**, then in the Precision Settings dialog box, edit the precision level for each format and select **OK**.

   ![Precision Settings dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898477075863/prcsnsting.gif)

   Designer provides two precision levels: High and Low. High precision provides better layout but slower efficiency, while low precision brings higher performance but maybe poorer visual effect. If low precision can give reports well looks, it is reasonable to apply low precision because faster performance is guaranteed at the same time. By default, when you export a report to formats such as PDF, RTF, Excel, Fax, or PostScript, Designer exports the text with high precision, thus the report layout of these formats is different from other formats such as HTML, Logi Report Result, XML, and Text.
6. In the Advanced Export Settings dialog box, select the checkbox for the required formats to apply the defined precision level and select **OK**. For formats that you do not select, Designer determines their precision.
7. Select **OK** in the Options dialog box to apply the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can export a report in either design or view mode. However, if you modify the report after opening it, you should use view mode to export it. To do this, select the **View** tab, and then select **Refresh Data**![](https://devnet.logianalytics.com/hc/article_attachments/9898422095639/btn_refresh.gif) on the toolbar. Designer then refetches data in the report from the database. After that, you can export the report to the required format.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735531983767-Printing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735531881623-Exporting-Reports-to-Mail)
