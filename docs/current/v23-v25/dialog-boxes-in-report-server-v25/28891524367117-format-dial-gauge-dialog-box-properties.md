---
title: "Format Dial Gauge Dialog Box Properties"
id: 28891524367117
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891524367117-Format-Dial-Gauge-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:50Z
source_host: docs-report.zendesk.com
---
# 
Format Dial Gauge Dialog Box Properties

This topic describes how you can use the Format Dial Gauge dialog box to format a dial gauge chart. Server displays the dialog box when you right-click on a dial gauge chart and select Format Graph from the shortcut menu.

This topic contains the following sections:

- Circular Graph Tab Properties

- Axis Tab Properties

- Pointer Tab Properties

- Target Tab Properties

- Frame Tab Properties

- Range Color Tab Properties

- Hint Tab Properties

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
Circular Graph Tab Properties

Specify the properties for dials in the dial gauge chart.

Circular

Specify the size of the dials.

- 
Angle
    Specify the degree for angles of the dials. Select the angle of the gauge from the drop-down list, or select Customized to open the Customize Gauge Angle dialog box to specify the start angle and end angle.

- 
Thickness
    Specify the thickness of the dials, in inches.

- 
Hole Size
    Specify the relative size of a dial in a percentage of total dial size.

- 
Start Style
    Specify the style of the start graph of the dials.

- 
End Style 
    Specify the style of the end graph of the dials.

Border

Specify the properties for the border of the dials. 

- 
Line Style

Specify the line style you want to apply to the border.

- 
Border Type

    Specify the type of the border.

- 
Color

    Specify the color of the border. To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

- 
Transparency

  Specify the transparency for color of the border.

- 
Thickness

    Specify the thickness of the border, in inches.

Show Range Name

Select if you want to show the names of the ranges defined in the Range Color tab. Then, you can use the following font properties to specify the format of the name text.

- 
Font
    Select the font face of the text.

- 
Size
    Specify the font size of the text.

- 
Fill Type
       Select the fill type of the text: none, color, texture, or gradient.

- 
Color
    Specify the font color of the text. 

- 
Font Style
    Specify the font style of the text: plain, bold, italic, or bold italic.

- 
Transparency
    Specify the color transparency of the text.

## 
Axis Tab Properties

The tab consists of four sub tabs: Axis, Tick Mark, Label, and Format.

### 
Axis

Specify the properties of the axis in the dial gauge.

Show Axis 

Select if you want to show the axis in the dial gauge.

Type

Specify the position relationship of the axis and the dials.

- 
Inside
    Select if you want to display the axis inside the dials.

- 
Outside
 Select if you want to display the axis outside the dials.

- 
Center
 Select if you want to display the axis in the center of the dials. 

Option

Specify the values you want to display on the axis.

- 
Minimum Value
    Specify the minimum value of the axis. You can also use a formula to control the property.

- 
Maximum Value
    Specify the maximum value of the axis. You can also use a formula to control the property.

Line

Specify the properties of the axis line.

- 
Color

    Specify the color of the line.

- 
Style

Select the style of the line.

- 
Transparency

    Specify the transparency for the color of the line.

- 
Thickness

  Specify the thickness of the line.

- 
Use Range Color

    Select to use the color you define for the ranges as the line color. In this case, Server disables the Color and Transparency properties. 

Gap

- 
Circular Axis Gap 
  Specify the gap between the axis and the dials if the axis is inside or outside of the dials.

### 
Tick Mark

Specify the properties of the tick marks on the axis.

Type

Specify the type of the tick marks on the axis.

- 
None
    Select if you don't want to display the tick marks on the axis. It is meaningless to specify all the other tick mark related properties when you select this type.

- 
Inside
    Select to display the tick marks inside the axis.

- 
Outside
    Select to display the tick marks outside the axis.

- 
Center
    Select to display the tick marks in the center of the axis.

Major Tick Mark Line 

Specify the properties of the major tick mark line.

- 
Correlate with Axis 

 Select if you want the line properties of the major tick marks to correlate with that of the axis automatically.
    

- 
Color

        Specify the color of the major tick mark line. Server disables this property when you select Use Range Color on the Axis > Axis tab.

- 
Style

        Select the style of the major tick mark line.

- 
Transparency

        Specify the color transparency of the major tick mark line. Server disables this property when you select Use Range Color on the Axis > Axis tab.

- 
Thickness

        Specify the thickness of the major tick mark line.

- 
Increment

    Specify the distance between two adjacent major tick marks on the axis.

- 
Number of Tick Marks 

    Specify the number major tick marks you want to display on the axis.

- 
Tick Mark Length 

    Specify the length of the major tick mark line, in inches.

Minor Tick Mark Line

Specify the properties of the minor tick mark line.

- 
Correlate with Axis

    Select if you want the line properties of the minor tick marks to correlate with that of the axis automatically.
    

- 
Color

        Specify the color of the minor tick mark line. Server disables this property when you select Use Range Color on the Axis > Axis tab.

- 
Style

        Select the style of the minor tick mark line.

- 
Transparency

        Specify the color transparency of the minor tick mark line. Server disables this property when you select Use Range Color on the Axis > Axis tab.

- 
Thickness

        Specify the thickness of the minor tick mark line.

- 
Increment

    Specify the distance between two adjacent minor tick marks on the axis.

- 
Number of Tick Marks 

Specify the number of minor tick marks you want to display on the axis.

- 
Tick Mark Length 

    Specify the length of the minor tick mark line, in inches.

### 
Label

Specify the properties of the major tick mark labels.

Option

Specify the type of the labels. 

- 
None
    Select if you don't want the labels to show.

- 
Normal
    Select if you want to customize the labels.
    
- 
Label Every N Major Tick Marks
          Specify the frequency at which you want to label the major tick marks.

- 
Number of Major Labels
        Specify the number of major tick mark labels to display on the axis.
        
- 
Auto
              Select to display all major tick mark labels.

- 
Fixed
 Select and then specify the number of the major tick mark labels to display on the axis.

- 
Range Value
 Select if you want the labels to show the range values you define.

- 
Min and Max Value
 Select if you want the labels to show the minimum value and maximum value you define on the Axis > Axis tab.

Gap

Specify the gap properties for the data labels.

- 
Label Axis Gap 

    Specify the distance between the data labels and the axis, in inches.

- 
Best Effect

    Select to adjust the data labels automatically to place them in the best positions. In this case, Server hides some labels when they overlap.

Font

Specify the font format of text in the data labels.

- 
Font

    Select the font face of the text.

- 
Size

    Specify the font size of the text.

- 
Fill Type

    Select the fill type of the text: none, color, texture, or gradient.

- 
Color 

    Specify the font color of the text. Server disables this property when you select Use Range Color on the Axis > Axis tab.

- 
Font Style

    Select the font style of the text: plain, bold, italic, or bold italic.

- 
Transparency

    Specify the color transparency of the text. Server disables this property when you select Use Range Color on the Axis > Axis tab.

Orientation

- 
Angle
    Specify the rotation angle of the data labels.

### 
Format

Specify the data format of the major tick mark labels. See Format.

## 
Pointer Tab Properties

Specify the properties of the pointers in the dial gauge.

Pointer Style 

Specify the style of the pointers.

- 
Arrow
    Select if you want to use arrow as the pointer style.
    
- 
Value Pointer
        Specify the style of the value pointers. Select a style from the drop-down list, or select Customized to specify another image as the value pointers in the Insert Image dialog box.

- 
Width 
        Specify the width of the arrow.

- 
Height 
        Specify the height of the arrow.

- 
Mark
 Select if you want to use mark as the pointer style.
    
- 
Value Pointer
        Specify the style of the value pointers. Select a style from the drop-down list, or select Customized to specify another image as the value pointers in the Insert Image dialog box.

- 
Width
        Specify the width of the marks.

- 
Height
        Specify the height of the marks.

- 
Position
        Specify the position relationship of the marks and the dial.

- 
Gap
        Specify the distance between the pointer and the dial, in inches.

- 
Style List
    Select to open the Style List dialog box to specify the style for pointers in the same data series respectively.

Pointer Color

Specify color properties of the pointers.

- 
Color
    Specify the color of the pointers. 
  

- 
Color List 
    Select to open the Color List dialog box to specify the pointer color.

- 
Transparency
    Specify the transparency for color of the pointers.

- 
Use Range Color
    Select if you want to use the color defined for the ranges as the pointer color. Then, Server disables the preceding three properties.

Pointer Value

Specify the pointer value properties.

- 
Show Pointer Value 
    Select if you want to show the pointer values.  
      - 
Position
          Select the position relationship between the values and the pointers. If you select customized, the X and Y settings in the General tab of the Format Pointer Label dialog box will take effect.

Pointer Border

Specify the pointer border properties. 

- 
Show Pointer Border
    Select if you want to show the border of the pointers. Then, Server enables the following border properties.
      
- 
Line Style
Specify the line style you want to apply to the border.

- 
Color
          Specify the color of the border.

- 
Transparency
Specify the transparency for color of the border.

- 
Thickness
Specify the weight of the border, in inches.

## 
Target Tab Properties

Specify the properties of the target in the dial gauge.

Use Target Value

Select if you want to use the target value for the dial gauge. 

- 
Target Value 
    Specify the target value. You can also use a formula to control the value.

Pointer Style 

Specify the pointer style for the target value.

- 
Target Pointer
  Specify the style of the target pointer. Select a style from the drop-down list, or select Customized to specify another image as the target pointer in the Insert Image dialog box.

- 
Width
    Specify the width of the target pointer.

- 
Height
    Specify the height of the target pointer.

- 
Position
    Specify the position of the target pointer relative to the dial.

- 
Gap
    Specify the distance between the target pointer and the dial.

Pointer Color 

Specify color properties of the target pointer. 

- 
Color
    Specify the color of the target pointer.

- 
Transparency
    Specify the transparency for color of the target pointer.

Target Value

Specify the properties of the target value.

- 
Show Target Value
    Select if you want to show the target value on the dial gauge.
    - 
Position
          Select the position of the target value relative to the dial. If you select customized, the X and Y settings in the General tab of the Format Target Label dialog box will take effect.

## 
Frame Tab Properties

Specify the properties for the frame of the dial gauge chart.

Size

Specify the size properties of the frame.

- 
Frame Size 
    Specify the size of the frame.

Fill

Specify the color and transparency of the frame.

- 
Fill
    Specify the color to fill the frame.

- 
Transparency
    Specify the transparency of the color to fill the frame.

Border

Specify the properties for the border of the frame.

- 
Line Style

Specify the line style you want to apply to the border.

- 
Border Type

    Specify the type of the border.

- 
Color

    Specify the color of the border. To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

- 
Transparency

  Specify the transparency for color of the border.

- 
Thickness

    Specify the thickness of the border, in inches.

Gauge Group Name 

Specify the properties for the gauge group name.

- 
Show Gauge Group Name 
    Select if you want to show names for the arcs in the dial gauge which are values of the field on its category axis. If the dial gauge contains no category field, the group name shows Report by default.
    - 
Position
          Select the position of the names relative to the dial.  If you select customized, the X and Y settings in the General tab of the Format Gauge Label dialog box will take effect.

## 
Range Color Tab Properties

Specify different colors to fill the dials in dial gauge in different ranges.

Add buttonSelect to add a new color range.

Remove button

Select to remove the selected color range.

Minimum

Specify the minimum value of the range.

Maximum

Specify the maximum value of the range.

Color

Specify the color schema of the range. 

Select in the color cell. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

Name

Specify the name of a range.

Others

Specify the properties for values that do not fall into any of the ranges you define.

- 
Name

Specify the name for the values.

- 
Color

    Specify the color for the values. To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

## 
Hint Tab Properties

Specify the properties of the data marker hint.

Show Category and Series

Select to include the category and series values in the data marker hint.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart.
