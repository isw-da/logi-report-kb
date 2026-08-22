---
title: "Exporting Report Result"
id: 1500010060902
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060902-Exporting-Report-Result
updated_at: 2021-07-23T19:16:10Z
---

# Exporting Report Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099421-Printing-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060922-Exporting-to-Mail)

# Exporting Report Result

This topic introduces how you can export page and web reports to different formats. It also describes the two useful configuration methods for customizing the page properties and layout precision of each export format.

You can export the result of a page or web report to the following file formats:

* [To Mail](https://devnet.logianalytics.com/hc/en-us/articles/1500010060922-Exporting-to-Mail)
* [To Logi Report Result](https://devnet.logianalytics.com/hc/en-us/articles/1500010060942-Exporting-to-Logi-Report-Result)
* [To HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500010099301--Exporting-to-HTML)
* [To PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500010099321-Exporting-to-PDF)
* [To Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500010099261-Exporting-to-Excel)
* [To Text](https://devnet.logianalytics.com/hc/en-us/articles/1500010099381-Exporting-to-Text)
* [To RTF](https://devnet.logianalytics.com/hc/en-us/articles/1500010099361-Exporting-to-RTF)
* [To XML](https://devnet.logianalytics.com/hc/en-us/articles/1500010099401-Exporting-to-XML)
* [To PostScript](https://devnet.logianalytics.com/hc/en-us/articles/1500010099341-Exporting-to-PostScript)
* [To Fax](https://devnet.logianalytics.com/hc/en-us/articles/1500010099281-Exporting-to-Fax)

## Customizing the Page Properties for Each Export Type

Before exporting a report, you can customize the page properties for each format type as follows:

1. Select **File** > **Page Setup**. Designer displays the [Page Setup dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060082-Page-Setup-Dialog-Box).
2. Switch to the **Export** tab.

   ![Page Setup dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4404848476439/pgstup_export.gif)
3. By default, Designer applies the [properties defined for the report page](https://devnet.logianalytics.com/hc/en-us/articles/1500010101321-Designing-the-Report-Pages#Setting) in the General tab of the dialog box to the outputs of all export formats. To define the page properties for each format, select a format from the **Export To** drop-down list, clear the **Auto** option and then define the properties as you want. Repeat this to define the properties for all formats.
4. Select **OK** to accept the settings.

When you clear the Auto option for an export format and select OK in the Page Setup dialog box, Designer adds a corresponding [export page setting object](https://devnet.logianalytics.com/hc/en-us/articles/1500010100681-Export-Page-Setting-Object-Properties) to the report structure tree in the Report Inspector. You can edit the export page properties there too. When you select the Auto option for this export format and select OK in the dialog box again, Designer removes its export page setting object automatically from the report structure tree.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Server also applies the page properties you specify for any export format when you advanced run and schedule to run the report in this format at runtime.

## Customizing the Layout Precision

You can customize the layout precision you want to apply when exporting reports in Designer. However for page reports, the customized precision can take effect only in report tabs whose [Precision Sensitive](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#PrecisionSensitive) property is true.

1. Select **File** > **Options**.
2. In the Options dialog box, select **Export to** in the **Category** box.
3. Select the **Layout Precision**. Designer displays the Advanced Export Settings dialog box.

   ![Advanced Export Settings dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856878999/advexptsting.gif)
4. Select **Customize for each format**.

   By default, Designer selects **Optimize for speed over visual effect**, which means Designer decides the precision level which is oriented towards speed more than visualization.
5. Select the **System Default Settings** button, then in the **Precision Settings** dialog box, edit the precision level for each format and select **OK**.

   ![Precision Settings dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848476951/prcsnsting.gif)

   Designer provides two precision levels: **High** and **Low**. High precision provides better layout but slower efficiency, while low precision brings higher performance but maybe poorer visual effect. If low precision can give reports well looks, it is reasonable to apply low precision because faster performance is guaranteed at the same time. By default, when exporting a report to formats such as PDF, RTF, Excel, Fax, or PostScript, Designer exports the text with high precision, thus the report result layouts of these formats are different from the other formats such as HTML, Logi Report Result, XML, and Text.
6. In the **Advanced Export Settings** dialog box, select the checkbox for the required formats to apply the defined precision level and select **OK**. For formats that you do not select, Designer decides their precision.
7. Select **OK** in the Options dialog box to apply the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can export the report result in either design or view mode. However, if you modify the report after opening it, it is recommended to use view mode to export the report result. To do this, select the **View** tab, and then select the **Refresh Data** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404848383767/btn_refresh.gif) on the toolbar. Designer then re-fetches data in the report from the database. After that, you can export the report result to the required format.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099421-Printing-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060922-Exporting-to-Mail)
