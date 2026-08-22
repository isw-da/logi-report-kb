---
title: "Format Pointer Label"
id: 1500009745761
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745761-Format-Pointer-Label
updated_at: 2021-07-25T07:20:03Z
---

# Format Pointer Label

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745741-Format-Platform)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745781-Format-Radar)

# Format Pointer Label

The Format Pointer Label dialog box is used to format the pointer labels in a gauge chart (excluding bubble gauge chart).

There are the following tabs in this dialog box: [General](#General), [Font](#Font) and [Format](#Format).

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

## General

Specifies the general properties of the labels.

![Format Pointer Label - General](https://devnet.logianalytics.com/hc/article_attachments/4404936925335/fmtpntlbl_gnrl.gif)

**Option**

Specifies the size and position of the labels.

* **Width**  
   Specifies the width of the labels, in inches.
* **Height**  
   Specifies the height of the labels, in inches.
* **X**  
   Specifies the horizontal coordinate of the top left corner of the labels, relative to their parent container. It takes effect when the Show Pointer Value option is selected and Position is set to customized in the Pointer tab of the gauge's corresponding Format XXX Gauge dialog box.
* **Y**  
   Specifies the vertical coordinate of the top left corner of the labels, relative to their parent container. It takes effect when the Show Pointer Value option is selected and Position is set to customized in the Pointer tab of the gauge's corresponding Format XXX Gauge dialog box.
* **Alignment**  
   Specifies the alignment of the label text.
* **Word Wrap**  
   Specifies whether to enable the word wrap function for the label text.

**Fill**

Specifies the color and transparency of the labels.

* **Color**  
   Specifies the color to fill the labels. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.
* **Transparency**  
   Specifies the transparency to fill the labels.

**Border**

Specifies the properties for borders of the labels.

* **Line Style**  
   Specifies the line style to apply to the border.
* **Border Type**  
   Specifies the type of the border.
* **Color**  
   Specifies the color of the border. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009746261-Select-Color) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.
* **Transparency**  
   Specifies the transparency for color of the border.
* **Thickness**  
   Specifies the thickness of the border, in inches.

**Orientation**

* **Angle**  
   Specifies the rotation angle of the labels.

## Font

Specifies properties for font of the label text.

![Format Pointer Label - Font](https://devnet.logianalytics.com/hc/article_attachments/4404936925591/fmtpntlbl_font.gif)

**Font**

Lists all the available font faces that can be selected to apply to the text.

**Size**

Specifies the font size of the text.

**Fill Type**

Specifies the fill type of the text. It can be one of the following: none, color, texture and gradient.

**Color**

Specifies the color of the text. It takes effect only when Fill Type in this tab is color.

**Font Style**

Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.

**Transparency**

Specifies the color transparency of the text.

## Format

Specifies the data format of the labels.

![Format Pointer Label - Format](https://devnet.logianalytics.com/hc/article_attachments/4404942590231/fmtpntlbl_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Displays all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500009721482-Data-Format#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the text box and then select Add to add it as the format of the specified category.

**Auto Scale in Number**

Specifies whether to
automatically scale the pointer labels that are of the Number data type when the label values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009745741-Format-Platform#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example, the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Sample**

Displays a preview sample of your selection.

**Stack**

Lists all the formats you select from different categories.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the labels.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745741-Format-Platform)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745781-Format-Radar)
