---
title: "Exporting to Excel"
id: 1500010099261
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099261-Exporting-to-Excel
updated_at: 2021-07-23T19:16:10Z
---

# Exporting to Excel

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099321-Exporting-to-PDF)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099381-Exporting-to-Text)

# Exporting to Excel

This topic describes how you can export the result of a page or web report to an Excel file.

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To Excel**. Designer displays the [Export to Excel dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058962-Export-to-Excel-Dialog-Box).

   ![Export to Excel dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848475927/expt2excl.gif)
3. Select the **Browse** button to specify the destination directory where to save the Excel and its file name. You can also type the location and file name manually in the **Directory** and **File Name** text boxes (make sure that the folder you specify does exist; otherwise, Designer displays an error message). If you do not type a name, Designer uses the report name as the Excel file name by default.
4. If you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report you want to export. Designer exports the selected report tabs into multiple sheets of the Excel file in the list order. You can make use of the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to change the order of the report tabs.
5. From the **Excel Version** drop-down list, select the version for the Excel file.
6. Select the format of the Excel file from the **Format** drop-down list.
   * To let Designer choose which format is the most appropriate, select **Auto Format**, then Designer determines whether to use Report Format or Column Format according to the objects in the report. If the report contains crosstabs or tables, Designer uses Column Format; otherwise, it uses Report Format. This option is selected by default. If you do not know which format is better, it is suggested that you select this option.
   * To make the format of the Excel output match the format as designed in the template, select **Report Format**, and then specify the available settings according to your requirements.
   * To export the report result to a general Excel file, select **Column Format**, in which case, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Column) property value for the report tab in the Report Inspector to decide the calculation method used for all components' row/column values in the report when exporting (due to the particularity of mailing label report, do not set the Columned property to true when you want to export it in this format).
   * To export only the report data without format, select **Data Format**. This option is only available for Excel 97-2003 Workbook (\*.xls). When you select Data Format, Designer cannot support formulas, barcodes, images, hyperlink property, charts, and all drawing objects such as lines, ovals, and boxes in the report, therefore, this format is not recommended when you export report result to Excel.
7. Select **More Options** to customize other properties for the Excel file.
8. If you have selected the format other than Data Format, select **Include Shapes in Export** to include the drawing objects in the Excel output, and specify the page header and footer text to display and whether to include gridlines when printing the exported Excel file.
9. From the **Word Wrap** drop-down list, specify the word wrap setting for the report components in the Excel output.
   * **All Keep Existing**  
     Select it if you want to keep all settings of each component's Word Wrap property as specified in the report.
   * **All Disabled**  
     Select it if you want to disable the Word Wrap property for all components, meaning, Designer takes the Word Wrap property for all components as false.
   * **All Enabled**  
     Select it if you want to enable the Word Wrap property for all components, meaning, Designer takes the Word Wrap property for all components as true.
10. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the Excel output. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
11. Select **OK** to start exporting.

You should pay attention to the following when using the Export to Excel feature:

* Designer can export multiple colors and languages in a report to an Excel file, but cannot export multiple pie charts and the Arc drawing object. For example, Excel only supports 56 kinds of colors, if there are more than 56 kinds of colors in a report, when you export the report to Excel, some colors are merged.
* Designer exports paragraphs and texts in a report as objects.
* If the report contains the Drop-down List object, Designer only exports the value selected in the list.
* If you set an object's Export to Excel property to false, Designer does not export the object and other objects contained in it.
* Designer exports gauge/surface chart in a report as bar chart, and stock chart as image.
* Designer does not export the minor tick marks on a chart.
* If the data type of the field on the category axis of a chart is Date, Time, or DateTime whose format confirms to the Date format of Excel, Designer exports the axis as a date axis, vice versa.
* If the field on the category axis of a chart is of the Number type and you use a constant interval to customize the tick marks on the axis, the settings cannot take effect.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Designer provides several properties related with exporting page report tabs to Excel, which you can use to enhance the report appearance in the Excel ouput, manage data in the Excel worksheet, improve the exporting performance, and so on. These properties include: [Merge to Next Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010061842-Banded-Page-Header-Properties#Panel), [Repeat in Detail Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010061842-Banded-Page-Header-Properties#Panel), [Remove Blank Row](https://devnet.logianalytics.com/hc/en-us/articles/1500010061842-Banded-Page-Header-Properties#Panel), [On New Sheet](https://devnet.logianalytics.com/hc/en-us/articles/1500010062402-Subreport-Properties#Sheet), [Rows per Sheet](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#Rows), [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index), [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010061722-Banded-Object-Properties#Index), [Bottom Attach Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010061882-Box-Properties#Attach), [Bottom Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500010061882-Box-Properties#Attach), [Top Attach Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010061882-Box-Properties#Attach), [Top Attach Row](https://devnet.logianalytics.com/hc/en-us/articles/1500010061882-Box-Properties#Attach), [Column Number](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#ColumnNumber), [Row Number](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#RowNumber), [Column Width List](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#ColumnWidth), and [Excel Buffer Size](https://devnet.logianalytics.com/hc/en-us/articles/1500010100701-Page-Report-Tab-Properties#ExcelBuffer). You can set them according to your requirements appropriately.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099321-Exporting-to-PDF)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099381-Exporting-to-Text)
