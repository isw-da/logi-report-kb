---
title: "Exporting/Printing Page Report Result"
id: 1500009777541
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777541-Exporting-Printing-Page-Report-Result
updated_at: 2021-07-24T00:47:53Z
---

# Exporting/Printing Page Report Result

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777601-Saving-a-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777681-Customizing-Page-Report-Studio-Profile)

# Exporting/Printing Page Report Result

When you are satisfied with the result of a report, you may want to export it to other formats or print it. This topic describes how you can export and print page report results.

This topic contains the following sections:

* [Exporting Page Report Result](#Export)
* [Printing Page Report Result](#Print)

## Exporting Page Report Result

You can export a report as a result version or as a local file to other formats. However, if the report you are going to export is linked to another report, in the exported result the link will no longer be available.

1. Select **Menu** > **File** > **Export**, or the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404880137111/btn_expt.gif) on the toolbar to display the [Export](https://devnet.logianalytics.com/hc/en-us/articles/1500009772181-Export-Dialog-Box-Properties) dialog box.

   ![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885396631/expt.gif)
2. In the File Name field, specify the name of the exported result file.
3. Specify the destination of the result:
   * **View Report Result**: The result will be directly opened in the web browser if the format is supported by a plug-in of the web browser; otherwise it will prompt you to save the result file.
   * **Save to File System**: The web browser will prompt you to save the result file to a specified folder. If selected, you need to provide a name for the result file in the File Name field.
   * **Save to Version System**: The result will be saved as a result version in Logi Report Server's [versioning system](https://devnet.logianalytics.com/hc/en-us/articles/1500009777341-Managing-Resource-Versions).
4. In the Select Report Tabs box, select the report tabs you want to export. The selected report tabs will be exported in the list order. You can change the order of the report tabs by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
5. From the Select Format drop-down list, select the format in which to export the result: HTML, PDF, Excel, Text, RTF, XML, PostScript, or Page Report Result.
6. To specify the additional setting of the selected format, select **More Options**.
7. From the Style Group drop-down list, select the style group you want to apply to the exported report result. If the page report is created in Logi Report Designer, when the <No Style> item is specified, the style group property predefined for specific export format in Logi Report Designer will be applied to export the report result to that format.
8. Set the other [properties for the selected format](https://devnet.logianalytics.com/hc/en-us/articles/1500009772181-Export-Dialog-Box-Properties#Property) as required.
9. Select **OK** to confirm.

**Tip:** Before exporting a report, you can customize the page properties for each exported result according to your requirement. For more information, see [Setting up the report page](https://devnet.logianalytics.com/hc/en-us/articles/1500009749002-General-Operations-in-Page-Report#Page).

## Printing Page Report Result

You can print the report result of the current page report to a PDF or HTML file.

1. Select **Menu** > **File** > **Printable Version**, or the **Printable Version** button ![Printable Version button](https://devnet.logianalytics.com/hc/article_attachments/4404880137367/btn_print.gif) on the toolbar. Server displays the [Printable Version](https://devnet.logianalytics.com/hc/en-us/articles/1500009772881-Printable-Version-Dialog-Box-Properties) dialog box.

   ![Printable Version dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880265751/print.gif)
2. Specify whether to print the current report tab or multiple report tabs in the current report.
3. Select the format in which the report result will be printed: PDF or HTML.
4. When only the current report tab is to be printed, specify the range of the pages in the report tab that you want to print.
   * **All**  
      If the option is selected, all pages in the current report tab will be printed.
   * **Current Page**  
      If the option is selected, only the current page of the report tab will be printed.
   * **Pages**  
      If the option is selected, you can define the pages in the current report tab that you want to print. Separate the page numbers and/or page ranges by commas.

   When multiple report tabs in the current report are to be printed, select the desired report tabs and adjust the printing order of the report tabs by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
5. Select **Apply** and the PDF or HTML result file is then opened in an associated program with which you can print the result to a printer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777601-Saving-a-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777681-Customizing-Page-Report-Studio-Profile)
