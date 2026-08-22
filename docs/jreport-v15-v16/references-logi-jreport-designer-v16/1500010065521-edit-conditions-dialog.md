---
title: "Edit Conditions Dialog"
id: 1500010065521
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065521-Edit-Conditions-Dialog
updated_at: 2021-07-24T10:38:59Z
---

# Edit Conditions Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030382-Edit-Color-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065541-Edit-Display-Name-Dialog)

# Edit Conditions Dialog

The Edit Conditions details and functions of the dialog vary according to different sources it is opened from.

If it is opened by selecting the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif) in the [Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500010064981-Conditional-Formatting-Dialog) dialog, [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500010066921-Insert-Link-Dialog) dialog, [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500010030482-Edit-Link-for-Page-Report-Dialog) dialog, the Display screen of the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500010064921-Chart-Wizard-Dialog#Display) or [Create Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010030062-Create-Chart-Dialog#Display) wizard for the Back-to-back Bench chart type in a query based page report, or selecting the Add or Edit button in the [Shape Map Area Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500010031682-Shape-Map-Area-Condition-Formatting-Dialog) dialog, it is used to add a new or edit an existing condition for the selected object.

![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901131543/edtcndtn.gif)

The options in the dialog are as follows.

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Lists the logic operator.

* **And**  
   Logic operator And which is applied to this and the next line.
* **Or**  
   Logic operator Or which is applied to this and the next line.
* **And Not**  
   Logic operator And Not which is applied to this and the next line.
* **Or Not**  
   Logic operator Or Not which is applied to this and the next line.

**Field**

Specifies the field on which the condition is based.

**Operator**

Specifies the operator to compose the condition expression.

* **=**  
   Equal to
* **>**  
   Greater than
* **>=**  
   Greater than or equal to
* **<**  
   Less than
* **<=**  
   Less than or equal to
* **!=**  
   Not equal to

**Value**

Specifies the value of how to build the condition.

* If you are editing conditional link or conditional formatting on a field, you can either type in the value manually or select the value from the drop-down list, where the top 50 values of the selected field are listed. When you are editing conditional formatting on a field in a crosstab, the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) is available. Select the button and you can choose an object from the drop-down list to use its value in the condition.
* If you are editing conditional formatting on map areas, type in the value manually or select the button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the value text box to specify the value.

**Condition Expression**

Displays the condition expression.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

If it is opened by selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif) in the Fill tab of the Format Bar/Pie/Donut/Rectangle dialog when Use Single Color with Condition is selected, it is used to add more complicated [conditional fill to the values of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts). The options in the dialog are as follows.

![Edit Conditions dialog - Format Bar/Pie/Donut/Rectangle](https://devnet.logianalytics.com/hc/article_attachments/4404909225751/edtcndtn1.gif)

**Select Query for Value Field**

Specifies the query which contains the fields you want to use as the values to build the condition.

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Lists the [logic operator](#Logic): And, Or, And Not, Or Not.

**Field**

Specifies the field on which the condition is based.

**Operator**

Specifies the [operator](#Operator) to compose the condition expression. It can be "=", ">", ">=", "<", "<=", "!=".

**Value**

Specifies the field in the selected query as the value to build the condition. You can also select <Input...> and input the value directly in the text box.

**Condition Expression**

Displays the condition expression.

**Color**

Specifies the color that will be applied to the chart values which meet the condition. Select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and input the value directly in the text box.

**Transparency**

Specifies the transparency of the color. Select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and input the value directly in the text box.

**Value**

Specifies to display the data in the condition expression as value. The option is applied only when the field which the condition is based on is a value field or a field that returns a number.

**Percent**

Specifies to display the data in the condition expression in percent. The option is applied only to pie chart, 100% Stacked Bar/Bench 2-D chart and 100% Stacked Bar/Bench 3-D chart, and only when the field which the condition is based on is a value field or a field that returns a number.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

If it is opened by selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif) in the Fill tab of the Format Line dialog when Use Single Color with Condition is selected, it is used to add more complicated [conditional fill to the values of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts). The options in the dialog are as follows.

![Edit Conditions dialog - Line](https://devnet.logianalytics.com/hc/article_attachments/4404909226007/edtcndtn3.gif)

**Select Query for Value Field**

Available when Imported Conditions is checked. It specifies the query which contains the fields you want to use as the values to build the condition.

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Lists the [logic operator](#Logic): And, Or, And Not, Or Not.

**Field**

Specifies the field on which the condition is based.

**Operator**

Specifies the [operator](#Operator) to compose the condition expression. It can be "=", ">", ">=", "<", "<=", "!=".

**Value**

Specifies the value of how to build the condition. When Imported Conditions is checked, you can select a field in the specified query as the value to build the condition.

**Condition Expression**

Displays the condition expression.

**Fill**

Specifies the fill effect of the chart values which meet the condition. Disabled when Apply Color to Line in the Node tab of the Format Line dialog is checked.

* **Color**  
   Specifies the color schema.

  If Imported Conditions is unchecked, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette), or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box. When Imported Conditions is checked, select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and input the value directly in the text box.
* **Transparency**  
   Specifies the transparency of the color schema. When Imported Conditions is checked, you can select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and input the value directly in the text box.

**Area**

Specifies properties for the areas that meet the condition, which are formed by the chart axes and the chart line. Applies to 2-D lines only.

* **Color**  
   Specifies the color schema.
  When Imported Conditions is checked, you can select a field in the specified query to control the color.
* **Transparency**  
   Specifies the transparency of the color schema. When Imported Conditions is checked, you can select a field in the specified query to control the transparency.

**Line**

Specifies the line pattern of the chart values that meet the condition.

* **Line Style**  
   Specifies the style of the chart line.
* **Thickness**  
   Specifies the line thickness, in pixels.

**Sample**

Displays a preview sample of your settings.

**Imported Conditions**

Specifies whether to use field values to build the condition and control the color and transparency properties values.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

If it is opened by selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) or ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif) in the Node tab of the Format Line dialog when Use Single Color with Condition is selected, it is used to add more complicated [conditional fill to the values of a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts). The options in the dialog are as follows.

![Edit Conditions dialog - Node](https://devnet.logianalytics.com/hc/article_attachments/4404901269527/edtcndtn4.gif)

**Select Query for Value Field**

Available when Imported Conditions is checked. It specifies the query which contains the fields you want to use as the values to build the condition.

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Lists the [logic operator](#Logic): And, Or, And Not, Or Not.

**Field**

Specifies the field on which the condition is based.

**Operator**

Specifies the [operator](#Operator) to compose the condition expression. It can be "=", ">", ">=", "<", "<=", "!=".

**Value**

Specifies the value of how to build the condition. When Imported Conditions is checked, you can select a field in the specified query as the value to build the condition.

**Condition Expression**

Displays the condition expression.

**Shape**

Specifies shape properties of the nodes the values of which meet the condition.

* **Style**  
   Specifies the style of the nodes.
* **Transparency**  
   Specifies the transparency of the color schema. When Imported Conditions is checked, you can select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and input the value directly in the text box.
* **Show Node**  
   Specifies whether to show the nodes. When Imported Conditions is checked, you can select a field in the specified query the values of which are true or false to control it, or select <Input...> and input the value directly in the text box. Only when the property is set to true, the node related properties for the line chart can take effect.
* **Width**  
   Specifies the width of the nodes, in pixels.
* **Height**  
   Specifies the height of the nodes, in pixels.
* **Color**  
   Specifies the color of the nodes.

  If Imported Conditions is unchecked, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette), or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box. When Imported Conditions is checked, select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and input the value directly in the text box.

**Border**

Specifies the border properties of the nodes the values of which meet the condition. Available when the node is not of the plus, multiplication, star1 or star2 style.

* **Border Color**  
   Specifies the border properties of the nodes. Available when the node is not of the plus, multiplication, star1 or star2 style.
  When Imported Conditions is checked, you can select a field in the specified query to control the color.
* **Transparency**  
   Specifies the transparency for the border of the nodes. When Imported Conditions is checked, you can select a field in the specified query to control the transparency.
* **Thickness**  
   Specifies the thickness for the border of the nodes, in pixels.
* **Line Style**   
   Specifies the line style for the border of the nodes.

**Imported Conditions**

Specifies whether to use field values to build the condition and control values of some node properties.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

If it is opened by selecting the button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) in the [Edit Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010030642-Edit-Values-Dialog) dialog. It is used to compose an expression for retrieving field values when [configuring business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500010028582-Business-View-Security#Configure).

![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901269783/edtcndtn2.gif)

The options in the dialog are as follows.

**Add Condition**

Adds a new condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in a group. Conditions can also be added to an existing group by selecting the conditions and the group while holding the Ctrl button, and then selecting the Group button.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Logic**

Lists the [logic operator](#Logic): And, Or, And Not, Or Not.

**Field**

The field is read only.

**Operator**

Specifies the operator to compose the condition expression.

* **=**  
   Equal to
* **>**  
   Greater than
* **>=**  
   Greater than or equal to
* **<**  
   Less than
* **<=**  
   Less than or equal to
* **!=**  
   Not equal to
* **[not] in**  
   Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For the operator "in" or "not in", multiple values separated by comma (,) are allowed.
* **[not] like**  
   Like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, only "\_" and "%" are supported.
* **[not] between**  
   Allows the system to evaluate whether or not data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", there are two value text boxes for inputting the same type of values.
* **is [not] null**  
   It is used in WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", the value text box is hidden.

**Value**

Specifies the value of how to build the condition. You can either type in the value manually or select the value from the drop-down list, where the top 50 values of the selected field are listed.

When the field is based on a formula which references a parameter, the value list will be null. Parameters are not supported here.

**SQL Statement**

Displays the statement expression.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010030382-Edit-Color-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010065541-Edit-Display-Name-Dialog)
