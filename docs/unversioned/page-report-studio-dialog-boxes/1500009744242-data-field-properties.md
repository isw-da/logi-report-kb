---
title: "Data Field Properties"
id: 1500009744242
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744242-Data-Field-Properties
updated_at: 2021-07-24T00:49:19Z
---

# Data Field Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744222-Customized-Page-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772081-Edit-Additional-Values-Dialog-Box-Properties)

# Data Field Properties

You can use the Data Field Properties dialog box to edit the properties of a DBField. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Font Tab Properties](#Font)
* [Border Tab Properties](#Border)
* [Others Tab Properties](#Others)
* [Display Tab Properties](#Render)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows general information of the data field.

![Data Field Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880542999/dbprpty_gnrl.gif)

**Name**

Specifies the display name of the data field.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Format**

Specifies the data format of the data field.

**Auto Scale in Number**

Specifies whether to
automatically scale the values that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report uses the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report uses scientific notation to scale the values.

The value **auto** means that the setting follows that of the parent data container. When you set the property to **true**, the specified format will apply to the integer part of the values after being scaled; but if the specified format conflicts with the Number data type, Logi Report will ignore the Auto Scale in Number setting.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

**X**

Specifies the X coordinate of the data field.

**Y**

Specifies the Y coordinate of the data field.

**Width**

Specifies the width of the data field.

**Height**

Specifies the height of the data field.

**Top Padding**

Specifies the space between the text of the field and its top border.

**Bottom Padding**

Specifies the space between the text of the field and its bottom border.

**Left Padding**

Specifies the space between the text of the field and its left border.

**Right Padding**

Specifies the space between the text of the field and its right border.

**Background**

Specifies the background color of the data field.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

**Foreground**

Specifies the foreground color of the data field.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

## Font Tab Properties

This tab shows the font-related information of the data field.

![Data Field Properties dialog - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404880543511/dbprpty_font.gif)

**Font**

Specifies the font face of the text.

**Size**

Specifies the font size of the text.

**Horizontal Alignment**

Specifies the horizontal alignment mode of the text in the data field.

**Vertical Alignment**

Specifies the vertical alignment mode of the text in the data field.

**Bold**

Specifies whether to make the text bold.

**Underline**

Specifies whether to underline the text.

**Strikethrough**

Specifies whether to attach a strikeout line to the text.

**Italic**

Specifies whether to make the text italic.

**Autofit**

Specifies whether to automatically adjust the width of the data field according to the maximum length of the contents.

**Word Wrap**

Specifies whether to wrap the text to the data field width.

**Ignore HTML Tag**

By default, Logi Report Engine ignores the HTML tag elements that are included in the values of the data field so they display exactly as what they are in the report. Set the option to false if you want Logi Report Engine to transfer the HTML tag elements to the web browser so they are translated into HTML by the web browser. The setting also applies in the HTML output of the report.

## Border Tab Properties

This tab shows information about borders of the data field.

![Data Field Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880543895/dbprpty_border.gif)

**Color**

Specifies the border color. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the border transparent, type Transparent in the text box.

**Width**

Specifies the border width in inches.

**Top Line**

Specifies the style of the top border line.

**Bottom Line**

Specifies the style of the bottom border line.

**Left Line**

Specifies the style of the left border line.

**Right Line**

Specifies the style of the right border line.

**Shadow**

Specifies whether the borders will have a shadow effect or not.

**Shadow Color**

Specifies the color of the border shadow. To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB.

## Others Tab Properties

You can view and configure the miscellaneous settings.

![Data Field Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404880544407/dbprpty_other.gif)

**TOC Anchor**

Specifies whether to add the node that represents the data field to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the data field in the report result when Server returns no record to its parent data component.

**Suppress If Null**

If true and the field value is null, Server will not display the data field.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

**Scope**

Available only for data fields in a table or crosstab. It is a representation of the standard HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information.

* **Row** - The current cell provides header information for the rest of the row that contains it.
* **Column** - The current cell provides header information for the rest of the column that contains it.
* **None** - Server will not generate the scope attribute when exporting to HTML.

**Logic Column**

Specifies whether to show the data field in the next visible table cell in the same row when you have hidden the column that holds the field.

## Display Tab Properties

You can use this tab to modify the display type of the data field as one of the following: Text, Barcode, Image, Text Field, Text Area, check box, Radio Button, Image Button, Button, Submit, Reset, and Hidden. What you need to do is select the display type from the **Display Type** drop-down list, and then set the corresponding options.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)For the display type **Text**, there is no option available. For a field that is displayed as rank, you cannot change its display type.

### Barcode

Specifies to display the data field as barcode.

![Data Field Properties dialog - Barcode Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404880545047/dbprpty_rndrbrcd.gif)

**Symbology**

Specifies the barcode type.

**Scale Mode**

Specifies the unit for the values of the quiet zone, narrow width, supplement, height, and ratio.

**Quiet Zone**

Specifies the space around the barcode.

**Narrow Width**

Specifies the width of the narrowest barcode bar.

**Supplement**

Specifies the supplement of the barcode.

**Height**

Specifies the height of the barcode bars.

**Message**

Specifies the default value of the barcode.

**Ratio**

Specifies the width ratio of the thick bar to the thin bar.

**Orientation**

Specifies the rotation angle in degrees.

**Use Default Message**

Specifies whether to use the Message value as the barcode value when you view the report result.

**Enable Checking Digits**

Specifies whether to include check digits in the barcode.

**Display HR**

Specifies whether to display the characters together with the barcode bars.

### Image

Specifies to display the data field as image.

![Data Field Properties dialog - Image Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404885595287/dbprpty_rndrimg.gif)

**Scaling Mode**

Studio enables this option when **Original Size** is false.

* **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
* **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
* **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
* **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
* **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.

When you select fit height, fit image, or fit width, the image scales under the limitation of Max Ratio.

**Rotation**

Type a degree to rotate the image at a specified angle.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)As you rotate the image, it is possible that parts of the image exceeds the image area. Logi Report does not display the parts of the image that go beyond the image area.

**Name**

Specifies the name of the image. It is mapped to the HTML element attribute "name".

**Alternate Text**

Specifies the alternate text of the image, which will be shown when the image cannot be displayed.

**Max Ratio**

Specifies the maximum scaling ratio up to which the image can be scaled. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio will be less than or equal to it.

**Width**

Specifies the width of the area for displaying the image. Studio enables this option when **Original Size** is false.

**Height**

Specifies the height of the area for displaying the image. Studio enables this option when **Original Size** is false.

**Original Size**

Specifies whether to show the image in its original size.

### Text Field

Specifies to display the data field as text field.

![Data Field Properties dialog - Text Field Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404885595543/dbprpty_rndrtxtfld.gif)

**Type**

Specifies whether to render the field as a normal text field or to a password box.

**Name**

Specifies the name of the text field. It is mapped to the HTML element attribute "name".

**Title**

Specifies the tip information which will be shown when you hover the mouse over the text field. It is mapped to the HTML element attribute "title".

**Character Width**

Specifies the width of the text field measured in the number of characters.

**Max Length**

Specifies the maximum number of the characters that can be input into the text field.

**Read Only**

Specifies whether to make the text field read-only.

**Disabled**

Specifies whether to make the text field disabled.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When displaying a data field as text field, the value you have specified for the field's font property Vertical Alignment no longer takes effect. This is because the property is not supported in HTML standards.

### Text Area

Specifies to display the data field as text area.

![Data Field Properties dialog - Text Area Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404885595799/dbprpty_rndrtxtarea.gif)

**Name**

Specifies the name of the text area. It is mapped to the HTML element attribute "name".

**Title**

Specifies the tip information which will be shown when you hover the mouse over the text area. It is mapped to the HTML element attribute "title".

**Wrap**

Specifies whether to wrap text to the width of the text area.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When displaying a data field as text area, the value you have specified for the field's font property Vertical Alignment no longer takes effect. This is because the property is not supported in HTML standards.

**Read Only**

Specifies whether to make the text area read-only.

**Disabled**

Specifies whether to make the text area disabled.

### Checkbox

Specifies to display the data field as check box.

![Data Field Properties dialog - Checkbox Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404880546199/dbprpty_rndrchkbx.gif)

**Name**

Specifies the name of the check box. It is mapped to the HTML element attribute "name".

**Title**

Specifies the tip information which will be shown when you hover the mouse over the check box. It is mapped to the HTML element attribute "title".

**Disabled**

Specifies whether to make the check box disabled.

**Initially Checked**

Specifies whether the check box is selected by default.

### Radio Button

Specifies to display the data field as radio button.

![Data Field Properties dialog - Radio Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404880546583/dbprpty_rndrradio.gif)

**Name**

Specifies the name of the radio button. It is mapped to the HTML element attribute "name".

**Title**

Specifies the tip information which will be shown when you hover the mouse over the radio button. It is mapped to the HTML element attribute "title".

**Disabled**

Specifies whether to make the radio button disabled.

**Initially Checked**

Specifies whether the radio button is selected by default.

### Image Button

Specifies to display the data field as image button.

![Data Field Properties dialog - Image Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404885596311/dbprpty_rndrimgbtn.gif)

**Scaling Mode**

Logi Report enables this option when **Original Size** is false.

* **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
* **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
* **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
* **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
* **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.

When you select fit height, fit image, or fit width, the image scales under the limitation of Max Ratio.

**Name**

Specifies the name of the image button. It is mapped to the HTML element attribute "name".

**Alternate text**

Specifies the alternate text of the image, which will be shown when the image cannot be displayed.

**Title**

Specifies the tip information which will be shown when you hover the mouse over the image button. It is mapped to the HTML element attribute "title".

**Max Ratio**

Specifies the maximum scaling ratio up to which the image can be scaled. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio will be less than or equal to it.

**Width**

Specifies the width of the area for displaying the image. Studio enables this option when **Original Size** is false.

**Height**

Specifies the height of the area for displaying the image. Studio enables this option when **Original Size** is false.

**Original Size**

Specifies whether to show the image in its original size.

**Disabled**

Specifies whether to make the image button disabled.

### Button

Specifies to display the data field as button.

![Data Field Properties dialog - Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404880546967/dbprpty_rndrbtn.gif)

**Name**

Specifies the name of the button. It is mapped to the HTML element attribute "name".

**Title**

Specifies the tip information which will be shown when you hover the mouse over the button. It is mapped to the HTML element attribute "title".

**Value**

Specifies the text displayed on the button by directly typing or using a formula. To make this property work, you need to set From Database to false.

**From Database**

If true, the current DBField value will be kept as the display text on the button. If false, you can use the Value property to specify the display text.

**Disabled**

Specifies whether to make the button disabled.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When displaying a data field as button, the value you have specified for the field's font property Vertical Alignment no longer takes effect. This is because the property is not supported in HTML standards.

### Submit

Specifies to display the data field as submit button.

![Data Field Properties dialog - Submit Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404880547351/dbprpty_rndrsbmt.gif)

**Name**

Specifies the name of the submit button. It is mapped to the HTML element attribute "name".

**Title**

Specifies the tip information which will be shown when you hover the mouse over the submit button. It is mapped to the HTML element attribute "title".

**Value**

Specifies the text displayed on the submit button by directly typing or using a formula. To make this property work, you need to set From Database to false.

**From Database**

If true, the current DBField value will be kept as the display text on the submit button. If false, you can use the Value property to specify the display text.

**Disabled**

Specifies whether to make the submit button disabled.

### Reset

Specifies to display the data field as reset button.

![Data Field Properties dialog - Reset Button Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404880548119/dbprpty_rndrrest.gif)

**Name**

Specifies the name of the reset button. It is mapped to the HTML element attribute "name".

**Title**

Specifies the tip information which will be shown when you hover the mouse over the reset button. It is mapped to the HTML element attribute "title".

**Value**

Specifies the text displayed on the reset button by directly typing or using a formula. To make this property work, you need to set From Database to false.

**From Database**

If true, the current DBField value will be kept as the display text on the reset button. If false, you can use the Value property to specify the display text.

**Disabled**

Specifies whether to make the reset button disabled.

### Hidden

Specifies to render the data field as hidden field.

![Data Field Properties dialog - Hidden Field Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404885596823/dbprpty_rndrhdn.gif)

**Name**

Specifies the name of the hidden field. It is mapped to the HTML element attribute "name".

**Value**

Specifies the value of the hidden field by directly typing or using a formula.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744222-Customized-Page-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009772081-Edit-Additional-Values-Dialog-Box-Properties)
