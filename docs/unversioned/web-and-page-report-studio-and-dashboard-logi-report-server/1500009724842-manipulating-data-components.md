---
title: "Manipulating Data Components"
id: 1500009724842
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components
updated_at: 2021-07-25T07:18:34Z
---

# Manipulating Data Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724822-Adding-Links-in-a-Report)

# Manipulating Data Components

You can manipulate data components, which refer to tables, crosstabs, charts, banded objects, KPIs, and geographic maps, in Web Report Studio as shown below. Note that, most of the manipulations require selecting the component first. To select a component, hover the mouse pointer on the component, when the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) appears at its upper left corner, select the icon.

Select the following links to view the topics:

* [Manipulating a Table](#Table)
* [Manipulating a Crosstab](#Crosstab)
* [Manipulating a Chart](#Chart)
* [Manipulating a Banded Object](#Banded)
* [Manipulating a KPI](#KPI)
* [Manipulating Geographic Map Group Markers/Areas](#Map)
* [Converting Between Table/Crosstab/Chart/Banded Object Using the Visualization Toolbar](#ConvertVT)
* [Saving a Data Component as a Library Component](#SaveAsLC)

## Manipulating a Table

* **Showing/Hiding the headers/footers and detail in a table**  
   Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the table, then on the shortcut menu, select/unselect the corresponding names from the Show > Table Header/Table Footer/Table Detail/Table Group Header/Table Group Footer submenu to show/hide them.

  ![Show Headers/Footers or Detail](https://devnet.logianalytics.com/hc/article_attachments/4404942453911/wbrpt_manplt_table1.gif)

  You can also hide a table header, footer or the detail as follows: select anywhere in the corresponding row and when the button ![Select Row](https://devnet.logianalytics.com/hc/article_attachments/4404936724503/btn_wbrpt_slctrow.gif)appears at the leftmost on the row select the button to select the row, then right-click on the selected row and select **Hide** from the shortcut menu.

  ![Change Field](https://devnet.logianalytics.com/hc/article_attachments/4404942454167/wbrpt_manplt_table2.gif)
* **Show/Hiding table columns**  
   There are the following ways to show/hide a table column:
  + To show/hide a column, right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the table, then on the shortcut menu, select/unselect the column names from the Show > Table Column submenu to show/hide them.
  + To hide a column, select anywhere in the column, select the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) appearing on the column header to select the column, then right-click on the selected column and select **Hide**.
  + To show/hide a detail column, select the table and then select the **Show/Hide Detail** button ![Show/Hide Detail button](https://devnet.logianalytics.com/hc/article_attachments/4404936718743/btn_wbrpt_dtlclm.gif) on the toolbar. From the drop-down list, select/unselect the object name to show/hide its detail column.
  + To show/hide a summary column, select the table and then select the **Show/Hide Summary** button ![Show/Hide Summary button](https://devnet.logianalytics.com/hc/article_attachments/4404942448151/btn_wbrpt_sum.gif) on the toolbar. From the drop-down list, select/unselect the aggregation object name to show/hide the corresponding summary.
* **Adjusting order of columns in a table**  
   The order of columns in a table can be easily adjusted. To do this, select anywhere in a column, then select the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Drag the selected column to the left or right boundary of another column, when a highlighted line appears along the column boundary, release the mouse.

  ![Adjust Column Order](https://devnet.logianalytics.com/hc/article_attachments/4404936725015/wbrpt_manplt_table3.gif)
* **Changing the table definition** 
  1. Select the table and do one of the following:
     + Select **Menu** > **Edit** > **Wizard**.
     + Select the **Table Wizard** button ![Table Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4404942449431/btn_wbrpt_wizard.gif) on the visualization toolbar.
     + Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the table and select **Table Wizard** from the shortcut menu.

     The [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009722462-Table-Wizard) appears.

     ![Table Wizard - Details tab](https://devnet.logianalytics.com/hc/article_attachments/4404936725271/tblwzd_dsply.gif)
  2. In the Table Title text box, edit the title of the table. You can select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. Select the **Filter** button to apply some filter conditions on the business view the table uses to narrow down data displayed in the table.
  4. Define the data displayed in the table.
     + For a group table:
       in the Details tab, add or change the detail fields displayed in the table; in the Group tab, modify the grouping criteria of the table; in the Summary tab, modify the summary fields of the table.
     + For a summary table: in the Columns tab, change the fields you want to display in the table; in the Summary tab, add or edit the aggregations in the header/footer rows of the table and groups.
  5. Select **OK** to apply the modifications.

  See [Inserting a Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Table) for more information about how to define a table.
* **Switching table column fields**  
   In addition to the above method, another more convenient way to change the fields displayed in the detail columns or group columns of a table is using the Switch command.
  + **To change the field in a detail column:**  
     Select anywhere in the column, then select the arrow button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Right-click on the column and select **Switch Column** from the shortcut menu. The objects in the business view used by the table and the available [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) which can be applied to the detail column are listed in the submenu with the currently used one selected. Select the object you want to use to replace the current one in the column.

    ![Change Field](https://devnet.logianalytics.com/hc/article_attachments/4404936725655/wbrpt_manplt_table4.gif)
  + **To change the group field in a group column:**  
     Right-click any value of the group and select **Switch Group**  from the shortcut menu. Group objects in the business view used by the table and the available [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) used as Group are listed in the submenu with the currently used one selected. Select the object you want to use to replace the current one in the column.
* **Adding/Removing groups in a table**  
   You can add more groups into a table or remove the groups that are not required from a table.
  + **To add a group into a table:**  
     Select the table, then on the toolbar select the **Add/Remove Group** button ![Add/Remove Group button](https://devnet.logianalytics.com/hc/article_attachments/4404936718999/btn_wbrpt_adrmvgrp.gif). Report Server displays a list containing the group objects in the business view used by the table. Select the group object you would like to add into the table as a group. If there is no existing group in the table, the added group will be placed at the left-above position. If the table already contains groups, the new group will be added as the highest level group and follow the same position pattern as the closest existing group.
  + **To remove a group from a table:**
    - Right-click any value of the group and select **Delete** from the shortcut menu.
    - Select the table, then use the Add/Remove Group button ![Add/Remove Group button](https://devnet.logianalytics.com/hc/article_attachments/4404936718999/btn_wbrpt_adrmvgrp.gif) on the toolbar: unselect the group you want to remove from the drop-down list.
    - Select any value of the group, then select the arrow button ![Select Row](https://devnet.logianalytics.com/hc/article_attachments/4404936724503/btn_wbrpt_slctrow.gif) that appears at the leftmost on the row to select the group row, or the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) on the column header to select the group column. Drag and drop the row or column outside the report page.
* **Sorting the data in a group table**  
   You can take the following ways to sort data in a group table, and when you sort a group table by values in a detail column and then values in another detail column, data in the table will be sorted by the later sort condition first and then by the former sort condition.
  + **Using shortcut menu**  
     To sort the data based on values in any column, right-click any value in the column, then on the shortcut menu select **Ascend** or **Descend** from the Sort submenu. If the column is a group column, groups in the current group level will be rearranged. To remove the sort condition, select **No Sort**.

    ![Sort Table by Shotcut Menu](https://devnet.logianalytics.com/hc/article_attachments/4404942454935/wbrpt_manplt_table7.gif)
  + **Using the sort button on table column header**  
     You can use the sort button on any table column header to sort values in the column if the feature is enabled in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#ColumnHeader). By default the feature is enabled.
    1. Put the mouse pointer on any column header and you can find the sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404942455191/btn_lblsort.gif).

       ![Sort Table by Column Header](https://devnet.logianalytics.com/hc/article_attachments/4404942455447/wbrpt_manplt_table8.gif)
    2. To sort values in the column ascending, select the upward triangle; to sort the values descending, select the downward triangle. When a sort order is applied, the corresponding triangle will be highlighted. To remove the sort order, select the highlighted triangle.

       A summary column that contains multiple aggregation objects cannot be sorted using this way. Moreover a group header in a table created in Web Report Studio is always merged as a table cell. If a summary column contains only one aggregation object which is in a merged group header, you cannot use this way to sort it either.
  + **Using labels**  
     With Logi Report Designer, you can bind a label in a table with a field used in the table to enable sorting on the label by setting the label's Bind Column and Sortable properties. Then when running the table in Web Report Studio you can select the sort button beside the label to sort values of the bound field. This functions the same as via the [table column headers](#HeaderSort).

    When a label is bound with a field, if the Sort on Column Header feature is also enabled, the former has higher priority. For example, if you bind the label in column A header with the field in column B, when selecting the sort button on column A header, values in column B are sorted.
* **Sorting the data in a summary table**  
   You can use the [same methods on group tables](#SortGroupTable) to sort the group and summary columns in summary tables. However for summary tables, you can define whether to use major sort or minor sort via the [Use Major Sort as Default](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#Sort) option in the server profile. By default, major sort is applied which is to sort data in a summary table by the last sort condition only, that is to say the later sort condition always replaces the former one. When minor sort is used, sort of a lower group is always based on the sort result of all its higher level groups.

  For example, a summary table contains group columns G1, G2 and G3 (G1 the highest group level and G3 the lowest) and the summary columns S1 and S2. When minor sort is applied, after sorting the group column G1 ascending, if you apply a sort on G2 descending, the table will be sorted based on G1 ascending first and then G2 descending; if you further sort G3 descending and the sort result is G1 ascending, G2 descending and G3 descending. Based on this sort result, if you apply the ascending order on the summary column S1, the table will be sorted based on G1 ascending, G2 descending and S1 ascending. Sort order on G3 is removed, this is because all summary columns calculate data based on the lowest group in a summary table and they are considered as one group, so on the lowest group and the summary columns only one sort order can take effect. Therefore based on the former sort result, if you apply a sort order on G3 again the sort on S1 will be removed.
* **Aggregating on a detail column**  
   You can summarize the data in a detail column. To do this:
  1. Do either of the following:
     + Right-click any value in the detail column and select **Aggregate On** from the shortcut menu.
     + Select anywhere in the column, then select the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. On the toolbar, select the **Aggregate On** button ![Aggregate On button](https://devnet.logianalytics.com/hc/article_attachments/4404936719255/btn_wbrpt_agrgton.gif).
  2. In the [Aggregate On](https://devnet.logianalytics.com/hc/en-us/articles/1500009748081-Aggregate-On) dialog box, specify a function from the Function drop-down list to summarize the data.
     When DistinctSum is selected, you should select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) next to the Distinct On text box to specify one or more group and detail objects according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields) dialog box.

     For the usage about each function, refer to Aggregate Functions in the *Logi Report Designer Guide*.

     ![Aggregate On dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936726167/agrgton.gif)
  3. When done, select **OK**.
     + If the table has groups, you will find data in each group level and the whole table are summarized respectively in the column.
     + If the table has no groups, the summary will be based on the whole table.

  When you finish summarizing a detail column, you can find a [dynamic aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) is created at the same time in the Dynamic Resource > Aggregations list in the Resources panel, which is given a default name Function\_DetailFieldName. You can use it again in the current report.
* **Customizing the data value formats**  
   You can customize the data format of the values in a table if they are of the Number or Date/Time type. To do this, right-click on any value, then select a format from the Format submenu, or type a format in the text box at the bottom of the submenu and select **Enter** on the keyboard.
* **Adjusting the width of table columns according to contents**  
   When the contents in a table column need more space to completely display, you can adjust the width of the table column according to the contents. To do this, select anywhere in the column and select the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column, then right-click on the selected column and select **Autofit** on the shortcut menu. However it takes effect only when the property Autofit for the data field or label in the column is also set to true.

* **Showing/Hiding summary fields in header/footer rows in a summary table**  
   When creating or editing a summary table via the table wizard, once you have placed any aggregation object on its table header/footer or group header/footer, after the table is generated the Show Summary Field command will be activated on the shortcut menu of all the summary columns in the table. You can use the menu command to show or hide the aggregation objects in the header/footer rows. To do this, select anywhere in the summary column that contains the required aggregation object, select the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) appearing on the column header to select the column, then right-click on the column and from the Show Summary Field submenu select/deselect the corresponding table/group header/footer to show/hide the aggregation object on the specified locations.
* **Removing table columns**  
   To remove a table column, select anywhere in the column, then select the button ![Select Column](https://devnet.logianalytics.com/hc/article_attachments/4404936724759/btn_wbrpt_slctclmn.gif) that appears on the column header to select the column. Right-click on the selected column and select **Delete** on the shortcut menu, or drag and drop the column outside the report page.

From the Resources panel, you can drag view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) into a table to add new columns/rows in the table. To do this, first select the table to locate the business view it uses in the Resources panel, then:

* **To add a new table column:**  
   Drag the required object from the Resources panel and move the mouse pointer to the boundary of an existing table column until a highlighted vertical line appears, then release the mouse. The new column will be placed where the highlighted line lies.

  ![Drag to Add Column](https://devnet.logianalytics.com/hc/article_attachments/4404942455703/wbrpt_manplt_table5.gif)
* **To add a new group row:**  
   Drag a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) or dynamic formula used as Group ![Dynamic Formula Used as Group](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources panel and move the mouse pointer in the detail section or to the boundary of an existing table group row until a highlighted horizontal line appears, then release the mouse. The new group row will be placed where the highlighted line lies.

  ![Drag to Add Group](https://devnet.logianalytics.com/hc/article_attachments/4404936726679/wbrpt_manplt_table6.gif)

## Manipulating a Crosstab

* **Changing the crosstab definition**
  1. Select the crosstab and then do one of the following:
     + Select **Menu** > **Edit** > **Wizard**.
     + Select the **Crosstab Wizard** button ![Crosstab Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4404942449431/btn_wbrpt_wizard.gif) on the visualization toolbar.
     + Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the crosstab and select **Crosstab Wizard** from the shortcut menu.

     The [Crosstab Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009721442-Crosstab-Wizard) appears.

     ![Crosstab Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404936726935/crstbwzd_data.gif)
  2. In the Crosstab Title text box, edit the title of the crosstab. You can select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. Select the **Filter** button to apply filter conditions on the business view the crosstab uses to narrow down data displayed in the crosstab.
  4. In the Data tab, change the column/row fields and aggregate fields displayed in the crosstab.
  5. In the Layout tab, specify the layout of the crosstab.
  6. Select **OK** to apply the modifications.

  See [Inserting a Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Crosstab) for more information about how to define a crosstab.
* **Switching crosstab fields**  
   In addition to the above method, another more convenient way to change the fields in a crosstab is to use the Switch command. To do this, right-click any column header/row header/aggregation value and select **Switch Column**/**Switch****Row**/**Switch Summary** from the shortcut menu. Objects in the business view used by the crosstab and the available [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) which can be applied as the row/column/aggregation field are listed in the submenu with the currently used one selected. Select the object you want to use to replace the current one.

  ![Switch Column](https://devnet.logianalytics.com/hc/article_attachments/4404942455959/wbrpt_manplt_crstb1.gif)
* **Sorting data in a crosstab**  
   You can make the data in a crosstab sorted based on any column or row field. To do this, right-click on any value on the column or row header, then choose the command **Sort** > **Ascend**  or **Sort** > **Descend**  from the shortcut menu. To remove the sort condition, select **Sort** > **No Sort** from the shortcut menu.
* **Converting a crosstab into a chart**
  1. Select the crosstab and then do either of the following:
     + Select **Menu** > **Edit** > **To Chart**.
     + Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the crosstab and select **To Chart** from the shortcut menu.

     Report Server displays the [To Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009722482-To-Chart) dialog box.

     ![To Chart dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936727191/tochart.gif)
  2. In the Title text box, type a title for the chart. You can select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. The Resources box lists the view elements used in the crosstab. The chart can only be defined based on these objects. Select the required chart type from the chart type drop-down list. Add a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources box to the Category box, and so to the Series box, and aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) to the Show Values box respectively.
  4. Select the **OK** button to finish the conversion.

  See [Inserting a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Chart) for more information about how to define a chart.
* **Rotating a crosstab**  
   Columns and rows in a crosstab can be exchanged. This operation is called rotating a crosstab.

  To rotate a crosstab, first select it, and then do one of the following:

  + Select **Menu** > **Edit** > **Rotate Crosstab**.
  + Select the **Rotate Crosstab** button ![Rotate Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404942448663/btn_rotate.gif) on the toolbar.
  + Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the crosstab and select **Rotate Crosstab** from the shortcut menu.
* **Customizing the data value formats**  
   You can customize the data format of the values in a crosstab if they are of Number or Date/Time type. To do this, right-click any value, then select a format from the Format submenu, or type a format in the text box at the bottom of the submenu and select **Enter** on the keyboard.
* **Auto fitting values in a crosstab**  
   When the values in the crosstab row/column headers or aggregation cells need more space to completely display, right-click any value in the row/column header or aggregation cell and select **Autofit**  from the shortcut menu. Web Report Studio then adjusts the width of the corresponding cells to match the contents in them. However for performance concern, you are recommended not to select the option as auto fitting the values in a crosstab may cause poor performance.
* **Changing the aggregate function for an aggregation in a crosstab**  
   Right-click the aggregation that is based on a detail object and select **Switch Function** from the shortcut menu, then choose a new function from the submenu. If DistinctSum is selected as the function, Report Server will display the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields) dialog box for you to specify the detail objects according to whose unique values to calculate DistinctSum.
* **Removing column/row headers or aggregations from a crosstab**  
   Drag a value in the column/row header or any aggregation value and drop it outside the report page.

From the Resources panel, you can drag view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-)  into a crosstab to add new column/row headers and aggregations in the crosstab. To do this, first select the crosstab to locate the business view it uses in the Resources panel, then:

* **To add a column header：**  
   Drag a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) or dynamic formula used as Group ![Dynamic Formula Used as Group](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources panel and move the mouse pointer to the boundary of a column header until a highlighted horizontal line appears, then release the mouse.

  ![Add Column Header](https://devnet.logianalytics.com/hc/article_attachments/4404936727831/wbrpt_manplt_crstb3.gif)

  + When the crosstab has no column/row/aggregation labels, the new column header will be directly placed where the highlighted line lies.
  + When you have specified any labels to label the column headers/row headers/aggregations in the crosstab using wizard, Report Server displays the [Insert Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009748961-Insert-Column) dialog box. By default the display name of the object will be used to label the new column header; to edit the label text for the new column header, select in the Label text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** option. Select **OK** and the new column header will be placed where the highlighted line lies.

    ![Insert Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942456471/insrtclmn.gif)
* **To add a row header:**   
   Drag a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) or dynamic formula used as Group ![Dynamic Formula Used as Group](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources panel and move the mouse pointer to the boundary of a row header until a highlighted vertical line appears, then release the mouse.

  ![Add Row Header](https://devnet.logianalytics.com/hc/article_attachments/4404936728215/wbrpt_manplt_crstb4.gif)

+ When the crosstab has no column/row/aggregation labels, the new row header will be directly placed where the highlighted line lies.
+ When you have specified any labels to label the column headers/row headers/aggregations in the crosstab using wizard, Report Server displays the [Insert Row](https://devnet.logianalytics.com/hc/en-us/articles/1500009749101-Insert-Row) dialog box. By default the display name of the object will be used to label the new row header; to edit the label text for the new row header, select in the Label text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** option. Select **OK** and the new row header will be placed where the highlighted line lies.

  ![Insert Row dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942456727/insrtrw.gif)

* **To add an aggregation in the crosstab:**   
   Drag a detail object ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif), aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif), dynamic formula used as Detail ![Dynamic Formula Used as Detail](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif), dynamic formula used as Aggregation ![Dynamic Formula Used as Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or dynamic aggregation ![Dynamic Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif)from the Resources panel and move the mouse pointer above or under the desired aggregation until a highlighted horizontal line appears, then release the mouse.
  The position determines whether detail aggregations, subtotals or grand totals will be created in the crosstab.

  ![Add Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404936728471/wbrpt_manplt_crstb5.gif)

  + If the selected object has been predefined with an aggregate function,
    - When the crosstab has no column/row/aggregation labels, the object is inserted into the specified position directly.
    - When you have specified any labels to label the column headers/row headers/aggregations in the crosstab using wizard, Report Server displays the [Insert Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009748881-Insert-Aggregation) dialog box. By default the display name of the object will be used to label the new aggregation; to edit the label text for the new aggregation, select in the Label text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** option. Select **OK** and the aggregation is inserted to the specified position.

      ![Insert Aggregation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942456983/wbrpt_manplt_crstb6.gif)
  + If the selected object has no predefined aggregate function, Report Server displays the Insert Aggregation dialog box. From the Aggregate Function drop-down list, select the function for calculating the object. When DistinctSum is selected, you should select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) next to the Distinct On text box to specify one or more detail objects according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields) dialog box. By default the display name of the object will be used to label the new aggregation; to edit the label text for the new aggregation, select in the Label text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** option. Select **OK** and the aggregation is inserted to the specified position. However, whether the label you specify would be displayed depends on if you have added any labels to label the column headers/row headers/aggregations in the crosstab using wizard and if there is appropriate position to place the label in the current crosstab. If no label is defined in the wizard, the label you add in the Insert Aggregation dialog box will be ignored.

After you have added a column/row header or aggregation using the drag method, when you open Crosstab Wizard, you can find the fields based on which the column/row header or aggregation is created in the corresponding box.

## Manipulating a Chart

For the chart in a KPI, that is a KPI chart, only some of the following operations are supported.

* **Changing the chart definition**
  1. Do one of the following to access the Chart Wizard:
     + Select the chart, then select **Menu** > **Edit** > **Wizard**.
     + Select the chart, then select the **Chart Wizard** button ![Chart Wizard button](https://devnet.logianalytics.com/hc/article_attachments/4404942449431/btn_wbrpt_wizard.gif) on the visualization toolbar.
     + Right-click on the chart and select **Chart Wizard** from the shortcut menu.

     The [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009721342-Chart-Wizard) appears.

     ![Chart Wizard](https://devnet.logianalytics.com/hc/article_attachments/4404936728727/chtwzd.gif)
  2. In the Chart Title text box, edit the title of the chart. You can select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. Select the **Filter** button to apply some filter conditions on the business view the chart uses to narrow down data displayed in the chart. The button is not available for a KPI chart.
  4. Change the fields displayed on the chart and specify other options as required.
  5. Upon finishing, select **OK** to apply the modifications.

  See [Inserting a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Chart) for more information about how to define a chart.
* **Switching chart fields**  
   In addition to the above method, another more convenient way to change the fields displayed on a chart is to use the Switch command.
  + **To change the field on the value axis:**  
     Right-click on the chart and select **Switch Values** on the shortcut menu. Aggregation objects in the business view used by the chart, as well as the available [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) (including dynamic aggregations and dynamic formulas used as Aggregation) are listed in the submenu with the currently used one selected. Select an unselected object to add it to the value axis.

    If a chart has multiple fields on its value axis, you can also select the up or down arrow beside the currently used ones to adjust their order, or select a selected field to remove it from the chart. When there is only one field on the value axis, it cannot be removed.

    ![Switch Value](https://devnet.logianalytics.com/hc/article_attachments/4404936728983/wbrpt_manplt_cht1.gif)

    For a combo chart, you can change the fields displayed on the chart one by one for each chart type.
  + **To change the field on the category/series axis:**  
     Right-click on the chart and select **Switch Category**/**Switch****Series** from the shortcut menu. Group objects in the business view used by the chart and the available [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) used as Group are listed in the submenu with the currently used one selected. Select the object you want to use to replace the current one on the axis.
* **Sorting the data in a chart**   
   Data labels on the category and series axes of a chart can be sorted alphabetically. To do this, right-click the chart, then on the shortcut menu select **Ascend** or **Descend** from the Sort Category or Sort Series submenu. To remove the sort condition, select **No Sort** on the Sort Category or Sort Series submenu.
* **Swapping chart groups**  
   You can swap the chart groups by switching data between the category and series axes, or between the category and value axes when the chart has no field on the series axis but several on the value axis.
  + To switch data between the category and series axes, first select the chart, then select the **Swap Chart Groups** button ![Swap Chart Groups button](https://devnet.logianalytics.com/hc/article_attachments/4404936719511/btn_wbrpt_swpgrp.gif) on the toolbar; or right-click on the chart and select **Swap Chart Groups** from the shortcut menu.
  + To switch data between the category and value axes, select the chart and then select the **Swap Chart Groups** button ![Swap Chart Groups button](https://devnet.logianalytics.com/hc/article_attachments/4404936719511/btn_wbrpt_swpgrp.gif) on the toolbar.
* **Formatting chart elements**  
  The elements in a chart can be formatted to suit your requirement.

+ To format the platform/paper/legend of a chart, right-click on the chart and select **Format Platform**/**Format Paper**/**Format Legend** from the shortcut menu. In the [Format Platform](https://devnet.logianalytics.com/hc/en-us/articles/1500009721842-Format-Platform) dialog box/[Format Paper](https://devnet.logianalytics.com/hc/en-us/articles/1500009721822-Format-Paper) dialog box/[Format Legend](https://devnet.logianalytics.com/hc/en-us/articles/1500009748541-Format-Legend) dialog box, specify the settings as required.
+ To format the wall of a chart, right-click on the chart and select **Format Walls** > **Format Wall**  from the shortcut menu. In the [Format Wall](https://devnet.logianalytics.com/hc/en-us/articles/1500009721962-Format-Wall)  dialog box, specify the settings as required.
+ To format an axis, right-click on the chart and select the axis from the Format Axis submenu. In the [Format Category (X) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009721742-Format-Category-X-Axis) dialog box, [Format Value (Y) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009748681-Format-Value-Y-Axis) dialog box or [Format Value (Y2) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009748701-Format-Value-Y2-Axis) dialog box, specify the axis settings.
+ To format the gridlines of an axis, right-click on the chart and select the corresponding command from the Format Gridlines submenu. In the [Format Category (X) Gridline](https://devnet.logianalytics.com/hc/en-us/articles/1500009721762-Format-Category-X-Gridline) dialog box, [Format Value (Y) Gridline](https://devnet.logianalytics.com/hc/en-us/articles/1500009748721-Format-Value-Y-Gridline) dialog box, [Format Value (Y2) Gridline](https://devnet.logianalytics.com/hc/en-us/articles/1500009721942-Format-Value-Y2-Gridline) dialog box or [Format Series (Z) Gridline](https://devnet.logianalytics.com/hc/en-us/articles/1500009748661-Format-Series-Z-Gridline) dialog box, set the gridline properties accordingly.
+ To format the graph such as the areas, bars or lines of a chart, right-click on the chart and select **Format Graph** from the shortcut menu (for a combo chart, the option name is Format Graph (Y) and Format Graph (Y2)). In the [Format Area](https://devnet.logianalytics.com/hc/en-us/articles/1500009721642-Format-Area) dialog box, [Format Bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009721662-Format-Bar) dialog box, [Format Bench](https://devnet.logianalytics.com/hc/en-us/articles/1500009721702-Format-Bench) dialog box, [Format Donut](https://devnet.logianalytics.com/hc/en-us/articles/1500009748481-Format-Donut) dialog box, [Format Indicator](https://devnet.logianalytics.com/hc/en-us/articles/1500009748501-Format-Indicator) dialog box, [Format Line](https://devnet.logianalytics.com/hc/en-us/articles/1500009748561-Format-Line) dialog box, [Format Pie](https://devnet.logianalytics.com/hc/en-us/articles/1500009748621-Format-Pie) dialog box, [Format Activity Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009721622-Format-Activity-Gauge) dialog box, [Format Bar Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009721682-Format-Bar-Gauge) dialog box, [Format Bubble Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009721722-Format-Bubble-Gauge) dialog box, [Format Dial Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009721782-Format-Dial-Gauge) dialog box or [Format Solid Gauge](https://devnet.logianalytics.com/hc/en-us/articles/1500009721902-Format-Solid-Gauge) dialog box, set the graph settings as required.
+ For a pie/donut chart, if you specify to display KPI values on it, you can format the KPI value labels, for example, edit the size and border of the labels, change the label font size, font color, and so on. To do this, right-click on the chart and select **Format KPI Label**  from the shortcut menu, then in the [Format KPI Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009748521-Format-KPI-Label) dialog box, set the properties according to your requirements.

  When an activity, bar, dial or solid gauge chart displays the gauge labels, pointer labels and target labels, you can also format the labels accordingly. To do this, right-click on the chart and select **Format Gauge Label**/**Format Pointer Label**/**Format Target Label** from the shortcut menu, then in the [Format Gauge Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009721802-Format-Gauge-Label) dialog box/[Format Pointer Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009721862-Format-Pointer-Label) dialog box/[Format Target Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009721922-Format-Target-Label) dialog box, specify the properties.
+ The nodes and lines in an org chart can also be formatted. To do this, right-click the org chart and select **Format Node**/**Format Line**  from the shortcut menu. In the [Format Org Node](https://devnet.logianalytics.com/hc/en-us/articles/1500009748601-Format-Org-Node) dialog box/[Format Org Line](https://devnet.logianalytics.com/hc/en-us/articles/1500009748581-Format-Org-Line) dialog box, specify the properties.
+ For a heat map chart, you can customize the rectangle separator and rectangle title of a specific group. To do this, right-click the heat map, point to **Format Rectangle**/**Format Rectangle Title** and then select a group name on the shortcut menu. Then in the [Format Rectangle](https://devnet.logianalytics.com/hc/en-us/articles/1500009748641-Format-Rectangle) dialog box/[Format Rectangle Title](https://devnet.logianalytics.com/hc/en-us/articles/1500009721882-Format-Rectangle-Title) dialog box, set the properties.

* **Changing the chart type**  
   Select the chart, then on the toolbar, select the **Chart Type** button ![Chart Type button](https://devnet.logianalytics.com/hc/article_attachments/4404936720023/btn_wbrpt_chttype.gif). From the drop-down list, select the desired chart type and its subtype.
* **Converting a chart into a crosstab**
  1. Select the chart and then do either of the following:
     + Select **Menu** > **Edit** > **To Crosstab**.
     + Right-click on the chart and select **To Crosstab** on the shortcut menu.

     Report Server displays the [To Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009722502-To-Crosstab) dialog box.

     ![To Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942457239/tocrstb.gif)
  2. In the Title text box, type a title for the crosstab. You can select ![Font button](https://devnet.logianalytics.com/hc/article_attachments/4404942454679/btn_wbrpt_font.gif) to customize the font, size, and style of the title.
  3. The Resources box lists the view elements used in the chart. The crosstab can only be defined based on these objects. Add the group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) to the Columns and Rows box as the group fields in the crosstab; add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or detail objects ![Detail Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) to the Summaries box as the aggregate fields to summarize data in the crosstab. For a detail object specify the aggregate function for it from the Aggregation drop-down list. When DistinctSum is selected as the aggregate function, you should select the button ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) next to the Distinct On text box to specify one or more detail objects according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields) dialog box.

     For each column/row/summary field, you can select in the Label text box and type a name to label the corresponding column header/row header/summary, or select the **Auto Map Field Name** check box beside the text box if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field (when the text box is blank and the check box is not selected, no label will be created). In the Sort column, specify a sorting manner on a group field.

     You can select the **Comparison Function** button to set the [comparison function](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Comparison) for the aggregate fields.

     If you want to remove any group/aggregate field, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).

     To adjust the order of group/aggregate fields, select a group/aggregate field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif).
  4. Select **OK** to finish the conversion.

  **Notes:**

  + The org chart type cannot be converted to crosstab or any other chart type, and vice versa.
  + Additional values are supported only in chart. If you convert a chart with additional values into crosstab, the additional values are not converted together with the chart.
* **Showing/Hiding the chart legend or legend label**  
   Right-click on the chart, then select the corresponding Show or Hide command from the shortcut menu to show or hide the legend or legend label. However, the legend will always be displayed in the export or print result.
* **Changing the chart legend position**  
   Chart legend can be placed at the top, bottom, left or right position in a chart. To change the legend position, select the chart, then on the toolbar, select the **Chart Options** button ![Chart Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936720279/btn_wbrpt_chtlayout.gif). From the drop-down menu, go to the **Legend** submenu and select the desired position.

  ![Chart Options > Legend Position](https://devnet.logianalytics.com/hc/article_attachments/4404936729495/wbrpt_manplt_cht2.gif)
* **Showing/Hiding labels on the X/Y axis**  
   Select the chart, then on the toolbar, select the **Chart Options** button ![Chart Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936720279/btn_wbrpt_chtlayout.gif). From the drop-down menu, go to the **Label** submenu, then select/unselect the desired labels to show/hide them.
* **Showing/Hiding X/Y gridlines**  
   Select the chart, then on the toolbar, select the **Chart Options** button ![Chart Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936720279/btn_wbrpt_chtlayout.gif). From the drop-down menu, go to the **Gridlines** submenu, then select/unselect the desired gridlines to show/hide them.

  When gridlines are shown, it is better to also have the wall shown so as to make the background gridlines more intuitive. To show the wall, follow the steps above, then on the Gridlines submenu, select **Wall**.
* **Customizing the data format of chart data labels**  
   You can customize the data format of the legend entry labels and data labels on the category and series axes if they are of Number or Date/Time type. To do this, right-click on any label and select the required format from the Format submenu, or type a format in the text box at the bottom of the submenu and select **Enter** on the keyboard.
* **Stopping or resuming a real time chart from refreshing**  
   For a real time chart, you can stop or resume it from automatically refreshing by right-clicking it and selecting the Pause Refresh or Resume command from the shortcut menu.
* **Zooming in chart values**  
   For a bar, bench, line, area, or stock chart, you can select the values you are interested in to have them zoomed in. To do this, make sure you are in View Mode of Web Report Studio, then drag the mouse from the start value to the end value you want to select and release the mouse.

  ![Zoom in Chart Values](https://devnet.logianalytics.com/hc/article_attachments/4404936729751/wbrpt_manplt_cht3.gif)

  The selected values are zoomed in. To return to the initial status, select the return button ![Return button](https://devnet.logianalytics.com/hc/article_attachments/4404942457751/btn_wbrpt_return.gif) on the upper right corner of the chart paper.

  ![Zoom in Chart Values](https://devnet.logianalytics.com/hc/article_attachments/4404936730007/wbrpt_manplt_cht4.gif)

## Manipulating a Banded Object

* **Editing the banded object template**  
   Web Report Studio provides the template editor for you to edit the templates of banded objects easily (to display the editor, right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the banded object and select **Edit Template** from the shortcut menu, or select ![Edit Template button](https://devnet.logianalytics.com/hc/article_attachments/4404936721047/btn_wbrpt_edt.gif) on the visualization toolbar; to exit the editor, select ![Return button](https://devnet.logianalytics.com/hc/article_attachments/4404936730263/btn_wbrpt_return1.gif) on the visualization toolbar or **Return** on the top-right corner of the Web Report Studio window). Banded objects can be nested and contain other components with absolute layout for precise design. By modifying the template of a banded object, you can easily design a complex report with sophisticated layout without having impact on the performance.

  By default, a banded object template contains the following panels which are identified on the left side by their abbreviations: a banded header panel (BH), a banded page header panel (BPH), a detail panel (DT), a banded page footer panel (BPF), a banded footer panel (BF), a group header panel (GH) and group footer panel (GF). You can add more panels, insert components and add data into the panels according to your requirements.

  ![Sort Banded Object by Shotcut Menu](https://devnet.logianalytics.com/hc/article_attachments/4404942458007/wbrpt_manplt_banded1.gif)

  + **Managing the banded panels**
    - To add a banded panel, select a panel of the same type, select ![Menu for Banded Panel button](https://devnet.logianalytics.com/hc/article_attachments/4404942458263/btn_wbrpt_optn.gif) in the panel and select **Insert Panel Before** or **Insert Panel After**. A blank panel of the same type is then inserted into the banded object.
    - To delete a banded panel from a banned object, select ![Menu for Banded Panel button](https://devnet.logianalytics.com/hc/article_attachments/4404942458263/btn_wbrpt_optn.gif) in the panel and select **Delete Panel**. Note that you cannot delete a panel of a certain type if it is the only one of that type.
    - To hide a banded panel from view, select ![Menu for Banded Panel button](https://devnet.logianalytics.com/hc/article_attachments/4404942458263/btn_wbrpt_optn.gif) in the panel and then select **Hide**.
    - To show a hidden banded panel, select **Show Hidden Objects** on the toolbar. Report Server displays the hidden panel and marks it with ![Unhide button](https://devnet.logianalytics.com/hc/article_attachments/4404936730647/btn_wbrpt_unhd.gif). Then select ![Unhide button](https://devnet.logianalytics.com/hc/article_attachments/4404936730647/btn_wbrpt_unhd.gif) or ![Menu for Banded Panel button](https://devnet.logianalytics.com/hc/article_attachments/4404942458263/btn_wbrpt_optn.gif) in the panel, and select **Unhide** from the shortcut menu to release its hidden state.
    - To resize a banded panel, drag the boundary below the banded panel until the panel is at the required height.
  + **Adding components and data to the banded panels**  
     You can [add components](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components) such as tables, crosstabs, charts, web controls, images, horizontal/vertical lines from the Components panel and drag view elements and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) from the Resources panel into the banded panels.

    When you add a table, crosstab or chart to the banded header panel, banded footer panel, group header panel or group footer panel, you can make it inherit data from the banded object. By inheriting the parent's business view, the report becomes powerful. For example, if you want a chart to be automatically filtered by the group of the parent banded object, you can put it in the group panel in the banded object and make it inherit data from its parent, then the chart will be replicated for each group in the parent. In addition, having data components inherit data from the parent banded objects whenever possible will have a dramatic effect on the performance of your reports.

    See an example below about embedding a chart in a banded object using inherited data.

    1. [Insert a banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Banded) using WorldWideSalesBV in the SampleReports catalog, which is only grouped by the Country group object.

       ![Banded Object with Coutnry Group](https://devnet.logianalytics.com/hc/article_attachments/4404936730903/wbrpt_manplt_banded4.gif)
    2. Go to the template editor of the banded object.
    3. Drag **Chart** from the Components panel to the GH panel.
    4. In the Insert Chart dialog box, define the chart as follows: make sure <Inherit from the Parent> is selected in the Data Source drop-down list, add **Total Sales** to the Bar Length box, **Country** to the X-Axis box, **Product Name** to the Clustering box. Then select **OK** to insert the chart in the group panel.

       ![Define the Embedded Chart](https://devnet.logianalytics.com/hc/article_attachments/4404936731159/wbrpt_manplt_banded5.gif)
    5. Exit the template editor. The banded object and chart display as follows. You can see the total sales for each product in each country are filtered in the chart according to the group-by field Country in the banded object.

       ![Report Result](https://devnet.logianalytics.com/hc/article_attachments/4404936731415/wbrpt_manplt_banded6.gif)
  + **Adding groups to the banded object**
    1. Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the banded object and select **Insert Group** from the shortcut menu. Report Server displays the [Insert Banded Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009748921-Insert-Banded-Group) dialog box.

       ![Insert Bander Group dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936731671/insrtbdgrp.gif)
    2. All the group objects in the business view on which the banded object is created are listed. Select the group object you would like to use for the new group.
    3. Select **OK**. A new group is now inserted into the banded object as the top level group.

    When there are existing groups in the banded object, you can also use either of the following ways to add a group:

    - Drag a group object ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources box to above or below the GH or GF panel of a group until a horizontal line appears and then release the mouse.

      ![insert Banded Group by Shotcut Menu](https://devnet.logianalytics.com/hc/article_attachments/4404936731927/wbrpt_manplt_banded7.gif)
    - Select ![Menu for Banded Panel button](https://devnet.logianalytics.com/hc/article_attachments/4404942458263/btn_wbrpt_optn.gif) in the GH or GF panel of a group and select **Insert Group Before** or **Insert Group After** and then select a group object.

      ![insert Banded Group by Shotcut Menu](https://devnet.logianalytics.com/hc/article_attachments/4404942458519/wbrpt_manplt_banded2.gif)

    When a group is added to the GH panel, the level of the new group follows the position. However when added to the GF panel, the new group is still placed in the new GH panel but with the opposite level. See the following table:

    | Inserted Position | Level of New Group |
    | --- | --- |
    | Above or before GH | Higher level |
    | Below or after GH | Lower level |
    | Above or before GF | Lower level |
    | Below or after GF | Higher level |
  + **Removing groups from the banded object**   
     Select ![Menu for Banded Panel button](https://devnet.logianalytics.com/hc/article_attachments/4404942458263/btn_wbrpt_optn.gif) in the GH or GF panel of the required group and select **Delete Group** from the shortcut menu.

**Tip:** Some operations in the template editor are also supported in the Edit Mode of Web Report Studio. For example, you can drag view elements and dynamic resources into a banded object to add new detail fields in the banded object. To do this, select the banded object to locate the business view it uses in the Resources panel, drag the required object from the Resources panel and move the mouse pointer to the detail section in the banded object and release the mouse. You can also add/remove groups in the banded object and insert/delete banded panels using the shortcut menu of the banded object.

* **Switching the group-by fields**  
   In the Edit Mode of Web Report Studio, you can change the group-by fields in a banded object using the Switch Group command. To do this, right-click any value of the required group level and select **Switch Group**  from the shortcut menu. Group objects in the business view used by the banded object and the available [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-) used as Group are listed in the submenu with the currently used one selected. Select the object you want to use to replace the current one.

  ![Sort Banded Object by Shotcut Menu](https://devnet.logianalytics.com/hc/article_attachments/4404936732183/wbrpt_manplt_banded3.gif)
* **Sorting the data in a banded object**  
   You can take the following ways to sort data in a banded object, and when you sort a banded object by values of a detail field and then values of another detail field, data in the banded object will be sorted by the later sort condition first and then by the former sort condition.
  + **Using shortcut menu**  
     To sort the data based on values of a detail field, right-click any value of the detail field, then on the shortcut menu select **Ascend** or **Descend** from the Sort submenu; to sort groups of a group level, right-click any value of the group level and select **Ascend** or **Descend** from the Sort submenu. To remove the sort condition, select **No Sort**.
  + **Using labels**  
     With Logi Report Designer, you can bind a label in a banded object with a field used in the banded object to enable sorting on the label by setting the label's Bind Column and Sortable properties. Then when running the banded object in Web Report Studio you can select the sort button beside the label to sort values of the bound field. This functions the same as via the [table column headers](#HeaderSort).

## Manipulating a KPI

* **Removing the KPI chart from a KPI**  
   Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of the KPI, then on the shortcut menu select **Remove KPI Chart**.

## Manipulating Geographic Map Group Markers/Areas

* **Going up/down on geographic map group markers/areas**
  + For the group level that is higher than some other group levels in a geographic map component, point to its group marker/area, right-click it and select **Go Down** from the shortcut menu to jump one group level down. The go-down action always happens along with the generation of a filter condition based on the selected value and you can find the condition at the bottom of the map after the result is generated. For example, if you perform the action on the country Germany and the next group level is state, you will get data of states in Germany only after going down.
  + For the group level that is lower than some other group levels in a geographic map component, point to its group marker/area, right-click it and select **Go Up** from the shortcut menu to jump one group level up.
* **Showing/Hiding geographic map group markers/areas**  
   By default, all visible group markers/areas of the current group level are shown. To hide them, right-click the geographic map (not the group markers/areas) and select **Hide Markers**/**Hide Areas** from the shortcut menu. If you want to show them again, right-click the geographic map and select **Show Markers**/**Show Areas** from the shortcut menu.

## Converting Between Table/Crosstab/Chart/Banded Object Using the Visualization Toolbar

Tables, crosstabs, and charts can be converted to one another easily using the visualization toolbar (a chart in a KPI can only be converted to another chart). Tables that are not in banded objects can also be converted to banded objects. When the current data component contains enough data fields for the target component type, the conversion is accomplished directly. Otherwise, a conversion dialog box pops up which allows you to reload all the objects from a business view and then to define the target component.

**To convert to a table:**

A table, crosstab, or chart can be converted to a table. Select the data component and then select ![Convert or drag to add table button](https://devnet.logianalytics.com/hc/article_attachments/4404936721303/btn_wbrpt_2tbl.gif) on the visualization toolbar.

* When you are converting a crosstab or chart to a table, the table will be generated directly according to the data fields in the crosstab or chart.
* When you are converting a table to a table, Report Server displays the [Convert to Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009721382-Convert-to-Table) dialog box for you to define the new table. You can select another business view for the table or use the current one. If the current one is used, select the **Show All Fields** link to show all the objects in the business view. See [Inserting a Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Table) for more information about how to define a table.

  ![Convert to Table dialog - Details tab](https://devnet.logianalytics.com/hc/article_attachments/4404936732439/cnvttbl_dtl.gif)

**To convert to a crosstab:**

A table or chart can be converted to a crosstab. Select the data component and then select ![Convert or drag to add crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404936721559/btn_wbrpt_2crstb.gif) on the visualization toolbar.

* When the data component contains enough data fields required by a crosstab, the crosstab will be generated directly according to the current data fields.
* When the current data fields are not enough for a crosstab, Report Server displays the [Convert to Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009748161-Convert-to-Crosstab) dialog box for you to select more fields to define the crosstab. You can select another business view for the crosstab or use the current one. If the current one is used, select the **Show All Fields** link to show all the objects in the business view. See [Inserting a Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Crosstab) for more information about how to define a crosstab.

  ![Convert To Crosstab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942458775/cnvtcrstb.gif)

**To convert to a chart:**

A table or crosstab can be converted to a chart. One chart type can also be converted to another. Select the data component and then select the desired chart type button on the visualization toolbar.

* When the data component contains enough data fields required by the target chart type, the chart will be generated directly according to the current data fields.
* When the current data fields are not enough for the target chart type, Report Server displays the [Convert to Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009748141-Convert-to-Chart) dialog box for you to select more fields to define the target chart type. You can select another business view for the chart or use the current one. If the current one is used, select the **Show All Fields** link to show all the objects in the business view. See [Inserting a Chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009751501-Inserting-Components#Chart) for more information about how to define a chart.

  ![Convert To Chart dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942459031/cnvtcht.gif)

**To convert a table to a banded object:**

A table that is not in any banded object can be converted to a banded object. To do this, select the data component and then select ![Convert or drag to add banded object button](https://devnet.logianalytics.com/hc/article_attachments/4404942449687/btn_wbrpt_2bd.gif) on the visualization toolbar, the table will be converted to a banded object automatically.

## Saving a Data Component as a Library Component

You can save the tables, crosstabs, charts, KPIs and geographic maps in a web report (not a [shared one](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports)) as library components and then use them in [dashboards](https://devnet.logianalytics.com/hc/en-us/articles/1500009745021-Creating-and-Saving-Dashboards) directly.

1. Right-click the icon ![Drag icon](https://devnet.logianalytics.com/hc/article_attachments/4404942451735/btn_pgrpt_drag.gif) of a data component and select **Save as Library Component** from the shortcut menu. Report Server displays the [Save As](https://devnet.logianalytics.com/hc/en-us/articles/1500009749441-Save-As#LC) dialog box.

   ![Save As dialog - Library Component](https://devnet.logianalytics.com/hc/article_attachments/4404942459287/svas_lc.gif)
2. In the Save In section, browse to the folder in the server resource tree where you want to save the library component. You can use the ![Up Level button](https://devnet.logianalytics.com/hc/article_attachments/4404936723607/btn_wbrpt_up.gif) button to return to the parent folder.

   If My Components or its subfolder is selected, only the current user can access and use the library component in dashboards. If a public folder is selected, the library component will be treated as a public resource and inherit user permissions from the report.
3. In the File Name box, type the name of the library component or use the default name. The default file type is Library Component.
4. You can select the **Advanced** button to set advanced settings for the library component.
   1. Specify the relationship between the library component and the catalog used to run it. By default the library component is linked to its catalog in which way it can always run with the latest version of the catalog. You can also choose to copy the catalog to the directory where the library component is saved by selecting the **Set Catalog Copy to Target Folder** option.

      There should be only one catalog per folder so if there is already a catalog in the folder where you are going to copy the catalog to, it may cause other library components in the folder not to be able to run as they may use the wrong catalog. Also, if there is a newer version of the same catalog in the target folder, it will be overwritten and existing library components that use it will not be able to run with the newer catalog version. Therefore, it is always better to link the catalog rather than copy it.
   2. If you want to save the library component together with the sort and filter criteria, select **Save Sort Criteria** and **Save Filter Criteria** correspondingly. Then Web Report Studio will automatically apply the criteria to the library component the next time it is opened.
   3. Optionally, type comments in the Description box as a description for the library component.
5. Select **OK** to convert the data component to a library component and save the library component. Then select **OK** in the Confirm dialog box.

If you are saving to an existing library component, Report Server will display a Confirm dialog box asking whether you want to replace it or [save a new version into it](https://devnet.logianalytics.com/hc/en-us/articles/1500009750221-Creating-Versions#Save).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751521-Making-Simple-Modifications-to-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724822-Adding-Links-in-a-Report)
