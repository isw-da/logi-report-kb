---
title: "Applying OpenType Fonts"
id: 43951152728973
section: "Designing Your Reports - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/43951152728973-Applying-OpenType-Fonts
updated_at: 2026-03-03T14:24:40Z
source_host: docs-report.zendesk.com
---
# Applying OpenType Fonts in Reports

You might find that well-designed reports in Designer become truncated when you run the reports on Server on a different platform. The reason is that various platforms use different font systems, and when JDK maps the fonts to a different platform, the reports appear with a discrepancy. To solve this problem, Report adopts the OpenType Font (OTF) administrative system of Java. You can design reports in any fonts in Designer. Then, when you publish the reports into the runtime environment, you can publish the fonts together with the reports, which are independent of the platform fonts. Report also provides the PDF embedded fonts solution, meaning Report can embed the fonts in the PDF output, so users do not need to install the fonts on their local machines. This topic describes how you can design reports with OTF, apply the Bold and Italic properties to OTF, deliver OTF to the runtime environment, and export reports with OTF in different formats.

The following sections describe how to use OTF in your reports:

- Designing Reports with OTF

- Applying Bold and Italic Properties to OTF

- Publishing OTF to the Runtime Environment

- Delivering OTF in Excel/RTF/HTML/TXT

- 
Delivering OTF in PDF- Using -D Options to Configure OTF in PDF Output

## 
Designing Reports with OTF

When you design reports that you want to run on a platform different from where you design them, it is best to use OTF fonts.

To design reports with OTF

- Copy the OpenType Font files *.otf to the <designer_install_root>\font directory of Designer. You can find the OTF fonts in your system's Font directory or from the Internet.

- In Designer, open a report and select the text you want to apply the OTF font.

- On the Home menu bar, select the drop-down arrow of the font list and scroll down to the bottom of the list. You can then find the fonts with an ** before their name. These are the OTF fonts you have copied. Select the OTF font you want to apply.

- Preview the report and save the report until you are satisfied with the result.

- After upgrading JDK to v17, when you find the OTF you apply in a report slightly shifts upwards in the report output, you can add the -Dlogireport.applyLeading4Ascent option in Designer's startup file JReport.bat/JReport.sh in <install_root>\bin to improve the display, for example, -Dlogireport.applyLeading4Ascent="**FreeSerif;**SourceHanSerifSC-ExtraLight".

## 
Applying Bold and Italic Properties to OTF

Designer supports the Bold and Italic properties for OTF. When you select an OTF font and set the Bold/Italic property to "true", Designer first searches the <designer_install_root>\font directory automatically to check all the OTF files related with the OTF font you have selected previously. If there is such an OTF file holding the Bold/Italic property, Designer uses the font style defined in this file to match your setting and make the Bold/Italic property take effect; if not, Designer finds the specified font in your platform fonts and applys the Bold/Italic property directly.

## 
Publishing OTF to the Runtime Environment

When you publish reports from Designer to Server, if the reports use OTF fonts, Designer prompts you the Publish Additional Resources dialog box to publish the font files at the same time. After Designer finishes the publishing task, you can find the corresponding font files in the <server_install_root>\font directory of Server.

## 
Delivering OTF in Excel/HTML/TXT/RTF

For report outputs in Excel, HTML, TXT, and RTF, they can automatically find the OTF fonts from the system's Font directory to display the fonts correctly. However, to avoid any discrepancy in the report outputs, if you want to deliver the report in these formats, you should choose the OTF fonts that are common on the Windows systems. When you have to use fonts that do not exist in the client's system, you can choose the embedded OTF font solution as shown in the following section.

## 
Delivering OTF in PDF

To view PDF outputs with other character sets, for example, Chinese fonts, you need to install special language packages. Also, if you design reports with fonts that are not within Acrobat's internal fonts, Acrobat maps them differently. The two cases cause trouble to users when they view or print a report with Acrobat Reader. However, different from Excel, HTML, TXT, and RTF, PDF enables the embedding of the font description within a file. Report therefore provides the embedded OTF font solution for PDF outputs. You can find it extremely helpful in the following cases:

- When you select OTF fonts to design a report, and these fonts are not within the client's existing font systems.

- When you have used the OTF and Acrobat Reader has to be updated with the language extension package to view the result, but you do not want to trouble users with it.

By embedding OTF fonts, the file size increases a little. However, it is still of reasonable size to be transferred over a network.

To take advantage of the PDF Embedded OTF Font feature (this feature is not supported on library components), take the following steps:

- Select the OTF to design reports.

- Open the report.

- In the Report Inspector, select the node representing the page report tab or web report and find its Embedded Fonts property. The value drop-down list of the property shows all the OTF fonts the report uses. You can select multiple fonts by holding down the Ctrl or Shift key.

- Save the report and export it to PDF. Designer embeds the selected fonts in the PDF output.

When you select an embedded font while using OTF to design reports and set the Bold/Italic property to "true", if Designer can find the related OTF file to match your setting, Designer also embeds the matched font with the Bold/Italic property when you export the report to PDF.

### 
Using -D Options to Customize OTF in PDF Output

You can add the following options in Designer's startup file JReport.bat/JReport.sh in <install_root>\bin to specify some OTF properties in your PDF output.

- -Dlogireport.pdf.UsePdfFontAscent
Use this option when you want to apply the float ascent value in the PDF font for embedded OTFs in your PDF output (by default, Designer applies that of the JDK font). The value of this option can contain multiple items separated by the ";" character. Each item should be an OTF font name starting with "**" or be the AllEmbeddedTTF keyword, for example, -Dlogireport.pdf.UsePdfFontAscent="**FreeSerif;**SourceHanSerifSC-ExtraLight;AllEmbeddedTTF".
- When one of these items is AllEmbeddedTTF, Designer applies the ascent of the PDF font for all embedded OTFs in the PDF output。

- When none of these items is AllEmbeddedTTF, Designer only applies the ascent of the PDF font for the embedded OTFs the names of which you have included in this option.

- -Dlogireport.pdf.MapToTTF
Use this option to map non-OTF fonts to OTF fonts in the PDF output. The value of the option can contain multiple items separated by the ";" character. Each item should either be a font name that does not start with "**" in the Font Face property drop-down list, or be the keyword All, for example, -Dlogireport.pdf.MapToTTF="Arial;Times New Roman;All".
- When one of these items is All, Designer tries to map each non-OTF font in the report template to an OTF font if there is a matched OTF file in the <install_root>\font directory of Designer.

- When none of these items is All, for each item, if it is used in the report template, Designer tries to map it to an OTF font.

- -Dlogireport.pdf.EmbeddedFonts
Use this option to specify the OTF fonts you want to embed into the PDF output. The value of the option can contain multiple items separated by the ";" characters. Each item should either be an OTF font name that starts with "**" in the Font Face property drop-down list, or be the keyword All, for example, -Dlogireport.pdf.EmbeddedFonts="**FreeSerif;**SourceHanSerifSC-ExtraLight;All".
- When one of these items is All, Designer embeds every OTF in the report template into the PDF output.

- When none of these items is All, for each item, if it is used in the report template, Designer embeds the OTF into the PDF output.
