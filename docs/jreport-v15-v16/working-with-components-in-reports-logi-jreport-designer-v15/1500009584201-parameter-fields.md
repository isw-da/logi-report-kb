---
title: "Parameter Fields"
id: 1500009584201
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584201-Parameter-Fields
updated_at: 2021-07-24T05:55:58Z
---

# Parameter Fields

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583921-DBFields)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563602-Summary-Fields)

# Parameter Fields

A parameter in Logi JReport is a variable whose value is determined at runtime. The runtime parameters help you dynamically control your report results.

Below is a list of the sections covered in this topic:

> * [Inserting a Parameter Field in a Report](#Insert)
> * [Changing the Display Type of a Parameter Field](#Change)
> * [Applying Web Actions to a Parameter Field](#Apply)
> * [Binding a Link to a Parameter Field](#Bind)
> * [Adding Conditional Formats to a Parameter Field](#Format)

## Inserting a Parameter Field in a Report

Parameter fields can be inserted in the report areas listed in [Component placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports#Relationship).

To insert a parameter field into a report, select the required parameter from the Data panel, then drag it to the destination. If the given parameters are not what your want, select the **<New Parameter...>** item to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter) as required. For a business view based report, you can create [local parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Param) to use in the report specifically.

For a query based report, you can also use dialog to insert a parameter field into it as follows:

1. Position the mouse pointer at the destination where you want to insert the parameter and select **Insert** > **Parameter** or **Home** >
   **Insert** > **Parameter.**

   The [Insert Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009587581-Insert-Fields-Dialog) dialog appears.

   ![Insert Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893874583/instfld.gif)
2. Select the required parameter from the Parameters node, then specify its layout in the Insert Layout box.
3. Select the **Insert** button to insert the parameter into the destination.

**Note:** If you insert a parameter into the detail panel of a banded object or table, the name of the parameter will automatically be inserted as a label into the corresponding header panel. Otherwise the parameter and its name label will be placed in the same panel. If you do not want to insert the name label automatically, you can uncheck Insert field name label with field in the Options dialog (**File** > **Options** > **Component** > **Insert field name label with field**).

## Changing the Display Type of a Parameter Field

The display type of a parameter field can be changed, that is to say, you can map the parameter field to another value or image to be displayed instead.

**To change the display type a parameter field:**

1. Right-click the parameter field and select **Display Type** from the shortcut menu.
2. In the Display Type dialog, specify the required display type in the Display As box, and set the options for the selected type.
   * To change the display type of a parameter to list or drop-down list, select the item List or Drop-down List, and then in the Web Options panel, set the name and title. You may notice that a default list item had been added, and its value is the parameter. If you check Use Runtime Value, when running the report, you need to specify a value for the parameter, and then the item same as the value will be selected in the list or drop-down list by default; if you uncheck the option, the Selected text box will be enabled for you to input a value and the item same as this value will be selected. For the List type, you can check Allow Multiple Selections to enable more than one item selected.
   * For other display types, refer to [Changing the Display Type of a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009563422-Changing-the-Display-Type-of-a-Label) for details.
3. Upon finishing, select the **OK** button to close the dialog.

## Applying web actions to a parameter field

A parameter field can be bound with web actions. This allows you to customize a parameter field to make it respond to interactive events, and execute corresponding actions, such as sorting and filtering.

**To apply web actions to a parameter field:**

1. Right-click the parameter field and select **Display Type** from the shortcut menu.
2. In the Web Behaviors box of the Display Type dialog, choose an event from the Events column, then select in the Actions column and select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears in the text box.
3. In the Web Action List dialog, select a web action and define the action as required.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) in the Display Type dialog to add more web behavior lines and specify the events and actions accordingly. If a web behavior is not required, select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove it.
5. Adjust the order of the added web actions by selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif). Then, when an event that has been bound with more than one action happens, the upper action will be triggered first.
6. When done , select **OK** to accept the settings.

For more information about web actions, see [Applying Web Actions to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label).

## Binding a Link to a Parameter Field

You can make a parameter field link to another report, a location specified by a URL, an e-mail address, or a Blob data type field. The link can either be a simple link or a conditional link. With conditional links, different targets can be loaded based on different conditions.

**To bind a link to a parameter field:**

1. Right-click the parameter field and select **Link** on the shortcut menu.
2. In the Insert Link dialog, specify whether it is a conditional link or a simple link, then select the link target and set the options for the link target as required.
3. When done, select **OK**.

For details about different link targets, see [Binding a Link to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label).

## Adding Conditional Formats to a Parameter Field

You can add conditional formats to a parameter field, then when a specified condition is fulfilled, the format bound with the condition will be applied to the field values automatically. This is very useful to highlight values that might need to be acted on by the end user.

**To add conditional formats to a parameter field:**

1. Right-click the parameter field and select **Conditional Formatting**  from the shortcut menu.
2. In the Conditional Formatting dialog, select the  button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a condition.
3. Set the format that will be applied to the field values when the specified condition is fulfilled.
4. Repeat the above two steps to add more conditions and define the format for each condition.
5. When done, select **OK** to save the settings.

For more details about conditional formatting, see [Adding Conditional Formats to a DBField](https://devnet.logianalytics.com/hc/en-us/articles/1500009583921-DBFields#Format).

**See an example:** The SampleComponents catalog, included with Logi JReport Designer, contains reports that have examples of how each component type could be used in a report. For the parameter field examples, open the following reports: `<install_root>\Demo\Reports\SampleComponents\Parameter.cls`, and `<install_root>\Demo\Reports\SampleComponents\ParameterField.cls`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583921-DBFields)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563602-Summary-Fields)
