---
title: "Exporting the Report Result"
id: 1500009649382
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649382-Exporting-the-Report-Result
updated_at: 2021-07-24T20:53:55Z
---

# Exporting the Report Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649462-Printing-the-Report-Result)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile)

# Exporting the Report Result

When you are satisfied with the result of the active report, you may want to export it as a result version or as a local file to other formats. However, if the report you are going to export is linked to another report, in the exported result the link will no longer be available.

1. Select **Menu** > **File** > **Export**, or the **Export** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920358295/btn_expt.gif) on the toolbar to display the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009669641-Export) dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920467735/expt.gif)
2. In the File Name field, specify the name of the exported result file.
3. Specify the destination of the result:
   * **View Report Result**: The result will be directly opened in the web browser if the format is supported by a plug-in of the web browser; otherwise it will prompt you to save the result file.
   * **Save to File System**: The web browser will prompt you to save the result file to a specified folder. If selected, you need to provide a name for the result file in the File Name field.
   * **Save to Version System**: The result will be saved as a result version in Logi JReport Server's [versioning system](https://devnet.logianalytics.com/hc/en-us/articles/1500009673701-Managing-Versions).
4. In the Select Report Tabs box, select the report tabs you want to export. The selected report tabs will be exported in the list order. You can change the order of the report tabs by selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).
5. From the Select Format drop-down list, select the format in which to export the result: HTML, PDF, Excel, Text, RTF, XML, PostScript, or Page Report Result.
6. To specify the additional setting of the selected format, select **More Options**.
7. From the Style Group drop-down list, select the style group you want to apply to the exported report result. If the page report is created in Logi JReport Designer, when the <No Style> item is specified, the style group property predefined for specific export format in Logi JReport Designer will be applied to export the report result to that format.
8. Set the other [properties for the selected format](https://devnet.logianalytics.com/hc/en-us/articles/1500009669641-Export#Property) as required.
9. Select **OK** to confirm.

**Tip:** Before exporting a report, you can customize the page properties for each exported result according to your requirement. For more information, refer to [Setting up the report page](https://devnet.logianalytics.com/hc/en-us/articles/1500009673961-General-Operations#Page).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649462-Printing-the-Report-Result)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674101-Customizing-Page-Report-Studio-Profile)
