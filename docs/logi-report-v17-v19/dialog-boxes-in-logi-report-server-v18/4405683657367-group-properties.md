---
title: "Group Properties"
id: 4405683657367
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683657367-Group-Properties
updated_at: 2022-01-27T07:58:43Z
---

# Group Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683631895-Formula-Editor-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690509079-Image-Properties)

# Group Properties

You can use the Group Properties dialog box to edit the properties of a group object. This topic describes the properties in the dialog box.

Server displays this dialog box when you right-click the group header or footer in a banded object and select **Group**.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Others Tab Properties](#Others)

You see these elements on both tabs:

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## General Tab Properties

Specify the general properties of the group object.

![Group Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420461704471/grpprpty_gnrl.gif)

**Expand Detail Data**

Select **true** to expand the detailed records in the group level.

**Keep Group Together**

Select **true** to try to keep a group wholly in a report page (try not to make a group across two pages).

**Repeat While Group Footer**

Select **true** to repeat the group header if a page break occurs on the group footer when you set the group header to be repeated.

**Shrink Footer**

Select **true** to shrink the group footer when you shrink detailed records in the group level.

**Special Function**

Specify a special function for the group level to group. This property is available only when the group field is of the Date/Time type.

**Select Type**

Specify the type for the Select N condition:

* **ALL**  
  Select to retrieve all groups.
* **TOP\_N**  
  Select to display the first N groups of the group level. Here N is the integer you type in the Select N text box.
* **BOTTOM\_N**  
  Select to display the last N groups of the group level. N is the integer you type in the Select N text box.

**Select N**

When **Select Type** is not **ALL**, you can type an integer in the Select N text box, to indicate the number of groups you want to display.

**Sort**

Select a sort direction for the groups of the group level.

## Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

![Group Properties dialog box - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4420453635223/grpprpty_other.gif)

**TOC Anchor**

Select **true** if you want to add the object to the TOC tree in the TOC Browser.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683631895-Formula-Editor-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690509079-Image-Properties)
