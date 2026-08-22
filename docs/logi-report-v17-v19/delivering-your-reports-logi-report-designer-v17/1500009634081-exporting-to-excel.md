---
title: "Exporting to Excel"
id: 1500009634081
section: "Delivering Your Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634081-Exporting-to-Excel
updated_at: 2021-07-24T16:03:59Z
---

# Exporting to Excel

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611002-Exporting-to-PDF) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611082-Exporting-to-Text)

# Exporting to Excel

This topic introduces how to export the results of a report to an Excel file.

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To Excel**. The [Export to Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009631081-Export-to-Excel-Dialog) dialog appears.

   ![Export to Excel dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911671959/expt2excl.gif)
3. Select the **Browse** button to specify the destination directory where the exported Excel file will be placed and the name of the file. You can also type the location and file name manually in the Directory and File Name text boxes (make sure that the folder you specify does exist, otherwise an error message will be produced).
4. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported into multiple sheets of the Excel file in the list order. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404911669015/btn_mvup3.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904224919/btn_mvdwn3.gif) to change the order of the report tabs.
5. From the Excel Version drop-down list, select the version for the exported Excel file.
6. Select the format of the exported Excel file from the Format drop-down list.
   * To let Logi Report choose which format is the most appropriate, select **Auto Format**, then Logi Report will judge whether to use Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Column Format will be used; otherwise it is Report Format. This option is selected by default. If you do not know which format is better, it is suggested that you select this option.
   * To make the format of the result file match the format as designed in the template, select **Report Format**, and then specify the available settings according to your requirements.
   * To export the report result to a general Excel file, select **Column Format**, in which case, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Column) property value for the report tab in the Report Inspector to decide the calculation method used for all components' row/column values in the report when exporting (due to the particularity of mailing label report, do not set the Columned property to true when you want to export it in this format).
   * To export only the report data without format, select **Data Format**. This option is only available for the Excel version Excel 97-2003 Workbook (\*.xls). When Data Format is selected, formulas, barcodes, images, hyperlink property, charts and all drawing objects such as line, oval, and box will not be supported, therefore this format is not recommended when exporting report result to Excel.
7. You can select **More Options** to customize other properties for the exported Excel file.
8. If you have selected the format other than Data Format, select **Include Shapes in Export** if you want to include the drawing objects in the exported Excel file, and specify the page header and footer text to be displayed and whether to include gridlines when printing the exported Excel file.
9. From the Word Wrap drop-down list, specify the word wrap setting for the report components in the Excel result.
   * **All Keep Existing**  
      Keeps all settings of each component's Word Wrap property as specified in the report.
   * **All Disabled**  
      Disables the Word Wrap property for all components, that is the Word Wrap property is made false for all components.
   * **All Enabled**  
      Enables the Word Wrap property for all components, that is the Word Wrap property will be made true for all components.
10. Select **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the Excel result. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
11. Select **OK** to start exporting.

You should pay attention to the following when using the Export to Excel feature:

* Multiple colors and languages in a report can be exported to an Excel file, but multiple pie charts and the Arc drawing object cannot be. For example, Excel only supports 56 kinds of colors, if there are more than 56 kinds of colors in a report, when you export the report to Excel, some colors will be merged.
* Paragraphs and texts in the report will be exported as objects.
* If the data type of the field on the category axis of a chart is Date, DateTime or Time whose format confirms to the date format of the Excel, the axis will be exported as a date axis, otherwise, it will not be exported as a date axis.
* Gauge and surface chart in the report will be exported as bar chart while stock chart will be exported as image.
* The minor tick marks on a chart will not be exported.
* If the field on the category axis of a chart is of Number type and you use a constant interval to customize the tick marks on the axis, the settings will not take effect.
* If the report contains the Drop-down List object, only the value selected in the list will be exported.
* If you set an object's Export to Excel property to false, the object and other objects contained in it will not be exported.

**Tip:** Logi Report provides several properties related with exporting page report tabs to Excel, which can help you enhance the report appearance in the exported Excel file, manage data in the Excel worksheet, improve the exporting performance, and so on. These properties include: [Merge to Next Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009612062-Banded-Page-Header-Properties#Panel), [Repeat in Detail Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009612062-Banded-Page-Header-Properties#Panel), [Remove Blank Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009612062-Banded-Page-Header-Properties#Panel), [On New Sheet](https://devnet.logianalytics.com/hc/en-us/articles/1500009635721-Subreport-Properties#Sheet), [Rows per Sheet](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Rows), [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index), [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009635041-Banded-Object-Properties#Index), [Bottom Attach Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009612102-Box-Properties#Attach), [Bottom Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009612102-Box-Properties#Attach), [Top Attach Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009612102-Box-Properties#Attach), [Top Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009612102-Box-Properties#Attach), [Column Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#ColumnNumber), [Row Number](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#RowNumber), [Column Width List](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#ColumnWidth), [Excel Buffer Size](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#ExcelBuffer). You can set them according to your requirements appropriately.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611002-Exporting-to-PDF) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611082-Exporting-to-Text)
