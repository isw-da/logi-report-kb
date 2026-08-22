---
title: "Banded Object Properties"
id: 4405683791127
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683791127-Banded-Object-Properties
updated_at: 2022-01-27T07:59:10Z
---

# Banded Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690569495-Banded-Line-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690570391-Banded-Panel-Properties)

# Banded Object Properties

You can use the Banded Object Properties dialog box to update the properties of a banded object in a web report. This topic describes the properties in the dialog box.

Server displays the dialog box when you right-click a banded object and select **Properties** from the shortcut menu.

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

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)**Close button**

Select to close the dialog box without saving any changes.

## General Tab Properties

Specify the general properties of the banded object.

![Banded Object Properties dialog box - General tab](https://devnet.logianalytics.com/hc/article_attachments/4420447259927/bdobjprpty_gnrl.gif)

**Name**

Specify the display name of the banded object.

**Show NLS Value**

Select to show the translated name for the display name of the object in the **Name** text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

**Position**

Specify the position of the banded object.

* **absolute**  
   Select if you want to use the X and Y property values to decide the banded object's position.
* **static**  
   Select if you want to place the banded object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**X**

Specify the X coordinate of the banded object, in inches.

**Y**

Specify the Y coordinate of the banded object, in inches.

**Width**

Specify the width of the banded object, in inches.

**Height**

Specify the height of the banded object, in inches.

**Background**

Specify the background color of the banded object.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type **Transparent** in the text box.

## Border Tab Properties

Specify the border properties of the banded object.

![Banded Object Properties dialog box - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4420461664279/bdobjprpty_border.gif)

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

![Banded Object Properties dialog box - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4420453591063/bdobjprpty_expt.gif)

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

![Banded Object Properties dialog box - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4420453591447/bdobjprpty_othr.gif)

**Suppress**

Select if you want to hide the banded object in the report. Server will skip all formulas and calculations.

**Suppress When Empty**

Select if you want to hide the banded object in the report when it contains no contents.

**Suppress When No Records**

Select if you want to hide the banded object in the report when no record returns to its parent data component.

**Enable Navigation**

Select if you want to enable page navigation on the banded object. Then, if the banded object contains more than one page, Server displays a page navigation bar specific for the banded object under it, and you can use the bar to view the desired pages.
You can further specify the height and width of the page for the banded object to display multiple pages, by setting the following two properties. If you later you resize the banded object, Server will reset the two properties to the resized values.

* **Navigation Width**  
   Specify
  the display width of the banded object. Type a numeric value to specify the width. Leave it blank if you want Server to calculate the display width.
* **Navigation Height**Specify the display height of the banded object. Type a numeric value to specify the height. Leave it blank if you want Server to calculate the display height.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690569495-Banded-Line-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690570391-Banded-Panel-Properties)
