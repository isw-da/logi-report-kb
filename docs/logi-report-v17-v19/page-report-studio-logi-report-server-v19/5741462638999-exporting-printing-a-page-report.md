---
title: "Exporting/Printing a Page Report"
id: 5741462638999
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741462638999-Exporting-Printing-a-Page-Report
updated_at: 2022-10-31T17:18:15Z
---

# Exporting/Printing a Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741462847767-Saving-a-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741439209879-Customizing-Page-Report-Studio-Profile)

# Exporting/Printing a Page Report

When you are satisfied with a report, you may want to export it to other formats or print it. This topic describes how you can export and print a page report.

This topic contains the following sections:

* [Exporting a Page Report](#Export)
* [Printing a Page Report](#Print)

## Exporting a Page Report

You can export a report as a result version or as a local file to other formats. However, if the report you are going to export is linked to another report, in the exported report the link will no longer be available.

1. Select **Menu** > **File** > **Export**, or the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/9905578054551/btn_expt.gif) on the toolbar to display the [Export](https://devnet.logianalytics.com/hc/en-us/articles/5741410455959-Export-Dialog-Box-Properties) dialog box.

   ![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/9905673783575/expt.gif)
2. In the File Name field, specify the name of the exported report file.
3. Specify the destination of the report:
   * **View Report Result**: Select to directly open the report in the web browser if the format is supported by a plug-in of the web browser; otherwise Server will prompt you to save the report file.
   * **Save to File System**: Select if you want the web browser to prompt you to save the report file to a specified folder. You need to provide a name for the report file in the File Name field.
   * **Save to Version System**: Select to save the report as a result version in Logi Report Server's [versioning system](https://devnet.logianalytics.com/hc/en-us/articles/5741462048023-Managing-Resource-Versions).
4. In the Select Report Tabs box, select the report tabs you want to export. Server will export the selected report tabs in the list order. You can change the order of the report tabs by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif).
5. From the Select Format drop-down list, select the format in which you want to export the report: HTML, PDF, Excel, Text, RTF, XML, PostScript, or Page Report Result.
6. To specify the additional setting of the selected format, select **More Options**.
7. From the Style Group drop-down list, select the style group you want to apply to the exported report output. If the page report is created in Logi Report Designer, when you specify the <No Style> item, the style group property predefined for specific export format in Logi Report Designer will apply to export the report to that format.
8. Set the other [properties for the selected format](https://devnet.logianalytics.com/hc/en-us/articles/5741410455959-Export-Dialog-Box-Properties#Property) as you want.
9. Select **OK** to confirm.

**Tip:** Before exporting a report, you can customize the page properties for each exported output. For more information, see [Setting up the report page](https://devnet.logianalytics.com/hc/en-us/articles/5741438977943-General-Operations-in-Page-Report#Page).

## Printing a Page Report

You can print the current page report to a PDF or HTML file.

1. Select **Menu** > **File** > **Printable Version**, or the **Printable Version** button ![Printable Version button](https://devnet.logianalytics.com/hc/article_attachments/9905616008343/btn_print.gif) on the toolbar. Server displays the [Printable Version](https://devnet.logianalytics.com/hc/en-us/articles/5741389268887-Printable-Version-Dialog-Box-Properties) dialog box.

   ![Printable Version dialog](https://devnet.logianalytics.com/hc/article_attachments/9905661887895/print.gif)
2. Specify whether to print the current report tab or multiple report tabs in the current report.
3. Select the format in which you want to print the report: PDF or HTML.
4. When you only want to print the current report tab, specify the range of the pages in the report tab that you want to print.
   * **All**  
      If the option is selected, all pages in the current report tab will be printed.
   * **Current Page**  
      If the option is selected, only the current page of the report tab will be printed.
   * **Pages**  
      If the option is selected, you can define the pages in the current report tab that you want to print. Separate the page numbers and/or page ranges by commas.

   When you want to print multiple report tabs in the current report, select the report tabs you want and adjust the printing order of the report tabs by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif).
5. Select **Apply**. Server opens the PDF or HTML output file in an associated program with which you can print it to a printer.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741462847767-Saving-a-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741439209879-Customizing-Page-Report-Studio-Profile)
