---
title: "Editing Reports"
id: 5735534157079
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports
updated_at: 2022-11-02T08:22:57Z
---

# Editing Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735555715607-Previewing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports)

# Editing Reports

You can modify a report at any time to make it better serve your requirements. In Designer, to edit a report is actually to edit the components in it. This topic introduces the general and common operations you can perform on the report components. For more information about working with different components, refer to the specific topic of each component in [Components](https://devnet.logianalytics.com/hc/en-us/articles/5735520464535-Working-with-Components-in-Reports).

This topic contains the following sections:

* [Inserting Components to a Report](#Insert)
* [Duplicating Components](#Duplicate)
* [Resizing Components](#Resize)
* [Deleting Components from a Report](#Delete)
* [Editing Component Properties](#Property)
* [Changing Component Position](#Change)
* [Applying Conditional Formatting in a Report](#Format)
* [Predefining Sort and Filter Conditions for Page Report Data Components](#Predefine)

## Inserting Components to a Report

After the initial design work of a report, you are also free to insert more components into it. To insert a component, you can either use the **Insert** ribbon or the **Components** panel.

## Duplicating Components

You can duplicate any component in a report without creating it the second time.

**To duplicate a component**

1. Select the component, then right-click the component and select **Copy** on the shortcut menu, or navigate to **Home** > **Copy**.
2. Select in the destination where you want to place the component.
3. Right-click the mouse and select **Paste** on the shortcut menu, or navigate to **Home** > **Paste**.

## Resizing Components

1. Select the component with the size you want to change. The sizing handles then appear along the four boundaries of the component.
2. Drag a sizing handle to resize the component to the required size.
3. Repeat the steps to resize other components.

## Deleting Components from a Report

If you find any components contained in a report are not required, you can use either of the following two methods to remove it:

* In the Report Inspector, select the node which represents the component and select **Delete** on the keyboard.
* In the design area, right-click the component and select **Delete** from the shortcut menu.

## Editing Component Properties

Each component has a set of properties that you can use to customize the appearance and behavior of the component.

**To edit the properties of a component**

1. Select the component in the report or from the report structure tree in the Report Inspector.
2. In the Properties sheet, modify the property values. See [Report Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735584998167-Report-Object-Properties) for more information about the properties.

After editing the properties, you can [save them as a CSS style](https://devnet.logianalytics.com/hc/en-us/articles/5735586532503-Working-with-CSS-Styles#Create) for future use.

## Changing Component Position

Report templates in Designer use a flow layout model, that is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is to be part of the flow, or separate from it. Besides the report body, [tabular cells](https://devnet.logianalytics.com/hc/en-us/articles/5735564433175-Working-with-Tabulars), [text boxes](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes), and [KPIs](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs) themselves can also act as flow layout containers.

In a flow layout container, Designer positions the components relative to one another or absolutely based on their Position property value, which can be one of the following:

* **Static**  
  Designer positions the component at the location where you insert it. The X and Y coordinate properties are disabled. You cannot move the component to another position other than by moving its insertion point. This can happen when the text flow preceding the insertion point expands.
* **Relative**  
  Designer positions the component at an offset to the position at which you insert it. The offset is determined by the X and Y coordinate property values. This value is not available for some types of components.
* **Absolute**  
  Designer locates the component at the position that you specify by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance, it is not affected when you insert text before it.
  The position of an object in a banded object can only be absolute.

  When you set the Position property for components in the same flow layout container to "Absolute" and the components overlap, you can specify the display order of the objects by right-clicking an object and selecting an option from the **Move** submenu, or selecting the objects and selecting the corresponding move button in the **Format** ribbon.

  + ![Move Backward button](https://devnet.logianalytics.com/hc/article_attachments/9898404800407/btn_mvbckwd.gif)**Move Backward**  
    Select to move the component one step towards the back.
  + ![Move to Back button](https://devnet.logianalytics.com/hc/article_attachments/9898404813591/btn_mv2bck.gif)**Move to Back**  
    Select to move the component to the back.
  + ![Move Forward button](https://devnet.logianalytics.com/hc/article_attachments/9898404829847/btn_mvfrwd.gif)**Move Forward**  
    Select to move the component one step closer to the front.
  + ![Move to Front button](https://devnet.logianalytics.com/hc/article_attachments/9898421563159/btn_mv2frnt.gif)**Move to Front**  
    Select to move the component to the front.

You can change the Position property of a component using these methods:

* In the design area, right-click the component and on the shortcut menu, select a command from the **Position** submenu.
* In the design area, select the component, then select the **Format**/**Home** ribbon and select an option from the **Position** drop-down list.
* In the Report Inspector, select the node that represents the component, then set its **Position** property.

In the same flow layout container, when components overlap, they follow the rule that the component inserted later covers the one earlier and the component with absolute position covers the one with static position. When different types of objects in a chart overlap, the covering order is: chart legend > chart label > chart paper or chart data label.

## Applying Conditional Formatting in a Report

Conditional formatting enables you to highlight the values that are important in a report or users might need to act on at runtime.

You can apply conditional formatting to the following data fields in a report: DBField, Formula Field, Parameter Field, and Summary Field. For more information, see [Adding Conditional Formatting to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields#Format).

You can also apply conditional formatting to [areas in shape maps](https://devnet.logianalytics.com/hc/en-us/articles/5735521118231-Using-Shape-Maps#Format) and [markers in geographic maps](https://devnet.logianalytics.com/hc/en-us/articles/5735564357015-Modifying-Geographic-Maps#Format).

In a chart, you can add [conditional color fills](https://devnet.logianalytics.com/hc/en-us/articles/5735511924119-Applying-Conditional-Color-Fills-to-Charts) to apply different color patterns to its data markers based on different value ranges.

## Predefining Sort and Filter Conditions for Page Report Data Components

For query-based page reports, you can predefine sort and filter conditions on the charts, tables, crosstabs, and banded objects in them, so that after you publish the page reports to Server and run them in Page Report Studio, these data components display data in the order you prefer, and narrow down to show only the data you desire.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The predefined sort and filter conditions in a page report are based on the result set of all the other sort and filter conditions applied to the report. They also affects the preview result in Designer, and the result produced from being run in other formats besides Page Report Result.

**To predefine sort conditions in a page report**

1. Select a chart, table, crosstab, or banded object in the report.
2. Navigate to **Report** > **Edit Sort & Filter**. Designer displays the [Edit Sort and Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508795927-Edit-Sort-and-Filter-Dialog-Box), and the Sort tab is active by default.

   ![Edit Sort and Filter dialog box - Sort](https://devnet.logianalytics.com/hc/article_attachments/9898474478871/edtsrtfltr_srt.gif)
3. The **Fields** box lists all the data fields in the dataset the data component uses. Select the fields by which to sort the data from the box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add them to the **Sort By** box.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If you have not applied the [Customize Display Name](https://devnet.logianalytics.com/hc/en-us/articles/5735569625367-Customizing-Field-Display-Names-for-Datasets-in-a-Report) feature to the dataset the data component uses, no fields are available in the Fields box. In this case, select **Edit Display Name** to enable the feature on the dataset first.
4. To modify the sort direction for a field, select ![Sort Ascending button](https://devnet.logianalytics.com/hc/article_attachments/9898457444503/btn_srtasnd.gif) (ascending) or ![Sort Descending button](https://devnet.logianalytics.com/hc/article_attachments/9898474508567/btn_srtdsnd.gif) (descending) from the drop-down list in the **Direction** column.
5. To change the sort priority of the fields, select a field in the **Sort By** box, and then select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to move it higher or lower.
6. Select **OK** to accept the settings.

**To predefine filter conditions in a page report**

1. Select a chart, table, crosstab, or banded object in the report.
2. Navigate to **Report** > **Edit Sort & Filter**. Designer displays the Edit Sort and Filter dialog box. Switch to the **Filter** tab.

   ![Edit Sort and Filter dialog box - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898474527255/rpt_edit_srtfltr.gif)
3. Select **Add Condition** to add a condition line.
4. From the field drop-down list, select the field on which the filter condition is based.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If you have not applied the [Customize Display Name](https://devnet.logianalytics.com/hc/en-us/articles/5735569625367-Customizing-Field-Display-Names-for-Datasets-in-a-Report) feature to the dataset the data component uses, no fields are available in the field drop-down list. In this case, select **Edit Display Name** to enable the feature on the dataset first.
5. From the operator drop-down list, choose the operator with which to compose the filter condition.
6. In the value combo box, type the value of how to filter the field or select the value from the drop-down list. When the condition is based on a String field, you can apply an empty string as the value, by simply leaving the text box blank (value length=0).
7. Repeat the preceding steps to define more condition lines and specify the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".
   * To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together).
   * To take out any condition or group from a group, select it and select **Ungroup**.
   * To adjust the priority of the condition lines, select it and select **Up** or **Down**.
   * To delete a condition line, select it and select **Delete**.
8. Select **OK** to save the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735555715607-Previewing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports)
