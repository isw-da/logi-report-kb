---
title: "To Chart Dialog Box Properties"
id: 5741437074583
section: "Dialog Boxes in Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741437074583-To-Chart-Dialog-Box-Properties
updated_at: 2022-10-31T17:17:49Z
---

# To Chart Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741452114711-Tabular-Properties-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741460447511-To-Crosstab-Dialog-Box-Properties)

# To Chart Dialog Box Properties

This topic describes how you can use the To Chart dialog box to specify settings for converting a crosstab into a chart excluding the organization chart. The dialog box varies with different chart types: [common chart types](#Common), [organization chart](#Org), and [heat map](#Map).

Server displays the dialog box when you right-click a crosstab and then select **To Chart** on the shortcut menu or select Menu > Edit > To Chart.

**OK**

Select to convert the crosstab into a chart and close the dialog box.

**Cancel**

Select to close the dialog box without conversion.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/9905613168791/btn_help.gif)**Help button**

Select to view information about the dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905575212823/btn_close.gif)**Close button**

Select to close the dialog box without conversion.

## For Common Chart Types

![To Chart dialog - Common](https://devnet.logianalytics.com/hc/article_attachments/9905617995799/tochart.gif)

**Title**

Specify a title for the chart.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/9905615721239/btn_wbrpt_font.gif)**Font button**

Specify the font properties of the chart title.

After you select the button, Server displays the following dialog box for you to edit the font properties:

![](https://devnet.logianalytics.com/hc/article_attachments/9905716575255/fontprpty.gif "Font Properties")

* **Font**  
  Select the font face of the title.
* **Font Style**   
  Select the font style of the title: regular, bold, italic, or bold italic.
* **Size**  
  Specify the font size of the title.
* **Align**  
  Specify the position of the title to be left, right, center, or justify.
* **Font Color**  
  Specify the font color of the title.

  To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428592023-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.
* **Background Color**  
  Specify the background color of the title.
* **OK**  
  Select to apply any changes you made here and close the dialog box.
* **Cancel**  
  Select to close the dialog box without saving any changes.

**Resources**

Server displays all the view elements that the crosstab is using.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif) **Sort button**

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

The order can be one of the following:

* **Predefined Order**  
  Select if you want to sort the resources in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the resources in alphabetical order. Logi Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**

Select to launch the search bar to search for view elements.

See the following properties in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/9905619099031/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **![Close button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)****Close button**  
  Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/9905631409303/btn_srchtlbr_adv.gif)**More Options button**  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/9905631449623/btn_srchtlbr_prv.gif) **Previous button**  
  Select to go to the previous matched text when you have selected **Highlight All**.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/9905619191959/btn_srchtlbr_nxt.gif)**Next button**  
   Select to go to the next matched text when you have selected **Highlight All**.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif)**Add button**

Select to add the selected group or aggregation object to display in the chart.

**Value box**

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box lists the values you want to display in the chart.

* **Primary Axis**  
   Select a chart type to the primary axis.
* **Secondary Axis**  
   Select a chart type for the secondary axis. Active only when you select **Secondary Axis**. Not available to gauge charts.
* **X-Axis**  
   Server lists the value that you want to show on the X axis of the bubble chart.
* **Y-Axis**  
   Server lists the value that you want to show on the Y axis of the bubble chart.
* **Size**  
   Server lists the value that you want to show as the bubble size.

![Add Combo Chart](https://devnet.logianalytics.com/hc/article_attachments/9905632658071/btn_wbrpt_adcmbtyp.gif)**Add Combo Chart button**

Select to add a combo chart to the Primary Axis or Secondary Axis. Not available to gauge charts.

![Edit Additional Value](https://devnet.logianalytics.com/hc/article_attachments/9905619243799/btn_wbrpt_edit.gif)**Edit button**

Select to open the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741444402455-Edit-Additional-Value-Dialog-Box-Properties) to edit the selected additional value.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif)**Add Axis button**

Select to add a new pair of Y Axis and Radius for the bubble chart.

**Secondary Axis**

Specify whether to show the secondary axis in the chart. Not available to gauge chart.

**Category box**

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) that will display on the category axis of the chart.

**Series box**

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) that will display on the series axis of the chart.

![Top N button](https://devnet.logianalytics.com/hc/article_attachments/9905632725527/btn_wbrpt_topn.gif)**Top N button**

Select to open the [Category Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741434586391-Category-Options-Dialog-Box-Properties) or [Series Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459816727-Series-Options-Dialog-Box-Properties) to define the sort order of the category or series values and specify the number of the category or series values that will display in the chart.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**

Select to remove the selected resource.

## For Organization Chart

The chart type is Org.

![To Chart dialog - Organization](https://devnet.logianalytics.com/hc/article_attachments/9905716684311/tochart_org.gif)

**Chart Title**

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/9905615721239/btn_wbrpt_font.gif)

Specify the [font properties](#Font) of the chart title.

**Resources**

Server displays the resources that you can add to the chart.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif)**Sort button**

Select an [order](#Order) for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**

Select to launch the [search bar](#Search) to search for view elements.

**Primary Axis**

* **Chart Type**  
   Select **Org** from the chart type drop-down list.
* **Node**  
   Add a field from the Resources box which identifies the entity by selecting both the field and Node and then selecting the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif).
* **Parent**  
   Add a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif).
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**Remove button**   
   Select to remove the selected child node or parent field.

**Properties**

The Properties box presents a node model of the org chart. You can insert data fields, labels, and images into the node as the information about the entity in the org chart, using ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif). By default, Server places all added objects at the left top of the node, and you need to adjust their positions and sizes in the node. You can also resize the node.

To remove an object from the node, select it, and then select the **Remove** button ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif).

## For Heat Map

![To Chart dialog - Heat Map](https://devnet.logianalytics.com/hc/article_attachments/9905716712471/tochart_htmp.gif)

**Title**

**Chart Title**

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/9905615721239/btn_wbrpt_font.gif)**Font button**

Specify the [font properties](#Font) of the chart title.

**Resources**

Server displays the resources that you can add to the chart.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905577646231/btn_sort.gif)**Sort button**

Select an [order](#Order) for sorting the resources in the business view. The order applies to all the resource trees where you see the business view in Web Report Studio.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/9905577660311/btn_srch.gif)**Search button**

Select to launch the [search bar](#Search) to search for view elements.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif)**Add button**

Select to add the selected field into the Area or Property box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/9905574572823/btn_rmvitem.gif)**Remove button**

Select to remove the selected field from the Area or Property box.

**Chart type drop-down list**

Select **Heat Map** as the chart type.

**Area**

Server lists the fields you add to group the data to different areas. There should be at least one group. When there are multiple groups, Server defines their levels by their positions from top down. The group at the top is of the highest level and the bottom the lowest.

* **Color by**  
   Select to color by a group. You can use 0 or more groups as the color-by fields.
* **Label by**  
   Select to show the group name in the innermost rectangle.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif)**Move Up button**  
   Select to move the selected group field higher in the list.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)**Move Down button**  
   Select to move the selected group field lower in the list.
* ![Top N button](https://devnet.logianalytics.com/hc/article_attachments/9905632725527/btn_wbrpt_topn.gif)**Top N button**  
   Select to open the [Group Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741459041175-Group-Options-Dialog-Box-Properties) to define the sort order of the group values and specify the number of the group values you want to display in the chart.

**Property**

Server lists the summary fields you add as size-by/color-by or you want to display in the innermost rectangle.

* **Size by**  
   Select to size by one summary or none.
* **Color by**  
   Select to color by one summary or none.
* **Label by**  
   Select to show a summary in the innermost rectangle.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741452114711-Tabular-Properties-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741460447511-To-Crosstab-Dialog-Box-Properties)
