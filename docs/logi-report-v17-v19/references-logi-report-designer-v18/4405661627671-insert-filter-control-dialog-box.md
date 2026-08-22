---
title: "Insert Filter Control Dialog Box"
id: 4405661627671
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661627671-Insert-Filter-Control-Dialog-Box
updated_at: 2022-01-27T20:35:47Z
---

# Insert Filter Control Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661626647-Insert-Fields-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661629079-Insert-Group-Column-Dialog-Box)

# Insert Filter Control Dialog Box

You can use the Insert Filter Control dialog box to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Filter) into a report for filtering data. This topic describes the options in the dialog box.

Designer displays the Insert Filter Control dialog box when you navigate to Insert > Web Controls > Filter Control, or drag the Filter Control icon ![Filter Control icon](https://devnet.logianalytics.com/hc/article_attachments/4420402426903/icon_fltrcntrl.gif) from the Components panel into a report.

![Insert Filter Control dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410697879/instfltrctrl.gif)

You see the following options in the dialog box:

**Control Type**

Select the [type](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Type) of the filter control.

**Select Fields**

Select the fields to bind to the filter control. All the selected fields should be of the same data type.

**Customize Initial Values**

Select to customize the value list of the filter control.

Designer displays different customization options for different filter control types:

* **For Text List, Drop-down List, or Single Value Slider**  
  ![Customize Values for Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4420394755607/cmpnt_wbcntrl_advc_fltr2.gif)
  + **Fetch Data**  
    Select to open the [Fetch Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664511127-Fetch-Data-Dialog-Box) to select values from the database and add the selected values to the value text box.
  + **Value text box**  
    You can type values directly in the text box. Make sure the accuracy of their formats and values.

    The value text box is an editable multirow plain text box. It supports general text editing operations such as Copy, Paste, Cut, Backspace, and Delete. You can select Enter on the keyboard to start a new row. Each row is a value of the user-defined value list.

    If you select Customize Initial Values but do not add any value the value box, Designer applies all values of the selected fields in the filter control.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420402355351/btn_clndr.gif)**Calendar button**  
    Select to open the calendar widget to specify a date and time value.
* **For Range Slider**  
  ![Customize Values for Range Value Slider](https://devnet.logianalytics.com/hc/article_attachments/4420394756375/cmpnt_wbcntrl_advc_fltr3.gif)
  + **From**  
    Select the start value of the slider from the drop-down list or type the value in the text box.
  + **To**  
    Select the end value of the slider from the drop-down list or type the value in the text box.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420402355351/btn_clndr.gif)**Calendar button**  
    Select to open the calendar widget to specify a date and time value.

**Link to Other Filters**

When you select this option, the filter control can be affected by other filter controls that apply to the same data components as the filter control.

**Special Function**

Designer displays this option for the Slide filter types. You can use it to specify a [special function](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables#Function) for the selected fields if they are of the Date/Time type.

**Apply To**

Select the target data components you want to apply the filter control to. This drop-down list displays all the data components in the current report that are based on the same data resources containing the selected fields.

**OK**

Select to insert the filter control into the report and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661626647-Insert-Fields-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661629079-Insert-Group-Column-Dialog-Box)
