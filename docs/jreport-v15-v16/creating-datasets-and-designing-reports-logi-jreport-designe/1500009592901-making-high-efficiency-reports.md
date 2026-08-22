---
title: "Making High-efficiency Reports"
id: 1500009592901
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592901-Making-High-efficiency-Reports
updated_at: 2021-07-24T05:53:47Z
---

# Making High-efficiency Reports

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592941-Managing-Report-Tabs-in-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571042-Saving-a-Page-Report)

# Making High-efficiency Reports

The following ways are provided for you to make reports efficient, reliable, and fast at runtime:

* Suppress all unused panels in a banded object, such as Group Header and Footer panels which are not adding values to the report tab.

  To do this, select the panel, go to the Report Inspector, and then change the property Suppress to true. When you right select in the panel and select Hide it also sets Suppress to true.

  This is more efficient than just hiding the panel.
* Set the precision (length) of DBFields or record level formulas to the size of the maximum value you need to display in the report tab. Making them larger than necessary wastes resources.

  **To do this:**

  1. Make sure the option "Forbid editing data object properties" is unchecked in the Catalog category of the Options dialog.
  2. Go to the Catalog Manager, expand the Properties sheet.
  3. Select the DBField or record level formula, then change the Precision property to an appropriate value.
* You can improve the report performance by setting the data buffer size to a larger value.  

  By default, the size of data buffer is 2MB. When data exceeds the default size, data will be written to disk, which will slow down the report processing. Logi JReport Designer enables you to set data buffer size by specifying two properties of a dataset or subreport in the Report Inspector: Records per Page and Max Page Number. For details, see [Data Buffer](https://devnet.logianalytics.com/hc/en-us/articles/1500009591461-Properties-of-Dataset-in-Page-Report#DataBuffer).
* Adjust Result Buffer.  

  The result buffer is used to store the report result in pages. Its default size is 4 which indicates 4 pages of the report result are allocated to the result buffer, other pages will be stored on disk. If you have enough memory, to get better performance, you can increase the result buffer size to store more pages of report result.

  To adjust the result buffer size, in the Report Inspector, highlight the node which represents the report tab, and then change the value of Result Buffer Size to the number of pages you want to hold in memory.
* Adjust Excel Buffer for exporting to Excel.  
    
   The Excel buffer is used to store the report result in excel buffer sheets when exporting to Excel format. Its default size is 1, which indicates 1 sheet of the report result are allocated to the result buffer; other sheets will be stored on disk. If you have enough memory, you can increase the Excel buffer size to store more sheets of excel format report result in memory. For details, see
  [Setting the Excel Buffer Size](https://devnet.logianalytics.com/hc/en-us/articles/1500009589261-Setting-the-Excel-Buffer-Size).
* When running a report to the Delimited Format (such as the CSV format) on Logi JReport Server, the property Fast Pass can help you speed up the generation process. Setting Fast Pass to true will enable you to specify the position of the object you want to display in the result file, thus Logi JReport will not calculate the position for every object during the generation process.

  **To use this method:**

  1. In the Report Inspector, select the node that represents the report tab and set the properties Fast Pass and Columned to **true**.
  2. For each DBField or label, set the exact coordinate using the properties Column Index and Row Index.

     For example, set the properties Column Index=0 and Row Index=2 for a DBField, Logi JReport Designer will put this DBField into the first column and the third row in the generated Text file.
  3. Set the property **engine.single\_thread=false** in the file server.propertise in `<server_install_root>\bin`. This enables the property Fast Pass to take effect when running the report to the Delimited Format.
* Cache Section.

  The Cache Section property is used to cache the objects in the detail panel of a banded object instead of creating them repeatedly. You can set Cache Section in the Report Inspector to true to improve the performance.

  **Note:** Cache Section doesn't work if there is crosstab, text object, chart, and so on in the detail panel of the banded object, because these objects contain child-DBFields.
* Cache Value (only for DBFields).

  The Cache Value property is used to cache the layout attributes (font size, font face, width and so on) of DBFields when exporting the report to any format. To get better performance, set it to true in the Report Inspector.
* [Push Down Group Query](https://devnet.logianalytics.com/hc/en-us/articles/1500009590441-JDBC-HIVE-Connection-Properties#PushDown).

  The Push Down Group Query property controls whether to push down group level summary computations in reports to the DBMS at runtime. By pushing down the computations, the DBMS' computation capability can be made use of, and thus the reports' running efficiency will be improved.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592941-Managing-Report-Tabs-in-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571042-Saving-a-Page-Report)
