---
title: "Tabular Properties"
id: 1500009745202
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745202-Tabular-Properties
updated_at: 2021-07-24T00:49:02Z
---

# Tabular Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773161-Tabular-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745282-Text-Box-Properties)

# Tabular Properties

You can use the Tabular Properties dialog box to edit the properties of a tabular. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Others Tab Properties](#Others)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows some general information of the tabular.

![Tabular Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404885541399/tblrprpty_gnrl.gif)

**Name**

Specifies the display name of the tabular.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Vertical Auto Size**

Specifies whether to automatically adjust the height of the tabular according to the size of the components inserted.

**Horizontal Auto Size**

Specifies whether to automatically adjust the width of the tabular according to the size of the components inserted.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

**X**

Specifies the X coordinate of the tabular.

**Y**

Specifies the Y coordinate of the tabular.

**Width**

Specifies the width of the tabular.

**Height**

Specifies the height of the tabular.

**Background**

Specifies the background color of the tabular.

To change the color, select the color indicator to access the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

## Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

![Tabular Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404885541783/tblrprpty_other.gif)

**TOC Anchor**

Specifies whether to add the node that represents the tabular to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the tabular in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773161-Tabular-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745282-Text-Box-Properties)
