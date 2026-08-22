---
title: "Changing the Display Type of Objects in Reports"
id: 1500010034802
section: "Creating Datasets and Designing Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010034802-Changing-the-Display-Type-of-Objects-in-Reports
updated_at: 2022-07-18T07:19:29Z
---

# Changing the Display Type of Objects in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports)

# Changing the Display Type of Objects in Reports

Display Type allows you to map an object such as a label to other value or image to be displayed instead in a report. It is supported on the following objects: [labels](https://devnet.logianalytics.com/hc/en-us/articles/1500010029102-Labels), data fields ([DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010063761-DBFields), [summary fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010029262-Summary-Fields-), [formula fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010063801-Formula-Fields), [parameter fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010029182-Parameter-Fields)), [special fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010029242-Special-Fields) and [basic web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010064081-Using-Basic-Web-Controls).

The display types Logi JReport Designer provides include:

* General types: [Text](#Text), [Image](#Image), [Barcode](#Barcode), [QR Code](#QRCode)  and [Rank](#Rank) (for objects in web reports and library components, only Text is supported)
* Display types that can be used as basic web controls directly: Text Field, Hidden Field, Text Area, Checkbox, Radio Button, Image Button, Button, List, and Drop-down List (only parameter fields can be displayed as List and Drop-down List, and the List and Drop-down List web controls can be displayed as each other)

The Display Type feature is not supported on page report creating using business views.

The following shows changing the display type of an object in a report as a general type:

* [Displaying an Object as Text](#Text)
* [Displaying an Object as Image](#Image)
* [Displaying an Object as Barcode](#Barcode)
* [Displaying an Object as QR Code](#QRCode)
* [Displaying an Object as Rank](#Rank)

For details about how to change the display type of an object to a basic web control, see [Inserting basic web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Insert).

## Displaying an Object as Text

1. Right-click the object and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **Text**.

   ![Display Type dialog - Text](https://devnet.logianalytics.com/hc/article_attachments/4404901135255/dsplytp_txt.gif)
3. In the Web Options panel, if you want to specify a tooltip for the text, uncheck the **Auto** option, then in the Tool Tip text box enter the tooltip you want to show for the text. If the component is in a page report that is created using query resources, you can also [use a formula to control the tooltip](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties): select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and select a formula from the drop-down list. If a DBField is selected from the drop-down list, the first record of the field in the database will be used as the tooltip. The tooltip will be displayed when you hover the mouse over the text at server runtime or in HTML results.

   When the Auto option is checked, the tooltip cannot be customized. Then at server runtime or in HTML result, when the text cannot be fully displayed, you can hover the mouse over the text to get its full content in the tooltip.
4. In the Web Behaviors panel, bind web actions to the object [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) if needed.
5. Select **OK** in the Display Type dialog to accept the settings on the object.

## Displaying an Object as Image

1. Right-click the object and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **Image**.

   ![Display Type dialog - Image](https://devnet.logianalytics.com/hc/article_attachments/4404901135511/dsplytp_img.gif)
3. In the Web Options panel, select the **Browse** button to specify the image source. If you want to [use a formula to control the image source](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties), select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and select it from the drop-down list. If a DBField is selected from the drop-down list, the first record of the field in the database will be used as the image source.

   For a data field such as DBField, formula and summary in which image data is stored, you can also check the From DBField radio button to make the data field the image source. Then you can specify the type for decoding the image from the Decode Type drop-down list and decide whether to parse the image using the data URI scheme. If the image type is SVG, the image will be displayed within the display area of the data field and the Size settings in the following steps 7 to 9 are ignored. The viewport of the SVG image if defined will be used to scale the image to fit into the display area, otherwise the display area is used as the viewport. The SVG image cannot be displayed if it refers to external resources or contains JavaScript code, and the dynamic effect in SVG is not supported.
4. Type the name of the image in the Name text box, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and use a formula or DBField to control the name.
5. Type a string in the Alternate Text text box to serve as content when the image cannot be displayed, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and use a formula or DBField to control the alternate text.
6. In the Tool Tip text box, enter the tooltip you want to show for the image, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and use a formula or DBField to control the tooltip. The tooltip will be displayed when you hover the mouse over the image at server runtime or in HTML results.
7. In the Max Ratio text box, specify the maximum scaling ratio of the image. By default the scaling ratio of the image is not limited. If it is set to any value greater than 0, the actual scaling ratio is less than or equal to it.
8. Specify the rotation degree of the image in the Rotation text box.
   * 0 - No rotation.
   * Positive value - Rotates the image clockwise.
   * Negative value - Rotates the image anticlockwise.
9. If you want to use customized image size, uncheck **Original Size**, then set the display width and height of the image in the Width and Height text boxes, check **Constrain Proportion** to constrain aspect ratio of the image when setting the width and height. Then specify the scaling mode of the image from the Scaling Mode drop-down list.

   The following are the available scaling modes:

   * **actual size** - If selected, the image will be shown in its actual size.
   * **fit image** - If selected, the image will be scaled to be wholly shown.
   * **fit width** - If selected, the image will be scaled to fit the width of the image viewer.
   * **fit height** - If selected, the image will be scaled to fit the height of the image viewer.
   * **customize** - If selected, the image will be scaled according to the width and height that you specify in the Width and Height text boxes.
10. In the Web Behaviors panel, bind web actions to the component [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) if needed.
11. Select **OK** to accept the settings on the object.

## Displaying an Object as Barcode

1. Right-click the object and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **Barcode**.

   ![Display Type dialog - Barcode](https://devnet.logianalytics.com/hc/article_attachments/4404901135767/dsplytp_brcd.gif)
3. In the Web Options panel, select the required barcode type from the Symbology drop-down list. You can preview the format of the selected symbology in the Preview box.
4. In the Tool Tip text box, enter the tooltip you want to show for the barcode. If you want to [use a formula to control the tooltip](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties), select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and select a formula from the drop-down list. If a DBField is selected from the drop-down list, the first record of the field in the database will be used as the tooltip. The tooltip will be displayed when you hover the mouse over the barcode at server runtime or in HTML results.
5. From the Scale Mode drop-down list, select the unit for the values of Quiet Zone, Narrow Width, Supplement, Height and Ratio.
6. Specify the space around the barcode in the Quite Zone text box (most symbologies require quiet zones that precede and follow the barcode).
7. Change the default value of the barcode in the Default Message text box if necessary. If you check Use Default Message, the message will be used as the barcode value when you view the report result. Otherwise, the message will only be used in design mode.
8. Specify the supplement of the barcode if necessary. If you select the barcode type as Code 39, Code 128/128A/128B/128C or Codabar, you will not need to set the supplement.
9. Set the barcode bar width in the Narrow Width text box, and the height of the bars in the Height text box.
10. Specify the width ratio of the thick bar to the thin bar in the Ratio text box if you selected the barcode type as Code 39 or Codabar. The ratio can only be 2.0 or 3.0. Any ratio values not equal to 2.0 or 3.0 will be regarded as 2.0.
11. Specify the rotation angle in degrees in the Orientation text box if necessary.
12. Select the **Enable Checking Digits** checkbox if you want to include check digits in the barcode.
13. If you selected the barcode type as Code 39, Code 128/128A/128B/128C, or Codabar, then you can check **Display HR** to display the barcode numbers together with the barcode.
14. In the Web Behaviors panel, bind web actions to the component [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) if needed.
15. Select **OK** to accept the settings on the component.

Barcodes can also be used as independent component and inserted into a report directly. For details, see the section [Barcodes](https://devnet.logianalytics.com/hc/en-us/articles/1500010028682-Barcodes).

## Displaying an Object as QR Code

1. Right-click the object and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **QR Code**.

   ![Display Type dialog - QR Code](https://devnet.logianalytics.com/hc/article_attachments/4404909127831/dsplytp_qrcd.gif)
3. In the Web Options panel, set the margin between the image in the middle of the QR Code and the border of the QR Code.
4. Select the error correction level for the QR Code. Error correction helps in making a QR Code stay readable, even when some pixels are missing. There are four correction levels. Level L means 7% of the code words can be recovered from a damaged symbol, level M 15%, level Q 25% and level H 30%. The higher the level is the bigger the QR Code gets.
5. Change the default value of the QR Code in the Default Message text box if necessary, which will be used for the QR Code in design mode. If you want to use it as the value of the QR Code in the report result, check **Use Default Message**.
6. In the Web Behaviors panel, bind web actions to the component [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) if needed.
7. Select **OK** to accept the settings on the component.

QR Codes can also be used as independent component and inserted into a report directly. For details, see the section [Barcodes](https://devnet.logianalytics.com/hc/en-us/articles/1500010028682-Barcodes).

## Displaying an Object as Rank

1. Right-click the object and select **Display Type** from the shortcut menu to open the Display Type dialog.
2. In the Display As box, select **Rank**.

   ![Display Type dialog - Rank](https://devnet.logianalytics.com/hc/article_attachments/4404901136023/dsplytp_rank.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010030262-Display-Type-Dialog#Rank), select the **Browse** button to select an image file to be the default image (used if a value does not fit any of the specified value ranges).
4. Type a string in the Default Image Alternate Text text box. The string will be displayed when the default image cannot be loaded or is not available. If you want to [use a formula to control the alternate text](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties), select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and select a formula from the drop-down list. If a DBField is selected from the drop-down list, the first record of the field in the database will be used as the alternate text.
5. In the Default Tool Tip text box, enter the tooltip you want to show for the default image, or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and use a formula or DBField to control the tooltip. The tooltip will be displayed when you hover the mouse over the image at server runtime or in HTML results.
6. Specify the rotation degree of the default image in the Default Image Rotation text box.
   * 0 - No rotation.
   * Positive value - Rotate the image clockwise.
   * Negative value - Rotate the image anticlockwise.Note that when you rotate an image, the rectangle that holds the image maintains its original size, which may result in that the image exceeds the field border and therefore the parts that extends outside of the border will be cut off.
7. In the Value Range box, specify different ranges according to your requirements. For each value range, you should specify the minimum value, maximum value, image, alternate text, tooltip and rotation. A value, which is larger than or equal to the minimum value of a range and less than the maximum value, will be displayed as the image, or the alternate text if the image cannot be loaded or is not available. For a value belonging to two or more overlapping ranges, the highest range in the Value Range box will apply.

   Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) or ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif) to add or delete a range, and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to adjust the order of the ranges.
8. In the Web Behaviors panel, bind web actions to the component [the same as you do to web controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Action) if needed.
9. Select **OK** to accept the settings on the component.

Ranks can also be used as independent component and inserted into a report directly. For details, refer to the section [Ranks](https://devnet.logianalytics.com/hc/en-us/articles/1500010029202-Ranks).

**Notes:**

* If you have specified a tooltip, the tooltip will be displayed differently on different browsers:
  + On Internet Explorer, the tip text is automatically wrapped if its length exceeds the maximal tip width the browser allows. In addition, for Internet Explorer, you can manually make some text displayed in a new line by adding &#10 or &#13 ahead of the text when editing the tooltip.
  + On Firefox, the tip text is displayed in one line with the maximal tip width the browser allows, and the text that cannot be displayed within the width will be cut off and replaced by ellipsis.
* When you rotate an image, the rectangle that holds the image maintains its original size, which may result in that the image exceeds the field border and therefore the parts that extends outside of the border will be cut off.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports)
