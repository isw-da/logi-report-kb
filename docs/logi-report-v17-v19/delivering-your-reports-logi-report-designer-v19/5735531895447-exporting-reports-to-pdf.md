---
title: "Exporting Reports to PDF"
id: 5735531895447
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735531895447-Exporting-Reports-to-PDF
updated_at: 2022-11-02T07:57:53Z
---

# Exporting Reports to PDF

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel)

# Exporting Reports to PDF

This topic describes how you can export a page or web report as PDF.

1. Open the report that you want to export.
2. Navigate to **File** > **Export** > **To PDF**. Designer displays the [Export to PDF dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513955223-Export-to-PDF-Dialog-Box).

   ![Export to PDF dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898476898711/expt2pdf.gif)
3. By default, Designer saves the PDF in the same folder and same name as the report file. You can type the destination directory and file name for the output in the **Directory** and **File Name** text boxes, or select **Browse** to specify the location and file name with File Explorer of your operating system. When the file name you specify does not contain the .pdf extension, Designer automatically adds the extension to the output file. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")If you want to use your preferred extension (or to have no extension) for the file name of the output, select **Use Custom File Extension**, then you can type your file name with any extension or no extension.
4. When you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can select a report tab and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to change the order of the report tabs.
5. Select **No Margin** to remove the margins in the PDF output, which you set at report design time.
6. Select **TOC** to include the [TOC tree](https://devnet.logianalytics.com/hc/en-us/articles/5735585983511-TOC-Properties) of the report in the PDF output.
7. If you are exporting a page report that uses query resources, when the report contains grouped banded objects and you have added summaries (including group level formulas) to the groups, you can select **Drilldown** to generate the drilldown files for the fields of each group, so that when you view the PDF output, you can drill down on a summary to get the details about the corresponding group the same as you do when [previewing the report in Logi Report format](https://devnet.logianalytics.com/hc/en-us/articles/5735555715607-Previewing-Reports#GoToDetail). However, you should make sure that you have not hidden or suppressed the summaries; otherwise, you are not able to get the drilldown files.
8. Select **Accessible PDF** if you want to generate an [accessible PDF](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF) for the report.
9. By default, Designer compresses images in the report by 20% of the original size in the PDF output. You can customize the proportion or clear **Compress Image** to keep the original size.
10. Specify in which way to generate charts, web controls, UDOs, and barcodes in the report.
    The recommended way is using images to generate them.
    * **Generate charts and barcodes using images**  
      Select this option if you want Designer to export charts, barcodes, web controls, and UDOs in the report to common images, which look dimmed and the file size may be relatively large. However, when you select both Compress Image and this option, the transparency property of these objects cannot take effect.
    * **Generate charts and barcodes using vector graphics**  
      Select this option if you want Designer to export charts, barcodes, web controls, and UDOs in the report to vector graphics, which is anamorphic when it is zoomed out or zoomed in.
11. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the PDF output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
12. By default, Designer clips the content that is beyond its parent container in the PDF output. If you want to fully display the content, clear **Clipping Area**.
13. In the **Zoom** combo box, specify the zooming of the report content in the PDF output. You can select an item from the drop-down list or type a percentage in the text box. A valid percentage is greater than 0 and no larger than 6400% (you can type the value with or without the percent symbol). Designer treats any invalid input as "Default" (no zoom setting).
14. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")In the **Title** and **Subject** text boxes, type the text you want to use for the Title and Subject properties of the PDF.
15. If you want to encrypt the PDF to prevent users from opening, printing, and editing it without authorization, select **Encrypt**, then in the [Encrypt dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522749847-Encrypt-Dialog-Box):

    ![Encrypt dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898459891863/encrypt.gif)

    1. From the **Compatibility** drop-down list, select the encryption type. "Acrobat 3.0 and Later" means using a low encryption level (40-bit RC4), while "Acrobat 5.0 and Later" uses a high encryption level (128-bit RC4).
    2. In the **Options** box, select **Require a password to open the document** if you want the PDF is password protected, then specify the password in the **Document Open Password** text box and confirm it in the **Confirm Password** text box.
    3. If you want to use a permission password to restrict users from printing and editing the PDF, select **Use a password to restrict printing and editing of the document and its security settings**, then specify the password and confirm it accordingly. The permission password should be different from the one used for opening the PDF.
    4. By default, Designer selects **None** in the **Printing Allowed** drop-down list, which means the PDF cannot be printed. If you want users to print the file, select the required option from the list.
       * **Low Resolution**  
         Select to let users print the PDF at no higher than 150-dpi resolution. Printing may be slower because each page is printed as a bit-mapped image. Designer displays this option only when you select Acrobat 5.0 and Later in the Compatibility drop-down list.
       * **High Resolution**  
         Select to let users print the PDF at any resolution, directing high-quality vector output to PostScript and other printers that support advanced high-quality printing features.
    5. From the **Changes Allowed** drop-down list, select what editing actions you want to grant users on the PDF (by default, Designer selects **None** in the list, which means users cannot make any change to the PDF, including filling in signature and form fields).
       * **Inserting, deleting, and rotating pages**  
         Select to allow users to insert, delete and, rotate pages, and create bookmarks and thumbnail pages in the PDF. This option is available only when you select Acrobat 5.0 and Later in the Compatibility drop-down list.
       * **Filling in form fields and signing**  
         Select to allow users to fill in forms and add digital signatures in the PDF. This option doesn't allow users to add comments or create form fields.
       * **Commenting, filling in form fields and signing**  
         Select to allow users to fill in forms and add digital signatures and comments in the PDF.
       * **Any except extracting pages**  
         Select to allow users to change the PDF using any method listed in the Changes Allowed menu, except removing pages.
    6. Select **Enable copying of text, images and other content** to allow users to select and copy the content of the PDF.
    7. When you select Acrobat 5.0 and Later in the Compatibility drop-down list, Designer displays the **Enable text access for screen reader devices for the visually impaired** option and selects it by default. If you do not want to enable the use of screen readers for visually impaired users on the PDF, you can clear the option.
    8. Select **OK** to finish configuring the encryption settings for the PDF.
16. To configure the signature for the PDF, select **Sign**, then in the [Sign dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735552629655-Sign-Digital-ID-Dialog-Box):

    ![Sign Digital ID dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898476914967/signid.gif)

    1. From the **Method** drop-down list, select the signing digital signature method: Windows Certificate Security, Default Certificate Security, or VeriSign Digital Signatures. The methods are provided by the Adobe Acrobat software.
    2. Select **Browse** to select the digital ID file. You can also type the file path in the **Digital ID File** text box manually.
    3. Specify the password for the digital ID file and confirm the password respectively.
    4. From the **Reason for Signing Document** drop-down list, select the reason for signing the file. You can also specify the reason by yourself by typing it in the text box.
    5. Specify the location and your contact information if you want.
    6. Select **OK** to accept the changes.
17. Select **OK** to start exporting.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Before exporting a page report tab or a web report that uses [True Type Fonts](https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports), you should select the report tab name or the web report in the Report Inspector, and then set Embedded Fonts equal to all true type fonts that you have used in the report tab or web report. Otherwise, the PDF output may not display correctly.
* When you export a report to PDF, in which there is an object beyond its container, Designer ignores the overstepped part in the PDF output, but Designer can still export the overstepped part of objects in a paragraph to PDF.
* If you find that the page size of the PDF output in Adobe Acrobat is different from that printed under the same zooming, you can check the Resolution setting in Adobe, because different resolutions result in different page size on the screen.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516034199-Exporting-Reports-to-Excel)
