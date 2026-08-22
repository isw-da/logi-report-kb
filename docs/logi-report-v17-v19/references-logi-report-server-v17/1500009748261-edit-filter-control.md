---
title: "Edit Filter Control"
id: 1500009748261
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748261-Edit-Filter-Control
updated_at: 2021-07-25T07:19:26Z
---

# Edit Filter Control

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748241-Edit-Detail-Table)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748281-Edit-Image)

# Edit Filter Control

The Edit Filter Control dialog box is used to [edit a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500009751581-Using-Web-Controls#Filter). It appears when you right-click on a filter control and then select Edit, or when you select ![Select Fields](https://devnet.logianalytics.com/hc/article_attachments/4404942451479/btn_chsr2.gif) beside the Filter On text box on the the General tab of the [Filter Control Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009721602-Filter-Control-Properties) dialog box.

![Edit Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936863127/edtfltrctrl.gif)

**Control Type**

Specifies the type of the filter control.

**Select Fields**

Specifies the fields to bind to the filter control. All the selected fields should be of the same data type. The incomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

**Customize Initial Values**

Specifies to customize the value list of the filter control.

* **Fetch Data**  
   Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009748801-Fetch-Data) dialog box to select values from the database and adds the selected values to the text box below.
* **Text box**  
   You can type values directly in the text box. Make sure the accuracy of their formats and values.

  The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete and etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user defined value list.

  When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
* ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif)  
   Specifies a Date/Time value in the text box.

**Link to Other Filters**

Specifies whether the filter control can be affected by other on-screen filters that apply to the same data components as the filter control.

**Apply To**

Specifies the components to which the filter created with the filter control will be applied.

**OK**

Inserts a filter control into the report and closes the dialog box.

**Cancel**

Cancels the insertion and closes the dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748241-Edit-Detail-Table)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748281-Edit-Image)
