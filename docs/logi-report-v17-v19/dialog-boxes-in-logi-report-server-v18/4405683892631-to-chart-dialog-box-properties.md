---
title: "To Chart Dialog Box Properties"
id: 4405683892631
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683892631-To-Chart-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:31Z
---

# To Chart Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683891479-Tabular-Properties-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690613527-To-Crosstab-Dialog-Box-Properties)

# To Chart Dialog Box Properties

This topic describes how you can use the To Chart dialog box to specify settings for converting a crosstab into a chart excluding the organization chart. The dialog box varies with different chart types: [common chart types](#Common), [organization chart](#Org), and [heat map](#Map).

Server displays the dialog box when you right-click a crosstab and then select **To Chart** on the shortcut menu or select Menu > Edit > To Chart.

**OK**

Select **OK** to apply the settings.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4420447202071/btn_help.gif)

Select to view information about the To Chart dialog box.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420447202455/btn_close.gif)

Select to close the dialog box without saving any changes.

## For Common Chart Types

![To Chart dialog - Common](https://devnet.logianalytics.com/hc/article_attachments/4420461476119/tochart.gif)

**Title**

Specifies a title for the chart.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4420461453847/btn_wbrpt_font.gif)

Specifies the font properties of the chart title.

After you select the button, Server displays the following dialog box for you to edit the font properties:

![](https://devnet.logianalytics.com/hc/article_attachments/4420461616279/fontprpty.gif "Font Properties")

* **Font**  
  Select the font face of the title.
* **Font Style**   
  Select the font style of the title: regular, bold, italic, and bold italic.
* **Size**  
  Specify the font size of the title.
* **Align**  
  Specify the position of the title to be left, right, center, or justify.
* **Font Color**  
  Specify the font color of the title.

  To change the color, select the color indicator. Server displays the color palette. Select a color, or select **More Colors** to access the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683802391-Color-Picker-Dialog-Box-Properties) in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.
* **Background Color**  
  Specify the background color of the title.
* **OK**  
  Select to apply any changes you made here and exit the dialog box.
* **Cancel**  
  Select to close the dialog box without saving any changes.

**Resources**

Displays all the view elements used in the crosstab.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif) **Sort button**

Select an order for sorting the resources in the business view. The order applies to all the resource trees where you see the business view.

The order can be one of the following:

* **Predefined Order**  
  Select if you want to sort the resources in the order as in the Business View Editor of Designer.
* **Resource Types**  
  Select if you want to sort the resources by the resource type. Namely, category objects come first, then group objects, then aggregation objects, and at last detail objects.
* **Alphabetical Order**  
  Select if you want to sort the resources in alphabetical order. Logi Report sorts the resources that are not in any category first, and then the categories. It also sorts the resources in each category alphabetically.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)**Search button**

Select to launch the search bar to search for view elements.

See the following properties in the search bar:

![Quick Search Toolbar](https://devnet.logianalytics.com/hc/article_attachments/4420453420055/btn_srchtlbr.gif)

* **Text box**  
  Type the text you want to search in the text box. Server lists the values that contain the matched text.
* **![Close button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)****Close button**  
  Select to close the search bar.
* ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4420447073047/btn_srchtlbr_adv.gif)**More Options button**  
  Select the button and Server displays more search options.
  + **Highlight All**   
    Select if you want to highlight all matched text.
  + **Match Case**   
    Select if you want to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Select if you want to search for text that looks the same as the typed text.
* ![Previous Text](https://devnet.logianalytics.com/hc/article_attachments/4420453420311/btn_srchtlbr_prv.gif) **Previous button**  
  Select to go to the previous matched text when you have selected **Highlight All**.
* ![Next Text](https://devnet.logianalytics.com/hc/article_attachments/4420447073431/btn_srchtlbr_nxt.gif)**Next button**  
   Select to go to the next matched text when you have selected **Highlight All**.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)

Adds the selected group or aggregation object to be displayed in the chart.

**Category box**

The actual name of the box varies with different chart types, for example, it is X-Axis for a clustered bar chart. The box lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) that will be displayed on the category axis of the chart.

**Series box**

The actual name of the box varies with different chart types, for example, it is Clustering for a clustered bar chart. The box lists the group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4420461474455/btn_bvgrp.gif) that will be displayed on the series axis of the chart.

**Value box**

The actual name of the box varies with different chart types, for example, it is Bar Length for a clustered bar chart. The box specifies the types for chart and sets the values for the Primary Axis or Secondary Axis separately.

* **Primary Axis**  
   Adds a chart type to the primary axis.
* **Secondary Axis**  
   Adds a chart type to the secondary axis. Not available to gauge chart.
* **X-Axis**  
   Lists the value you want to show on the X axis of the bubble chart.
* **Y-Axis**  
   Lists the value you want to show on the Y axis of the bubble chart.
* **Size**   
   Lists the value you want to show as the bubble size.

**Secondary Axis**

Specifies whether to show the secondary axis in the chart. Not available to gauge chart.

![Top N button](https://devnet.logianalytics.com/hc/article_attachments/4420447081367/btn_wbrpt_topn.gif)

Opens the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/4405683806743-Category-Options-Dialog-Box-Properties) dialog box or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/4405683875351-Series-Options-Dialog-Box-Properties) dialog box to define the sort order of the category or series values and specify the number of the category or series values that will be displayed in the chart.

![Add Combo Chart](https://devnet.logianalytics.com/hc/article_attachments/4420461489943/btn_wbrpt_adcmbtyp.gif)

Adds a combo chart to the Primary Axis or Secondary Axis. Not available to gauge chart.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447073687/btn_add1.gif)

Adds a new pair of Y Axis and Radius for the bubble chart.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)

Removes the selected view element.

## For Organization Chart

![To Chart dialog - Organization](https://devnet.logianalytics.com/hc/article_attachments/4420461617303/tochart_org.gif)

**Chart Title**

Specify the title of the chart. The title is a special label bound with the chart. You can position the chart title freely in a report. Once you remove the chart from the report, Server removes the chart title too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4420461453847/btn_wbrpt_font.gif)

Specifies the [font properties](#Font) of the chart title.

**Resources**

Displays the resources that can be added to the chart.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif)

Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)

Launches the [search bar](#Search) to search for view elements.

**Value box**

* **Primary Axis**  
   Select Org from the chart type drop-down menu.
* **Node**  
   Adds a field from the Resources box which identifies the entity by selecting both the field and Child and then selecting ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).
* **Parent**  
   Adds a field from the Resources box which shows the "reporting to" relationship among the entity members, that is, which child node field member reports to or belongs to which child node field member, by selecting both the field and Parent and then selecting ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif).
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)  
   Removes the selected child node or parent field.

**Properties**

The Properties box presents a node model of the org chart. Data fields, labels and images can be inserted into the node as the information about the entity in the org chart, using ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif). By default, all added objects are placed at the left top of the node, you need to adjust their positions and sizes in the node. You can also resize the node.

To remove an object from the node, select it, and then select ![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif).

## For Heat Map

![To Chart dialog - Heat Map](https://devnet.logianalytics.com/hc/article_attachments/4420461617687/tochart_htmp.gif)

**Title**

Specifies the title of the chart. The title is a special label bound with the chart. Though it can be positioned freely in a report, once you remove the chart from the report, the title will be removed too.

![Font button](https://devnet.logianalytics.com/hc/article_attachments/4420461453847/btn_wbrpt_font.gif)

Specifies the [font properties](#Font) of the chart title.

**Resources**

Displays the resources that can be added to the chart.

![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420461453463/btn_sort.gif)

Sorts the view elements in the specified [order](#Order) from the drop-down list. Once a user changes the order, it will be applied to all the resource trees where business view elements are listed for this user.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4420453392407/btn_srch.gif)

Launches the [search bar](#Search) to search for view elements.

![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4420461488151/btn_additem.gif)

Adds the selected field into the Area or Property box.

![Remove Item button](https://devnet.logianalytics.com/hc/article_attachments/4420447082647/btn_rmvitem.gif)

Removes the selected field from the Area or Property box.

**Chart type drop-down list**

Displays Heat Map as the selected chart type.

**Area**

Lists the fields used to group the data to different areas. There should be at least one group. When there are multiple groups, their levels are defined by their positions from top down. The group at the top is of the highest level and the bottom the lowest.

* **Color by**  
   Specifies whether to color by a group. 0-n groups can be used as the color-by fields.
* **Label by**  
   Specifies whether to show the group name in the innermost rectangle.
* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)  
   Moves the selected group field higher in the list.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)  
   Moves the selected group field lower in the list.
* ![Top N button](https://devnet.logianalytics.com/hc/article_attachments/4420447081367/btn_wbrpt_topn.gif)  
   Opens the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/4405690591895-Group-Options-Dialog-Box-Properties) dialog box to define the sort order of the group values and specify the number of the group values that will be displayed in the chart.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420453394455/btn_delete.gif)  
   Removes the selected group field.

**Property**

Lists the summary fields used as size-by/color-by or displayed in the innermost rectangle.

* **Size by**  
   Specifies to size by one summary or none.
* **Color by**  
   Specifies to color by one summary or none.
* **Label by**  
   Specifies whether to show a summary in the innermost rectangle.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683891479-Tabular-Properties-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690613527-To-Crosstab-Dialog-Box-Properties)
