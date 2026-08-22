---
title: "Label Properties"
id: 45203967663245
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203967663245-Label-Properties
updated_at: 2026-04-30T14:09:57Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Label Properties

This topic describes how you can use the Label Properties dialog box to update the properties of a label in a web report. Server displays the dialog box when you right-click a label and select Properties from the shortcut menu.

This topic contains the following sections:

- General Tab Properties

- Font Tab Properties

- Border Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

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

Available when the label is related to a field. By default, this property is selected. Server automatically maps the label text to the dynamic display name of the field and ignores the text you specified in the Text  box.

Width

Specify the width of the object.

Height

Specify the height of the object.

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

Rotation(deg):

Specify the rotation degree of the text.

Top Padding

Specify the space between the text of the object and its top border.

Bottom Padding

Specify the space between the text of the object and its bottom border.

Left Padding

Specify the space between the text of the object and its left border.

Right Padding

 Specify the space between the text of the object and its right border.

Background

Specify the background color of the object.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range. 

Foreground

Specify the foreground color of the object.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

Artifact

Specifies whether to add an artifact tag when exporting to PDF.

## 
Font Tab Properties

Specify the font properties of the label.

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

Select if you want to add a shadow effect to the border. Web Report Studio and JDashboard cannot render the shadow effect. 

Shadow Color

Specify the color of the border shadow.
