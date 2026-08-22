---
title: "Inserting Charts in a Report"
id: 1500009628941
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009628941-Inserting-Charts-in-a-Report
updated_at: 2022-03-28T07:12:25Z
---

# Inserting Charts in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628461-How-Data-Is-Represented-in-a-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts)

# Inserting Charts in a Report

With the chart wizard, it is easy to create charts in a report, however the wizard varies with the data resource type used for the chart: business view or query resource. In addition, based on different chart types some screens of the chart wizard display differently.

A web report and library component can only use business views. For a page report it can be created either based on query resources or business views, which is determined at the time when  [the page report is created](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page) by the Create Using Business View option. Once defined, all the data components in the page report can only be created on the specified data resource type.

The 3-D chart types are only supported in page reports that are created using query resources.

A chart can be inserted in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports#Relationship). When a chart is inserted into a banded object that is created using a query resource, you can use a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500009628401-Setting-Up-Data-Container-Links-in-Banded-Objects) to define the relationship between the chart and its parent.

This topic shows creating charts using different data resources and define the data of specific chart types as follows:

* [Creating a Chart Based on a Business View](#BV)
* [Creating a Chart Based on a Query Resource](#Query)
* [Defining the Data for an Organization Chart](#Org)
* [Defining the Data for a Heat Map](#HeatMap)
* [Defining the Values to be Compared on a Back-to-Back Chart](#Back)

## Creating a Chart Based on a Business View

1. In a report, position the mouse pointer at the destination where you want to insert the chart.
2. Do either of the following:
   * Drag the desired chart type button from the Visual category of the Components panel to the destination.
   * Select **Insert** > **Chart** or **Home** > **Insert** > **Chart**.

   The [Create Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009607502-Create-Chart-Dialog#BV) wizard appears, which contains a set of screens for helping you define a chart easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select a business view in the current catalog using which to create the chart. When the chart is to be inserted into the banded header, banded footer, group header, group footer panel of a banded object in a web report, you can also select **Inherit from the Parent** to inherit data from the business view used by the parent banded object.

   ![Create BV Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916811415/crtcht_dt_bv.gif)
4. In the Type screen, specify the type of the chart. Logi Report automatically filters out the chart types that cannot be supported in the report where the chart is to be inserted and lists only the supported types.
   * To create a single chart, select the **Single Chart** radio button, and then select the required type from the Chart Type box and its subtype accordingly.

     ![Create BV Chart - Single](https://devnet.logianalytics.com/hc/article_attachments/4404904376343/crtcht_type_bv.gif)
   * To create a combo chart, select the **Combo Chart** radio button. You can see that the Chart Type Groups box lists the two value axes: the primary axis (Y1) and the secondary axis (Y2), and an <Add Combo Type> item is displayed for each axis. A default chart subtype has been added to the primary axis. To add an additional subtype to an axis, select the corresponding **<Add Combo Type>**, and you will find that a subtype has been added. To change any subtype listed in the box, select it then choose your required chart type from the Chart Type box, and select the thumbnail for the subtype you want. To delete a subtype, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif). Most often combo charts will use a bar chart on the primary axis and a line chart on the secondary axis to make a readable chart.

     ![Create BV Chart - Combo](https://devnet.logianalytics.com/hc/article_attachments/4404904460311/cmpnt_cht_inst_combo.gif)
5. In the Display screen, define the data to display in the chart. You can specify a title for the chart in the Title text box.

   ![Create BV Chart - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904376727/crtcht_dsply_bv.gif)

   The following shows defining the data on a chart generally. If you have selected the Org or Heat Map chart type, data on the chart are specified differently (for details see [Defining the Data for an Organization Chart](#Org)  and [Defining the Data for a Heat Map](#HeatMap)).

   The Resources box lists all the view elements in the specified business view, and the [dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) created for the business view in the current report. Add them to the category, series and value axes of the chart respectively. You can also create more dynamic resources to use in the chart.

   * To add the category field of the chart, select a group object ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif), detail object ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425495/bv_detail.gif), dynamic formula used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif), or dynamic formula used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828823/bv_dynfmla_dtl.gif), then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) beside the Category box or drag and drop it from the Resources box to the Category box. You can define [special group](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#Special), [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#Group) and [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#SelectN) on the field.
   * To add the series field of the chart, select a group object ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif), or dynamic formula used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif), then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) beside the Series box or drag and drop it from the Resources box to the Series box. You can also define [special group](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#Special), [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#Group) and [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#SelectN) on the field.
   * To add a field to the value axis of the chart, select an aggregation object ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif), a group object ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif)/detail object ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425495/bv_detail.gif) that is of Numeric type (an indicator chart also supports String or Boolean type), dynamic aggregation ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif), dynamic formula used as Aggregation ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif), dynamic formula used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif)/Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828823/bv_dynfmla_dtl.gif) that returns Numeric values (for an indicator chart String or Boolean value too), or an [additional value](#Additional), then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) beside the Show Values box or drag and drop it from the Resources box to the Show Values box. You can add multiple fields on the value axis and use ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the display order of the fields on the axis. If you are creating a combo chart, specify the fields on the value axis of each subtype respectively. For a bubble chart, the Show Values box contains three nodes: X-Axis, Y-Axis and Size and you need to specify the fields to display on the bubble X axis and Y axis and the field to determine the size of the bubbles respectively. When a field is added for the bubble X axis, this field will be displayed on the category axis instead of the one specified in the Category box, while the field defined in the Category box will still be included in data calculation. See [Creating Motion Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500009629001-Creating-Motion-Charts) for a bubble chart example.

     **Tip:** When the category field is a detail object, aggregation objects cannot be used on the value axis, and vice versa. On the value axis, group objects and detail objects cannot be used together with aggregation objects, and for an indicator chart, group objects and detail objects that are of different data types cannot be mixed either.

   If you want to remove any field from the chart, select it in the corresponding axis box and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. You can also make the chart a [real time chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009606162-Creating-Real-Time-Charts) or a [motion chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009629001-Creating-Motion-Charts).

   **To add an additional value to the value axis:**

   1. From the Resources box, select **Constant** **Value**/**Average****Value** in the Additional Value node and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) beside the Show Values box. The [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009630601-Edit-Additional-Value-Dialog) dialog appears.

      ![Edit Additional Value dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904355095/edtaddtnvlu_cnst.gif)
   2. In the Name text box, specify the display name for the constant/average value.
   3. Type the constant value with numeric type in the Value text box, or select a field based on which the average value will be calculated from the Based On drop-down list.
   4. Select **OK**, and the defined constant/average value is added into the Show Values box.

      If you want to further modify a constant/average value, select the value in the Show Values box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404904261015/btn_edit1.gif). In the Edit Additional Value dialog, edit the value as required.
6. In the Filter screen, apply a filter to reduce the data displayed in the chart. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the Filter drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   ![Create BV Chart - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404916812311/crtcht_fltr_bv.gif)
7. In the Layout screen, specify the layout of the chart.

   ![Create BV Chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904377495/crtcht_layout.gif)

   The following shows the layout options in general. Some options may not be available for certain chart types.

   | Option Type | Option Name | Description |
   | --- | --- | --- |
   | Data | Category Start Offset | Specifies the start offset of category from which the chart will be displayed. |
   |  | Category End Offset | Specifies the end offset of category to which the chart will be displayed. |
   |  | Series Start Offset | Specifies the start offset series from which the chart will be displayed. |
   |  | Series End Offset | Specifies the end offset of series to which the chart will be displayed. |
   |  | The above four options work together to control the range of the data to be displayed on the chart. [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Offset) for more information. | |
   |  | Reverse Category | Specifies whether to reverse the display order of the categories. |
   |  | Reverse Series | Specifies whether to reverse the display order of the series. |
   |  | Swap Groups | Specifies to display values from different data fields by switching data between the category and series axes, the category and values axes. |
   | Title | Chart Title | Specifies the title of the chart. |
   |  | Category (X) Axis Title | Specifies the title of the X-axis. |
   |  | Value (Y) Axis Title | Specifies the title of the Y-axis. |
   |  | Value (Y2) Axis Title | Specifies the title of the Y2-axis. |
   | Axis | Show Category (X) Axis | Specifies whether to show the category (X) axis in this chart. |
   |  | Show Value (Y) Axis | Specifies whether to show the value (Y) axis in this chart. |
   |  | Show Value (Y2) Axis | Specifies whether to show the value (Y2) axis in this chart. |
   |  | Show Series (Z) Axis | Specifies whether to show the series (Z) axis in this chart. |
   |  | If you choose not to display a certain axis, the labels and tick marks along the axis will be hidden as well. | |
   | Wall | Show Wall | Specifies whether to show the wall in this chart. |
   |  | Show Floor | Specifies whether to show the floor in this chart. |
   | Gridlines | Show Category (X) Axis Gridlines | Specifies whether to show the gridlines of category (X) axis. |
   |  | Show Value (Y) Axis Gridlines | Specifies whether to show the gridlines of value (Y) axis. |
   |  | Show Value (Y2) Axis Gridlines | Specifies whether to show the gridlines of value (Y2) axis. |
   |  | Show Series (Z) Axis Gridlines | Specifies whether to show the gridlines of series (Z) axis. |
   | Type | Top Down | Specifies to expand the org chart tree from top to bottom. |
   |  | Bottom Up | Specifies to expand the org chart tree from bottom to top. |
   |  | Left Right | Specifies to expand the org chart tree from left to right. |
   | Legend | Show Legend | Specifies whether to show the legend in this chart. |
   | Export | Mapping Component | This option is disabled when creating a chart. It specifies the component to which the chart will be mapped. For details, see [Creating Dynamic Charts in Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009605662-Creating-Dynamic-Charts-in-Excel). |
8. In the Style screen, select a style for the chart.

   ![Create BV Chart - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904377751/crtcht_sty.gif)

   When you have specified to insert the chart into a banded object in a page report, by default the chart will [inherit its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613462-Applying-Styles#Inherit). If you want to apply another style to the chart, clear the **Inherit Style** option and then select the required style from the Style box.
9. Select **Finish** to insert the chart.

   If you have selected a panel in a banded object as the chart destination, after finishing the wizard you need to select the mouse button in the destination once again in order to insert the chart there.

## Creating a Chart Based on a Query Resource

1. In a page report, position the mouse pointer at the destination where you want to insert the chart.
2. Do either of the following:
   * Drag the desired chart type button from the Visual category of the Components panel to the destination.
   * Select **Insert** > **Chart** or **Home** > **Insert** > **Chart**.

   The [Create Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009607502-Create-Chart-Dialog#Query) wizard appears, which contains a set of screens for helping you define a chart easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select the data resource in the current catalog using which to create the chart.

   ![Create Query Chart - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916812567/crtcht_dt.gif)

   If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one. When a query is selected, you can select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog). Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current page report to create the chart, select the **More Options** button and then:

   * Select the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog), or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report will still run the query separately for each dataset.
   * Select the **Current Dataset** radio button to make the chart inherit the dataset from its parent.
4. In the Type screen, specify the type of the chart. You can create either a [single chart or a combo chart](#Type).

   ![Create Query Chart - Type](https://devnet.logianalytics.com/hc/article_attachments/4404904378391/crtcht_type.gif)
5. In the Display screen, specify the fields on the category, series and value axes of the chart respectively.

   ![Create Query Chart - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904378903/crtcht_dsply.gif)

   The following shows defining the data on a chart generally. If you have selected the Org or Heat Map chart type, data on the chart are specified differently (for details see [Defining the Data for an Organization Chart](#Org)  and [Defining the Data for a Heat Map](#HeatMap)).

   The Resources box lists all the DBFields in the specified data resource as well as the valid formulas and summaries of the DBFields in the current catalog. When the predefined formulas or summaries cannot meet your requirements, you can select **<New Formula...>** in the Formulas node to [create formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009634201-Creating-Formulas-in-a-Catalog), or **<New Summary...>** in the Summaries node to [create summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Create) to use in the chart (if the chart is to be inserted in a banded object and it inherits the parent's dataset, make sure the summaries take Down group by level if you want to use dynamic summaries). Add them to the chart axes to define the chart.

   * To add a field to the category/series axis of the chart, select a DBField or formula and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) beside the Category/Series box or drag and drop it from the Resources box to the target box. You can define [special group](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#Special), [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#Group) and [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#SelectN) on the field.
   * To add a field to the value axis of the chart, select a summary, DBField of Numeric type (an indicator chart also supports String or Boolean type), formula that returns Numeric values (for an indicator chart String or Boolean values too), or an [additional value](#Additional), then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) beside the Show Values box or drag and drop it from the Resources box to the Show Values box. You can add multiple fields on the value axis and use ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the display order of the fields on the axis. If you are creating a combo chart, you need to specify the fields on the value axis of each subtype respectively.

     For a bubble chart, the Show Values box contains three items: X Axis, Y Axis and Radius. You need to specify the fields to display on the bubble X axis and Y axis and the field to determine the size of the bubbles respectively. When a field is added for the bubble X axis, this field will be displayed on the category axis instead of the one specified in the Category box, while the field defined in the Category box will still be included in data calculation. See [Creating Motion Charts](https://devnet.logianalytics.com/hc/en-us/articles/1500009629001-Creating-Motion-Charts) for a bubble chart example.

     For a back-to-back chart, you need to specify how the comparison on the value axis of the chart is. For details, see [Defining the values to be compared on a back-to-back chart](#Back).

     **Tips:**

     + Whether DBFields, formulas and summaries can be used together on the value axis depends on if they have the same group setting. If a DBField is added on the value axis, no summaries and group level formulas are allowed on the axis; if a summary is added, only formulas calculated on the same group level as the summary can be added and vice versa. For an indicator chart, DBFields and formulas that are of different data types cannot be mixed on the value axis.
     + If you have defined a subtype of the Stock type, you should add fields for the subtype in the order indicated by the subtype name, for example, if you define the Open-High-Low-Close 2-D subtype, then you should add four fields to the Show Values box for this subtype, and arrange them to the order of Open-High-Low-Close.

   If you want to remove any field from the chart, select it in the corresponding axis box and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box.
6. In the Filter screen, add filter conditions on the fields that have been added to the chart to reduce the data. For how to define a filter, [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009636161-Filtering-Reports#DefineFilter).

   ![Create Query Chart - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904379927/crtcht_fltr.gif)
7. In the Layout screen, specify the [layout](#Layout) of the chart.

   ![Create Query Chart - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904377495/crtcht_layout.gif)
8. In the Style screen, select a style for the chart.

   ![Create Query Chart - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904377751/crtcht_sty.gif)

   When you have specified to insert the chart into a banded object, by default the chart will [inherit its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613462-Applying-Styles#Inherit). If you want to apply another style to the chart, clear the **Inherit Style** option and then select the required style from the Style box.
9. Select **Finish** to insert the chart.

   If you have selected a panel in a banded object as the chart destination, after finishing the wizard you need to select the mouse button in the destination once again in order to insert the chart there.

## Defining the Data for an Organization Chart

An organization (org) chart is a tree-structure diagram showing hierarchical relationships of one people to another, one position to another, one department to another, and so on in an organization. The hierarchical relations are defined by the node field and parent field. The node field values are displayed as nodes in the org chart, and two nodes that have hierarchical relationship are connected by a line. All the relations will finally go to one root node which presents the top level position. The closer to the top root node, the higher the level.

Org chart nodes are also containers in which data objects, labels and images can be inserted. In this way you can add the information you want to display in the nodes to get data about each node.

To define the data to display in an org chart, in the Display screen of the Create Chart wizard:

![Org Display](https://devnet.logianalytics.com/hc/article_attachments/4404916811799/crtcht_dsply_org_bv.gif)

1. From the Node drop-down list select the field to be used as the node field.
2. From the Parent drop-down list select the field which defines the ownership or reporting to relationship among the node field values. The parent field should be of the same data type as the node field and the values of the parent field should be a subset of those of the node field.

   In the following example, the node field contains three employee names: Tony, Amanda and Jack, and the parent field is also about employee names and contains Amanda who is the leader of Tony and Jack who is the leader of Amanda. Jack will be the top root node of the org chart.

   | Employee Name (node field) | Leader Name (parent field) |
   | --- | --- |
   | Tony | Amanda |
   | Amanda | Jack |
   | Jack |  |
3. The Properties box displays a node model for specifying the information you want to display in each node in the org chart. You can add the data fields available in the Resources box and labels and images to display in the nodes.

   To add an object, select it in the Resources box, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it to the node model. You can resize the node model and adjust the position and size of the added objects in the node model as required, which can also be performed in the Design area of Logi Report Designer after the chart is created. To remove an unwanted object from the node model, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or press **Delete** on the keyboard.

## Defining the Data for a Heat Map

A heat map displays data in a matrix as rectangles marked by colors and sizes. Multiple group levels are translated into rectangles representing a higher-level group further divided into smaller rectangles that represent the lower level group. The rectangles representing the lowest-level group are called the innermost rectangles. Group-by fields and summarized data can be displayed in the innermost rectangles for showing the group values and for calculating data of the groups. Each rectangle has a title which shows the corresponding group value and is by default hidden for better appearance (to have the title of a rectangle shown, locate its Rectangle Title node in the Report Inspector and set the Invisible property to false).

To define the data to display in a heat map, in the Display screen of the Create Chart wizard:

![Heat Map Display](https://devnet.logianalytics.com/hc/article_attachments/4404916812055/crtcht_dsply_htmp_bv.gif)

1. In the Resources box, choose a field as the group-by field and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) beside the Area box or drag and drop it from the Resources box to the Area box to add a group in the heat map. Repeat this to add more groups. You can use ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) and ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) above the Area box to adjust the group levels. To remove a group from the heat map, select it in the Area box and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box.

   When creating the heat map using a business view, you can use the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif) in the specified business view or the dynamic formulas used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif) created for the business view in the current report as the group-by fields. When creating using a query resource, any DBField or formula in the Resources box can be used as the group-by fields.
2. In the Area box, select the **Color By** checkboxes for the groups that are used to determine the fill color of the rectangles, and the **Label By** checkboxes for the groups you want to display in the innermost rectangles.
3. You can define [special group](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#Special), [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#Group) and [Order/Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts#SelectN) on each group.
4. From the Resources box add fields to the Property box to calculate data based on the lowest group of the heat map.

   When creating the heap map using a business view, you can add aggregation objects ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif), dynamic aggregations ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) and dynamic formulas used as Aggregation ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) to calculate data. When creating using a query resource, if no group is added in the Area box, you can insert any dynamic summary or static summary, and the group-by field of the static summary will be inserted into the Area box automatically; if there are multiple groups, the static summaries to be inserted should match the lowest-level group. For example, if the group levels are A > B > C, the static summaries grouped by C can be inserted into the Summaries box, but the static summaries grouped by A, B or other fields cannot.
5. In the Property box, select one field's **Size By** checkbox to use it to determine the size of the rectangles (the negative values of the size-by field will be ignored when the heat map is generated); select one field's **Color By** checkbox which is used to determine the fill color of the rectangles; select the **Label By** checkboxes for these you want to display in the innermost rectangles. At least one option must be selected for a field in the Property box, otherwise it will not be used in the heat map.

After a heat map is created, you can further edit it in the design area. Only the first rectangle which represents the lowest group level in the heap map is editable and can contain objects. You can insert the group fields of the heat map from the Data panel, as well as labels and images via the Components panel into it. For the objects in the rectangle, you can edit or delete them just like they do in a text box. The inserted objects do not support absolute position since the width and height of the rectangle are determined dynamically at runtime.

## Defining the Values to be Compared on a Back-to-Back Bench Chart

A back-to-back bench chart is used for comparing values on the value axis. It displays and compares the contribution of each data value on the origin left and origin right across categories. For example, you may want a chart that compares the sales of each country in Latin America and North America, you can then use a back-to-back chart to display category Year and series Country, and define a condition on the series to make the Latin American countries display on the origin left of the category axis and North American countries on the origin right. Then you get to easily see not only the individual countries but can compare both regions.

When you define how the comparison on the value axis of a back-to-back bench chart is created, you can either [add two values on the origin left and origin right of the value axis](#Value) to compare if it is a 2-D chart, or make the comparison based on the series field values if the chart contains a series field. When the comparison is based on series values, you need to further define the series values to display on the origin left and origin right of the value axis: either [manually](#SeriesValue) or [use a condition](#SeriesCondition).

**To make the comparison based on fields displayed on the value axis of a 2-D back-to-back bench chart:**

1. In the Display screen of the Create Chart wizard, select **Show Values**.

   ![Compare by Show Values](https://devnet.logianalytics.com/hc/article_attachments/4404904461079/cmpnt_cht_inst_back1.gif)
2. In the Resources box, select a DBField of Numeric type, a formula that returns Numeric values or a summary, specify where you want the field to display on the value axis, the origin left or right by selecting the chart type node in the Left or Right box, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop the field to the Left or Right box.
3. Select the chart type node in the opposite box and add the field to display on the opposite origin of the value axis. Only one field is allowed for one origin.

   To remove the field added on either origin, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box.

**To compare based on the series field and define the series values manually:**

1. In the Display screen of the Create Chart wizard, select **Series Values**.

   ![Compare by Series Values](https://devnet.logianalytics.com/hc/article_attachments/4404904461335/cmpnt_cht_inst_back2.gif)
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the Left/Right box to add a value line, double-click in the line and type the required value of the series field.
3. Repeat the above step to add more values.

   To adjust the display order of the values, select a value and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif). To remove a value, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).
4. In the Show Values box, add a DBField of Numeric type, a formula that returns Numeric values or a summary to display on the value axis of the chart.

   When the chart is generated, the specified series values will be shown on the origin left/right of the value axis on the chart and the undefined values of the series field on the opposite origin.

**To compare based on the series field and use a condition to define the series values:**

1. In the Display screen of the Create Chart wizard, select **Series Conditions**.

   ![Compare by Series Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404916838551/cmpnt_cht_inst_back3.gif)
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404904261015/btn_edit1.gif) above the Left/Right box. The [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog) dialog appears.

   ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904187799/edtcndtn.gif)
3. Select the **Add Condition** button to add a condition line.
4. Select the series field from the first drop-down list, from the operator drop-down list set the operator with which to compose the condition.
5. All values of the series field are listed in the third drop-down list. Select the value or values according to the selected operator. If you want to type in the value manually, when multiple values are required, you should separate them with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".
6. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
7. Select **OK** to finish defining the condition. The condition expression is displayed in the Left/Right box.
8. In the Show Values box, add a DBField of Numeric type, a formula that returns Numeric values or a summary to display on the value axis of the chart.

   When the chart is generated, the series values that meet the specified condition will be shown on the origin left/right of the value axis on the chart and the remaining values of the series field on the opposite origin.

**Example of creating a back-to-back bench chart**

Suppose you want to have a chart to compare the sales for individual countries in Latin America and North America, you can create it as follows:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog, select **Chart** and select **OK**. The Chart Wizard is displayed.
4. In the Data screen, select **More Options** to expand the dataset selection panel.
5. Select the **Existing****Dataset** radio button, and select **<New Dataset...>**.
6. In the New Dataset dialog, select **WorldWideSales** from the Queries node, then select **OK** to create the dataset and close the dialog. A new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) WorldWideSales is added to the dataset list and selected by default in the Data screen of the Chart Wizard.

   Next we will filter the dataset to use data in the Latin America and North America regions only. By using dataset filter, the reports that use the same query will not be affected.
7. Select the **Edit** button. In the Dataset Editor, switch to the **Filter** tab, then [specify the filter condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets#Filter) as *Region = Latin America Or Region = North America* and select **OK**.

   ![Filter Dataset](https://devnet.logianalytics.com/hc/article_attachments/4404904461719/cmpnt_cht_inst_backeg1.gif)
8. Select **Next** in the Chart Wizard.
9. In the Type screen, select the **Bench** chart type, then select the  **Back to Back Bench 2-D** subtype. Select **Next**.
10. In the Display screen, add **Country** in the Customers table to the Clustering (Series) box.
11. Select **Series Conditions** and select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404904261015/btn_edit1.gif) above the Right box.
12. In the Edit Condition dialog, specify the filter condition as *Country in Canada,Mexico,USA*. Select **OK** to return to the Chart Wizard.
13. Add the summary **Sum\_SalesbyYear** that is listed at the end of the resource tree to the Bar Length (Show Values) box. The summary is grouped by the formula YearOfOrderDate, so the formula is added to the Y-Axis (Category) box automatically.

    ![Add a Summary to the Chart](https://devnet.logianalytics.com/hc/article_attachments/4404904461975/cmpnt_cht_inst_backeg2.gif)
14. Select **Finish** to create the chart.
15. Save the report and select the **View** tab to preview the chart. You can see sales for countries in Latin America are shown on the origin left of the value axis and sales of North American countries on the origin right.

    ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404904462359/cmpnt_cht_inst_backeg3.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628461-How-Data-Is-Represented-in-a-Chart) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628961-Modifying-Charts)
