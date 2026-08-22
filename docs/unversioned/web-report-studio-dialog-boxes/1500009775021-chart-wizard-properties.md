---
title: "Chart Wizard Properties"
id: 1500009775021
section: "Web Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009775021-Chart-Wizard-Properties
updated_at: 2021-07-24T00:48:33Z
---

# Chart Wizard Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775001-Chart-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775061-Color-List-Dialog-Box-Properties)

# Chart Wizard Properties

This topic describes how you can use Chart Wizard to edit a chart. Chart Wizard varies with different chart types: [common chart types](#Common), [organization chart](#Org), [heat map](#Map), and [KPI chart](#KPI).

Server displays the wizard when you do one of the following:

* Select a chart, then select Menu > Edit > Wizard.
* Select a chart, then select the Chart Wizard button ![Chart Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4404885314711/btn_wbrpt_wizard.gif) on the visualization toolbar.
* Right-click the icon ![Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404880145943/btn_pgrpt_drag.gif) of a chart, then select Chart Wizard from the shortcut menu.
* Right-click any part of a chart other than the legend and label, or right-click the blank area in a KPI chart, then select Chart Wizard from the shortcut menu.

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404880314903/btn_help.gif)

Select to view information about Chart Wizard.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404885431447/btn_close.gif)

Select to close the dialog box without saving any changes.

## Chart Wizard Properties for Common Chart Types

![Chart Wizard - common](https://devnet.logianalytics.com/hc/article_attachments/4404885325079/chtwzd.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif)

Specifies the font properties of the chart title.

After you select the button, Server displays the following dialog box for you to edit the font properties:

![](https://devnet.logianalytics.com/hc/article_attachments/4404880315543/fontprpty.gif "Font Properties")

* **Font**  
  Specifies the font face of the title.
* **Font Style**   
  Specifies the font style of the title. It can be one of the following: regular, bold, italic, and bold italic.
* **Size**  
  Specifies the font size of the title.
* **Align**  
  Specifies the position of the title to be left, right, center, or justify.
* **Font Color**  
  Specifies the font color of the title.
* **Background Color**  
  Specifies the background color of the title.

  To specify a color, select the color image to select a color from the color palette, or select **More Colors** in the color palette to select a color using the [Color Picker](../dlg_wbrpt_colorpkr.htm) dialog box.
* **OK**  
  Accepts the font settings and closes the dialog box.
* **Cancel**  
  Cancels editing the font properties and closes the dialog box.

**Data Source**

Displays the business view used by the chart.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009747922-Query-Filter-Dialog-Box-Properties) dialog box to specify the filter which you want to apply to the selected business view.

**Resources**

Displays the resources that can be added to the chart.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the view elements in the specified order from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

The order can be one of the following:

* **Predefined Order**  
  Select if you want to sort the view elements in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the view elements by resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the view elements in alphabetical order. Logi Report sorts the elements that are not in any category first, and then the categories. It also sorts the elements in each category alphabetically.

![Quick Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the search bar to search for view elements.

See the following options in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4404880162071/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **X**  
  Select to close the search bar or clear the typed text.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885330071/btn_srchtlbr_adv.gif)  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162711/btn_srchtlbr_prv.gif)  
  When you selected **Highlight All**, you can use this button to go to the previous matched text.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4404880162967/btn_srchtlbr_nxt.gif)  
   When you selected **Highlight All**, you can use this button to go to the next matched text.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected resource to be displayed in the chart.

**Value box**

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects.

* **Primary Axis**  
   Adds a chart type to the primary axis.
* **Secondary Axis**  
   Adds a chart type to the secondary axis. Active only when the option Secondary Axis is selected. Not available to gauge chart.
* **X-Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y-Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Size**  
   Lists the value you want to show as the bubble size.

![Add Combo Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404880175127/btn_wbrpt_adcmbtyp.gif)

Adds a combo chart to the Primary Axis or Secondary Axis. Not available to gauge chart.

![Edit Additional Value button](https://devnet.logianalytics.com/hc/article_attachments/4404880163863/btn_wbrpt_edit.gif)

Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009746922-Edit-Additional-Value-Dialog-Box-Properties) dialog box to edit the selected additional value.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)

Moves the selected view element one level up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)

Moves the selected view element one level down.

![Add Y Axis button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)

Adds a new pair of Y Axis and Radius for the bubble chart.

**Secondary Axis**

Specifies whether to show the secondary axis in the chart. Not available to gauge chart.

**Category box**

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object ![Group Object icon](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) that will be displayed on the category axis of the chart.

For a real time chart, if no object is specified on the category axis, Use System Refresh Time will be automatically displayed in the Category text box, namely, the time at which the chart refreshes itself will be used as the category value.

**Series box**

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object ![Group Object icon](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) that will be displayed on the series axis of the chart. Not available to real time chart.

![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880176279/btn_wbrpt_topn.gif)

Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009746902-Category-Options-Dialog-Box-Properties) dialog box or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009747962-Series-Options-Dialog-Box-Properties) dialog box to define the sort order of the category or series values and specify the number of the category or series values that will be displayed in the chart.

**Motion Bar for Playable Chart**

Lists the group object ![Group Object icon](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you want to use as the motion field. A motion field can only be of Integer, Date or Time data type. Available to single bar, bench, and bubble chart types only.

* **Special Function**  
   Available only when the motion field is of Date data type. Select it to define the special function.
  + **Field**  
     Displays on which field the special function will be applied.
  + **Function**  
     Specifies the special function to the field.
  + **OK**  
     Accepts the special function settings and leaves the dialog box.
  + **Cancel**  
     Cancels the special function settings and leaves the dialog box.

**Real Time**

Specifies to run the chart in real time mode, which means it will be updated automatically using real time data. Available to single bar, bench, line, and area chart types only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of records that will be kept for the real time data in the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009776581-Unique-Key-Dialog-Box-Properties) dialog box to configure a unique key for the real time chart.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected resource.

## Chart Wizard Properties for Organization Chart

![Chart Wizard - organization chart](https://devnet.logianalytics.com/hc/article_attachments/4404880402071/chtwzd_org.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif)

Specifies the [font properties](#Font) of the chart title.

**Data Source**

Displays the business view that has been used in the chart.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009747922-Query-Filter-Dialog-Box-Properties) dialog box to specify the filter you want to apply to the selected business view.

**Resources**

Displays the resources that can be added to the chart.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Quick Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the [search bar](#Search) to search for view elements.

**Value box**

* **Primary Axis**  
   Select Org from the chart type drop-down menu.
* **Node**  
   Adds a field from the Resources box which identifies the entity by selecting both the field and Child and then selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif).
* **Parent**  
   Adds a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif).
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
   Removes the selected child node or parent field.

**Properties**

The Properties box presents a node model of the org chart. Data fields, labels and images can be inserted into the node as the information about the entity in the org chart, using ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif). By default, all added objects are placed at the left top of the node, you need to adjust their positions and sizes in the node. You can also resize the node.

To remove an object from the node, select it and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif).

## Chart Wizard Properties for Heat Map

![Chart Wizard - heat map](https://devnet.logianalytics.com/hc/article_attachments/4404885493527/chtwzd_htmp.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif)

Specifies the [font properties](#Font) of the chart title.

**Data Source**

Displays the business view that has been used in the chart.

**Filter**

Opens the [Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009747922-Query-Filter-Dialog-Box-Properties) dialog box to specify the filter you want to apply to the selected business view.

**Resources**

Displays the resources that can be added to the chart.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Quick Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the [search bar](#Search) to search for view elements.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected field into the Area or Property box.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif)

Removes the selected field from the Area or Property box.

**Chart type drop-down list**

Displays Heat Map as the selected chart type.

**Area**

Lists the fields used to group the data to different areas. There should be at least one group. When there are multiple groups, their levels are defined by their positions from top down. The group at the top is of the highest level and the bottom the lowest.

* **Color by**  
   Specifies whether to color by a group. 0-n groups can be used as the color-by fields.
* **Label by**  
   Specifies whether to show the group name in the innermost rectangle.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)  
   Moves the selected group field one level up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)  
   Moves the selected group field one level down.
* ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880176279/btn_wbrpt_topn.gif)  
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009775881-Group-Options-Dialog-Box-Properties) dialog box to define the sort order of the group values and specify the number of the group values that will be displayed in the chart.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
   Removes the selected group field.

**Property**

Lists the summary fields used as size-by/color-by or displayed in the innermost rectangle.

* **Size by**  
   Specifies to size by one summary or none.
* **Color by**  
   Specifies to color by one summary or none.
* **Label by**  
   Specifies whether to show a summary in the innermost rectangle.

## Chart Wizard Properties for KPI Chart

![Chart Wizard - KPI](https://devnet.logianalytics.com/hc/article_attachments/4404880402327/chtwzd_kpi.gif)

**Chart Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif)

Specifies the [font properties](#Font) of the chart title.

**Data Source**

Displays the business view used by the chart.

**Resources**

Displays the resources that can be added to the chart.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif)

Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Quick Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif)

Launches the [search bar](#Search) to search for view elements.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif)

Adds the selected resource to be displayed in the chart.

**Value box**

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to show in the chart. For a real time chart, the values you add must be of Numeric type and cannot be aggregation objects.

* **Primary Axis**  
   Adds a chart type to the primary axis.
* **Secondary Axis**  
   Adds a chart type to the secondary axis. Active only when the option Secondary Axis is selected.

![Add Combo Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404880175127/btn_wbrpt_adcmbtyp.gif)

Adds a combo chart to the Primary Axis or Secondary Axis.

![Edit Additional Value button](https://devnet.logianalytics.com/hc/article_attachments/4404880163863/btn_wbrpt_edit.gif)

Opens the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009746922-Edit-Additional-Value-Dialog-Box-Properties) dialog box to edit the selected additional value.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)

Moves the selected view element one level up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)

Moves the selected view element one level down.

**Secondary Axis**

Specifies whether to show the secondary axis in the chart.

**Category box**

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object ![Group Object icon](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) that will be displayed on the category axis of the chart.

For a real time chart, if no object is specified on the category axis, Use System Refresh Time will be automatically displayed in the Category text box, namely, the time at which the chart refreshes itself will be used as the category value.

**Series box**

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object ![Group Object icon](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) that will be displayed on the series axis of the chart. Not available to real time chart.

![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880176279/btn_wbrpt_topn.gif)

Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009746902-Category-Options-Dialog-Box-Properties) dialog box or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009747962-Series-Options-Dialog-Box-Properties) dialog box to define the sort order of the category or series values and specify the number of the category or series values that will be displayed in the chart.

**Motion Bar for Playable Chart**

Lists the group object ![Group Object icon](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) you want to use as the motion field. A motion field can only be of Integer, Date or Time data type. Available to single bar and bench chart types only.

* **Special Function**  
   Available only when the motion field is of Date data type. Select it to define the special function.
  + **Field**  
     Displays on which field the special function will be applied.
  + **Function**  
     Specifies the special function to the field.
  + **OK**  
     Accepts the special function settings and leaves the dialog box.
  + **Cancel**  
     Cancels the special function settings and leaves the dialog box.

**Real Time**

Specifies to run the chart in real time mode, which means it will be updated automatically using real time data. Available to single bar, bench, line, and area chart types only.

* **Use System Time for Category**  
   Specifies to use the time at which the chart refreshes itself as the category value.
* **Refresh Interval**  
   Specifies the time interval at which the chart will get data and refresh itself automatically.
* **Show Most Recent N Points**  
   Specifies the number of records that will be kept for the real time data in the chart.
* **Incremental Fetch**  
   Opens the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009776581-Unique-Key-Dialog-Box-Properties) dialog box to configure a unique key for the real time chart.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected resource.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009775001-Chart-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009775061-Color-List-Dialog-Box-Properties)
