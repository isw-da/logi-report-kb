---
title: "Edit Filter Control Dialog Box"
id: 1500010096261
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096261-Edit-Filter-Control-Dialog-Box
updated_at: 2021-07-23T19:15:16Z
---

# Edit Filter Control Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058742-Edit-Gradient-Color-Dialog-Box)

# Edit Filter Control Dialog Box

You can use the Edit Filter Control dialog box to [edit a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Filter). This topic describes the options in the dialog box.

Designer displays the Edit Filter Control dialog box when you right-click a filter control and select Edit Filter Control from the shortcut menu.

![Edit Filter Control dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848585879/edtfltrctrl.gif)

You see the following options in the dialog box:

**Control Type**

The drop-down list contains the [filter control types](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Type) you can apply for the current report. Select the type you need.

**Select Fields**

Select the fields to bind to the filter control. All the selected fields should be of the same data type. You cannot bind uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

**Customize Initial Values**

Select to customize the value list of the filter control.

Designer displays different customizing options according to different control types:

* **For Text List, Drop-down List, or Single Value Slider**  
  ![Customize Values for Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404848522519/cmpnt_wbcntrl_advc_fltr2.gif)
  + **Fetch Data**  
    Select to open the [Fetch Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097381-Fetch-Data-Dialog-Box) to select values from the database and adds the selected values to the text box below.
  + **Text box**  
    You can type values directly in the text box. Make sure the accuracy of their formats and values.

    The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete, and so on. You can use the Enter key on the keyboard to start a new row. Each row is a value of the user-defined value list.

    If you select Customize Initial Values but do not type anything in the text box, Designer applies all values of the selected fields in the filter control.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif)**Calendar button**  
    Select to open the calendar to specify a Date/Time value using the calendar.
* **For Range Slider**  
  ![Customize Values for Range Value Slider](https://devnet.logianalytics.com/hc/article_attachments/4404848523031/cmpnt_wbcntrl_advc_fltr3.gif)
  + **From**  
    Select the start value of the slider from the drop-down list or type the value in the text box.
  + **To**  
    Select the end value of the slider from the drop-down list or type the value in the text box.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif)**Calendar button**  
    Select to open the calendar to specify a Date/Time value using the calendar.

**Link to Other Filters**

Select to link the filter control with other filter controls that apply to the same data components as the filter control. For the case of one filter using a business view and another using a query, if the business view contains the query definition, the two filters are also linked.

**Special Function**

Designer displays the option only to the slider control types. Select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Function) for the specified fields if they are of the Date/Time type.

**Apply To**

The drop-down list contains all the data components in the current report that are based on the same data resources the selected fields are in. Select the target data components to which you want to apply the filter control.

**OK**

Select to apply the changes to the filter control and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058722-Edit-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058742-Edit-Gradient-Color-Dialog-Box)
