---
title: "Changing the Display Type of Objects in a Report"
id: 5735555544087
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735555544087-Changing-the-Display-Type-of-Objects-in-a-Report
updated_at: 2022-11-02T08:22:56Z
---

# Changing the Display Type of Objects in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report)

# Changing the Display Type of Objects in a Report

Display Type enables you to map an object such as a label to display as other value or image instead in a report. You can apply it to the following objects: [labels](https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels), data fields ([DBFields](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields), [summary fields](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields), [formula fields](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields), [parameter fields](https://devnet.logianalytics.com/hc/en-us/articles/5735512482071-Working-with-Parameter-Fields)), [special fields](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields), and [basic web controls](https://devnet.logianalytics.com/hc/en-us/articles/5735521282967-Using-Basic-Web-Controls). This topic introduces the display types Designer supports and how you can change the display type of an object.

The display types Designer provides include:

* General types: [Text](#Text), [Image](#Image), [Barcode](#Barcode), [QR Code](#QRCode), and [Rank](#Rank) (you can use Text only for objects in web reports and library components)
* Display types that you can use as basic web controls directly: Text Field, Hidden Field, Text Area, Checkbox, Radio Button, Image Button, Button, List, and Drop-down List (you can only display parameter fields as List and Drop-down List, and display the List and Drop-down List web controls as each other)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You cannot use the Display Type feature in business view-based page reports.

The following sections show changing the display type of an object in a report as a general type:

* [Displaying an Object as Text](#Text)
* [Displaying an Object as Image](#Image)
* [Displaying an Object as Barcode](#Barcode)
* [Displaying an Object as QR Code](#QRCode)
* [Displaying an Object as Rank](#Rank)

For more information about how to change the display type of an object to a basic web control, see [Inserting Basic Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/5735527852183-Using-Basic-Web-Controls-in-a-Report#Insert).

## Displaying an Object as Text

1. Right-click the object and select **Display Type** from the shortcut menu. Designer displays the Display Type dialog box.
2. In the Display As box, select **Text**.

   ![Display Type dialog box - Text](https://devnet.logianalytics.com/hc/article_attachments/9898474540183/dsplytp_txt.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/5735513570199-Display-Type-Dialog-Box#Text),
   1. If you want to specify a tool tip for the text, clear the **Auto** option, then in the **Tool Tip** text box, specify the tool tip to show for the text. When the object is in a query-based page report, you can also [use a formula to control the tool tip](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties): select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select a formula from the drop-down list. If you select a DBField from the drop-down list, Designer applies the first record of the field in the database as the tool tip. The tool tip displays when users hover the mouse over the text at runtime or in the HTML output of the report.
   2. When you select the Auto option, you cannot customize the tool tip. Then at runtime or in the HTML output, when the text cannot display completely, users can hover the mouse over the text to get its full content in the tool tip.
4. In the **Web Behaviors** panel, [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) of the object.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Designer does not display the Web Behaviors panel, when the object is not directly contained in a tabular cell for web reports.
5. Select **OK** to accept the settings on the object.

## Displaying an Object as Image

1. Right-click the object and select **Display Type** from the shortcut menu. Designer displays the Display Type dialog box.
2. In the Display As box, select **Image**.

   ![Display Type dialog box - Image](https://devnet.logianalytics.com/hc/article_attachments/9898457501079/dsplytp_img.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/5735513570199-Display-Type-Dialog-Box#Image), select **Browse** to specify the image source. If you want to [use a formula to control the image source](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties), select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select it from the drop-down list. When you select a DBField from the drop-down list, Designer applies the first record of the field in the database as the image source. For a data field such as DBField, formula, and summary in which image data is stored, you can also select **From DBField** to apply the data field as the image source. Then, you can specify the type for decoding the image from the **Decode Type** drop-down list and decide whether to parse the image using the data URI scheme.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When the image type is SVG, Designer shows the image within the display area of the data field and ignores the Size settings in the following steps 7 to 9. Designer uses the viewport of the SVG image when you define to scale the image to fit into the display area; otherwise, Designer uses the display area as the viewport. Designer cannot displays the SVG image when it refers to external resources or contains JavaScript code, and does not support the dynamic effect in SVG.
4. In the **Name** text box, type the name of the image or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select a formula or DBField to control the name.
5. In the **Alternate Text** text box, type a string to serve as the content when the image cannot display or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select a formula or DBField to control the alternate text.
6. In the **Tool Tip** text box, type the tool tip to show for the image or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select a formula or DBField to control the tool tip. The tool tip displays when users hover the mouse over the image at runtime or in the HTML output of the report.
7. In the **Max Ratio** text box, specify the maximum scaling ratio of the image. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio is less than or equal to it.
8. In the **Rotation** text box, specify the rotation degree of the image.
   The value 0 means no rotation; a positive value means rotating the image clockwise and a negative value anticlockwise.
9. By default, Designer displays the image in its original size. Clear **Original Size** if you want to use customized image size, then set the width and height of the area for displaying the image in the **Width** and **Height** text boxes, select **Constrain Proportion** to constrain the aspect ratio when setting the width and height, and specify the scaling mode of the image from the **Scaling Mode** drop-down list. The scaling mode you select controls the image behavior when you adjust the size of the area for displaying the image.
   * **actual size**  
     Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
   * **fit image**  
     Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
   * **fit width**  
     Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
   * **fit height**  
     Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
   * **customize**  
     Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.
10. In the **Web Behaviors** panel, [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) of the object.
11. Select **OK** to accept the settings on the object.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If you specify a rotation degree for the image, the area for displaying the image maintains its original size in the report, hence it may result in that the rotated image exceeds the area boundary. In this case, Designer cuts the parts that extend outside the area.

## Displaying an Object as Barcode

1. Right-click the object and select **Display Type** from the shortcut menu. Designer displays the Display Type dialog box.
2. In the Display As box, select **Barcode**.

   ![Display Type dialog box - Barcode](https://devnet.logianalytics.com/hc/article_attachments/9898474564503/dsplytp_brcd.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/5735513570199-Display-Type-Dialog-Box#Barcode), select the required barcode type from the **Symbology** drop-down list. You can preview the format of the selected symbology in the **Preview** box.
4. In the **Tool Tip** text box, specify the tool tip to show for the barcode. If you want to [use a formula to control the tool tip](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties), select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select a formula from the drop-down list. When you select a DBField from the drop-down list, Designer applies the first record of the field in the database as the tool tip. The tool tip displays when users hover the mouse over the barcode at runtime or in the HTML output of the report.
5. From the **Scale Mode** drop-down list, select the unit for the values of Quiet Zone, Narrow Width, Supplement, Height, and Ratio.
6. In the **Quite Zone** text box, specify the space around the barcode (most symbologies require quiet zones that precede and follow the barcode).
7. You can change the default value of the barcode in the **Default Message** text box, which Designer applies to the barcode in design mode. If you also want to use this value as the value of the barcode in the report, select **Use Default Message**.
8. Specify the supplement of the barcode. If you select the barcode type as Code 39, Code 128/128A/128B/128C, or Codabar, you do not need to set the supplement.
9. Set the barcode bar width in the **Narrow Width** text box, and the height of the bars in the **Height** text box.
10. Specify the width ratio of the thick bar to the thin bar in the **Ratio** text box when you select the barcode type as Code 39 or Codabar. The ratio can only be 2.0 or 3.0. Designer regards any ratio values not equal to 2.0 or 3.0 as 2.0.
11. In the **Orientation** text box, specify the rotation angle, in degrees.
12. Select **Enable Checking Digits** if you want to include check digits in the barcode. When you select the barcode type as Code 39, Code 128/128A/128B/128C, or Codabar, you can select **Display HR** to display the barcode numbers together with the barcode.
13. In the **Web Behaviors** panel, [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) of the object.
14. Select **OK** to accept the settings on the object.

You can also use barcodes as independent component and insert them into a report directly. For more information, see [Barcodes](https://devnet.logianalytics.com/hc/en-us/articles/5735498517911-Working-with-Barcodes).

## Displaying an Object as QR Code

1. Right-click the object and select **Display Type** from the shortcut menu. Designer displays the Display Type dialog box.
2. In the Display As box, select **QR Code**.

   ![Display Type dialog box - QR Code](https://devnet.logianalytics.com/hc/article_attachments/9898474577815/dsplytp_qrcd.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/5735513570199-Display-Type-Dialog-Box#QRCode), set the margin between the image in the middle of the QR Code and the border of the QR Code.
4. Select the error correction level for the QR Code. Error correction helps in making a QR Code stay readable, even when some pixels are missing. There are four correction levels. Level L means 7% of the code words can be recovered from a damaged symbol, level M 15%, level Q 25%, and level H 30%. The higher the level is, the bigger the QR Code gets.
5. You can change the default value of the QR Code in the **Default Message** text box, which Designer applies to the QR Code in design mode. If you also want to use this value as the value of the QR Code in the report, select **Use Default Message**.
6. In the **Web Behaviors** panel, [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) of the object.
7. Select **OK** to accept the settings on the object.

You can also use QR Codes as independent component and insert them into a report directly. For more information, see [Barcodes](https://devnet.logianalytics.com/hc/en-us/articles/5735498517911-Working-with-Barcodes).

## Displaying an Object as Rank

1. Right-click the object and select **Display Type** from the shortcut menu. Designer displays the Display Type dialog box.
2. In the Display As box, select **Rank**.

   ![Display Type dialog box - Rank](https://devnet.logianalytics.com/hc/article_attachments/9898457538199/dsplytp_rank.gif)
3. In the [Web Options panel](https://devnet.logianalytics.com/hc/en-us/articles/5735513570199-Display-Type-Dialog-Box#Rank), select **Browse** to select an image file to be the default image (Designer applies the image when a value does not fit any of the specified value ranges).
4. In the **Default Image Alternate Text** text box, type a string to serve as the content when the default image cannot display. If you want to [use a formula to control the alternate text](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties), select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select a formula from the drop-down list. When you select a DBField from the drop-down list, Designer applies the first record of the field in the database as the alternate text.
5. In the **Default Tool Tip** text box, type the tool tip to show for the default image or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9898457345303/btn_fmla.gif) and select a formula or DBField to control the tool tip. The tool tip displays when users hover the mouse over the image at runtime or in the HTML output of the report.
6. In the **Default Image Rotation** text box, specify the rotation degree of the default image.
   * 0 - No rotation.
   * Positive value - Rotates the image clockwise.
   * Negative value - Rotates the image anticlockwise.
7. In the **Value Range** box, select in the cell of the corresponding column to specify the minimum value, maximum value, image, alternate text, tool tip, and rotation of the first range.
8. Select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif) to add and define more ranges. Designer displays a value, which is larger than or equal to the minimum value of a range and less than the maximum value, as the image, or the alternate text when the image cannot be loaded or is not available. For a value belonging to two or more overlapping ranges, Designer applies the highest range in the Value Range box.
9. To delete a range, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif). You can also use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the order of the ranges.
10. In the **Web Behaviors** panel, [specify web behaviors](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#WebControl) of the object.
11. Select **OK** to accept the settings on the object.

You can also use ranks as independent component and insert them into a report directly. For more information, see [Ranks](https://devnet.logianalytics.com/hc/en-us/articles/5735564383767-Working-with-Ranks).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* If you specify a tool tip for an object, on Firefox, the tool tip displays in one line with the maximal tip width the browser allows. Firefox cuts the text that cannot display within the width and replaces it with an ellipsis (...).
* When you rotate an image, the rectangle that holds the image maintains its original size, which may result in that the image exceeds the field border and therefore the parts that extends outside the border is cut off.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report)
