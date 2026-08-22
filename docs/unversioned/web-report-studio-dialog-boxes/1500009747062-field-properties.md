---
title: "Field Properties"
id: 1500009747062
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747062-Field-Properties
updated_at: 2021-07-24T00:48:28Z
---

# Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747542-Fetch-Data-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747082-Fill-Effects-Dialog-Box-Properties)

# Field Properties

This topic describes how you can use the Field Properties dialog box to update the properties of a field. Server displays the dialog box when you right-click a field and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)

You see these elements on all the tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about the Field Properties dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## General Tab Properties

This tab shows some general information of the field.

![Field Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404885485975/dbprpty_gnrl.gif)

**Name**

Specifies the display name of the field.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Format**

Specifies the format of the field.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled; but if the specified format conflicts with the Number data type, Logi Report will ignore the Auto Scale in Number setting.

**Height**

Specifies the height of the field.

**Width**

Specifies the width of the field.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

**Top Padding**

Specifies the space between the text of the field and its top border.

**Bottom Padding**

Specifies the space between the text of the field and its bottom border.

**Left Padding**

Specifies the space between the text of the field and its left border.

**Right Padding**

Specifies the space between the text of the field and its right border.

**Background**

Specifies the background color of the field.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the field.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box.

The following four options are available when image data is stored in the field, for example, a DBField with image as the data, or a formula field the expression of which is `openBinFile()`, `openBinURL()`, and so on. You can specify to use the original size of the image or customize the size by yourself.

**Original Size**

Web Report Studio adopts the original size of the image by default. Clear this option if you want to scale the image, then specify the scaling mode.

**Scaling Mode**

Logi Report enables this option when you clear **Original Size**.

* **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
* **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
* **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
* **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
* **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.

**Image Height**

Specifies the height of the area for displaying the image. Available when Original Size is unselected.

**Image Width**

Specifies the width of the area for displaying the image. Available when Original Size is unselected.

## Font Tab Properties

This tab shows the font-related information of the field.

![Field Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880393111/dbprpty_font.gif)

**Font**

Specifies the font face of the text.

**Size**

Specifies the font size of the text.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the text in the field.

**Vertical Alignment**

Specifies the vertical alignment mode of the text in the field.

**Bold**

Specifies whether to make the text bold or not.

**Underline**

Specifies whether the text will be underlined or not.

**Strikethrough**

Specifies whether to attach a strikeout line to the text.

**Italic**

Specifies whether to make the text italic or not.

**Autofit**

Specifies whether to automatically adjust the width of the field. If the field is in a table column, the property takes effect only when the option Autofit on the shortcut menu of the column is also set to true. takes effect only when the option Autofit on the shortcut menu of the column containing the field is also set to true.

**Word Wrap**

Specifies whether to wrap the text to the field width.

**Ignore HTML Tag**

By default, Logi Report Engine ignores the HTML tag elements that are included in the values of the field so they display exactly as what they are in the report. Clear the option if you want Logi Report Engine to transfer the HTML tag elements to the web browser so they are translated into HTML by the web browser. The setting also applies in the HTML output of the report.

## Border Tab Properties

This tab shows information about borders of the field.

![Field Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404885486231/dbprpty_border.gif)

**Color**

Specifies the border color.

**Width**

Specifies the border width.

**Top Line**

Specifies the style of the top border line.

**Bottom Line**

Specifies the style of the bottom border line.

**Left Line**

Specifies the style of the left border line.

**Right Line**

Specifies the style of the right border line.

**Shadow**

Specifies whether the borders will have a shadow effect or not. This property cannot be rendered in Web Report Studio or JDashboard.

**Shadow Color**

Specifies the color of the border shadow. This property cannot be rendered in Web Report Studio or JDashboard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747542-Fetch-Data-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747082-Fill-Effects-Dialog-Box-Properties)
