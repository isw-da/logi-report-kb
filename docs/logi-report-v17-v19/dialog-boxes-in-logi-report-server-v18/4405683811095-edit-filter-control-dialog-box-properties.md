---
title: "Edit Filter Control Dialog Box Properties"
id: 4405683811095
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683811095-Edit-Filter-Control-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:15Z
---

# Edit Filter Control Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683810071-Edit-Detail-Table-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683812119-Edit-Image-Dialog-Box-Properties)

# Edit Filter Control Dialog Box Properties

You can use the Edit Filter Control dialog box to [edit a filter control](https://devnet.logianalytics.com/hc/en-us/articles/4405684046615-Using-Web-Controls-in-Web-Report#Filter). This topic describes the properties in the dialog box.

Server displays the dialog box when you right-click a filter control and then select **Edit**, or when you select the ellipsis button ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4420453393175/btn_chsr2.gif) beside the **Filter On** text box on the General tab of the [Filter Control Properties dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690580759-Filter-Control-Properties).

![Edit Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4420461654935/edtfltrctrl.gif)

**Control Type**

Select the [type](https://devnet.logianalytics.com/hc/en-us/articles/4405690494487-Filtering-the-Data-Components-in-a-Dashboard#Type) of the filter control.

**Select Fields**

Select the fields you want to bind to the filter control. All the selected fields should be of the same data type. You cannot bind uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

**Customize Initial Values**

By default, Server applies all the values of the selected fields in the filter control. Select **Customize Initial Values** if you want to customize the value list.

* **Fetch Data**  
   Select to open the [Fetch Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405690589847-Fetch-Data-Dialog-Box-Properties) to select values from the database and adds the selected values to the text box.
* **Text box**  
   You can type values directly here. Make sure the accuracy of their formats and values.

  The value box is an editable multi-row plain text box. It supports general text editing operations such as copy, paste, cut, backspace, and delete. Press Enter to start a new row. Each row is a value of the user defined value list.

  When you have selected **Customize Initial Values** but do not provide any values in the value box, Server will add all the values of the selected fields in the filter control.
* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4420461463447/btn_clndr.gif)**Calendar icon**  
   Select to open the calendar to specify a Date/Time value.

**Link to Other Filters**

Clear if you don't want the filter control to be affected by other filter controls that apply to the same data components as the filter control.

**Apply To**

Select the components which you want the filter control to filter. **<All>** means all the data components involving the selected fields in the dashboard.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683810071-Edit-Detail-Table-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683812119-Edit-Image-Dialog-Box-Properties)
