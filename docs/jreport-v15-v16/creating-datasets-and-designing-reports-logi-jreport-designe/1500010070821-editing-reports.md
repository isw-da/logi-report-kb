---
title: "Editing Reports"
id: 1500010070821
section: "Creating Datasets and Designing Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports
updated_at: 2021-07-24T10:37:44Z
---

# Editing Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070941-Previewing-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070861-Filtering-Reports)

# Editing Reports

You can make further modifications to a report at any time in order to make it better satisfy your requirements. In Logi JReport Designer, to edit a report is actually to edit the components in it. This topic lists the basic operations used for editing a page report. For more details about working with different components, refer to the specific section of each component in the [Components](https://devnet.logianalytics.com/hc/en-us/articles/1500010063261-Working-with-Components-in-Reports-) topic.

Below is a list of the sections covered in this topic:

* [Inserting Other Components into a Report](#Insert)
* [Duplicating Components](#Duplicate)
* [Resizing Components](#Resize)
* [Deleting Components from a Report](#Delete)
* [Editing Component Properties](#Property)
* [Changing Component Position](#Change)
* [Applying Conditional Formats in a Report](#Format)
* [Predefining Sort and Filter Conditions in a Page Report](#Predefine)

## Inserting Other Components into a Report

After the initial design work of a report, you are also free to insert more components into it. To insert a component, you can either use the Insert menu tab or the Components panel.

## Duplicating Components

You can duplicate any component in a report without creating it the second time.

1. Select the component which you want to duplicate.
2. Right-click the component and then select **Copy** from the shortcut menu (or select the corresponding menu command).
3. In the required position, right-click your mouse, and then select **Paste**.

## Resizing Components

1. Select the component with the size you want to change, and the sizing handles will then appear along the four boundaries of the component.
2. Drag a sizing handle to resize the component to the required size.
3. Repeat the steps to resize other components.

## Deleting cComponents from a Report

If you find any components contained in a report are not required, you can use either of the following two ways to remove it:

* In the Report Inspector, select the node which represents the component and press the **Delete** button on your keyboard.
* In the design area, right-click the component and select **Delete** from the shortcut menu.

## Editing Component Properties

Each component has a set of properties that can be used to customize the appearance and behavior of the component.

To edit the properties of a component, select the component in the report or from the report structure tree in the Report Inspector, then in the Properties sheet modify the property values as required. See [Report Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties) for detailed information about the properties.

After editing the properties you can [save them as a CSS style](https://devnet.logianalytics.com/hc/en-us/articles/1500010070981-CSS-Styles#Create) for future use if needed.

## Changing Component Position

Report templates in Logi JReport use a flow layout model. That is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is to be part of the flow, or separate from it. Besides the report body, [tabular cells](https://devnet.logianalytics.com/hc/en-us/articles/1500010029322-Tabulars), [text boxes](https://devnet.logianalytics.com/hc/en-us/articles/1500010063961-Text-Boxes) and [KPIs](https://devnet.logianalytics.com/hc/en-us/articles/1500010029082-KPIs) themselves in Logi JReport can also act as flow layout containers.

In a flow layout container, objects are positioned relative to one another or absolutely based on their Position property value:

* **Static**  
   The component will be positioned at the location in which it is inserted. The X and Y coordinate properties are disabled. The position of the component cannot be moved other than by having its insertion point moved. This can happen when the text flow preceding the insertion point expands.
* **Relative**  
   The component will be positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y coordinate property values. This value is not available for some kinds of components.
* **Absolute**  
   The component will be located at the position specified by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance it is not affected by having text inserted before it.
  The position of an object in a banded object can only be Absolute.

  When components in the same flow layout container have their Position property value set to Absolute and overlap, you can set the display order of the objects by right-clicking an object and selecting an item from the Move submenu, or selecting the objects and selecting the corresponding move button on the Format menu tab.

  + **![Move Backward button](https://devnet.logianalytics.com/hc/article_attachments/4404901113623/btn_mvbckwd.gif) Move Backward**  
     Moves the component one step towards the back.
  + **![Move to Back button](https://devnet.logianalytics.com/hc/article_attachments/4404909111831/btn_mv2bck.gif) Move to Back**  
     Moves the component to the back.
  + **![Move Forward button](https://devnet.logianalytics.com/hc/article_attachments/4404901113879/btn_mvfrwd.gif) Move Forward**  
     Moves the component one step closer to the front.
  + **![Move to Front button](https://devnet.logianalytics.com/hc/article_attachments/4404909112087/btn_mv2frnt.gif) Move to Front**  
     Moves the component to the front.

You can change the Position property of a component in any of the following ways:

* In the design area, right-click the component and on the shortcut menu, select the required item from the Position submenu.
* In the design area, select the component, then select the **Format**/**Home** menu tab and select the required item from the Position drop-down list.
* In the Report Inspector, select the node which represents the component, then set its Position property value as required.

In the same flow layout container, when components overlap, they follow the rule that the component inserted later covers the one earlier and the component with Absolute position covers the one with Static position. If different types of objects in a chart overlap, the order of covering is as follows: chart legend > chart label > chart paper or chart data label.

## Applying Conditional Formats in a Report

Conditional format enables you to highlight the values that are important in a report or might need to be acted on by the end users.

You can apply conditional formats on the following data fields in a report: DBField, Formula Field, Parameter Field, Summary Field. For more information, see [Adding conditional formats to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010063761-DBFields#Format).

[Areas in shape maps](https://devnet.logianalytics.com/hc/en-us/articles/1500010063881-Shape-Maps#Format) and [markers in geographic maps](https://devnet.logianalytics.com/hc/en-us/articles/1500010063861-Modifying-Geographic-Maps#Format)  can also be applied with conditional formats.

In a chart, you can add [conditional color fills](https://devnet.logianalytics.com/hc/en-us/articles/1500010063341-Applying-Conditional-Color-Fills-to-Charts) to apply different color patterns to its data markers based on different value ranges.

## Predefining Sort and Filter Conditions in a Page Report

For page reports creating using query resources, you can predefine sort and filter conditions on the charts, tables, crosstabs and banded objects in them so that when the page reports are published to Logi JReport Server and loaded in Page Report Studio, data in the specified data components in the reports will be displayed in the order you prefer, or be narrowed down as you desire.

The predefined sort and filter conditions in a page report are based on the result set of all the other sort and filter conditions applied to the report.

**To predefine sort conditions in a report:**

1. Select a chart, table, crosstab or banded object in the report to which the sort conditions will be applied.
2. Select **Report** > **Edit Sort & Filter** to show the [Edit Sort and Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010030562-Edit-Sort-and-Filter-Dialog) dialog. The Sort tab is active by default.

   ![Edit Sort and Filter dialog - Sort](https://devnet.logianalytics.com/hc/article_attachments/4404909126807/edtsrtfltr_srt.gif)
3. In the Fields box, all the fields in the dataset the data component uses are displayed. Select the field by which to sort the data from the box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) to add it to the Sort By box. To sort by two or more fields, select all of them and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif).

   If the [Customize Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets#Customize) feature hasn't been applied to the dataset the data component uses, no fields are available in the Fields box. In this case, select the **Edit Display Name** button in the dialog first to enable the feature on the dataset.
4. To modify the sort direction for a field, select ![Sort Ascending button](https://devnet.logianalytics.com/hc/article_attachments/4404909127063/btn_srtasnd.gif) (ascending) or ![Sort Descending button](https://devnet.logianalytics.com/hc/article_attachments/4404909127319/btn_srtdsnd.gif) (descending) in the Direction column.
5. To change the sort priority of the fields, select the field in the Sort By box, and then select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to move it up or down.
6. Select **OK** to accept the settings.

**To predefine filter conditions in a report:**

1. Select a chart, table, crosstab or banded object in the report to which the filter conditions will be applied.
2. Select **Report** > **Edit Sort & Filter** to show the Edit Sort and Filter dialog, then switch to the **Filter** tab.

   ![Edit Sort and Filter dialog - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404909127575/rpt_edit_srtfltr.gif)
3. Select the **Add Condition** button to add a condition line.
4. From the field drop-down list, select the field on which the filter will be based.

   If the [Customize Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010070661-Creating-and-Managing-Datasets#Customize) feature hasn't been applied to the dataset the data component uses, no fields are available in the field drop-down list. In this case, select the **Edit Display Name** button in the dialog first to enable the feature on the dataset.
5. From the operator drop-down list, set the operator with which to compose the filter expression.
6. In the value combo box, type the value of how to filter the field or select the value from the drop-down list.
7. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
8. Select **OK** to save the condition.

**Note:** The predefined sort and filter conditions will also affect the preview result in Logi JReport Designer, and the result produced from being run in other formats besides Page Report Result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070941-Previewing-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010070861-Filtering-Reports)
