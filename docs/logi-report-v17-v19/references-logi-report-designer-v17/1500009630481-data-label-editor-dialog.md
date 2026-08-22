---
title: "Data Label Editor Dialog"
id: 1500009630481
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630481-Data-Label-Editor-Dialog
updated_at: 2021-07-24T16:04:50Z
---

# Data Label Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607682-Data-Format-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630501-Data-Manager-Dialog)

# Data Label Editor Dialog

The Data Label Editor helps you to [edit data labels](https://devnet.logianalytics.com/hc/en-us/articles/1500009606142-Editing-Range-Groups-on-Category-Values) in the range groups of a chart. It appears when you select Edit Data Labels in the Data Label sub tab of the Range tab in the [Format Category (X) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009608382-Format-Category-X-Axis-Dialog#Datalb) dialog.

![Data Label Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904356375/dtlbedtr.gif)

The following are details about options in the editor.

**Toolbar**

You can use the following toolbar buttons to edit the format of the data labels.

* ![Insert Drop-down List button](https://devnet.logianalytics.com/hc/article_attachments/4404916807319/btn_insrtdrpdwn.gif) **Insert Drop-down List**  
   Inserts a drop-down list into the editor.
* ![Font Face button](https://devnet.logianalytics.com/hc/article_attachments/4404911579799/btn_fntface.gif) **Font Face**  
   Specifies the font face of the text in the selected object.
* ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4404911580055/btn_fntsize.gif)**Font Size**  
   Specifies the font size of the text in the selected object.
* ![Style button](https://devnet.logianalytics.com/hc/article_attachments/4404911580311/btn_stybx.gif)**Style**  
   Specifies the style group applied to the selected object.
* ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404904159639/btn_bold.gif)**Bold**  
   Specifies whether or not to bold the text in the selected object.
* ![Italic button](https://devnet.logianalytics.com/hc/article_attachments/4404911580695/btn_italic.gif)**Italic**  
   Specifies whether or not to italicize the text in the selected object.
* ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4404904159895/btn_underline.gif)**Underline**  
   Specifies whether or not to underline the text in the selected object.
* ![Justify button](https://devnet.logianalytics.com/hc/article_attachments/4404904165271/btn_justify.gif)**Justify**  
   Adjusts horizontal spacing so that the content is aligned evenly along both the left and right margins in the selected object.
* ![Left button](https://devnet.logianalytics.com/hc/article_attachments/4404904164375/btn_left.gif)**Left**  
   Aligns the content of the selected object to the left boundary of the object.
* ![Center button](https://devnet.logianalytics.com/hc/article_attachments/4404904164759/btn_center.gif)**Center**  
   Aligns the content of the selected object to the center of the object.
* ![Right button](https://devnet.logianalytics.com/hc/article_attachments/4404904165015/btn_right.gif)**Right**  
   Aligns the content of the selected object to the right boundary of the object.
* ![Background Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904160151/btn_bkgrdcolor.gif)**Background Color**  
   Specifies the background color of the selected object on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette).
* ![Foreground Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904160407/btn_fntcolor.gif)**Foreground Color**  
   Specifies the foreground color of the selected object on the color palette.
* ![Format Box button](https://devnet.logianalytics.com/hc/article_attachments/4404904277143/btn_fntfmt.gif)**Format Box**  
   Specifies the format of the values in the selected object.
  + **Auto Scale in Number**  
     Available when the selected object is of the Number data type. It specifies whether to automatically scale the object values that fall into the two ranges:
    - When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
    - When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

    By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Data label edit box**

You can edit the data labels you want to display on the range groups in this box. The box works like a special text box. A line in the box is a chart iterator, which is a special paragraph with markers or text.

To edit the data labels, select the information to show for each data label from the corresponding data label drop-down list. Select the **Insert Drop-down List** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404916807319/btn_insrtdrpdwn.gif) to insert more data labels if the existing ones cannot meet your requirement. To delete a data label, select it and press **Backspace** on the keyboard.

To insert an iterator after an existing iterator, select on the existing iterator to select it, then press the **Enter** key on the Keyboard. You can edit the content in a selected chart iterator, such as adding, deleting, or modifying markers and text segment in it. To edit the properties of an iterator, select it, right-click on the blank space and select **Chart Iterator** from the shortcut menu to edit the iterator in the [Chart Iterator](https://devnet.logianalytics.com/hc/en-us/articles/1500009630021-Chart-Iterator-Dialog) dialog.

**OK**

Applies the settings and closes the dialog.

**Cancel**

Cancels the settings and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607682-Data-Format-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630501-Data-Manager-Dialog)
