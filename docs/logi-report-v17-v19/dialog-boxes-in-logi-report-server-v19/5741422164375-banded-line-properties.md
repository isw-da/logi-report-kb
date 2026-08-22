---
title: "Banded Line Properties"
id: 5741422164375
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741422164375-Banded-Line-Properties
updated_at: 2022-10-31T17:17:13Z
---

# Banded Line Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741443918871-Aggregate-On-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741434211351-Banded-Object-Properties)

# Banded Line Properties

You can use the Banded Line Properties dialog box to update the properties of a line in a banded object. This topic describes the properties in the dialog box.

Server displays the dialog box when you right-click a line in a banded object and select **Properties** from the shortcut menu.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Line Property Tab Properties](#Property)
* [Export Tab Properties](#Export)
* [Excel Tab Properties](#Excel)

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

Specify the general properties of the line.

![Banded Line Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/9905734917271/bdlineprpty_gnrl.gif)

**Name**

Specify the display name of the line.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Position**

Specify the position of the line.

* **absolute**  
   Select if you want to use the X and Y property values to decide the line's position.
* **static**  
   Select if you want to place the line at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**Top Attach Pos X**

Specify the horizontal coordinate of the upper left point of the line in a banded panel. A line can cross panels, and the coordinate indicates the relative position in the involved panel.

Web Report Studio only supports horizontal lines and vertical lines, so you need to ensure that the line you draw is horizontal or vertical.

**Top Attach Pos Y**

Specify the vertical coordinate of the upper left point of the line in a banded panel.

**Bottom Attach Pos X**

Specify the horizontal coordinate of the lower right point of the line in a banded panel.

**Bottom Attach Pos Y**

Specify the vertical coordinate of the lower right point of the line in a banded panel.

## Line Properties Tab Properties

Specify the line properties.

![Banded Line Properties dialog box - Line Properties tab](https://devnet.logianalytics.com/hc/article_attachments/9905756823831/bdlineprpty_prpty.gif)

**Line Color**

Specify the color of the line.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

If you want to make the color transparent, type **Transparent** in the text box.

**Line Thickness**

Specify the thickness of the line.

**Line Style**

Select the style of the line.

**Suppress When No Records**

Select if you want to hide the line in the report when no record returns to its parent data component.

## Export Tab Properties

Configure the export settings.

![Banded Line Properties dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/9905756866839/bdlineprpty_expt.gif)

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

## Excel Tab Properties

Configure the settings for the Excel output.

![Banded Line Properties dialog box- Excel tab](https://devnet.logianalytics.com/hc/article_attachments/9905735008919/bdlineprpty_excl.gif)

[**Bottom Attach Column**](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#Attach)

Specify the X coordinate of the lower-right corner of the line in the Excel output, measured in the number of cells.

[**Bottom Attach Row**](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#Attach)

Specify the Y coordinate of the lower-right corner of the line in the Excel output, measured in the number of cells.

[**Top Attach Column**](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#Attach)

Specify the X coordinate of the upper-left corner of the line in the Excel output, measured in the number of cells.

[**Top Attach Row**](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel#Attach)

Specify the Y coordinate of the upper-left corner of the line in the Excel output, measured in the number of cells.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741443918871-Aggregate-On-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741434211351-Banded-Object-Properties)
