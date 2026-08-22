---
title: "Display Type Dialog"
id: 1500009565002
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog
updated_at: 2021-07-24T05:55:30Z
---

# Display Type Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586261-Display-Attributes-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565162-Download-Customized-Control-Dialog)

# Display Type Dialog

The Display Type dialog appears when you right-click a field and select Display Type from the shortcut menu. It helps you to define the [display type](https://devnet.logianalytics.com/hc/en-us/articles/1500009563422-Changing-the-Display-Type-of-a-Label) of the field, which can be one of the following:

* [Text](#Text)
* [Image](#Image)
* [Barcode](#Barcode)
* [Rank](#Rank)
* [Text Field](#TextField)
* [Hidden Field](#HiddenField)
* [Text Area](#TextArea)
* [Checkbox](#Checkbox)
* [Radio Button](#RadioButton)
* [Image Button](#ImageButton)
* [Button](#Button)
* [List](#List)
* [Drop-down List](#DropdownList)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

**Note:** The two display types - List and Drop-down List are only available when the field is a parameter field.

## Text

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Dispay Type dialog - Text](https://devnet.logianalytics.com/hc/article_attachments/4404893930391/dsplytp_txt.gif)

**Tool Tip**

Specifies the tooltip of the text, which will be shown when you hover the mouse over the text in HTML report result or at runtime. You can also [use a formula to control the tooltip](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

* **Auto**  
   When the Auto option is checked, the tooltip cannot be customized. Then at runtime or in HTML report result, when the text cannot be fully displayed, you can hover the mouse over the text to get its full content in the tooltip.

**Web Behaviors**

Specifies some web behaviors to the text.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new web behavior line.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected web behavior.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected web behavior up a step.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected web behavior down a step.
* **Events**  
   Specifies the trigger event.
* **Actions**  
   Specifies the web action you want the event to trigger.
  + ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif)  
     Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog to bind some web action to the event.

## Image

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Image](https://devnet.logianalytics.com/hc/article_attachments/4404889370647/dsplytp_img.gif)

**Source**

Specifies where the image you want to use comes from.

* **From URL**  
   Specifies to use an image from a URL. You can select the Browse button to specify the path or input the URL directly in the text field. These types of images are supported: GIF, BMP, JPG, and PNG.
* **From DBField**  
   For a DBField, formula, or a summary, you can check this option to make the value of the DBField/formula/summary the image source.
  + **Decode Type**  
     Specifies the type for decoding the image. It can be GIF or JPG, BMP, PNG, AUTODETECT (this is to detect an image type saved in the database automatically).

**Name**

Specifies the name of the image. You can input the name directly in the text field or [use a formula to control it](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Alternate Text**

Specifies the alternate text of the image, which will be shown when the image cannot be displayed.

**Tool Tip**

Specifies the tooltip of the image, which will be shown when you hover the mouse over the image in HTML report result or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Size**

Specifies the size of the image.

* **Original Size**  
   Specifies whether to use the original size of the image. This will give you the best results when the image is already the size you want to display and is more efficient than scaling the image every time the report runs.
* **Constrain Proportions**  
   If checked, when you set the display width or height of the image, the other will be adjusted accordingly based on the image's width-to-height ratio. Available only when the Original Size option is unchecked.
* **Width**  
   Specifies the new display width of the image. Available only when the Original Size option is unchecked.
* **Height**  
   Specifies the new display height of the image. Available only when the Original Size option is unchecked.
* **Scaling Mode**  
   Specifies the scaling mode of the image. Available only when the Original Size option is unchecked. There are five types available for you:
  + **actual size**   
     If selected, the image will be shown in its actual size.
  + **fit image**  
     If selected, the image will be scaled to be wholly shown.
  + **fit width**  
     If selected, the image will be scaled to fit the width of the image viewer.
  + **fit height**  
     If selected, the image will be scaled to fit the height of the image viewer.
  + **customize**  
     If selected, the image will be scaled according to the width and height that you specify in the Width and Height fields.
* **Max Ratio**  
   Specifies the maximum scaling ratio of the image. By default the scaling ratio of the image is not limited. If it is set to any value greater than 0, the actual scaling ratio will be less than or equal to it.
* **Rotation**  
   Specifies the angle, at which to rotate the image, in degrees. The following is the meaning of different values:
  + 0 - No rotation.
  + Positive value - Rotates the image clockwise.
  + Negative value - Rotates the image anticlockwise.

  **Note:** When rotating an image, the rectangle that holds the image maintains its original size, which may result in that the image exceeds the field border and therefore the parts that extend outside of the border will be cut off.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the image.

## Barcode

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Barcode](https://devnet.logianalytics.com/hc/article_attachments/4404889370903/dsplytp_brcd.gif)

**Symbology**

Specifies the type of the barcode. It could be UPC A/E, EAN 13/8, CODE 39, CODE 128, CODabar, and Code 128A/128B/128C.

**Tool Tip**

Specifies the tooltip of the barcode, which will be shown when you hover the mouse over the barcode in HTML report result or at runtime. You can also [use a formula to control the tooltip](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Scale Mode**

Specifies the unit for the values of Quiet Zone, Narrow Width, Supplement, Height and Ratio.

**Quiet Zone**

Specifies the space around the barcode.

**Default Message**

Specifies the default value for the barcode, which will be used for the barcode in design mode.

**Supplement**

Specifies the supplement for the barcode. The barcode types, Code 39, Code 128/128A/128B/128C and Codabar, don't have supplements.

**Use Default Massage**

If checked, the value you specify in the Default Message field will be used as the barcode value when you view the report result. Otherwise, the value will only be used in design mode.

**Enable Checking Digits**

Specifies whether to include check digits in the barcode.

**Display HR**

Specifies whether to display the barcode numbers together with the barcode. Enabled only for Code 39, Code 128/128A/128B/128C and Codabar.

**Size**

Specifies the size of the barcode.

* **Narrow Width**  
   Specifies the width between the barcode bars.
* **Ratio**  
   Specifies the width ratio of the thick bar to the thin bar in the CODE39/Codabar barcode. The Ratio box can have only 2 effective values, 2.0 and 3.0, any ratio values are not equal to 2.0 or 3.0 will be granted as 2.0. Enabled only for CODE39 and Codabar.
* **Height**  
   Specifies the height for the bars of the barcode.
* **Orientation**  
   Specifies the orientation for the barcode.

**Preview**

Displays the format of the selected symbology.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the barcode.

## Rank

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Rank](https://devnet.logianalytics.com/hc/article_attachments/4404893930647/dsplytp_rank.gif)

**Default Image for All Value Ranges**

Specifies the default image for all value ranges, which will be applied when the value of a field does not fall into any of the defined ranges. You can select the Browse button to specify the image path or input the path and file name of the image directly in the text field.

**Default Image Alternate Text**

Specifies the alternate text for the default image, which will be shown when the default image cannot be displayed.

**Default Tool Tip**

Specifies the tooltip of the default image, which will be shown when you hover the mouse over the image in HTML report result or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Default Image Rotation**

Specifies the default image's rotation angle, in degrees. The following is the meaning of different values:

* 0 - No rotation.
* Positive value - Rotates the image clockwise.
* Negative value - Rotates the image anticlockwise.

**Note:** When rotating an image, the rectangle that holds the image maintains its original size, which may result in that the image exceeds the field border and therefore the parts that extend outside of the border will be cut off.

**Value Range**

Specifies the value ranges.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new value range.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected value range.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected value range up a step.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected value range down a step.
* **Minimum (>=)**  
   Specifies the minimum value for this range.
* **Maximum (<)**  
   Specifies the maximum value for this range.
* **Image**  
   Specifies the image of this value range, then when a field's value falls into this range, this image will be displayed.
* **Alternate Text**  
   Specifies the alternate text for this value range's image, which will be shown when the image cannot be displayed.
* **Tool Tip**  
   Specifies the tooltip of this value range's image, which will be shown when you hover the mouse over the image when the report runs in HTML format or in Page Report Studio.
* **Rotation**  
   Specifies the rotation angle of this value range's image, in degrees.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the rank.

## Text Field

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Text Field](https://devnet.logianalytics.com/hc/article_attachments/4404889371159/dsplytp_txtfld.gif)

**Type**

Specifies the type of the text field.

* **Standard**  
   Specifies that the text field is a standard text field.
* **Password**  
   Specifies that the text field is a password text field, which means that the value input in the text field will be hidden using asterisks.

**Name**

Specifies the name of the text field.

**Value**

Specifies the value of the text field.

**Tool Tip**

Specifies the tooltip of the text field, which will be shown when you hover the mouse over the text field in HTML report result or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Display Width**

Specifies the display width of the text field.

**Max Length**

Specifies the maximum length of the string that is allowed in the text field.

**Read Only**

Specifies whether to make the field read-only to others.

**Disabled**

Specifies whether the text field is disabled or enabled.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the text field.

## Hidden Field

A hidden field is visible only in design mode. The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Hidden Field](https://devnet.logianalytics.com/hc/article_attachments/4404893930903/dsplytp_hidfld.gif)

**Name**

Specifies the name of the hidden field.

**Value**

Specifies the value of the hidden field.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the hidden field.

## Text Area

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Text Area](https://devnet.logianalytics.com/hc/article_attachments/4404893931159/dsplytp_txtarea.gif)

**Name**

Specifies the name of the text area.

**Value**

Specifies the value of the text area.

**Tool Tip**

Specifies the tooltip of the text area, which will be shown when you hover the mouse over the text area in HTML report result or at runtime.

**Display Width**

Specifies the display width of the text area.

**Number of Lines**

Specifies the number of lines that is allowed in the text area.

**Auto Wrap**

Specifies whether to wrap the text in the text area.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Read Only**

Specifies whether to make the text area read-only to others.

**Disabled**

Specifies whether the text area is disabled or enabled.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the text area.

## Checkbox

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404893931415/dsplytp_bx.gif)

**Name**

Specifies the name of checkbox.

**Value**

Specifies the value of the checkbox.

**Tool Tip**

Specifies the tooltip of the checkbox, which will be shown when you hover the mouse over the checkbox in HTML report result or at runtime.

**Initially Checked**

Specifies whether or not the checkbox is selected by default.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Disabled**

Specifies whether the checkbox is enabled or disabled.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the checkbox.

## Radio Button

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Radio Button](https://devnet.logianalytics.com/hc/article_attachments/4404889371415/dsplytp_rdbtn.gif)

**Name**

Specifies the name of radio button.

**Value**

Specifies the value of the radio button.

**Tool Tip**

Specifies the tooltip of the radio button, which will be shown when you hover the mouse over the radio button in HTML report result or at runtime.

**Initially Checked**

Specifies whether or not the radio button is selected by default.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Disabled**

Specifies whether the radio button is enabled or disabled.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the radio button.

## Image Button

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Image Button](https://devnet.logianalytics.com/hc/article_attachments/4404889371671/dsplytp_imgbtn.gif)

**Source**

Specifies where the image button you want to use comes from.

* **From URL**  
   Specifies to use an image from a URL. You can select the Browse button to specify the path or input the URL directly in the text field. These types of images are supported: GIF, BMP, JPG, and PNG.
* **From DBField**  
   For a DBField, formula, or a summary, you can check this option to make the value of the DBField/formula/summary the image source.
  + **Decode Type**  
     Specifies the type for decoding the image. It can be GIF or JPG, BITMAP, AUTODETECT (this is to detect an image type saved in the database automatically).

**Name**

Specifies the name of the image button.

**Value**

Specifies the value of the image button.

**Alternate Text**

Specifies the alternate text of the image, which will be shown when the image cannot be displayed.

**Tool Tip**

Specifies the tooltip of the image button, which will be shown when you hover the mouse over the image button in HTML report result or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Disabled**

Specifies whether the image button is disabled or enabled.

**Size**

Specifies the size of the image.

* **Original Size**  
   Specifies whether to use the original size of the image. This will give you the best results when the image is already the size you want to display and is more efficient than scaling the image every time the report runs.
* **Constrain Proportions**  
   If checked, when you set the width or height of the image, the other will be adjusted accordingly based on the image's width-to-height ratio. Available only when the Original Size option is unchecked.
* **Width**  
   Specifies the new display width of the image. Available only when the Original Size option is unchecked.
* **Height**  
   Specifies the new display height of the image. Available only when the Original Size option is unchecked.
* **Max Ratio**  
   Specifies the maximum scaling ratio of the image. By default the scaling ratio of the image is not limited. If it is set to any value greater than 0, the actual scaling ratio will be less than or equal to it.
* **Scaling Mode**  
   Specifies the scaling mode of the image. Available only when the Original Size option is unchecked. There are five types available for you:
  + **actual size**  
     If selected, the image will be shown in its actual size.
  + **fit image**  
     If selected, the image will be scaled to be wholly shown.
  + **fit width**  
     If selected, the image will be scaled to fit the width of the image viewer.
  + **fit height**  
     If selected, the image will be scaled to fit the height of the image viewer.
  + **customize**  
     If selected, the image will be scaled according to the width and height that you specify in the Width and Height fields.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the image button.

## Button

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - Button](https://devnet.logianalytics.com/hc/article_attachments/4404893931671/dsplytp_btn.gif)

**Name**

Specifies the name of the button.

**Value**

Specifies the value of the button.

**Tool Tip**

Specifies the tooltip of the button, which will be shown when you hover the mouse over the button in HTML report result or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Action**

Specifies the default action that will happen when the button is selected.

* **None**  
   Specifies that no default action happens when the button is selected.
* **Submit Form**  
   Specifies that the default action of the button is to submit a form.
* **Reset Form**  
   Specifies that the default action of the button is to reset a form.

**Disabled**

Specifies whether the button is disabled or enabled.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the button.

## List

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![Display Type dialog - List](https://devnet.logianalytics.com/hc/article_attachments/4404893931927/dsplytp_lst.gif)

**Name**

Specifies the name of the list.

**Tool Tip**

Specifies the tooltip of the list, which will be shown when you hover the mouse over the list in HTML report result or at runtime.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a new item in the list.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected item.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected item up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected item down a step.

**Item Label**

Specifies the display text or format of the item value. Select the desired one from the drop-down list.

**Value**

Specifies the item value.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif)  
   Opens the [Insert Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009587581-Insert-Fields-Dialog) dialog to add field to control the value.

**Selected**

Specifies the value that will be selected in the list by default.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Allow Multiple Selections**

Specifies whether to allow selecting multiple items in the list at the same time.

**Use Runtime Value**

When changing the display type of a parameter to list, you can check this option to use the runtime value as the selected value of the list.

**Disabled**

Specifies whether the list is disabled or enabled.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the list.

## Drop-down List

The following are details about options for this display type. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404889371927/dsplytp_drpdwnlst.gif)

**Name**

Specifies the name of the drop-down list.

**Tool Tip**

Specifies the tooltip of the drop-down list, which will be shown when you hover the mouse over the drop-down list in HTML report result or at runtime.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a new item in the drop-down list.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected item.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected item up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected item down a step.

**Item Label**

Specifies the display text or format of the item value. Select the desired one from the drop-down list.

**Value**

Specifies the item value.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif)  
   Opens the [Insert Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009587581-Insert-Fields-Dialog) dialog to add field to control the value.

**Selected**

Specifies the value that will be selected in the drop-down list by default.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Use Runtime Value**

When changing the display type of a parameter to drop-down list, you can check this option to use the runtime value as the selected value of the drop-down list.

**Disabled**

Specifies whether the drop-down list is disabled or enabled.

**[Web Behaviors](#Behaviors)**

Specifies some web behaviors to the drop-down list.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586261-Display-Attributes-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565162-Download-Customized-Control-Dialog)
