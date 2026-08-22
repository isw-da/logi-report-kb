---
title: "Exporting Reports"
id: 4405664595479
section: "Delivering Your Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664595479-Exporting-Reports
updated_at: 2022-01-27T20:34:44Z
---

# Exporting Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664599447-Printing-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664597271-Exporting-to-Mail)

# Exporting Reports

This topic introduces how you can export page and web reports to different formats. It also describes the two useful configuration methods for customizing the page properties and layout precision of each export format.

You can export a page or web report to the following file formats:

* [Mail](https://devnet.logianalytics.com/hc/en-us/articles/4405664597271-Exporting-to-Mail)
* [Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/4405664598551-Exporting-to-Logi-Report-Result)
* [HTML](https://devnet.logianalytics.com/hc/en-us/articles/4405664596375--Exporting-to-HTML)
* [PDF](https://devnet.logianalytics.com/hc/en-us/articles/4405661756567-Exporting-to-PDF)
* [Excel](https://devnet.logianalytics.com/hc/en-us/articles/4405661753751-Exporting-to-Excel)
* [Text](https://devnet.logianalytics.com/hc/en-us/articles/4405661760663-Exporting-to-Text)
* [RTF](https://devnet.logianalytics.com/hc/en-us/articles/4405661759255-Exporting-to-RTF)
* [XML](https://devnet.logianalytics.com/hc/en-us/articles/4405661761687-Exporting-to-XML)
* [PostScript](https://devnet.logianalytics.com/hc/en-us/articles/4405661757591-Exporting-to-PostScript)
* [Fax](https://devnet.logianalytics.com/hc/en-us/articles/4405661755031-Exporting-to-Fax)

## Customizing the Page Properties for Each Export Format

Before exporting a report, you can customize the page properties for the output of each export format.

1. Navigate to **File** > **Page Setup**. Designer displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664543511-Page-Setup-Dialog-Box).
2. Select the **Export** tab.

   ![Page Setup dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4420402386583/pgstup_export.gif)
3. By default, Designer applies the [properties that you define for the report page](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#Setting) in the General tab of the dialog box to the output of all export formats. You can customize the page properties for each export format respectively: select a format from the **Export To** drop-down list, clear **Auto** and then edit the properties.
4. Select **OK** to accept the settings.

When you clear the Auto option for an export format and select OK in the Page Setup dialog box, Designer adds a corresponding [export page setting object](https://devnet.logianalytics.com/hc/en-us/articles/4405664667799-Export-Page-Setting-Object-Properties) to the report structure tree in the Report Inspector. You can edit the page properties for the output of the export format there too. When you select the Auto option for this export format and select OK in the dialog box again, Designer removes its export page setting object automatically from the report structure tree.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) Server also applies the page properties you specify for any export format when users advanced run and schedule to run the report in this format at runtime.

## Customizing the Layout Precision

You can customize the layout precision to apply when exporting reports in Designer. However for page reports, the customized precision can take effect only in report tabs whose [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#PrecisionSensitive) property is "true".

1. Navigate to **File** > **Options**.
2. In the Options dialog box, select **Export to** in the **Category** box.
3. Select the **Layout Precision**. Designer displays the Advanced Export Settings dialog box.

   ![Advanced Export Settings dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420394712215/advexptsting.gif)
4. Select **Customize for each format**.

   By default, Designer selects **Optimize for speed over visual effect**, meaning, Designer decides the precision level which is oriented towards speed more than visualization.
5. Select **System Default Settings**, then in the Precision Settings dialog box, edit the precision level for each format and select **OK**.

   ![Precision Settings dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410651799/prcsnsting.gif)

   Designer provides two precision levels: High and Low. High precision provides better layout but slower efficiency, while low precision brings higher performance but maybe poorer visual effect. If low precision can give reports well looks, it is reasonable to apply low precision because faster performance is guaranteed at the same time. By default, when you export a report to formats such as PDF, RTF, Excel, Fax, or PostScript, Designer exports the text with high precision, thus the report layout of these formats is different from other formats such as HTML, Logi Report Result, XML, and Text.
6. In the Advanced Export Settings dialog box, select the checkbox for the required formats to apply the defined precision level and select **OK**. For formats that you do not select, Designer decides their precision.
7. Select **OK** in the Options dialog box to apply the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) You can export a report in either design or view mode; however, if you modify the report after opening it, you should use view mode to export it. To do this, select the **View** tab, and then select **Refresh Data**![](https://devnet.logianalytics.com/hc/article_attachments/4420402316311/btn_refresh.gif) on the toolbar. Designer then refetches data in the report from the database. After that, you can export the report to the required format.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664599447-Printing-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664597271-Exporting-to-Mail)
