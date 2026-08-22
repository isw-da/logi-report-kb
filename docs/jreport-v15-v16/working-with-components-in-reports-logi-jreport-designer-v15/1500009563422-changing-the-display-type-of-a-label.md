---
title: "Changing the Display Type of a Label"
id: 1500009563422
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563422-Changing-the-Display-Type-of-a-Label
updated_at: 2021-07-24T05:56:01Z
---

# Changing the Display Type of a Label

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label)

# Changing the Display Type of a Label

For labels in a page report that is created using query resources, their display type can be changed, that is to say, you can map the labels to other values or images to be displayed instead.

Logi JReport provides 13 kinds of display types: text, image, barcode, rank, text field, hidden field, text area, checkbox, radio button, image button, button, list, and drop-down list. In a web report and library component the only display type is Text where you are able to add a Tool Tip.

**To change the display type of a label:**

1. Right-click the label and select **Display Type** to open the Display Type dialog.
2. In the Display As box, select the required type.
3. Set the options for the selected type in the Web Options panel.
4. Select the **OK** button to close the dialog.

A label can be displayed as one of the following general types:

> * [As Text](#Text)
> * [As Image](#Image)
> * [As Barcode](#Barcode)
> * [As Rank](#Rank)

The display type of a label can also be changed to a web control, including text field, password, text area, checkbox, radio button, image button, and button. A label cannot be displayed as list or drop-down list. For details about how to make settings of these display types, see [Using Basic Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009584641-Using-Basic-Web-Controls).

## As Text

To define the display type of a label as text, follow the steps below:

1. Right-click the label and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **Text**.

   ![Display Type dialog - Text](https://devnet.logianalytics.com/hc/article_attachments/4404893930391/dsplytp_txt.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#Text), if you want to specify a tooltip for the text, uncheck the **Auto** option, then in the Tool Tip field, enter the tip you want to show for the text. Then at server runtime or in HTML results, when you hover the mouse over the text, the tooltip will be displayed. If you want to use a formula to control the tip, select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) and select a formula from the drop-down list. You can also select the **<CREATE FORMULA>** item in the list to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) as required. If the label is in a crosstab, you can also use a [crosstab formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas) created in the crosstab to control the tooltip, or select <CREATE CROSSTAB FORMULA> to create one.

   When the Auto option is checked, the tooltip cannot be customized. Then at server runtime or in HTML results, when the text cannot be fully displayed, you can hover the mouse over the text to get its full content in the tooltip.
4. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label) to the label in the Web Behaviors box.
5. Upon finishing, select the **OK** button to close the dialog.

## As Image

To define the display type of a label as image, follow the steps below:

1. Right-click the label and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **Image**.

   ![Display Type dialog - Image](https://devnet.logianalytics.com/hc/article_attachments/4404889370647/dsplytp_img.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#Image), select the **Browse** button to specify the image source. If you want to use a formula to control the image source, select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) and select a formula from the drop-down list. You can also select the **<CREATE FORMULA>** item in the list to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) as required. If the label is in a crosstab, you can also use a [crosstab formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas) created in the crosstab to control the image source, or select <CREATE CROSSTAB FORMULA> to create one.

   For a DBField, formula, or a summary, you can also check the From DBField radio button to make the value of the DBField/formula/summary the image source. If you choose this option, the Decode Type drop-down list is enabled, from which you can specify the type for decoding the image.
4. Type the name of the image in the Name field, or use a formula to control the name.
5. Type a string in the Alternate Text field to serve as content when the image cannot be displayed, or use a formula to control the alternate text.
6. In the Tool Tip field, enter the tip you want to show for the image or use a formula to control the tooltip. Then at server runtime or in HTML results, when you hover the mouse over the image, the tooltip will be displayed.
7. Specify the scaling mode of the image from the Scaling Mode drop-down list, and the maximum scaling ratio in the Max Ratio field. By default the scaling ratio of the image is not limited.

   The following are the available scaling modes:

   * **actual size** - If selected, the image will be shown in its actual size.
   * **fit image** - If selected, the image will be scaled to be wholly shown.
   * **fit width** - If selected, the image will be scaled to fit the width of the image viewer.
   * **fit height** - If selected, the image will be scaled to fit the height of the image viewer.
   * **customize** - If selected, the image will be scaled according to the width and height that you specify in the Width and Height box.
8. Specify the size of the image.
   * If you choose to use the original size of the image, check the **Original Size** option.
   * If you want to use customized image size, uncheck **Original Size**, and then set the display width and height of the image in the Width and Height fields. Check the **Constrain Proportion** option if you want to constrain aspect ratio of the image when setting the width and height.
9. Specify the rotation degree of the image in the Rotation field.
   * 0 - No rotation.
   * Positive value - Rotates the image clockwise.
   * Negative value - Rotates the image anticlockwise.
10. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label) to the label in the Web Behaviors box.
11. Upon finishing, select the **OK** button to close the dialog.

## As Barcode

A barcode can also be inserted into a report as a component. For details, see the section [Barcodes](https://devnet.logianalytics.com/hc/en-us/articles/1500009562902-Barcodes).

To define the display type of a label as barcode, follow the steps below:

1. Right-click the label and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **Barcode**.

   ![Display Type dialog - Barcode](https://devnet.logianalytics.com/hc/article_attachments/4404889370903/dsplytp_brcd.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#Barcode), select the required barcode type from the Symbology drop-down list. You can preview the format of the selected symbology in the Preview box (for details about the different symbologies of barcodes, see [Appendix 1: Barcode Symbologies](https://devnet.logianalytics.com/hc/en-us/articles/1500009562562-Appendix-1-Barcode-Symbologies)).
4. In the Tool Tip field, enter the tip you want to show for the barcode. Then at server runtime or in HTML results, when you hover the mouse over the barcode, the tooltip will be displayed.

   If you want to use a formula to control the tip, select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) and select a formula from the drop-down list. You can also select the **<CREATE FORMULA>** item in the list to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) as required. If the label is in a crosstab, you can also use a [crosstab formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas) created in the crosstab to control the tooltip, or select <CREATE CROSSTAB FORMULA> to create one.
5. From the Scale Mode drop-down list, select the unit for the values of Quiet Zone, Narrow Width, Supplement, Height and Ratio.
6. Specify the space around the barcode in the Quite Zone field (most symbologies require quiet zones that precede and follow the barcode).
7. Change the default value of the barcode in the Default Message field if necessary. If you check Use Default Message, the message will be used as the barcode value when you view the report result. Otherwise, the message will only be used in design mode.
8. Specify the supplement of the barcode if necessary.  
     
    If you select the barcode type as Code 39, Code 128/128A/128B/128C or Codabar, you will not need to set the supplement.
9. Set the barcode bar width in the Narrow Width field, and the height of the bars in the Height field.
10. Specify the width ratio of the thick bar to the thin bar in the Ratio field if you selected the barcode type as Code 39 or Codabar. The ratio can only be 2.0 or 3.0. Any ratio values not equal to 2.0 or 3.0 will be regarded as 2.0.
11. Specify the rotation angle in degrees in the Orientation field if necessary.
12. Select the **Enable Checking Digits** checkbox if you want to include check digits in the barcode.
13. If you selected the barcode type as Code 39, Code 128/128A/128B/128C, or Codabar, then you can check **Display HR** to display the barcode numbers together with the barcode.
14. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label) to the label in the Web Behaviors box.
15. Upon finishing, select **OK** to close the dialog.

## As Rank

Ranks can also be used as component and inserted into a report directly. For details, refer to the section [Ranks](https://devnet.logianalytics.com/hc/en-us/articles/1500009584221-Ranks).

To define the display type of a label as rank, follow the steps below:

1. Right-click the label and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **Rank**.

   ![Display Type dialog - Rank](https://devnet.logianalytics.com/hc/article_attachments/4404893930647/dsplytp_rank.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009565002-Display-Type-Dialog#Rank), select the **Browse** button to select an image file to be the default image (used if a value does not fit any of the specified value ranges).
4. Type a string in the Default Image Alternate Text field. The string will be displayed when the default image cannot be loaded or is not available. If you want to use a formula to control the alternate text, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) and select a formula from the drop-down list. You can also select the **<CREATE FORMULA>** item in the list to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) as required. If the label is in a crosstab, you can also use a [crosstab formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas) created in the crosstab to control the alternate text, or select <CREATE CROSSTAB FORMULA> to create one.
5. In the Default Tool Tip field, enter the tip you want to show for the default image, or use a formula to control the tooltip. Then at server runtime or in HTML results, when you hover the mouse over the image, the tooltip will be displayed.
6. Specify the rotation degree of the default image in the Default Image Rotation field.
   * 0 - No rotation.
   * Positive value - Rotate the image clockwise.
   * Negative value - Rotate the image anticlockwise.Note that when you rotate an image, the rectangle that holds the image maintains its original size, which may result in that the image exceeds the field border and therefore the parts that extends outside of the border will be cut off.
7. In the Value Range box, specify different ranges according to your requirements. For each value range, you should specify the minimum value, maximum value, image, alternate text, tooltip and rotation. A value, which is larger than or equal to the minimum value of a range and less than the maximum value, will be displayed as the image, or the alternate text if the image cannot be loaded or is not available. For a value belonging to two or more overlapping ranges, the highest range in the Value Range box will apply.

   Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) or ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to add or delete a range, and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the ranges.
8. If needed, [bind web actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label) to the label in the Web Behaviors box.
9. Upon finishing, select the **OK** button to close this dialog.

**Notes:**

* If you have specified a tooltip, the tooltip is displayed differently on different browsers:
  + On Internet Explorer, the tip text is automatically wrapped if its length exceeds the maximal tip width the browser allows. In addition, for Internet Explorer, you can manually make some text displayed in a new line by adding &#10 or &#13 ahead of the text when editing it in the Tool Tip field.
  + On Firefox, the tip text is displayed in one line with the maximal tip width the browser allows, and the text that cannot be displayed within the width will be cut off and replaced by ellipsis.
* When you rotate an image, the rectangle that holds the image maintains its original size, which may result in that the image exceeds the field border and therefore the parts that extends outside of the border will be cut off.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label)
