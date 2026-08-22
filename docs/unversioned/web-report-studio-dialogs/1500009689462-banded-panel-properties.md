---
title: "Banded Panel Properties"
id: 1500009689462
section: "Web Report Studio Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009689462-Banded-Panel-Properties
updated_at: 2021-11-03T06:57:29Z
---

# Banded Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009715581-Banded-Object-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715521-Bind-Data)

# Banded Panel Properties

The Banded Panel Properties dialog helps you to specify the properties of a banded panel and contains the following tabs: [General](#General), [Border](#Border), [Export](#Export) and [Others](#Others). This dialog appears when you right-click a banded panel and select Properties from the shortcut menu.

**OK**

Applies the banded panel properties and closes this dialog.

**Cancel**

Cancels the changes and closes this dialog.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4412139537431/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4412112572951/btn_close.gif)

Ignores the setting and closes this dialog.

## General

This tab shows some general information of the banded panel.

![Banded Panel Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4412139561879/bdpnlprpty_gnrl.gif)

**Name**

Specifies the display name of the panel.

**Show NLS Value**

Specifies to show the translated name for the display name of the panel in the Name text box if you have enabled the NLS feature and translated it.

If checked, this option takes effect only when the display name of the object is not modified.

**Width**

Specifies the width of the panel in inches.

**Height**

Specifies the height of the panel in inches.

**Background**

Specifies the background color of the panel.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range. You can also input a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, input Transparent in the text box.

## Border

This tab shows information about borders of the banded panel.

![Banded Panel Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4412131456279/bdpnlprpty_border.gif)

**Color**

Specifies the border color.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009715801-Color-Picker-) dialog in which you can select a color within a wider range. You can also input a color string in the format #RRGGBB directly in the text box. If you want to make the color transparent, input Transparent in the text box.

**Width**

Specifies the border width in inches.

**Top Line**

Specifies the style of the top border line.

**Bottom Line**

Specifies the style of the bottom border line.

**Left Line**

Specifies the style of the left border line.

**Right Line**

Specifies the style of the right border line.

## Export

You can use this tab to configure the export settings.

![Banded Panel Properties dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4412112603927/bdpnlprpty_expt.gif)

**Export to CSV**

Specifies whether to include the panel when you save the report result as a TXT file with Delimited Format selected.

**Export to Excel**

Specifies whether to include the panel when exporting the report to Excel.

**Export to HTML**

Specifies whether to include the panel when exporting the report to HTML.

**Export to PDF**

Specifies whether to include the panel when exporting the report to PDF.

**Export to PostScript**

Specifies whether to include the panel when exporting the report to PostScript.

**Export to Report Result**

Specifies whether to include the panel in Web Report Studio or when the report is opened in Web Report Result.

**Export to RTF**

Specifies whether to include the panel when exporting the report to RTF.

**Export to Text**

Specifies whether to include the panel when exporting the report to Text with Delimited Format unselected.

**Export to XML**

Specifies whether to include the panel when exporting the report to XML.

## Others

You can use this tab to configure other settings.

![Banded Panel Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4412139562135/bdpnlprpty_othr.gif)

**Suppress**

Specifies whether to show the panel in the report. All formulas and calculations will be skipped if the property is set to true. Available to the following panels in a banded object: banded header panel, banded footer panel, banded page header panel, banded page footer panel, group header panel, group footer panel and detail panel.

**Suppress Blank Panel**

Specifies whether a panel with no data is included in the report. The default is false which means an empty panel is shown. Available to the following panels in a banded object: banded header panel, banded footer panel, banded page header panel, banded page footer panel, group header panel, group footer panel and detail panel.

**Suppress When No Records**

Specifies whether to display the panel in the report result when no record is returned to its parent data component. Available to the following panels in a banded object: banded header panel, banded footer panel, banded page header panel, banded page footer panel, group header panel, group footer panel and detail panel.

**Underlay**

Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Available to the following panels in a banded object: banded header panel, banded footer panel, banded page header panel, banded page footer panel, group header panel, group footer panel and detail panel.

**Fill Whole Page**

Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Available to the following panels in a banded object: banded header panel, banded footer panel, group header panel, group footer panel and detail panel in a banded object.

**On New Page**

Specifies whether the panel starts on a new page. This property is applied only when the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Available to the banded header panel, banded footer panel, group header panel, group footer panel and detail panel in a banded object.

**Cross Page**

Specifies whether the panel can be split across a page break. This property is applied only when the report has page layout enabled. Available to the following panels in a banded object: banded header panel, banded footer panel, group header panel, group footer panel and detail panel.

[**Tile Detail Panel**](https://devnet.logianalytics.com/hc/en-us/articles/1500009718261-Detail-Panel#TileDetailPanel)

Specifies whether to tile records in the detail panel. Available only to the detail panel in a banded object.

For a vertical banded object, you can tile each set of records in the detail panel, by selecting this property and also setting the detail panel's width/height equal to or less than 1/2 that of the banded object. The detail panel width defines the width of each record tile.

**Tile Horizontal**

When you select Tile Detail Panel, you can use the Tile Horizontal property to specify the direction for tiling records in the detail panel.

Select **Tile Horizontal** if you want to tile records first in the row, and then in the column. Clear the Tile Horizontal checkbox if you want to tile records first in the column, and then in the row.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009715581-Banded-Object-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009715521-Bind-Data)
