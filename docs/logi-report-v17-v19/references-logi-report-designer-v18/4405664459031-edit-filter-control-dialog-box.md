---
title: "Edit Filter Control Dialog Box"
id: 4405664459031
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664459031-Edit-Filter-Control-Dialog-Box
updated_at: 2022-01-27T20:35:52Z
---

# Edit Filter Control Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661511703-Edit-Gradient-Color-Dialog-Box)

# Edit Filter Control Dialog Box

You can use the Edit Filter Control dialog box to [edit a filter control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Filter). This topic describes the options in the dialog box.

Designer displays the Edit Filter Control dialog box when you right-click a filter control and select Edit Filter Control from the shortcut menu.

![Edit Filter Control dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556204055/edtfltrctrl.gif)

You see the following options in the dialog box:

**Control Type**

This drop-down list contains the [filter control types](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Type) you can apply for the current report. Select the type you need.

**Select Fields**

Select the fields to bind to the filter control. All the selected fields should be of the same data type. You cannot bind uncomparable data type fields to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary, and Varbinary.

**Customize Initial Values**

Select to customize the value list of the filter control.

Designer displays different customizing options according to different control types:

* **For Text List, Drop-down List, or Single Value Slider**  
  ![Customize Values for Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4420556204311/cmpnt_wbcntrl_advc_fltr2.gif)
  + **Fetch Data**  
    Select to open the [Fetch Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664511127-Fetch-Data-Dialog-Box) to select values from the database and adds the selected values to the text box below.
  + **Text box**  
    You can type values directly in the text box. Make sure the accuracy of their formats and values.

    This text box is an editable multirow plain text box. It supports general text editing operations including Copy, Paste, Cut, Backspace, Delete, and so on. You can select Enter on the keyboard to start a new row. Each row is a value of the user-defined value list.

    If you select Customize Initial Values but do not type anything in the text box, Designer applies all values of the selected fields in the filter control.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420550878743/btn_clndr.gif)**Calendar button**  
    Select to open the calendar widget to specify a Date/Time value.
* **For Range Slider**  
  ![Customize Values for Range Value Slider](https://devnet.logianalytics.com/hc/article_attachments/4420556204567/cmpnt_wbcntrl_advc_fltr3.gif)
  + **From**  
    Select the start value of the slider from the drop-down list or type the value in the text box.
  + **To**  
    Select the end value of the slider from the drop-down list or type the value in the text box.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420550878743/btn_clndr.gif)**Calendar button**  
    Select to open the calendar widget to specify a Date/Time value.

**Link to Other Filters**

Select to link the filter control with other filter controls that apply to the same data components as the filter control. For the case of one filter using a business view and another using a query, if the business view contains the query definition, the two filters are also linked.

**Special Function**

Designer displays this option only to the slider control types. Select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables#Function) for the specified fields if they are of the Date/Time type.

**Apply To**

This drop-down list contains all the data components in the current report that are based on the same data resources the selected fields are in. Select the target data components to which you want to apply the filter control.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661510295-Edit-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661511703-Edit-Gradient-Color-Dialog-Box)
