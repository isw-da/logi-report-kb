---
title: "Applying True Type Fonts in Reports"
id: 5735534328983
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports
updated_at: 2022-11-02T08:23:04Z
---

# Applying True Type Fonts in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735547328663-Making-High-Efficiency-Reports)

# Applying True Type Fonts in Reports

You might find that well-designed reports in Designer become truncated when you run the reports on Server on a different platform. The reason is that various platforms use different font systems, and when JDK maps the fonts to a different platform, the reports appear with a discrepancy. To solve this problem, Logi Report adopts the True Type Font (TTF) administrative system of Java. You can design reports in any fonts in Designer. Then, when you publish the reports into the runtime environment, you can publish the fonts together with the reports, which are independent of the platform fonts. Logi Report also provides the PDF embedded fonts solution, meaning Logi Report can embed the fonts in the PDF output, so users do not need to install the fonts on their local machines. This topic describes how you can design reports with TTF, apply the Bold and Italic properties to TTF, deliver TTF to the runtime environment, and export reports with TTF in different formats.

The following sections describe how to use TTF in your reports:

* [Designing Reports with TTF](#Design)
* [Applying Bold and Italic Properties to TTF](#Apply)
* [Publishing TTF to the Runtime Environment](#Publish)
* [Delivering TTF in Excel/RTF/HTML/TXT](#DeliverExcel)
* [Delivering TTF in PDF](#DeliverPDF)

## Designing Reports with TTF

When you design reports that you want to run on a platform different from where you design them, it is best to use TTF fonts.

**To design reports with TTF**

1. Copy the True Type Font files **\*.ttf** to the `<designer_install_root>\font` directory of Designer. You can find the TTF fonts in your system's Font directory or from the Internet.
2. In Designer, open a report and select the text you want to apply the TTF font.
3. On the Home menu bar, select the drop-down arrow of the font list and scroll down to the bottom of the list. You can then find the fonts with an **\*** before their name. These are the TTF fonts you have copied. Select the TTF font you want to apply.
4. Preview the report and save the report until you are satisfied with the result.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9898419824023/criticalicon.gif)Logi Report uses the JDK TTF, however JDK has a problem in printing reports with rs\_song.ttf (some characters are incorrect). You should therefore use other Chinese TTF fonts such as SimSun.ttf, PMingLiu.ttf, and LF\_FangSong.ttf.

## Applying Bold and Italic Properties to TTF

Designer supports the Bold and Italic properties for TTF. When you select a TTF font and set the Bold/Italic property to "true", Designer first searches the `<designer_install_root>\font` directory automatically to check all the TTF files related with the TTF font you have selected previously. If there is such a TTF file holding the Bold/Italic property, Designer uses the font style defined in this file to match your setting and make the Bold/Italic property take effect; if not, Designer finds the specified font in your platform fonts and applys the Bold/Italic property directly.

## Publishing TTF to the Runtime Environment

When you [publish reports](https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources) from Designer to Server, if the reports use TTF fonts, Designer prompts you the Publish Additional Resources dialog box to publish the font files at the same time. After Designer finishes the publishing task, you can find the corresponding font files in the `<server_install_root>\font` directory of Server.

## Delivering TTF in Excel/HTML/TXT/RTF

For report outputs in Excel, HTML, TXT, and RTF, they can automatically find the TTF fonts from the system's Font directory to display the fonts correctly. However, to avoid any discrepancy in the report outputs, if you want to deliver the report in these formats, you should choose the TTF fonts that are common on the Windows systems. When you have to use fonts that do not exist in the client's system, you can choose the embedded TTF font solution as shown in the following section.

## Delivering TTF in PDF

To view PDF outputs with other character sets, for example, Chinese fonts, you need to install special language packages. Also, if you design reports with fonts that are not within Acrobat's internal fonts, Acrobat maps them differently. The two cases cause trouble to users when they view or print a report with Acrobat Reader. However, different from Excel, HTML, TXT, and RTF, PDF enables the embedding of the font description within a file. Logi Report therefore provides the embedded TTF font solution for PDF outputs. You can find it extremely helpful in the following cases:

* When you select TTF fonts to design a report, and these fonts are not within the client's existing font systems.
* When you have used the TTF and Acrobat Reader has to be updated with the language extension package to view the result, but you do not want to trouble users with it.

By embedding TTF fonts, the file size increases a little. However, it is still of reasonable size to be transferred over a network.

To take advantage of the PDF Embedded TTF Font feature (this feature is not supported on library components), take the following steps:

1. [Select the TTF to design reports](#Design).
2. Open the report.
3. In the Report Inspector, select the node representing the page report tab or web report and find its **Embedded Fonts** property. The value drop-down list of the property shows all the TTF fonts the report uses. You can select multiple fonts by holding down the Ctrl or Shift key.
4. Save the report and export it to PDF. Designer embeds the selected fonts in the PDF output.

When you select an embedded font while using TTF to design reports and set the Bold/Italic property to "true", if Designer can [find the related TTF file to match your setting](#Apply), Designer also embeds the matched font with the Bold/Italic property when you export the report to PDF.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569908631-Designing-the-Report-Pages)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735547328663-Making-High-Efficiency-Reports)
