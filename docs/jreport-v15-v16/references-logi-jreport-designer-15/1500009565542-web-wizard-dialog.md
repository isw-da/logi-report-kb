---
title: "Web Wizard Dialog"
id: 1500009565542
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565542-Web-Wizard-Dialog
updated_at: 2021-07-24T05:55:20Z
---

# Web Wizard Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589201-Web-Report-Option-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567942-Windows-Media-Player-Parameter-Dialog)

# Web Wizard Dialog

The Web Wizard appears when you select File > Export > To HTML. It helps you to [export a report to HTML format](https://devnet.logianalytics.com/hc/en-us/articles/1500009568082-Exporting-to-HTML), and consists of the following tabs:

* [Report](#Report)
* [Directory](#Directory)
* [Chart Applet](#Chart)
* [Note](#Note)

**Previous**

Retains changes and returns to the previous tab.

**Next**

Retains changes and goes to the next tab.

**Finish**

Completes the exporting.

**Cancel**

Does not retain any changes and closes the wizard.

**Help**

Displays the help document about this feature.

## Report

Specifies the options applied to the report. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893919511/webwzrd_rpt.gif)

**Export to**

Specifies whether to export the report result to a single HTML file or multiple HTML files.

* **Single File**  
   If checked, the report result will be generated in a single HTML file.
* **Multiple Files**  
   If checked, the report result will be generated into multiple HTML files, and Logi JReport will designate a serial number for each HTML page. For example, if you named a 3-page report as "sales", Logi JReport will create three files called sales\_1.html, sales\_2.html, and sales\_3.html.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893919511/webwzrd_rpt.gif)

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. If the report has only one report tab, it is selected by default.

**Web Page Name**

Specifies the name of the exported file. When exporting a page report, you need to specify the name for each report tab.

If you do not type the name, Logi JReport will use the report name as the default HTML file name. Logi JReport automatically attaches the extension \*.html, so you do not have to type the extension yourself.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893839511/btn_mvup3.gif)

Moves the specified report tab one step up.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893839767/btn_mvdwn3.gif)

Moves the specified report tab one step down.

**Web Browser**

Specifies the web browser for which the HTML result adapts.

**Text Overflow**

Specifies whether the text overflow is visible or hidden.

**No Margin**

Specifies whether to remove the margins originally set when the report was designed.

**Drilldown**

Specifies whether to include the drilldown file in the exported HTML file.

**TOC**

Specifies whether to enable the TOC (Table of Contents) in the exported HTML file.

**No Hyperlink**

If checked, there will be no hyperlinks for navigating previous and next pages on the navigation bar of the exported HTML file. Enabled only when Single File is selected.

**No Page Number**

If checked, there will be no page number information showing the current page number and total page number on the navigation bar of the exported HTML file. Enabled only when Single File is selected.

**Embedded CSS**

Specifies whether to embed the cascading style sheet (CSS) in the exported HTML files; otherwise, the .css file will be generated individually. Enabled only when Multiple Files is selected.

**Section 508 Compliant Output**

If checked, the accessibility attributes defined for the report elements via the Report Inspector will be exported to the HTML result which is Section 508 compliant. See [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/1500009562542-Accessibility) for more information.

When Section 508 Compliant Output is checked, the Use HTML Data Table and Relative Font Size options will be checked and disabled. The output will be Section 508 compliant including HTML data table, accessible attributes, and relative font feature.

**Use HTML Data Table**

Specifies whether the table and crosstab components will be output as table objects in the HTML result.

**Absolute Font Size**

Specifies whether to generate the report result using an absolute font size, which means the font size is fixed and cannot be adjusted according to the font size settings in the web browser.

**Relative Font Size**

Specifies whether to generate the report result using a relative font size, which means the font size can be adjusted according to the font size settings in the web browser.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the exported HTML file. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

## Directory

Specifies the location in which to place the exported HTML files. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889363223/webwzrd_drctry.gif)

**Directory**

Specifies the destination directory where you want to place the exported HTML file.

## Chart Applet

If you have used dynamic charts in your report, they can still be available in the exported HTML file. If Embed chart applet has been checked, dynamic 3-D charts will remain interactive and be available in the outputted HTML file. If Save in image has been checked, the charts will be converted to images. Also, you can specify the format of the images by choosing from the drop-down list (GIF or JPEG. The default format is JPEG). [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893919767/webwzrd_cht.gif)

**Applet Chart**

Uses a Java applet to display the charts in an HTML result file.

If checked, for Google Chrome, the report in the file can be viewed only when NPAPI is enabled for the web browser.

**Image Chart**

If checked, charts will be converted to images and you can specify the image type from the drop-down list. However, the transparency property of the charts takes effect only when PNG is selected as the image type.

* **Auto Select**  
   If selected, the image format will be set to JPG or GIF by the Logi JReport system automatically. If the image colors are less than 256 colors, GIF will be applied; otherwise, it is JPG.
* **GIF**  
   If selected, the GIF format will be applied, which is a lossless compression technique and supports only 256 colors. GIF is better than JPG for images with only a few distinct colors, such as line drawings, black and white images and small text that is only a few pixels high.
* **JPG (JPEG)**  
   If selected, the JPG (JPEG) format will be applied, which is supported on the Web. JPG is a lossy compression technique that is designed to compress color and grayscale continuous-tone images. JPG images support 16 million colors and are best suited for photographs and complex graphics.
* **PNG**  
   If selected, the PNG format will be applied, which provides a portable, legally unencumbered, well-compressed (effectively 100 percent lossless compression), well-specified standard for lossless bitmapped image file. PNG supports indexed-color images of up to 256 colors and shows a more interchangeable, flexible and robust function than GIF.

## Note

This tab includes important information about HTML. We recommend that you read the contents in the Note tab before you convert your report to HTML format. [See the tab](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404893920023/webwzrd_note.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589201-Web-Report-Option-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567942-Windows-Media-Player-Parameter-Dialog)
