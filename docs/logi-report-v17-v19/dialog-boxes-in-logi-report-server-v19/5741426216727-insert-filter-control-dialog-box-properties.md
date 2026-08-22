---
title: "Insert Filter Control Dialog Box Properties"
id: 5741426216727
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741426216727-Insert-Filter-Control-Dialog-Box-Properties
updated_at: 2022-10-31T17:16:43Z
---

# Insert Filter Control Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741419595031-Incremental-Condition-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741432184471-Insert-HTML-Dialog-Box-Properties)

# Insert Filter Control Dialog Box Properties

You can use the Insert Filter Control dialog box to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/5741416414103-Filtering-the-Data-Components-in-a-Dashboard) into the dashboard body to filter component data. This topic describes the properties in the dialog box.

Server displays the dialog box when you drag **Filter Control** from Toolbox in the Resources panel to the dashboard body.

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/9905760285463/insrtfltrctrl.gif)

**Title**

Specify the title of the filter control.

**Control Type**

Select the [type](https://devnet.logianalytics.com/hc/en-us/articles/5741416414103-Filtering-the-Data-Components-in-a-Dashboard#Type) of the filter control.

**Select Fields**

Select the fields you want to bind to the filter control. All the selected fields should be of the same data type. You cannot bind uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

**Customize Initial Values**

By default, Server applies all the values of the selected fields in the filter control. Select **Customize Initial Values** if you want to customize the value list.

The customization UI varies with control types:

* **For Text List, Drop-down List, or Single Value Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/9905771961623/dshbrd_fltr_cstmz.gif)
  + **Fetch Data**  
    Select to open the [Fetch Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741412875287-Fetch-Data-Dialog-Box-Properties) to select values from the database. Server adds the selected values to the value box.
  + **Value box**  
    You can type values directly here. Make sure the accuracy of their formats and values.

    The value box is an editable multi-row plain text box. It supports general text editing operations such as copy, paste, cut, backspace, and delete. Press Enter to start a new row. Each row is a value of the user defined value list.

    When you have selected **Customize Initial Values** but do not provide any values in the value box, Server will add all the values of the selected fields in the filter control.
  + ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/9905617212951/btn_clndr.gif)**Calendar icon**  
    Select to open the calendar to specify a Date/Time value.
* **For Range Slider**  
  ![Customize Initial Values](https://devnet.logianalytics.com/hc/article_attachments/9905771994007/dshbrd_fltr_rngcus.gif)
  + **From**  
     Select the start value of the slider from the drop-down list.
  + **To**  
     Select the end value of the slider from the drop-down list.
  + ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/9905617212951/btn_clndr.gif)**Calendar icon**  
    Select to open the calendar to specify a Date/Time value.

**Link to Other Filters**

Clear if you don't want the filter control to be affected by other filter controls that apply to the same data components as the filter control.

**Special Function**

Select a special function for the selected fields if they are of the Date/Time type. Available only to the slider control types.

**Apply To**

Select the components which you want the filter control to filter. **<All>** means all the data components involving the selected fields in the dashboard.

**OK**

Select to insert the filter control in the dashboard body.

**Cancel**

Select to close the dialog box without the insertion.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without the insertion.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741419595031-Incremental-Condition-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741432184471-Insert-HTML-Dialog-Box-Properties)
