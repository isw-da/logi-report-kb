---
title: "Managing Cells, Columns, and Rows in a Table"
id: 1500009584301
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584301-Managing-Cells-Columns-and-Rows-in-a-Table
updated_at: 2021-07-24T05:55:57Z
---

# Managing Cells, Columns, and Rows in a Table

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584281-Using-Customized-Controls-in-a-Table)

# Managing Cells, Columns, and Rows in a Table

This topic introduces how to manage cells, columns, and rows in table.

**Tip:** When a table cell is entirely occupied by another object, it would be difficult to access its shortcut menu. You can resize the object in the cell first, then in the Report Inspector, select the node representing the cell that holds the object to select the cell itself. After that, you can right-click on the blank area in the cell to get the shortcut menu.

Below is a list of the sections covered in this topic:

> * [Formatting Table Cells](#Cell)
> * [Resizing a Column/Row](#Resize)
> * [Inserting a Row](#Row)
> * [Inserting a Column](#Column)
> * [Converting a Column](#Convert)
> * [Showing Certain Columns](#Show)
> * [Hiding a Column/Row](#Hide)
> * [Deleting a Column/Rrow](#Delete)

## Formatting Table Cells

* To merge cells in the group header/group footer/table footer panel, select adjacent cells, right-click and select **Merge** (or select **Home** > **Merge**).
* To unmerge cells, right-click it and select **Unmerge** from the shortcut menu. The cell will then be split into multiple cells.

  Unmerging is the reverse operation to merging, and therefore only previously merged cells can be unmerged.
* To format the borders of a table cell, take the following steps:
  1. Right-click the cell and select **Format Border** from the shortcut menu. The [Format Cell](https://devnet.logianalytics.com/hc/en-us/articles/1500009587121-Format-Cell-Dialog) dialog appears.

     ![Format Cell dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889354775/fmtcell.gif)
  2. Specify whether the borders will be displayed or not by checking None, Box or Custom. If Custom is checked, you can select ![Left Border button](https://devnet.logianalytics.com/hc/article_attachments/4404889405591/btn_lftbrdr.gif), ![Right Border button](https://devnet.logianalytics.com/hc/article_attachments/4404889406103/btn_rtbrdr.gif), ![Top Border button](https://devnet.logianalytics.com/hc/article_attachments/4404889406359/btn_tpbrdr.gif), or ![Bottom Border button](https://devnet.logianalytics.com/hc/article_attachments/4404889406615/btn_btmbrdr.gif) to set the visible/invisible status of the left, right, top, or bottom border.
  3. Specify the border color from the Color drop-down list. If you want to use a formula to control the color, select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) and select a formula from the drop-down list. If the given formulas cannot meet your requirements, select **<Create Formula>** to [create one](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula).
  4. Set the border style in the Style list box.
  5. When done, select **OK** to accept the changes.

## Resizing a Column/Row

You can take one of the following ways to resize columns/rows of a table:

* To resize a column, drag the boundary on the right side of the column to the required width. If the boundary is not the rightmost one, the column width will change, but the total width of the table will not change. If you want to change both the column width and the table width, press the Shift button on the keyboard while dragging. To resize a row, drag the boundary below the row to the required height. Both the row height and the table height will change. If you want to change just the row height, press the Shift button on the keyboard while dragging the boundary.
* Select a table cell, change its Height or Width property in the Report Inspector, or right-click it, select **Row Height** or **Column Width** from the shortcut menu, then in the corresponding dialog, type a value and select **OK**. The height/width of the row/column in which the cell is located will then be changed according to your specification.
* Select the column/row, right-click it and select **Column Width**/**Row Height** from the shortcut menu. In the Column Width/Row Height dialog, type a value in the text box and select **OK**. The width/height of the column/row will then be changed according to your specification.

## Inserting a Row

1. Select a cell or a row in the table, right-click it and then select **Insert** on the shortcut menu.
2. In the Insert dialog, specify where the row will be inserted, above or below the selected cell.

   ![Insert dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893981207/cmpnt_table_clmn1.gif)
3. Select **OK**. A new row of the same type is then inserted into the table according to the specified position.

## Inserting a Column

A table can have the following types of columns: common column, summary column, detail column and group column. You can insert any type of column into a table.

**To insert a common column:**

* Select a cell in the table, right-click it and select **Insert** on the shortcut menu. In the Insert dialog, specify where the column will be inserted, before or after the selected cell, then select **OK**. A new common column will then be inserted into the table in the position you specify.
* Select a column in the table, right-click it, then on the shortcut menu, select **Insert** > **Common Column**. A new common column will then be inserted before the selected column.
* Select the table, right-click it, then on the shortcut menu, select **Insert** > **Common Column**. A new common column will then be inserted as the last column in the table.

**To insert a detail/summary column:**

1. Select the table or a column in the table, right-click it, then select **Insert** > **Detail Column**/**Summary Column** on the shortcut menu.
2. In the corresponding insert column dialog, specify the resource you want to use for the new column.
3. Select **OK**. A new detail/summary column will then be inserted. However the position to which the column will be inserted differs according to where the shortcut menu is accessed. If you use the column shortcut menu to insert the column, the new column will be placed before the selected column; if you use the table shortcut menu to insert the column, it will be placed after the last detail/summary column, or as the last column in the table when there is no detail/summary column.

**To insert a group column:**

1. Select the table or a column in the table, right-click it, then select **Insert** > **Group Column** on the shortcut menu. The [Insert Group Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009587621-Insert-Group-Column-Dialog) dialog appears.

   ![Insert Group Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893873431/instgrpclmn.gif)
2. In the Resources box, select the field you want to use for the new group column and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it as the group by field, then specify the sorting direction of the newly added group in the Sort column, and if the type of the added field is Numeric/String/Date/Time, select a special function for the field from the Special Function column as required (for details, see [Group the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data)).
3. Specify the position of the group by field: Group Above, Group Left Above, or Group Left.
4. Repeat the above two steps to add more group columns if required.
5. Select **OK** to insert the group columns.

   The next time when you open the Insert Group Column dialog to add more group columns, all the added group by fields will be listed in the dialog. You can choose to remove or edit them if required.

## Converting a Column

You can convert a group column into a detail column. For a detail column, when the field in it can be used as group by field, you can also convert it to a group.

* To convert a group column into a detail column, select the group column, right-click it, and select **Convert to Detail** from the shortcut menu, then the conversion is done.
* **To convert a detail column into a group:**
  1. Select the detail column you want to convert, right-click it and select **Convert to Group** from the shortcut menu (the menu option is disabled when the field in the selected detail column has already been used as group by field in the table).
  2. In the Select Group Position dialog, specify the position for the newly converted group by field.

     ![Select Group Position dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889320727/slctgrppstn.gif)

     + **Group Above**  
        If selected, a new group header row is added to hold the group by field and the detail column is removed.
     + **Group Left Above**  
        If selected, the detail column is converted to a group column and a new group header row is added to hold the group by field.
     + **Group Left**  
        If selected, the detail column is converted to a group column and the group by field is added to the left of the detail field in the same column.
  3. Select **OK** to save the changes.

## Showing Certain Columns

1. Right-click the table and select **Show Column** from the shortcut menu. The [Show Column](https://devnet.logianalytics.com/hc/en-us/articles/1500009567362-Show-Column-Dialog) dialog appears.

   ![Show Column dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893855895/shwcol.gif)
2. All the columns in the table are listed, with text in cells of the table header row representing corresponding columns. By default, the columns are listed according to their order in the table. Check **Auto Sort** if you want them to be listed alphabetically.
3. Check the checkboxes ahead of the columns you want to show.
4. Select **OK** to accept the changes.

## Hiding a Column/Row

To hide a table row, select the row, right-click it, and select **Hide** from the shortcut menu.

To hide a table column, you can use any of the following methods:

* Select the column to be hidden, right-click it, and select **Hide Column** from the shortcut menu.
* Select the table, right-click it and select **Show Column** from the shortcut menu. In the Show Column dialog, uncheck the column to be hidden.
* Select the cell in the table header, which is in the column you want to hide, right-click the cell and select **Hide Column** from the shortcut menu. If the table has more than one header row, use the header in the first row to access the Hide Column command.

## Deleting a Column/Row

Take either of the following methods:

* Select the specific column or row to be deleted, right-click it and select **Delete** from the shortcut menu to delete it.
* Select a cell which is in the column/row to be deleted, right-click it, and then select **Delete** from the shortcut menu. In the Delete dialog, select **Column** or **Row**, select **OK**. The column or row is then deleted from the table.

**Note:** When a table is created, by default its structure is fixed and no row can be deleted. If you want to delete a row, you need to [insert a same row](#Row) first by using the shortcut menu, then you can delete the original row.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584281-Using-Customized-Controls-in-a-Table)
