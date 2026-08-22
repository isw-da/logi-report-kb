---
title: "Insert Filter Control Dialog Box Properties"
id: 1500009773461
section: "JDashboard Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773461-Insert-Filter-Control-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:56Z
---

# Insert Filter Control Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773441-Incremental-Condition-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745502-Insert-HTML-Dialog-Box-Properties)

# Insert Filter Control Dialog Box Properties

Use the Insert Filter Control dialog box to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009743862-Filtering-the-Data-Components-in-a-Dashboard) into the dashboard body to filter component data. This topic describes how to define a filter control.

JDashboard displays the dialog box when you drag Filter Control from Toolbox in the Resources panel to the dashboard body.

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880447639/insrtfltrctrl.gif)

**Title**

Title of the filter control.

**Control Type**

[Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009743862-Filtering-the-Data-Components-in-a-Dashboard#Type) of the filter control.

**Select Fields**

Select the fields to bind to the filter control. All the selected fields should be of the same data type. You cannot bind the uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

**Customize Initial Values**

Customize the value list of the filter control.

The customization UI is different according to control types:

* **For Text List, Drop-down List, or Single Value Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4404880448151/dshbrd_fltr_cstmz.gif)
  + **Fetch Data**  
    Select **Fetch Data** to open the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009773401-Fetch-Data-Dialog-Box-Properties) dialog box to select values from the database and add the selected values to the text box below.
  + **Text box**  
    You can type values directly in the text box. Make sure the accuracy of their formats and values.

    The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete, etc. Press Enter to start a new row. Each row is a value of the user defined value list.

    When you have selected **Customize Initial Values** but do not provide any values in the text box, JDashboard will add all the values of the selected fields in the filter control.
  + ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif)**Calendar icon**  
    Select this icon to open the Calendar to specify a Date/Time value.
* **For Range Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/4404880448663/dshbrd_fltr_rngcus.gif)
  + **From**  
     Select the start value of the slider from the drop-down list or type the value in the text box.
  + **To**  
     Select the end value of the slider from the drop-down list or type the value in the text box.
  + ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif)**Calendar icon**  
    Select this icon to open the calendar to specify a Date/Time value.

**Link to Other Filters**

Clear this option if you do not want the filter control to be affected by other filter controls that apply to the same data components as the filter control.

**Special Function**

Select a special function for the selected fields if they are of the Date/Time type. Available only to the slider control types.

**Apply To**

Select the data components from the drop-down list to apply the filter control to. **<All>** means all the data components involving the selected fields in the dashboard.

**OK**

Select **OK** to insert the filter control in the dashboard body.

**Cancel**

Select **Cancel** to close the dialog box without the insertion.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select this button to view information about the Insert Filter Control dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select this button to close the dialog box without the insertion.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773441-Incremental-Condition-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745502-Insert-HTML-Dialog-Box-Properties)
