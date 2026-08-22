---
title: "Insert Filter Control Dialog Box Properties"
id: 1500009775981
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775981-Insert-Filter-Control-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:18Z
---

# Insert Filter Control Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747602-Insert-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747622-Insert-Image-Dialog-Box-Properties)

# Insert Filter Control Dialog Box Properties

This topic describes how you can use the Insert Filter Control dialog box to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009750222-Using-Web-Controls-in-Web-Report#Filter) to a report for filtering data components in the report. Server displays the dialog box when you drag **Filter Control** from the **Components** panel to a report.

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880144407/insrtfltrctrl.gif)

**Control Type**

Specifies the type of the filter control.

**Select Fields**

Specifies the fields to bind to the filter control. All the selected fields should be of the same data type. The incomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

**Customize Initial Values**

Specifies to customize the value list of the filter control.

* **Fetch Data**  
   Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009747542-Fetch-Data-Dialog-Box-Properties) dialog box to select values from the database and adds the selected values to the text box below.
* **Text box**  
   You can type values directly in the text box. Make sure the accuracy of their formats and values.

  The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete, etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user defined value list.

  When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif)  
   Specifies a Date/Time value in the text box.

**Link to Other Filters**

Specifies whether the filter control can be affected by other on-screen filters that apply to the same data components as the filter control.

**Apply To**

Specifies the components to which the filter created with the filter control will be applied.

**OK**

Inserts a filter control into the report and closes the dialog box.

**Cancel**

Cancels the insertion and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747602-Insert-Crosstab-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747622-Insert-Image-Dialog-Box-Properties)
