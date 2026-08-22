---
title: "Filter Control Properties"
id: 28898508182669
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898508182669-Filter-Control-Properties
updated_at: 2026-02-26T02:14:15Z
source_host: docs-report.zendesk.com
---
# 
Filter Control Properties 

You can use the Filter Control Properties dialog box to edit the properties of a filter control. This topic describes the properties in the dialog box.

This topic contains the following sections:

- General Tab Properties

- Font Tab Properties

- Border Tab Properties

- Title Tab Properties

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
General Tab Properties

You can specify the general information of the filter control.

Name

Specify the name of the filter control.

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

Format

Specify the field value format in the filter control. 

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The value auto means that the setting follows that of the parent data container. When you set the property to true, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Report will ignore the Auto Scale in Number setting.

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

Filter On

Server displays the fields that the filter control is based on. You can select the ellipsis button  to open the Edit Filter Control dialog box.

X

Specify the X coordinate of the filter control.

Y

Specify the Y coordinate of the filter control.

Width

Specify the width of the filter control, in inches.

Height

Specify the height of the filter control, in inches.

Background

Specify the background color of the filter control.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

Foreground

Specify the foreground color of the filter control.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

Show Title

Select to show the title of the filter control. 

Arifact

Specifies whether to add an artifact tag when exporting to PDF.

## 
Font Tab Properties

Specify the font properties of the text in the filter control.

Font

Select the font face of the text. 

Size

Specify the font size of the text. 

Bold

Select true to make the text bold.

Underline

Select true to underline the text.

Italic

Select true to make the text italic.

## 
Border Tab Properties

You can specify the border properties of the filter control.

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

## 
Title Tab Properties

You can specify the title properties of the filter control. This tab is available when you selected Show Title on the General tab of the dialog box.

Text

Server enables this property when you disable Auto Map Field Name. Type the text you want to display as the title.

When you add only one DBField to the text list filter control  and insert the On-screen Filter special field in a  data container that uses the same data resource as the DBField, Report also applies the text in the filter expression of the special field.

- 
Auto Map Field Name
  Select to automatically map the title text to the dynamic display name of a field bound with the filter control.

Background

Specify the background color of the title.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

Foreground

Specify the foreground color of the title.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

Font

Select the font face of the text. 

Size

Specify the font size of the text. 

Horizontal Alignment

Select the horizontal alignment mode of the text.

Title Height

Specify the height of the title, to ensure larger font sizes display without being cut off. Type a numeric value to change the height.

Bold

Select true to make the text bold.

Underline

Select true to underline the text.

Italic

Select true to make the text italic.
