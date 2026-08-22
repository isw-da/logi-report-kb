---
title: "Exporting to Text"
id: 4405661760663
section: "Delivering Your Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661760663-Exporting-to-Text
updated_at: 2022-01-27T20:34:46Z
---

# Exporting to Text

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661753751-Exporting-to-Excel)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661759255-Exporting-to-RTF)

# Exporting to Text

This topic describes how you can export a page or web report to a regular Text file or a CSV file. It also shows how you can improve the performance of running a page report to Delimited Format on Server.

This topic contains the following sections:

* [Exporting a Report to a Text File](#Text)
* [Exporting a Report to a CSV File](#CSV)
* [Improving the Performance of Running a Page Report to Delimited Format on Server](#Performance)

## Exporting a Report to a Text File

1. Open the report that you want to export.
2. Navigate to **File** > **Export** > **To Text**. Designer displays the [Export to Text dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661549207-Export-to-Text-Dialog-Box).

   ![Export to Text dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550853143/expt2txt.gif)
3. Select **Browse** to specify the destination directory and file name of Text file. You can also type the location and file name manually in the **Export to** text box (make sure that the folder you specify does exist; otherwise, Designer displays an error message).
4. If you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can select a report tab and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to change the order of the report tabs.
5. Make sure **Delimited Format** is cleared.
6. Specify whether to use user-defined density to export the report. If yes, specify the horizontal density and vertical density respectively ([select here](#Density) for some notes about setting the density).
   * **Horizontal Density**  
     Specify the value for each unit of the horizontal density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between columns.
   * **Vertical Density**  
     Specify the value for each unit of the vertical density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between columns.

   However, by exporting using user-defined densities, if you do not set the densities appropriately, the report fields may overlap each other in the output.
7. Select **Compress**
   if you want to generate the report in a compressed size, meaning, there is no clearance between the columns.
8. By default, Designer exports all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. If you only want to export data in the Detail panel, clear **Header and Footer**.
9. Specify whether to use CR-LF in Windows convention, or LF in UNIX convention as the end-of-line character.
10. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the Text output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
11. Select **OK** to start exporting.

The following are some tips for you when exporting a report to a Text file:

* Designer ignores the Columned property on the page report tabs or the web report when exporting the report to Text.
* Designer locates each object in the Text output according to its dimension values (X, Y, Width, and Height) that you have set in the Report Inspector.
* Designer cannot export the List object to a Text file.
* If the report contains the Drop-down List object, Designer only exports the selected value in the list.
* The objects, which seem in the same line in other formats (such as PDF), may be in different lines, or some unwanted blank lines are generated in the Text output. The exception is caused by the differences between the dimension values: Y and Height.
* When you set the value of Horizontal/Vertical Density,
  + The value of Horizontal/Vertical Density must be greater than the character's width/height of the smallest field in the report (smallest field is the field with the smallest font size); otherwise, Designer cannot apply the value you set.
  + If the value of Vertical Density is greater than 0 and the value of Horizontal Density is less than 0, Designer applies the value that you specify for Vertical Density and specifies the value of Horizontal Density.
  + If the value of Vertical Density is less than 0 and the value of Horizontal Density is greater than 0, Designer applies the value that you specify for Horizontal Density and specifies the value of Vertical Density.
  + If the values of Vertical Density and Horizontal Density are both greater than 0 and the value of Horizontal Density is less than 11, Designer applies the values that you specify for the two densities; otherwise, Designer specifies them.
  + If the values of Vertical Density and Horizontal Density are both less than 1, Designer specifies these densities.

## Exporting a Report to a CSV File

When exporting a report to a CSV file, you can set the [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) property on each page report tab or the web report to decide whether to export the report to a general CSV file or a columned CSV file. If you set the property to "false", Designer exports the report to a general CSV file; if you want to export the report to a columned CSV file, set the property to "true".

The following example shows exporting a page report which contains only one report tab to a general CSV file.

1. Open the page report.
2. In the Report Inspector, select the node that represents the report tab and set the **Columned** property to **false**.
3. Navigate to **File** > **Export** > **To Text**.
4. In the Export to Text dialog box, keep the default export destination.
5. Select **Delimited Format**.
6. Select **CSV Format** from the **Format** drop-down list.
7. To well align the records in the CSV output, you should select **Use Quote Mark**; otherwise, the commas in data values such as $78,321.00 conflicts with the delimiter (comma), and may potentially cause the data being separated incorrectly when the output file is further processed by other applications.

   For example, in the following output, it is difficult to figure out whether the value is $78321.00 or $78 and 321.00.

   Scarsdale,The Java King,(914) 657-9823,(914) 657-8745,$78,321.00
8. Select **Repeat Last Column Value If Null** so that when a cell in the CSV output has no value, Designer uses the value of the previous cell in the same column.
9. By default, Designer removes the blank spaces at the beginning and end of the field values in the CSV output. If you want to keep the spaces, clear **Trim Blank Spaces**.
10. Keep the other settings to the defaults.
11. Select **OK** to start exporting.

The following are some tips for you when exporting a report to a CSV file:

* You should not export a mailing label banded object to a columned CSV file.
* Whether you export a report to a general CSV file or a columned CSV file,
  + The data of each field should be in one column. If there is no data in a column, Designer places empty strings (" ") there automatically. In this case, Designer cannot compress the empty strings. Designer can compress a row if you select the Compress option only when there is no data in the entire line.
  + In the Export to Text dialog box, if you select Custom Delimited, you should export the report to a .txt file instead of a .csv file. Then, open the output file with Excel. In the Text Import Wizard dialog box, select **Delimited**, select **Next**, select **Other** in the Delimiters panel and type the delimiter you specify in the Export to Text dialog box, and then select **Finish** to view the report.
* When you export a report to a general CSV file,
  + Designer locates the objects in the output according to its dimension values (X, Y, Width, and Height) that you set in the Report Inspector.
  + In the output, you may find that some column names are not aligned with their DBFields, so they may display in different columns. To resolve this problem, make both the column names and its DBFields to be left aligned and adjust their location using the same geometry X.
* When exporting a report to a columned CSV file,
  you should specify the position for each object; otherwise, Designer places all the objects in the first column and the first row in the output.
  + Designer locates the objects in the output according to their Column Index and Row Index property values. When setting values for these two properties, pay attention to the following:
    - Make sure the values of the two properties for all objects in the report do not conflict with each other; otherwise, Designer may replace some objects in the output.
    - If the value of either property for an object is less than 1, Designer ignores this object and all its children.
    - In the output, you may find that some column names are not aligned with their DBFields. They may display in different columns. To resolve this problem, set the Column Index value of the column name and its DBField to the same.
  + If the report contains drawing objects, you need to manually adjust these objects' geometry properties: Top Attach Column, Top Attach Row, Bottom Attach Column, and Bottom Attach Row.

## Improving the Performance of Running a Page Report to Delimited Format on Server

If you want to improve the performance of running a page report to the delimited format such as CSV on Server, you need to predefine some properties for the report in Designer, and edit specific properties on Server. The following example shows how to do this.

1. In Designer, open the page report tab you want to run to the delimited format on Server.
2. In the Report Inspector, select the node of the report tab, set the properties **Fast Pass** and **Columned** to **true**.
3. Choose the object you want to display in the output, and then set the location for where you want to display it in the output.

   For example, for each DBField in the report tab, specify its exact coordinate using the properties **Column Index** and **Row Index**. Column Index refers to the column where to locate the object in the output, and Row Index refers to the row where to place the object. The numbers of the column and row start with 1, and are counted within its parent. For example, if you want to place a DBField in the first column and the second row in the detail panel of a banded object, set Column Index to **1** and Row Index to **2**.
4. Go to the **server.properties** file in `<server_install_root>\bin`, and change the property engine.single\_thread to **false**. This enables the property Fast Pass to take effect when running the report tab to the delimited format.
5. Publish the page report containing the report tab to Server. When you run or schedule the report, after you choose the report tab and then select the **Text** format, you can select **Delimited Format** to generate a delimited format file.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When you set the Fast Pass property to "true", in the banded header panel, the values of the objects that use global parameters to make calculations are incorrect. Page level calculation, such as Page Number and Total Page Number, is also incorrect. In order to avoid such errors, you should move these objects from the banded header panel to the banded footer panel.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661753751-Exporting-to-Excel)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661759255-Exporting-to-RTF)
