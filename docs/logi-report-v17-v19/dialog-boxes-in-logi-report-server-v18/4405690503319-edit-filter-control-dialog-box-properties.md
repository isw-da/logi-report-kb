---
title: "Edit Filter Control Dialog Box Properties"
id: 4405690503319
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690503319-Edit-Filter-Control-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:37Z
---

# Edit Filter Control Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683623447-Edit-Conditions-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683624599-Encoding-Dialog-Box-Properties)

# Edit Filter Control Dialog Box Properties

You can use the Edit Filter Control dialog box to [edit a filter control](https://devnet.logianalytics.com/hc/en-us/articles/4405683962775-Applying-Web-Controls-in-Page-Report#Filter) in a report. This topic describes the properties in the dialog box.

![Edit Filter Control dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420461713047/edtfltrctrl.gif)

**Control Type**

You can only select **Text List** as [the type of the filter control](https://devnet.logianalytics.com/hc/en-us/articles/4405690494487-Filtering-the-Data-Components-in-a-Dashboard).

**Select Fields**

Select the fields you want to bind to the filter control from the list. All the selected fields should be of the same data type. You cannot bind the uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

The common usage is to select one field, and then based on the field to filter the data of the components that use the same data source as the selected field.

To filter components using different data sources, choose a common field all the data sources contain and select the field in all the data sources one by one.

**Customize Initial Values**

By default, Server applies all the values of the selected fields in the filter control. You can select this property to customize the value list.

* **Fetch Data**  
   Select to open the [Fetch Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690507927-Fetch-Data-Dialog-Box-Properties) to select values from the database. Server adds the selected values to the value box.
* **Value box**  
   You can type values directly here. Make sure the accuracy of their formats and values.

  The value box is an editable multi-row plain text box. It supports general text editing operations such as copy, paste, cut, backspace, and delete. Press Enter to start a new row. Each row is a value of the user defined value list.

  When you have selected **Customize Initial Values** but do not provide any values in the value box, Server will add all the values of the selected fields in the filter control.
* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463447/btn_clndr.gif)**Calendar icon**  
   Select to open the calendar to specify a Date/Time value.

**Link to Other Filters**

Clear if you don't want the filter control to be affected by other filter controls that apply to the same data components as the filter control.

In the case of one filter using a business view and another using a query, if the business view contains the query definition, Server also interlinks the two filter controls.

* **Example of other filters** 

  When:

  + You applied Filter1 to DC1, DC2, and DC3.
  + You applied Filter2 to DC1.
  + You applied Filter3 to DC2.
  + You applied Filter4 to DC2 and DC3.

  The result:

  + For Filter1, other filters are Filter2, Filter3, and Filter4.
  + For Filter2, other filter is Filter1.
  + For Filter3, other filters are Filter1 and Filter4.
  + For Filter4, other filters are Filter1 and Filter3.
* **Example of different behaviors when Link to Other Filters is true and false**

  There are three filter controls, and they all apply to a table:

  + FilterControl\_Country contains the Country field and Link to Other Filters is true.
  + FilterControl\_City contains the City field and Link to Other Filters is true.
  + FilterControl\_City1 contains the City field and Link to Other Filters is false.

  When you select USA in FilterControl\_Country, Server grays the cities that do not belong to USA in FilterControl\_City, but does not affect FilterControl\_City1.

**Apply To**

Select the components which you want the filter control to filter. **<All>** means all the data components involving the selected fields in the dashboard.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683623447-Edit-Conditions-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683624599-Encoding-Dialog-Box-Properties)
