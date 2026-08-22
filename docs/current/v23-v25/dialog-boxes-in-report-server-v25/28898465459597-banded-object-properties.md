---
title: "Banded Object Properties"
id: 28898465459597
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898465459597-Banded-Object-Properties
updated_at: 2026-02-26T02:11:26Z
source_host: docs-report.zendesk.com
---
# 
Banded Object Properties

You can use the Banded Object Properties dialog box to edit the properties of a banded object. This topic describes the properties in the dialog box.

This topic contains the following sections:

- General Tab Properties

- Border Tab Properties

- Others Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
General Tab Properties

Use this tab to update general information of the banded object.

Name

Specify the display name of the banded object.

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

Specify the X coordinate of the banded object, in inches.

Y

Specify the Y coordinate of the banded object, in inches.

Width

Specify the width of the banded object, in inches.

Height

Specify the height of the banded object, in inches.

Auto Fit

Select if you want to automatically adjust the width of a vertical banded object or the height of a horizontal banded object according to the contents. 

Background

Specify the background color of the banded object.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

If you want to make the background transparent, type Transparent in the text box.

## 
Border Tab Properties

Use this tab to specify border information of the banded object.

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
Others Tab Properties

Configure some miscellaneous settings.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

TOC Anchor

Select true if you want to add the object to the TOC tree in the TOC Browser.

Suppress When No Records

Select true if you want to hide the object in the report when no record returns to its parent data component. 

Export to XLS

Select true if you want to export the object when you save the report as an XLS file (make sure to check Data Format in the Export dialog box).

Export to CSV

Select true if you want to export the object when you save the report as a TXT file with Delimited Format.
