---
title: "Tabular Properties"
id: 5741389758487
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741389758487-Tabular-Properties
updated_at: 2022-10-31T17:16:35Z
---

# Tabular Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741440922135-Tabular-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741431809303-Text-Box-Properties)

# Tabular Properties

You can use the Tabular Properties dialog box to edit the properties of a tabular. This topic describes the properties in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Others Tab Properties](#Others)

You see these elements on both tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the tabular.

![Tabular Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905761516695/tblrprpty_gnrl.gif)

**Name**

Specify the display name of the tabular.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Vertical Auto Size**

Select **true** to automatically adjust the tabular height according to the size of the components in the tabular.

**Horizontal Auto Size**

Select **true** to automatically adjust the tabular width according to the size of the components in the tabular.

**Position**

Select the position mode of the object when it is directly contained in the report body, a tabular cell, or a text box.

* **Absolute**  
  Select if you want to use the X and Y property values to decide the object's position.
* **Static**  
  Select if you want to place the object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**X**

Specify the X coordinate of the tabular.

**Y**

Specify the Y coordinate of the tabular.

**Width**

Specify the width of the tabular.

**Height**

Specify the height of the tabular.

**Background**

Specify the background color of the tabular.

To change the color, select the color indicator to access the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties), and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

## Others Tab Properties

Configure some miscellaneous settings.

![Tabular Properties dialog box - Others tab](https://devnet.logianalytics.com/hc/article_attachments/9905773289111/tblrprpty_other.gif)

**TOC Anchor**

Select **true** if you want to add the object to the TOC tree in the TOC Browser.

**Suppress When No Records**

Select **true** if you want to hide the object in the report when no record returns to its parent data component.

**Export to XLS**

Select **true** if you want to export the object when you save the report as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

Select **true** if you want to export the object when you save the report as a TXT file with Delimited Format.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741440922135-Tabular-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741431809303-Text-Box-Properties)
