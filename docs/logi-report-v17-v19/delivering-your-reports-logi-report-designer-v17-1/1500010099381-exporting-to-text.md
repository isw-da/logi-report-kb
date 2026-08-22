---
title: "Exporting to Text"
id: 1500010099381
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099381-Exporting-to-Text
updated_at: 2021-07-23T19:16:12Z
---

# Exporting to Text

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099261-Exporting-to-Excel)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099361-Exporting-to-RTF)

# Exporting to Text

This topic describes how you can export the result of a page or web report to a regular Text file or a CSV file. It also shows how you can improve the performance of running a page report to Delimited Format on Server.

This topic contains the following sections:

* [Exporting the Report Result to a Text File](#Text)
* [Exporting the Report Result to a CSV File](#CSV)
* [Improving the Performance of Running a Page Report to Delimited Format on Server](#Performance)

## Exporting the Report Result to a Text File

1. Open the report that you want to export.
2. Select **File** > **Export**  >  **To Text**. Designer displays the [Export to Text dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096741-Export-to-Text-Dialog-Box).

   ![Export to Text dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848472855/expt2txt.gif)
3. Select the **Browse** button to specify the destination directory and file name of Text file. You can also type the location and file name manually in the **Export to** text box (make sure that the folder you specify does exist; otherwise, Designer displays an error message).
4. If you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can make use of the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to change the order of the report tabs.
5. Make sure that the **Delimited Format** checkbox is unselected.
6. Specify whether to use user-defined density to export the report result. If yes, specify the horizontal density and vertical density respectively ([select here](#Density) for some notes about setting the density):
   * **Horizontal Density**  
     Specify the value for each unit of the horizontal density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between columns.
   * **Vertical Density**  
     Specify the value for each unit of the vertical density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between columns.

   However, by exporting using user-defined densities, if you do not set the densities appropriately, the fields in the report may overlap each other, so you are not recommended to use this way to export the report result to Text.
7. Select **Compress**
   if you want to generate the report result in a compressed size, that is to say there is no clearance between the columns.
8. By default, Designer exports all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. If you only want to export data in the Detail panel, clear **Header and Footer**.
9. Specify whether to use CR-LF in Windows convention, or LF in Unix convention as the end-of-line character.
10. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the Text output. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
11. Select **OK** to start exporting.

You should pay attention to the following when using the Export to Text feature:

* Designer ignores the property Columned on the page report tabs or the web report during exporting.
* Designer locates each object in the Text output according to its dimension values (X, Y, Width, and Height) that you have set in the Report Inspector.
* Designer cannot export the List object to a Text file.
* If the report contains the Drop-down List object, Designer only exports the selected value in the list.
* The objects, which seem in the same line in other formats (such as PDF), may be in the different lines, or some unwanted blank lines are generated. The exception is caused by the differences between the dimension values: Y and Height.
* When you set the value of Horizontal/Vertical Density:
  + The value of Horizontal/Vertical Density must be greater than the character's width/height of the smallest field in the report (smallest field is the field with the smallest font size); otherwise, Designer cannot apply the value you set.
  + If the value of Vertical Density is greater than 0 and the value of Horizontal Density is less than 0, Designer applies the value that you specify for Vertical Density and specify the value of Horizontal Density.
  + If the value of Vertical Density is less than 0 and the value of Horizontal Density is greater than 0, Designer applies the value that you specify for Horizontal Density and specify the value of Vertical Density.
  + If the values of Vertical Density and Horizontal Density are both greater than 0 and the value of Horizontal Density is less than 11, Designer applies the values that you specify for the two densities; otherwise, Designer specifies them.
  + If the values of Vertical Density and Horizontal Density are both less than 1, Designer specifies these densities.

## Exporting the Report Result to a CSV File

When exporting the result of a report to a CSV file, you can set the property Columned on each page report tab or the web report to decide whether to export the result to a general CSV file or a columned CSV file. If you set the property to false, Designer exports the report to a general CSV file. If you want to export the report to a columned CSV file, set the property to true.

The following is an example about exporting a page report which contains only one report tab to a general CSV file:

1. Open the page report.
2. In the Report Inspector, select the root node that represents the report tab and set the property **Columned** to **false**.
3. Select **File** > **Export**  >  **To Text**.
4. In the Export to Text dialog box, keep the default export destination.
5. Select the **Delimited Format** checkbox, and then select **CSV Format** from the **Format** drop-down list.
6. To enable records to be aligned well in the CSV output, you are recommended to select **Use Quote Mark**; otherwise, the commas in data values such as $78,321.00 conflicts with the delimiter (comma), and may potentially cause the data being separated incorrectly when the exported file is further processed by other applications. The following shows an example:

   Scarsdale,The Java King,(914) 657-9823,(914) 657-8745,$78,321.00

   As shown above, it is difficult to determine whether the value is $78321.00 or $78 and 321.00.
7. Select **Repeat Last Column Value If Null** so that when a cell in the CSV output has no value, Designer uses the value of the previous cell in the same column.
8. Keep the other settings to the defaults.
9. Select **OK** to start exporting.

You should pay attention to the following when exporting a report to a CSV file:

* Whether a report is exported to a general CSV file or a columned CSV file,
  + The data of each field should be in one column. If there is no data in a column, Designer places empty strings (" ") there automatically. In this case, Designer cannot compress the empty strings. Designer can compress a row if you select the Compress option only when there is no data in the entire line.
  + In the Export to Text dialog box, if you select Custom Delimited, you should export the report to a .txt file instead of a .csv file. Then, open the exported file with Excel. In the Text Import Wizard dialog box, select the **Delimited** radio button, select **Next**, select **Other** in the Delimiters panel and input the delimiter you specify in the Export to Text dialog box, and then select **Finish** to view the result.
* When you specify to export a report to a general CSV file,
  + Designer locates the objects in the output according to its dimension values (X, Y, Width, and Height) that you set in the Report Inspector.
  + In the exported file, you may find that some column names are not aligned with their DBFields, so they may display in different columns. To resolve this problem, make both the column names and its DBFields to be left aligned and adjust their location using the same geometry X before exporting it to a general CSV file.
* When you specify to export a report to a columned CSV file,
  + Designer locates the objects in the exported file according to their Row Index and Column Index property values. When setting values for these two properties, pay attention to the following:
    - Make sure that the Row Index and Column Index property values for all objects in the report do not conflict with each other; otherwise, some objects may be replaced.
    - If either the Row Index value or Column Index value of an object is less than 1, Designer ignores this object and all its children.
  + In the exported file, you may find that some column names are not aligned with their DBFields. They may display in different columns. To resolve this problem, set the Column Index value of the column name and its DBField to the same; if they are different, adjust it manually before exporting it to CSV format.
  + If the report contains drawing objects, you need to manually adjust these objects' geometry properties, which are Top Attach Column, Top Attach Row, Bottom Attach Column, and Bottom Attach Row.
  + You are not recommended to export a mailing label report to a columned CSV file.

## Improving the Performance of Running a Page Report to Delimited Format on Server

If you want to improve the performance of running a page report to Delimited Format (such as the CSV format) on Server, you need to predefine some properties for the report in Designer, and edit specific properties in Server. The following example shows how to do this.

1. In Designer, open the page report tab you want to run to Delimited Format on Server.
2. In the Report Inspector, browse to the node of the report tab, find the two properties: **Fast Pass** and **Columned**, and then set them to **true**.
3. Choose the object you want to display in the result file, and then set the location for where you want to display it in the result file.

   To do this, select the object, and set its **Column Index** and **Row Index** properties in the Report Inspector as required. Column Index refers to the column where to locate the object in the result file, and Row Index refers to the row where to place the object in the result file. The numbers of the column and row start with 1, and are counted within its parent. For example, if you want to place the object in the first column and the second row in the detail section, set **Column Index = 1** and **Row Index = 2**.
4. Go to the **server.properties** file in `<server_install_root>\bin`, and change the property **engine.single\_thread = false**. This enables the property Fast Pass to take effect when running the report tab to Delimited Format.
5. Publish the page report containing the report tab to Server. When you run or schedule the report, after you choose the report tab and then select the Text format, you can select the **Delimited Format** option to generate a Delimited Format file.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* When you set the Fast Pass property to true, in the report header panel, the values of the objects that use global parameters to make calculations are incorrect. Page level calculation, such as Page Number and Total Page Number, is also incorrect. In order to avoid such errors, you should move these objects from the report header panel to the report footer panel.
* Remember to set the positions for objects with the Column Index and Row Index properties; otherwise, Designer places all the objects in the first column and the first row in the result file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099261-Exporting-to-Excel)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099361-Exporting-to-RTF)
