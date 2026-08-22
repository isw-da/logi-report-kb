---
title: "Manipulating Data Components"
id: 1500009675261
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components
updated_at: 2021-07-24T20:53:35Z
---

# Manipulating Data Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650322-Binding-Links-to-Objects)

# Manipulating Data Components

You can manipulate data components, which refer to tables, crosstabs, charts, KPI components, and geographic maps, in Web Report Studio, as shown below. Note that, most of the manipulations require selecting the component first. To select a component, hover the mouse pointer on the component, when the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) appears at its upper left corner, select the icon.

Below is a list of the sections covered in this topic:

* [Manipulating a Table](#Table)
* [Manipulating a Crosstab](#Crosstab)
* [Manipulating a Chart](#Chart)
* [Manipulating a KPI Component](#KPI)
* [Manipulating Geographic Map Group Markers/Areas](#Map)
* [Converting Between Table/Crosstab/Chart Using Visualization Toolbar](#ConvertVT)

## Manipulating a Table

* **Changing the table definition** 
  1. Select the table and do one of the following:
     + Select **Menu** > **Edit** > **Wizard**.
     + Select the **Table Wizard** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920367127/btn_wbrpt_wizard.gif) on the visualization toolbar.
     + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the table and select **Table Wizard** from the shortcut menu.

     The [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009672621-Table-Wizard) appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373271/tblwzd_dsply.gif)
  2. In the Table Title text field, edit the title of the table. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. Select the **Filter** button to apply some filter conditions to narrow down data displayed in the table.
  4. Define the data displayed in the table.
     + When the table is one of the types: Group Left, Group Above, or Group Left Above,
       - In the Details tab, add or change the fields displayed in the table.
       - In the Group tab, modify the grouping criteria of the table.
       - In the Summary tab, modify the summary fields of the table.
     + When the table type is Summary Table:
       - In the Columns tab, change the fields you want to display in the table.
       - In the Summary tab, add or edit the aggregations in the header/footer rows of the table and groups.
  5. Upon finishing, select **OK** to apply the modifications.

  Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components#Table) for more information about how to define a table.
* **Switching table column fields**  
   In addition to the above method, another more convenient way to change the fields displayed in the detail columns or group columns of a table is by using the Switch command.
  + **To change the field in a detail column:**  
     Select anywhere in the column, then select the arrow button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Right-select on the column and select **Switch Column** from the shortcut menu. The fields available for the detail column are listed in the submenu with the current used field checked. Select the field you want to use to replace the current one in the column.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404926635671/wbrpt_manplt_table1.gif)
  + **To change the field in a group column:**  
     Right-select the group field and select **Switch Group**  from the shortcut menu. The fields available for the group column are listed in the submenu with the current used field checked. Select the field you want to use to replace the current one in the column.
* **Adding a table column or group row by dragging**  
   To drag a field into a table to become a table column, drag it from the Resources panel and then move the mouse pointer on the column header to the border of an existing table column until a highlighted vertical line appears, then release the mouse, and the new column will be placed where the highlighted line lies.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926635927/wbrpt_manplt_table3.gif)

  To drag a group field into a table to become a group row, drag it from the Resources panel and then move the mouse pointer in the detail section or to the border of an existing table group row until a highlighted horizontal line appears, then release the mouse, and the new group row will be placed where the highlighted line lies.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926636183/wbrpt_manplt_table4.gif)
* **Removing a table column or group by dragging**  
   To remove a table column, select anywhere in the column, then select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Drag and drop the column to the Resources panel. Confirm the removal in the displayed dialog.

  To remove a group, select any value of the group, then select the arrow button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920374423/btn_wbrpt_slctrow.gif) that appears at the leftmost on the row to select the group row. Drag and drop the row to the Resources panel. Confirm the removal in the displayed dialog.
* **Adjusting order of columns in a table**  
   The order of columns in a table can be easily adjusted. To do this, select anywhere in a column, then select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Drag the column to the left or right boundary of another column, when a highlighted line appears along the column boundary, release the mouse button, and you can see the order changes.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920374679/wbrpt_manplt_table7.gif)
* **Adjusting the width of table columns according to contents**  
  When the contents in cells of a table column need more space to completely display, you can adjust the width of the table column according to the contents. To do this, select anywhere in the column, then select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Right-select on the column and select **Autofit** on the shortcut menu. It takes effect only when the property Autofit for the field or label in the column is also set to true.
* **Aggregating on a detail column**  
   You can summarize the data in a detail column. To do this:
  1. Do either of the following:
     + Right-select any value in the detail column and select **Aggregate On** from the shortcut menu.
     + Select anywhere in the column, then select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. On the toolbar, select the **Aggregate On** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920364183/btn_wbrpt_agrgton.gif).
  2. In the [Aggregate On](https://devnet.logianalytics.com/hc/en-us/articles/1500009647042-Aggregate-On) dialog, specify a function from the Function drop-down list to summarize the data.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920375063/agrgton.gif)
  3. When done, select **OK**.
     + If the table has groups, you will find data in each group level and the whole table are summarized respectively in the column.
     + If the table has no groups, the summary will be based on the whole table.

  When you finish summarizing a detail column, you will find a [dynamic aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-) is created at the same time which is given a default name Function\_DetailFieldName in the Dynamic Resource > Aggregations list in the Resources panel and you can use it again in the current report if required.
* **Show/Hiding table columns**  
   There are the following ways to show/hide a table column:
  + To show/hide a column, right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the table, then on the shortcut menu, select/unselect the column names from the Show > Table Column submenu to show/hide them.
  + To hide a column, select anywhere in the column, select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) appearing on the column header to select the column, then right-click on the column and select **Hide**.
  + To show/hide a detail column, select the table, then on the toolbar, select the **Show/Hide Detail** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920363543/btn_wbrpt_dtlclm.gif). From the drop-down list, select/unselect the field name to show/hide its detail column.
  + To show/hide a summary column, from a table, select the table and then select the **Show/Hide Summary** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920363799/btn_wbrpt_sum.gif). From the drop-down list, select/unselect the aggregation field name to show/hide the corresponding summary.
* **Showing/Hiding the headers/footers and detail in a table**  
   Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the table, then on the shortcut menu, select/unselect the corresponding names from the Show > Table Header/Table Footer/Table Detail/Table Group Header/Table Group Footer submenu to show/hide them.
* **Adding/Removing groups in a table**  
   You can add more groups into a table or remove the groups that are not required from a table.
  + **To add a group into a table:**  
     Select the table, then on the toolbar, select the **Add/Remove Group** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926630551/btn_wbrpt_adrmvgrp.gif) and you will get a drop-down list of fields in the business view that can be used as group by fields. From the list you can select the field you would like to add into the table as a group. If there is no existing group in the table, the added group will be placed at the left-above position. If the table already contains groups, the new group will be added as the highest level group and follow the same position pattern as the closest existing group.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404920375447/wbrpt_manplt_table11.gif)
  + **To remove a group from a table:**Right-select any value of the group and select **Delete** from the shortcut menu, then select **Yes** in the message dialog to confirm the removal. Or first select the table, then use the Add/Remove Group button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926630551/btn_wbrpt_adrmvgrp.gif) on the toolbar: unselect the group you want to remove from the drop-down list, then select **Yes** in the message dialog.
* **Showing/Hiding summary fields in header/footer rows in a summary table**   
   When creating or editing a summary table via the table wizard, once you have placed any aggregation field on its table header/footer or group header/footer, after the table is generated the Show Summary Field command is activated on the shortcut menu of all the summary columns in the table. You can use the menu command to show or hide the aggregation fields in the header/footer rows. To do this, select anywhere in the summary column that contains the required aggregation field, select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373783/btn_wbrpt_slctclmn.gif) appearing on the column header to select the column, then right-click on the column and from the Show Summary Field submenu select/deselect the corresponding table/group header/footer to show/hide the aggregation field on the specified locations.

* **Customizing the field value data format**  
   To customize the data format of the values of a field in a table, right-click on any value of the field, then select a format from the Format submenu, or input a format in the text box at the bottom of the submenu and select **Enter** on the keyboard.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920376343/wbrpt_manplt_table17.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating a Crosstab

* **Changing the crosstab definition**
  1. Select the crosstab and then do one of the following:
     + Select **Menu** > **Edit** > **Wizard**.
     + Select the **Crosstab Wizard** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920367127/btn_wbrpt_wizard.gif) on the visualization toolbar.
     + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the crosstab and select **Crosstab Wizard** from the shortcut menu.

     The [Crosstab Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009647122-Crosstab-Wizard) appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920376599/crstbwzd.gif)
  2. In the Crosstab Title text field, edit the title of the crosstab. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. Select the **Filter** button to apply some filter conditions to narrow down data displayed in the crosstab.
  4. Change the fields and summaries used by the crosstab.
  5. Upon finishing, select **OK** to apply the modifications.

  Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components#Crosstab) for more information about how to define a crosstab.
* **Switching crosstab fields**  
   In addition to the above method, another more convenient way to change the fields in a crosstab is by using the Switch command. To do this, right-click a row header/column header/summary and select **Switch Row**/**Switch****Column**/**Switch Summary** from the shortcut menu. The fields available for the row/column/summary are listed in the submenu with the current used field checked. Select the field you want to use to replace the current one.
* **Adding or removing row/column headers by dragging**  
   To drag a group field into a crosstab to become a column header, drag it from the Resources panel and then move the mouse pointer to a border of a column header until a highlighted horizontal line appears, then release the mouse.

  ![Add Column Header image](https://devnet.logianalytics.com/hc/article_attachments/4404920376983/wbrpt_manplt_crstb2.gif)

  + When the crosstab has no column/row/summary labels, the new column header will be directly placed where the highlighted line lies.
  + When you have specified any labels to label the columns/rows/summaries in the crosstab using wizard, the [Insert Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009672141-Insert-Column) dialog appears. You can specify a label to label the new column header if necessary. Select **OK** and the new column header will be placed where the highlighted line lies.

    ![Insert Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404920377239/insrtclmn.gif)

  To drag a group field into a crosstab to become a row header, drag it from the Resources panel and then move the mouse pointer to a border of the row header until a highlighted vertical line appears, then release the mouse.

  ![Add Row Header image](https://devnet.logianalytics.com/hc/article_attachments/4404926637463/wbrpt_manplt_crstb3.gif)

  + When the crosstab has no column/row/summary labels, the new row header will be directly placed where the highlighted line lies.
  + When you have specified any labels to label the columns/rows/summaries in the crosstab using wizard, the [Insert Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009647642-Insert-Row) dialog appears. You can specify a label to label the new row header if necessary. Select **OK** and the new column header will be placed where the highlighted line lies.

    ![Insert Row dialog](https://devnet.logianalytics.com/hc/article_attachments/4404926637719/insrtrw.gif)

  To remove a row/column header from a crosstab, first select it, then drag and drop it to the Resources panel.
* **Inserting aggregate fields by dragging**  
   You can drag and drop fields (detail fields, aggregation fields, and dynamic formulas/aggregations) from the Resources panel to a crosstab to add them as aggregate fields to summarize data in the crosstab. To do this, in the Resources panel, drag the required field and move the mouse pointer above or under the desired subtotal or grand total cell until a highlighted horizontal line appears, then release the mouse.

  ![Insert Aggregation image](https://devnet.logianalytics.com/hc/article_attachments/4404920377879/wbrpt_manplt_crstb5.gif)

  + If the selected field has been predefined with an aggregate function,
    - When the crosstab has no column/row/summary labels, the field is inserted into the specified position directly.
    - When you have specified any labels to label the columns/rows/summaries in the crosstab using wizard, the [Insert Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009647542-Insert-Aggregation) dialog appears. You can specify a label to label the newly created summaries if necessary. Select **OK** and the field is inserted to the specified position.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404926638103/wbrpt_manplt_crstb6.gif)
  + If the selected field has no predefined aggregate function, the Insert Aggregation dialog appears. From the Aggregate Function drop-down list, select the function to summarize the field, then input a label to label the newly created summaries if necessary. Select **OK** and the field is inserted to the specified position. However, whether the label you specify would be generated depends on if you have added any labels to label the columns/rows/summaries in the crosstab using wizard. If no label is defined in the wizard, the label you add in the Insert Aggregation dialog will be ignored. After the field is inserted in the crosstab, you can switch the aggregate function it uses at anytime. To do this, right-click the field and select **Switch Function** from the shortcut menu, then choose a new function from the submenu.

  When you have added an aggregate field using this way, you can find the new aggregate field in the Summaries box of the Crosstab Wizard.
* **Converting a crosstab into a chart**
  1. Select the crosstab and then do either of the following:
     + Select **Menu** > **Edit** > **To Chart**.
     + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the crosstab and select **To Chart** from the shortcut menu.

     The [To Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009648002-To-Chart) dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920378135/tochart.gif)
  2. In the Title text field, input a title for the chart. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. The Resources box lists all the view elements used in the selected crosstab including group and aggregation objects. The chart can only be defined based on the view elements listed. Select the required chart type from the chart type drop-down list. Add a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) from the Resources box to the Category box, and so to the Series box, and aggregation objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) to the Show Values box respectively.

     If you select a bubble chart type, you need to specify the fields to be shown on the bubble X axis, Y axis and the value you want to show as the bubble radius in the Show Values box. Note that when you specify a value for the bubble X axis, this value will be displayed on the category axis instead of the one specified in the Category box. However, the value defined in the Category box will also be included in data calculation.
  4. Select the **OK** button to finish the conversion.

  Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components#Chart) for more information about how to define a chart.
* **Rotating a crosstab**  
   Columns and rows in a crosstab can be exchanged. This operation is called rotating a crosstab.

  To rotate a crosstab, first select it, and then do one of the following:

  + Select **Menu** > **Edit** > **Rotate Crosstab**.
  + Select the **Rotate Crosstab** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920364567/btn_rotate.gif) on the toolbar.
  + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the crosstab and select **Rotate Crosstab** from the shortcut menu.
* **Adjusting the width of crosstab fields according to the contents**  
   When the contents in the field of a crosstab need more space to completely display, you can adjust the width of the field according to its contents. To achieve it, right-click the field and select **Autofit** from the shortcut menu.
* **Customizing the field value data format**  
   To customize the data format of the values of a field in a crosstab, right-click on any value of the field, then select a format from the Format submenu, or input a format in the text box at the bottom of the submenu and select **Enter** on the keyboard.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926638359/wbrpt_manplt_crstb9.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating a Chart

For the chart in a KPI component, that is a KPI chart, only the first seven of the following operations are supported.

* **Changing the chart definition**
  1. Do one of the following to access the Chart Wizard:
     + Select the chart, then select **Menu** > **Edit** > **Wizard**.
     + Select the chart, then select the **Chart Wizard** button ![Chart Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4404920367127/btn_wbrpt_wizard.gif) on the visualization toolbar.
     + Right-select the icon ![Chart button](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the chart, then select **Chart Wizard** from the shortcut menu.

     The [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009647082-Chart-Wizard) appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920378775/chtwzd.gif)
  2. In the Chart Title text field, edit the title of the chart. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. Select the **Filter** button to apply some filter conditions to narrow down data displayed in the chart. The button is not available for a KPI chart.
  4. Change the values displayed on the chart.
  5. Upon finishing, select **OK** to apply the modifications.

  Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components#Chart) for more information about how to define a chart.
* **Switching chart fields**  
   In addition to the above method, another more convenient way to change the fields displayed on a chart is by using the Switch command.
  + **To change the field on the category/series axis:**  
     Select the chart, right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the chart or right-click on the chart platform or paper, then select **Switch Category**/**Switch****Series** from the shortcut menu. The fields available for the category/series axis are listed in the submenu with the current used field checked. Select the field you want to use to replace the current one on the axis.
  + **To change the field on the value axis:**  
     Select the chart, right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the chart or right-click on the chart platform or paper, then select **Switch Values** from the shortcut menu. The fields available for the value axis are listed in the submenu with the current used field checked. Select an unchecked field to add it to the value axis.

    If a chart has multiple fields on its value axis, you can also select the up or down arrow beside the current used fields to adjust their order, or select a checked field to remove it from the chart. When there is only one field on the value axis, it cannot be removed.

    For a combo chart, you can change the fields displayed on the chart one by one for each chart type.
* **Swapping chart groups**  
   You can swap the chart groups by switching data between the category and series axes, or between the category and value axes of a chart if no field on the series axes.
  + To switch data between the category and series axes, first select the chart, then select the **Swap Chart Groups** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920364823/btn_wbrpt_swpgrp.gif) on the toolbar; or right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the chart, or right-click on the chart platform/paper and select **Swap Chart Groups** from the shortcut menu.
  + To switch data between the category and value axes, select the chart and then select the **Swap Chart Groups** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920364823/btn_wbrpt_swpgrp.gif) on the toolbar.
* **Changing the chart type**  
  Select the chart, then on the toolbar, select the **Chart Type** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920365335/btn_wbrpt_chttype.gif). From the drop-down menu, select the desired chart type and its subtype.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379287/wbrpt_manplt_cht6.gif)
* **Zooming in chart values**  
  For a bar, bench, line, area, or stock chart, you can select the values you are interested in to have them zoomed in. To do this, drag the mouse from the start value to the end value you want to select in View Mode of Web Report Studio, then release the mouse. The selected values will be zoomed in. If you want to return to the initial status, just select the return button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926638615/btn_wbrpt_return.gif) on the upper right corner of the chart paper.
* **Stopping or resuming a real time chart from refreshing**  
  For a real time chart, you can stop or resume it from automatically refreshing by right-clicking it and selecting the Pause Refresh or Resume command from the shortcut menu.
* **Formatting chart elements**  
  You can format the chart platform, paper, legend, wall, X and Y axes/gridlines, and rectangles and rectangle titles of heat maps using the corresponding format command on the shortcut menu of a chart (for a KPI chart only platform, paper and wall). For details about the element properties, refer to the specific format dialog in [Web Report Studio Dialogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009647022-Web-Report-Studio-Dialogs).
* **Converting a chart into a crosstab**
  1. Select the chart and then do either of the following:
     + Select **Menu** > **Edit** > **To Crosstab**.
     + Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the chart, or right-click on the chart platform or paper and select **To Crosstab** on the shortcut menu.

     The [To Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009648022-To-Crosstab) dialog appears.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404926638871/tocrstb.gif)
  2. In the Title text field, input a title for the crosstab. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920373527/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. Select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379799/btn_addrow.gif) to add it as a group field to the Columns or Rows box; select an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) or a detail object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356631/btn_bvdtl.gif) and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920380311/btn_addsum.gif) to add it as an aggregate field to the Summaries box. If a detail object is added, specify the aggregate function for it in the Aggregation column. Repeat this to add more group and aggregate fields.

     In the Label column, you can edit the label of a group field or aggregate field. By default the Label column is blank and no label will be created for the added fields in the generated crosstab. You can make Logi JReport automatically provide the labels to them. To enable the feature, go to Logi JReport Console/Administration page > Profile > Customize Profile > Common tab, select **Add Labels for Crosstab Rows and Columns** and/or **Add Labels for Crosstab Summaries** as required.

     In the Sort column, specify a sorting manner on a group field.

     If necessary, select the **Comparison Function** button to set the [comparison function](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components#Comparison) for the aggregate fields.

     If you want to remove any group/aggregate field, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif).

     To adjust the order of group/aggregate fields, select a group/aggregate field and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).
  4. Select **OK** to finish the conversion.
* **Showing/Hiding the chart legend or legend label**   
  Select the chart, right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the chart or right-click on the chart platform or paper, then select the corresponding Show or Hide command from the shortcut menu to show or hide the legend or legend label. However, the legend will always be displayed at the export or print result.
* **Showing/Hiding labels on the X/Y axis**  
   Select the chart, then on the toolbar, select the **Chart Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926632215/btn_wbrpt_chtlayout.gif). From the drop-down menu, go to the **Label** submenu, then select/unselect the desired labels to show/hide them.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639639/wbrpt_manplt_cht7.gif)
* **Showing/Hiding X/Y gridlines**  
   Select the chart, then on the toolbar, select the **Chart Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926632215/btn_wbrpt_chtlayout.gif). From the drop-down menu, go to the **Gridlines** submenu, then select/unselect the desired gridlines to show/hide them.

  When gridlines are shown, it is better to also have the wall shown so as to make the background gridlines more intuitive. To show the wall, follow the steps above, then on the Gridlines submenu, select **Wall**.
* **Changing the chart legend position**  
   Chart legend can be placed at the top, bottom, left or right position in a chart. To change the legend position, select the chart, then on the toolbar, select the **Chart Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926632215/btn_wbrpt_chtlayout.gif). From the drop-down menu, go to the **Legend** submenu and select the desired position.
* **Customizing the data format of chart data labels**  
   You can customize the data format of the legend entry labels and data labels on the category and series axes if they are of Number or Date/Time type. To do this, right-click on any label and select the required format from the Format submenu, or input a format in the text box at the bottom of the submenu and select **Enter** on the keyboard.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381719/wbrpt_manplt_cht8.gif)

**Notes:**

* The org chart type cannot be converted to crosstab or any other chart type, and vice versa.
* Additional values are supported only in chart. If you convert a chart with additional values into crosstab, the additional values are not converted together with the chart.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating a KPI Component

* **Removing the KPI chart from a KPI component**  
   Right-select the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the KPI component, then on the shortcut menu select **Remove KPI Chart**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Manipulating Geographic Map Group Markers/Areas

* **Going up/down on geographic map group markers/areas**
  + For the group level that is higher than some other group levels in a geographic map component, point to its group marker/area, right-click it and select **Go Down** from the shortcut menu to jump one group level down.
  + For the group level that is lower than some other group levels in a geographic map component, point to its group marker/area, right-click it and select **Go Up** from the shortcut menu to jump one group level up.
* **Showing/Hiding geographic map group markers/areas**  
   By default, all visible group markers/areas are shown. To hide them, right-click the geographic map (not the group markers/areas) and select **Hide Markers**/**Hide Areas** from the shortcut menu. If you want to show them again, right-click the geographic map and select **Show Markers**/**Show Areas** from the shortcut menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Converting Between Table/Crosstab/Chart Using Visualization Toolbar

Tables, crosstabs, and charts can be converted to one another easily using the visualization toolbar (a chart in a KPI component can only be converted to another chart). When the current data component contains enough data fields for the target component type, the conversion is accomplished directly. Otherwise, a conversion dialog pops up which allows you to reload all the data fields from a business view and then to define the target component.

**To convert to a table:**

A table, crosstab, or chart can be converted to a table. Select the data component and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926632471/btn_wbrpt_2tbl.gif) on the visualization toolbar.

* When you are converting a crosstab or chart to a table, the table will be generated directly according to the data fields in the crosstab or chart.
* When you are converting a table to a table, the [Convert to Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009671621-Convert-to-Table) dialog is displayed for you to define the new table. You can select another business view for the table or use the current one. If the current one is used, select the **Show All Fields** link to show all the elements in the business view. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components#InsertStandard) for more information about how to define a table.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926640151/cnvttbl_dtl.gif)

**To convert to a crosstab:**

A table or chart can be converted to a crosstab. Select the data component and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920367639/btn_wbrpt_2crstb.gif) on the visualization toolbar.

* When the data component contains enough data fields required by a crosstab, the crosstab will be generated directly according to the current data fields.
* When the current data fields are not enough for a crosstab, the [Convert to Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009671601-Convert-to-Crosstab) dialog is displayed for you to select more fields to define the crosstab. You can select another business view for the crosstab or use the current one. If the current one is used, select the **Show All Fields** link to show all the elements in the business view. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components#Crosstab) for more information about how to define a crosstab.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926640663/cnvtcrstb.gif)

**To convert to a chart:**

A table or crosstab can be converted to a chart. One chart type can also be converted to another. Select the data component and then select the desired chart type button on the visualization toolbar.

* When the data component contains enough data fields required by the target chart type, the chart will be generated directly according to the current data fields.
* When the current data fields are not enough for the target chart type, the [Convert to Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009671581-Convert-to-Chart) dialog is displayed for you to select more fields to define the target chart type. You can select another business view for the chart or use the current one. If the current one is used, select the **Show All Fields** link to show all the elements in the business view. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009675221-Inserting-Components#Chart) for more information about how to define a chart.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926640919/cnvtcht.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675241-Making-Simple-Modifications-to-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650322-Binding-Links-to-Objects)
