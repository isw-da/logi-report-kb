---
title: "Format Bar Gauge Dialog Box Properties"
id: 45203911579149
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203911579149-Format-Bar-Gauge-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:22Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Format Bar Gauge Dialog Box Properties 

You can use the Format Bar Gauge dialog box to format a bar gauge chart. This topic describes the properties in the dialog box.

This topic contains the following sections:

- Staff Graph Tab Properties

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

Help

Select to view information about the dialog box.

## 
Staff Graph Tab Properties

Specify the properties for bars in the bar gauge.

Bar

Specify the properties of the bars.

- 
Layout
    Select the layout of the bars. It can be vertical or horizontal.

- 
Thickness
    Specify the thickness of the bars, in inches.

- 
Start Style
    Select the style for the start graph of the bars.

- 
End Style
    Select the style for the end graph of the bars. 

Border

Specify the properties of the bar border.

- 
Line Style
  Select the line style of the border.

- 
Thickness
    Specify the thickness of the border, in inches.

- 
Color
    Specify the color of the border. To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

- 
Transparency
  Specify the transparency for the border color.

Show Range Name

Select to show the names of the ranges you define on the Range Color tab. Then, you can continue to specify the font properties of the text in the range names. 

- 
Font
 Select the font face you want to apply to the text.

- 
Size
    Specify the font size of the text.

- 
Fill Type
    Select the fill type of the text: none, color, gradient, or texture.

- 
Color
    Specify the font color of the text. 

- 
Font Style
    Select the font style of the text: plain, bold, italic, or bold italic.

- 
Transparency
    Specify the color transparency of the text.

## 
Axis Tab Properties

The tab consists of four more tabs: Axis, Tick Mark, Label, and Format.

### 
Axis

Specify the properties of the axis in the bar gauge.

Show Axis 

Select to show the axis. 

Type

Specify the position relationship of the axis and the bar. When you set the Layout property to horizontal on the Staff Graph tab, you see these properties: 

- 
Top
    Select to display the axis on the top of the bar.

- 
Bottom
    Select to display the axis on the bottom of the bar.

- 
Center
    Select to display the axis in the center of the bar. 

When you set the Layout property to vertical on the Staff Graph tab, you see these properties:

- 
Left
    Select to display the axis on the left of the bar.

- 
Right
    Select to display the axis on the right of the bar.

- 
Center
    Select to display the axis in the center of the bar. 

Option

Specify the values you want to display in the chart.

- 
Minimum Value
    Specify the minimum value to display in the chart.

- 
Maximum Value
    Specify the maximum value to display in the chart.

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
Staff Axis Gap 
  Specify the gap between the axis and the bar when the axis is not in the center of the bar.

### 
Tick Mark

Specify the properties of the tick marks on the axis.

Type

Specify the position relationship of the axis and the tick marks. When you set the Layout property to horizontal on the Staff Graph tab, you see these properties:

- 
None
    Select if you don't want to display the tick marks on the axis. Then, ignore all the other tick mark related properties.

- 
Top
 Select to display the tick marks on the top of the axis. 

- 
Bottom
    Select to display the tick marks on the bottom of the axis.

- 
Center
    Select to display the tick marks in the center of the axis.

When you set the Layout property to vertical on the Staff Graph tab, you see these properties:

- 
None
       Select if you don't want to display the tick marks on the axis. Then, ignore all the other tick mark related properties.

- 
Left
    Select to display the tick marks on the left of the axis. 

- 
Right
    Select to display the tick marks on the right of the axis.

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
 Select and specify the number of the major tick mark labels to display on the axis.

- 
Range Value
 Select if you want the labels to show the range values you define.

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

Specify the properties of the pointers in the bar gauge.

Use Pointer

Select to use pointers to indicate values in the bar gauge.

- 
Pointer Style
    Specify the properties of the pointers.
    
- 
Value Pointer

        Specify the style of the value pointers. Select a style from the list, or select Customized to specify another image as the value pointers in the Insert Image dialog box.

- 
Width

        Specify the width of the pointers.

- 
Height

        Specify the height of the pointers.

- 
Position

        Select the position of the pointers relative to the bar.

- 
Gap

        Specify the distance between the pointers and the bar.

- 
Style List

             Select to open the Style List dialog box to specify the style for pointers in the same data series, respectively.

- 
Pointer Color

    Specify color properties of the pointers.
    

- 
Color

        Specify the color of the pointers.

- 
Color List 

        Select to open the Color List dialog box to specify the color pattern for pointers in the same data series, respectively.

- 
Transparency

        Specify the transparency for the color of the pointers.

- 
Use Range Color

       Select to use the color you define for the ranges as the pointer color. Then, Server disables the preceding three properties. 

- Pointer Value

- 
     Specify the properties for the values of the pointers.    

- 
Show Pointer Value

         Select to show the values for the pointers.
         

- 
Position

             Select the position relationship between the values and the pointers.  If you select customized, the X and Y settings on the General tab of the Format Pointer Label dialog box will take effect.

Use Color Bar

Select to use color bars to indicate values in the bar gauge. 

- 
Pointer Color

    Specify the properties of the color bars.
    

- 
Color

        Specify the color of the bars.

- 
Transparency

        Specify the transparency for the color of the bars.

- 
Thickness

        Specify the thickness of the color bars.

- 
Color List 

        Select to open the Color List dialog box to specify the color pattern for color bars in the same data series, respectively.

- 
Pointer Value

    Specify the properties for the values of the color bars.
    

- 
Show Pointer Value

        Select to show values for the color bars. 

- 
Position

        Select the position relationship between the values and the color bars. If you select customized, the X and Y settings on the General tab of the Format Pointer Label dialog box will take effect.

Pointer Border

Specify the properties of the pointer border. 

- 
Show Pointer Border

    Select to show the border of the pointers and enable the border properties.
      

- 
Line Style

Select the line style of the border.

- 
Color

          Specify the color of the border.

- 
Thickness

Specify the weight of the border, in inches.

- 
Transparency

Specify the transparency for the border color.

## 
Target Tab Properties

Specify the properties of the target in the bar gauge.

Use Target Value

Select to use the target value for the bar gauge. 

- 
Target Value 

    Specify the target value.

Pointer Style  

Specify the pointer style for the target value.

- 
Target Pointer

    Specify the style of the target pointer. Select a style from the list, or select Customized to specify another image as the target pointer in the Insert Image dialog box.

- 
Width

    Specify the width of the target pointer.

- 
Height

    Specify the height of the target pointer.

- 
Position

    Specify the position of the target pointer relative to the bar.

- 
Gap

    Specify the distance between the target pointer and the bar.

Pointer Color 

Specify the color properties of the target pointer. 

- 
Color

    Specify the color of the target pointer.

- 
Transparency

    Specify the transparency for the color of the target pointer.

Target Value

Specify the properties of the target value.

- 
Show Target Value 

    Select to display the target value on the bar gauge.
    

- 
Position

        Select the position of the target value relative to the bar. If you select customized, the X and Y settings on the General tab of the Format Target Label dialog box will take effect.

## 
Frame Tab Properties

Specify the properties for the frame of the bar gauge chart.

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

Select the line style of the border.

- 
Border Type

    Select the type of the border.

- 
Color

    Specify the color of the border. To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

- 
Transparency

  Specify the transparency for the color of the border.

- 
Thickness

    Specify the thickness of the border, in inches.

Gauge Group Name 

Specify the properties for the gauge group name.

- 
Show Gauge Group Name 

    Select to display names for the bars in the bar gauge which are the values of the field on its category axis. If the bar gauge contains no category field, the group name shows Report by default.
    

- 
Position

        Select the position of the names relative to the bars. If you select customized, the X and Y settings on the General tab of the Format Gauge Label dialog box will take effect.

## 
Range Color Tab Properties

Specify different colors to fill the bars in the bar gauge in different ranges.

Use Gradient Effect

Select to use gradient effect for the color.

Add button

Select to add a new color range.

Remove button

Select to remove the selected color range.

Range table

- 
Minimum

Specify the minimum value of a range.

- 
Maximum

Specify the maximum value of a range.

- 
Color

Select the color cell to open the Select Color dialog box, and specify a new color.

- 
Name

Specify the name of a range.

Others

Specify the properties for values that do not fall into any of the ranges you define in the range table.

- 
Name

Specify the name for the values.

- 
Color

    Specify the color for the values. To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

## 
Hint Tab Properties

Specify the properties of the data marker hint.

Show Category and Series

Select to include the category and series values in the data marker hint.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart platform.
