---
title: "Insert Filter Control"
id: 1500009720182
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009720182-Insert-Filter-Control
updated_at: 2021-07-25T07:19:49Z
---

# Insert Filter Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720162-Incremental-Condition)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746881-Insert-HTML)

# Insert Filter Control

The Insert Filter Control dialog box is used to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009745061-Filtering-the-Data-Components-in-a-Dashboard) into the dashboard body to filter component data. It appears when you drag Filter Control from Toolbox in the Resources panel to the dashboard body.

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936897943/insrtfltrctrl.gif)

**Title**

Specifies the title of the filter control.

**Control Type**

Specifies the [type](https://devnet.logianalytics.com/hc/en-us/articles/1500009745061-Filtering-the-Data-Components-in-a-Dashboard#Type) of the filter control.

**Select Fields**

Specifies the fields to bind to the filter control. All the selected fields should be of the same data type. The uncomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary and Varbinary.

**Customize Initial Values**

Specifies to customize the value list of the filter control.

The customization UI is different according to control types:

* **For Text List, Drop-down List or Single Value Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4404936898199/dshbrd_fltr_cstmz.gif)
  + **Fetch Data**  
    Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009720122-Fetch-Data) dialog box to select values from the database and adds the selected values to the text box below.
  + **Text box**  
    You can type values directly in the text box. Make sure the accuracy of their formats and values.

    The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete and etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user defined value list.

    When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
  + ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif)**Calendar icon**  
    Opens the calendar to specify a Date/Time value.
* **For Range Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4404936898583/dshbrd_fltr_rngcus.gif)
  + **From**  
     Select the start value of the slider from the drop-down list or type the value in the text box.
  + **To**  
     Select the end value of the slider from the drop-down list or type the value in the text box.
  + ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif)**Calendar icon**  
    Opens the calendar to specify a Date/Time value.

**Link to Other Filters**

Specifies whether the filter control can be affected by other filter controls that apply to the same data components as the filter control.

**Special Function**

Specifies a special function for the selected fields if they are of the Date/Time type. Available only to the slider control types.

**Apply To**

Specifies the data components from the drop-down list to apply the filter control to. <All> means all data components involving the selected fields in the dashboard.

**OK**

Closes this dialog box and inserts the filter control in the dashboard body.

**Cancel**

Cancels the insertion and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720162-Incremental-Condition)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746881-Insert-HTML)
