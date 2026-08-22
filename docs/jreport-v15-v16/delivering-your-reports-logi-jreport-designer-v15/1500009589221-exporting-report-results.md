---
title: "Exporting Report Results"
id: 1500009589221
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589221-Exporting-Report-Results
updated_at: 2021-07-24T05:54:42Z
---

# Exporting Report Results

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589461-Printing-Report-Results)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568102-Exporting-to-Mail)

# Exporting Report Results

You can export report results to the following file formats:

* [To Mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009568102-Exporting-to-Mail)
* [To Logi JReport Result](https://devnet.logianalytics.com/hc/en-us/articles/1500009568122-Exporting-to-Logi-JReport-Result)
* [To HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009568082-Exporting-to-HTML)
* [To PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500009589381-Exporting-to-PDF)
* [To Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009568022-Exporting-to-Excel)
* [To Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009568142-Exporting-to-Text)
* [To RTF](https://devnet.logianalytics.com/hc/en-us/articles/1500009589421-Exporting-to-RTF)
* [To XML](https://devnet.logianalytics.com/hc/en-us/articles/1500009589441-Exporting-to-XML)
* [To PostScript](https://devnet.logianalytics.com/hc/en-us/articles/1500009589401-Exporting-to-PostScript)
* [To Fax](https://devnet.logianalytics.com/hc/en-us/articles/1500009568062-Exporting-to-Fax)
* [To Applet](https://devnet.logianalytics.com/hc/en-us/articles/1500009589241-Exporting-to-Applet)

**Customizing the page properties for each result type**

Before exporting a report, you can customize the page properties for each result type as follows:

1. Select **File** > **Page Setup**. The [Page Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009588121-Page-Setup-Dialog) dialog appears.
2. Switch to the **Export** tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893843735/pgstup_export.gif)
3. By default, the [properties defined for the report page](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page#Setting) in the General tab of the dialog will be applied to the exported result of all export formats. To define the page properties for each exported result, select a format from the Export To drop-down list, uncheck the **Auto** option and then define the properties as you want. Repeat this to define the properties for all formats.
4. Select **OK** to accept the settings. The page properties specified for any export format will also be applied when advanced running and scheduling to run the report in this format on Logi JReport Server.

When you uncheck the Auto option for an export format and select OK in the Page Setup dialog, a corresponding [export page setting object](https://devnet.logianalytics.com/hc/en-us/articles/1500009569762-Properties-of-Export-Page-Setting-Object-in-Page-Report) will be added to the report structure tree in the Report Inspector. You can edit the export page properties there too. When you check the Auto option for this export format and select OK in the dialog again, its export page setting object will be removed automatically from the report structure tree.

**Customizing the layout precision**

You can customize the layout precision that will be applied when exporting reports in Logi JReport Designer. However for page reports, the customized precision can take effect only in report tabs whose [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#PrecisionSensitive) property is set to true.

1. Select **File** > **Options**.
2. In the Options dialog, select **Export to** in the Category box.
3. Select the **Layout Precision** button to open the Advanced Export Settings dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893843991/advexptsting.gif)
4. Select **Customize for each format**.

   By default, Optimize for speed over visual effect is selected, which means Logi JReport will decide the precision level which is oriented towards speed more than visualization.
5. Select the **System Default Settings** button, then in the Precision Settings dialog, edit the precision level for each format and select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889310871/prcsnsting.gif)

   Logi JReport provides two precision levels: high and low. High precision provides better layout but slower efficiency while low precision brings higher performance but maybe poorer visual effect. If low precision can give reports well looks, it is reasonable to apply low precision for at the same time faster performance is guaranteed. By default when exporting a report to formats such as PDF, RTF, Excel, Fax or PostScript, the text will be exported with high precision. Thus the report result layouts of these formats are different from the other formats such as HTML, Logi JReport Result, Applet, XML, and Text.
6. In the Advanced Export Settings dialog, check the checkbox for the required formats to apply the defined precision level and select **OK**. For formats that are not checked, Logi JReport will decide their precision.
7. Select **OK** in the Options dialog to apply the settings.

**Note:** You can export the report data in either design or view mode. However, if you modify the report after opening it, it is recommended to use view mode to export the report data. To do this, select the **View** tab, and then select the **Refresh Data** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893802519/btn_refresh.gif) on the toolbar. The data will then be re-fetched from the database. After which you can export the report data to the required format.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589461-Printing-Report-Results)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568102-Exporting-to-Mail)
