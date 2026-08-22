---
title: "Data Field Properties"
id: 4405683621271
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683621271-Data-Field-Properties
updated_at: 2022-01-27T07:58:38Z
---

# Data Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683619223-Customized-Page-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690502295-Edit-Additional-Values-Dialog-Box-Properties)

# Data Field Properties

You can use the Data Field Properties dialog box to edit the properties of a DBField. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Others Tab Properties](#Others)
* [Display Tab Properties](#Render)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the data field.

![Data Field Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420461713303/dbprpty_genrl.gif)

**Name**

Specify the display name of the data field.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Format**

Specify the data format of the data field.

**Format Locale**

Specify the locale for displaying and formatting values of the object when its data type is locale sensitive, such as the date and time formats, and number and currency formats. Default is the locale of your JVM or the language of the NLS report. Choose an option from the drop-down list if you want to change the locale.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) When you use a formula to control the locale, the return value should be the two-letter language and country codes as defined by ISO-639 and ISO-3166 in the format *language\_country*, for example, de\_DE.

**Auto Scale in Number**

Select **true** if you want to automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Logi Report will ignore the **Auto Scale in Number** setting.

**Position**

Select the position mode of the object when it is directly contained in the report body, a tabular cell, or a text box.

* **Absolute**  
  Select if you want to use the X and Y property values to decide the object's position.
* **Static**  
  Select if you want to place the object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**X**

Specify the X coordinate of the data field.

**Y**

Specify the Y coordinate of the data field.

**Width**

Specify the width of the data field.

**Height**

Specify the height of the data field.

**Top Padding**

Specify the space between the text of the object and its top border.

**Bottom Padding**

Specify the space between the text of the object and its bottom border.

**Left Padding**

Specify the space between the text of the object and its left border.

**Right Padding**

Specify the space between the text of the object and its right border.

**Background**

Specify the background color of the data field.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

**Foreground**

Specify the foreground color of the data field.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

## Font Tab Properties

Specify the font properties of the data field.

![Data Field Properties dialog box - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4420447332503/dbprpty_font.gif)

**Font**

Select the font face of the text.

**Size**

Specify the font size of the text.

**Horizontal Alignment**

Select the horizontal alignment mode of the text in the object.

**Vertical Alignment**

Select the vertical alignment mode of the text in the object.

**Bold**

Enable this property if you want to make the text bold.

**Italic**

Enable this property if you want to make the text italic.

**Underline**

Enable this property if you want to underline the text.

**Strikethrough**

Enable this property if you want to attach a strikeout line to the text.

**Autofit**

Enable this property if you want to automatically expand the object width according to the maximum length of the contents.

**Reduce Width When Autofit**

Enable this property if you want to reduce the width of the object according to its content when you specify to automatically adjust its width (the object's Autofit being true) and the actual width of the content is smaller than that of the object.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) This property takes effect when you set Position of the object to absolute; but, it does not work if the Word Wrap property of the object is true.

**Word Wrap**

Enable this property if you want to wrap the text to the object width.

**Ignore HTML Tag**

Enable this property if you don't want Logi Report Engine to parse the HTML tag elements in the text, at runtime or in the HTML output, so they display exactly as what they are in the report.

Disable this property if you want Engine to transfer the HTML tag elements to the web browser so the web browser translates them into HTML.

## Border Tab Properties

Specify the border properties of the data field.

![Data Field Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420461713559/dbprpty_border.gif)

**Color**

Specify the border color.

**Width**

Specify the border width in inches.

**Top Line**

Select the style of the top border line.

**Bottom Line**

Select the style of the bottom border line.

**Left Line**

Select the style of the left border line.

**Right Line**

Select the style of the right border line.

**Shadow**

Select **true** if you want to add a shadow effect to the border.

**Shadow Color**

Specify the color of the border shadow. To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683679639-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

## Others Tab Properties

Configure some miscellaneous settings.

![Data Field Properties dialog box - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4420453654167/dbprpty_other.gif)

**TOC Anchor**

Select **true** if you want to add the object to the TOC tree in the TOC Browser.

**Suppress When No Records**

Select **true** if you want to hide the object in the report when no record returns to its parent data component.

**Suppress If Null**

If true and the field value is null, Server will not display the data field.

**Export to XLS**

Select **true** if you want to export the object when you save the report as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

Select **true** if you want to export the object when you save the report as a TXT file with Delimited Format.

**Logic Column**

You see this property when the object is in a table. Select **next visible column** if you want to show the object in the next visible table cell in the same row when you have hidden the column that holds the object.

## Display Tab Properties

You can use this tab to modify the display type of the data field as one of the following: Text, Barcode, QR Code, Image, Text Field, Text Area, Checkbox, Radio Button, Image Button, Button, Submit, Reset, and Hidden. Select an item from the **Display Type** list, and then set the corresponding properties.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) For the **Text** display type, there is no property available. For a field that displays as rank, you cannot change its display type.

### Barcode

Select to display the data field as barcode.

![Data Field Properties dialog box - Barcode Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420461714327/dbprpty_rndrbrcd.gif)

**Symbology**

Select the barcode type.

**Scale Mode**

Select the unit for the values of Quiet Zone, Narrow Width, Supplement, Height, and Ratio.

**Quiet Zone**

Specify the space around the barcode.

**Narrow Width**

Specify the width of the narrowest barcode bar.

**Supplement**

Specify the supplement of the barcode.

**Height**

Specify the height of the barcode bars.

**Message**

Specify the default value of the barcode.

**Ratio**

Specify the width ratio of the thick bar to the thin bar.

**Orientation**

Specify the rotation angle in degrees.

**Use Default Message**

Select **true** to use the Message value as the barcode value in the report.

**Enable Checking Digits**

Select **true** to include check digits in the barcode.

**Display HR**

Select **true** to display the characters together with the barcode bars.

### QR Code

Select to display the data field as QR Code.

![Data Field Properties dialog box - QR Code Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420447334295/dbprpty_qrcd.gif)

**Margin**

Specify the margin between the image in the middle of the QR Code and the border of the QR Code.

**Error Correction Level**

Select the error correction level for the QR Code: L, M, Q, or H.

**Default Message**

Specify the default value of the QR Code.

**Use Default Message**

Select **true** to use the default value of the QR Code in the report.

### Image

Select to display the data field as image.

![Data Field Properties dialog box - Image Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420461714711/dbprpty_rndrimg.gif)

**Scaling Mode**

Server enables this property when **Original Size** is **false**.

* **actual size**  
  Select to show the image in its actual size. If the display area is smaller than the image, Server hides part of the image.
* **fit image**Select if you want the image to fill the display area and keep the original perspective ratio under the limitation of Max Ratio.
* **fit width**Select if you want the image to fit the display area width under the limitation of Max Ratio.
* **fit height**Select if you want the image to fit the display area height, under the limitation of Max Ratio.
* **customize**Select if you want to specify the width and height of the image in the size fields.

When you select fit height, fit image, or fit width, the image scales under the limitation of Max Ratio.

**Rotation**

Type a degree to rotate the image at a specified angle.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) As you rotate the image, it is possible that part of the image exceeds the image area. Logi Report hides the part of the image that goes beyond the image area.

**Name**

Specify the name of the image. It maps to the HTML element attribute "name".

**Alternate Text**

Specify the alternate text of the image, which shows when the image cannot display.

**Max Ratio**

Specify the maximum scaling ratio up to which the image can scale. By default, the scaling ratio of the image is limitless.

**Width**

Specify the width of the area for displaying the image. Server enables this property when **Original Size** is **false**.

**Height**

Specify the height of the area for displaying the image. Studio enables this property when **Original Size** is **false**.

**Original Size**

Select **true** to show the image in its original size.

### Text Field

Select to display the data field as text field.

![Data Field Properties dialog box - Text Field Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420461715095/dbprpty_rndrtxtfld.gif)

**Type**

Select **Standard** to render the field as a normal text field or select **Password** to render the field as a password box.

**Name**

Specify the name of the text field. It maps to the HTML element attribute "name".

**Title**

Specify the tip information which shows when you hover over the text field. It maps to the HTML element attribute "title".

**Character Width**

Specify the width of the text field, measured in the number of characters.

**Max Length**

Specify the maximum number of the characters that you can type in the text field.

**Read Only**

Select **true** to make the text field read-only.

**Disabled**

Select **true** to disable the text field.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) When displaying a data field as text field, the value you have specified for the field's font property **Vertical Alignment** no longer takes effect, because the HTML standard does not support the property.

### Text Area

Select to display the data field as text area.

![Data Field Properties dialog box - Text Area Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420453657879/dbprpty_rndrtxtarea.gif)

**Name**

Specify the name of the text area. It maps to the HTML element attribute "name".

**Title**

Specify the tip information which shows when you hover over the text area. It maps to the HTML element attribute "title".

**Wrap**

Select **true** to wrap text to the width of the text area.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) When displaying a data field as text area, the value you have specified for the field's font property **Vertical Alignment** no longer takes effect, because the HTML standard does not support the property.

**Read Only**

Select **true** to make the text area read-only.

**Disabled**

Select **true** to disable the text area.

### Checkbox

Select to display the data field as checkbox.

![Data Field Properties dialog box - Checkbox Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420447335319/dbprpty_rndrchkbx.gif)

**Name**

Specify the name of the checkbox. It maps to the HTML element attribute "name".

**Title**

Specify the tip information which shows when you hover over the checkbox. It maps to the HTML element attribute "title".

**Disabled**

Select **true** to disable the checkbox.

**Initially Checked**

Select **true** to select the checkbox by default.

### Radio Button

Select to display the data field as radio button.

![Data Field Properties dialog box - Radio Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420447335575/dbprpty_rndrradio.gif)

**Name**

Specify the name of the radio button. It maps to the HTML element attribute "name".

**Title**

Specify the tip information which shows when you hover over the radio button. It maps to the HTML element attribute "title".

**Disabled**

Select **true** to disable the radio button.

**Initially Checked**

Select **true** to select the radio button by default.

### Image Button

Select to display the data field as image button.

![Data Field Properties dialog box - Image Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420447335831/dbprpty_rndrimgbtn.gif)

**Scaling Mode**

Server enables this property when **Original Size** is **false**.

* **actual size**  
  Select to show the image in its actual size. If the display area is smaller than the image, Server hides part of the image.
* **fit image**Select if you want the image to fill the display area and keep the original perspective ratio under the limitation of Max Ratio.
* **fit width**Select if you want the image to fit the display area width under the limitation of Max Ratio.
* **fit height**Select if you want the image to fit the display area height, under the limitation of Max Ratio.
* **customize**Select if you want to specify the width and height of the image in the size fields.

When you select fit height, fit image, or fit width, the image scales under the limitation of Max Ratio.

**Name**

Specify the name of the image button. It maps to the HTML element attribute "name".

**Alternate text**

Specify the alternate text of the image, which shows when the image cannot display.

**Title**

Specify the tip information which shows when you hover over the image button. It maps to the HTML element attribute "title".

**Max Ratio**

Specify the maximum scaling ratio up to which the image can scale. By default, the scaling ratio of the image is limitless.

**Width**

Specify the width of the area for displaying the image. Server enables this property when **Original Size** is **false**.

**Height**

Specify the height of the area for displaying the image. Server enables this property when **Original Size** is **false**.

**Original Size**

Select **true** to show the image in its original size.

**Disabled**

Select **true** to disable the image button.

### Button

Select to display the data field as button.

![Data Field Properties dialog box - Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420447336087/dbprpty_rndrbtn.gif)

**Name**

Specify the name of the button. It maps to the HTML element attribute "name".

**Title**

Specify the tip information which shows when you hover over the button. It maps to the HTML element attribute "title".

**Value**

Specify the text you want to display on the button. To make this property work, you need to set **From Database** to **false**.

**From Database**

Select **true** to use the current DBField value as the display text on the button. Select **false** and you can use the **Value** property to specify the display text.

**Disabled**

Select **true** to disable the button.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) When displaying a data field as button, the value you have specified for the field's font property **Vertical Alignment** no longer takes effect, because the HTML standard does not support the property.

### Submit

Select to display the data field as submit button.

![Data Field Properties dialog box - Submit Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420447339543/dbprpty_rndrsbmt.gif)

**Name**

Specify the name of the submit button. It maps to the HTML element attribute "name".

**Title**

Specify the tip information which shows when you hover over the submit button. It maps to the HTML element attribute "title".

**Value**

Specify the text you want to display on the submit button. To make this property work, you need to set **From Database** to **false**.

**From Database**

Select **true** if you want to use the current DBField value as the display text on the submit button. Select **false** and you can use the Value property to specify the display text.

**Disabled**

Select **true** to disable the submit button.

### Reset

Select to display the data field as reset button.

![Data Field Properties dialog box - Reset Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420447340311/dbprpty_rndrrest.gif)

**Name**

Specify the name of the reset button. It maps to the HTML element attribute "name".

**Title**

Specify the tip information which shows when you hover over the reset button. It maps to the HTML element attribute "title".

**Value**

Specify the text you want to display on the reset button. To make this property work, you need to set **From Database** to **false**.

**From Database**

Select **true** if you want to use the current DBField value as the display text on the reset button. Select **false** and you can use the Value property to specify the display text.

**Disabled**

Select **true** to disable the reset button.

### Hidden

Select to render the data field as hidden field.

![Data Field Properties dialog box - Hidden Field Display Type](https://devnet.logianalytics.com/hc/article_attachments/4420461716503/dbprpty_rndrhdn.gif)

**Name**

Specify the name of the hidden field. It maps to the HTML element attribute "name".

**Value**

Specify the value of the hidden field.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683619223-Customized-Page-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690502295-Edit-Additional-Values-Dialog-Box-Properties)
