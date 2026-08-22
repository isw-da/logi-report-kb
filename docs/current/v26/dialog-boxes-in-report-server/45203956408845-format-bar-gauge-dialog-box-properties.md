---
title: "Format Bar Gauge Dialog Box Properties"
id: 45203956408845
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203956408845-Format-Bar-Gauge-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:42Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Format Bar Gauge Dialog Box Properties

This topic describes how you can use the Format Bar Gauge dialog box to format the bar gauges in a bar gauge chart. Server displays the dialog box when you right-click on a bar gauge chart and select Format Graph from the shortcut menu.

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

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

## 
Staff Graph Tab Properties

Specify the properties for bars in the bar gauge.

Bar

Specify the properties of the bars.

- 
Layout
    Specify the layout of the bars. It can be vertical or horizontal.

- 
Thickness
    Specify the thickness of the bars, in inches.

- 
Start Style
    Specify the style for the start graph of the bars.

- 
End Style
    Specify the style for the end graph of the bars. 

Border

Specify the properties of the bar border.

- 
Line Style
    Specify the line style of the border.

- 
Thickness
Specify the thickness of the border, in inches.

- 
Color
    Specify the color of the border. To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range.

- 
Transparency
  Specify the transparency for the border color.

Show Range Name

Select if you want to show the names of the ranges defined in the Range Color tab. Then, you can continue to specify the font properties of the text in the range names.

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

## 
Axis Tab Properties

The tab consists of four sub tabs: Axis, Tick Mark, Label, and Format.

### 
Axis

Specify the properties of the axis in the bar gauge.

Show Axis 

Select if you want to show the axis. 

Type

Specify the position relationship of the axis and the bar. When Layout is horizontal in the Staff Graph tab, the following are available: 

- 
Top
    Select if you want to display the axis on the top of the bar.

- 
Bottom
    Select if you want to display the axis on the bottom of the bar.

- 
Center
    Select if you want to display the axis in the center of the bar.

When Layout is vertical in the Staff Graph tab, the following are available: 

- 
Left
    Select if you want to display the axis on the left of the bar.

- 
Right
 Select if you want to display the axis on the right of the bar.

- 
Center
    Select if you want to display the axis in the center of the bar. 

Option

Specify the values you want to display in the chart.

- 
Minimum Value
    Specify the minimum value in the chart. You can also use a formula to control the property.

- 
Maximum Value
    Specify the maximum value in the chart. You can also use a formula to control the property.

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

Specify the position relationship of the axis and the tick marks. When Layout is horizontal in the Staff Graph tab, the following are available: 

- 
None
    Select if you don't want to display the tick marks on the axis. It is meaningless to specify all the other tick mark related properties when you select this type.

- 
Top
       Select to display the tick marks on the top of the axis. 

- 
Bottom
    Select to display the tick marks on the bottom of the axis.

- 
Center
       Select to display the tick marks in the center of the axis.

When Layout is vertical in the Staff Graph tab, the following are available: 

- 
None
    Select if you don't want to display the tick marks on the axis. It is meaningless to specify all the other tick mark related properties if this type is selected.

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
        Specify the number of major tick mark labels you want to display on the axis.
        
- 
Auto
              Select to display all major tick mark labels.

- 
Fixed
 Select and then specify the number of the major tick mark labels you want to display on the axis.

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

Specify the data format of the major tick mark labels.

Category

Select a category type to customize its format.

Format

Select a format, and then select Add to add it as the format of the specified category. You can add only one format for each category.

Properties

Server displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box, and then select Add to add it as the format of the specified category.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart. When you set the property to true, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Report will ignore the Auto Scale in Number setting.

Sample

Server displays a preview sample of your settings.

Stack

Server displays all the formats you select for different categories.

Add

Select to add a format to the Stack box.

Remove

Select to remove a format from the Stack box.

Apply

Select to apply the specified format in the Stack box to the major tick mark labels.

## 
Pointer Tab Properties

Specify the properties of the pointers in the bar gauge.

Use Pointer

Select to use pointers to indicate values in the bar gauge.

- 
Pointer Style
    Specify properties of the pointers.
    
- 
Value Pointer
      Specify the style of the value pointers. Select a style from the drop-down list or select Customized to specify another image as the value pointers in the Insert Image dialog box.

- 
Width
        Specify the width of the pointers.

- 
Height
        Specify the height of the pointers.

- 
Position
        Specify the position of the pointers relative to the bar.

- 
Gap
        Specify the distance between the pointers and the bar.

- 
Style List
        Select to open the Style List dialog box to specify the style for pointers in the same data series respectively.

- 
Pointer Color
    Specify color properties of the pointers.
    
- 
Color
        Specify the color of the pointers.

- 
Color List 
        Select to open the Color List dialog box to specify the color pattern for pointers in the same data series respectively.

- 
Transparency
        Specify the transparency for color of the pointers.

- 
Use Range Color
 Select to use the color defined for the ranges as the pointer color. Then, Server disables the preceding three properties. 

- 
Pointer Value
Specify properties for values of the pointers.
  - 
Show Pointer Value
      Select if you want to show values for the pointers.
      - 
Position
          Select the position relationship between the values and the pointers. If you select customized, the X and Y settings in the General tab of the Format Pointer Label dialog box will take effect.

- 
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
        Specify the transparency for color of the bars.

- 
Thickness
        Specify the thickness of the color bars.

- 
Color List 
 Select to open the Color List dialog box to specify the color pattern for color bars in the same data series respectively.

- 
Pointer Value
Specify properties for values of the color bars.
  
- 
Show Pointer Value
      Select if you want to show values for the color bars. 

- 
Position
      Select the position relationship between the values and the color bars. If you select customized, the X and Y settings in the General tab of the Format Pointer Label dialog box will take effect.

- 
Pointer Border
Specify the pointer border properties.
    - 
Show Pointer Border
        Select if you want to show the border of the pointers. Then, Server enables the following border properties\.
          
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

Specify the properties of the target in the bar gauge.

Use Target Value

     Select if you want to use the target value for the bar gauge. 

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
    Specify the position of the target pointer relative to the bar.

- 
Gap
    Specify the distance between the target pointer and the bar.

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
         Select if you want to show the target value on the bar gauge.
    - 
Position
        Select the position of the target value relative to the bar. If you select customized, the X and Y settings in the General tab of the Format Target Label dialog box will take effect.

## 
Frame Tab Properties

Specify properties for the frame of the bar gauge chart.

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

Specify properties for the gauge group name.

- 
Show Gauge Group Name 
 Select if you want to show names for the bars in the bar gauge which are values of the field on its category axis. If the bar gauge contains no category field, the group name shows Report by default.
    - 
Position
Select the position of the names relative to the bars. If you select customized, the X and Y settings in the General tab of the Format Gauge Label dialog box will take effect.

## 
Range Color Tab Properties

Specify different colors to fill the bars in bar gauge in different ranges.

Use Gradient Effect

Select if you want to use gradient effect for the color.

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
