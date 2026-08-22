---
title: "Exporting Report Result"
id: 1500009634061
section: "Delivering Your Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634061-Exporting-Report-Result
updated_at: 2021-07-24T16:04:00Z
---

# Exporting Report Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611102-Printing-Report-Result) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634121-Exporting-to-Mail)

# Exporting Report Result

This topic introduces the exporting formats for report results.

You can export the result of a report to the following file formats:

* [To Mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009634121-Exporting-to-Mail)
* [To Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500009611042-Exporting-to-Logi-Report-Result)
* [To HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009610982--Exporting-to-HTML)
* [To PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500009611002-Exporting-to-PDF)
* [To Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009634081-Exporting-to-Excel)
* [To Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009611082-Exporting-to-Text)
* [To RTF](https://devnet.logianalytics.com/hc/en-us/articles/1500009634141-Exporting-to-RTF)
* [To XML](https://devnet.logianalytics.com/hc/en-us/articles/1500009634181-Exporting-to-XML)
* [To PostScript](https://devnet.logianalytics.com/hc/en-us/articles/1500009611022-Exporting-to-PostScript)
* [To Fax](https://devnet.logianalytics.com/hc/en-us/articles/1500009610962-Exporting-to-Fax)

## Customizing the Page Properties for Each Result Type

Before exporting a report, you can customize the page properties for each result type as follows:

1. Select **File** > **Page Setup**. The [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009609582-Page-Setup-Dialog) dialog appears.
2. Switch to the **Export** tab.

   ![Page Setup dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4404911672215/pgstup_export.gif)
3. By default, the [properties defined for the report page](https://devnet.logianalytics.com/hc/en-us/articles/1500009613402-Designing-the-Report-Pages#Setting) in the General tab of the dialog will be applied to the exported result of all export formats. To define the page properties for each exported result, select a format from the Export To drop-down list, clear the **Auto** option and then define the properties as you want. Repeat this to define the properties for all formats.
4. Select **OK** to accept the settings. The page properties specified for any export format will also be applied when advanced running and scheduling to run the report in this format on Logi Report Server.

When you clear the Auto option for an export format and select OK in the Page Setup dialog, a corresponding [export page setting object](https://devnet.logianalytics.com/hc/en-us/articles/1500009635581-Export-Page-Setting-Object-Properties) will be added to the report structure tree in the Report Inspector. You can edit the export page properties there too. When you select the Auto option for this export format and select OK in the dialog again, its export page setting object will be removed automatically from the report structure tree.

## Customizing the Layout Precision

You can customize the layout precision that will be applied when exporting reports in Logi Report Designer. However for page reports, the customized precision can take effect only in report tabs whose [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#PrecisionSensitive) property is set to true.

1. Select **File** > **Options**.
2. In the Options dialog, select **Export to** in the Category box.
3. Select the **Layout Precision** button to open the Advanced Export Settings dialog.

   ![Advanced Export Settings dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904228119/advexptsting.gif)
4. Select **Customize for each format**.

   By default, Optimize for speed over visual effect is selected, which means Logi Report will decide the precision level which is oriented towards speed more than visualization.
5. Select the **System Default Settings** button, then in the Precision Settings dialog, edit the precision level for each format and select **OK**.

   ![Precision Settings dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911672471/prcsnsting.gif)

   Logi Report provides two precision levels: high and low. High precision provides better layout but slower efficiency while low precision brings higher performance but maybe poorer visual effect. If low precision can give reports well looks, it is reasonable to apply low precision for at the same time faster performance is guaranteed. By default when exporting a report to formats such as PDF, RTF, Excel, Fax or PostScript, the text will be exported with high precision. Thus the report result layouts of these formats are different from the other formats such as HTML, Logi Report Result, XML, and Text.
6. In the Advanced Export Settings dialog, select the checkbox for the required formats to apply the defined precision level and select **OK**. For formats that are not selected, Logi Report will decide their precision.
7. Select **OK** in the Options dialog to apply the settings.

**Note:** You can export the report result in either design or view mode. However, if you modify the report after opening it, it is recommended to use view mode to export the report result. To do this, select the **View** tab, and then select the **Refresh Data** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404911595287/btn_refresh.gif) on the toolbar. Data in the report will then be re-fetched from the database. After which you can export the report result to the required format.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611102-Printing-Report-Result) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634121-Exporting-to-Mail)
