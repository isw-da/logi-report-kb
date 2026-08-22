---
title: "Inserting, Moving, and Deleting an Object"
id: 1500009562442
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562442-Inserting-Moving-and-Deleting-an-Object
updated_at: 2021-07-24T05:56:19Z
---

# Inserting, Moving, and Deleting an Object

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582861-Opening-and-Closing-a-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562502-Getting-Property-Information)

# Inserting, Moving, and Deleting an Object

To insert an object in a report, you can use the methods below:

* **insert(String parent, int type, String name)**  
   Inserts an object into the parent node.
* **insert(String parent, int type, String name, String mapping)**  
   Inserts a DBField, parameter, formula or summary into the parent node.
* **insertTable(String parent, TableTemplateInfo info, boolean increasePanel)**  
  Inserts a table into the parent node.
* **insert(String parent, String name, CTRowColFieldInfo colInfo[], CTRowColFieldInfo rowInfo[], CTAggFieldInfo aggInfo[])**  
   Insert a crosstab object and its children into the parent node.
* **insert(String parent, CTRowColFieldInfo colInfo, CTRowColFieldInfo rowInfo, CTAggFieldInfo aggInfo)**   
   Inserts crosstab children into the crosstab.
* **insert(String parent, String name, String paperName, int charttype, String gName1, String gName2, String value, ChartLegendInfo chartLegendInfo, ChartLabelInfo chartLabelInfo)**  
   Inserts a chart object and its children into the parent node.
* **insert (String parent, int type, String name, String topSection , String bottomSection)**   
   Inserts a shape object into the report and returns the handle of the new shape.
* **insert(String parent, String name, GroupInfo groupInfo)**  
   Inserts a group/sort into the parent node.

To change the position of an object, use the following method:

* **public boolean changeZOrder(String objectHandle,
  int zorderType)**  
   Moves an object to front/back, or forward/backward

To delete an object from a report, use the following method:

* **delete(String handle)**  
  Deletes an object from its parent node.

**Parameters**

* parent - Parent handle node.
* type - Class type that you want to insert.
* name - Instance name of the new object.
* mapping - Mapping name of the database field, parameter, formula or summary.
* info - The table information including the information of the data, group, or columns in the table.
* increasePanel - Indicates whether to increase the bounds when the table is out of the panel bounds. If it is true, the page width will be increased according to the table's width and position. If it is false, the table and its columns' width will be adjusted to fit the page.
* colInfo - Field information array of the column.
* rowInfo - Field information array of the row.
* aggInfo - Field information array of the aggregate.
* paperName - Instance name of ChartCoordinatepaper object.
* charttype - Type of the chart.
* group1 - Mapping name of the first group.
* group2- Mapping name of the second group. It can be null.
* value - Mapping name of a summary.
* chartLegendInfo - Field information array of the chart legend.
* chartLabelInfo - Field information array of the chart title and notes.
* topSection - Handle of the top section attached by the shape.
* bottomSection - Handle of the bottom section attached by the shape.
* groupInfo - The group information.
* objectHandle - Handle of the object whose z-order will be moved.
* zorderType - Direction to which the object will be moved.
* handle - Handle of the object that is to be deleted.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582861-Opening-and-Closing-a-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562502-Getting-Property-Information)
