---
title: "Insert Filter Control Dialog Box Properties"
id: 1500009772641
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772641-Insert-Filter-Control-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:09Z
---

# Insert Filter Control Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772601-Insert-Detail-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744682-Insert-Group-Column-Dialog-Box-Properties)

# Insert Filter Control Dialog Box Properties

You can use the Insert Filter Control dialog box to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009749062-Applying-Web-Controls-in-Page-Report#Filter) into a report for filtering data components in the report (excluding its subreport). This topic describes the options in the dialog box.

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880249367/insrtfltrctrl.gif)

**Control Type**

Specifies [the type of the filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009743862-Filtering-the-Data-Components-in-a-Dashboard).

**Select Fields**

Specifies the fields to bind to the filter control from the drop-down list. All the selected fields should be of the same data type. You cannot bind the uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

The common usage is to select one field, and then based on the field to filter the data of the components created on the same data source as the selected field.

To filter components using different data sources, choose a common field all the data sources contain and select the field in all the data sources one by one.

**Customize Initial Values**

By default, Server applies all the values of the selected fields in the filter control. You can select this option to customize the value list.

* **Fetch Data**  
   Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009744582-Fetch-Data-Dialog-Box-Properties) dialog box to select values from the database and adds the selected values to the text box below.
* **Text box**  
  You can type values directly in the text box. Make sure the accuracy of their formats and values.

  The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete, etc. You can press the Enter key on the keyboard to start a new row. Each row is a value of the user defined value list.

  When you have selected **Customize Initial Values** but the text box is empty, Server will apply all the values of the selected fields in the filter control.
* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif)  
   Specifies a Date/Time value in the text box.

**Link to Other Filters**

Specifies whether other on-screen filters that apply to the same data components as the filter control can affect the filter control. In the case when one filter control is based on a business view and another a query, if the business view contains the query definition, Server also interlinks the two filter controls.

**Apply To**

Specifies the components to which you want to apply the filter created with the filter control.

**OK**

Inserts a filter control into the report and closes the dialog box.

**Cancel**

Cancels the operation and closes the dialog box.

**Help**

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009772601-Insert-Detail-Column-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744682-Insert-Group-Column-Dialog-Box-Properties)
