---
title: "Modifying Tables"
id: 1500010029302
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010029302-Modifying-Tables
updated_at: 2021-07-24T10:39:19Z
---

# Modifying Tables

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063941-Inserting-Tables-in-a-Report-) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables)

# Modifying Tables

For any table in a report, you can further modify it at any time. For example you can change the data displayed in the table, summarize the data in a detail column of the table, and so on.

This topic introduces modifying a table as follows:

* [Editing a Table with Wizard](#Edit)
* [Sorting the Detail Data](#Sort)
* [Inserting Columns and Rows](#Insert)
* [Converting Columns](#Convert)
* [Aggregating on the Detail Columns](#Aggregate)
* [Showing/Hiding the Summaries](#Summary)
* [Formatting Cells](#Cell)
* [Resizing the Columns and Rows](#Resize)
* [Showing, Hiding, and Deleting the Columns/Rows](#Show)

**Tip:** Some table operations require to use the shortcut menu on table cells, however when a table cell is entirely occupied by another object, it would be difficult to access its shortcut menu. In this case, you can resize the object in the cell first, then in the Report Inspector, select the node representing the cell that holds the object to select the cell itself, after that you can right-click on the blank area in the cell to get the shortcut menu.

## Editing a Table with Wizard

Once a table has been created, you can further modify it by accessing its shortcut menu wizard which is composed by a set of screens that are similar to the wizard screens used to create the table. For example, you can change the data used by the table, edit the groups in the table, and so on.

1. Right-click the table and select **Table Wizard** from the shortcut menu to display the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500010068221-Table-Wizard-Dialog).
2. In the Data screen, specify a new data source for the table if required.
3. In the Display screen, specify the detail fields to display in the table. Use the button ![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif) to replace any current field. Select the **Sort Fields By** button to specify in which manner to [sort the detail values](#Sort).
4. In the Group screen, specify the criteria for [grouping data in the table](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables).
5. In the Style screen, select the style you want to apply to the table.
6. Select **Finish** to accept the changes.

For more detailed information about defining a table, see [Inserting Tables in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010063941-Inserting-Tables-in-a-Report-).

## Sorting the Detail Data

By default, the detail records in a table are displayed randomly; they are displayed in the order they are returned from the fetch operation. You can specify that Logi JReport sort the records in a table, and also within the groups in the table if any.

1. When creating or editing a table with the table wizard, select the **Sort Fields By** button in the Display screen. The [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500010067861-Sort-Fields-By-Dialog) dialog appears.

   ![Sort Fields By dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901180055/sortfldby.gif)
2. From the Resources box, select a field as the sort-by field and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or drag and drop it to the right box.
   * For a table created using a business view, you can choose from the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404901314071/bv_grp.gif) and detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404901314327/bv_detail.gif) in the business view the table uses, as well as the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404901314583/bv_dynfmla_grp.gif) and dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404909271703/bv_dynfmla_dtl.gif) created for the business view in the current report.
   * For a table created using a query resource in a page report, you can choose from the DBFields in the query resource and the formulas and parameters valid to the DBFields in the current catalog. For the usage about parameters as sort-by fields, see [Sorting Data Dynamically](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases#Sort).
3. From the drop-down list in the Sort column, specify in which manner to sort the field, Ascend or Descend.
4. Add more sort-by fields and specify the sort manner of each field using the same way. Select ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) to adjust the order of the sort-by fields, which will determine the sort priority of the fields at runtime. If a sort-by field is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)** or drag and drop it to the Resources box.
5. Select **OK** to accept the sort settings.

   For example, if a table displays the detail fields for product quantity and cost and you want to sort the detail values first by quantity ascending and then cost descending. You can specify the sort manner as follows:

   ![Sort By Fields](https://devnet.logianalytics.com/hc/article_attachments/4404901314839/cmpnt_table_mdfy_srt1.gif)

   And the results will be:

   ![Sort Results](https://devnet.logianalytics.com/hc/article_attachments/4404901315095/cmpnt_table_mdfy_srt2.gif)

**Note:** The following SQL type of data cannot be sorted: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.

## Inserting Columns and Rows

Besides using the table wizard to create the columns and rows in a table, you can also insert columns and [rows](#InsertRow) directly using the Insert Column/Row feature. A table can contain the following types of columns: [group columns](#GroupColumn), [detail columns](#DetailColumn), [summary columns](#SumColumn) and [common columns](#CommonColumn).

**To insert a group column:**

1. Select the table or a column in the table, right-click it, then select **Insert** > **Group Column** on the shortcut menu. The [Insert Group Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010031462-Insert-Group-Column-Dialog) dialog appears, with the existing groups the table contains listed in an indented structure in the right box. You can edit the groups if you want.

   ![Insert Group Column](https://devnet.logianalytics.com/hc/article_attachments/4404901204887/instgrpclmn.gif)
2. In the right box, select the group level of the new group column by selecting Table or an existing group, then select a data field in the Resources box as the group-by field and
   select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or drag and drop it to the right box.
   * For a table created using a business view, you can select from the group objects in the business view, as well as the [dynamic formulas used as Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) created for the business view in the current report.
   * For a table created using a query resource, you can select from the DBFields in the query resource, as well as the formulas and parameters valid to these DBFields in the current catalog. For the usage about parameters as group-by fields, see [Grouping Data Dynamically](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases#Group).
3. In the Sort column, set the [sort manner](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Sort) of groups at this group level.
4. Specify the position of the group-by field in the table:
   * **Table (Group Above**)  
      Specifies to place the group-by field in its own row above the detail information.
   * **Table (Group Left Above**)  
      Specifies to place the group-by field in its own row and column above and left of the detail information.
   * **Table (Group Left**)  
      Specifies to place the group-by field in its own column left of the detail information.
5. If the table is created using a query resource, you can also specify the following:
   * Select the **Select N** button to specify the [Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#SelectN) for the group level.
   * Select the **Group Filter** button to specify the filter condition to [filter groups](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Filter) at this group level.
   * If the group-by field is of Numeric/String/Date/Time type, select a [special function](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables#Function) for it from the Special Function drop-down list.
6. Repeat the above steps to add more group columns if required. You can make use of the ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) buttons to adjust the group levels.
7. Select **OK** to insert the group columns.

**To insert a detail column:**

1. Select the table or a column in the table, right-click it, then select **Insert** > **Detail Column** on the shortcut menu. The [Insert Detail Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010066881-Insert-Detail-Column-Dialog) dialog appears.

   ![Insert Detail Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901206167/instdtlclmn.gif)
2. Select the data field you want to use for the detail column.

* For a table created using a business view, you can select from the group objects and details objects in the business view, as well as the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) used as Group or Detail created for the business view in the current report.
* For a table created using a query resource, you can select from the DBFields in the query resource, as well as the formulas and parameters valid to these DBFields in the current catalog.

3. Select **OK**. A new detail column is inserted in the table and where it is placed depends on the following: if you use the column shortcut menu to insert the column, the new column is placed before the selected column; if you use the table shortcut menu to insert the column, it is placed after the last detail column, or as the last column in the table when there is no detail column.

**To insert a summary column:**

1. Select the table or a column in the table, right-click it, then select **Insert** > **Summary Column** on the shortcut menu. The [Insert Summary Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010066981-Insert-Summary-Column-Dialog) dialog appears.

   ![Insert Summary Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909177367/instsumclmn.gif)
2. Select the data field you want to use for the summary column.

* For a table created using a business view, you can select from the aggregation objects in the business view, as well as the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula)  used as Aggregation and [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg) created for the business view in the current report.
* For a table created using a query resource, you can select from the dynamic summaries in the current catalog that are valid to the DBFields in the query resource, as well as the static summaries without group-by fields or based on the same group-by fields as these in the table if the table contains groups. The formulas that are valid to the summaries are also available in the resource list.

3. Select **OK**. A new summary column is inserted in the table which calculates data as follows:
   * For a table created using a business view,
     if it is a summary table in a web report or library component, the summary column calculates data based on the innermost group of the table and the whole table; otherwise the summary column calculates data based on each group of the table and the whole table.
   * For a table created using a query resource, when the selected summary is a dynamic summary, the summary column calculates data based on each group of the table and the whole table; when the summary is a static summary with a group-by field, the summary column calculates data based on the same group in the table; for a static summary without a group-by field, the summary column calculated data based on the whole table.

   Where the new summary column is placed in the table depends on the following: if you use the column shortcut menu to insert the column, the new column is placed before the selected column; if you use the table shortcut menu to insert the column, it is placed after the last summary column, or as the last column in the table when there is no summary column.

**To insert a common column:**

* Select a cell in the table, right-click it and select **Insert** on the shortcut menu. In the Insert dialog, specify where the column will be inserted, before or after the selected cell, then select **OK**. A new common column will then be inserted into the table in the position you specify.
* Select a column in the table, right-click it, then on the shortcut menu, select **Insert** > **Common Column**. A new common column will then be inserted before the selected column.
* Select the table, right-click it, then on the shortcut menu, select **Insert** > **Common Column**. A new common column will then be inserted as the last column in the table.

You can then drag the required data fields from the Data panel or objects allowed for table cell from the Components panel into the column.

**To insert a row:**

1. Select a cell or a row in the table, right-click it and then select **Insert** on the shortcut menu.
2. In the Insert dialog, specify where the row will be inserted, above or below the selected cell.

   ![Insert](https://devnet.logianalytics.com/hc/article_attachments/4404909271959/cmpnt_table_clmn1.gif)
3. Select **OK**. A new row of the same type is then inserted into the table according to the specified position. You can drag the required data fields from the Data panel or objects allowed for table cell from the Components panel into the row.

## Converting Columns

You can convert the group columns into detail columns. For a detail column, when the field in it can be used as group-by field, you can also convert it to a group column.

**To convert a group column into a detail column:**

Select the group column, right-click it, and select **Convert to Detail** from the shortcut menu, then the conversion is done.

**To convert a detail column into a group:**

1. Select the detail column you want to convert, right-click it and select **Convert to Group** from the shortcut menu (the menu option is disabled when the field in the selected detail column has already been used as group-by field in the table).
2. In the Select Group Position dialog, specify the position for the newly converted group-by field.

   ![Select Group Position](https://devnet.logianalytics.com/hc/article_attachments/4404901180567/slctgrppstn.gif)

   * **Group Above**  
      If selected, a new group header panel is added to hold the group-by field and the detail column is removed.
   * **Group Left Above**  
      If selected, the detail column is converted to a group column and a new group header panel is added to hold the group-by field.
   * **Group Left**  
      If selected, the detail column is converted to a group column and the group-by field is added to the left of the detail field in the same column.
3. Select **OK** to save the changes.

## Aggregating on the Detail Columns

You can calculate data based on any detail column in a table if required.

1. Right-click the detail column and select **Aggregate On** from the shortcut menu. The [Aggregate On](https://devnet.logianalytics.com/hc/en-us/articles/1500010064801-Aggregate-On-Dialog) dialog appears.

   ![Aggregate On](https://devnet.logianalytics.com/hc/article_attachments/4404901294871/agrgton.gif)
2. From the Aggregate Function drop-down list, specify the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function) to calculate the field in the detail column. When DistinctSum is selected, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.
3. Specify the Group By option.
   * If the table has groups and you want the summary to be applied on certain group level, check **Group By** and select the corresponding group-by field from the drop-down list below.
   * If you want the summary to be applied on the whole dataset, check **Group By** and do not select any field from the drop-down list below.
   * If you want to create a dynamic summary, keep **Group By** unchecked. Then the summary will be applied on every group level and the whole dataset at the same time.
4. Select **OK**. Data in the detail column will be calculated based on the group-by setting using the specified function.

Then:

* For a table that is created using a query resource in a page report, a [summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries) which is given a default name Function\_DetailFieldName will be created and saved into the current catalog.
* For a table that is created using a business view, a [dynamic aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg) which is given a default name Function\_DetailFieldName will be created in the current report.

## Showing/Hiding the Summaries

When creating or editing a summary table via the table wizard in a web report or library component, once you have added any summary on its table header/footer or group header/footer, after the table is generated the Show Summary Field command will be activated on the shortcut menu of all the summary columns in the table. You can use the menu command to show or hide the summaries in the headers/footers.

1. Right-click the summary column that contains the required summary.
2. From the Show Summary Field submenu select/deselect the corresponding table/group header/footer to show/hide the summary on the specified locations.

   The summary will be placed in the intersection of its summary column and the table/group headers/footers.

## Formatting Cells

* To merge cells in the group header/group footer/table footer, select adjacent cells, right-click and select **Merge** (or select **Home** > **Merge**).
* To unmerge cells, right-click it and select **Unmerge** from the shortcut menu. The cell will then be split into multiple cells.

  Unmerging is the reverse operation to merging, and therefore only previously merged cells can be unmerged.
* To format the borders of a table cell, take the following steps:
  1. Right-click the cell and select **Format Border** from the shortcut menu. The [Format Cell](https://devnet.logianalytics.com/hc/en-us/articles/1500010066341-Format-Cell-Dialog) dialog appears.

     ![Format Cell](https://devnet.logianalytics.com/hc/article_attachments/4404901248023/fmtcell.gif)
  2. Specify whether the borders will be displayed or not by checking None, Box or Custom. If Custom is checked, you can select ![Left Border button](https://devnet.logianalytics.com/hc/article_attachments/4404901315351/btn_lftbrdr.gif), ![Right Border button](https://devnet.logianalytics.com/hc/article_attachments/4404901315607/btn_rtbrdr.gif), ![Top Border button](https://devnet.logianalytics.com/hc/article_attachments/4404909272215/btn_tpbrdr.gif), or ![Bottom Border button](https://devnet.logianalytics.com/hc/article_attachments/4404901315863/btn_btmbrdr.gif) to set the visible/invisible status of the left, right, top, or bottom border.
  3. Specify the border color from the Color drop-down list. If you want to [use a formula to control the color](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties), select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) and select a formula from the drop-down list.
  4. Set the border style in the Style list box.
  5. When done, select **OK** to accept the changes.

## Resizing the Columns and Rows

You have the following ways to resize the columns/rows in a table:

* To resize a column, drag the boundary on the right side of the column to the required width. If the boundary is not the rightmost one, the column width will change, but the total width of the table will not change. If you want to change both the column width and the table width, press the Shift button on the keyboard while dragging. To resize a row, drag the boundary below the row to the required height. Both the row height and the table height will change. If you want to change just the row height, press the Shift button on the keyboard while dragging the boundary.
* Select a table cell, change its Height or Width property in the Report Inspector, or right-click it, select **Row Height** or **Column Width** from the shortcut menu, then in the corresponding dialog, type a value and select **OK**. The height/width of the row/column in which the cell is located will then be changed according to your specification.
* Select a column/row, right-click it and select **Column Width**/**Row Height** from the shortcut menu. In the Column Width/Row Height dialog, type a value in the text box and select **OK**. The width/height of the column/row will then be changed according to your specification.

## Showing, Hiding, and Deleting the Columns/Rows

**To specify which columns you want to show in a table:**

1. Right-click the table and select **Show Column** from the shortcut menu. The [Show Column](https://devnet.logianalytics.com/hc/en-us/articles/1500010067721-Show-Column-Dialog) dialog appears.

   ![Show Column](https://devnet.logianalytics.com/hc/article_attachments/4404909157271/shwcol.gif)
2. All the columns in the table are listed, with text in cells of the table header panel representing corresponding columns. By default, the columns are listed according to their order in the table. Check **Auto Sort** if you want them to be listed alphabetically.
3. Check the checkboxes ahead of the columns you want to show.
4. Select **OK** to accept the changes.

**To hide a table row:**

Select the row, right-click it, and select **Hide** from the shortcut menu.

**To hide a table column:**

* Select the column to be hidden, right-click it, and select **Hide Column** from the shortcut menu.
* Select the table, right-click it and select **Show Column** from the shortcut menu. In the Show Column dialog, uncheck the column to be hidden.
* Select the cell in the table header, which is in the column you want to hide, right-click the cell and select **Hide Column** from the shortcut menu. If the table has more than one header panel, use the header in the first row to access the Hide Column command.

**To delete a column/row:**

* Select the specific column or row to be deleted, right-click it and select **Delete** from the shortcut menu to delete it.
* Select a cell which is in the column/row to be deleted, right-click it, and then select **Delete** from the shortcut menu. In the Delete dialog, select **Column** or **Row**, select **OK**. The column or row is then deleted from the table.

**Note:** When a table is created, by default its structure is fixed and no row can be deleted. If you want to delete a row, you need to [insert a same row](#InsertRow) first by using the shortcut menu, then you can delete the original row.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063941-Inserting-Tables-in-a-Report-) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables)
