---
title: "Format Rectangle Dialog"
id: 1500010031102
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010031102-Format-Rectangle-Dialog
updated_at: 2021-07-24T10:38:45Z
---

# Format Rectangle Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031082-Format-Radar-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066521-Format-Rectangle-Title-Dialog)

# Format Rectangle Dialog

The Format Rectangle dialog helps you to [format the rectangles of the specified group in a heat map](https://devnet.logianalytics.com/hc/en-us/articles/1500010063561-Formatting-the-Rectangles-and-Rectangle-Titles-in-a-Heat-Map#Rectangle). It appears:

* When there is only one group in the heat map, right-click on the heat map, and then select Format Rectangle from the shortcut menu.
* When there are two or more groups in the heat map, right-click on the heat map, and then select a desired group field from the Format Rectangle submenu.

The dialog contains the following tabs: [Fill](#Fill), [Separator](#Separator) and [Behaviors](#Behaviors) (the Behaviors tab is available to charts in library components only).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Fill

Specifies the fill properties for rectangles of the heat map.

![Format Rectangle - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404901224983/fmtrctgl_fill.gif)

**Use Single Color**

It varies with color patterns as follows.

* When the heat map is colored by one of the following cases: no field, 1 to n groups, 1 to n groups and 1 summary
  + **Color**  
     Specifies the color schema for the rectangles. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
  + **Transparency**  
     Specifies the transparency of the color schema.
  + **Self Settings**  
    Specifies whether to edit the color pattern for the rectangles themselves. When unchecked, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500010069721-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.
  + **Vary Colors by Color List**  
     Specifies whether or not to make colors of the rectangles vary.
  + **Color List**  
     Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500010030022-Color-List-Dialog) dialog to modify the color pattern for each rectangle.
* When the heat map is colored by a summary
  + **Start color**  
     Specifies the start color mapped to the minimum summary value.
  + **End color**  
     Specifies the end value mapped to the maximum summary value.
  + **Reversed**  
     Specifies whether to reverse the start color and end color.

    Once the option is switched between checked and unchecked, the start and end color on the gradient color bar will be switched accordingly.
  + **Color When Zero**  
     Specifies whether to map the zero value to a specific color.
    If it is unchecked, the gradient color changes from the start color to the end color directly; when checked, the gradient color changes from the start color to the zero value color, and then from the zero value color to the end color.
  + **Color When Null**  
     Specifies the color for the null values.

**Use Single Color with condition**

If checked, each rectangle can have its own single color pattern based on the defined conditions. You can select the Advanced or Normal button to switch between the two editing modes to edit the conditions.

* **Normal**
  + **Select Field**  
     Lists all the available fields to which the conditional fill can be applied. Select the field on which you want to define the conditions from the drop-down list.
  + **Value**  
     Specifies the value of the condition. Available when you select a group-by field or a field whose return value is not a number from the Select Field drop-down list.
  + **Start Value**  
     Specifies the start value of the condition. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **End Value**  
     Specifies the end value of the condition. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
  + **Transparency**  
     Specifies the transparency for the color of the condition.
  + ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)  
     Adds a new condition line.
  + ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901177495/btn_rmv1.gif)  
     Removes the selected condition line.
  + **Label**  
     If checked, you can modify the condition expression of the selected condition line which will be shown as the legend entry label.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
* **Advanced**
  + **Condition**  
     Displays the condition you have defined in the Edit Condition dialog.
  + **Color**  
     Specifies the color that will be applied to the values which meet the condition.
  + **Transparency**  
     Specifies the transparency for the color of the condition.
  + ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif)  
     Opens the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500010065521-Edit-Conditions-Dialog#Chart) dialog to create or edit a condition.
  + **Label**  
     If checked, you can modify the condition expression of the selected condition line which will be shown as the legend entry label.
  + **Value**  
     Specifies to display data in the condition expression as value. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.
  + **Percent**  
     Specifies to display data in the condition expression in percent. Available only when you select a value field or a field that returns a number from the Select Field drop-down list.

**Sample**

Displays a preview sample of your settings.

## Separator

Specifies the line properties of the separator dividing the rectangles of the heat map.

![Format Rectangle - Separator](https://devnet.logianalytics.com/hc/article_attachments/4404909201303/fmtrctgl_sprtr.gif)

**Color**

Specifies the color of the separator.

**Transparency**

Specifies the color transparency of the separator.

**Line Style**

Specifies the line style of the separator.

**Thickness**

Specifies the thickness of the separator.

**Sample**

Shows a rectangle sample according to the settings on the tab.

## Behaviors

Specifies web behaviors to the rectangles of the heat map. This tab is only available to heat maps in library components.

![Format Rectangle - Behaviors](https://devnet.logianalytics.com/hc/article_attachments/4404909201559/fmtrctgl_bhvr.gif)

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a new web behavior line.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected web behavior.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected web behavior up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected web behavior down a step.

**Events**

Specifies the trigger event by selecting one from the drop-down list.

**Actions**

Specifies the action you want the event to trigger.

* ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif)  
   Opens the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500010068321-Web-Action-List-Dialog) dialog to bind a web action to the event.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031082-Format-Radar-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066521-Format-Rectangle-Title-Dialog)
