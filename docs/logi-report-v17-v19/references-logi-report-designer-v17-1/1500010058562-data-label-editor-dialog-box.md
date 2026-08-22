---
title: "Data Label Editor Dialog Box"
id: 1500010058562
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058562-Data-Label-Editor-Dialog-Box
updated_at: 2021-07-23T19:15:13Z
---

# Data Label Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096101-Data-Manager-Dialog-Box)

# Data Label Editor Dialog Box

You can use the Data Label Editor dialog box to [edit data labels](https://devnet.logianalytics.com/hc/en-us/articles/1500010057102-Editing-Range-Groups-on-Category-Values) in the range groups of a chart. This topic describes the options in the dialog box.

Designer displays the Data Label Editor dialog box when you select Edit Data Labels in the Data Label sub tab of the Range tab in the [Format Category (X) Axis dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097021-Format-Category-X-Axis-Dialog-Box#Datalb).

![Data Label Editor](https://devnet.logianalytics.com/hc/article_attachments/4404856980887/dtlbedtr.gif)

You see the following options in the dialog box:

**Toolbar**

You can use the following toolbar buttons to edit the format of the data labels.

* ![Insert Drop-down List button](https://devnet.logianalytics.com/hc/article_attachments/4404848589847/btn_insrtdrpdwn.gif) **Insert Drop-down List**  
  Select to insert a drop-down list into the editor.
* ![Font Face button](https://devnet.logianalytics.com/hc/article_attachments/4404856791447/btn_fntface.gif) **Font Face**  
  Specify the font face of the text in the selected object.
* ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4404856791703/btn_fntsize.gif)**Font Size**  
  Specify the font size of the text in the selected object.
* ![Style button](https://devnet.logianalytics.com/hc/article_attachments/4404848369559/btn_stybx.gif)**Style**  
  Specify the style group applied to the selected object.
* ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404848369815/btn_bold.gif)**Bold**  
  Select to make the text in bold style in the selected object.
* ![Italic button](https://devnet.logianalytics.com/hc/article_attachments/4404856792087/btn_italic.gif)**Italic**  
  Select to italicize the text in the selected object.
* ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4404856792343/btn_underline.gif)**Underline**  
  Select to add a horizontal line under the text in the selected object.
* ![Justify button](https://devnet.logianalytics.com/hc/article_attachments/4404848373271/btn_justify.gif)**Justify**  
  Select to adjust the horizontal spacing so that the content is aligned evenly along both the left and right margins in the selected object.
* ![Left button](https://devnet.logianalytics.com/hc/article_attachments/4404856795543/btn_left.gif)**Left**  
  Select to align the content of the selected object to the left boundary of the object.
* ![Center button](https://devnet.logianalytics.com/hc/article_attachments/4404848372759/btn_center.gif)**Center**  
  Select to align the content of the selected object to the center of the object.
* ![Right button](https://devnet.logianalytics.com/hc/article_attachments/4404848373015/btn_right.gif)**Right**  
  Select to align the content of the selected object to the right boundary of the object.
* ![Background Color button](https://devnet.logianalytics.com/hc/article_attachments/4404856792855/btn_bkgrdcolor.gif)**Background Color**  
  Select to specify the background color of the selected object in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette).
* ![Foreground Color button](https://devnet.logianalytics.com/hc/article_attachments/4404848370327/btn_fntcolor.gif)**Foreground Color**  
  Select to specify the foreground color of the selected object in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette).
* ![Format Box button](https://devnet.logianalytics.com/hc/article_attachments/4404856925591/btn_fntfmt.gif)**Format Box**  
  Select to specify the data format of the values in the selected object.
  + **Auto Scale in Number**  
    Designer displays the option when the selected object is of the Number data type. You can use it to specify whether to automatically scale the object values that fall into the following two ranges:
    - When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
    - When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

    By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Data label editing box**

You can edit the data labels you want to display on the range groups in this box. The box works like a special text box. A line in the box is a chart iterator, which is a special paragraph with markers or text.

To edit the data labels, select the information to show for each data label from the corresponding data label drop-down list. Select the **Insert Drop-down List** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404848589847/btn_insrtdrpdwn.gif) to insert more data labels if the existing ones cannot meet your requirement. To delete a data label, select it and select Backspace on the keyboard.

To insert an iterator after an existing iterator, select on the existing iterator to select it, then select Enter. You can edit the content in a selected chart iterator, such as adding, deleting, or modifying markers and text segment in it. To edit the properties of an iterator, select it, right-click on the blank space and select **Chart Iterator** from the shortcut menu to edit the iterator in the [Chart Iterator dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058182-Chart-Iterator-Dialog-Box).

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096081-Data-Format-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096101-Data-Manager-Dialog-Box)
