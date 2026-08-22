---
title: "Insert Fields Dialog"
id: 1500009587581
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009587581-Insert-Fields-Dialog
updated_at: 2021-07-24T05:55:07Z
---

# Insert Fields Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566442-Insert-Detail-Column-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587601-Insert-Filter-Control-Dialog-for-Library-Component-)

# Insert Fields Dialog

The Insert Fields dialog appears when you select Insert > DBField/Formula/Parameter, or the button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the Value column of the Display Type dialog when the display type is defined as List or Drop-down List, or the button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the Value column of the [Web Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009567902-Web-Options-Dialog) dialog when defining the web options of a list or drop-down list in the configuration panel of a library component. It helps you to insert fields into a report, or to add fields to control values of the list/drop-down list item. [See the dialog](javascript:%20void(null)).

![Insert Fields dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893874583/instfld.gif)

The following are details about options in the dialog.

**DBField List**

Specifies to insert a field.

* **Dataset**  
   This node is automatically expanded when inserting a DBField. It lists the tables and fields from the current dataset. If you want to insert DBField from another dataset, select the dataset from the dataset drop-down list. You can also select the <Choose Data From...> item from the dataset drop-down list to create a new dataset.
* **Formulas**  
   This node is automatically expanded when inserting a formula field. It lists all the formulas in the current catalog. You can also select the <New Formula...> item to create one.

* **Parameters**  
   This node is automatically expanded when inserting a parameter field. It lists all the parameters in the current catalog. You can also select the <New Parameter...> item to create one.
* **Dynamic Resources**  
   This node is available only when you are defining values for a list or drop-down list in a library component. It lists all the dynamic formulas in the current library component. You can also select the <New Formula...> item to create one.

**All**

This radio button is available only when the dialog is opened from the Display Type dialog or Web Options dialog. You can check it to add an All value to the list/drop-down list.

**Insert Layout**

When multiple fields are selected, you can arrange these objects horizontally or vertically by selecting Horizontal or Vertical, or by selecting the Default radio button to set it with the default layout.

* **Vertical Space**  
   Specifies the space between fields that are arranged vertically.
* **Horizontal Space**  
   Specifies the space between fields that are arranged horizontally.

**Insert**

Inserts the selected fields into the specified location in the report.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566442-Insert-Detail-Column-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587601-Insert-Filter-Control-Dialog-for-Library-Component-)
