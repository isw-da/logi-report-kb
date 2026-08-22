---
title: "Exporting to Text"
id: 1500009568142
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568142-Exporting-to-Text
updated_at: 2021-07-24T05:54:39Z
---

# Exporting to Text

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589281-Improving-the-Performance-of-Exporting-to-Excel)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589421-Exporting-to-RTF)

# Exporting to Text

Logi JReport supports exporting to both a regular Text file and a CSV file.

Below is a list of the sections covered in this topic:

> * [Exporting the Report Results to a Text File](#Text)
> * [Exporting the Report Results to a CSV File](#CSV)
> * [Improving the Performance of Running a Report to Delimited Format on Logi JReport Server](#Performance)

## Exporting the Report Results to a Text File

To export the results of a report to a Text file, follow the steps below:

1. Open the report that you want to export.
2. Select **File** > **Export**  >  **To Text**. The [Export to Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009565602-Export-to-Text-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889309335/expt2txt.gif)
3. Specify the destination of the exported file.
4. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839511/btn_mvup3.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839767/btn_mvdwn3.gif) to change the order or the report tabs.
5. Make sure that the Delimited Format checkbox is unchecked.
6. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported Text result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
7. Specify other settings according to your requirements.
8. Select **OK** to perform the export operation.

**Note:** When exporting a report to a Text file, pay attention to the following:

* The property Columned on the page report tabs or the web report will be ignored.
* Each object in the exported result file will be located according to its dimension values (x, y, width and height) you set in the Report Inspector.
* The list object could not be exported to a Text file.
* If the report contains drop-down list object, only the selected value in the list can be exported.
* The objects, which seem in the same line in other formats (such as PDF), may be in the different lines, or some unwanted blank lines will be generated. The exception is caused by the differences between the dimension values - y and height.

## Exporting the Report Results to a CSV File

When exporting the results of a report to a CSV file, you can set the property Columned to decide whether to export the results to a general CSV file or a columned CSV file. If you set the property to false, the report will be exported to a general CSV file. If you want to export the report to a columned CSV file, set the property to true.

The following is an example about exporting a page report which contains only one report tab to a general CSV file:

1. Open the page report.
2. In the Report Inspector, select the root node that represents the report tab and set the property Columned to false.
3. Select **File** > **Export**  >  **To Text**. The [Export to Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009565602-Export-to-Text-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889309335/expt2txt.gif)
4. Specify the destination of the exported file as required.
5. Check **Delimited Format**  checkbox, and then select **CSV Delimited** from the Format drop-down list.
6. To enable records to be aligned well in the exported file, you are recommended to check **Use Quote Mark**. Otherwise, the commas in data values such as $78,321.00 will conflict with the delimiter (comma), and may potentially cause the data to be separated incorrectly when the exported file is further processed by other applications. The following shows an example:

   Scarsdale,The Java King,(914) 657-9823,(914) 657-8745,$78,321.00

   As shown above, it is difficult to determine whether the value is $78321.00 or $78 and 321.00.
7. Select **OK** to start exporting.

**Notes:**

* Whether a report is exported to a general CSV file or a columned CSV file,
  + The data of each field should be in one column. If there is no data in a column, empty strings (" ") will be placed there automatically. In which case, the empty strings cannot be compressed. Only if there is no data in the entire line, can a row be compressed when you check the Compress option.
  + In the Export to Text dialog, if you select Custom Delimited, you should export the report to a .txt file instead of a .csv file. Then, open the exported file with Excel, and the Text Import wizard will be displayed. In this wizard, check the **Delimited** radio button, select **Next**, check **Other** on the Delimiters panel and key in the delimiter you specify in the Export to Text dialog, and then select **Finish** to view the results.
* When you specify to export a report to a general CSV file,
  + Objects in the exported file will be located according to its dimension values (X, Y, Width, Height) you set in the Report Inspector.
  + In the exported file, you may find that some column names are not aligned with their DBFields, so they may be displayed in different columns. To resolve this problem, make both the column names and its DBFields to be left aligned and adjust their location using the same Geometry X before exporting it to a general CSV file.
* When you specify to export a report to a columned CSV file,
  + Objects in the exported file will be located according to their Row Index and Column Index property values. When setting values for these two properties, pay attention to the following:
    - Make sure that the Row Index and Column Index property values for all objects in the report do not conflict with each other. Otherwise, some objects may be replaced.
    - If either the Row Index value or Column Index value of an object is less than 1, Logi JReport will ignore this object and all its children.
  + In the exported file, you may find that some column names are not aligned with their DBFields. They may be displayed in different columns. To resolve this problem, set the Column Index value of the column name and its DBField to the same; if they are different, adjust it manually before exporting it to CSV format.
  + If the report contains drawing objects, you need to manually adjust these objects' geometry properties, which are Top Attach Column, Top Attach Row, Bottom Attach Column and Bottom Attach Row.
  + You are not recommended to export a mailing label report to a columned CSV file.

## Improving the Performance of Running a Report to Delimited Format on Logi JReport Server

When exporting a page report to Text, if you want to improve the performance of running the page report to Delimited Format (such as the CSV format) on Logi JReport Server, you are first required to set certain settings in Logi JReport Designer. After which you can then publish the report to Logi JReport Server for running to Delimited Format. See the example below:

1. Start Logi JReport Designer and open the page report tab you want to run to Delimited Format on Logi JReport Server.
2. In the Report Inspector, browse to the node of the report tab, find the two properties Fast Pass and Columned, and then set them to true.
3. Choose the object you want to display in the result file, and then set the location for where you want it to be shown in the result file.

   To do this, select the object, and set its Column Index and Row Index properties in the Report Inspector as required. ColumnIndex refers to the column where the object will be located, and RowIndex refers to the row where the object will be located in the result file. The numbers of the column and row start with 1, and are counted within its parent. For example, if you want to place the object in the first column and the second row in the detail section, set ColumnIndex = 1 and RowIndex = 2.
4. Go to the server.properties file in `<server_install_root>\bin`, and change the property engine.single\_thread = false. This enables the property Fast Pass to take effect when running the report tab to Delimited Format.
5. Publish the page report containing the report tab to Logi JReport Server. When you run or schedule the report, after you choose the report tab and then choose To Text format, select the **Delimited Format** box, and then select **Submit** to generate a Delimited Format file.

**Notes:**

* When the Fast Pass property is set to true, in the report header panel, the values of the objects that use global parameters to make calculations will be incorrect. Page level calculation, such as Page Number and Total Page Number, will also be incorrect. In order to avoid such errors, you should move these objects from the report header panel to the report footer panel.
* Remember to set the positions for objects with the Column Index and Row Index properties. Otherwise, all the objects will be located in the first column and the first row of the result file.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589281-Improving-the-Performance-of-Exporting-to-Excel)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589421-Exporting-to-RTF)
