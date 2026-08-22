---
title: "Image Properties"
id: 1500009713401
section: "Page Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009713401-Image-Properties
updated_at: 2021-11-03T06:58:08Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009687522-Group-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009713421-Insert-Aggregation)

# Image Properties

The Image Properties dialog helps you to edit the properties of an image. It contains the following tabs: [General](#General) and [Others](#Others).

**OK**

Applies the settings and closes this dialog.

**Cancel**

Cancels the settings and closes this dialog.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the image.

![Image Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412131496599/imgprpty_gnrl.gif)

**Name**

Specifies the display name of the image.

**Show NLS Value**

Specifies to show the translated name for the display name of the image in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the image is not modified.

**Picture Name**

Displays the image file name.

**Scaling Mode**

Specifies the scaling mode for the image. The mode can be:

* **Actual Size**: The image will be shown in its actual size.
* **Customize**: The image size will be equal to the image field size.
* **Fit Image**: The image will be scaled largest to wholly show in the image field.
* **Fit Width**: The image will be scaled largest to fit the width of the image field.
* **Fit Height**: The image will be scaled largest to fit the height of the image field.

**Horizontal Alignment**

Specifies the horizontal alignment of the image in its container.

**Vertical Alignment**

Specifies the vertical alignment of the image in its container.

**Rotation**

Rotates the image at a specified angle in degrees. The following is the meaning of different values:

* 0 - No rotation.
* Positive value - Rotate the image clockwise.
* Negative value - Rotate the image anticlockwise.

**Note:** When you rotate an image, the rectangle that holds the image maintains its original size, which may result in that the image exceeds the field border and therefore the parts that extend outside of the border will be cut off.

**X**

Specifies the X coordinate of the image.

**Y**

Specifies the Y coordinate of the image.

**Width**

Specifies the width of the image.

**Height**

Specifies the height of the image.

**Alt**

Specifies the alternate text which will be shown if the image cannot be displayed.

**Title**

Specifies tip information about the image, which will be displayed when the mouse pointer hovers on the image.

## Others

You can use this tab to view and configure some miscellaneous settings.

![Image Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4412139581079/imgprpty_other.gif)

**TOC Anchor**

Specifies whether or not to add the node that represents the image to the TOC tree that is displayed in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the image in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, the image will not be exported when you save the report result as an XLS file (make sure to check Data Format in the Export dialog).

**Export to CSV**

If true, the image will not be exported when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009687522-Group-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009713421-Insert-Aggregation)
