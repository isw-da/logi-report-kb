---
title: "Exporting to PDF"
id: 1500009589381
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589381-Exporting-to-PDF
updated_at: 2021-07-24T05:54:40Z
---

# Exporting to PDF

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568082-Exporting-to-HTML)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568022-Exporting-to-Excel)

# Exporting to PDF

To export the results of a report to PDF file, follow the steps below:

1. Open the report that you want to export.
2. Select **File** > **Export** > ****To** PDF**.
3. In the [Export to PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500009586741-Export-to-PDF-Dialog) dialog, specify the settings as required.

   ![Export to PDF dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893840535/expt2pdf.gif)
4. When done, select **OK** to generate the file.

The following example shows how to export the results of a report to PDF format and view the exported result file, taking the sample report CustomerAnalysis.cls in SampleReports.cat as an example:

1. Select **File** > **Open**.
2. In the Open Report dialog, select the **Browse** button to open the catalog file **SampleReports.cat** in `<install_root>\Demo\Reports\SampleReports`, then open **CustomerAnalysis.cls** in the catalog.
3. Select **File** > **Export** >  **To PDF** to open the Export to PDF dialog.
4. Specify the path where the files will be exported and the file name as required. Here we use the default path `C:\Logi JReport\Designer\Demo\Reports\SampleReports\` and default name CustomerAnalysis\_CustomerAnalysis.pdf.
5. Check **TOC**, **Drilldown** and **Generate charts and barcodes using vector graphics**.
6. Check the **Encrypt** option to set the document open password and permissions password in the Encrypt dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893840791/encrypt.gif)
7. Check the **Sign** option to set a digital ID for the PDF file in the Sign Digital ID dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893841047/signid.gif)
8. Select **OK**.
9. In the Enter Parameter Values dialog, select **Default** to generate the results using the default parameter values.
10. Open the directory `C:\Logi JReport\Designer\Demo\Reports\SampleReports\` and find the exported files.
11. Open the file **CustomerAnalysis\_CustomerAnalysis.pdf** with the inputted document open password or permissions password using the Adobe Acrobat software.
12. The signature is displayed in the left Security Settings panel, and all information you set can be found there.
13. The Table of Contents (TOC) is displayed in the left panel, and includes the names of both groups and subgroups. If you select a group, the contents will be shown in the right panel.
14. Place the mouse pointer over a summary field. When it becomes a hand, select to view the details of the summary.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404889309847/frmt_expt_pdf.gif)

    Note that summaries should be inserted into the report in advance. They cannot be hidden or suppressed; otherwise you will not be able to get the drill-down files.

    Also, since the option Generate charts and barcodes using vector graphics is checked when exporting the report, when zooming in the chart, you will find that the chart is a vector graphic which never distorts.

**Notes:**

* If the color mode of your display adapter is less than 256 colors, when you export to PDF file using the standard method, charts cannot be compressed. This is because Logi JReport catches an image with less than 256 colors as a GIF image. A GIF image cannot be compressed.
* When you export a report which has summary fields, if the Drill Down checkbox is checked, every summary field in this report will generate a new file which is linked in the main file.
* In the Sign Digital ID dialog, by default, the information of Digital ID File and Password are checked. If there are any problems, the error messages will prompt you, such as Unable to import the chosen Digital ID file! or Incorrect password! and so on.
* Before exporting a page report tab or a web report using true type fonts, you should select the report tab name or the web report in the Report Inspector, and then set Embedded Fonts equal to all true type fonts that you have used in the report tab or web report. Otherwise the PDF files may not be displayed correctly.
* When you export a web control object, barcode or UDO to PDF, if you select Generate charts and barcodes using vector graphics, the results will be the vector graphic; if you select the Generate charts and barcodes using images, the results will be the bitmap.
* When a report, in which there is an object beyond its container, is exported to PDF, the overstepped part will be ignored in PDF file, but the overstepped part of objects in a paragraph can still be exported to PDF.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568082-Exporting-to-HTML)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568022-Exporting-to-Excel)
