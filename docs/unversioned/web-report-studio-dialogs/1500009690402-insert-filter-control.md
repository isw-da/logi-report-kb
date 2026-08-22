---
title: "Insert Filter Control"
id: 1500009690402
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009690402-Insert-Filter-Control
updated_at: 2021-11-03T06:57:14Z
---

# Insert Filter Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009690382-Insert-Crosstab)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009716581-Insert-Image)

# Insert Filter Control

The Insert Filter Control dialog helps you to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009719281-Using-Web-Controls#Filter) into a report for filtering data components in the report. This dialog appears when you drag Filter Control from the Components panel to a report.

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4412139488663/insrtfltrctrl.gif)

**Control Type**

Specifies the type of the filter control.

**Select Fields**

Specifies the fields to bind to the filter control. All the selected fields should be of the same data type. The uncomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary and Varbinary.

**Customize Initial Values**

Specifies to customize the value list of the filter control.

* **Fetch Data**  
   Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009690282-Fetch-Data) dialog to select values from the database and adds the selected values to the text box below.
* **Text box**  
   You can type in values directly in the text box. Make sure the accuracy of their formats and values.

  The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete and etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user-defined value list.

  When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
* ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4412112486935/btn_clndr.gif)  
   Specifies a Date/Time value in the text box.

**Link to Other Filters**

Specifies whether the filter control can be affected by other on-screen filters that apply to the same data components as the filter control.

**Apply To**

Specifies the components to which the filter created with the filter control will be applied.

**OK**

Inserts a filter control into the report and closes the dialog.

**Cancel**

Cancels the insertion and closes the dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009690382-Insert-Crosstab)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009716581-Insert-Image)
