---
title: "Exporting to Excel"
id: 1500009568022
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568022-Exporting-to-Excel
updated_at: 2021-07-24T05:54:43Z
---

# Exporting to Excel

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589381-Exporting-to-PDF)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589261-Setting-the-Excel-Buffer-Size)

# Exporting to Excel

To export the results of a report to an Excel file, follow the steps below:

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To Excel**. The [Export to Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565522-Export-to-Excel-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889310615/expt2excl.gif)
3. Select the **Browse** button to specify the destination directory where the exported Excel file will be placed, or type the destination directory into the Directory text field directly (make sure that the folder you specify here does exist).
4. Specify the name of the exported Excel file in the File Name text field. If you do not type the name, Logi JReport will use the report name as the Excel file name by default.
5. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported into multiple sheets of the Excel file in the list order. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839511/btn_mvup3.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839767/btn_mvdwn3.gif) to change the order or the report tabs.
6. From the Excel Version drop-down list, select the version for the exported Excel file.
7. Specify the format of the exported Excel file.
   * To make the format of the result file match the format as designed in the template, check **Report Format**, and then specify the available settings according to your requirements.
   * To export the report results to a general Excel file, check **Column Format**, in which case, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property value for the report tab in the Report Inspector to decide the calculation method used for all components' row/column values in the report when exporting (due to the particularity of mailing label report, do not set the Columned property to true when you want to export it in this format).
   * To export only the report data without format, check **Data Format**. This option is only available for the Excel version Excel 97-2003 Workbook (\*.xls).
8. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported Excel result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
9. When done, select **OK** to start exporting.

**Notes:**

* Multiple colors and languages in a report can be exported to an Excel file, but multiple pie charts and the arc drawing object cannot be. For example, Excel only supports 56 kinds of colors, if there are more than 56 kinds of colors in a report, when you export the report to Excel, some colors will be merged.
* When exporting a report to Excel,
  + Paragraphs and texts in the report will be exported as objects.
  + If the data type of the field on the category axis of a chart is Date, DateTime or Time whose format confirms to the date format of the Excel, the axis will be exported as a date axis, otherwise, it will not be exported as a date axis.
  + Gauge and surface chart in the report will be exported as bar chart while stock chart will be exported as image.
  + The minor tick marks on a chart will not be exported.
  + If the field on the category axis of a chart is of Number type and you use a constant interval to customize the tick marks on the axis, the settings will not take effect.
  + If the report contains a drop-down list, only the value selected in the list will be exported.
  + If you set an object's Export to Excel property to false, the object and other objects contained in it will not be exported.
* When Data Format is selected in the Export to Excel dialog, formulas, barcodes, images, HyperLink property, charts and all drawing objects will not be supported, therefore, we recommend not using this format when exporting report results to Excel.

The following topics are related to exporting the report results to Excel:

> * [Setting the Excel Buffer Size](https://devnet.logianalytics.com/hc/en-us/articles/1500009589261-Setting-the-Excel-Buffer-Size)
> * [Setting the Maximum Number of Rows for Every Worksheet](https://devnet.logianalytics.com/hc/en-us/articles/1500009589301-Setting-the-Maximum-Number-of-Rows-for-Every-Worksheet)
> * [Setting the Excel Column Width](https://devnet.logianalytics.com/hc/en-us/articles/1500009568042-Setting-the-Excel-Column-Width)
> * [Realigning Objects for a Better Appearance in the Exported Excel File](https://devnet.logianalytics.com/hc/en-us/articles/1500009589341-Realigning-Objects-for-a-Better-Appearance-in-the-Exported-Excel-File)
> * [Specifying Subreport Location in the Exported Excel File](https://devnet.logianalytics.com/hc/en-us/articles/1500009589361-Specifying-Subreport-Location-in-the-Exported-Excel-File)
> * [Controlling Banded Object Panels in the Exported Excel File](https://devnet.logianalytics.com/hc/en-us/articles/1500009589321-Controlling-Banded-Object-Panels-in-the-Exported-Excel-File)
> * [Improving the Performance of Exporting to Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009589281-Improving-the-Performance-of-Exporting-to-Excel)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589381-Exporting-to-PDF)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589261-Setting-the-Excel-Buffer-Size)
