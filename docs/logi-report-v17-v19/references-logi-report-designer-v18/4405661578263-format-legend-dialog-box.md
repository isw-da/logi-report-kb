---
title: "Format Legend Dialog Box"
id: 4405661578263
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661578263-Format-Legend-Dialog-Box
updated_at: 2022-01-27T20:35:48Z
---

# Format Legend Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661577239-Format-Label-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661579287-Format-Line-Dialog-Box)

# Format Legend Dialog Box

You can use the Format Legend dialog box to [format the legend of a chart](https://devnet.logianalytics.com/hc/en-us/articles/4405661358231-Formatting-the-Legend). This topic describes the options in the dialog box.

Designer displays the Format Legend dialog box when you right-click the legend of a chart and select Format Legend from the shortcut menu, or double-click the legend of a chart.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

* [Fill Tab](#Fill)
* [Border Tab](#Border)
* [Placement Tab](#Placement)
* [Font Tab](#Font)
* [Orientation Tab](#Orientation)
* [Format Tab](#Format)
* [Mark Tab](#Mark)
* [Label Tab](#Label)
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

## Fill Tab

Use this tab to specify the color pattern to fill the legend.

![Format Legend dialog box - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420556168599/fmtlgnd_fill.gif)

**Color**

Specify the color to fill the legend. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency of the color.

**Sample**

This box displays a preview sample based on your selections.

## Border Tab

Use this tab to specify properties for the border of the legend.

![Format Legend dialog box - Border](https://devnet.logianalytics.com/hc/article_attachments/4420556170647/fmtlgnd_border.gif)

**Border Type**

Select the type of the border.

* **none**  
  Select if you do not want to show the border.
* **raised**  
  Select to show 3-D border which appears as if it is raised off the page.
* **recess**  
  Select to show 3-D border which appears as if it is pressed into the page.
* **shadow**  
  Select to show two shadowed borders, beneath and to the right of the object.
* **solid**  
  Select to use single-line border.

**Color**

Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency for the color of the border.

**Line Style**

Select the line style of the border.

**Thickness**

Specify the width of the border, in pixels.

**End Caps**

Select the ending style of the border line.

* **butt**  
  Select to end unclosed sub paths and dash segments with no added decoration.
* **round**  
  Select to end unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square**  
  Select to end unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Select the joint style of the border line.

* **miter**  
  Select to join path segments by extending their outside edges until they meet.
* **round**  
  Select to join path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
  Select to join path segments by connecting the outer corners of their wide outlines with a straight segment.

**Sample**

This box displays a preview sample based on your selections.

**Path**

You can specify the fill pattern of the border in this box.

* **Outline Path**  
  Select to use outline path for the border.
* **Fill Path**  
  Select to use whole path for the border.

**Dash**

You can specify the dash size of the border
in this box if you select a dash line style for the border.

* **Auto Adjust Dash**  
  Select to adjust the dash size automatically.
* **Fixed Dash Size**  
  Select to use fixed dash size.

## Placement Tab

Use this tab to specify the location of the legend in the chart.

![Format Legend dialog box - Placement](https://devnet.logianalytics.com/hc/article_attachments/4420550902807/fmtlgnd_plcmnt.gif)

**Position**

Specify the position of the legend to be at the left, right, top, or bottom of the chart, or customized by dragging on the chart manually.

**Alignment**

Specify the alignment of the legend at the selected position.

**Legend Label Gap**

You can specify the margins between the legend entries and legend boundaries, and the spacing between the legend entry labels in this box.

* **Vertical Margin**  
  Specify the minimum vertical distance between the legend entry labels, in pixels.
* **Vertical Label Spacing**  
  Specify the vertical distance between the legend entries and the legend boundaries, in pixels.
* **Horizontal Margin**  
  Specify the minimum horizontal distance between legend entry labels, in pixels.
* **Horizontal Label Spacing**  
  Specify the horizontal distance between the legend entries and the legend boundaries, in pixels.

**Reverse Legend**

Select to arrange the legend entries in a reverse order.

**Show Scrollbar**

Select to show a scroll bar in the legend to fully view the legend content when the content does not fit into the legend.

**Truncate**

Select to truncate the legend entry label text when the text overflows the labels.

## Font Tab

Use this tab to specify the font format of the text in the legend entry labels.

![Format Legend dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4420542132375/fmtlgnd_font.gif)

**Font**

You can specify the font format of the text in the legend entry labels in this box.

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

You can specify the special effects of the text in the legend entry labels in this box.

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

Use this tab to specify the rotation angle for the legend entry labels.

![Format Legend dialog box - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4420550903575/fmtlgnd_orntatn.gif)

**Angle**

Specify the rotation angle for the legend entry labels. When you change the rotation angle in the text box, the red line in the spin box changes correspondingly, and vice versa.

## Format Tab

Use this tab to specify the data format of the legend entry labels. Designer applies the specified format only when you set the property [Label Format Source](https://devnet.logianalytics.com/hc/en-us/articles/4405661843991-Chart-Legend-Properties#LabelFormatSource) of the chart legend to "Legend Label Format" in the Report Inspector.

![FFormat Legend dialog box - Format](https://devnet.logianalytics.com/hc/article_attachments/4420550903831/fmtlgnd_fmt.gif)

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

Select to apply the specified format to the legend entry labels.

## Mark Tab

Use this tab to specify the format of the legend entry marks.

![Format Legend dialog box - Mark](https://devnet.logianalytics.com/hc/article_attachments/4420550904087/fmtlgnd_mark.gif)

**Customize**

Select to customize the format of the legend entry marks.

**Use Node as Mark**

Designer enables this option only when the chart is a line chart. Select it if you want to apply the format of line nodes to the legend entry marks, meaning, the legend entry marks automatically inherit the style and color of the line nodes.

**Use Line and Node as Mark**

Designer enables this option only when the chart is a line chart. Select it if you want to apply the format of the lines and line nodes to the legend entry marks, meaning the legend entry marks automatically inherit the style and color of the lines and line nodes.

**Mark Items**

You can specify the style of the legend entry marks in this box. Select the mark item from the box one by one and choose the style for each item from the drop-down list. Designer disables this box when you select Use Node as Mark or Use Line and Node as Mark.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif)**Add button**  
  Select to add a mark item to the box.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420542080407/btn_trashcan.gif)**Remove button**  
  Select to delete a specified mark item from the box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif)**Move Up button**  
  Select to move a specified mark item higher in the box.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif)**Move Down button**  
  Select to move a specified mark item lower in the box.

**Icon**

You can specify properties of the entry marks in this box.

* **Width**  
  Specify the width of the marks, in pixels.
* **Height**  
  Specify the height of the marks, in pixels.
* **H-Alignment**  
  Select the horizontal alignment of the marks relative to the legend entry labels: left, center, or right.
* **V-Alignment**  
  Select the vertical alignment of the marks relative to the legend entry labels: top, center, or bottom.
* **Icon-Text Gap**  
  Specify the gap between each entry mark and entry label, in pixels.

**Border**

You can specify the border properties of the marks in this box. Designer disables this box when you select Use Node as Mark or Use Line and Node as Mark.

* **Color**  
  Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Transparency**  
  Specify the transparency for the color of the border.
* **Line Style**  
  Select the line style of the border.
* **Thickness**  
  Specify the width of the border, in pixels.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Designer displays the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif) for some options if the chart uses a query resource. It indicates that you can [use a formula to control the value of an option](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties).

**Preview**

This box displays a preview of your settings.

## Label Tab

Designer enables the options in the Label tab only when the legend entry labels show the values of the field on the category or series axis of the chart. You can use this tab to customize the text of the legend entry labels.

![Format Legend dialog box - Label](https://devnet.logianalytics.com/hc/article_attachments/4420556171159/fmtlgnd_lbl.gif)

**Auto**

Designer selects this option by default, meaning, it displays the values of the category/series field in the legend entry labels.

* **Label Text**  
  Specify the text of the legend entry labels. Select a field from the drop-down list to use its values as the label text or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556117783/btn_x.gif) to type the label text manually.

## Behaviors Tab

Designer displays the Behaviors tab only when the chart is in a library component. You can use it to specify web behaviors to the legend.

![Format Legend dialog box - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420550904343/fmtlgnd_bhvr.gif)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661577239-Format-Label-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661579287-Format-Line-Dialog-Box)
