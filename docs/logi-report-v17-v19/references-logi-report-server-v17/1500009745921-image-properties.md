---
title: "Image Properties"
id: 1500009745921
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745921-Image-Properties
updated_at: 2021-07-25T07:20:02Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719522-Group-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745941-Insert-Aggregation)

# Image Properties

The Image Properties dialog box is used to edit the properties of an image.

There are the following tabs in this dialog box: [General](#General) and [Others](#Others).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the image.

![Image Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404942586775/imgprpty_gnrl.gif)

**Name**

Specifies the display name of the image.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Picture Name**

Displays the image file name.

**Scaling Mode**

Specifies the scaling mode of the image, which controls the image behavior when you adjust the size of the area for displaying the image.

* **actual size** - Shows the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
* **fit image** - Adjusts the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
* **fit width** - Adjusts the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
* **fit height** - Adjusts the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
* **customize** - Adjusts the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.

**Horizontal Alignment**

Specifies the horizontal alignment of the image in its container.

**Vertical Alignment**

Specifies the vertical alignment of the image in its container.

**Rotation**

Rotates the image at a specified angle in degrees. The following is the meaning of different values:

* 0 - No rotation.
* Positive value - Rotate the image clockwise.
* Negative value - Rotate the image anticlockwise.

**Note:** When a rotation degree is specified for the image, in the report result the area for displaying the image maintains its original size hence it may result in that the rotated image exceeds the area boundary. In this case Logi Report will cut the parts that extend outside of the area.

**X**

Specifies the X coordinate of the image.

**Y**

Specifies the Y coordinate of the image.

**Width**

Specifies the width of the area for displaying the image.

**Height**

Specifies the height of the area for displaying the image.

**Alt**

Specifies the alternate text of the image, which will be shown when the image cannot be displayed.

**Title**

Specifies tip information about the image, which will be displayed when the mouse pointer hovers on the image.

## Others

You can use this tab to view and configure some miscellaneous settings.

![Image Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404936919703/imgprpty_other.gif)

**TOC Anchor**

Specifies whether or not to add the node that represents the image to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the image in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the image will not be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog box).

**Export to CSV**

If true, the image will not be exported when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719522-Group-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745941-Insert-Aggregation)
