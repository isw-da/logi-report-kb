---
title: "Editing Reports"
id: 1500010062762
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062762-Editing-Reports
updated_at: 2021-07-23T19:16:48Z
---

# Editing Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101341-Previewing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101241-Filtering-Reports)

# Editing Reports

You can modify a report at any time in order to make it better satisfy your requirements. In Designer, to edit a report is actually to edit the components in it. This topic introduces the general and common operations you can perform on the report components. For more information about working with different components, refer to the specific topic of each component in [Components](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports).

This topic contains the following sections:

* [Inserting Other Components into a Report](#Insert)
* [Duplicating Components](#Duplicate)
* [Resizing Components](#Resize)
* [Deleting Components from a Report](#Delete)
* [Editing Component Properties](#Property)
* [Changing Component Position](#Change)
* [Applying Conditional Formats in a Report](#Format)
* [Predefining Sort and Filter Conditions for Page Report Data Components](#Predefine)

## Inserting Other Components into a Report

After the initial design work of a report, you are also free to insert more components into it. To insert a component, you can either use the **Insert** menu tab or the **Components** panel.

## Duplicating Components

You can duplicate any component in a report without creating it the second time.

1. Select the component which you want to duplicate.
2. Right-click the component and then select **Copy** from the shortcut menu (or select the corresponding menu command).
3. In the required position, right-click your mouse, and then select **Paste**.

## Resizing Components

1. Select the component with the size you want to change. The sizing handles then appear along the four boundaries of the component.
2. Drag a sizing handle to resize the component to the required size.
3. Repeat the steps to resize other components.

## Deleting Components from a Report

If you find any components contained in a report are not required, you can use either of the following two methods to remove it:

* In the Report Inspector, select the node which represents the component and press the **Delete** button on your keyboard.
* In the design area, right-click the component and select **Delete** from the shortcut menu.

## Editing Component Properties

Each component has a set of properties that you can use to customize the appearance and behavior of the component.

To edit the properties of a component, select the component in the report or from the report structure tree in the Report Inspector, then in the Properties sheet, modify the property values as required. See [Report Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties) for detailed information about the properties.

After editing the properties, you can [save them as a CSS style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062822-Working-with-CSS-Styles#Create) for future use.

## Changing Component Position

Report templates in Designer use a flow layout model, that is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is to be part of the flow, or separate from it. Besides the report body, [tabular cells](https://devnet.logianalytics.com/hc/en-us/articles/1500010094961-Working-with-Tabulars), [text boxes](https://devnet.logianalytics.com/hc/en-us/articles/1500010094981-Working-with-Text-Boxes), and [KPIs](https://devnet.logianalytics.com/hc/en-us/articles/1500010057242-Working-with-KPIs) themselves in can also act as flow layout containers.

In a flow layout container, Designer positions the objects relative to one another or absolutely based on their Position property value:

* **Static**  
  Designer positions the component at the location in which you insert it. The X and Y coordinate properties are disabled. You cannot move the component to another position other than by moving its insertion point. This can happen when the text flow preceding the insertion point expands.
* **Relative**  
  Designer positions the component at an offset to the position at which you insert it. The offset is determined by the X and Y coordinate property values. This value is not available for some types of components.
* **Absolute**  
  Designer locates the component at the position that you specify by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance, it is not affected when you insert text before it.
  The position of an object in a banded object can only be Absolute.

  If you set the Position property value for components in the same flow layout container to Absolute and the components overlap, you can specify the display order of the objects by right-clicking an object and selecting an item from the **Move** submenu, or selecting the objects and selecting the corresponding move button on the **Format** menu tab.

  + ![Move Backward button](https://devnet.logianalytics.com/hc/article_attachments/4404856794647/btn_mvbckwd.gif)**Move Backward**  
    Moves the component one step towards the back.
  + ![Move to Back button](https://devnet.logianalytics.com/hc/article_attachments/4404856795031/btn_mv2bck.gif)**Move to Back**  
    Moves the component to the back.
  + ![Move Forward button](https://devnet.logianalytics.com/hc/article_attachments/4404848372247/btn_mvfrwd.gif)**Move Forward**  
    Moves the component one step closer to the front.
  + ![Move to Front button](https://devnet.logianalytics.com/hc/article_attachments/4404856795287/btn_mv2frnt.gif)**Move to Front**  
    Moves the component to the front.

You can change the Position property of a component using any of the following methods:

* In the design area, right-click the component and on the shortcut menu, select the required item from the **Position** submenu.
* In the design area, select the component, then select the **Format**/**Home** menu tab and select the required item from the **Position** drop-down list.
* In the Report Inspector, select the node which represents the component, then set its Position property value as required.

In the same flow layout container, when components overlap, they follow the rule that the component inserted later covers the one earlier and the component with Absolute position covers the one with Static position. If different types of objects in a chart overlap, the covering order is as follows: chart legend > chart label > chart paper or chart data label.

## Applying Conditional Formats in a Report

Conditional format enables you to highlight the values that are important in a report or the report users might need to act on at runtime.

You can apply conditional formats to the following data fields in a report: DBField, Formula Field, Parameter Field, and Summary Field. For more information, see [Adding Conditional Formats to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields#Format).

You can also apply conditional formats to [areas in shape maps](https://devnet.logianalytics.com/hc/en-us/articles/1500010094801-Using-Shape-Maps#Format) and [markers in geographic maps](https://devnet.logianalytics.com/hc/en-us/articles/1500010057362-Modifying-Geographic-Maps#Format).

In a chart, you can add [conditional color fills](https://devnet.logianalytics.com/hc/en-us/articles/1500010094361-Applying-Conditional-Color-Fills-to-Charts) to apply different color patterns to its data markers based on different value ranges.

## Predefining Sort and Filter Conditions for Page Report Data Components

For page reports using query resources, you can predefine sort and filter conditions on the charts, tables, crosstabs, and banded objects in them, so that after you publish the page reports to Server and run them in Page Report Studio, the specified data components in the reports display data in the order you prefer, and narrow down to show only the data you desire.

The predefined sort and filter conditions in a page report are based on the result set of all the other sort and filter conditions applied to the report.

**To predefine sort conditions in a report:**

1. Select a chart, table, crosstab, or banded object in the report.
2. Select **Report** > **Edit Sort & Filter**. Designer displays the [Edit Sort and Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096421-Edit-Sort-and-Filter-Dialog-Box), and the Sort tab is active by default.

   ![Edit Sort and Filter dialog box - Sort](https://devnet.logianalytics.com/hc/article_attachments/4404856835095/edtsrtfltr_srt.gif)
3. The **Fields** box lists all the fields in the dataset the data component uses. Select the field by which to sort the data from the box and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add it to the **Sort By** box. To sort by two or more fields, select all of them and then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif).

   If you have not applied the [Customize Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets#Customize) feature to the dataset the data component uses, no fields are available in the Fields box. In this case, select the **Edit Display Name** button to enable the feature on the dataset first.
4. To modify the sort direction for a field, select ![Sort Ascending button](https://devnet.logianalytics.com/hc/article_attachments/4404856835351/btn_srtasnd.gif) (ascending) or ![Sort Descending button](https://devnet.logianalytics.com/hc/article_attachments/4404856835735/btn_srtdsnd.gif) (descending) in the **Direction** column.
5. To change the sort priority of the fields, select the field in the **Sort By** box, and then select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button to move it higher or lower.
6. Select **OK** to accept the settings.

**To predefine filter conditions in a report:**

1. Select a chart, table, crosstab, or banded object in the report.
2. Select **Report** > **Edit Sort & Filter**. Designer displays the Edit Sort and Filter dialog box. Switch to the **Filter** tab.

   ![Edit Sort and Filter dialog box - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856836247/rpt_edit_srtfltr.gif)
3. Select the **Add Condition** button to add a condition line.
4. From the field drop-down list, select the field on which the filter is based.

   If you have not applied the [Customize Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets#Customize) feature to the dataset the data component uses, no fields are available in the field drop-down list. In this case, select the **Edit Display Name** button in the dialog box to enable the feature on the dataset first.
5. From the operator drop-down list, set the operator with which to compose the filter expression.
6. In the value combo box, type the value of how to filter the field or select the value from the drop-down list.
   You can apply an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0).
7. Repeat steps 3 to 6 to add more condition lines and define the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".

   To group some condition lines, select them and select the **Group** button, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select the **Up** or **Down** button; to delete a condition line, select it and select the **Delete** button.
8. Select **OK** to save the condition.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) The predefined sort and filter conditions also affects the preview result in Designer, and the result produced from being run in other formats besides Page Report Result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101341-Previewing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101241-Filtering-Reports)
