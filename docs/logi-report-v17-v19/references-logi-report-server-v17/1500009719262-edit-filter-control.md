---
title: "Edit Filter Control"
id: 1500009719262
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009719262-Edit-Filter-Control
updated_at: 2021-07-25T07:20:08Z
---

# Edit Filter Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719242-Edit-Conditions)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719282-Encoding)

# Edit Filter Control

The Edit Filter Control dialog box is used to [edit a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009750541-Applying-Web-Controls#Filter) in a report.

![Edit Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942598807/edtfltrctrl.gif)

**Control Type**

A text list filter control can be inserted in a report. A filter control in this type allows you to select one or more values to define a filter condition.

**Select Fields**

Specifies the fields to bind to the filter control from the drop-down list. All the selected fields should be of the same data type. The uncomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

The common usage is to select one field, and then based on the field to filter the data of the components created on the same data source as the selected field.

To filter components using different data sources, choose a common field all the data sources contain and select the field in all the data sources one by one.

**Customize Initial Values**

By default all values of the selected fields will be used in the filter control. You can select this option to customize the value list.

* **Fetch Data**  
   Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009719502-Fetch-Data) dialog box to select values from the database and adds the selected values to the text box below.
* **Text box**  
   You can type values directly in the text box. Make sure the accuracy of their formats and values.

  The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete and etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user defined value list.

  When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif)  
   Specifies a Date/Time value in the text box.

**Link to Other Filters**

Specifies whether the filter control can be affected by other on-screen filters that apply to the same data components as the filter control. For the case of one filter using a business view and another using a query, if the business view contains the query definition, the two filters are also linked.

Here other filters include all the other on-screen filters that are applied to the data components which the filter control is applied to.

* **Example of other filters** 

  When:

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

Specifies the components to which the filter created with the filter control will be applied.

**OK**

Inserts a filter control into the report and closes the dialog box.

**Cancel**

Cancels the operation and closes the dialog box.

**Help**

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719242-Edit-Conditions)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719282-Encoding)
