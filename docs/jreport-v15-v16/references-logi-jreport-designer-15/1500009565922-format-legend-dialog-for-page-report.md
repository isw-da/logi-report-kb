---
title: "Format Legend Dialog (for Page Report)"
id: 1500009565922
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565922-Format-Legend-Dialog-for-Page-Report
updated_at: 2021-07-24T05:55:13Z
---

# Format Legend Dialog (for Page Report)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587261-Format-Legend-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565902-Format-Legend-Dialog-for-Web-Report-)

# Format Legend Dialog (for Page Report)

The Format Legend dialog for page report appears when you double-click the legend of a chart in a page report, or right-click it and select Format Legend from the shortcut menu. This dialog allows you to [format the legend in a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009563122-Formatting-the-Legend), and consists of the following tabs:

* [Fill](#Fill)
* [Border](#Border)
* [Placement](#Placement)
* [Font](#Font)
* [Orientation](#Orientation)
* [Format](#Format)
* [Mark](#Mark)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Fill

Specifies the color and its transparency for the legend of the chart. [See the tab](javascript:%20void(null)).

![Format Legend dialog for Page Report - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404893894295/fmtlgnd_fill.gif)

**Color**

Specifies the color to fill the legend. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.

**Transparency**

Specifies the transparency of the color.

## Border

Specifies the properties for border of the legend. [See the tab](javascript:%20void(null)).

![Format Legend dialog for Page Report - Border](https://devnet.logianalytics.com/hc/article_attachments/4404889347351/fmtlgnd_border.gif)

**Border Style**

Specifies the type for border of the legend.

* **none**  
   The object has no visible border lines.
* **raised**  
   The object has 3D borders that appear as if they are raised off the page.
* **recess**  
   The object has 3D borders that appear as if they are pressed into the page.
* **shadow**  
   The object has two shadowed borders, beneath and to the right of the object.
* **solid**  
   The object has single-line borders.

**Color**

Specifies the color for border of the legend.

**Line Style**

Specifies the line style to apply to the border of the legend.

**Thickness**

Specifies the thickness of the border, in pixels.

**Transparency**

Specifies the transparency for the color of the border.

**End Caps**

Specifies the ending style of the border line.

* **Butt**  
   Ends unclosed sub paths and dash segments with no added decoration.
* **Round**  
   Ends unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **Square**  
   Ends unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Specifies the line joint style for the border line.

* **Miter**  
   Joins path segments by extending their outside edges until they meet.
* **Round**  
   Joins path segments by rounding off the corner at a radius of half the line width.
* **Bevel**  
   Joins path segments by connecting the outer corners of their wide outlines with a straight segment.

**Path**

Specifies the fill pattern of the border line.

* **Outline Path**  
   Specify the fill pattern of the border line to be outline path.
* **Fill Path**  
   Specify the fill pattern of the border line to be whole path.

**Dash**

Specifies the dash size of the border line.

* **Auto Adjusted Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

**Sample**

Displays a preview sample of your selection.

## Placement

Specifies the location of the legend object. [See the tab](javascript:%20void(null)).

![Format Legend dialog for Page Report - Placement](https://devnet.logianalytics.com/hc/article_attachments/4404893894551/fmtlgnd_plcmnt.gif)

**Position**

Specifies the position of the legend to be left, right, top, bottom or customized by dragging on the chart manually. You can preview the samples when the position is not Customized.

**Alignment**

Specifies the alignment format for the legend.

**Legend-Label Gap**

Specifies the minimum distance between the legend entry labels.

* **Vertical Margin**  
   Specifies the minimum vertical distance between the legend entry labels, in pixels.
* **Vertical Label Spacing**  
   Specifies the vertical distance between legend labels, in pixels.
* **Horizontal Margin**  
   Specifies the minimum horizontal distance between legend entry labels, in pixels.
* **Horizontal Label Spacing**  
   Specifies the horizontal distance between the legend entry labels, in pixels.

**Reverse Legend**

Specifies whether the legend entries will be re-arranged in a reverse order.

**Show Scrollbar**

Specifies whether to show a scrollbar on the legend to fully view the legend content when the content does not fit into the legend.

**Truncate**

Specifies whether to truncate the legend entry label text when the text overflow the labels.

## Font

Specifies the font format of text in the legend entry labels. [See the tab](javascript:%20void(null)).

![Format Legend dialog for Page Report - Font](https://devnet.logianalytics.com/hc/article_attachments/4404893894807/fmtlgnd_font.gif)

**Font**

Specifies the font format of text in the legend entry labels.

* **Font list**  
   Lists all the available font faces that can be selected to apply to the text.
* **Font Size**  
   Specifies the font size of the text.
* **Font Color**  
   Specifies the font color of the text.
* **Transparency**  
  Specifies the transparency of the text.
* **Rotation**  
   Specifies the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
   Specifies the gradient of the text.

**Effects**

Specifies the special effects of text in the legend entry labels.

* **Style**  
   Specifies the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
   Specifies the style of the horizontal line with which the text is struck through. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
   Specifies the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned.
* **Superscript**  
   Raises the text above the baseline and changes the text to a smaller font size, if a smaller size is available.
* **Embossed**  
   Makes the text appear to be raised off the page in relief.
* **Outlined**  
   Displays the inner and outer borders of each character.
* **Subscript**  
   Lowers the text below the baseline and changes the text to a smaller font size, if a smaller size is available.
* **Engraved**  
   Makes the text appear to be imprinted or pressed into the page.
* **Shadowed**  
   Adds a shadow beneath and to the right of the text.

**Sample**

Displays the specified font and any text effects.

## Orientation

Specifies the alignment format of the legend entry labels. [See the tab](javascript:%20void(null)).

![Format Legend dialog for Page Report - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404893895063/fmtlgnd_orntatn.gif)

**Orientation**

Specifies the orientation of the legend entry labels.

**Angle**

Specifies the angel of the legend entry labels.

## Format

Specifies properties for the legend entry labels. [See the tab](javascript:%20void(null)).

![Format Legend dialog for Page Report - Format](https://devnet.logianalytics.com/hc/article_attachments/4404889347607/fmtlgnd_fmt.gif)

**Category**

Specifies different formats to display the legend entry labels.

* **Scale**  
   Lists all the formats of a value of a scale type that can be applied to the legend entry labels.
* **Number**  
   Lists all the formats of a value of a number type that can be applied to the legend entry labels.
* **Date/Time**  
   Lists all the formats of a value of a date/time type that can be applied to the legend entry labels.
* **Text**  
   Lists all the formats of a value of a text type that can be applied to the legend entry labels.
* **Mapping**  
   Lists all the formats of a value of a mapping type that can be applied to the legend entry labels.

**Format**

Displays all the formats of the selected category. For more details about every format, see [A Detailed Chart Property Reference](https://devnet.logianalytics.com/hc/en-us/articles/1500009569442-A-Detailed-Chart-Property-Reference#DataFormat).

**Properties**

Specifies the properties for the format that you selected.

**Stack**

Lists all the formats that you selected from different categories.

**Sample**

Displays the effects of the selected format that has been added into the Stack list box.

**Add**

Adds a format to the Stack list box.

**Remove**

Removes a format from the Stack list box.

**Apply**

Applies the specified format in the Stack list box to the legend entry marks.

**Note:** To make settings in this tab take effect, you need to first make sure that the property [Label Format Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009569482-Properties-of-Chart-Legend-in-Page-Report#LabelFormatSource) of the chart legend has been set to Legend Label Format in the Report Inspector.

## Mark

Specifies the format of the legend entry marks. [See the tab](javascript:%20void(null)).

![Format Legend dialog for Page Report - Mark](https://devnet.logianalytics.com/hc/article_attachments/4404893895319/fmtlgnd_mark.gif)

**Customize**

Specifies whether to customize the format of the legend entry marks.

**Use Node as Mark**

Specifies whether to apply the format of line nodes to the legend entry marks. If selected, the legend entry marks will automatically inherit the style and color of line nodes. Available for line charts only.

**Use Line and Node as Mark**

Specifies whether to apply the format of lines and line nodes to the legend entry marks. If checked, the legend entry marks will automatically inherit the style and color of lines and line nodes. Available for line charts only.

**Mark Items**

Specifies the style of the legend entry marks. Select the mark item from the box one by one and choose the style for each item from the drop-down list. Available only when Customize is checked.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a mark item to the box.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes a specified mark item from the box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves a selected mark item up a step.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves a selected mark item down a step.

**Icon**

Specifies the properties of the icons.

* **Width**  
   Specifies the width of the icons, in pixels.
* **Height**  
   Specifies the height of the icons, in pixels.
* **H-Alignment**  
   Specifies the horizontal alignment format of the icons. It could be left, center and right.
* **V-Alignment**  
   Specifies the vertical alignment format of the icons. It could be top, center and bottom.
* **Icon-Text Gap**  
   Specifies the gap between each entry mark and entry label, in pixels.

**Border**

Specifies the border properties of the icons. Available only when Customize is checked.

* **Color**  
   Specifies the color of the icon border.
* **Style**  
   Specifies the line style of the icon border.
* **Thickness**  
   Specifies the thickness of the icon border, in pixels.
* **Transparency**  
   Specifies the transparency of the icon border.
* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif)  
  Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties).

**Preview**

Displays the specified item and mark effects.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009587261-Format-Legend-Dialog-for-Library-Component-)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565902-Format-Legend-Dialog-for-Web-Report-)
