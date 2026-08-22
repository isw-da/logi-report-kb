---
title: "Insert Filter Control Dialog"
id: 1500010066901
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010066901-Insert-Filter-Control-Dialog
updated_at: 2021-07-24T10:38:40Z
---

# Insert Filter Control Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031442-Insert-Fields-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031462-Insert-Group-Column-Dialog)

# Insert Filter Control Dialog

The Insert Filter Control dialog helps you to [insert a filter control](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Filter) into a report for filtering data. It appears when you select Insert > Web Controls > Filter Control, or drag ![Filter Control button](https://devnet.logianalytics.com/hc/article_attachments/4404909181847/btn_instfltrcntrl.gif) from the Components panel into a report.

![Insert Filter Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909183255/instfltrctrl.gif)

The following are details about options in the dialog:

**Control Type**

Specifies the [type](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Type) of the filter control.

**Select Fields**

Specifies the fields to bind to the filter control. All the selected fields should be of the same data type. The uncomparable data type fields cannot be bound to a single filter control, such as Binary, Blob, Clob, Longvarchar, Longvarbinary and Varbinary.

**Customize Initial Values**

Specifies to customize the value list of the filter control.

The customization UI is different according to the control types:

* **For Text List, Drop-down List or Single Value Slider**  
  ![Customize Values for Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404901205143/cmpnt_wbcntrl_advc_fltr2.gif)
  + **Fetch Data**  
     Opens the [Fetch Data](https://devnet.logianalytics.com/hc/en-us/articles/1500010066721-Fetch-Data-Dialog) dialog to select values from the database and adds the selected values to the text box below.
  + **Text box**  
     You can type in values directly in the text box. Make sure the accuracy of their formats and values.

    The text box is an editable multi-row plain text box. It supports general text editing operations including copy, paste, cut, backspace, delete and etc. The Enter key on the keyboard is used to start a new row. Each row is a value of the user defined value list.

    When Customize Initial Values is selected but the text box is empty, all values of the selected fields will be used in the filter control.
  + ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404901205399/btn_slctdt.gif)  
     Specifies a Date/Time value using the calendar.
* **For Range Slider**  
  ![Customize Values for Range Value Slider](https://devnet.logianalytics.com/hc/article_attachments/4404901205655/cmpnt_wbcntrl_advc_fltr3.gif)
  + **From**  
     Select the start value of the slider from the drop-down list or type the value in the text box. For Date/Time type fields, you can also select ![Calendar](https://devnet.logianalytics.com/hc/article_attachments/4404901205399/btn_slctdt.gif) to specify a value using the calendar.
  + **To**  
     Select the end value of the slider from the drop-down list or type the value in the text box. For Date/Time type fields, you can also select ![Calendar](https://devnet.logianalytics.com/hc/article_attachments/4404901205399/btn_slctdt.gif) to specify a value using the calendar.

**Link to Other Filters**

Specifies whether the filter control can be affected by other filter controls that apply to the same data components as the filter control. For the case of one filter using a business view and another using a query, if the business view contains the query definition, the two filters are also linked.

**Special Function**

Specifies a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Function) for the selected fields if they are of the Date/Time type. Available only to the slider control types.

**Apply To**

Specifies the target data components you want to apply the filter control to. The drop-down list includes all the data components in the current report that are based on the same data resources the selected fields are in.

**OK**

Inserts the filter control into the report and closes the dialog.

**Cancel**

Cancels the operation and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031442-Insert-Fields-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031462-Insert-Group-Column-Dialog)
