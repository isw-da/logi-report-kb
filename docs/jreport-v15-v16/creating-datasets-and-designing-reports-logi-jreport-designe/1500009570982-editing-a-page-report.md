---
title: "Editing a Page Report"
id: 1500009570982
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report
updated_at: 2021-07-24T05:53:47Z
---

# Editing a Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571062-Creating-Report-Tabs-in-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page)

# Editing a Page Report

After a page report is built, you can make further modifications to it, in order to make it better satisfy your requirements. In Logi JReport, to edit a page report is actually to edit the components in its report tabs. This topic only lists the basic operations used for editing a page report. For more details, you can refer to the specific section of each component in the chapter [Components](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports).

**Note:** The other way to edit a page report is by changing its properties in the Report Inspector. For detailed property descriptions, see [Properties in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500009590661-Report-Object-Properties).

Below is a list of the sections covered in this topic:

> * [Inserting Other Components into a Page Report](#Insert)
> * [Duplicating the Components](#Duplicate)
> * [Resizing the Components](#Resize)
> * [Editing Component Properties](#Property)
> * [Changing the Position Property of Components](#Change)
> * [Showing Components in a TOC Tree](#TOC)
> * [Deleting Components from a Page Report](#Delete)

## Inserting Other Components into a Page Report

After the initial design work of a page report, you are also free to insert more components into it. To insert a component, you can either use the menu command or the Components panel.

## Duplicating the Components

You can duplicate any component in a page report without creating it the second time.

1. Select the component which you want to duplicate.
2. Right-click the component and then select **Copy** from the shortcut menu (or select the corresponding menu command).
3. In the required position, right-click your mouse, and then select **Paste**.

## Resizing the Components

To resize a component in a page report, follow the steps below:

1. Select the component with the size you want to change, and the sizing handles will then appear along the four boundaries of the component.
2. Drag a sizing handle to resize the component to the required size.
3. Repeat the steps to resize other components.

## Editing Component Properties

Each component has a set of properties that can be used to customize the appearance and behavior of the component.

To edit the properties of a component, select the component in the report or from the report structure tree in the Report Inspector, then in the Properties sheet modify the property values as required. See [Properties in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500009590661-Report-Object-Properties) for detailed information about the properties.

After editing the properties you can [save them as a CSS style](https://devnet.logianalytics.com/hc/en-us/articles/1500009571302-Creating-a-CSS-Style) for future use if needed.

## Changing the Position Property of Components

Report templates in Logi JReport use a flow layout model. That is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is to be part of the flow, or separate from it. Besides the report body, [tabular cells](https://devnet.logianalytics.com/hc/en-us/articles/1500009563742-Tabulars), [text boxes](https://devnet.logianalytics.com/hc/en-us/articles/1500009563762-Text-Boxes) and [KPI components](https://devnet.logianalytics.com/hc/en-us/articles/1500009583981-KPI-Components) themselves in Logi JReport can also act as flow layout containers.

In a flow layout model, objects are positioned relative to one another or absolutely. The Position property controls the position of components in the flow layout container. Components placed in other areas, such as table cells or banded panels are not affected by the Position property.

The Position property can be one of the following values:

* **Static**  
   The component will be positioned at the location in which it is inserted. The X and Y coordinate properties are disabled. The position of the component cannot be moved other than by having its insertion point moved. This can happen when the text flow preceding the insertion point expands.
* **Relative**  
   The component will be positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y coordinate property values. This value is not available for some kinds of components.
* **Absolute**  
   The component will be located at the position specified by dragging and dropping or by setting its X and Y coordinate property values. The component insertion point does not change, for instance it is not affected by having text inserted before it.

  When components in the same flow layout container have their Position property value set to Absolute and overlap, you can set the display order of the objects by right-clicking an object and selecting an item from the Move submenu, or selecting the objects and selecting the corresponding move button on the Format menu tab.

  + **![](https://devnet.logianalytics.com/hc/article_attachments/4404893797783/btn_mvbckwd.gif) Move Backward**  
     Moves the component one step towards the back.
  + **![](https://devnet.logianalytics.com/hc/article_attachments/4404893798039/btn_mv2bck.gif) Move to Back**  
     Moves the component to the back.
  + **![](https://devnet.logianalytics.com/hc/article_attachments/4404889281559/btn_mvfrwd.gif) Move Forward**  
     Moves the component one step closer to the front.
  + **![](https://devnet.logianalytics.com/hc/article_attachments/4404893798295/btn_mv2frnt.gif) Move to Front**  
     Moves the component to the front.

**To change the position property of a component**:

* In the design area, right-click the component and on the shortcut menu, select the required item from the Position submenu.
* In the design area, select the component, then select the **Format**/**Home** menu tab and select the required item from the Position drop-down list.
* In the Report Inspector, select the node which represents the component, then set its Position property value as required.

## Showing Components in a TOC Tree

Some components in a page report can be set up to show in a table of contents. Then when previewing the report in Logi JReport Format, viewing it in Page Report Studio, exporting it to PDF or HTML format, TOC Browser can be used to locate the corresponding component.

**To show a component in a TOC tree:**

1. Select the component node in the Report Inspector.
2. Set its TOC Anchor property to **true**.
3. Specify the display value for the anchor by setting the Anchor Display Value property.

Logi JReport also allows you to specify other [properties for a TOC tree](https://devnet.logianalytics.com/hc/en-us/articles/1500009591941-Properties-of-TOC-in-Page-Report), including its CSS style, colors and fonts. You can specify these properties by selecting the TOC node in the Report Inspector.

## Deleting Components from a Page Report

If you find any components contained in a page report are not required, you can use either of the following two ways to remove it from the report tab:

* In the Report Inspector, select the node which represents the component and press the **Delete** button on your keyboard.
* In the design area, right-click the component and select **Delete** from the shortcut menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571062-Creating-Report-Tabs-in-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571022-Designing-a-Report-Page)
