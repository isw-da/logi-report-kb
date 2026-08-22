---
title: "Format Donut Dialog Box"
id: 1500010097041
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097041-Format-Donut-Dialog-Box
updated_at: 2021-07-23T19:15:28Z
---

# Format Donut Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059182-Format-Dial-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059202-Format-Floor-Dialog-Box)

# Format Donut Dialog Box

You can use the Format Donut dialog box to [format the donuts of a donut chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010056982-Formatting-the-Pies-Donuts-and-KPI-Value-Labels-in-a-Pie-Donut-Chart). This topic describes the options in the dialog box.

Designer displays the Format Donut dialog box when you right-click a donut in a donut chart and select Format Donut from the shortcut menu, or double-click any section in a donut of a donut chart.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

* [General Tab](#General)
* [Fill Tab](#Fill)
* [Border Tab](#Border)
* [Data Label Tab](#Data)
* [Hint Tab](#Hint)
* [Behaviors Tab](#Behaviors)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## General Tab

Use this tab to specify the general properties of the donuts.

![Format Donut - General](https://devnet.logianalytics.com/hc/article_attachments/4404848555799/fmtdonut_gnrl.gif)

**Option**

You can specifies the options of the donuts in this box.

* **Gap Amount**  
  Specify the gap between two donuts.
* **Explode Amount**  
  Specify the gap between every section and the central point of a donut.
* **Donut Hole**  
  Specifythe radius percentage of the donut hole to the total donut circle.
* **Show Donut Name**  
  Select to show the names of the donuts.

**KPI Value**

Designer enables the options in this box if you do not set the chart property [Swap Groups](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#SwapGroups) to "true".

* **Show KPI Value**  
  Select to show the KPI value for each donut.
* **KPI Value**  
  Specify the KPI value to display on each donut. Type the value in the text box or select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif) and select a formula or summary from the drop-down list to use its value as the KPI value.
  + **Auto**  
    Select to use the total value of each donut as the KPI value.
* **Position**  
  Select the position of the KPI value relative to the donuts: top, bottom, center, or customized. If you select "customized", you can specify the position by dragging any KPI value in the donut chart in the design area.

## Fill Tab

Use this tab to specify the color pattern to fill the donut sections.

![Format Donut - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404848556055/fmtdonut_fill.gif)

**Use Single Color**

Select to apply single color pattern to the donut sections.

* **Self Settings**  
  Select to apply the color pattern to the donuts themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.
* **Color**  
  Specify the color for the selected donut section if the chart has no series field, or the color of the donut sections in the current data series if the chart has series field. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the transparency of the color.
* **Color List**  
  Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058302-Color-List-Dialog-Box) to modify the color pattern for donut sections in the same data series respectively.

**Use Single Color with Condition**

Select to apply different color patterns to the donut sections based on different conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
    The drop-down list contains all the available fields to which you can apply the conditional fill. Select the field on which you want to define the conditions.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
    Select to add a new condition.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
    Select to delete the specified user-defined condition.
  + **Value**  
    Designer displays the column when you select the category or series field of the chart, or a field the values of which are not numbers from the Select Field drop-down list. It shows the values that you specify for each condition.
  + **Start Value**  
    Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the start values that you specify for each condition.
  + **End Value**  
    Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the end values that you specify for each condition.
  + **Color**  
    The column shows the colors that you specify to apply to the values which meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    The column shows the transparency of the colors that you specify for the conditions.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    Designer displays the option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list.
    Select it if you want to display data in the condition expression as value.
  + **Percent**  
    Designer displays the option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. Select it if you want to display data in the condition expression in percent.
* **Advanced**
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
    Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box#Chart) to edit the condition and its color pattern.
  + **Condition**  
    The column shows the default condition "Other" and the expression of the condition that you define in the Edit Condition dialog box.
  + **Color**  
    The column shows the color that you specify to apply to the values which meet the condition you define in the Edit Condition dialog box. For the default "Other" condition, you can edit its color by selecting the color indicator and selecting a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or inputting the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    The column shows the transparency of the color that you specify for the condition in the Edit Condition dialog box. For the default "Other" condition, you can select in the cell to specify the transparency.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    The option indicates that Designer displays data in the condition expression as value. You cannot change it.
  + **Percent**  
    Designer does not support the option when you edit conditions in the advanced mode.

**Use Multiple Colors with Condition**

Designer does not support this fill type on donut charts.

**Sample**

The box displays a preview sample of your selection.

## Border Tab

Use this tab to specify the properties for the border of the donut sections.

![Format Donut - Border](https://devnet.logianalytics.com/hc/article_attachments/4404856953751/fmtdonut_border.gif)

**Show Border**

Select to show the border of the donut sections. Designer enables the other border properties in this tab after you select the option.

**Color**

Specify the color of the border. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specify the transparency for the color of the border.

**Line Style**

Select the line style of the border.

**Thickness**

Specify the thickness of the border, in pixels.

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

The box displays a preview sample of your selection.

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

## Data Label Tab

Use this tab to specify the properties of data labels on the donuts.

![Format Donut - Data Label](https://devnet.logianalytics.com/hc/article_attachments/4404848556439/fmtdonut_data.gif)

**Static Data Label**

You can specify the properties of the static data labels on the donuts in this box.

* **Show Static Data Label**  
  Select to show the static data labels. Designer enables the other static data label properties after you select this option.
* **Position**  
  Select the position of the static data labels on the donuts.
  + **auto fit**  
    Select to display the static data labels automatically.
  + **sticker**  
    Select to display the static data labels beside the donut sections.
  + **slim leg**  
    Select to display the static data labels beside the donut sections and pointed by thin lines.
  + **best fit**  
    Select to display the static data labels at the best fit position automatically.
  + **on slices**  
    Select to display the static data labels on the donut sections (slices).
* **Data Label Type**  
  Select in which way to display the values in the static data labels.
  + **value**  
    Select to show the value for each donut section.
  + **category name**  
    Select to show the category name for each donut section.
  + **percent**  
    Select to show the percentage of each donut section to the total.
  + **value and percent**  
    Select to show the value and the percentage for each donut section.
  + **category name, value**  
    Select to show the category name and value for each donut section.
  + **category name, percent**  
    Select to show the category name and percentage for each donut section.
  + **category name, value, percent**  
    Select to show the category name, value, and percentage for each donut section.
* **Auto Scale in Number**  
  Specify whether to automatically scale the Number values in the static data labels which fall into the following two ranges:
  + When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
  + When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

  By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.
* **Line Color**  
  Specify the color of the thin lines that point to the static data labels. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Suppress Label When 0**  
  Select if you do not want to display the static data label whose value is 0 in the chart.
* **Show Truncated Label**  
  Select to truncate the static data labels that go beyond the boundaries of the chart paper instead of them being hidden altogether.

**Font**

You can specify the font format of the text in the static data labels in this box.

* **Font list**  
  The drop-down list contains all the font faces that you can select to apply to the text.
* **Font Size**  
  Specify the font size of the text.
* **Font Color**  
  Specify the font color of the text. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Transparency**  
  Specify the color transparency of the text.
* **Rotation**  
  Specify the rotation angle of the text around its center, in degrees. The default value is 0.
* **Shearing**  
  Specify the gradient of the text.

**Effects**

You can specify the special effects for the text in the static data labels in this box.

* **Style**  
  Select the font style of the text. It can be one of the following: plain, bold, italic, and bold italic.
* **Strikethrough**  
  Select the style of the horizontal line using which to strikethrough the text. It can be one of the following: none, thin line, bold line, and double lines.
* **Underline**  
  Select the style of the horizontal line under the text. It can be one of the following: none, single, single lower, bold line, bold lower, double lines, bold double, patterned line, and bold patterned. When you select "patterned line" or "bold patterned", Designer draws a line or bold line in the pattern of the text.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) Web Report Studio and JDashboard do not support underlining chart text, therefore, Logi Report Engine ignores this property when the chart runs in Web Report Studio or is used in a dashboard.

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

## Hint Tab

Use this tab to specify the properties for the hint of the donut sections.

![Format Donut - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404856954007/fmtdonut_hint.gif)

**Show Category and Series**

Select to include the category and series values in the hint.

**Auto Scale in Number**

Specify whether to automatically scale the Number values in the hint which fall into the following two ranges:

* When 1000 <= value < 10^15, Designer applies the following quantity unit symbols of the International System of Units to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, Designer uses scientific notation to scale the values.

By default, Designer selects "auto" for the option, meaning, Designer applies the setting that you specify for the same property [on the chart in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500010061902-Chart-Properties#AutoScale) for the values. If you select "true", Designer applies the specified format to the integer part of the values after scaling them; however, if the specified format conflicts with the logic of Auto Scale in Number, for example, the values display in percentage, Designer ignores the Auto Scale in Number setting. Select "false" if you do not want to scale the values.

## Behaviors Tab

Designer displays the Behaviors tab only when the donut chart is in a library component. You can use it to specify web behaviors to the donuts.

![Format Donut - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404856954263/fmtdonut_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new web behavior line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Up button**

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Down button**

Select to move the specified web behavior lower in the list.

**Events**

The column shows the events that you select to trigger the web actions.

**Actions**

The column shows the actions that you specify for the events to trigger. To bind a web action to an event, select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the action cell and Designer displays the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box) for you to specify the web action.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059182-Format-Dial-Gauge-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059202-Format-Floor-Dialog-Box)
