---
title: "Text Box Properties"
id: 12480378465421
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480378465421-Text-Box-Properties
updated_at: 2025-05-30T02:59:29Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Text Box Properties 

You can use the Text Box Properties dialog box to edit the properties of a text box. This topic describes the properties in the dialog box.

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

Specify the general properties of the text box.

Name

Specify the display name of the text box, which shows on its shortcut menu. 

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

Vertical Alignment

Specify vertical justification of the text in the text box.

Vertical Auto Size

Select true to automatically adjust the height of the text box according to the size of the components in the text box.

Position

        Select the position mode of the component when it is directly contained in the report body, a tabular cell, or a text box.
        

- 
absolute
Server locates the component  at the position that you specify by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance, it is not affected when you insert text before it.
 The position of an object in a banded object can only be absolute.

- 
static
Server positions the component at the location where you insert it. The X and Y coordinate properties are disabled. You cannot move the component to another position other than by moving its insertion point. This can happen when the text flow preceding the insertion point expands.

- 
relative
Server positions the component at an offset to the position at which you insert it. The offset is determined by the X and Y coordinate property values. This value is not available for some types of components.

 Server displays relative in the default value list for the Position option, when the current position is relative. However, relative is no longer available in the value list after you apply static or absolute and reenter the dialog box.

X

Specify the X coordinate of the text box.

Y

Specify the Y coordinate of the text box.

Width

Specify the width of the text box.

Height

Specify the height of the text box.

Background

Specify the background color of the text box.

To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

## 
Border Tab Properties

Specify the border properties of the text box. 

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

TOC Anchor

Select true if you want to add the object to the TOC tree in the TOC Browser.

Suppress When No Records

Select true if you want to hide the object in the report when no record returns to its parent data component. 

Export to XLS

Select true if you want to export the object when you save the report as an XLS file (make sure to check Data Format in the Export dialog box).

Export to CSV

Select true if you want to export the object when you save the report as a TXT file with Delimited Format.

Previous Topic  Next Topic
