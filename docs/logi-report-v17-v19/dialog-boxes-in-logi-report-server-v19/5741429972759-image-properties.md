---
title: "Image Properties"
id: 5741429972759
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741429972759-Image-Properties
updated_at: 2022-10-31T17:17:33Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741459041175-Group-Options-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741429988631-Insert-Aggregation-Dialog-Box-Properties)

# Image Properties

This topic describes how you can use the Image Properties dialog box to edit the properties of an image. Server displays the dialog box when you right-click an image and select **Properties** from the shortcut menu.

![Image Properties dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905730374423/imgprpty.gif)

**Name**

Specify the display name of the image.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Image Name**

Specify the image file name.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9905615792535/btn_wbrpt_fmla.gif)**Formula button**

When this button is available to a property, you can control the value of the property by a formula. Select this button, and then select a formula or select **<Edit Expression>** to create an expression using the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5741450053911-Formula-Editor-Properties).

**Scaling Mode**

* **actual size**  
  Select to show the image in its actual size. If the display area is smaller than the image, Server hides part of the image.
* **fit image**Select if you want the image to fill the display area and keep the original perspective ratio under the limitation of Max Ratio.
* **fit width**Select if you want the image to fit the display area width under the limitation of Max Ratio.
* **fit height**Select if you want the image to fit the display area height, under the limitation of Max Ratio.
* **customize**Select if you want to specify the width and height of the image in the size fields.

**Horizontal Alignment**

Specify the horizontal alignment of the image in its container.

**Vertical Alignment**

Specify the vertical alignment of the image in its container.

**Rotation**

Rotate the image at a specified angle in degrees. The following is the meaning of different values:

* 0 - No rotation.
* Positive value - Rotate the image clockwise.
* Negative value - Rotate the image anticlockwise.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) When you specify a rotation degree for the image, in the report the area for displaying the image retains its original size hence it may result in that the rotated image exceeds the area boundary. In this case, Logi Report hides the parts that extend outside of the area.

**Width**

Specify the width of the area for displaying the image.

**Height**

Specify the height of the area for displaying the image.

**Alt**

Specify the alternate text of the image, which will show when the image cannot display.

**Title**

Specify tip information about the image, which will show when you hover over the image.

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741459041175-Group-Options-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741429988631-Insert-Aggregation-Dialog-Box-Properties)
