---
title: "Banded Panel Properties"
id: 5741428347415
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741428347415-Banded-Panel-Properties
updated_at: 2022-10-31T17:17:15Z
---

# Banded Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741434211351-Banded-Object-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741443946135-Bind-Data-Dialog-Box-Properties)

# Banded Panel Properties

You can use the Banded Panel Properties dialog box to update the properties of a banded panel in a web report. This topic describes the properties in the dialog box.

Server displays the dialog box when you right-click a banded panel and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Border Tab Properties](#Border)
* [Export Tab Properties](#Export)
* [Others Tab Properties](#Others)

You see these elements on all the tabs:

**OK**

Select to apply any changes you made here and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## General Tab Properties

Specify the general properties of the banded panel.

![Banded Panel Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905756583703/bdpnlprpty_gnrl.gif)

**Name**

Specify the display name of the panel.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Width**

Specify the width of the panel in inches.

**Height**

Specify the height of the panel in inches.

**Background**

Specify the background color of the panel.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

## Border Tab Properties

Specify the border properties of the banded panel.

![Banded Panel Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/9905734751255/bdpnlprpty_border.gif)

**Color**

Specify the border color.

**Width**

Specify the border width in inches.

**Top Line**

Select the style of the top border line.

**Bottom Line**

Select the style of the bottom border line.

**Left Line**

Select the style of the left border line.

**Right Line**

Select the style of the right border line.

## Export Tab Properties

Configure the export settings.

![Banded Panel Properties dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/9905734771095/bdpnlprpty_expt.gif)

**Export to CSV**

Select if you want to include the object in the Text output with Delimited Format.

**Export to Excel**

Select if you want to include the object in the Excel output.

**Export to HTML**

Select if you want to include the object in the HTML output.

**Export to PDF**

Select if you want to include the object in the PDF output.

**Export to PostScript**

Select if you want to include the object in the PostScript output.

**Export to Report Result**

Select if you want to include the object when opening the report in Web Report Result.

**Export to RTF**

Select if you want to include the object in the RTF output.

**Export to Text**

Select if you want to include the object in the Text output without Delimited Format.

**Export to XML**

Select if you want to include the object in the XML output.

## Others Tab Properties

Configure other settings.

![Banded Panel Properties dialog box - Others tab](https://devnet.logianalytics.com/hc/article_attachments/9905756655639/bdpnlprpty_othr.gif)

**Suppress**

Select if you want to hide the panel in the report. Server will skip all formulas and calculations.

This property is available to the following panels in a banded object: banded header/footer panel, banded page header/footer panel, group header/footer panel, and detail panel.

**Suppress Blank Panel**

Select if you want to hide the panel in the report when it contains no contents.

This property is available to the following panels in a banded object: banded header/footer panel, banded page header/footer panel, group header/footer panel, and detail panel.

**Suppress When No Records**

Select if you want to hide the panel in the report when no record returns to its parent data component.

This property is available to the following panels in a banded object: banded header/footer panel, banded page header/footer panel, group header/footer panel, and detail panel.

**Underlay**

Select if you want to layer the panel beneath the next panel in the banded object. You can use a panel layered beneath a subsequent panel to contain a background picture or watermark. However, you cannot layer banded page header, page footer, or group footer panels.

This property is available to the following panels in a banded object: banded header/footer panel, banded page header/footer panel, group header/footer panel, and detail panel.

**Fill Whole Page**

Select if you want to extend the panel to the bottom of the page, so that the next panel starts on a new page.

This property is available to the following panels in a banded object: banded header/footer panel, group header/footer panel, and detail panel.

**On New Page**

Select if you want the panel to start on a new page. This property works only when you enable the page layout of the report. The default behavior is that the panel starts on a new page only if the previous page is filled.

This property is available to the following panels in a banded object: banded header/footer panel, group header/footer panel, and detail panel.

**Cross Page**

Select if you want to split the panel across a page break. This property works only when you enable the page layout of the report.

This property is available to the following panels in a banded object: banded header/footer panel, group header/footer panel, and detail panel.

[**Tile Detail Panel**](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#TileDetailPanel)

Select if you want to tile records in the detail panel. This property is available only to the detail panel in a banded object.

For a vertical banded object, you can tile each set of records in the detail panel, by selecting this property and also setting the detail panel's width/height equal to or less than 1/2 that of the banded object. The detail panel width defines the width of each record tile.

**Tile Horizontal**

When you select Tile Detail Panel, you can use the Tile Horizontal property to specify the direction for tiling records in the detail panel.

Select **Tile Horizontal** if you want to tile records first in the row, and then in the column. Clear the Tile Horizontal checkbox if you want to tile records first in the column, and then in the row.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741434211351-Banded-Object-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741443946135-Bind-Data-Dialog-Box-Properties)
