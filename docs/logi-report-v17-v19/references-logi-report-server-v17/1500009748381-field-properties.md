---
title: "Field Properties"
id: 1500009748381
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748381-Field-Properties
updated_at: 2021-07-25T07:19:25Z
---

# Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748801-Fetch-Data)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748401-Fill-Effects)

# Field Properties

The Field Properties dialog box is used to specify the properties of a field. It appears when you right-click a field and select Properties from the shortcut menu.

There are the following tabs in this dialog box: [General](#General), [Font](#Font) and [Border](#Border).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## General

This tab shows some general information of the field.

![Field Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404942552343/dbprpty_gnrl.gif)

**Name**

Specifies the display name of the field.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Format**

Specifies the format of the field.

**Auto Scale in Number**

Specifies whether to
automatically scale the field values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows that of the field's parent data container. When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example, the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

**Height**

Specifies the height of the field.

**Width**

Specifies the width of the field.

**Position**

Displays the position mode of the field. If the field is directly contained in the report body, a tabular cell, or a text box, its position mode can be modified.

* **Absolute**: The field's position will be decided by its X and Y property values.
* **Static**: The field will be positioned at the default location in its container. If selected, the X, Y and other position-related properties will be hidden or disabled.

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

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the field.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box.

The following four options are available when image data is stored in the field, for example, a DBField with image as the data, or a formula field the expression of which is `openBinFile()`, `openBinURL()`, and so on. You can specify to use the original size of the image or customize the size by yourself.

**Original Size**

Web Report Studio adopts the original size of the image by default. Clear this option if you want to scale the image, then specify the scaling mode as required.

**Scaling Mode**

Specifies the scaling mode of the image, which controls the image behavior when you adjust the size of the area for displaying the image. Available when Original Size is unselected.

* **actual size** - Shows the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
* **fit image** - Adjusts the image to fill up the area for displaying the image, with its original perspective remained.
* **fit width** - Adjusts the image to fit the width of the area for displaying the image.
* **fit height** - Adjusts the image to fit the height of the area for displaying the image.
* **customize** - Adjusts the image according to the width and height that you specify in the Image Height and Image Width text boxes.

**Image Height**

Specifies the height of the area for displaying the image. Available when Original Size is unselected.

**Image Width**

- Specifies the width of the area for displaying the image. Available when Original Size is unselected.

## Font

This tab shows the font-related information of the field.

![Field Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404936862615/dbprpty_font.gif)

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

Specifies whether or not to attach a strikeout line to the text.

**Italic**

Specifies whether to make the text italic or not.

**Autofit**

Specifies whether or not to automatically adjust the width of the field. If the field is in a table column, the property takes effect only when the optin Autofit on the shortcut menu of the column is also set to true. takes effect only when the optin Autofit on the shortcut menu of the column containing the field is also set to true.

**Word Wrap**

Specifies whether or not to wrap the text to the field width.

**Ignore HTML Tag**

If this option is unselected, Logi Report will parse HTML tag elements in the field value while the report is to be saved as an HTML file; or the field value will appear in the HTML file the same as that in Web Report Studio (HTML tag elements in the field value, if any, will not be parsed).

## Border

This tab shows information about borders of the field.

![Field Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404942552727/dbprpty_border.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748801-Fetch-Data)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748401-Fill-Effects)
