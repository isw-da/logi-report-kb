---
title: "Label Properties"
id: 28898546444173
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898546444173-Label-Properties
updated_at: 2026-02-26T02:14:16Z
source_host: docs-report.zendesk.com
---
# 
Label Properties 

You can use the Label Properties dialog box to edit the properties of a label. This topic describes the properties in the dialog box.

This topic contains the following sections:

- General Tab Properties

- Font Tab Properties

- Border Tab Properties

- Others Tab Properties

- Display Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
General Tab Properties

Specify the general properties of the label.

Name

Specify the display name of the label.

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

Text

Specify the text of the label.

Auto Map Field Name

Server enables this property when the label is related to a field. Select true if you want to automatically map the label text to the dynamic display name of the field. Server then ignores the contents in the Text field. 

Position

- 
absolute

Server locates the component  at the position that you specify by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance, it is not affected when you insert text before it.
 The position of an object in a banded object can only be absolute.

- 
rotation(deg)

Specify the rotation degree of the text. 

- 
static

Server positions the component at the location where you insert it. The X and Y coordinate properties are disabled. You cannot move the component to another position other than by moving its insertion point. This can happen when the text flow preceding the insertion point expands.

- 
relative

Server positions the component at an offset to the position at which you insert it. The offset is determined by the X and Y coordinate property values. This value is not available for some types of components.

 Server displays relative in the default value list for the Position option, when the current position is relative. However, relative is no longer available in the value list after you apply static or absolute and reenter the dialog box.

X

Specify the X coordinate of the label.

Y

Specify the Y coordinate of the label.

Width

Specify the width of the label.

Height

Specify the height of the label.

Top Padding

Specify the space between the text of the object and its top border.

Bottom Padding

Specify the space between the text of the object and its bottom border.

Left Padding

Specify the space between the text of the object and its left border.

Right Padding

 Specify the space between the text of the object and its right border.

Background

Specify the background color of the label.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

Foreground

Specify the foreground color of the label.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

Arifact

Specifies whether to add an artifact tag when exporting to PDF.

## 
Font Tab Properties

Specify the font properties of the label text. 

Font

Select the font face of the text. 

Size

Specify the font size of the text.

Horizontal Alignment

Select the horizontal alignment mode of the text in the object.

Vertical Alignment

Select the vertical alignment mode of the text in the object.

Bold

Enable this property if you want to make the text bold.

Italic

Enable this property if you want to make the text italic.

Underline

Enable this property if you want to underline the text.

Strikethrough

Enable this property if you want to attach a strikeout line to the text.

Autofit

Enable this property if you want to automatically expand the object width according to the maximum length of the contents.

Reduce Width When Autofit

Enable this property if you want to reduce the width of the object according to its content when you specify to automatically adjust its width (the object's Autofit being true) and the actual width of the content is smaller than that of the object. 

 This property takes effect when you set Position of the object to absolute; but, it does not work if the Word Wrap property of the object is true.

Word Wrap

Enable this property if you want to wrap the text to the object width.

Ignore HTML Tag

Enable this property if you don't want Report Engine to parse the HTML tag elements in the text, at runtime or in the HTML output, so they display exactly as what they are in the report. 

Disable this property if you want Engine to transfer the HTML tag elements to the web browser so the web browser translates them into HTML.

## 
Border Tab Properties

Specify the border properties of the label.

Color

Specify the border color.

Width

Specify the border width in inches.

Top Line

Select the style of the top border line.

Bottom Line

Select the style of the bottom border line.

Left Line

Select the style of the left border line.

Right Line

Select the style of the right border line.

Shadow

Select true if you want to add a shadow effect to the border.

Shadow Color

Specify the color of the border shadow. To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

## 
Others Tab Properties

You can use this tab to view and configure some miscellaneous settings.

TOC Anchor

Select true if you want to add the object to the TOC tree in the TOC Browser.

Suppress When No Records

Select true if you want to hide the object in the report when no record returns to its parent data component. 

Export to XLS

Select true if you want to export the object when you save the report as an XLS file (make sure to check Data Format in the Export dialog box).

Export to CSV

Select true if you want to export the object when you save the report as a TXT file with Delimited Format.

Logic Column

You see this property when the object is in a table. Select next visible column if you want to show the object in the next visible table cell in the same row when you have hidden the column that holds the object.

## 
Display Tab Properties

Use this tab to modify the display type of the label. For more information, see Data Field Properties.
