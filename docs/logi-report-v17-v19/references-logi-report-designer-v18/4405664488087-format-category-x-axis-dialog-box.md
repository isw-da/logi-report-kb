---
title: "Format Category (X) Axis Dialog Box"
id: 4405664488087
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664488087-Format-Category-X-Axis-Dialog-Box
updated_at: 2022-01-27T20:35:41Z
---

# Format Category (X) Axis Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664486807-Format-Bullet-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661568407-Format-Category-X-Gridline-Dialog-Box)

# Format Category (X) Axis Dialog Box

You can use the Format Category (X) Axis dialog box to [format the category (X) axis of a chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664375831-Formatting-the-Axes#Category). This topic describes the options in the dialog box.

Designer displays the Format Category (X) Axis dialog box when you right-click any chart element and navigate to Format Axes > Format Category (X) Axis on the shortcut menu, or double-click the category axis of a chart.

The dialog box contains the following tabs (Designer displays some tabs only to specific chart types only, and the Behaviors tab only when the chart is in a library component):

* [Axis Tab](#Axis)
* [Tick Mark Tab](#Tick)
* [Font Tab](#Font)
* [Orientation Tab](#Orientation)
* [Format Tab](#Format)
* [Range Tab](#Range)
* [Behaviors Tab](#Behaviors)

You see these buttons in the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## Axis Tab

Use this tab to specify the general properties of the category axis.

![Format Category (X) Axis dialog box - Axis](https://devnet.logianalytics.com/hc/article_attachments/4420550909463/fmtctgryaxis_axis.gif)

**Option**

You can specify the axis options in this box.

* **Show Gridlines**  
  Select to show gridlines on the axis.

  Designer displays the following four options only when the chart is a scatter chart, or a bubble chart which shows different fields on the category axis and the bubble X axis.

* **Minimum Value**  
  Specify the minimum value to display on the axis.
* **Maximum Value**  
  Specify the maximum value to display on the axis.
* **Increment**  
  Specify the distance between two adjacent values on the axis. Available only t
* **Number of Tick Marks**  
  Specify how many tick marks you want to display on the axis.

**Line**

You can specify the line style for the axis in this box.

* **Color**  
  Specify the color of the axis. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Style**  
  Select the line style for the axis.
* **Transparency**  
  Specify the transparency for the color of the axis.
* **Thickness**  
  Specify the thickness for the line of the axis, in pixels.

**Label**

You can specify options for the labels on the axis in this box.

* **Label Axis Gap**  
  Specify the distance between the labels and the axis, in pixels.
* **Best Effect**  
  Select to adjust the labels automatically to place them at the best position on the axis. When you select this option, Designer hides some labels if they overlap.
* **Auto**  
  Select to display the values of the field that you add to the axis as the major tick mark labels. Clear it if you want to customize the label text.
  + **Label Text**  
    Specify the text of the major tick mark labels on the axis. Select a field from the drop-down list to use its values as the label text or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556117783/btn_x.gif) to type the label text manually.

## Tick Mark Tab

You see the following subtabs in the Tick Mark tab:

* [Major Tick Mark Subtab](#Majortm)
* [Minor Tick Mark Subtab](#Minortm)
* [Scale Subtab](#Scale)

### Major Tick Mark Subtab

Use this subtab to specify properties of the major tick marks on the category axis.

![Format Category (X) Axis dialog box - Tick Mark - Major Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420542139415/fmtctgryaxis_mark_major.gif)

**Type**

You can specify the type of the major tick marks on the axis in this box.

* **None**  
  Select if you do not want to display major tick marks on the axis. It is meaningless to specify all the other major tick mark properties if you select this type.
* **Inside**  
  Select to display the major tick marks inside the axis.
* **Outside**  
  Select to display the major tick marks outside the axis.
* **Cross**  
  Select to display the major tick marks across the axis.

**Line**

You can specify the line properties of the major tick marks on the axis in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the major tick marks. When you clear this option, you can specify the line properties for the major tick marks separately using the following options:
  + **Color**  
    Specify the color of the major tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
  + **Style**  
    Select the style of the major tick mark line.
  + **Transparency**  
    Specify the transparency for the color of the major tick mark line.
  + **Thickness**  
    Specify the thickness of the major tick mark line, in pixels.
* **Tick Mark Length**  
  Specify the length of the major tick marks, in pixels.

**Option**

You can specify the other properties of the major tick mark labels on the axis in this box.

* **Show Major Tick Mark Labels**  
  Select to display the labels of the major tick marks on the axis. Designer enables the other options in the Options box when you select this option.
* **Label Every N Major Tick Marks**  
  Specify the frequency at which to label the major tick marks.
* **Show Axis Label Tips**  
  Select to display the complete label text when you point to a label on the axis.
* **Number of Major Labels**  
  Specify how many major tick mark labels to display on the axis.
  + **Auto**  
    Select to display all the major tick mark labels.
  + **Fixed**  
    Select and specify the number of the major tick mark labels you want to display.

### Minor Tick Mark Subtab

Use this subtab to specify properties of the minor tick marks on the category axis.

![Format Category (X) Axis dialog box - Tick Mark - Minor Tick Mark](https://devnet.logianalytics.com/hc/article_attachments/4420556179991/fmtctgryaxis_mark_minor.gif)

**Type**

You can specify the type of the minor tick marks on the axis in this box.

* **None**  
  Select if you do not want to display minor tick marks on the axis. It is meaningless to specify all the other minor tick mark properties if you select this type.
* **Inside**  
  Select to display the minor tick marks inside the axis.
* **Outside**  
  Select to display the minor tick marks outside the axis.
* **Cross**  
  Select to display the minor tick marks across the axis.

**Line**

You can specify the line properties of the minor tick marks on the axis in this box.

* **Correlate with Axis**  
  Select to apply the [line properties](#Line) that you define for the axis in the Axis tab to the minor tick marks. When you clear this option, you can specify the line properties for the minor tick marks separately using the following options:
  + **Color**  
    Specify the color of the minor tick mark line. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
  + **Style**  
    Select the style of the minor tick mark line.
  + **Transparency**  
    Specify the transparency for the color of the minor tick mark line.
  + **Thickness**  
    Specify the thickness of the minor tick mark line, in pixels.
* **Tick Mark Length**  
  Specify the length of the minor tick marks, in pixels.

**Option**

You can specify the other properties of the minor tick mark labels on the axis in this box.

* **Show Minor Tick Mark Labels**  
  Select to display the labels of the minor tick marks on the axis. Designer enables the other options in the Options box when you select this option.
* **Label Every N Minor Tick Marks**  
  Specify the frequency at which to label the minor tick marks.
* **Number of Minor Labels**  
  Specify how many minor tick mark labels to display on the axis.
  + **Auto**  
    Select to display all the minor tick mark labels.
  + **Fixed**  
    Select and specify the number of the minor tick mark labels you want to display.

### Scale Subtab

Use this tab to customizes the way to label the major and minor tick marks on the category axis with constant interval. Designer enables the Scale subtab only when the field on the category axis is one of the following types: Number, Date, Time, and DateTime (for a bubble chart, only when the category field is one of the types and the Bubble X Axis uses the category field), and does not display it for scatter charts.

![Format Category (X) Axis dialog box - Tick Mark - Scale](https://devnet.logianalytics.com/hc/article_attachments/4420556180247/fmtctgryaxis_mark_scale.gif)

**Use Constant Interval**

Select to use a constant interval to label the tick marks. If you select this option, Designer increases the values of the tick marks continually on the axis based on the following properties instead of just using the data values, and ignores the [customized major tick mark labels](#LabelText) in the Axis tab.

**Minimum**

Specify the minimum value to label the tick marks.

* **Auto**  
  Select to let Designer calculate the minimum value automatically.
* **Fixed**  
  Select and specify the minimum value by inputting it in the text box directly, selecting ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) to select a field, or selecting ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420550878743/btn_clndr.gif) to specify a date and time value from the calendar widget if the field on the category axis is of Date, Time, or DateTime type.

**Maximum**

Specify the maximum value to label the tick marks.

* **Auto**  
  Select to let Designer calculate the maximum value automatically.
* **Fixed**  
  Select and specify the maximum value by inputting it in the text box directly, selecting ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) to select a field, or selecting ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4420550878743/btn_clndr.gif) to specify a date and time value from the calendar widget if the field on the category axis is of Date, Time, or DateTime type.

**Major Unit**

Specify the unit between two adjacent major tick marks.

* **Auto**  
  Select to let Designer define the unit automatically.
* **Fixed**  
  Select and type the unit in the text box. If the field on the category axis is of the Date, Time, or DateTime type, you can also choose a unit from the drop-down list.

**Minor Unit**

Specify the unit between two adjacent minor tick marks.

* **Auto**  
  Select to let Designer define the unit automatically.
* **Fixed**  
  Select and type the unit in the text box. If the field on the category axis is of the Date, Time, or DateTime type, you can also choose a unit from the drop-down list.

## Font Tab

You see the following subtabs in the Font tab:

* [Major Label Subtab](#Majorft)
* [Minor Label Subtab](#Minorft)

### Major Label Subtab

Use this subtab to specify the font format of the major tick mark labels on the category axis.

![Format Category (X) Axis dialog box - Font - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4420542140055/fmtctgryaxis_font_major.gif)

**Font**

You can specify the font format of the text in the major tick mark labels in this box.

* **Font list**  
  This drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the color transparency of the text.
* **Rotation**  
  Specify the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
  Specify the gradient of the text.

**Effects**

You can specify the special effects of the text in the major tick mark labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Web Report Studio and JDashboard do not support underlining chart text, therefore, this property is ignored when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Outlined**  
  Select to display the inner and outer borders of each character.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

**Sample**

This box displays a preview sample based on your selections.

### Minor Label Subtab

Use this subtab to specify the font format of the minor tick mark labels on the category axis.

![Format Category (X) Axis dialog box - Font - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4420550909975/fmtctgryaxis_font_minor.gif)

**Correlate with Major Label**

Select to apply the font properties that you define for the major tick mark labels in the Major Label subtab to the minor tick mark labels.

**Font**

You can specify the font format of the text in the minor tick mark labels in this box.

* **Font list**  
  This drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the color transparency of the text.
* **Rotation**  
  Specify the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
  Specify the gradient of the text.

**Effects**

You can specify the special effects of the text in the minor tick mark labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Web Report Studio and JDashboard do not support underlining chart text, therefore, this property is ignored when the chart runs in Web Report Studio or is used in a dashboard.

* **Superscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Embossed**  
  Select to make the text appear to be raised off the page in relief.
* **Outlined**  
  Select to display the inner and outer borders of each character.
* **Subscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.
* **Engraved**  
  Select to make the text appear to be imprinted or pressed into the page.
* **Shadowed**  
  Select to add a shadow beneath and to the right of the text.

**Sample**

This box displays a preview sample based on your selections.

## Orientation Tab

You see the following subtabs in the Orientation tab:

* [Major Label Subtab](#Majorlb)
* [Minor Label Subtab](#Minorlb)

### Major Label Subtab

Use this subtab to specify the rotation angle of the major tick mark labels on the category axis.

![Format Category (X) Axis dialog box - Orientation - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4420550910231/fmtctgryaxis_orntatn_major.gif)

**Automatic**

Select to adjust the rotation angle of the major tick mark label text on the axis automatically according to the length of the text, in degrees.

**Angle**

Select and specify the rotation angle of the major tick mark label text on the axis in the text box. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

### Minor Label Subtab

Use this subtab to specify the rotation angle of the minor tick mark labels on the axis.

![Format Category (X) Axis dialog box - Orientation - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4420550910487/fmtctgryaxis_orntatn_minor.gif)

**Correlate with Major Label**

Select to apply the rotation angle that you define for the major tick mark label text in the Major Label subtab to the minor tick mark label text.

**Automatic**

Select to adjust the rotation angle of the minor tick mark label text on the axis automatically according to the length of the label text, in degrees.

**Angle**

Select and specify the rotation angle of the minor tick mark label text on the axis in the text box. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

## Format Tab

You see the following subtabs in the Format tab:

* [Major Label Subtab](#Majorfmt)
* [Minor Label Subtab](#Minorfmt)

### Major Label Subtab

Use this subtab to specify the data format of the major tick mark labels on the category axis.

![Format Category (X) Axis dialog box - Format - Major Label](https://devnet.logianalytics.com/hc/article_attachments/4420556181015/fmtctgryaxis_fmt_major.gif)

**Category & Format**

These two boxes list the [category types and the formats of each category](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box#DataFormat) that Designer provides by default. Select a category and a format for this category, then select **Add** to add it as the format of the category. You can add only one format for each category.

**Properties**

This text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select **Add** to add it as the format of the category.

**Auto Scale in Number**

Specify whether to automatically scale the Number values that fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Sample**

This box displays a sample for the selected format.

**Stack**

This box lists all the formats that you select from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove the specified format from the Stack box.

**Apply**

Select to apply the specified format to the major tick mark labels.

**Truncate**

Select to truncate the label text that is longer than 10 characters and only show the first 7 characters.

### Minor Label Subtab

Use this subtab to specify the data format of the minor tick mark labels on the category axis.

![Format Category (X) Axis dialog box -Format - Minor Label](https://devnet.logianalytics.com/hc/article_attachments/4420542141207/fmtctgryaxis_fmt_minor.gif)

**Correlate with Major Label**

Select to apply the data format that you specify for the major tick mark labels in the Major Label subtab to the minor tick mark labels.

**Category & Format**

These two boxes list the [category types and the formats of each category](https://devnet.logianalytics.com/hc/en-us/articles/4405664452759-Data-Format-Dialog-Box#DataFormat) that Designer provides by default. Select a category and a format for this category, then select **Add** to add it as the format of the category. You can add only one format for each category.

**Properties**

This text box shows the properties of the format that you select in the Format box. If the default formats Designer provides for a category cannot meet your requirement, you can define your own format in the text box and select **Add** to add it as the format of the category.

**Auto Scale in Number**

Specify whether to automatically scale the Number values that fall into the two ranges:

* When 1000 <= value < 10^15, Logi Report Engine applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Logi Report Engine uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

**Sample**

This box displays a sample for the selected format.

**Stack**

This box lists all the formats that you select from different categories.

**Add**

Select to add a format to the Stack box.

**Remove**

Select to remove the specified format from the Stack box.

**Apply**

Select to apply the specified format to the minor tick mark labels.

## Range Tab

Designer displays the Range tab only when the chart is of the Bar, Bench, Line, or Area type and its value fields do not contain detail information. You can use it to divide the category values into different range groups and edit data labels for them.

You see the following subtabs in the Range tab:

* [Properties Subtab](#Properties)
* [Data Label Subtab](#Datalb)

### Properties Subtab

Use this subtab to specify properties of the range groups on the category axis.

![Format Category (X) Axis dialog box - Range - Properties](https://devnet.logianalytics.com/hc/article_attachments/4420542141719/fmtctgryaxis_range_prpty.gif)

**Enable Range**

Select to enable the range function.

* **Special Group**   
  Select to open the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664591383-User-Defined-Group-Dialog-Box) to define how to group the category values.

**Gridline**

You can specify the style for the range separating lines in this box.

* **Line Color**  
  Specify the color of the range separating lines. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Line Style**  
  Select the style of the range separating lines.
* **Transparency**  
  Specify the transparency for the color of the range separating lines.
* **Thickness**  
  Specify the thickness of the range separating lines, in pixels.

**Fill**

You can specify the fill effects for each range group in this box.

* **Group Name**   
  This column shows the names of the ranges that you have added using the User Defined Group dialog box.
* **Color**  
  This column shows the colors that you specify for the range groups.
* **Transparency**  
  This column shows the transparency that you specify for the color of each range group.

### Data Label Subtab

Use this subtab to specify properties of the data labels in the range groups on the category axis.

![Format Category (X) Axis dialog box - Range - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4420550911511/fmtctgryaxis_range_dtlb.gif)

**Show Data Labels**

Designer enables this option when you select Enable Range and have defined the range groups in the Properties subtab. You can select it to show data labels for the range groups.

* **Edit Data Labels**  
  Select to open the [Data Label Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664453655-Data-Label-Editor-Dialog-Box) to edit data labels for the range groups.

**Data Label Type**

Select in which way to display the values in the data labels of the range groups.

* **value**  
  Select to show the value for each group range.
* **percent**  
  Select to show the percentage of each group range to the total.
* **value and percent**  
  Select to show the value and the percentage for each group range.

**Percent within Group**

Designer enables this option when you select "percent" or "value and percent" from the Data Label Type drop-down list. You can select it to calculate the percent value within each range group. If you do not select this option, the calculation is based on all the range groups.

**Alignment**

Select the alignment style for the data labels in the range groups: left, center, or right.

**Size**

You can specify the size of the data label area on the range groups in this box.

* **Height**  
  Specify the height of the data label area. It cannot exceed the maximum height.
* **Width**  
  Specify the width of the data label area.
* **Maximum Height**  
  Specify the maximum height of the data label area. It cannot exceed the height of the chart paper.

**Fill**

You can specify the fill effect for the data label area in this box.

* **Color**  
  Specify the color to fill the data label area. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the transparency of the color.

**Border**

You can specify properties for the borders of the data label area in this box.

* **Color**  
  Specify the color of the borders. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Line Style**  
  Select the line style of the borders.
* **Transparency**  
  Specify the transparency for the color of the borders.
* **End Caps**  
  Select the ending style of the border line.

+ **butt**  
  Select to end unclosed sub paths and dash segments with no added decoration.
+ **round**  
  Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
+ **square**  
  Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

* **Thickness**  
  Specify the width of the borders, in pixels.
* **Line Joint**  
  Select the joint style for the border line.
  + **miter**  
    Select to join path segments by extending their outside edges until they meet.
  + **round**  
    Select to join path segments by rounding off the corner at a radius of half the line width.
  + **bevel**  
    Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

**Margin**

You can specify the distance between the edge and the borders in this box.

* **Top**  
  Specify the distance between the top edge and the top border.
* **Bottom**  
  Specify the distance between the bottom edge and the bottom border.
* **Left**  
  Specify the distance between the left edge and the left border.
* **Right**  
  Specify the distance between the right edge and the right border.

**Padding**

You can specify the distance between the value in a data label and its borders.

* **Top**  
  Specify the distance between the value in a data label and the top border.
* **Bottom**  
  Specify the distance between the value in a data label and the bottom border.
* **Left**  
  Specify the distance between the value in a data label and the left border.
* **Right**  
  Specify the distance between the value in a data label and the right border.

## Behaviors Tab

Designer displays the Behaviors tab only when the chart is in a library component. You can use it to specify web behaviors on the category axis of the chart.

![Format Category (X) Axis dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420556182295/fmtctgryaxis_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif)**Add button**

Select to add a new web behavior line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**

Select to delete the specified web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif)**Move Up button**

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif)**Move Down button**

Select to move the specified web behavior lower in the list.

**Events**

This column shows the events that you select to trigger the web actions.

**Actions**

This column shows the web actions that you specify for the events to trigger. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif) in each cell to bind the web action using the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661744791-Web-Action-List-Dialog-Box).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664486807-Format-Bullet-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661568407-Format-Category-X-Gridline-Dialog-Box)
