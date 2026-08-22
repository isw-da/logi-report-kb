---
title: "Image Properties"
id: 1500009772561
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772561-Image-Properties
updated_at: 2021-07-24T00:49:11Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744602-Group-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744622-Insert-Aggregation-Dialog-Box-Properties)

# Image Properties

Make updates using the Image Properties dialog box to edit the properties of an image. This topic describes how to update Image Properties.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Others Tab Properties](#Others)

You see these elements on both tabs:

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

**Help**

Select **Help** to view information about the Image Properties dialog box.

## General Tab Properties

Use this tab to view and configure general image settings.

![Image Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880497431/imgprpty_gnrl.gif)

**Name**

You can update the image name that is displayed in the app.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Picture Name**

Image file name.

**Scaling Mode**

* **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off.
* **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of Max Ratio.
* **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Max Ratio.
* **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Max Ratio.
* **customize** - Select to adjust the image according to the width and height that you specify in the Width and Height text boxes, regardless of Max Ratio.

**Horizontal Alignment**

Select left, right, or center for the horizontal alignment of the image in its container.

**Vertical Alignment**

Select top, bottom, or center for the vertical alignment of the image in its container.

**Rotation**

Type a degree to rotate the image at a specified angle.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)As you rotate the image, it is possible that parts of the image exceed the image area. Logi Report does not display the parts of the image that go beyond the image area.

**X**

X coordinate of the image.

**Y**

Y coordinate of the image.

**Width**

Width of the display area.

**Height**

Height of the display area.

**Alt**

Alternate text of the image. Logi Report will display the alternate text when it cannot display the image.

**Title**

Tip information about the image, which Logi Report will display when the mouse pointer hovers on the image.

## Others Tab Properties

Use this tab to view and configure miscellaneous settings.

![Image Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404880497687/imgprpty_other.gif)

**TOC Anchor**

Specify whether to add the node that represents the image to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specify whether to display the image in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744602-Group-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744622-Insert-Aggregation-Dialog-Box-Properties)
