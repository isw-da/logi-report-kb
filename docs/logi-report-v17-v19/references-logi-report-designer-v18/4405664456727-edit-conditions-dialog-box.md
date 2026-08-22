---
title: "Edit Conditions Dialog Box"
id: 4405664456727
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664456727-Edit-Conditions-Dialog-Box
updated_at: 2022-01-27T20:36:15Z
---

# Edit Conditions Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661507479-Edit-Color-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661508887-Edit-Display-Name-Dialog-Box)

# Edit Conditions Dialog Box

You can use the Edit Conditions dialog box to edit conditions for the selected object. This topic describes the options in the dialog box, which vary according to different sources where you open it.

---

If you open the dialog box by selecting Add ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) or Edit ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif) in the [Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664435607-Conditional-Formatting-Dialog-Box), [Insert Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664522263-Insert-Link-Dialog-Box), [Edit Link dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661518487-Edit-Link-Dialog-Box), the Display screen of the [Chart Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661468695-Chart-Wizard-Dialog-Box#Display) or [Create Chart dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661481111-Create-Chart-Dialog-Box#Display) for the Back-to-back Bench chart type in a query-based page report, or selecting the Add or Edit button in the [Shape Map Area Conditional Formatting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661643287-Shape-Map-Area-Condition-Formatting-Dialog-Box), you can use it to add a new or edit an existing condition for the selected object.

![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542158487/edtcndtn.gif)

You see the following options in the dialog box:

**Add Condition**

Select to add a new condition line.

**Delete**

Select to delete the specified condition line.

**Group**

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

**Ungroup**

Select to ungroup the specified conditions.

**Up**

Select to move the specified condition or group up to a higher level.

**Down**

Select to move the specified condition or group down to a lower level.

**Logical operator drop-down menu**

Specify the logical operator to apply for the specified condition lines. It can be
"And", "Or", "And Not", or "Or Not".

**Field text box**

Specify the field on which to set the condition.

**Operator drop-down list**

Specify the operator to compose the condition expression.

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

**Value text box**

Specify the value of how to build the condition.

* If you are editing conditional link or conditional formatting on a field, you can either type the value in the text box or select the value from the drop-down list, which contains the top 50 values of the selected field. When you are editing conditional formatting on a field in a crosstab, Designer displays the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4420556102807/btn_fmla.gif). Select the button and you can choose an object from the drop-down list to use its value in the condition.
* If you are editing conditional formatting on shape map areas, type the value or select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) next to the value text box to specify the value.

**Condition Expression**

This box displays the SQL statement of the condition expressions.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If you open the dialog box by selecting Add ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) or Edit ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif) in the Fill tab of the [Format Bar dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661559447-Format-Bar-Dialog-Box), [Format Pie dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661581335-Format-Pie-Dialog-Box), [Format Donut dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661569943-Format-Donut-Dialog-Box), or [Format Rectangle dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661585687-Format-Rectangle-Dialog-Box) while selecting Use Single Color with Condition, you can use it to add more complicated [conditional fill to the values of the chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts).

![Edit Conditions dialog box - Format Bar/Pie/Donut/Rectangle](https://devnet.logianalytics.com/hc/article_attachments/4420550940695/edtcndtn1.gif)

You see the following options in the dialog box:

**Select Query for Value Field**

This drop-down list contains the queries which you can use for editing the conditions. Select the query which contains the fields you want to use as the values to build the conditions.

**Add Condition**

Select to add a new condition line.

**Delete**

Select to delete the specified condition line.

**Group**

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

**Ungroup**

Select to ungroup the specified conditions.

**Up**

Select to move the specified condition or group up to a higher level.

**Down**

Select to move the specified condition or group down to a lower level.

**Logical operator drop-down menu**

Specify the logical operator to apply for the specified condition lines. It can be
"And", "Or", "And Not", or "Or Not".

**Field text box**

Specify the field on which to set the condition.

**Operator drop-down list**

Specify the [operator](#Operator) to compose the condition expression. It can be "=", ">", ">=", "<", "<=", or "!=".

**Value text box**

Specify the field in the selected query as the value to build the condition. You can also select <Input...> and type the value in the text box.

**Condition Expression**

This box displays the SQL statement of the condition expressions.

**Color**

Specify the color to apply to the chart values which meet the condition. Select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and type the value in the text box.

**Transparency**

Specify the transparency of the color. Select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and type the value in the text box.

**Value**

Select to display the data in the condition expression as value. Designer applies this option only when the field which the condition is based on is a value field of the chart, or a field containing numeric values.

**Percent**

Select to display the data in the condition expression in percent. Designer applies this option only to pie chart, 100% Stacked Bar/Bench 2-D chart, and 100% Stacked Bar/Bench 3-D chart, and only when the field which the condition is based on is a value field of the chart, or a field containing numeric values.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If you open the dialog box by selecting Add ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) or Edit ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif) in the Fill tab of the [Format Line dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661579287-Format-Line-Dialog-Box#Fill) while selecting Use Single Color with Condition, you can use it to add more complicated [conditional fill to the values of the line chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts).

![Edit Conditions dialog box - Line](https://devnet.logianalytics.com/hc/article_attachments/4420556204951/edtcndtn3.gif)

You see the following options in the dialog box:

**Select Query for Value Field**

Designer displays the drop-down list when you select Imported Conditions. It contains the queries which you can use for editing the conditions. Select the query that contains the fields you want to use as the values to build the conditions.

**Add Condition**

Select to add a new condition line.

**Delete**

Select to delete the specified condition line.

**Group**

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

**Ungroup**

Select to ungroup the specified conditions.

**Up**

Select to move the specified condition or group up to a higher level.

**Down**

Select to move the specified condition or group down to a lower level.

**Logical operator drop-down menu**

Specify the logical operator to apply for the specified condition lines. It can be
"And", "Or", "And Not", or "Or Not".

**Field text box**

Specify the field on which to set the condition.

**Operator drop-down list**

Specify the [operator](#Operator) to compose the condition expression. It can be "=", ">", ">=", "<", "<=", "!=".

**Value text box**

Specify the value of how to build the condition. When you select Imported Conditions, you can select a field in the specified query as the value to build the condition.

**Condition Expression**

This box displays the SQL statement of the condition expressions.

**Fill**

You can specify the fill effect of the chart values which meet the condition in this box. Designer disables this box if you select Apply Color to Line in the Node tab of the Format Line dialog box.

* **Color**  
  Specify the color.

  If you clear Imported Conditions, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), or type the hexadecimal value (for example, 0xff0000) of a color in the text box; if you select Imported Conditions, you can select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and type the value in the text box.
* **Transparency**  
  Specify the transparency of the color. When you select Imported Conditions, you can select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and type the value in the text box.

**Area**

You can specify properties for the areas that meet the condition in this box (the areas are formed by the chart axes and the chart line). Designer applies these properties to 2-D lines only.

* **Color**  
  Specify the color.

  If you clear Imported Conditions, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), or type the hexadecimal value (for example, 0xff0000) of a color in the text box; if you select Imported Conditions, you can select a field in the specified query the values of which contain strings such as 0x000000 to control the color, or select <Input...> and type the value in the text box.
* **Transparency**  
  Specify the transparency of the color. When you select Imported Conditions, you can select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and type the value in the text box.

**Line**

You can specify the line pattern of the chart values that meet the condition in this box.

* **Line Style**  
  Specify the style of the chart line.
* **Thickness**  
  Specify the line thickness, in pixels.

**Sample**

This box displays a preview sample of your settings.

**Imported Conditions**

Select to use field values to build the conditions and control the color and transparency properties.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If you open the dialog box by selecting Add ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550832791/btn_add.gif) or Edit ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420556150039/btn_edit.gif) in the Node tab of the [Format Line dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661579287-Format-Line-Dialog-Box#Node) while selecting Use Single Color with Condition, you can use it to add more complicated [conditional fill to the values of the line chart](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts).

![Edit Conditions dialog box - Node](https://devnet.logianalytics.com/hc/article_attachments/4420542158999/edtcndtn4.gif)

You see the following options in the dialog box:

**Select Query for Value Field**

Designer displays the drop-down list when you select Imported Conditions. It contains the queries which you can use for editing the conditions. Select the query that contains the fields you want to use as the values to build the conditions.

**Add Condition**

Select to add a new condition line.

**Delete**

Select to delete the specified condition line.

**Group**

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

**Ungroup**

Select to ungroup the specified conditions.

**Up**

Select to move the specified condition or group up to a higher level.

**Down**

Select to move the specified condition or group down to a lower level.

**Logical operator drop-down menu**

Specify the logical operator to apply for the specified condition lines. It can be
"And", "Or", "And Not", or "Or Not".

**Field text box**

Specify the field on which to set the condition.

**Operator drop-down list**

Specify the [operator](#Operator) to compose the condition expression. It can be "=", ">", ">=", "<", "<=", "!=".

**Value text box**

Specify the value of how to build the condition. When you select Imported Conditions, you can select a field in the specified query as the value to build the condition.

**Condition Expression**

This box displays the SQL statement of the condition expressions.

**Shape**

You can specify the shape properties of the nodes, the values of which meet the condition in this box.

* **Style**  
  Specify the style of the nodes.
* **Transparency**  
  Specify the transparency of the color. If you select Imported Conditions, you can select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and type the value in the text box.
* **Show Node**  
  Specify whether to show the nodes. If you select Imported Conditions, you can select a field in the specified query the values of which are true and false to control it, or select <Input...> and type the value in the text box. Designer applies the node related properties for the line chart only when you set this option to "true".
* **Width**  
  Specify the width of the nodes, in pixels.
* **Height**  
  Specify the height of the nodes, in pixels.
* **Color**  
  Specify the color of the nodes.

  If you do not select Imported Conditions, you can select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), or type the hexadecimal value (for example, 0xff0000) of a color in the text box; if you select Imported Conditions, you can select a field in the specified query the values of which contain strings such as "0x000000" to control the color, or select <Input...> and type the value in the text box.

**Border**

Designer displays the box when you select the Style option other than "plus", "multiplication", "star1", or "star2". You can use it to specify the border properties for the nodes, the values of which meet the condition.

* **Border Color**  
  Specify the color of the border.

  If you do not select Imported Conditions, you can select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette), or type the hexadecimal value (for example, 0xff0000) of a color in the text box; if you select Imported Conditions, you can select a field in the specified query the values of which contain strings such as "0x000000" to control the color, or select <Input...> and type the value in the text box.
* **Transparency**  
  Specify the transparency for the color of the border. If you select Imported Conditions, you can select a field in the specified query the values of which are integers between 0 and 100 to control the transparency, or select <Input...> and type the value in the text box.
* **Thickness**  
  Specify the width of the border, in pixels.
* **Line Style**   
  Select the line style of the border.

**Line**

Designer displays the box when you select the Style option of "plus", "multiplication", "star1", or "star2". You can use it to specify the line properties for the nodes, the values of which meet the condition.

* **Thickness**  
  Specify the width of the nodes, in pixels.
* **Line Style**   
  Select the line style of the nodes.

**Imported Conditions**

Select to use field values to build the conditions and control values of some node properties.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

If you open the dialog box by selecting the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550827287/btn_ellipsis2.gif) in the [Edit Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664469271-Edit-Values-Dialog-Box), you can use it to compose an expression for retrieving values when [configuring business view security](https://devnet.logianalytics.com/hc/en-us/articles/4405664363415-Configuring-Business-View-Security-in-a-Catalog).

![Edit Conditions dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556205335/edtcndtn2.gif)

You see the following options in the dialog box:

**Add Condition**

Select to add a new condition line.

**Delete**

Select to delete the specified condition line.

**Group**

Select to add the specified conditions in a group. You can also add conditions to an existing group by selecting the conditions and the group while holding Ctrl on the keyboard and then selecting the Group button.

**Ungroup**

Select to ungroup the specified conditions.

**Up**

Select to move the specified condition or group up to a higher level.

**Down**

Select to move the specified condition or group down to a lower level.

**Logical operator drop-down menu**

Specify the logical operator to apply for the specified condition lines. It can be
"And", "Or", "And Not", or "Or Not".

**Field text box**

This text box displays the group object on which to define the condition. It is read only.

**Operator drop-down list**

Specify the operator to compose the condition expression.

* **=**  
  Equal to
* **>=**  
  Greater than or equal to
* **>**  
  Greater than
* **<**  
  Less than
* **<=**  
  Less than or equal to
* **!=**/**<>**  
  Not equal to
* **[not] in**  
  The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the operator "in" or "not in", you can use multiple values separated by comma (,).
* **[not] like**  
  The like string pattern matching operator is used to compare the first expression string value to the pattern string (the second expression). If you want to use wildcard character in the pattern string, you can only use "\_" and "%".
* **[not] between**  
  The operator allows the system to evaluate whether data values are located between a range of values indicated in the predicate. For the operator "between" or "not between", Designer displays two value text boxes for inputting the same type of values.
* **is [not] null**  
  The operator is used in the WHERE clause predicates to match null values occurring in a specified data field. For the operator "is null" or "is not null", Designer does not display the value text box.

**Value text box**

Specify the value of how to build the condition. You can either type the value in the text box or select the value from the drop-down list, which contains the top 50 values of the selected field.

When the field is based on a formula which references a parameter, the value list is null. Parameters are not supported here.

**SQL Statement**

This box displays the SQL statement of the condition expressions.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661507479-Edit-Color-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661508887-Edit-Display-Name-Dialog-Box)
