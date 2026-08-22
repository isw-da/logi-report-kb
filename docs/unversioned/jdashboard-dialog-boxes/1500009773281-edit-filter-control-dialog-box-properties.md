---
title: "Edit Filter Control Dialog Box Properties"
id: 1500009773281
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773281-Edit-Filter-Control-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:00Z
---

# Edit Filter Control Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773241-Customize-Component-Title-Bar-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745382-Edit-HTML-Dialog-Box-Properties)

# Edit Filter Control Dialog Box Properties

You can use the Edit Filter Control dialog box to [edit the filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009743862-Filtering-the-Data-Components-in-a-Dashboard#Insert). This topic describes the options in the dialog box.

JDashboard displays the dialog box after you select ![](https://devnet.logianalytics.com/hc/article_attachments/4404880135063/btn_dshbrd_more.gif) on the title bar of a filter control and then select Edit Setting from the drop-down menu.

![Edit Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885535895/edtfltrctrl.gif)

**Title**

Specifies the title of the filter control.

**Control Type**

Specifies the [type](https://devnet.logianalytics.com/hc/en-us/articles/1500009743862-Filtering-the-Data-Components-in-a-Dashboard#Type) of the filter control.

**Select Fields**

Specifies the fields to bind to the filter control. All the selected fields should be of the same data type. The uncomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

**Customize Initial Values**

Specifies to customize the value list of the filter control.

The customization UI is different according to control types:

* **For Text List, Drop-down List or Single Value Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4404880448151/dshbrd_fltr_cstmz.gif)
  + **Fetch Data**  
     Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009773401-Fetch-Data-Dialog-Box-Properties) dialog box to select values from the database and adds the selected values to the text box below.
  + **Text box**  
    You can type values directly in the text box. Make sure the accuracy of their formats and values.

    The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete, etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user defined value list.

    When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
  + ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif)**Calendar icon**  
    Opens the calendar to specify a Date/Time value.
* **For Range Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4404880448663/dshbrd_fltr_rngcus.gif)
  + **From**  
    Select the start value of the slider from the drop-down list or type the value in the text box.
  + **To**  
     Select the end value of the slider from the drop-down list or type the value in the text box.
  + ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif)**Calendar icon**  
    Opens the calendar to specify a Date/Time value.

**Link to Other Filters**

Specifies whether the filter control can be affected by other filter controls that apply to the same data components as the filter control.

**Special Function**

Specifies a special function for the selected fields if they are of the Date/Time type. Available only to the slider control types.

**Apply To**

Specifies the data components from the drop-down list to apply the filter control to. <All> means all data components involving the selected fields in the dashboard.

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Cancels the editing and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773241-Customize-Component-Title-Bar-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745382-Edit-HTML-Dialog-Box-Properties)
