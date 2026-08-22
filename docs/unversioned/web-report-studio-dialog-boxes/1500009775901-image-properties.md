---
title: "Image Properties"
id: 1500009775901
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775901-Image-Properties
updated_at: 2021-07-24T00:48:21Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775881-Group-Options-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747562-Insert-Aggregation-Dialog-Box-Properties)

# Image Properties

This topic describes how you can use the Image Properties dialog box to edit the properties of an image. Server displays the dialog box when you right-click an image and select **Properties** from the shortcut menu.

![Image Properties dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880353687/imgprpty.gif)

**Name**

Specifies the display name of the image.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Image Name**

Specifies the image file name.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404880159895/btn_wbrpt_fmla.gif)

Indicates the value of the option can be controlled by a formula. Select this button and select a formula from the drop-down list, or select **<Edit Expression>** to create an expression using the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009775341-Formula-Editor-Properties).

**Scaling Mode**

* **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
* **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
* **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
* **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
* **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.

**Horizontal Alignment**

Specifies the horizontal alignment of the image in its container.

**Vertical Alignment**

Specifies the vertical alignment of the image in its container.

**Rotation**

Rotates the image at a specified angle in degrees. The following is the meaning of different values:

* 0 - No rotation.
* Positive value - Rotate the image clockwise.
* Negative value - Rotate the image anticlockwise.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When you specify a rotation degree for the image, in the report result the area for displaying the image maintains its original size hence it may result in that the rotated image exceeds the area boundary. In this case Logi Report cuts the parts that extend outside of the area.

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

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Ignores the setting and closes this dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775881-Group-Options-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747562-Insert-Aggregation-Dialog-Box-Properties)
