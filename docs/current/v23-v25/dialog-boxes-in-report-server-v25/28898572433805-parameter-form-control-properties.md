---
title: "Parameter Form Control Properties"
id: 28898572433805
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898572433805-Parameter-Form-Control-Properties
updated_at: 2026-02-26T02:11:48Z
source_host: docs-report.zendesk.com
---
# 
Parameter Form Control Properties 

You can use the Parameter Form Control Properties dialog box to edit the properties of a parameter form control. This topic describes the properties in the dialog box.

This topic contains the following sections:

- General Tab Properties

- Border Tab Properties

- Title Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
General Tab Properties

Specify the general properties of the parameter form control.

Name

Specify the name of the parameter form control.

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

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

Specify the X coordinate of the parameter form control.

Y

Specify the Y coordinate of the parameter form control.

Width

Specify the width of the parameter form control.

Height

Specify the height of the parameter form control.

Background

Specify the background color of the parameter form control.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

Show Title

Select if you want to show the title of the parameter form control. 

## 
Border Tab Properties

Specify the border properties of the parameter form control.

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

Specify the title properties of the parameter form control. This tab is available when you select Show Title on the General tab.

Text

Specify the text of the title.

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

Bold

Select true to make the text bold.

Underline

Select true to underline the text.

Italic

Select true to make the text italic.
