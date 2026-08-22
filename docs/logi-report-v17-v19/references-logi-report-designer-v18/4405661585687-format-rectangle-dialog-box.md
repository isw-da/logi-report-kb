---
title: "Format Rectangle Dialog Box"
id: 4405661585687
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661585687-Format-Rectangle-Dialog-Box
updated_at: 2022-01-27T20:36:09Z
---

# Format Rectangle Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664498583-Format-Radar-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664501399-Format-Rectangle-Title-Dialog-Box)

# Format Rectangle Dialog Box

You can use the Format Rectangle dialog box to [format the rectangles of the specified group in a heat map](https://devnet.logianalytics.com/hc/en-us/articles/4405664384279-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map#Rectangle). This topic describes the options in the dialog box.

Designer displays the Format Rectangle dialog box when you do either of the following:

* When there is only one group in the heat map, right-click the heat map and select Format Rectangle from the shortcut menu.
* When there are two or more groups in the heat map, right-click the heat map and select a desired group field from the Format Rectangle submenu.

The dialog box contains the following tabs (Designer displays the Behaviors tab only when the chart is in a library component):

* [Fill Tab](#Fill)
* [Separator Tab](#Separator)
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

Use this tab to specify the color pattern to fill the rectangles of the heat map.

![Format Rectangle - Fill](https://devnet.logianalytics.com/hc/article_attachments/4420394775319/fmtrctgl_fill.gif)

**Use Single Color**

Select to apply single color pattern to the rectangles. Designer displays different options for setting the color pattern according to how the heat map is colored by.

* You see the following options if the heat map is colored by a summary:
  + **Start color**  
    Specify the start color which Designer maps to the minimum value of the summary. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
  + **End color**  
    Specify the end color which Designer maps to the maximum value of the summary.
  + **Reversed**  
    Select to reverse the start color and end color on the gradient color bar.
  + **Color When Zero**  
    Select to map the zero value to the specified color.
    When you do not select this option, the gradient color changes from the start color to the end color directly; otherwise, the gradient color changes from the start color to the zero value color, and then from the zero value color to the end color.
  + **Color When Null**  
    Specify the color for the null value.
* You see the following options if the heat map is colored by one of the following cases: no field, 1 to n groups, 1 to n groups and 1 summary:
  + **Color**  
    Specify the color for the rectangles. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
  + **Transparency**  
    Specify the transparency of the color.
  + **Self Settings**  
    Select to apply the color pattern to the rectangles themselves only. If you do not select the option, Designer synchronizes the color settings you define here to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/4405664650263-Chart-Properties#Pattern) on the chart object in the Report Inspector, which the data markers of other subtypes can also apply if the chart is a combo chart.t.
  + **Vary Colors by Color List**  
    Select to apply different colors to the rectangles.
  + **Color List**  
    Select to open the [Color List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661476887-Color-List-Dialog-Box) to modify the color pattern for each rectangle.

**Use Single Color with condition**

Select to make each rectangle apply its own single color pattern based on the defined conditions. You can select Advanced or Normal to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
    This drop-down list contains all the available fields to which you can apply the conditional fill. Select the field on which you want to define the conditions.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif)**Add button**  
    Select to add a new condition.
  + ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif)**Remove button**  
    Select to delete the specified user-defined condition.
  + **Value**  
    Designer displays the column when you select a group-by field of the chart, or a field the values of which are not numbers from the Select Field drop-down list. It shows the values that you specify for each condition.
  + **Start Value**  
    Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the start values that you specify for each condition.
  + **End Value**  
    Designer displays the column when you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. It shows the end values that you specify for each condition.
  + **Color**  
    This column shows the colors that you specify to apply to the values which meet the conditions. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
  + **Transparency**  
    This column shows the transparency of the colors that you specify for the conditions.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.
  + **Value**  
    Designer displays this option after you select a value field of the chart, or a field containing numeric values from the Select Field drop-down list. Select it if you want to display data in the condition expression as value.
  + **Percent**  
    Designer does not support this option when you edit conditions for a heat map.
* **Advanced**
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420394656407/btn_edit.gif)**Edit button**  
    Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664456727-Edit-Conditions-Dialog-Box#Chart) to create or edit a condition.
  + **Condition**  
    This column shows the default condition "Other" and the expressions of the condition that you define in the Edit Condition dialog box.
  + **Color**  
    This column shows the color that you specify for the default "Other" condition and the color that you specify to apply to the values which meet the condition you define in the Edit Condition dialog box. To edit the color of the default "Other" condition, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value (for example, 0xff0000) of a color in the text box.
  + **Transparency**  
    This column shows the transparency of the color that you specify for the default "Other" condition and the transparency of the color that you specify for the values which meet the condition you define in the Edit Condition dialog box.
  + **Label**  
    Select to modify the expression of the specified condition, which Designer displays as its legend entry label.

**Sample**

This box displays a preview sample based on your selections.

## Separator Tab

Use this tab to specify the line properties of the separator dividing the rectangles in the heat map.

![Format Rectangle - Separator](https://devnet.logianalytics.com/hc/article_attachments/4420394775703/fmtrctgl_sprtr.gif)

**Color**

Specify the color of the separator. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Transparency**

Specify the transparency for the color of the separator.

**Line Style**

Select the line style of the separator.

**Thickness**

Specify the thickness of the separator.

**Sample**

This box displays a preview sample based on your selections.

## Behaviors Tab

Designer displays the Behaviors tab only when the heat map is in a library component. You can use it to specify web behaviors to the rectangles of the heat map.

![Format Rectangle - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4420410734871/fmtrctgl_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif)**Add button**

Select to add a new web behavior line.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif)**Remove button**

Select to delete the specified web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified web behavior higher in the list. At runtime, when an event bound with more than one action happens, JDashboard triggers the upper action first.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified web behavior lower in the list.

**Events**

This column shows the events that you select to trigger the web actions.

**Actions**

This column shows the web actions that you specify for the events to trigger. Select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420410588951/btn_ellipsis1.gif) in each cell to bind the web action using the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661744791-Web-Action-List-Dialog-Box).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664498583-Format-Radar-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664501399-Format-Rectangle-Title-Dialog-Box)
