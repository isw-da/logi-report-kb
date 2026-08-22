---
title: "Editing Reports"
id: 4405661931671
section: "Creating Datasets and Designing Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports
updated_at: 2022-01-27T20:35:08Z
---

# Editing Reports

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664696343-Previewing-Reports)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664691735-Filtering-Reports)

# Editing Reports

You can modify a report at any time to make it better serve your requirements. In Designer, to edit a report is actually to edit the components in it. This topic introduces the general and common operations you can perform on the report components. For more information about working with different components, refer to the specific topic of each component in [Components](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports).

This topic contains the following sections:

* [Inserting Other Components into a Report](#Insert)
* [Duplicating Components](#Duplicate)
* [Resizing Components](#Resize)
* [Deleting Components from a Report](#Delete)
* [Editing Component Properties](#Property)
* [Changing Component Position](#Change)
* ![This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.](https://devnet.logianalytics.com/hc/article_attachments/4420542050071/___newv18.3.jpg "New for version 18.3.")[Adding Table of Contents in a Report](#TOC)
* [Applying Conditional Formatting in a Report](#Format)
* [Predefining Sort and Filter Conditions for Page Report Data Components](#Predefine)

## Inserting Other Components into a Report

After the initial design work of a report, you are also free to insert more components into it. To insert a component, you can either use the **Insert** menu tab or the **Components** panel.

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

To edit the properties of a component, select the component in the report or from the report structure tree in the Report Inspector, then in the Properties sheet, modify its property values. See [Report Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties) for detailed information about the properties.

After editing the properties, you can [save them as a CSS style](https://devnet.logianalytics.com/hc/en-us/articles/4405661944471-Working-with-CSS-Styles#Create) for future use.

## Changing Component Position

Report templates in Designer use a flow layout model, that is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is to be part of the flow, or separate from it. Besides the report body, [tabular cells](https://devnet.logianalytics.com/hc/en-us/articles/4405661404695-Working-with-Tabulars), [text boxes](https://devnet.logianalytics.com/hc/en-us/articles/4405664406679-Working-with-Text-Boxes), and [KPIs](https://devnet.logianalytics.com/hc/en-us/articles/4405661382551-Working-with-KPIs) themselves can also act as flow layout containers.

In a flow layout container, Designer positions the components relative to one another or absolutely based on their Position property value, which can be one of the following:

* **Static**  
  Designer positions the component at the location where you insert it. The X and Y coordinate properties are disabled. You cannot move the component to another position other than by moving its insertion point. This can happen when the text flow preceding the insertion point expands.
* **Relative**  
  Designer positions the component at an offset to the position at which you insert it. The offset is determined by the X and Y coordinate property values. This value is not available for some types of components.
* **Absolute**  
  Designer locates the component at the position that you specify by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance, it is not affected when you insert text before it.
  The position of an object in a banded object can only be absolute.

  If you set the Position property value for components in the same flow layout container to Absolute and the components overlap, you can specify the display order of the objects by right-clicking an object and selecting an item from the **Move** submenu, or selecting the objects and selecting the corresponding move button on the **Format** menu tab.

  + ![Move Backward button](https://devnet.logianalytics.com/hc/article_attachments/4420550815255/btn_mvbckwd.gif)**Move Backward**  
    Moves the component one step towards the back.
  + ![Move to Back button](https://devnet.logianalytics.com/hc/article_attachments/4420556081175/btn_mv2bck.gif)**Move to Back**  
    Moves the component to the back.
  + ![Move Forward button](https://devnet.logianalytics.com/hc/article_attachments/4420542059927/btn_mvfrwd.gif)**Move Forward**  
    Moves the component one step closer to the front.
  + ![Move to Front button](https://devnet.logianalytics.com/hc/article_attachments/4420556081431/btn_mv2frnt.gif)**Move to Front**  
    Moves the component to the front.

You can change the Position property of a component using these methods:

* In the design area, right-click the component and on the shortcut menu, select a command from the **Position** submenu.
* In the design area, select the component, then select the **Format**/**Home** menu tab and select an option from the **Position** drop-down list.
* In the Report Inspector, select the node which represents the component, then set its **Position** property.

In the same flow layout container, when components overlap, they follow the rule that the component inserted later covers the one earlier and the component with absolute position covers the one with static position. If different types of objects in a chart overlap, the covering order is: chart legend > chart label > chart paper or chart data label.

## This image notes any new content for version 18.3 of the product. For more information please see the Release Notes or Enhancements topics.Adding Table of Contents in a Report

You can add a Table of Contents in a page report or web report, to enable easy navigation of the report contents when previewing the report in Designer and in the report outputs.

To insert a TOC in a report

1. Open the report, and for a page report, switch to the page report tab.
2. Navigate to **Insert** > **TOC Page**. Designer adds a Table of Contents at the beginning of the report, and automatically creates a [TOC page panel](https://devnet.logianalytics.com/hc/en-us/articles/4405664695447-Designing-the-Report-Pages#TOC) to position the TOC.

   ![Insert TOC in Report](https://devnet.logianalytics.com/hc/article_attachments/4420556100887/rpt_edit_toc1.gif)
3. In the Report Inspector, specify the **TOC Anchor** and **Anchor Display Value** properties of the objects in the report that you want to add in the TOC. Basically, you can include data components, tabulars, text boxes, group panels in banded object, and DBFields, formula fields, parameter fields, images, and labels inside banded objects in the TOC.
4. Edit [properties of the TOC](https://devnet.logianalytics.com/hc/en-us/articles/4420402744215-TOC-Container-Properties) to specify the font style, leader character, indentation, and line spacing for entries in the TOC.
5. You can insert the **TOC Page Number** special field in the header or footer of the TOC page panel to display page numbers for the Table of Contents. Logi Report Engine calculates the TOC page numbers differently than the report pages.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) By default, Designer does not show the header or footer of the TOC page panel. To insert objects in them, you need to first edit their **Invisible** property to "true"; or you can select in the TOC page and navigate to **View** > **Page Header**/**Page Footer**.
6. Select the **View** tab to preview the report and select **Show TOC Page** to display the Table of Contents.

   ![Preview Report with TOC](https://devnet.logianalytics.com/hc/article_attachments/4420556101271/rpt_edit_toc2.gif)
7. Select an item in the TOC and Designer opens the page containing the corresponding object.

After adding TOC in a report, when you export or print the report in Designer or at runtime, and when you run the report in advanced mode or schedule to run it in formats except Page Report for a page report or Web Report for a web report, you can also use the TOC in the report output to easily locate the content you need to focus on.

In addition to the Table of Contents generated by inserting the TOC Page object, Designer also provides the [TOC object](https://devnet.logianalytics.com/hc/en-us/articles/4405664678167-TOC-Properties) for each page report tab and web report in the Report Inspector. This TOC object corresponds to the TOC tree of the report. Once you set the TOC Anchor property of an object to "true", you also include the object in the TOC tree. Then, when you export the report to [HTML](https://devnet.logianalytics.com/hc/en-us/articles/4405664596375--Exporting-to-HTML) and [PDF](https://devnet.logianalytics.com/hc/en-us/articles/4405661756567-Exporting-to-PDF) in Designer, you can select the TOC option to enable displaying the TOC tree in the Table of Contents panel of the PDF and HTML browsers; at runtime, you can view the TOC tree in the TOC Browser of Page Report Studio when running a page report.

## Applying Conditional Formatting in a Report

Conditional formatting enables you to highlight the values that are important in a report or users might need to act on at runtime.

You can apply conditional formatting to the following data fields in a report: DBField, Formula Field, Parameter Field, and Summary Field. For more information, see [Adding Conditional Formatting to DBFields](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields#Format).

You can also apply conditional formatting to [areas in shape maps](https://devnet.logianalytics.com/hc/en-us/articles/4405664397975-Using-Shape-Maps#Format) and [markers in geographic maps](https://devnet.logianalytics.com/hc/en-us/articles/4405661389335-Modifying-Geographic-Maps#Format).

In a chart, you can add [conditional color fills](https://devnet.logianalytics.com/hc/en-us/articles/4405664369943-Applying-Conditional-Color-Fills-to-Charts) to apply different color patterns to its data markers based on different value ranges.

## Predefining Sort and Filter Conditions for Page Report Data Components

For page reports using query resources, you can predefine sort and filter conditions on the charts, tables, crosstabs, and banded objects in them, so that after you publish the page reports to Server and run them in Page Report Studio, the specified data components in the reports display data in the order you prefer, and narrow down to show only the data you desire.

The predefined sort and filter conditions in a page report are based on the result set of all the other sort and filter conditions applied to the report.

**To predefine sort conditions in a report**

1. Select a chart, table, crosstab, or banded object in the report.
2. Navigate to **Report** > **Edit Sort & Filter**. Designer displays the [Edit Sort and Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661529879-Edit-Sort-and-Filter-Dialog-Box), and the Sort tab is active by default.

   ![Edit Sort and Filter dialog box - Sort](https://devnet.logianalytics.com/hc/article_attachments/4420542077207/edtsrtfltr_srt.gif)
3. The **Fields** box lists all the data fields in the dataset the data component uses. Select the fields by which to sort the data from the box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420550823447/btn_addarrow.gif) to add them to the **Sort By** box.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you have not applied the [Customize Display Name](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets#Customize) feature to the dataset the data component uses, no fields are available in the Fields box. In this case, select **Edit Display Name** to enable the feature on the dataset first.
4. To modify the sort direction for a field, select ![Sort Ascending button](https://devnet.logianalytics.com/hc/article_attachments/4420550831383/btn_srtasnd.gif) (ascending) or ![Sort Descending button](https://devnet.logianalytics.com/hc/article_attachments/4420542077591/btn_srtdsnd.gif) (descending) from the drop-down list in the **Direction** column.
5. To change the sort priority of the fields, select a field in the **Sort By** box, and then select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420542078103/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420542078359/btn_mvdwn.gif) to move it higher or lower.
6. Select **OK** to accept the settings.

**To predefine filter conditions in a report**

1. Select a chart, table, crosstab, or banded object in the report.
2. Navigate to **Report** > **Edit Sort & Filter**. Designer displays the Edit Sort and Filter dialog box. Switch to the **Filter** tab.

   ![Edit Sort and Filter dialog box - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420556102551/rpt_edit_srtfltr.gif)
3. Select **Add Condition** to add a condition line.
4. From the field drop-down list, select the field on which the filter is based.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you have not applied the [Customize Display Name](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets#Customize) feature to the dataset the data component uses, no fields are available in the field drop-down list. In this case, select **Edit Display Name** to enable the feature on the dataset first.
5. From the operator drop-down list, set the operator with which to compose the filter expression.
6. In the value combo box, type the value of how to filter the field or select the value from the drop-down list. You can apply an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0).
7. Repeat steps 3 to 6 to add more condition lines and define the logic relationship between the condition lines: "And", "Or", "And Not", or "Or Not".

   To group some condition lines, select them and select **Group**, Designer then adds the selected condition lines in one group and applies them as one line of filter expression (you can also group conditions and groups together); to take out any condition or group from a group, select it and select **Ungroup**; to adjust the priority of the condition lines, select it and select **Up** or **Down**; to delete a condition line, select it and select **Delete**.
8. Select **OK** to save the condition.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) The predefined sort and filter conditions also affects the preview result in Designer, and the result produced from being run in other formats besides Page Report Result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664696343-Previewing-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664691735-Filtering-Reports)
