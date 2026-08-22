---
title: "Exporting Reports to HTML"
id: 5735553350295
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735553350295-Exporting-Reports-to-HTML
updated_at: 2022-11-02T07:57:52Z
---

# Exporting Reports to HTML

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525374615-Exporting-Reports-to-Logi-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735531895447-Exporting-Reports-to-PDF)

# Exporting Reports to HTML

This topic describes how you can export a page or web report to an HTML file.

1. Open the report that you want to export.
2. Navigate to **File** > **Export**  > **To HTML**. Designer displays the [Web Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500658839-Web-Wizard-Dialog-Box).

   ![Web Wizard - Report](https://devnet.logianalytics.com/hc/article_attachments/9898459923351/expt2html_rpt.gif)
3. In the **Report** tab, specify whether you want to export the report to a single HTML file or multiple HTML files. If you select to export the report to multiple files, Designer designates a serial number for each HTML file.
4. By default, Designer saves the HTML file in the same name as the report file. You can type another name for the HTML file in the **Web Page Name** text box.
   When the file name you specify does not contain the .html extension, Designer automatically adds the extension to the output file. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")If you want to use your preferred extension (or to have no extension) for the file name of the output, select **Use Custom File Extension**, then you can type your file name with any extension or no extension.
5. When you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can select a report tab and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to change the order of the report tabs.
6. From the **Web Browser** drop-down list, select the web browser the HTML output adapts.
7. Specify whether the text overflow is **visible** or **hidden**. If you select hidden, Designer cuts the overflowed text in the HTML output.
8. Select **No Margin** to remove the margins in the HTML output, which are set at report design time.
9. If you are exporting a page report that uses query resources, when the report contains grouped banded objects and you have added summaries (including group level formulas) to the groups, you can select **Drilldown** to generate the drilldown files for the summary of each group, so that when you view the HTML output, you can drill down on a summary to get the details about the corresponding group the same as you do when [previewing the report in Logi Report format](https://devnet.logianalytics.com/hc/en-us/articles/5735555715607-Previewing-Reports#GoToDetail). However, you should make sure that you have not hidden or suppressed the summaries; otherwise, you are not able to get the drilldown files.
10. By default, Designer includes the [TOC tree](https://devnet.logianalytics.com/hc/en-us/articles/5735585983511-TOC-Properties) of the report in the HTML output. If you do not want to export this TOC tree, clear **TOC**.
11. Specify either of the following:
    * If you select to export the report to a single file, by default, there is a navigation bar on each page of the HTML output for you to navigate to the previous and next page of the report. The navigation bar also contains the page number information showing the current page number and total page number. If you want to remove the navigation links and page number, select **No Hyperlink** and **No Page Number**. When you specify to show the navigation links and page number, you can [localize them to your preferred language](https://devnet.logianalytics.com/hc/en-us/articles/5735525819287-Localizing-Page-Navigation-Links-in-HTML-Output).
    * If you select to export the report to multiple files, select **Embedded CSS** to embed the cascading style sheet (CSS) in the HTML output; otherwise, Designer generates the .css file individually.
12. Specify whether to generate the report using a relative font size or absolute font size. When relative font size is used, you can adjust the font size in the HTML output according to the font size settings in the web browser.
13. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the HTML output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
14. Select **Section 508 Compliant Output** if you want to generate [Section 508 compliant HTML output](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF) for the report. When you select Section 508 Compliant Output, Designer selects the **Use HTML Data Table** and **Relative Font Size** options and disables them automatically. The output is Section 508 compliant including HTML data table, accessible attributes, and relative font.
15. In the **Directory** tab, select **Browse** to specify the directory where you want to save the HTML file. You can also type the location in the **Directory** text box.

    ![Web Wizard - Directory](https://devnet.logianalytics.com/hc/article_attachments/9898459931543/expt2html_drctry.gif)
16. If the report contains charts, Designer converts the charts to images in the HTML output. You can specify the image format to convert the charts in the **Image Chart** tab.

    ![Web Wizard - Image Chart](https://devnet.logianalytics.com/hc/article_attachments/9898476962199/expt2html_cht.gif)

    * **Auto Select**  
      Select this option if you want Designer to set the image format to JPG or GIF automatically. If the image colors are less than 256 colors, Designer applies GIF; otherwise, it uses JPG.
    * **GIF**  
      Select this option if you want to convert the charts in GIF, which is a lossless compression technique and supports only 256 colors. GIF is better than JPG for images with only a few distinct colors, such as the line drawing objects, black and white images, and small text that is only a few pixels high.
    * **JPG (JPEG)**  
      Select this option if you want to convert the charts in JPG (JPEG), which is supported on the Web. JPG is a lossy compression technique that is designed to compress color and grayscale continuous-tone images. JPG images support 16 million colors and are best suited for photographs and complex graphics. The transparency property of the charts takes effect only in PNG format.
    * **PNG**  
      Select this option if you want to convert the charts in PNG, which provides a portable, legally unencumbered, well-compressed (effectively 100 percent lossless compression), and well-specified standard for lossless bitmapped image file. PNG supports indexed-color images of up to 256 colors and shows a more interchangeable, flexible, and robust function than GIF.
17. The **Note** tab includes important information about exporting to HTML. You should read the content before you export your report to HTML. Designer cannot export multimedia objects and drawing objects (except for straight lines and boxes) to HTML.

    ![Web Wizard - Note](https://devnet.logianalytics.com/hc/article_attachments/9898476973463/expt2html_note.gif)
18. Select **Finish** to generate the HTML file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525374615-Exporting-Reports-to-Logi-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735531895447-Exporting-Reports-to-PDF)
