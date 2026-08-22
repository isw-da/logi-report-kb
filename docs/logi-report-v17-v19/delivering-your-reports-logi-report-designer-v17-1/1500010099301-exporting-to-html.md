---
title: " Exporting to HTML"
id: 1500010099301
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099301--Exporting-to-HTML
updated_at: 2021-07-23T19:16:10Z
---

#  Exporting to HTML

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060942-Exporting-to-Logi-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099321-Exporting-to-PDF)

# Exporting to HTML

This topic describes how you can export the result of a page or web report to an HTML file.

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To HTML**. Designer displays the [Web Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096681-Web-Wizard-Dialog-Box).

   ![Web Wizard - Report](https://devnet.logianalytics.com/hc/article_attachments/4404856877591/webwzrd_rpt.gif)
3. In the **Report** tab, specify whether to export the report result to a single HTML file or multiple HTML files.
4. By default, Designer applies the name of the report as the name of the HTML file. You can specify another name for the HTML file in the **Web Page Name** text box if you want.

   If you select to export the report result to multiple files, Designer designates a serial number for each HTML file. For example, if you name a 3-page report as "sales", Designer creates three files called sales\_1.html, sales\_2.html, and sales\_3.html.
5. If you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can make use of the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to change the order of the report tabs.
6. From the **Web Browser** drop-down list, select the web browser the HTML output adapts.
7. Specify whether the text overflow is **visible** or **hidden**. If you select hidden, Designer cuts the overflowed text in the HTML output.
8. Select the **No Margin** checkbox to remove the margins in the HTML output, which are set at report design time.
9. If you are exporting a page report that uses query resources, when the report contains grouped banded objects and you have added summaries to the groups, you can select **Drilldown** to generate the drilldown files for the summary of each group, so that when you view the HTML output, you can drill down on a summary to get the details about the corresponding group the same as you do when [previewing the report in Logi Report format](https://devnet.logianalytics.com/hc/en-us/articles/1500010101341-Previewing-Reports#ShowDetail). However, you should make sure that you have not hidden or suppressed the summaries; otherwise, you are not able to get the drilldown files.
10. By default, Designer includes the Table of Contents in the HTML output, using which you can easily locate the report objects in the HTML file (to make a report object shown in the TOC, you need to make sure its [TOC Anchor](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#TOC) property is true). If you do not want the TOC in the HTML output, clear **TOC**.
11. If you select to export the report result to a single file, by default, there is a navigation bar on each page of the HTML output for you to navigate to the previous and next page of the report result. The navigation bar also contains the page number information showing the current page number and total page number. If you want to remove the navigation links and page number, select **No Hyperlink** and **No Page Number**. When you specify to show the navigation links and page number, you can [localize them to your preferred language](https://devnet.logianalytics.com/hc/en-us/articles/1500010061202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs).

    If you select to export the report result to multiple files, select **Embedded CSS** to embed the cascading style sheet (CSS) in the HTML output; otherwise, Designer generates the .css file individually.
12. Specify whether to generate the report result using a relative font size or absolute font size. When relative font size is used, you can adjust the font size in the HTML output according to the font size settings in the web browser.
13. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the HTML output. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
14. Select **Section 508 Compliant Output** if you want to generate Section 508 compliant HTML output for the report. For more information, see [Exporting Reports to Accessible HTML and PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500010099241-Exporting-Reports-to-Accessible-HTML-and-PDF).

    When you select Section 508 Compliant Output, Designer selects the **Use HTML Data Table** and **Relative Font Size** options and disables them automatically. The output is Section 508 compliant including HTML data table, accessible attributes, and relative font.
15. In the **Directory** tab, select **Browse** to specify the directory where to save the HTML file. You can also type the location in the **Directory** text box manually.

    ![Web Wizard - Directory](https://devnet.logianalytics.com/hc/article_attachments/4404856878103/webwzrd_drctry.gif)
16. If the report contains charts, Designer converts the charts to images in the HTML output. You can specify in which image format to convert the charts in the **Image Chart** tab.

    ![Web Wizard - Image Chart](https://devnet.logianalytics.com/hc/article_attachments/4404848475031/webwzrd_cht.gif)

    * **Auto Select**  
      Select it if you want Designer to set the image format to JPG or GIF automatically. If the image colors are less than 256 colors, Designer applies GIF; otherwise, it uses JPG.
    * **GIF**  
      Select it if you want to convert the charts in GIF, which is a lossless compression technique and supports only 256 colors. GIF is better than JPG for images with only a few distinct colors, such as the line drawing objects, black and white images, and small text that is only a few pixels high.
    * **JPG (JPEG)**  
      Select it if you want to convert the charts in JPG (JPEG), which is supported on the Web. JPG is a lossy compression technique that is designed to compress color and grayscale continuous-tone images. JPG images support 16 million colors and are best suited for photographs and complex graphics. The transparency property of the charts takes effect only in PNG format.
    * **PNG**  
      Select it if you want to convert the charts in PNG, which provides a portable, legally unencumbered, well-compressed (effectively 100 percent lossless compression), and well-specified standard for lossless bitmapped image file. PNG supports indexed-color images of up to 256 colors and shows a more interchangeable, flexible, and robust function than GIF.
17. The **Note** tab includes important information about exporting to HTML. You are recommended to read the contents before you export your report to HTML. Note that Designer cannot export multimedia objects and drawing objects (except for straight lines and boxes) to HTML.

    ![Web Wizard - Note](https://devnet.logianalytics.com/hc/article_attachments/4404848475287/webwzrd_note.gif)
18. Select **Finish** to generate the HTML file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060942-Exporting-to-Logi-Report-Result)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099321-Exporting-to-PDF)
