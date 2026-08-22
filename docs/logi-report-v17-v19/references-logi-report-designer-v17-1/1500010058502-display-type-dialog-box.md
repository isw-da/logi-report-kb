---
title: "Display Type Dialog Box"
id: 1500010058502
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058502-Display-Type-Dialog-Box
updated_at: 2021-11-10T06:50:54Z
---

# Display Type Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058482-Display-Attributes-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058662-Download-Customized-Control-Dialog-Box)

# Display Type Dialog Box

You can use the Display Type dialog box to [define the display type of an object](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports) in a report. This topic describes the options in the dialog box.

Designer displays the Display Type dialog box when you right-click a label, data field, special field, or basic web control in a report and select Display Type from the shortcut menu.

You can change the display type of an object to one of the following depending on the type of the report containing the object and the type of the object itself:

* [Text](#Text)
* [Image](#Image)
* [Barcode](#Barcode)
* [QR Code](#QRCode)
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

You see these button for all the display types.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Designer displays the two display types: List and Drop-down List in the Display Type dialog box, only when you use the dialog box for defining the display type of a parameter field, or a List or Drop-down List web control.

## Text Display Type

You see the following options for the Text display type:

![Dispay Type dialog box - Text](https://devnet.logianalytics.com/hc/article_attachments/4404848416791/dsplytp_txt.gif)

**Tool Tip**

Specify the tool tip of the text, which displays when the report users hover the mouse over the text in the HTML output of the report or at runtime.

* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
  Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value as the tool tip.
* **Auto**  
  Designer selects the option by default, which means using the full content of the text in the tool tip. Clear the option if you want to customize the tool tip.

**Web Behaviors**

You can specify the web behaviors that you want to bind to the text in this panel.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to add a new web behavior line.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified web behavior.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
  Select to move the specified web behavior higher in the list. When an event bound with more than one action happens at runtime, Logi Report Engine triggers the upper action first.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified web behavior lower in the list.
* **Events**  
  The column shows the trigger events that you select for the web behaviors.
* **Actions**  
  The column shows the web actions that you specify to trigger when the events occur at runtime.
  + ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif)**Ellipsis button**  
    Select to open the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box) to bind a web action to the specified event.

## Image Display Type

You see the following options for the Image display type:

![Display Type dialog box - Image](https://devnet.logianalytics.com/hc/article_attachments/4404848417303/dsplytp_img.gif)

**Source**

Specify where the image you want to use comes from.

* **From URL**  
  Select to use an image from a URL. You can select the Browse button to specify the path or type the URL in the text box. You can use these types of images: GIF, BMP, JPG, and PNG.
* **From DBField**  
  Designer enables the option for a DBField, formula, or summary. Select it to make the current data field the image source.
  + **Decode Type**  
    The drop-down list contains the types that you can apply for decoding the image: GIF or JPG, Bitmap, SVG, and Auto Detect (this is to detect an image type saved in the database automatically). Select the type that you want to use.
  + **Data URI Scheme**  
    Select if you want to parse the image using the data URI scheme.

**Name**

Specify the name of the image.

**Alternate Text**

Specify the alternate text of the image, which shows when the image cannot display.

**Tool Tip**

Specify the tool tip of the image, which displays when the report users hover the mouse over the image in the HTML output of the report or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Size**

You can specify the size of the image in this box. Designer disables the options in the box when you select From DBField as the image source and SVG as Decode Type.

* **Original Size**  
  Select to use the original size of the image. To use customized size for the image, clear the option and Designer enables the following options:
  + **Constrain Proportions**  
    If you select the option, when you set the width or height of the area for displaying the image, Designer adjusts the other accordingly based on the specified width-to-height ratio.
  + **Width**  
    Specify the width of the area for displaying the image.
  + **Height**  
    Specify the height of the area for displaying the image.
  + **Scaling Mode**  
    Select the scaling mode of the image.
    - **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
    - **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
    - **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
    - **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
    - **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.
* **Max Ratio**  
  Specify the maximum scaling ratio up to which Designer can scale the image. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio is less than or equal to it.
* **Rotation**  
  Specify the angle, at which to rotate the image, in degrees. The following is the meaning of different values:
  + 0 means no rotation.
  + Positive value means to rotate the image clockwise.
  + Negative value means to rotate the image anticlockwise.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the image in this panel.

## Barcode Display Type

You see the following options for the Barcode display type:

![Display Type dialog box - Barcode](https://devnet.logianalytics.com/hc/article_attachments/4404848417559/dsplytp_brcd.gif)

**Symbology**

Select the type of the barcode: UPC A, UPC E, EAN 13, EAN 8, CODE 39, CODE 128, Codabar, Code 128A, Code 128B, or Code 128C.

**Tool Tip**

Specify the tool tip of the barcode, which displays when the report users hover the mouse over the barcode in the HTML output of the report or at runtime.

* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)  
  Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value as the tool tip.

**Scale Mode**

Select the unit for the values of Quiet Zone, Narrow Width, Supplement, Height, and Ratio.

**Quiet Zone**

Specify the space around the barcode.

**Default Message**

Specify the default value for the barcode, which Designer applies for the barcode in design mode.

**Supplement**

Specify the supplement for the barcode. The barcode types, Code 39, Code 128, Code 128A, Code 128B, Code 128C, and Codabar, don't have supplements.

**Use Default Massage**

Select to use the value that you specify in the Default Message text box as the barcode value when you view the report result; otherwise, Designer only applies the value in design mode.

**Enable Checking Digits**

Select to include check digits in the barcode.

**Display HR**

Designer enables this option for the following barcode types: Code 39, Code 128, Code 128A, Code 128B, Code 128C, and Codabar. Select it to display the barcode numbers together with the barcode.

**Enable Length Optimization**

Designer displays the option for the barcode type Code 128 only. Select it to enable optimizing the length of the barcode in the report result.

**Size**

You can specify the size of the barcode in this box.

* **Narrow Width**  
  Specify the width between the barcode bars.
* **Ratio**  
  Designer enables this option only for the CODE 39 and Codabar barcode types. Use it to specify the width ratio of the thick bar to the thin bar in the barcode. You can set the ratio to one of the following two effective values only: 2.0 or 3.0. Designer regards any ratio values that are not equal to 2.0 or 3.0 as 2.0.
* **Height**  
  Specify the height for the bars of the barcode.
* **Orientation**  
  Specify the orientation for the barcode.

**Preview**

The box displays the format of the selected symbology.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the barcode in this panel.

## QR Code Display Type

You see the following options for the QR Code display type:

![Dispay Type dialog box - QR Code](https://devnet.logianalytics.com/hc/article_attachments/4404856836887/dsplytp_qrcd.gif)

**Margin**

Specify the margin between the image in the middle of the QR Code and the border of the QR Code.

**Error Correction Level**

Select the level of error correction for the QR Code: L, M, Q, or H.

**Default Message**

Specify the default value for the QR Code.

**Use Default Massage**

Select to generate the QR Code using the default value.

**Preview**

The box displays a preview of the QR Code.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the QR Code in this panel.

## Rank Display Type

You see the following options for the Rank display type:

![Display Type dialog box - Rank](https://devnet.logianalytics.com/hc/article_attachments/4404856837143/dsplytp_rank.gif)

**Default Image for All Value Ranges**

Specify the default image for all value ranges, which Designer applies when the value of a field does not fall into any of the defined ranges. You can select the Browse button to specify the image path or type the path and file name of the image in the text box.

**Default Image Alternate Text**

Specify the alternate text for the default image, which shows when the default image cannot display.

**Default Tool Tip**

Specify the tool tip of the default image, which displays when the report users hover the mouse over the image in the HTML output of the report or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Default Image Rotation**

Specify the default image's rotation angle, in degrees. The following is the meaning of different values:

* 0 means no rotation.
* Positive value means to rotate the image clockwise.
* Negative value means to rotate the image anticlockwise.

**Value Range**

You can specify the value ranges for the rank in this box.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to add a new value range.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified value range.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
  Select to move the specified value range higher in the list.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified value range lower in the list.
* **Minimum (>=)**  
  The column shows the minimum values that you specify for the ranges.
* **Maximum (<)**  
  The column shows the maximum values that you specify for the ranges.
* **Image**  
  The column shows the images that you specify for the value ranges, which display when the field's values fall into the ranges.
* **Alternate Text**  
  The column shows the alternate text that you specify for the images of the value ranges, which shows when the images cannot display.
* **Tool Tip**  
  The column shows the tool tips that you specify for the images of the value ranges, which display when the report users hover the mouse over the images in the HTML output of the report or in Page Report Studio.
* **Rotation**  
  The column shows the rotation angles that you specify for the images of the value ranges, in degrees.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the rank in this panel.

## Text Field Display Type

You see the following options for the Text Field display type:

![Display Type dialog box - Text Field](https://devnet.logianalytics.com/hc/article_attachments/4404848591511/dsplytp_txtfld.gif)

**Type**

Specify the type of the text field.

* **Standard**  
  Select to display the text field as a standard text field.
* **Password**  
  Select to display the text field as a password text field, which means that the value specified in the text field is hidden using asterisks.

**Name**

Specify the name of the text field.

**Value**

Select the value of the text field.

**Tool Tip**

Specify the tool tip of the text field, which displays when the report users hover the mouse over the text field in the HTML output of the report or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Display Width**

Specify the display width of the text field.

**Max Length**

Specify the maximum length of the string that is allowed in the text field.

**Read Only**

Select to make the field read-only to others.

**Disabled**

Select if you want to disable the text field.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the text field in this panel.

## Hidden Field Display Type

You see the following options for the Hidden Field display type:

![Display Type dialog box - Hidden Field](https://devnet.logianalytics.com/hc/article_attachments/4404856982551/dsplytp_hidfld.gif)

**Name**

Specify the name of the hidden field.

**Value**

Select the value of the hidden field.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the hidden field in this panel.

## Text Area Display Type

You see the following options for the Text Area display type:

![Display Type dialog box - Text Area](https://devnet.logianalytics.com/hc/article_attachments/4404856982807/dsplytp_txtarea.gif)

**Name**

Specify the name of the text area.

**Value**

Select the value of the text area.

**Tool Tip**

Specify the tool tip of the text area, which displays when the report users hover the mouse over the text area in the HTML output of the report or at runtime.

**Display Width**

Specify the display width of the text area.

**Number of Lines**

Specify the number of lines that is allowed in the text area.

**Auto Wrap**

Specify whether to wrap the text in the text area.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Read Only**

Select to make the text area read-only to others.

**Disabled**

Select if you want to disable the text area.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the text area in this panel.

## Checkbox Display Type

You see the following options for the Checkbox display type:

![Display Type dialog box - Checkbox](https://devnet.logianalytics.com/hc/article_attachments/4404848592151/dsplytp_bx.gif)

**Name**

Specify the name of checkbox.

**Value**

Select the value of the checkbox.

**Tool Tip**

Specify the tool tip of the checkbox, which displays when the report users hover the mouse over the checkbox in the HTML output of the report or at runtime.

**Initially Checked**

Specify whether or not the checkbox is selected by default.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Disabled**

Select if you want to disable the checkbox.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the checkbox in this panel.

## Radio Button Display Type

You see the following options for the Radio Button display type:

![Display Type dialog box - Radio Button](https://devnet.logianalytics.com/hc/article_attachments/4404848592407/dsplytp_rdbtn.gif)

**Name**

Specify the name of radio button.

**Value**

Select the value of the radio button.

**Tool Tip**

Specify the tool tip of the radio button, which displays when the report users hover the mouse over the radio button in the HTML output of the report or at runtime.

**Initially Checked**

Specify whether or not the radio button is selected by default.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Disabled**

Select if you want to disable the radio button.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the radio button in this panel.

## Image Button Display Type

You see the following options for the Image Button display type:

![Display Type dialog box - Image Button](https://devnet.logianalytics.com/hc/article_attachments/4404856983447/dsplytp_imgbtn.gif)

**Source**

Specify where the image you want to use for the image button comes from.

* **From URL**  
  Select to use an image from a URL. You can select the Browse button to specify the path or type the URL in the text box. You can use these types of images: GIF, BMP, JPG, and PNG.
* **From DBField**  
  Designer enables the option for a DBField, formula, or summary. Select it to make the current data field the image source.
  + **Decode Type**  
    The drop-down list contains the types that you can apply for decoding the image: GIF or JPG, BITMAP, SVG, and AUTODETECT (this is to detect an image type saved in the database automatically). Select the type that you want to use.

**Name**

Specify the name of the image button.

**Value**

Select the value of the image button.

**Alternate Text**

Specify the alternate text of the image, which shows when the image cannot display.

**Tool Tip**

Specify the tool tip of the image button, which displays when the report users hover the mouse over the image button in the HTML output of the report or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Disabled**

Select if you want to disable the image button.

**Size**

You can specify the size of the image in this box.

* **Original Size**  
  Select to use the original size of the image. To use customized size for the image, clear the option and Designer enables the following options:
  + **Constrain Proportions**  
    If you select the option, when you set the width or height of the area for displaying the image, Designer adjusts the other accordingly based on the specified width-to-height ratio.
  + **Width**  
    Specify the width of the area for displaying the image.
  + **Height**  
    Specify the height of the area for displaying the image.
  + **Scaling Mode**  
    Select the scaling mode of the image.
    - **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
    - **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
    - **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
    - **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
    - **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the image button in this panel.

## Button Display Type

You see the following options for the Button display type:

![Display Type dialog box - Button](https://devnet.logianalytics.com/hc/article_attachments/4404856983703/dsplytp_btn.gif)

**Name**

Specify the name of the button.

**Value**

Select the value of the button.

**Tool Tip**

Specify the tool tip of the button, which displays when the report users hover the mouse over the button in the HTML output of the report or at runtime.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Action**

Specify the default action that happens when the report users select the button.

* **None**  
  Select if you do not want any action to happen.
* **Submit Form**  
  Select if you want to submit a form.
* **Reset Form**  
  Select if you want to reset a form.

**Disabled**

Select if you want to disable the button.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the button in this panel.

## List Display Type

You see the following options for the List display type:

![Display Type dialog box - List](https://devnet.logianalytics.com/hc/article_attachments/4404856983959/dsplytp_lst.gif)

**Name**

Specify the name of the list.

**Tool Tip**

Specify the tool tip of the list, which displays when the report users hover the mouse over the list in the HTML output of the report or at runtime.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Designer enables the button when you are using the dialog box for defining the web options of a List web control. You can select it to add a new item in the list.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Designer enables the button when you are using the dialog box for defining the web options of a List web control. You can select it to delete the specified item.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Designer enables the button when you are using the dialog box for defining the web options of a List web control. You can select it to move the specified item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Designer enables the button when you are using the dialog box for defining the web options of a List web control. You can select it to move the specified item lower in the list.

**Item Label**

The column shows the display text or format that you select for the item values. Select in the cell to select the desired item label from the drop-down list.

**Value**

The column shows the values that you specify for the items.

If you are using the dialog box for defining the web options of a List web control, you can select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the cell to specify a field to control the value using the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097601-Insert-Fields-Dialog-Box).

**Selected**

Specify the value to be selected in the list by default.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Allow Multiple Selections**

Select to allow selecting multiple items in the list at the same time.

**Use Runtime Value**

Designer enables this option when you use the dialog box for changing the display type of a parameter to List. Select it to use the runtime value of the parameter as the selected value of the drop-down list.

**Disabled**

Select if you want to disable the list.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the list in this panel.

Designer displays the following options when the object is in a web report or library component:

**Display**

Specify to display the list as Text, Button, Checkbox, or Radio Button. When you select Radio Button, Designer disables the Allow Multiple Selections option.

**Vertical**

Select to display items in one column vertically in the list, and add a vertical scrollbar in the list if it cannot completely display all the items within the specified height.

**Horizontal**

Select to display the items horizontally following the Z order in the list.

**Item Width**

Designer enables this option when you select Horizontal. You can use it to specify the width of each item in the list.

**Item Height**

Specify the height of each item in the list.

**Horizontal Gap**

Designer enables this option when you select Horizontal. You can use it to specify the horizontal gap between two adjacent items in the list.

**Vertical Gap**

Specify the vertical gap between two adjacent items in the list.

## Drop-down List Display Type

You see the following options for the Drop-down List display type:

![Display Type dialog box - Drop-down List](https://devnet.logianalytics.com/hc/article_attachments/4404856984215/dsplytp_drpdwnlst.gif)

**Name**

Specify the name of the drop-down list.

**Tool Tip**

Specify the tool tip of the drop-down list, which displays when the report users hover the mouse over the drop-down list in the HTML output of the report or at runtime.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Designer enables the button when you are using the dialog box for defining the web options of a Drop-down List web control. You can select it to add a new item in the drop-down list.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Designer enables the button when you are using the dialog box for defining the web options of a Drop-down List web control. You can select it to delete the specified item.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Designer enables the button when you are using the dialog box for defining the web options of a Drop-down List web control. You can select it to move the specified item higher in the drop-down list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Designer enables the button when you are using the dialog box for defining the web options of a Drop-down List web control. You can select it to move the specified item lower in the drop-down list.

**Item Label**

The column shows the display text or format that you select for the item values. Select in the cell to select the desired item label from the drop-down list.

**Value**

The column shows the values that you specify for the items.

If you are using the dialog box for defining the web options of a Drop-down List web control, you can select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the cell to specify a field to control the value using the [Insert Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097601-Insert-Fields-Dialog-Box).

**Selected**

Specify the value to be selected in the drop-down list by default.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

* Designer displays the button when the object is in a page report that uses query resources. It indicates that you can use [a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) or a DBField to control the value of an option. Select the button and then select a formula or DBField from the drop-down list to use its value for the option.

**Use Runtime Value**

Designer enables this option when you use the dialog box for changing the display type of a parameter to Drop-down List. Select it to use the runtime value of the parameter as the selected value of the drop-down list.

**Disabled**

Select if you want to disable the drop-down list.

**[Web Behaviors](#Behaviors)**

You can specify the web behaviors that you want to bind to the drop-down list in this panel.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058482-Display-Attributes-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058662-Download-Customized-Control-Dialog-Box)
