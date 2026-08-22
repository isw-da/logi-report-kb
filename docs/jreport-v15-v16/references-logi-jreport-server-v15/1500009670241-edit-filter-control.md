---
title: "Edit Filter Control"
id: 1500009670241
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009670241-Edit-Filter-Control
updated_at: 2021-07-24T20:54:58Z
---

# Edit Filter Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645942-Customize-Component-Title-Bar)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009670261-Edit-HTML)

# Edit Filter Control

The Edit Filter Control dialog appears after you select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the title bar of a filter control and then select Edit Setting. It helps you to edit the filter control. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404926758167/edtfltrctrl.gif)

**Title**

Specifies the title of the filter control.

**Control Type**

Select a [type](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data#Type) from the drop-down list.

**Select Fields**

Specifies the fields to bind to the filter control from the drop-down list. All the selected fields should be of the same data type. The uncomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

The common usage is to select one field, and then based on the field to filter the data of the components created on the same data source as the selected field.

To filter components using different data sources, choose a common field all the data sources contain and select the field in all the data sources one by one.

**Customize Initial Values**

By default all values of the selected fields will be used in the filter control. You can check the option to customize the value list.

The customization UI is different according to control types:

* **For Text List and Single Value Slider**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920591511/instfltrctrl_txt.gif)

  + **Fetch Data**  
     Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009646082-Fetch-Data) dialog to select values from the database and adds the selected values to the text box below.
  + **Text box**  
     You can type in values directly in the text box. Make sure the accuracy of their formats and values.

    The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete and etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user-defined value list.

    When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
  + ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif)  
     Specifies a Date/Time value in the text box.
  + **Special Function**  
     Specifies a special function for the selected fields. Available to Single Value Slider only when the selected fields are of Date/Time type.

    | **Special Function** | Description |
    | --- | --- |
    | None | All the records that have the same field value will be displayed together as a group. |
    | For each day | The records, of which the field values are in the same day, will be grouped together. |
    | For each week | The records, of which the field values are in the same week, will be grouped together. |
    | For each bi-week | The records, of which the field values are in the same bi-week, will be grouped together. |
    | For each half month | The records, of which the field values are in the same half month, will be grouped together. |
    | For each month | The records, of which the field values are in the same month, will be grouped together. |
    | For each quarter | The records, of which the field values are in the same quarter, will be grouped together. |
    | For each half year | The records, of which the field values are in the same half year, will be grouped together. |
    | For each year | The records, of which the field values are in the same year, will be grouped together. |
* **For Range Slider**

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920592151/instfltrctrl_rng.gif)

  + **From**  
     Select the start value of the slider from the drop-down list or type the value in the text box. For the Date/Time type, you can also select the ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif) button to specify a value.
  + **To**  
     Select the end value of the slider from the drop-down list or type the value in the text box. For the Date/Time type, you can also select the ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif) button to specify a value.
  + **Special Function**Specifies a special function for the selected fields. Available only when the selected fields are of Date/Time type.

**Link to Other Filters**

Specifies whether the filter control can be affected by other on-screen filters that apply to the same data components and that contain the same data type of fields from the same business view or query as the filter control. For the case of one filter using a business view and another using a query, if the business view contains the query definition, the two filters are also linked.

Here other filters include all the other on-screen filters that are applied to the data components which the filter control is applied to.

* **Example of other filters** 

  When

  + Filter1 is applied to DC1, DC2, and DC3.
  + Filter2 is applied to DC1.
  + Filter3 is applied To DC2.
  + Filter4 is applied to DC2 and DC3.

  The result:

  + For Filter1, other filters are Filter2, Filter3, and Filter4.
  + For Filter2, other filter is Filter1.
  + For Filter3, other filters are Filter1 and Filter4.
  + For Filter4, other filters are Filter1 and Filter3.
* **Example of different behaviors when Link to Other Filters is set to true and false**

  There are three filter controls and they all apply to a table:

  + FC\_Country contains the Country field and Link to Other Filters is true.
  + FC\_City contains the City field and Link to Other Filters is true.
  + FC\_City1 contains the City field and Link to Other Filters is false.

  When you select USA in FC\_Country, the cities that do not belong to USA will be grayed in FC\_City while FC\_City1 is not affected.

**Apply To**

Specifies the data components from the drop-down list to apply the filter control to. <All> means all data components involving the selected fields in the dashboard.

**OK**

Closes this dialog and applies the changes to the filter control.

**Cancel**

Cancels the editing and closes this dialog.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920501783/btn_help.gif)

Displays the help document about this feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926700311/btn_close.gif)

Ignores the setting and closes this dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009645942-Customize-Component-Title-Bar)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009670261-Edit-HTML)
