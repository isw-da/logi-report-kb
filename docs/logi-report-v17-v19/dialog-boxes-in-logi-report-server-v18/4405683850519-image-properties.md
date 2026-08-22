---
title: "Image Properties"
id: 4405683850519
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683850519-Image-Properties
updated_at: 2022-01-27T07:59:21Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690591895-Group-Options-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683851543-Insert-Aggregation-Dialog-Box-Properties)

# Image Properties

This topic describes how you can use the Image Properties dialog box to edit the properties of an image. Server displays the dialog box when you right-click an image and select **Properties** from the shortcut menu.

![Image Properties dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447213719/imgprpty.gif)

**Name**

Specifies the display name of the image.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Image Name**

Specifies the image file name.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420447036695/btn_wbrpt_fmla.gif)

Indicates the value of the option can be controlled by a formula. Select this button and select a formula from the drop-down list, or select **<Edit Expression>** to create an expression using the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/4405683820183-Formula-Editor-Properties).

**Scaling Mode**

* **actual size**  
  Select to show the image in its actual size. If the display area is smaller than the image, Server hides part of the image.
* **fit image**Select if you want the image to fill the display area and keep the original perspective ratio under the limitation of Max Ratio.
* **fit width**Select if you want the image to fit the display area width under the limitation of Max Ratio.
* **fit height**Select if you want the image to fit the display area height, under the limitation of Max Ratio.
* **customize**Select if you want to specify the width and height of the image in the size fields.

**Horizontal Alignment**

Specifies the horizontal alignment of the image in its container.

**Vertical Alignment**

Specifies the vertical alignment of the image in its container.

**Rotation**

Rotates the image at a specified angle in degrees. The following is the meaning of different values:

* 0 - No rotation.
* Positive value - Rotate the image clockwise.
* Negative value - Rotate the image anticlockwise.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) When you specify a rotation degree for the image, in the report the area for displaying the image maintains its original size hence it may result in that the rotated image exceeds the area boundary. In this case Logi Report cuts the parts that extend outside of the area.

**Width**

Specifies the width of the area for displaying the image.

**Height**

Specifies the height of the area for displaying the image.

**Alt**

Specifies the alternate text of the image, which will be shown when the image cannot be displayed.

**Title**

Specifies tip information about the image, which will be displayed when the mouse pointer hovers on the image.

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690591895-Group-Options-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683851543-Insert-Aggregation-Dialog-Box-Properties)
