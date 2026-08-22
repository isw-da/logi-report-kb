---
title: "Insert Filter Control"
id: 1500009714141
section: "JDashboard Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009714141-Insert-Filter-Control
updated_at: 2021-11-03T06:57:53Z
---

# Insert Filter Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714121-Incremental-Condition)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714161-Insert-HTML)

# Insert Filter Control

The Insert Filter Control dialog helps you to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009712581-Filtering-the-Data-Components-in-a-Dashboard) into the dashboard body to filter component data. This dialog appears when you drag Filter Control from Toolbox in the Resources panel to the dashboard body.

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131482903/insrtfltrctrl.gif)

**Title**

Specifies the title of the filter control.

**Control Type**

Specifies the [type](https://devnet.logianalytics.com/hc/en-us/articles/1500009712581-Filtering-the-Data-Components-in-a-Dashboard#Type) of the filter control.

**Select Fields**

Specifies the fields to bind to the filter control. All the selected fields should be of the same data type. The uncomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary and Varbinary.

**Customize Initial Values**

Specifies to customize the value list of the filter control.

The customization UI is different according to control types:

* **For Text List, Drop-down List or Single Value Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4412131483415/dshbrd_fltr_cstmz.gif)
  + **Fetch Data**  
     Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009688262-Fetch-Data) dialog to select values from the database and adds the selected values to the text box below.
  + **Text box**  
     You can type in values directly in the text box. Make sure the accuracy of their formats and values.

    The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete and etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user-defined value list.

    When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif)  
     Specifies a Date/Time value using the calendar.
* **For Range Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4412139572887/dshbrd_fltr_rngcus.gif)
  + **From**  
     Select the start value of the slider from the drop-down list or type the value in the text box. For Date/Time type fields, you can also select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) to specify a value using the calendar.
  + **To**  
     Select the end value of the slider from the drop-down list or type the value in the text box. For Date/Time type fields, you can also select ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif) to specify a value using the calendar.

**Link to Other Filters**

Specifies whether the filter control can be affected by other filter controls that apply to the same data components as the filter control.

**Special Function**

Specifies a special function for the selected fields if they are of the Date/Time type. Available only to the slider control types.

**Apply To**

Specifies the data components from the drop-down list to apply the filter control to. <All> means all data components involving the selected fields in the dashboard.

**OK**

Closes this dialog and inserts the filter control in the dashboard body.

**Cancel**

Cancels the insertion and closes this dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714121-Incremental-Condition)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714161-Insert-HTML)
