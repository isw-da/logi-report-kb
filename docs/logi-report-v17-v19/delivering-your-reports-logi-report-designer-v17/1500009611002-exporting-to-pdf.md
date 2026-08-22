---
title: "Exporting to PDF"
id: 1500009611002
section: "Delivering Your Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009611002-Exporting-to-PDF
updated_at: 2022-08-24T00:13:57Z
---

# Exporting to PDF

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610982--Exporting-to-HTML) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634081-Exporting-to-Excel)

# Exporting to PDF

This topic introduces how to export the results of a report to a PDF file.

1. Open the report that you want to export.
2. Select **File** > **Export** > ****To** PDF**. The [Export to PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500009631101-Export-to-PDF-Dialog) dialog appears.

   ![Export to PDF dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904225815/expt2pdf.gif)
3. Select the **Browse** button to specify the destination directory where the exported PDF file will be placed and the name of the file. You can also type the location and file name manually in the Directory and File Name text boxes (make sure that the folder you specify does exist, otherwise an error message will be produced).
4. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404911669015/btn_mvup3.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904224919/btn_mvdwn3.gif) to change the order of the report tabs.
5. Select the **No Margin** checkbox to remove the margins in the exported PDF result, which are set at report design time.
6. Select **TOC** to enable the Table of Contents in the exported PDF file. Using the TOC, you can easily locate the report objects in the PDF file; however to make a report object shown in the TOC, you need to make sure its [TOC Anchor](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#TOC) property is true.
7. If you are exporting a page report created using query resources, when the report contains grouped banded objects and summaries are added to the groups, you can select **Drilldown** to generate the drilldown files for the summary of each group, so that when you view the exported PDF file, you can drill down on a summary to get the details about the corresponding group the same as you do when [previewing the report in Logi Report format](https://devnet.logianalytics.com/hc/en-us/articles/1500009613422-Previewing-Reports#ShowDetail). However you should make sure that the summaries are not hidden or suppressed; otherwise you will not be able to get drilldown files.
8. Select **Accessible PDF** 
   if you want to generate an accessible PDF file for the report. See [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/1500009628201-Accessibility) for more information.
9. By default images in the report will be compressed by 20% of the original size in the PDF result. You can customize the proportion or clear **Compress Image** to keep the original size.
10. Specify in which way to generate charts, web controls, UDOs and barcodes in the report.
    The recommended way is using images to generate them.
    * **Generate charts and barcodes using images**If selected, charts and barcodes as well as web controls and UDOs in the report will be exported to common pictures, which will look dimmed and the file size may be relatively large. However, when Compress Image and this option are both selected, the transparency property of these objects will not take effect.
    * **Generate charts and barcodes using vector graphics**If selected, charts and barcodes as well as web controls and UDOs in the report will be exported to vector graphics, which will not be anamorphic when it is zoomed out or zoomed in.
11. Select **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the PDF result. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
12. By default the content that is beyond its parent container will be clipped in the PDF result. If you want the content to be fully displayed, clear **Clipping Area**.
13. ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")In the Zoom combo box, specify the zooming of the report content in the exported PDF file. You can select an item from the drop-down list or type a percentage in the text box. A valid percentage is greater than 0 and no larger than 6400% (you can type the value with or without the percent sign). Any invalid input will be treated as Default (no zoom setting).
14. If you want to encrypt the PDF file to prevent users from opening, printing and editing the document without authorization, select the **Encrypt** checkbox, then in the [Encrypt](https://devnet.logianalytics.com/hc/en-us/articles/1500009631001-Encrypt-Dialog) dialog:

    ![Encrypt dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911669911/encrypt.gif)

    1. From the Compatibility drop-down list, select the encryption type to encrypt the PDF document. The option Acrobat 3.0 and later uses a low encryption level (40-bit RC4), while the other option Acrobat 5.0 and later uses a high encryption level (128-bit RC4).
    2. In the Options box, select **Require a password to open the document** if you want the exported PDF file is password protected, then specify the password in the Document Open Password text box and confirm it in the Confirm Password text box.
    3. If you want to use a permission password to restrict users from printing and editing the exported PDF, select **Use a password to restrict printing and editing of the document and its security settings**, then specify the password and confirm it accordingly. The permission password should be different from the one used for opening the document.
    4. By default None is selected in the Printing Allowed drop-down list, which means the exported PDF file cannot be printed. If you want users to print the file, select the required option from the list.
       * **Low Resolution**  
          Lets users print the document at no higher than 150-dpi resolution. Printing may be slower because each page is printed as a bitmapped image. This option is available only Acrobat 5.0 and Later is selected in the Compatibility drop-down list.
       * **High Resolution**  
          Lets users print at any resolution, directing high-quality vector output to PostScript and other printers that support advanced high-quality printing features.
    5. From the Changes Allowed drop-down list, select what editing actions you want to grant users for the exported PDF file (by default None  
       is selected in the list so users cannot make any change to the file, including filling in signature and form fields).
       * **Inserting, deleting, and rotating pages**  
          Lets users insert, delete and rotate pages, as well as create bookmarks and thumbnail pages. This option is available only Acrobat 5.0 and Later is selected in the Compatibility drop-down list.
       * **Filling in form fields and signing**  
          Lets users fill in forms and add digital signatures. This option doesn't allow users to add comments or create form fields.
       * **Commenting, filling in form fields** **and signing**  
          Lets users fill in forms and add digital signatures and comments.
       * **Any except extracting pages**  
          Lets users change the document using any method listed in the Changes Allowed menu, except removing pages.
    6. Select **Enable copying of text, images and other content** if you want to allow users to select and copy the contents of the exported PDF file.
    7. When Acrobat 5.0 and Later is selected in the Compatibility drop-down list, the Enable text access for screen reader devices for the visually impaired checkbox is available and selected by default. If you do not want to enable the use of screen readers for visually impaired users on the exported PDF file, you can clear the option.
    8. Select **OK** to finish configuring the encryption settings for the PDF file.
15. To configure the signature for the PDF file, select the **Sign** checkbox, then in the [Sign](https://devnet.logianalytics.com/hc/en-us/articles/1500009633401-Sign-Digital-ID-Dialog) dialog:

    ![Sign Digital ID dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911670167/signid.gif)

    1. From the Method drop-down list, select the signing digital signature method: Windows Certificate Security, Default Certificate Security or VeriSign Digital Signatures. The methods are provided by the Adobe Acrobat software.
    2. Select the **Browse** button to select the digital ID file. You can also type the file path in the Digital ID File text box manually.
    3. Specify the password for the digital ID file and confirm the password respectively.
    4. From the Reason for Signing Document drop-down list, select the reason for signing the document. You can also specify the reason by yourself.
    5. You can specify the location and your contact information.
    6. Select **OK** to accept the changes.
16. Select **OK** to start exporting.

**Notes:**

* Before exporting a page report tab or a web report that uses [True Type Fonts](https://devnet.logianalytics.com/hc/en-us/articles/1500009628261-True-Type-Fonts), you should select the report tab name or the web report in the Report Inspector, and then set Embedded Fonts equal to all true type fonts that you have used in the report tab or web report. Otherwise the PDF file may not be displayed correctly.
* When a report, in which there is an object beyond its container, is exported to PDF, the overstepped part will be ignored in the PDF file, but the overstepped part of objects in a paragraph can still be exported to PDF.
* If you find that the page size of the exported PDF file in Adobe Acrobat is different from that printed under the same zooming, you can check the Resolution setting in Adobe because different resolutions result in different page size on the screen.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610982--Exporting-to-HTML) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009634081-Exporting-to-Excel)
