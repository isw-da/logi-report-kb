---
title: "HTML Option Dialog"
id: 1500009631941
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631941-HTML-Option-Dialog
updated_at: 2021-07-24T16:04:29Z
---

# HTML Option Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631901-Horizontal-Banded-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608782-Image-Button-Dialog)

# HTML Option Dialog

The HTML Option dialog helps you to specify the parameters for running a report in HTML format. It appears when you set the Default Format for Viewing Report property of a report tab or a web report to HTML and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the value cell in the Report Inspector.

![HTML Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916786583/htmloptn.gif)

The following are details about options in the dialog:

**No Margin**

Removes the margins you originally set while designing the report.

**Multiple Files**

Generates the report result to multiple HTML files. Logi Report designates a serial number for each HTML page. For example, if you named a 3-page report as "sales", Logi Report will create three files called sales\_1.html, sales\_2.html, and sales\_3.html.

* **Embedded CSS**  
   Specifies to embed the cascading style sheet (CSS) in the HTML files; otherwise, the .css file will be generated individually.

**Single File**

Generates the report result to a single HTML file.

* **No Hyperlink**  
   If the option is selected, there will be no hyperlinks for navigating previous and Next Topics on the navigation bar of the HTML file.
* **No Page Number**  
   If the option is selected, there will be no page number information showing the current page number and total page number on the navigation bar of the HTML file.

**Drilldown**

Generates the report result into an HTML file with the Drilldown feature enabled. The Drilldown feature enables you to inspect certain items for further detailed data.

**Section 508 Compliant Output**

If the option is selected, the accessibility attributes defined for the report elements via the Report Inspector will be exported to the HTML result which is Section 508 compliant. See [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/1500009628201-Accessibility) for more information.

When Section 508 Compliant Output is selected, the Use HTML Data Table and Relative Font Size options will be selected and disabled. The output will be Section 508 compliant including HTML data table, accessible attributes, and relative font feature.

**Use HTML Data Table**

Specifies whether the table and crosstab components will be output as table objects in the HTML result.

**Absolute Font Size**

Generates the report result using an absolute font size, which means that the font size is fixed, and cannot be adjusted according to the font size settings in the web browser.

**Relative Font Size**

Generates the report result using a relative font size. The font size can be adjusted according to the font size settings in the web browser.

**Image Chart**  
 If selected, charts will be displayed as images. You can specify the image type from the drop-down list. The options are:

* **Auto-select**  
   If selected, the image format will be detected to JPG or GIF by the Logi Report system automatically. If the image colors are less than 256 colors, GIF will be applied; otherwise, it is JPG.
* **GIF**  
   If selected, the GIF format will be applied, which is a lossless compression technique and supports only 256 colors. GIF is better than JPG for images with only a few distinct colors, such as line drawings, black and white images and small text that is only a few pixels high.
* **JPEG**  
   If selected, the JPEG format will be applied, which is supported on the Web. JPEG is a lossy compression technique that is designed to compress color and grayscale continuous-tone images. JPEG images support 16 million colors and are best suited for photographs and complex graphics.
* **PNG**  
   If selected, the PNG format will be applied, which provides a portable, legally unencumbered, well-compressed (effectively 100 percent lossless compression), well-specified standard for lossless bitmapped image file. PNG supports indexed-color images of up to 256 colors and shows a more interchangeable, flexible and robust function than GIF.

**Resolution**

Specifies the resolution of the HTML result to zoom in/out, in DPI. The default value is obtained from the operation system, which is the resolution of your monitor, for example, 72 DPI on Unix or 96 on Windows. You can set higher/lower value to zoom in/out.

**Web Browser**

Specifies the web browser for which the HTML result adapts.

**Text Overflow**

Specifies whether the text overflow is visible or hidden.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the HTML result. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631901-Horizontal-Banded-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009608782-Image-Button-Dialog)
