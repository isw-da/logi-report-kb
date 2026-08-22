---
title: "Font Face Display Issues in PDF Export"
id: 360047981574
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047981574-Font-Face-Display-Issues-in-PDF-Export
updated_at: 2020-07-27T22:36:29Z
---

# Font Face Display Issues in PDF Export

### Problem

Some fonts are getting cut off or incorrectly displayed when exporting a report to PDF.

### Solution

You might find that well-designed reports in Logi Report Designer become truncated when you run the reports in Logi Report Server on a different platform. The reason is that various platforms use different font systems and by mapping the fonts to a different platform by JDK, the report result is shown with a discrepancy.

To solve this problem, Java provides the True Type Font (TTF) administrative system. Logi Report supports the TTF system, which enables you to design reports in any font. When you publish the reports into the runtime environment, you can publish the fonts together with the reports.

For details of how to design your reports with TTF fonts in Logi Report Designer and how to publish the TTF fonts to the Logi Report Server, please refer to the following online document:  
  
<https://documentation.logianalytics.com/logireportdesignerguidev17/content/html/appendix/ttf.htm>

Additionally, to view PDF report results with other character sets (e.g. Chinese fonts), you will need to install special language packages. If you design reports with fonts that are not within Acrobat's internal fonts, they will be mapped differently. The above two cases will cause trouble when viewing or printing a report with Acrobat Reader. Logi Report provides the embedded TTF font solution for PDF report results to solve this issue. For details of how to embed TTF fonts inside the PDF result, please refer to the section "Delivering TTF result in PDF" in the above document, or click on the following link:  
  
<https://documentation.logianalytics.com/logireportdesignerguidev17/content/html/appendix/ttf.htm#DeliverPDF>
