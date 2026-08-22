---
title: "Inserting Components"
id: 1500009751501
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components
updated_at: 2021-07-25T07:18:34Z
---

# Inserting Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components)

# Inserting Components

You can insert components into a web report via the Components panel on the left of the Web Report Studio window.

The following table lists the report areas that are valid targets for the various components：

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

Select the following links to view the topics:

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

The procedure for inserting tables in a web report varies with the way using which you use to access Web Report Studio: [quick start way or traditional way](https://devnet.logianalytics.com/hc/en-us/articles/1500009724642-Web-Report-Studio#Way).

**To insert a table when Web Report Studio is in the quick start way**:

1. Drag ![Drag to add table button](https://devnet.logianalytics.com/hc/article_attachments/4404936721303/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table.
2. In the Select Data Source dialog box, [select a business view and define the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009751621-Quick-Start-with-a-Table-Report) as required.
3. Select **OK** to insert the table.

**To insert a table when Web Report Studio is in the traditional way:**

When Web Report Studio is in the traditional way, you can choose the table type as you want: [Group Above, Group Left, Group Left Above](#Group) or [Summary Table](#Summary).

* **Inserting a group table**
  1. Drag ![Drag to add table button](https://devnet.logianalytics.com/hc/article_attachments/4404936721303/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table. Report Server displays the [Insert Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009749121-Insert-Table) dialog box.

     ![Insert Table dialog - Details tab](https://devnet.logianalytics.com/hc/article_attachments/4404942462999/insrttbl_dsply.gif)
  2. Specify a title for the table in the Table Title text box and select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to set the font properties for the title.
  3. From the Data Source drop-down list, select the business view using which to create the table. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters) to the business view to narrow down data displayed in the table.

     When the table is to be inserted into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel and group footer panel, it by default [inherits data](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components#Inherit) from the business view used by the parent banded object (<Inherit from the Parent> is selected in the Data Source drop-down list by default). You can select another business view to create the table if you want.
  4. Select a group type from the table type drop-down list: Group Above, Group Left, or Group Left Above.
  5. In the Details tab, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources box to be displayed as detail fields in the table. To adjust the display order of the objects, select one and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif). By default the display names of the added objects will be used to label the corresponding detail columns; to edit the label text for a detail column, select in the Label text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.
  6. If you want to sort the detail data in the table by values of specified fields, select the **Sort Fields By** button and set the sort manner in the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009748201-Custom-Sort) dialog box.

     ![Custom Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936738583/cstmsrt.gif)

     1. From the Resources box select an object in the current business view and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) to add it to the right box as the sort-by field.
     2. Select a sort order from the Sort column. Detail data in the table will be sorted based on values of the sort-by field in ascending or descending order.
     3. Repeat the above two steps to add more sort-by fields.
     4. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) to adjust the order of the sort-by fields, which will determines the sort priority of the fields.
     5. Select **OK** to accept the sort settings.
  7. In the Group tab, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) as the grouping criteria. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) to adjust the group levels. In the Sort column specify the sort manner of groups in each group level, which can be No Sort, Ascend, Descend, or [Custom Sort](#GroupSort).

     ![Insert Table dialog - Group tab](https://devnet.logianalytics.com/hc/article_attachments/4404942463255/insrttbl_grp.gif)

     **To customize the sort manner of a group:**

     1. Select **Custom Sort** as the sort manner for the group. Report Server displays the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009748201-Custom-Sort) dialog box.

        ![Custom Sort dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936738583/cstmsrt.gif)
     2. From the Resources box select an object in the current business view and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) to add it to the right box as the sort-by field.
     3. Select a sort order from the Sort column. Then the groups at this group level will be sorted by the values of the first record in each group on the related field based on the defined sort direction.
     4. Repeat the above two steps to add more sort-by fields.
     5. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) to adjust the order of the sort-by fields, which will determines the sort priority of the fields.
     6. Select **OK** to accept the sort settings.
  8. In the Summary tab, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) to summarize data in the table as follows: in the right box, specify the group to which the aggregation will be applied, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)to adjust the order of the aggregations in the current group or move an aggregation to another group. For the Group Left table, you can use the Row and Column columns to control the position of the aggregations in the table.

     ![Insert Table dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4404942463511/insrttbl_sum.gif)
  9. Select **OK** to insert the table.
* **Inserting a summary table**  
   Summary tables are used for showing group and summary information so they can only contain group and aggregation objects. In a summary table, the groups on the left have higher group levels than those on the right and calculation of the aggregation objects is always based on the innermost group no matter where they are positioned in the table.
  1. Drag ![Drag to add table button](https://devnet.logianalytics.com/hc/article_attachments/4404936721303/btn_wbrpt_2tbl.gif) from the visualization toolbar or **Table** from the Components panel to the destination where you want to insert the table. Report Server displays the [Insert Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009749121-Insert-Table) dialog box.
  2. Specify a title for the table in the Table Title text box and select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to set the font properties for the title.
  3. From the Data Source drop-down list, select the business view using which to create the table. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters) to the business view to narrow down data displayed in the table.

     When the table is to be inserted into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel and group footer panel, it by default [inherits data](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components#Inherit) from the business view used by the parent banded object (<Inherit from the Parent> is selected in the Data Source drop-down list by default). You can select another business view to create the table if you want.
  4. Select **Summary Table** from the table type drop-down list.
  5. In the Columns tab, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) and aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) in the specified business view from the Resources box to display in the table. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) to adjust the display order of the added objects. The order of the group objects determines the group levels in the table: the topmost group object the highest group level and the lowest group object the innermost group level. All the aggregations are parallel and calculated based on the lowest group. In the Sort column specify the sort manner of groups in each group level, which can be No Sort, Ascend, Descend, or [Custom Sort](#GroupSort).

     ![Insert Table dialog - Columns tab](https://devnet.logianalytics.com/hc/article_attachments/4404936739095/insrttbl_clmn.gif)
  6. In the Summary tab, you can insert the aggregation objects selected in the Columns tab to the table header/footer and to the group headers/footers of existing groups. First select an aggregation object in the Resources box, then select the check boxes representing the required locations.
     The aggregation will be placed in the intersection of its summary column and the table/group header/footer row.

     ![Insert Table dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4404942463767/insrttbl_sum1.gif)
  7. Select **OK** to insert the table.

## Inserting a Crosstab

1. Drag **Crosstab** from the Components panel or ![Drag to add crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404936721559/btn_wbrpt_2crstb.gif) from the visualization toolbar to the destination where you want to insert the crosstab. Report Server displays the [Insert Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009748981-Insert-Crosstab) dialog box.

   ![Insert Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936739351/insrtcrstb_data.gif)
2. Specify a title for the crosstab in the Crosstab Title text box and select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to set the font properties for the title.
3. From the Data Source drop-down list, select the business view using which to create the crosstab. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters) to the business view to narrow down data displayed in the crosstab.

   When the crosstab is to be inserted into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel and group footer panel, it by default [inherits data](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components#Inherit) from the business view used by the parent banded object (<Inherit from the Parent> is selected in the Data Source drop-down list by default). You can select another business view to create the crosstab if you want.
4. In the Data tab, select a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) or ![Add Row button](https://devnet.logianalytics.com/hc/article_attachments/4404936739735/btn_addrow.gif) to add it as a column or row group in the crosstab from the Resources box. In the Sort column, specify the sort manner of the group.
5. Select an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or a detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) and select ![Add Summary button](https://devnet.logianalytics.com/hc/article_attachments/4404942464023/btn_addsum.gif) to add it to the Summaries box as an aggregate field to create aggregations in the crosstab. If a detail object is added, specify the aggregate function for it from the Aggregation drop-down list. When DistinctSum is selected as the function, you should select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) next to the Distinct On text box to specify one or more detail objects according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields) dialog box. You can specify a comparison function for the aggregate field.

   **To define comparison function for an aggregate field:**

   1. Select the aggregate field in the Summaries box and select the **Comparison Function** button. Report Server displays the [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009721362-Comparison-Function) dialog box.

      ![Comparison Function dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936739991/cmprsnfctn.gif)
   2. From the Function drop-down list, select the required function: Percentage, Permillage or Difference.
   3. Specify a position for the comparison function.
      * **Comparison Function Spans on Row Direction**  
         The comparison function will be placed into the column total cell of the crosstab.
      * **Comparison Function Spans on Column Direction**  
         The comparison function will be placed into the row total cell of the crosstab.
   4. Numbers that form the calculation of the comparison function are determined by the Break By and Refer To drop-down lists.

      Items in the Break by drop-down list vary based on the position of the comparison function. It specifies the first parameter of the comparison function: the detail aggregation in the crosstab (Aggregate) or the subtotal of a specified row/column group.

      Items in the Refer to drop-down list also vary according to what you have selected from the Break by drop-down list. It specifies the other parameter of the comparison function: the grand total or subtotal for an outer row/column group.
   5. Select **OK** and you can see that a new object is added into the Summaries box. Set the label text for the object in the Label column as required.
6. For each column/row/summary field, you can select in the Label text box and type a name to label the corresponding column header/row header/summary, or select the **Auto Map Field Name** check box beside the text box if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field (when the text box is blank and the check box is not selected, no label will be created).
7. Add more column/row groups and aggregate fields to display in the crosstab. To adjust the display order of the fields, select a field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif); to remove an unwanted field, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).
8. In the Layout tab, specify the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009748981-Insert-Crosstab#Layout) for the crosstab.

   ![Insert Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936740247/insrtcrstb_layout.gif)
9. Select **OK** to insert the crosstab.

**Tip:** When you create a crosstab with wizard, by default there will be no labels generated for its columns, rows and summaries (the Label columns in the Columns, Rows and Summaries boxes of the wizard are blank by default). You can make Web Report Studio automatically provide the labels which by default are the display names of the added objects by setting the [profile options](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#Crosstab) Add Labels for Crosstab Rows and Columns and Add Labels for Crosstab Summaries. You can also customize the profile option Display Crosstab Summaries Vertically to make the summaries in crosstabs displayed horizontally in Web Report Studio.

## Inserting a Chart

Normally, a chart displays values in a static way and you cannot change the values on it once it is created. However, Logi Report provides you with options to make the chart interactive and dynamic. For example, if your data source uses data that changes quickly over time such as stock market values, you can create a real time chart, so that the chart will update itself based on a defined interval using the real time data from the data source. You can make a chart move at runtime based on the value changes of a motion field by creating a motion chart. In a motion chart, the chart is playable. You can start or stop the chart to play the dynamic trend of the motion field, control the moving speed of the chart, and if you create a bubble motion chart, you can even use a trail control to make the chart move showing a bubble or line trail.

In Web Report Studio, when you create a chart, you can choose to make it a [common chart](#Common), an [organization chart](#Org), a [heat map](#Heatmap), a [real time chart](#RealTime), or a [motion chart](#Motion).

**To create a common chart:**

1. Drag **Chart** from the Components panel or a chart icon from the visualization toolbar to the destination where you want to insert the chart. Report Server displays the [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009748941-Insert-Chart) dialog box.

   ![Insert Chart dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942464279/insrtcht.gif)
2. Specify a title for the chart in the Chart Title text box and select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to set the font properties for the title.
3. From the Data Source drop-down list, select the business view using which to create the chart. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters) to the business view to narrow down data displayed in the chart.

   When the chart is to be inserted into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel and group footer panel, it by default [inherits data](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components#Inherit) from the business view used by the parent banded object (<Inherit from the Parent> is selected in the Data Source drop-down list by default). You can select another business view to create the chart if you want.
4. To create a single chart, in the Primary Axis box, select the required chart type from the chart type drop-down list.

   To create a combo chart, select**![Add Combo Chart](https://devnet.logianalytics.com/hc/article_attachments/4404936740503/btn_wbrpt_adcmbtyp.gif)** above the Primary Axis box and an additional chart type will be added. You can replace the additional chart type by selecting the required one from the chart type drop-down list. Repeat this to add more chart types. Select the **Secondary Axis** check box if you want to have the secondary axis (Y2) and define the chart types on the axis as required. To delete a type, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).
5. In the Primary Axis or Secondary Axis box, select a chart type and add an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif), a numeric detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif), or an [additional value](#Value)![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404936740759/btn_wbrpt_adtnl.gif) as the value of the type. You can add more than one value to a chart type. Each added chart type shall have at least one value.

   If you select the Bubble chart type, you need to specify the values for the bubble X axis and Y axis and the value to determine the size of the bubbles respectively. When a value is added for the bubble X axis, it will be displayed on the category axis instead of that specified for the category axis, while the value added to the category axis will still be included in data calculation.

   ![Bubble Value](https://devnet.logianalytics.com/hc/article_attachments/4404936741015/wbrpt_edt_insrt_bblcht.gif)

   **To add an additional value to a chart type:**

   1. Select the chart type in the value box.
   2. In the Resources box, expand the **Additional Values** node, then select **Constant Value**/**Average Value**.
   3. Select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) beside the value box. Report Server displays the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009721502-Edit-Additional-Value) dialog box.
   4. In the Name text box, specify the display name for the constant/average value.
   5. Type the constant value with numeric type in the Value text box, or select a field based on which the average value will be calculated from the Based On drop-down list.
   6. Select **OK**, and the defined constant/average value will be added to the chart type.

      To modify a constant/average value, select the value in the value box, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936735255/btn_wbrpt_edit.gif). In the Edit Additional Value dialog box, edit the value as required.
6. Add a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) or a detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) from the Resources box to display it on the category axis of the chart. Add a group object to display on the series axis. The box names of the two axes vary with different chart types, for example, they are X-Axis and Clustering for a clustered bar chart.
7. If you want to customize the sort order and define Select N condition for values displayed on the category/series axis of the chart, select ![Category/Series Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936741271/btn_wbrpt_topn.gif) above the axis box, then define the order and condition in the [Category Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009721462-Category-Options) dialog box or [Series Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009749301-Series-Options) dialog box.
   1. In the Category Order/Series Order box, specify in which order values of the category/series field will be sorted.

      ![Category Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936741527/ctgryoptn.gif)
   2. In the Category Selection/Series Selection box, specify the Select condition to All, Top N or Bottom N. If All is selected, all category/series values will be shown in the chart; if Top N or Bottom N is selected, the text box next to it is activated and you can specify an integer here, which means that the first or last N category/series values will be shown in the chart**.**
   3. Select the **Based On** check box and set the two drop-down lists that follow according to your requirement.

      If Based On is unselected, all category/series values or its first/last N values will be sorted in the order you specify in the Category Order/Series Order box of the dialog box; if you select it, you can make the values sorted based on a field added to the value axis of the chart and select a sort order as you want. When Custom Sort is selected from the Based On drop-down list, you can customize based on which fields to sort the values and set the sort order for each sort-by field using the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009748201-Custom-Sort) dialog box.
   4. If you have selected Top N or Bottom N from the Select drop-down list, you can select the **Remaining Categories**/**Series In** check box and then type a string in the text box, so that the category/series values beyond the first or last N range will be merged into the group with the name as the string.
   5. If you are specifying the Order/Select N condition for the category axis, you can also select **Overall Series** to calculate the top or bottom N category values based on the series values.
   6. You can type a number M in the Skip First text box, then the first M category/series values will be skipped and the Select N condition will begin with M+1. The skipped values will be merged into the Remaining Categories/Series group.
   7. Select **OK** to accept the settings.
8. Select **OK** to insert the chart.

**To create an organization chart:**

Organization chart, also referred to as org chart, is a one-root-node-tree-structure diagram showing the ownership or reporting to relations among the nodes which are mapped to a specific entity.

1. Repeat the above [steps 1 to 3](#Common)  for creating a common chart.
2. In the Primary Axis box, select the **Org** chart type.

   ![Insert Chart dialog - Organization](https://devnet.logianalytics.com/hc/article_attachments/4404936741783/insrtcht_org.gif)
3. Select **Node** in the Primary Axis box, select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) or a detail object ![](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) from the Resources box and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif). The values of the object will be displayed as the nodes in the org chart.
4. Select **Parent** in the Primary Axis box, select a group object or a detail object from the Resources box and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) to define the ownership or reporting to relationship among the node field values. The parent field should be of the same data type as the node field but different from the node field. The values of the parent field should be a subset of those of the node field. For example, if the node field is Employee ID, the parent field can be the one about IDs showing which employ ID reports to which employ ID.
5. The Properties box displays a node model for specifying the information you want to display in each node in the org chart. You can add group objects, detail objects, labels, and images to display in the nodes. To add an object, select it in the Resources box and select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) beside the Properties box. You can resize the node model and adjust the position and size of the added objects in the node model as required. To remove an unwanted object from the node model, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936742039/btn_rmvitem.gif).
6. Select **OK** to insert the chart.

**To create a heat map:**

A heat map displays values by colors and sizes in a matrix. It is composed of several rectangles that are grouped by group objects. Each rectangle represents a value of a group object or a combination of values of multiple group objects.

1. Repeat the above [steps 1 to 3](#Common)  for creating a common chart.
2. In the Primary Axis box, select the **Heat Map** chart type.

   ![Insert Chart dialog - Heat Map](https://devnet.logianalytics.com/hc/article_attachments/4404942464535/insrtcht_htmp.gif)
3. Add group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) into the Area box to create groups in the heat map. You can use ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) to adjust the group levels. Each combination of the groups in all the group levels is represented by a rectangle in the heat map.
   To remove a group, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).
4. If you want to customize the sort order and define Select N condition on a group, select it and select ![Group Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936741271/btn_wbrpt_topn.gif) above the Area box. In the [Group Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009748841-Group-Options) dialog box, specify the order and condition [the same as you do for the category/series axis](#SlctN).
5. Add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) into the Property box to define the properties of the rectangles.
6. In the Area and Property boxes, select the **Color By** check boxes for the objects that are used to determine the fill color of the rectangles, and the **Label By** check boxes for the objects the values of which you want to display in the rectangles. Only one object in the Property box can be used for Color By. In the Property box, select an object's **Size By** check box to use it to determine the size of the rectangles. The negative values of the size-by object will be ignored when the heat map is generated.

**To create a real time chart:**

Real time chart is supported on single bar, bench, line, and area chart types.

1. Repeat the above [steps 1 to 3](#Common)  for creating a common chart.
2. In the Primary Axis box, select a chart type of bar, bench, line, or area, then add the detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif)of numeric type as the data of the type.
3. Select the **Real Time** check box.
4. By default, Use System Time for Category is selected and you can see the text Use System Refresh Time in the category box, which means the time at which the chart refreshes itself will be used as the category value. You can clear the Use System Time for Category option and add another group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) to display on the category axis. If you want to customize the sort order and define Select N condition for values on the category axis, select ![Category Options](https://devnet.logianalytics.com/hc/article_attachments/4404936741271/btn_wbrpt_topn.gif) above the category box, then [define the order and condition](#SlctN) in the Category Options dialog box.
5. In the Refresh Interval text box. specify the time interval at which the chart will get data and refresh itself automatically.
6. In the Show Most Recent text box, specify the most recent N records to be kept for the real time data on the chart.
7. Select the **Incremental Fetch** button to add the objects you want to use as the unique key of the real time chart in the [Unique Key](https://devnet.logianalytics.com/hc/en-us/articles/1500009749541-Unique-Key) dialog box.

   ![Unique Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936742295/unqkey.gif)

   Once a unique key is defined, each time when the chart automatically updates itself, the data that has the same unique key value as the previous loaded data records will be filtered and only data with different unique key value will be added to the chart. For instance, if you add the fields Country and Product ID as the unique key of a real time chart, when a record with the product ID 1 in USA has already been loaded into the chart, no more records of this product ID in USA will be added to the real time chart because they have the same unique key value. The most common usage is with a time field so when a time is part of the unique key the data in the chart will be updated each time new records are added to the database with more recent times.
8. Select **OK** to insert the chart.

**To create a motion chart:**

Motion chart is supported on single chart of bar, bench and bubble types.

1. Repeat the above [steps 1 to 3](#Common)  for creating a common chart.
2. In the Primary Axis box, select a chart type of bar, bench or bubble, then add the required aggregation objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or [additional values](#Value)![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404936740759/btn_wbrpt_adtnl.gif) as the data of the type.

   If you select the Bubble chart type, you need to specify the values for the bubble X axis and Y axis, as well as the value to determine the size of the bubbles respectively. When a value is added for the bubble X axis, it will be displayed on the category axis instead of that specified for the category axis, while the value added to the category axis will still be included in data calculation.
3. Add a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources box to display its values on the category or series axis of the chart. The box names of the two axes vary with different chart types, for example, they are X-Axis and Clustering for a clustered bar chart.
4. If you want to customize the sort order and define Select N condition for values on the category or series axis, select ![Category/Series Options](https://devnet.logianalytics.com/hc/article_attachments/4404936741271/btn_wbrpt_topn.gif) above the category or series box, then [define the order and condition](#SlctN) in the Category/Series Options dialog box.
5. Select **Motion Bar for Playable Chart**, add a group object of Integer, Date or Time type as the motion field. When the group object is of the Date data type, you can define special function for it by selecting the Special Function button.
6. Select **OK** to insert the chart.

When a motion chart is created, you can use the motion control section to make the chart move. Select the play button and the chart will show its dynamic trend based on the value change of the motion field which is bound in the motion bar. To stop it, select the button again. You can also control its moving speed by dragging the slider between Slow and Fast on the speed control. For a bubble chart, you can control whether the chart will be moving in bubble or line trail.

## Inserting a Banded Object

1. Drag **Banded Object** from the Components panel or ![Drag to add banded object button](https://devnet.logianalytics.com/hc/article_attachments/4404942449687/btn_wbrpt_2bd.gif) from the visualization toolbar to the destination where you want to insert the banded object. Report Server displays the [Insert Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009748901-Insert-Banded-Object) dialog box.

   ![Insert Banded Object dialog - Detail tab](https://devnet.logianalytics.com/hc/article_attachments/4404936742551/insrtbd_dtl.gif)
2. Specify a title for the banded object in the banded Title text box and select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to set the font properties for the title.
3. From the Data Source drop-down list, select the business view using which to create the banded object. You can select the **Filter** button to [add filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters) to the business view to narrow down data displayed in the banded object.
4. In the Details tab, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources box to be displayed as detail fields in the banded object. To adjust the display order of the objects, select one and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif). By default the display names of the added objects will be used to label the corresponding detail columns; to edit the label text for a detail column, select in the Label text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.
5. If you want to sort the detail data in the banded object by values of specified fields, select the **Sort Fields By** button and [set the sort manner](#Sort) in the Custom Sort dialog box.
6. In the Group tab, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) as the grouping criteria. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif) to adjust the group levels. In the Sort column specify the sort manner of groups in each group level, which can be No Sort, Ascend, Descend, or [Custom Sort](#GroupSort).

   ![Insert Banded Object dialog - Group tab](https://devnet.logianalytics.com/hc/article_attachments/4404942464791/insrtbd_grp.gif)
7. In the Summary tab, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) to summarize data in the banded object as follows: in the right box, specify the group to which the aggregation will be applied, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)to adjust the order of the aggregations in the current group or move an aggregation to another group.

   ![Insert Banded Object dialog - Summary tab](https://devnet.logianalytics.com/hc/article_attachments/4404936742807/insrtbd_sum.gif)
8. Select **OK** to insert the banded object.

## Inserting a KPI

1. Drag **KPI** from the Components panel or drag ![KPI button](https://devnet.logianalytics.com/hc/article_attachments/4404936743063/btn_kpi.gif) from the visualization toolbar to the destination where you want to insert the KPI.
2. In the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009722222-Select-Data-Source#KPI) dialog box, select a data source and then a business view in the current catalog to bind with the KPI. Select **OK**.

   ![Select Data Source for KPI dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942465047/slctdtsrc-kpi.gif)
3. A blank KPI is inserted in the report. You can now define the KPI by adding objects into it.

   ![Blank KPI template](https://devnet.logianalytics.com/hc/article_attachments/4404936743319/wbrpt_edt_insrt_kpi.gif)
4. Drag an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-#DynamicFormula) from the Resources panel as the KPI value. The name label of the object is added in the KPI at the same time. You can edit the label text.
5. Insert a KPI chart to demonstrate data about the KPI value.
   1. Right-click in the blank area of the KPI and then select **Insert KPI Chart** from the shortcut menu. Report Server displays the [Insert Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009748941-Insert-Chart#KPI) dialog box.
   2. Specify a title for the chart in the Chart Title text box, and you can select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to set the font properties for the title.
   3. The Data Source drop-down list shows the business view bound with the KPI. It cannot be changed.
   4. Select the type for the KPI chart. Only the following chart types are supported for a KPI chart: Bar, Bench, Line, Area, Pie, and Bullet.
   5. Define the KPI chart [in the same way you would do for a general chart](#Chart).
   6. Select **OK**. A chart is now inserted into the KPI.
6. Add more aggregation objects, dynamic formulas, [labels](#Label) or [images](#Image) into the KPI if you want.
7. [Resize](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components#Resize) the KPI and the objects in it and [adjust the position](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components#Move) of the objects by dragging to improve the layout.

## Inserting a Label

1. Drag **Label** from the Components panel to the destination.
2. Double-click the label, when the text box becomes editable type the desired text.
3. Select outside of the label to apply the change.

## Inserting an Image

1. Drag **Image** from the Components panel to the destination where you want to insert the image. Report Server displays the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009722002-Insert-Image) dialog box.

   ![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936743575/insrtimg.gif)
2. Specify the image you want to insert.
   * To use an image in the local file system, select **Local File**, then select **Browse** to find the image.
   * To use an image on a website, select **Web URL**, then type the image URL or paste the URL in the Image URL text box.
   * To use an image in the image library of Web Report Studio, select **Library**, then select the image in the My Images box.
3. Select **OK** to insert the image.

## Inserting a Web Control

You can insert the following web controls into a web report: parameter control, parameter form control, filter control, and navigation control. For details, see [Using Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009751581-Using-Web-Controls).

## Inserting a Special Field

To insert a special field into a web report, just drag the special field from the Components panel to the destination in the report.

## Inserting a Multimedia Object

1. Drag **Multimedia Object** from the Components panel to the destination where you want to insert the multimedia object. Report Server displays the [Insert Multimedia](https://devnet.logianalytics.com/hc/en-us/articles/1500009749041-Insert-Multimedia) dialog box.

   ![Insert Multimedia dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936743831/insrtmultmda.gif)
2. Choose from the three multimedia object types: Flash, Real Media file, or Windows Media File.
3. In the File Name/URL text box, specify the full path of the multimedia object you want to insert or use the Browse button to find it if it is on your local disk. Or you can provide a URL for loading it from a website.
4. The Plug-in page text box provides a default URL from which to download the player to play the inserted multimedia object on a web page.
5. In the Properties box, specify the properties for the multimedia object as required.
6. Select **OK** to insert the multimedia object.

## Inserting a Horizontal/Vertical Line

A horizontal/vertical line can only be inserted into a banded object in a web report. To do this, just drag **Horizontal Line** or **Vertical Line** from the Components panel to the destination in the banded object.

## Inserting a Page Break

For a web report that is not laid out using tabular (the [Use Tabular](https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard#Layout) check box is not selected in the Web Report Wizard), if you want a component in its report body to be placed in a new page when running or exporting the report in the formats that support page layout such as PDF, RTF, and so on, you can insert a page break above the component to achieve this. To insert a page break, drag **Page Break** from the Components panel to the destination.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components)
