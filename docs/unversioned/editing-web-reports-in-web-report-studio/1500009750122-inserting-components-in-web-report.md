---
title: "Inserting Components  in Web Report"
id: 1500009750122
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750122-Inserting-Components-in-Web-Report
updated_at: 2021-07-24T00:47:29Z
---

# Inserting Components  in Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778761-General-Operations-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components)

# Inserting Components in Web Report

You can insert components into a web report via the Components panel on the left of the Web Report Studio window. This topic describes how you can insert different components in web reports.

The following table lists the report areas that are valid targets for the various components:

|  | Report Layout Area | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Component | Report Body | Page Header/Footer | Tabular Cell | Table Cell | KPI | Banded Panel |
| Chart | Y | Y | Y | N | N | Y |
| Crosstab | Y | Y | Y | N | N | Y |
| Table | Y | Y | Y | N | N | Y |
| Banded Object | Y | Y | Y | N | N | N |
| KPI | Y | Y | Y | N | N | N |
| Label | Y | Y | Y | Y | Y | Y |
| Image | Y | Y | Y | N | Y | Y |
| Web Control | Y | Y | Y | N | N | Y |
| Special Field | Y | Y | Y | Y | Y | Y |
| Multimedia Object | Y | Y | Y | N | N | Y |
| Horizontal/Vertical Line | N | N | N | N | N | Y |
| Page Break | Y | N | N | N | N | N |
| Formula | N | Y | Y | Y | Y | Y |
| Group Object | N | Y | Y | Y | Y | Y |
| Detail Object | N | Y | Y | Y | Y | Y |
| Aggregation Object | N | N | N | Y | Y | Y |

This topic contains the following sections:

* [Inserting a Table](#Table)
* [Inserting a Crosstab](#Crosstab)
* [Inserting a Chart](#Chart)
* [Inserting a Banded Object](#Banded)
* [Inserting a KPI](#KPI)
* [Inserting a Label](#Label)
* [Inserting an Image](#Image)
* [Inserting a Web Control](#WebControl)
* [Inserting a Special Field](#Special)
* [Inserting a Multimedia Object](#Multimedia)
* [Inserting a Horizontal/Vertical Line](#Line)
* [Inserting a Page Break](#PageBreak)

## Inserting a Table

The procedure for inserting tables in a web report varies with the way you use to access Web Report Studio: [using the quick start method or the traditional method](https://devnet.logianalytics.com/hc/en-us/articles/1500009778701-Web-Report-Studio#Way).

**To insert a table when Web Report Studio is in the quick start way**:

1. Drag the table icon ![Drag to add table button](https://devnet.logianalytics.com/hc/article_attachments/4404880143255/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table. Server displays the Select Data Source dialog box.
2. [Select a business view and define the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009778861-Quick-Start-with-a-Table-Report).
3. Select **OK** to insert the table.

**To insert a table when Web Report Studio is in the traditional way:**

When Web Report Studio is in the traditional way, you can choose the table type as you want: [Group Above, Group Left, Group Left Above](#Group), or [Summary Table](#Summary).

* **Inserting a group table**
  1. Drag the table icon ![Drag to add table button](https://devnet.logianalytics.com/hc/article_attachments/4404880143255/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table. Server displays the [Insert Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009776041-Insert-Table-Dialog-Box-Properties) dialog box.

     ![Insert Table dialog - Details tab](https://devnet.logianalytics.com/hc/article_attachments/4404885334167/insrttbl_dsply.gif)
  2. Type a title for the table in the **Table Title** text box.
  3. Select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif) to set the font properties for the title.
  4. From the **Data Source** drop-down list, select the business view to create the table with.

     When you insert the table into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel, it by default [inherits data](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report#Inherit) from the business view used by the parent banded object (Server selects **<Inherit from the Parent>** in the Data Source drop-down list by default). You can select another business view to create the table if you want.
  5. Select the **Filter** button if you want to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778741-Applying-Filters-in-Web-Report) to the business view to narrow down data in the table.
  6. Select a group type from the table type drop-down list: Group Above, Group Left, or Group Left Above.
  7. In the **Details** tab, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) from the Resources box to display as detail fields in the table.
  8. To adjust the display order of the objects in the right box, select one and then select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
  9. By default, Server uses the display names of the added objects to label the corresponding detail columns. To edit the label text for a detail column, select in the Label text box and type a new one. If you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.
  10. If you want to sort the detail data in the table by values of specified fields, select the **Sort Fields By** button and set the sort manner in the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009775101-Custom-Sort-Dialog-Box-Properties) dialog box.

      ![Custom Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880169879/cstmsrt.gif)

      1. From the Resources box select an object in the current business view and select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) to add it to the right box as the sort-by field.
      2. Select a sort order from the **Sort** column. Server sorts the detail data in the table based on the values of the sort-by field in ascending or descending order.
      3. Repeat the above two steps to add more sort-by fields.
      4. Select the **Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Down** button![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) to adjust the order of the sort-by fields, which determines the sort priority of the fields.
      5. Select **OK** to accept the sort settings.
  11. In the **Group** tab, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) as the grouping criteria.
  12. You can select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)to adjust the group levels.
  13. In the Sort column select the sort manner of each group level, which can be No Sort, Ascend, Descend, or [Custom Sort](#GroupSort).

      ![Insert Table dialog - Group tab](https://devnet.logianalytics.com/hc/article_attachments/4404885334679/insrttbl_grp.gif)

      **To customize the sort manner of a group:**

      1. Select **Custom Sort** as the sort manner for the group. Server displays the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009775101-Custom-Sort-Dialog-Box-Properties) dialog box.

         ![Custom Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880169879/cstmsrt.gif)
      2. From the Resources box select an object in the current business view and select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) to add it to the right box as the sort-by field.
      3. Select a sort order from the **Sort** column. Then Server sorts the groups at this group level by the values of the first record in each group on the related field based on the defined sort direction.
      4. Repeat the above two steps to add more sort-by fields.
      5. Select the **Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) to adjust the order of the sort-by fields, which determines the sort priority of the fields.
      6. Select **OK** to accept the sort settings.
  14. In the **Summary** tab, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) to summarize data in the table as follows: in the right box, select the group to apply the aggregation to, then select an aggregation object in the Resources box and click the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) to add it to the right box. You can add several aggregations for any group level.

      ![Insert Table dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4404880171287/insrttbl_sum.gif)
  15. You can select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) to adjust the order of the aggregations in the current group or move an aggregation to another group.
  16. For the Group Left table, you can use the **Row** and **Column** columns to control the position of the aggregations in the table.
  17. Select **OK** to insert the table.
* **Inserting a summary table**  
   You can use summary tables for showing group and summary information, and they can only contain group and aggregation objects. In a summary table, the groups on the left have higher group levels than those on the right and calculation of the aggregation objects is always based on the innermost group no matter where you position them in the table.
  1. Drag the table icon ![Drag to add table button](https://devnet.logianalytics.com/hc/article_attachments/4404880143255/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table. Server displays the [Insert Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009776041-Insert-Table-Dialog-Box-Properties) dialog box.
  2. Type a title for the table in the **Table Title** text box.
  3. Select the **Font** button ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif) to set the font properties for the title.
  4. From the **Data Source** drop-down list, select the business view using which to create the table.

     When you are going to insert the table into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel, it by default [inherits data](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report#Inherit) from the business view used by the parent banded object (Server selects **<Inherit from the Parent>** by default). You can select another business view to create the table if you want.
  5. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778741-Applying-Filters-in-Web-Report) to the business view to narrow down data in the table.
  6. Select **Summary Table** from the table type drop-down list.
  7. In the **Columns** tab, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) and aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) in the specified business view from the Resources box to display in the table.

     ![Insert Table dialog - Columns tab](https://devnet.logianalytics.com/hc/article_attachments/4404880171671/insrttbl_clmn.gif)
  8. You can select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) to adjust the display order of the added objects. The order of the group objects determines the group levels in the table: the topmost group object the highest group level and the lowest group object the innermost group level. All the aggregations are parallel, and Server calculates them based on the lowest group.
  9. In the **Sort** column select the sort manner of groups in each group level, which can be No Sort, Ascend, Descend, or [Custom Sort](#GroupSort).
  10. In the **Summary** tab, you can insert the aggregation objects you selected in the Columns tab to the table header/footer and to the group headers/footers of existing groups. First select an aggregation object in the Resources box, then select the check boxes representing the required locations.
      Server places the aggregation in the intersection of its summary column and the table/group header/footer row.

      ![Insert Table dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4404880172311/insrttbl_sum1.gif)
  11. Select **OK** to insert the table.

## Inserting a Crosstab

1. Drag **Crosstab** from the Components panel or the crosstab icon ![Drag to add crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404880143511/btn_wbrpt_2crstb.gif) from the visualization toolbar to the destination where you want to insert the crosstab. Server displays the [Insert Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009747602-Insert-Crosstab-Dialog-Box-Properties) dialog box.

   ![Insert Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885335063/insrtcrstb_data.gif)
2. Type a title for the crosstab in the **Crosstab Title** text box.
3. Select the font button ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif) to set the font properties for the title.
4. From the **Data Source** drop-down list, select the business view using which to create the crosstab.

   When you are going to insert the crosstab into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel, it by default [inherits data](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report#Inherit) from the business view used by the parent banded object (Server selects **<Inherit from the Parent>** by default). You can select another business view to create the crosstab if you want.
5. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778741-Applying-Filters-in-Web-Report) to the business view to narrow down data in the crosstab.
6. In the **Data** tab, select a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) from the Resources box and then select the add buttons ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) or ![Add Row button](https://devnet.logianalytics.com/hc/article_attachments/4404880172823/btn_addrow.gif) to add it as a column or row group in the crosstab.
7. In the **Sort** column, specify the sort manner of the group.
8. Select an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) or a detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) then and select the add button ![Add Summary button](https://devnet.logianalytics.com/hc/article_attachments/4404880173207/btn_addsum.gif) to add it to the **Summaries** box as an aggregate field to create aggregations in the crosstab. If you added a detail object, select the aggregate function for it from the **Aggregate** drop-down list. When you selected **DistinctSum** as the function, you should select the button ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404885320983/btn_chsr.gif) next to the **Distinct On** text box to select one or more detail objects according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009776261-Select-Fields-Dialog-Box-Properties) dialog box.
9. You can specify a comparison function for the aggregate field.

   **To define comparison function for an aggregate field:**

   1. Select the aggregate field in the **Summaries** box and select **Comparison Function**. Server displays the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009775041-Comparison-Function-Dialog-Box-Properties) dialog box.

      ![Comparison Function dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880173719/cmprsnfctn.gif)
   2. From the **Function** drop-down list, select the required function: Percentage, Permillage, or Difference.
   3. Select a position for the comparison function.
      * **Comparison Function Spans on Row Direction**  
         Server places the comparison function into the column total cell of the crosstab.
      * **Comparison Function Spans on Column Direction**  
         Server places the comparison function into the row total cell of the crosstab.
   4. The **Break By** and **Refer To** options determine the numbers that form the calculation of the comparison function.

      Items in the **Break By** drop-down list vary based on the position of the comparison function. It indicates the first parameter of the comparison function: the detail aggregation in the crosstab (Aggregate) or the subtotal of a specified row/column group.

      Items in the **Refer To** drop-down list also vary according to what you have selected from the **Break by** drop-down list. It indicates the other parameter of the comparison function: the grand total or subtotal for an outer row/column group.
   5. Select **OK**. Server adds a new object into the **Summaries** box.
   6. Set the label text for the object in the **Label** column.
10. For each column/row/summary field, you can type a name in the Label text box to label the corresponding column header/row header/summary, or select the **Auto Map Field Name** check box beside the text box if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field. When the text box is blank and you have not selected the check box, Server does not create a label.
11. Add more column/row groups and aggregate fields to display in the crosstab.
12. To adjust the display order of the fields, select a field and then select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
13. To remove an unwanted field, select it and select the **Remove** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif).
14. In the **Layout** tab, specify the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009747602-Insert-Crosstab-Dialog-Box-Properties#Layout) for the crosstab.

    ![Insert Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880174231/insrtcrstb_layout.gif)
15. Select **OK** to insert the crosstab.

**Tip:** When you create a crosstab with wizard, by default, Server does not create labels for its columns, rows, and summaries (the **Label** columns in the Columns, Rows, and Summaries boxes of the wizard are blank by default). You can make Web Report Studio automatically provide the labels which by default are the display names of the added objects, by setting the [profile options](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#Crosstab)**Add Labels for Crosstab Rows and Columns** and **Add Labels for Crosstab Summaries**. You can also customize the profile option **Display Crosstab Summaries Vertically** to make the summaries in crosstabs display horizontally in Web Report Studio.

## Inserting a Chart

Normally, a chart displays values in a static way, and you cannot change the values on it once you created it. However, Logi Report provides you with options to make the chart interactive and dynamic. For example, if your data source uses data that changes quickly over time such as stock market values, you can create a real time chart, so that the chart will update itself based on a defined interval using the real time data from the data source. You can make a chart move at runtime based on the value changes of a motion field by creating a motion chart. In a motion chart, the chart is playable. You can start or stop the chart to play the dynamic trend of the motion field, control the moving speed of the chart, and if you create a bubble motion chart, you can even use a trail control to make the chart move showing a bubble or line trail.

In Web Report Studio, when you create a chart, you can choose to make it a [common chart](#Common), an [organization chart](#Org), a [heat map](#Heatmap), a [real time chart](#RealTime), or a [motion chart](#Motion).

**To create a common chart:**

1. Drag **Chart** from the Components panel or a chart icon from the visualization toolbar to the destination where you want to insert the chart. Server displays the [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009747582-Insert-Chart-Dialog-Box-Properties) dialog box.

   ![Insert Chart dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880174615/insrtcht.gif)
2. Type a title for the chart in the **Chart Title** text box.
3. Select the font button ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif) to set the font properties for the title.
4. From the **Data Source** drop-down list, select the business view using which to create the chart.

   When you are going to insert the chart into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, and group footer panel, it by default [inherits data](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report#Inherit) from the business view used by the parent banded object (Server selects **<Inherit from the Parent>** by default). You can select another business view to create the chart if you want.
5. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778741-Applying-Filters-in-Web-Report) to the business view to narrow down data in the chart.
6. To create a single chart, in the **Primary Axis** box on the right, select a chart type from the chart type drop-down list.

   To create a combo chart, select the **Add Combo Chart** button**![Add Combo Chart](https://devnet.logianalytics.com/hc/article_attachments/4404880175127/btn_wbrpt_adcmbtyp.gif)** above the **Primary Axis** box. Server adds an additional chart type. You can replace the additional chart type by selecting the required one from the chart type drop-down list. Repeat this to add more chart types. Select the **Secondary Axis** check box if you want to have the secondary axis (Y2) and then define the chart types on the axis. To delete a chart type, select it and then select the **Remove** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif).
7. In the **Primary Axis** or **Secondary Axis** box, select a chart type and then add an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif), a numeric detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif), or an [additional value](#Value)![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404880175511/btn_wbrpt_adtnl.gif) as the value of the type. You can add more than one value to a chart type. Each added chart type shall have at least one value.

   If you select the **Bubble** chart type, you need to specify the values for the bubble X axis and Y axis and the value to determine the size of the bubbles, respectively. When you added a value for the bubble X axis, Server displays it on the category axis instead of that you specified for the category axis, while still including the value you added to the category axis in data calculation.

   ![Bubble Value](https://devnet.logianalytics.com/hc/article_attachments/4404880176023/wbrpt_edt_insrt_bblcht.gif)

   **To add an additional value to a chart type:**

   1. Select the chart type in the value box.
   2. In the Resources box, select **Constant Value** or **Average Value** under the **Additional Values** node.
   3. Select the add button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) beside the value box. Server displays the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009746922-Edit-Additional-Value-Dialog-Box-Properties) dialog box.
   4. In the **Name** text box, type the display name for the constant/average value.
   5. Type the constant value of numeric type in the **Value** text box, or select a field based on which to calculate the average value from the **Based On** drop-down list.
   6. Select **OK**. Server adds the defined constant/average value to the chart type.

      To modify a constant/average value, select the value in the value box, then select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880163863/btn_wbrpt_edit.gif). In the Edit Additional Value dialog box, edit the value as required.
8. Add a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) or a detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) from the Resources box to display it on the category axis of the chart.
9. Add a group object to display on the series axis. The labels for the category and series axes vary with different chart types, for example, they are **X-Axis** and **Clustering** for a clustered bar chart.
10. If you want to customize the sort order and define Select N condition for values displayed on the category/series axis of the chart, select the **Top N** button ![Category/Series Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880176279/btn_wbrpt_topn.gif) above the axis box, then define the order and condition in the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009746902-Category-Options-Dialog-Box-Properties) dialog box or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009747962-Series-Options-Dialog-Box-Properties) dialog box.
    1. In the Category Order/Series Order box, select an order to sort values of the category/series field.

       ![Category Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880176791/ctgryoptn.gif)
    2. In the Category Selection/Series Selection box, set the **Select** condition to All, Top N, or Bottom N. If you select **All**, Server displays all category/series values in the chart. If you select **Top N** or **Bottom N**, Server displays a text box next to it, and you can type an integer N here, to display the first or last N category/series values in the chart**.**
    3. If you want to sort the values based on other fields, select the **Based On** check box. Server displays the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009775101-Custom-Sort-Dialog-Box-Properties) dialog box for you to select fields and set the sort order for them.

       When you do not select **Based On**, Server sorts all category/series values or its first/last N values in the order you selected in the Category Order/Series Order box of the dialog box.
    4. If you have selected **Top N** or **Bottom N** from the **Select** drop-down list, you can select the **Remaining Categories**/**Series In** check box and then type a string in the text box, so that Server merges the category/series values beyond the first or last N range into the group with the name as the string.
    5. If you have selected **Top N** or **Bottom N** and you are specifying the Order/Select N condition for the category axis, you can also select **Overall Series** to calculate the top or bottom N category values based on the series values.
    6. If you have selected **Top N** or **Bottom N**, you can type a number M in the **Skip First** text box, then Server skips the first M category/series values, and the Select N condition begins with M+1. Server merges the skipped values into the Remaining Categories/Series group.
    7. Select **OK** to accept the settings.
11. Select **OK** to insert the chart.

**To create an organization chart:**

Organization chart, also referred to as org chart, is a one-root-node-tree-structure diagram showing the ownership or reporting to relations among the nodes that you map to a specific entity.

1. Repeat the above [steps 1 to 5](#Common) for creating a common chart.
2. In the **Primary Axis** box, select the **Org** chart type.

   ![Insert Chart dialog - Organization](https://devnet.logianalytics.com/hc/article_attachments/4404880177175/insrtcht_org.gif)
3. Select **Node** in the Primary Axis box, select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) or a detail object ![](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) from the Resources box, and select the add button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif). Server displays the values of the object as the nodes in the org chart.
4. Select **Parent** in the Primary Axis box, select a group object or a detail object from the Resources box and select the add button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) to define the ownership or reporting to relationship among the node field values. The parent field should be of the same data type as the node field but different from the node field. The values of the parent field should be a subset of those of the node field. For example, if the node field is Employee ID, the parent field can be the one about IDs showing which employ ID reports to which employ ID.
5. The **Properties** box displays a node model for specifying the information you want to display in each node in the org chart. You can add group objects, detail objects, labels, and images to display in the nodes. To add an object, select it in the Resources box and select the add button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) beside the Properties box. You can resize the node model and adjust the position and size of the added objects in the node model. To remove an unwanted object from the node model, select it and then select the remove button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif).
6. Select **OK** to insert the chart.

**To create a heat map:**

A heat map displays values by colors and sizes in a matrix. It is composed of several rectangles that are grouped by group objects. Each rectangle represents a value of a group object or a combination of values of multiple group objects.

1. Repeat the above [steps 1 to 5](#Common) for creating a common chart.
2. In the **Primary Axis** box, select the **Heat Map** chart type.

   ![Insert Chart dialog - Heat Map](https://devnet.logianalytics.com/hc/article_attachments/4404880177687/insrtcht_htmp.gif)
3. Add group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) into the **Area** box to create groups in the heat map.
4. You can use the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) and the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) to adjust the group levels. Each combination of the groups in all the group levels is represented by a rectangle in the heat map.
5. To remove a group, select it and then select the remove button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885336599/btn_rmvitem.gif).
6. If you want to customize the sort order and define Select N condition on a group, select it and select the Top N button ![Group Options button](https://devnet.logianalytics.com/hc/article_attachments/4404880176279/btn_wbrpt_topn.gif) above the Area box. Server displays the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009775881-Group-Options-Dialog-Box-Properties) dialog box. Specify the order and condition [the same as you do for the category/series axis](#SlctN).
7. Add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) into the **Property** box to define the properties of the rectangles.
8. In the **Area** and **Property** boxes, select the **Color By** check boxes for the objects that determine the fill color of the rectangles, and the **Label By** check boxes for the objects the values of which you want to display in the rectangles. You can select only one object in the Property box for Color By.
9. In the Property box, select an object's **Size By** check box to use it to determine the size of the rectangles. Server ignores the negative values of the size-by object when it generates the heat map.

**To create a real time chart:**

You can create real time charts using single bar, bench, line, and area chart types.

1. Repeat the above [steps 1 to 5](#Common) for creating a common chart.
2. In the **Primary Axis** box, select a chart type of bar, bench, line, or area, then add the detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) of numeric type as the data.
3. Select the **Real Time** check box.
4. To use the time at which the chart refreshes itself as the category value, select **Use System Time for Category**, and you can see the text **Use System Time for Category** in the category box.

   When you do not select the **Use System Time for Category** option, you can add another group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) to display on the category axis. If you want to customize the sort order and define Select N condition for values on the category axis, select the Top N button ![Category Options](https://devnet.logianalytics.com/hc/article_attachments/4404880176279/btn_wbrpt_topn.gif) above the category box, then [define the order and condition](#SlctN) in the Category Options dialog box.
5. In the **Refresh Interval** text box, specify the time interval at which the chart will get data and refresh itself automatically.
6. In the **Show Most Recent** text box, type the most recent N records to keep for the real time data in the chart.
7. Select **Incremental Fetch** to add the objects you want to use as the unique key of the real time chart in the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009776581-Unique-Key-Dialog-Box-Properties) dialog box.

   ![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880178071/unqkey.gif)

   Once you defined a unique key, each time when the chart automatically updates itself, Server filters the data that has the same unique key value as the previous loaded data records and only adds data with different unique key value to the chart. For instance, if you add the fields **Country** and **Product ID** as the unique key of a real time chart, when Server has already loaded a record with the product ID 1 in USA into the chart, it adds no more records of this product ID in USA to the real time chart because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key, Server updates the data in the chart each time new records are added to the database with more recent times.
8. Select **OK** to insert the chart.

**To create a motion chart:**

You can create motion charts using single chart of bar, bench and bubble types.

1. Repeat the above [steps 1 to 5](#Common) for creating a common chart.
2. In the **Primary Axis** box, select a chart type of bar, bench, or bubble, then add the required aggregation objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) or [additional values](#Value)![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404880175511/btn_wbrpt_adtnl.gif) as the data of the type.

   If you select the **Bubble** chart type, you need to specify the values for the bubble X axis and Y axis, as well as the value to determine the size of the bubbles, respectively. When you add a value for the bubble X axis, Server displays it on the category axis instead of that you specified for the category axis, while still including the value added to the category axis in data calculation.
3. Add a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) from the Resources box to display its values on the category or series axis of the chart. The labels of the two axes vary with different chart types, for example, they are X-Axis and Clustering for a clustered bar chart.
4. If you want to customize the sort order and define Select N condition for values on the category or series axis, select the Top N button ![Category/Series Options](https://devnet.logianalytics.com/hc/article_attachments/4404880176279/btn_wbrpt_topn.gif) above the category or series box, then [define the order and condition](#SlctN) in the Category/Series Options dialog box.
5. Select **Motion Bar for Playable Chart**.
6. Add a group object of Integer, Date, or Time type as the motion field. When the group object is of the Date data type, you can define special function for it by selecting **Special Function**.
7. Select **OK** to insert the chart.

When you created a motion chart, you can use the motion control section to make the chart move. Select the play button, and the chart shows its dynamic trend based on the value change of the motion field which is bound in the motion bar. To stop it, select the button again. You can also control its moving speed by dragging the slider between Slow and Fast on the speed control. For a bubble chart, you can control whether the chart will be moving in bubble or line trail.

## Inserting a Banded Object

1. Drag **Banded Object** from the Components panel or the banded object icon ![Drag to add banded object button](https://devnet.logianalytics.com/hc/article_attachments/4404885315607/btn_wbrpt_2bd.gif) from the visualization toolbar to the destination where you want to insert the banded object. Server displays the [Insert Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009775921-Insert-Banded-Object-Dialog-Box-Properties) dialog box.

   ![Insert Banded Object dialog - Detail tab](https://devnet.logianalytics.com/hc/article_attachments/4404880178327/insrtbd_dtl.gif)
2. Type a title for the banded object in the Banded Title text box.
3. Select the font button ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif) to set the font properties for the title.
4. From the **Data Source** drop-down list, select the business view using which to create the banded object.
5. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778741-Applying-Filters-in-Web-Report) to the business view to narrow down data in the banded object.
6. In the **Details** tab, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) from the Resources box to display as detail fields in the banded object.
7. To adjust the display order of the objects, select one and select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
8. By default, Server uses the display names of the added objects to label the corresponding detail columns. To edit the label text for a detail column, select in the Label text box and type a new one. If you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.
9. If you want to sort the detail data in the banded object by values of specified fields, select **Sort Fields By** and [set the sort manner](#Sort) in the Custom Sort dialog box.
10. In the **Group** tab, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) as the grouping criteria.
11. You can select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) to adjust the group levels.
12. In the **Sort** column select the sort manner of groups in each group level, which can be No Sort, Ascend, Descend, or [Custom Sort](#GroupSort).

    ![Insert Banded Object dialog - Group tab](https://devnet.logianalytics.com/hc/article_attachments/4404880178967/insrtbd_grp.gif)
13. In the **Summary** tab, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) to summarize data in the banded object as follows: in the right box, select the group to which to apply the aggregation, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level.
14. You can select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif) to adjust the order of the aggregations in the current group or move an aggregation to another group.

    ![Insert Banded Object dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4404880179479/insrtbd_sum.gif)
15. Select **OK** to insert the banded object.

## Inserting a KPI

1. Drag **KPI** from the Components panel or drag the KPI icon ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/4404885316119/btn_kpi.gif) from the visualization toolbar to the destination where you want to insert the KPI. Server displays the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009776221-Select-Data-Source-Dialog-Box-Properties#KPI) dialog box.
2. Select a data source and then a business view in the current catalog to bind with the KPI.

   ![Select Data Source for KPI dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885337111/slctdtsrc-kpi.gif)
3. Select **OK**.
4. Server inserts a blank KPI in the report. You can now define the KPI by adding objects into it.

   ![Blank KPI template](https://devnet.logianalytics.com/hc/article_attachments/4404880180247/wbrpt_edt_insrt_kpi.gif)
5. Drag an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009750082-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report-#DynamicFormula) from the Resources panel as the KPI value.
6. Server adds the name label of the object in the KPI at the same time. You can edit the label text.
7. Insert a KPI chart to demonstrate data about the KPI value as follows:
   1. Right-click in the blank area of the KPI and then select **Insert KPI Chart** from the shortcut menu. Server displays the [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009747582-Insert-Chart-Dialog-Box-Properties#KPI) dialog box.
   2. Type a title for the chart in the **Chart Title** text box.
   3. You can select the font button ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404885319959/btn_wbrpt_font.gif) to set the font properties for the title.
   4. The **Data Source** drop-down list shows the business view bound with the KPI. You cannot change it.
   5. Select the chart type for the KPI chart in the Primary Axis box. You can only select the following chart types for a KPI chart: Bar, Bench, Line, Area, Pie, and Bullet.
   6. Define the KPI chart [in the same way you would do for a general chart](#Chart).
   7. Select **OK**. Server inserts the chart into the KPI.
8. Add more aggregation objects, dynamic formulas, [labels](#Label), or [images](#Image) into the KPI if you want.
9. [Resize](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Resize) the KPI and the objects in it and [adjust the position](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components#Move) of the objects by dragging to improve the layout.

## Inserting a Label

1. Drag **Label** from the Components panel to the destination.
2. Double-click the label. When the text box becomes editable, type the desired text.
3. Select outside of the label to apply the change.

## Inserting an Image

1. Drag **Image** from the Components panel to the destination where you want to insert the image. Server displays the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009747622-Insert-Image-Dialog-Box-Properties) dialog box.

   ![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885337367/insrtimg.gif)
2. Specify the image you want to insert.
   * To use an image in the local file system, select **Local File**. Then select **Browse** to find the image.
   * To use an image on a website, select **Web URL**. Then type the image URL or paste the URL in the **File URL** text box.
   * To use an image in the image library of Web Report Studio, select **Library**. Then select the image in the **My Pictures** box.
3. Select **OK** to insert the image.

## Inserting a Web Control

You can insert the following web controls into a web report: parameter control, parameter form control, filter control, and navigation control. For more information, see [Using Web Controls in Web Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750222-Using-Web-Controls-in-Web-Report).

## Inserting a Special Field

To insert a special field into a web report, simply drag the special field from the Components panel to the destination in the report.

## Inserting a Multimedia Object

1. Drag **Multimedia Object** from the Components panel to the destination where you want to insert the multimedia object. Server displays the [Insert Multimedia](https://devnet.logianalytics.com/hc/en-us/articles/1500009747662-Insert-Multimedia-Dialog-Box-Properties) dialog box.

   ![Insert Multimedia dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880181143/insrtmultmda.gif)
2. Choose from the three multimedia object types: Flash, Real Media file, or Windows Media File.
3. In the **File Name/URL** text box, specify the full path of the multimedia object you want to insert or use the **Browse** button to find it if it is on your local disk. Or you can provide a URL for loading it from a website.
4. The **Plug-in Page** text box provides a default URL from which to download the player to play the inserted multimedia object on a web page.
5. In the **Properties** box, specify the properties for the multimedia object.
6. Select **OK** to insert the multimedia object.

## Inserting a Horizontal/Vertical Line

You can only insert a horizontal/vertical line into a banded object in a web report. To do this, just drag **Horizontal Line** or **Vertical Line** from the Components panel to the destination in the banded object.

## Inserting a Page Break

For a web report that is not laid out using tabular (you did not select the [Use Tabular](https://devnet.logianalytics.com/hc/en-us/articles/1500009750022-Creating-Web-Reports-Using-the-Wizard#Layout) check box when you created the report using Web Report Wizard), if you want a component in its report body to be placed in a new page when running or exporting the report in the formats that support page layout such as PDF and RTF, you can insert a page break above the component to achieve this. To insert a page break, drag **Page Break** from the Components panel to the destination.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778761-General-Operations-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778821-Making-Simple-Modifications-to-Web-Report-Components)
