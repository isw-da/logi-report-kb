---
title: "Format Legend Dialog"
id: 1500010031022
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031022-Format-Legend-Dialog
updated_at: 2021-07-24T10:38:47Z
---

# Format Legend Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066421-Format-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031042-Format-Line-Dialog)

# Format Legend Dialog

The Format Legend dialog helps you to [format the legend of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063481-Formatting-the-Legend). It appears when you right-click it and select Format Legend from the shortcut menu, or double-click the legend of a chart.

The dialog contains the following tabs: [Fill](#Fill), [Border](#Border), [Placement](#Placement), [Font](#Font), [Orientation](#Orientation), [Format](#Format), [Mark](#Mark), [Label](#Label) and [Behaviors](#Behaviors) (the Behaviors tab is available to charts in library components only).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Fill

Specifies the color and its transparency for the legend of the chart.

![Format Legend dialog - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404909205911/fmtlgnd_fill.gif)

**Color**

Specifies the color to fill the legend. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.

**Transparency**

Specifies the transparency of the color.

**Sample**

Displays a preview sample of your selection.

## Border

Specifies the properties for border of the legend.

![Format Legend dialog - Border](https://devnet.logianalytics.com/hc/article_attachments/4404909206167/fmtlgnd_border.gif)

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

* **butt**  
   Ends unclosed sub paths and dash segments with no added decoration.
* **round**  
   Ends unclosed sub paths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **square**  
   Ends unclosed sub paths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Specifies the line joint style for the border line.

* **miter**  
   Joins path segments by extending their outside edges until they meet.
* **round**  
   Joins path segments by rounding off the corner at a radius of half the line width.
* **bevel**  
   Joins path segments by connecting the outer corners of their wide outlines with a straight segment.

**Path**

Specifies the fill pattern of the border line.

* **Outline Path**  
   Specify the fill pattern of the border line to be outline path.
* **Fill Path**  
   Specify the fill pattern of the border line to be whole path.

**Dash**

Specifies the dash size of the border line.

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

**Sample**

Displays a preview sample of your selection.

## Placement

Specifies the location of the legend object.

![Format Legend dialog - Placement](https://devnet.logianalytics.com/hc/article_attachments/4404909206423/fmtlgnd_plcmnt.gif)

**Position**

Specifies the position of the legend to be left, right, top, bottom or customized by dragging on the chart manually. You can preview the samples when the position is not Customized.

**Alignment**

Specifies the alignment format for the legend.

**Legend Label Gap**

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

Specifies the font format of text in the legend entry labels.

![Format Legend dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404909206679/fmtlgnd_font.gif)

**Font**

Specifies the font format of text in the legend entry labels.

* **Font list**  
   Lists all the available font faces that can be selected to apply to the text.
* **Font Size**  
   Specifies the font size of the text.
* **Font Color**  
   Specifies the font color of the text.
* **Transparency**  
  Specifies the color transparency of the text.
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
   Specifies the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When patterned line or bold patterned is selected, a line or bold line in the pattern of the text will be drawn.

  **Note:** Web Report Studio and JDashboard do not support underlining chart text so this property will be ignored when the chart runs in Web Report Studio or is used in a dashboard.
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

Specifies the alignment format of the legend entry labels.

![Format Legend dialog - Orientation](https://devnet.logianalytics.com/hc/article_attachments/4404901230615/fmtlgnd_orntatn.gif)

**Orientation**

Specifies the orientation of the legend entry labels.

**Angle**

Specifies the angel of the legend entry labels.

## Format

Specifies properties for the legend entry labels, which take effect only when the property [Label Format Source](https://devnet.logianalytics.com/hc/en-us/articles/1500010033962-Chart-Legend-Properties#LabelFormatSource) of the chart legend is set to Legend Label Format in the Report Inspector.

![FFormat Legend dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404909207063/fmtlgnd_fmt.gif)

**Category**

Lists the category types. Select one to customize its format.

**Format**

Lists all the [formats](https://devnet.logianalytics.com/hc/en-us/articles/1500010030282-Data-Format-Dialog#DataFormat) of the selected category. Select the required one and select Add to add it as the format of the specified category. You can add only one format for each category.

**Properties**

Specifies the properties for the format that you selected.

**Auto Scale in Number**

Enabled when the series field is of the Number data type. It specifies whether to
automatically scale the field values that fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

By default it is set to auto which means that the setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#AutoScale). When it is true, the specified format applies to the integer part of the values after scaled, but if the specified format conflicts with Auto Scale in Number, for example the values are displayed in percentage, then the Auto Scale in Number setting is ignored.

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

## Mark

Specifies the format of the legend entry marks.

![Format Legend dialog - Mark](https://devnet.logianalytics.com/hc/article_attachments/4404909207319/fmtlgnd_mark.gif)

**Customize**

Specifies whether to customize the format of the legend entry marks.

**Use Node as Mark**

Specifies whether to apply the format of line nodes to the legend entry marks. If selected, the legend entry marks will automatically inherit the style and color of line nodes. Available to line charts only.

**Use Line and Node as Mark**

Specifies whether to apply the format of lines and line nodes to the legend entry marks. If checked, the legend entry marks will automatically inherit the style and color of lines and line nodes. Available to line charts only.

**Mark Items**

Specifies the style of the legend entry marks. Select the mark item from the box one by one and choose the style for each item from the drop-down list. Available only when Customize is checked.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
   Adds a mark item to the box.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)  
   Removes a specified mark item from the box.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)  
   Moves a selected mark item up a step.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)  
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
   Specifies the color transparency of the icon border.
* ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif)  
   Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties). Available to charts created using query resources only.

**Preview**

Displays the specified item and mark effects.

## Label

Specifies the text of the legend entry labels. This tab is available only when the legend entry labels show the values of the field displayed on the category or series axis of the chart.

![Format Legend dialog - Label](https://devnet.logianalytics.com/hc/article_attachments/4404901230871/fmtlgnd_lbl.gif)

**Auto**

If checked, the legend entry labels display values of the category/series field. You can uncheck it to customize the label text.

* **Label Text**  
   Specifies the text of the legend entry labels. Select a field from the drop-down list to use its values as the label text or select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901161879/btn_x.gif) to input the desired label text manually.

## Behaviors

Specifies web behaviors to the legend of the chart. This tab is only available to charts in library components.

![Format Legend dialog - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404901231127/fmtlgnd_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event.

**Actions**  
 Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500010068321-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066421-Format-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031042-Format-Line-Dialog)
