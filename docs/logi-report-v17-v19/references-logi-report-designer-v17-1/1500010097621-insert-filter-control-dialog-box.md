---
title: "Insert Filter Control Dialog Box"
id: 1500010097621
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097621-Insert-Filter-Control-Dialog-Box
updated_at: 2021-07-23T19:15:39Z
---

# Insert Filter Control Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097601-Insert-Fields-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097641-Insert-Group-Column-Dialog-Box)

# Insert Filter Control Dialog Box

You can use the Insert Filter Control dialog box to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Filter) into a report for filtering data. This topic describes the options in the dialog box.

Designer displays the Insert Filter Control dialog box when you select Insert > Web Controls > Filter Control, or drag the Filter Control icon ![Filter Control icon](https://devnet.logianalytics.com/hc/article_attachments/4404848522135/icon_fltrcntrl.gif) from the Components panel into a report.

![Insert Filter Control dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856919703/instfltrctrl.gif)

You see the following options in the dialog box:

**Control Type**

Select the [type](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Type) of the filter control.

**Select Fields**

Select the fields to bind to the filter control. All the selected fields should be of the same data type.

**Customize Initial Values**

Select to customize the value list of the filter control.

Designer displays different customization options for different filter control types:

* **For Text List, Drop-down List, or Single Value Slider**  
  ![Customize Values for Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404848522519/cmpnt_wbcntrl_advc_fltr2.gif)
  + **Fetch Data**  
    Select to open the [Fetch Data dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097381-Fetch-Data-Dialog-Box) to select values from the database and add the selected values to the value text box.
  + **Value text box**  
    You can type values directly in the text box. Make sure the accuracy of their formats and values.

    The value text box is an editable multi-row plain text box. It supports general text editing operations such as Copy, Paste, Cut, Backspace, and Delete. You can use the Enter key on the keyboard to start a new row. Each row is a value of the user-defined value list.

    If you select Customize Initial Values but do not add any value the value box, Designer applies all values of the selected fields in the filter control.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif)**Calendar button**  
    Select to open the calendar to specify a Date/Time value.
* **For Range Slider**  
  ![Customize Values for Range Value Slider](https://devnet.logianalytics.com/hc/article_attachments/4404848523031/cmpnt_wbcntrl_advc_fltr3.gif)
  + **From**  
    Select the start value of the slider from the drop-down list or type the value in the text box.
  + **To**  
    Select the end value of the slider from the drop-down list or type the value in the text box.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif)**Calendar button**  
    Select to open the calendar to specify a Date/Time value.

**Link to Other Filters**

If you select the option, the filter control can be affected by other filter controls that apply to the same data components as the filter control.

**Special Function**

Designer displays the option for the Slide filter types. You can use it to specify a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Function) for the selected fields if they are of the Date/Time type.

**Apply To**

Select the target data components you want to apply the filter control to. The drop-down list includes all the data components in the current report that are based on the same data resources, in which the selected fields are contained.

**OK**

Select to insert the filter control into the report and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097601-Insert-Fields-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097641-Insert-Group-Column-Dialog-Box)
