---
title: "Working with Library Components"
id: 1500009562462
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562462-Working-with-Library-Components
updated_at: 2021-07-24T05:56:18Z
---

# Working with Library Components

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582821-Exiting-from-the-Editing-Status)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562402-Design-API-Samples)

# Working with Library Components

The entry API for working with library components is getLCEditor(). All the following operations use it as the entry:

* **createLC(String titleText)**  
   Creates a new library component.
* **addDataset(String name, String datasourceName, String BVName)**  
   Creates a new dataset from a business view.
* **setDataset(String objHandle, String datasetHandle)**  
   Applies an existing dataset used in the library component to the data component. It returns true if the dataset is bound to the data component successfully; otherwise false.
* **insertTable(TableTemplateInfo info, boolean increasePanel)**  
   Inserts a new table into the library component.
* **insertChart(ChartInfo info, String datasetName)**  
   Inserts a new chart into the library component.
* **insertCrossTab(CrossTabInfo info)**  
   Inserts a new crosstab into the library component.
* **insertImage(String imageName)**  
   Inserts an image into the library component. The image must be in the same folder as the catalog.
* **insertLabel(String text)**  
   Inserts a label into the library component.
* **insertSpecialField(int fieldType)**  
   Inserts a special field into the library component.
* **saveLC(String lcFileName)**  
   Saves the library component into the specified file (.lc).
* **loadLC(String lcFileName)**  
  Loads the library component from the specified file (.lc).
* **close(String handle)**  
   Closes the specified library component and clears all resources of the library component. It returns true if the library component is closed successfully; otherwise false.
* **quit()**  
  Quits from the library component editor and clears all resources of the editor.

**Parameters**

* titleText - The title of the library component to be created.
* name - The dataset's instance name.
* datasourceName - The name of the data source that the required query belongs to.
* BVName - The name of the business view that the dataset is based on.
* objHandle - The handler string of the data component.
* datasetHandle - The handler string of the existing dataset.
* info - The class that defines the information of the table, chart, or crosstab, such as its data, properties, columns, rows, groups, aggregations, and their properties.
* increasePanel - Indicates whether to increase the bounds when the table is out of the panel bounds. If it is true, the page width will be increased according to the table's width and position. If false, the table and its columns' width will be adjusted to fit the page.
* datasetName - The dataset's instance name.
* imageName - The name of the image to be inserted.
* text - The text of the label to be inserted.
* fieldType - The int value of the field type. The constants can be:
  + USERNAME
  + PRINTDATE
  + PRINTTIME
  + FETCHDATE
  + FETCHTIME
  + MODIFIEDDATE
  + MODIFIEDTIME
  + RECORDNUMBER
  + GROUPNAME
  + GROUPNUMBER
  + GROUPNUMBERS
  + PAGENUMBER
  + PAGENUMBERS
  + SQLSTATMENT
* lcFileName - The library component file name (.lc) with full path.
* handle - The handle of the library component object.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582821-Exiting-from-the-Editing-Status)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562402-Design-API-Samples)
