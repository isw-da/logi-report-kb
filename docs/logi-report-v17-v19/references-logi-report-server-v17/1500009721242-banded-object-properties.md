---
title: "Banded Object Properties"
id: 1500009721242
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009721242-Banded-Object-Properties
updated_at: 2021-07-25T07:19:31Z
---

# Banded Object Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748101-Banded-Line-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721262-Banded-Panel-Properties)

# Banded Object Properties

The Banded Object Properties dialog box is used to specify the properties of a banded object. It appears when you right-click a banded object and select Properties from the shortcut menu.

There are the following tabs in this dialog box: [General](#General), [Border](#Border), [Export](#Export) and [Others](#Others).

**OK**

Applies the banded object properties and closes this dialog box.

**Cancel**

Cancels the changes and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## General

This tab shows some general information of the banded object.

![Banded Object Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936869527/bdobjprpty_gnrl.gif)

**Name**

Specifies the display name of the banded object.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Position**

Specifies the position of the banded object.

* **absolute**  
   Specifies to use the X and Y property values to decide the banded object's position.
* **static**  
   Specifies to place the banded object at the default location in its container. Server will hide or disable the X, Y, and other position-related properties.

**X**

Specifies the X coordinate of the banded object, in inches.

**Y**

Specifies the Y coordinate of the banded object, in inches.

**Width**

Specifies the width of the banded object, in inches.

**Height**

Specifies the height of the banded object, in inches.

**Background**

Specifies the background color of the banded object.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

## Border

This tab shows information about borders of the banded object.

![Banded Object Properties dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404936873111/bdobjprpty_border.gif)

**Color**

Specifies the border color.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the color transparent, type Transparent in the text box.

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

![Banded Object Properties dialog - Export tab](https://devnet.logianalytics.com/hc/article_attachments/4404942557591/bdobjprpty_expt.gif)

**Export to CSV**

Specifies whether to include the banded object when you save the report result as a TXT file with Delimited Format selected.

**Export to Excel**

Specifies whether to include the banded object when exporting the report to Excel.

**Export to HTML**

Specifies whether to include the banded object when exporting the report to HTML.

**Export to PDF**

Specifies whether to include the banded object when exporting the report to PDF.

**Export to PostScript**

Specifies whether to include the banded object when exporting the report to PostScript.

**Export to Report Result**

Specifies whether to include the banded object in Web Report Studio or when the report is opened in Web Report Result.

**Export to RTF**

Specifies whether to include the banded object when exporting the report to RTF.

**Export to Text**

Specifies whether to include the banded object when exporting the report to Text with Delimited Format unselected.

**Export to XML**

Specifies whether to include the banded object when exporting the report to XML.

## Others

You can use this tab to configure other settings.

![Banded Object Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404942557847/bdobjprpty_othr.gif)

**Suppress**

Specifies whether to show the banded object in the report. All formulas and calculations will be skipped if the property is set to true.

**Suppress When Empty**

Specifies whether to display the banded object in the report result when no record is returned to it.

**Suppress When No Records**

Specifies whether to display the banded object in the report result when no record is returned to its parent data component.

**Enable Navigation**

Specifies whether to enable page navigation on the banded object. If it is set to true, if the banded object contains more than one page, a page navigation bar specific for the banded object will be available right below it. You can use the bar to view the desired pages.

When this property is set to true, you can further specify the height and width of the page for the banded object to display multiple pages, by setting the following two properties. If you later resize the banded object, the two properties will be reset to the resized values.

* **Navigation Width**  
   Specifies
  the width of the page for the banded object to display multiple pages. Type a numeric value to specify the width. If no value is given here, Logi Report will calculate the banded object page width.
* **Navigation Height**Specifies the height of the page for the banded object to display multiple pages. Type a numeric value to specify the height. If no value is given here, Logi Report will calculate the banded object page height.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748101-Banded-Line-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721262-Banded-Panel-Properties)
