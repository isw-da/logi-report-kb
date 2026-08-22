---
title: "Insert Filter Control"
id: 1500009687562
section: "Page Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009687562-Insert-Filter-Control
updated_at: 2021-11-03T06:58:06Z
---

# Insert Filter Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009687542-Insert-Detail-Column)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009687582-Insert-Group-Column)

# Insert Filter Control

The Insert Filter Control dialog helps you to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls#Filter) into a report for filtering data components in the report (excluding its subreport).

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131419159/insrtfltrctrl.gif)

**Control Type**

A text list filter control can be inserted in a report. A filter control in this type allows you to select one or more values to define a filter condition.

**Select Fields**

Specifies the fields to bind to the filter control from the drop-down list. All the selected fields should be of the same data type. The uncomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

The common usage is to select one field, and then based on the field to filter the data of the components created on the same data source as the selected field.

To filter components using different data sources, choose a common field all the data sources contain and select the field in all the data sources one by one.

**Customize Initial Values**

By default all values of the selected fields will be used in the filter control. You can check the option to customize the value list.

* **Fetch Data**  
   Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009687502-Fetch-Data) dialog to select values from the database and adds the selected values to the text box below.
* **Text box**  
  You can type in values directly in the text box. Make sure the accuracy of their formats and values.

  The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete and etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user-defined value list.

  When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
* ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif)  
   Specifies a Date/Time value in the text box.

**Link to Other Filters**

Specifies whether the filter control can be affected by other filter controls which are applied to the same data components as the filter control. In the case when one filter control is based on a business view and another a query, if the business view contains the query definition, the two filter controls are also interlinked.

**Apply To**

Specifies the components to which the filter created with the filter control will be applied.

**OK**

Inserts a filter control into the report and closes the dialog.

**Cancel**

Cancels the operation and closes the dialog.

**Help**

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009687542-Insert-Detail-Column)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009687582-Insert-Group-Column)
