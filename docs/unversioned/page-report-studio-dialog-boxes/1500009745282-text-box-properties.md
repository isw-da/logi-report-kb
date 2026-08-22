---
title: "Text Box Properties"
id: 1500009745282
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745282-Text-Box-Properties
updated_at: 2021-07-24T00:49:00Z
---

# Text Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745202-Tabular-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745262-Top-N-Dialog-Box-Properties)

# Text Box Properties

You can use the Text Box Properties dialog box to edit the properties of a text box. This topic describes the options in the dialog box.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Border Tab Properties](#Border)
* [Others Tab Properties](#Others)

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General Tab Properties

This tab shows some general information of the text box.

![Text Box Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880469911/txtbxprpty_gnrl.gif)

**Name**

Specifies the display name of the text box, which will be shown on its shortcut menu.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it.

If you select this option, it takes effect only when you have not modified the display name of the object.

**Vertical Alignment**

Specifies vertical justification of the text in the text box.

**Vertical Auto Size**

Specifies whether to automatically adjust the height of the text box according to the size of the components inserted.

**Position**

Displays the position mode of the component. If the component is directly contained in the report body, a tabular cell, or a text box, you can modify its position mode.

* **Absolute**  
  Logi Report will decide the component's position by its X and Y property values.
* **Static**  
  Logi Report will position the component at the default location in its container. It will also hide or disable the X, Y, and other position-related properties.

**X**

Specifies the X coordinate of the text box.

**Y**

Specifies the Y coordinate of the text box.

**Width**

Specifies the width of the text box.

**Height**

Shows the height of the text box.

**Background**

Specifies the background color of the text box.

To change the color, select the color indicator to bring out the [Select Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009745022-Select-Color-Dialog-Box-Properties) dialog box and then specify a new color, or type a color string in the format #RRGGBB. If you want to make the background transparent, type Transparent in the text box.

## Border Tab Properties

This tab shows information about borders of the text box.

![Text Box Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404880470167/txtbxprpty_border.gif)

**Color**

Specifies the border color.

**Width**

Specifies the border width.

**Top Line**

Specifies the style of the top border line.

**Bottom Line**

Specifies the style of the bottom border line.

**Left Line**

Specifies the style of the left border line.

**Right Line**

Specifies the style of the right border line.

## Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

![Text Box Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404880470551/txtbxprpty_other.gif)

**TOC Anchor**

Specifies whether to add the node that represents the text box to the TOC tree in the TOC Browser.

**Suppress When No Records**

Specifies whether to display the text box in the report result when no record is returned to its parent data component.

**Export to XLS**

If true, Server will export the component when you save the report result as an XLS file (make sure to check **Data Format** in the Export dialog box).

**Export to CSV**

If true, Server will export the component when you save the report result as a TXT file with Delimited Format selected.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745202-Tabular-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745262-Top-N-Dialog-Box-Properties)
