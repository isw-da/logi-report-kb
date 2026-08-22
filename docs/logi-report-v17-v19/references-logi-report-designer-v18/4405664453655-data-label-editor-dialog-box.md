---
title: "Data Label Editor Dialog Box"
id: 4405664453655
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664453655-Data-Label-Editor-Dialog-Box
updated_at: 2022-01-27T20:36:03Z
---

# Data Label Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661496855-Data-Manager-Dialog-Box)

# Data Label Editor Dialog Box

You can use the Data Label Editor dialog box to [edit data labels](https://devnet.logianalytics.com/hc/en-us/articles/4405661370647-Editing-Range-Groups-on-Category-Values) in the range groups of a chart. This topic describes the options in the dialog box.

Designer displays the Data Label Editor dialog box when you select Edit Data Labels in the Data Label subtab of the Range tab in the [Format Category (X) Axis dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664488087-Format-Category-X-Axis-Dialog-Box#Datalb).

![Data Label Editor](https://devnet.logianalytics.com/hc/article_attachments/4420542160407/dtlbedtr.gif)

You see the following options in the dialog box:

**Toolbar**

You can use the following toolbar buttons to edit properties of the data labels.

* ![Insert Drop-down List button](https://devnet.logianalytics.com/hc/article_attachments/4420556206103/btn_insrtdrpdwn.gif) **Insert Drop-down List**  
  Select to insert a drop-down list into the editor.
* ![Font Face button](https://devnet.logianalytics.com/hc/article_attachments/4420550809367/btn_fntface.gif) **Font Face**  
  Specify the font face of the text in the selected data labels.
* ![Font Size button](https://devnet.logianalytics.com/hc/article_attachments/4420556076951/btn_fntsize.gif)**Font Size**  
  Specify the font size of the text in the selected data labels.
* ![Style button](https://devnet.logianalytics.com/hc/article_attachments/4420542056599/btn_stybx.gif)**Style**  
  Specify the style group applied to the selected data labels.
* ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4420556077591/btn_bold.gif)**Bold**  
  Select to apply bold formatting to the text in the selected data labels.
* ![Italic button](https://devnet.logianalytics.com/hc/article_attachments/4420550810391/btn_italic.gif)**Italic**  
  Select to italicize the text in the selected data labels.
* ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4420556077847/btn_underline.gif)**Underline**  
  Select to add a horizontal line under the text in the selected data labels.
* ![Justify button](https://devnet.logianalytics.com/hc/article_attachments/4420542060823/btn_justify.gif)**Justify**  
  Select to adjust the horizontal spacing so that the content is aligned evenly along both the left and right margins in the selected data labels.
* ![Left button](https://devnet.logianalytics.com/hc/article_attachments/4420542060183/btn_left.gif)**Left**  
  Select to align the content of the selected data labels to the left boundary of the data labels.
* ![Center button](https://devnet.logianalytics.com/hc/article_attachments/4420556081687/btn_center.gif)**Center**  
  Select to align the content of the selected data labels to the center of the data labels.
* ![Right button](https://devnet.logianalytics.com/hc/article_attachments/4420542060567/btn_right.gif)**Right**  
  Select to align the content of the selected data labels to the right boundary of the data labels.
* ![Background Color button](https://devnet.logianalytics.com/hc/article_attachments/4420556078231/btn_bkgrdcolor.gif)**Background Color**  
  Select to specify the background color of the selected data labels in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette).
* ![Foreground Color button](https://devnet.logianalytics.com/hc/article_attachments/4420556078487/btn_fntcolor.gif)**Foreground Color**  
  Select to specify the foreground color of the selected data labels in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette).
* ![Format Box button](https://devnet.logianalytics.com/hc/article_attachments/4420550942231/btn_fntfmt.gif)**Format Box**  
  Select to specify the data format of the values in the selected data label.
  + **Auto Scale in Number**  
    Designer displays this option when the selected data label is of the Number data type. You can use it to specify whether to automatically scale the values of the data label that fall into the two ranges:
    - When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
    - When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.

    By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Data label editing box**

You can edit the data labels you want to display on the range groups in this box. The box works like a special text box. A line in the box is a chart iterator, which is a special paragraph with markers or text.

To edit the data labels, select the information to show for each data label from the corresponding data label drop-down list. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4420556206103/btn_insrtdrpdwn.gif) to insert more data labels if the existing ones cannot meet your requirement. To delete a data label, select it and select **Backspace** on the keyboard.

To insert an iterator after an existing iterator, select in the existing iterator to select it, then select **Enter** on the keyboard. You can edit the content in a selected chart iterator, such as adding, deleting, or modifying markers and text segment in it. To edit properties of an iterator, select it, right-click on the blank space and select **Chart Iterator** from the shortcut menu to edit the iterator in the [Chart Iterator dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664433559-Chart-Iterator-Dialog-Box).

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661496855-Data-Manager-Dialog-Box)
