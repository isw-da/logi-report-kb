---
title: "Working with Logi Report Studio"
id: 9905923717783
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9905923717783-Working-with-Logi-Report-Studio
updated_at: 2022-10-31T17:15:21Z
---

# Working with Logi Report Studio

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741463138711-Page-Report-Studio-Tag-Library)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741387513879-Introduction-to-the-Logi-Report-JDashboard-Logi-Report-Server-v19)

# This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Working with Logi Report Studio

Logi Report provides a template editor - Logi Report Studio for building reports more intuitively and conveniently. This topic describes how to use Logi Report Studio.

For more information about how to access Logi Report Studio, see [Enabling and Accessing Template Editor Logi Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/9905923782039-Enabling-and-Accessing-Template-Editor-Logi-Report-Studio).

![Logi Report Studio](https://devnet.logianalytics.com/hc/article_attachments/9905931573783/lrstudio.gif)

This topic contains the following sections:

* [Using Toolbar Buttons](#Toolbar)
* [Using the Components Panel](#ComponentsPanel)
* [Inserting a Summary Table](#InsertSummaryTable)
* [Inserting a Group Type Table](#InsertGroupTable)
* [Working with Tables](#WorkTable)
* [Inserting Columns in a Table](#InsertTableColumn)
* [Inserting a Banded Object](#InsertBanded)
* [Working with Banded Objects](#WorkBanded)
* [Inserting a Crosstab](#InsertCrosstab)
* [Working with Crosstabs](#WorkCrosstab)
* [Inserting a Blank Data Component](#BlankComponent)
* [Inserting a Label](#InsertLabel)
* [Inserting an Image](#InsertImage)
* [Inserting a Tabular](#InsertTabular)
* [Updating Object Properties Using Inspector](#Inspector)
* [Setting Up Data Container Links](#DataContainerLink)
* [Changing Component Position](#Position)
* [Moving Objects by Dragging](#Move)
* [Resizing Objects](#ResizeObject)
* [Removing Objects](#Remove)
* [Returning to Page Report Studio](#Return)

## Using Toolbar Buttons

The following table describes how you can use the buttons on the toolbar of Logi Report Studio.

| Button | Description |
| --- | --- |
| Undo button Undo | Select to undo the last operation. |
| Redo button Redo | Select to reverse the operation of **Undo**. |
| Delete button Delete | Select to remove the selected objects. |
| Font Face button Font Face | Select to update the font face of the selected text, label, or field. |
| Font Size button Font Size | Select to update the size of the selected text, label, or field. |
| Bold button Bold | Select to make the selected text, label, or field bold. |
| Italic button Italic | Select to make the selected text, label, or field italic. |
| Underline button Underline | Select to underline the selected text, label, or field. |
| Strikethrough button Strikethrough | Select to add a strikethrough to the selected text, label, or field. |
| Background Color button Background Color | Select to open the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/9905934902295-Color-Picker-Dialog-Box-Properties) in which you can specify a background color for the selected text, label, or field. |
| Foreground Color button Foreground Color | Select to open the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/9905934902295-Color-Picker-Dialog-Box-Properties) in which you can specify a foreground color for the selected text, label, or field. |
| Align Left button Left | Select to align the content in the specified object to the left border of the object. |
| Align Center button Center | Select to align the content in the specified object to the center of the object. |
| Align Right button Right | Select to align the content in the specified object to the right border of the object. |
| Justify button Justify | Select to adjust the horizontal spacing so as to align the content evenly along both the left and right margins in the specified object. |
| Merge button Merge | Select to merge the selected adjacent tabular or table cells that form a rectangular into one cell. |
| Unmerge button Unmerge | Select to unmerge the table cells that you merged. |
| Split button Split | Server enables the Split button when you select a tabular cell. Select the Split button and then select an item from the drop-down menu:   * **Horizontal**  Select to split the selected cell into two cells horizontally. * **Vertical**  Select to split the selected cell into two cells vertically. * **2x2**  Select to split the selected cell into four cells with two rows and two columns. |
| Resources Panel button Resources Panel | Select/Clear to display/close the Resources panel. |
| Components Panel button Components Panel | Select/Clear to display/close the Components panel. |
| Inspector Panel button Inspector Panel | Select/Clear to display/close the Inspector panel. |
| Return button Return | Select to [return to Page Report Studio](#Return). |

## Using the Components Panel

The Components panel displays all the components that you can add to your reports.

![Components panel](https://devnet.logianalytics.com/hc/article_attachments/9905903821591/lrstudio_cmpntpnl.gif)

You can search for components in the Components panel easily using the search bar. Type the keyword. Server displays the components that contains the keyword.

You can display the components in the Components panel in either the list view or grid view by selecting the List View button ![List View button](https://devnet.logianalytics.com/hc/article_attachments/9905903868951/btn_lrstd_lstvw.gif) or Grid View button ![Grid View button](https://devnet.logianalytics.com/hc/article_attachments/9905932204567/btn_lrstd_grdvw_29x29.gif) on the right of the search bar. In the grid view, server displays the icons of the items. In the list view, Server displays the icons and names of the items.

## Inserting a Summary Table

1. Drag **Summary Table** in the **Grid** category from the [Components panel](#ComponentsPanel) to the template edit area. Server displays the Format Summary Table panel on the left of the template edit area.

   ![Format Summary Table panel](https://devnet.logianalytics.com/hc/article_attachments/9905932227223/lrstudio_fmtsmrytbl.gif)
2. From the drop-down menu in the Resources panel, select a business view or dataset from which you want to add data to the table. Server displays the business view or dataset with its resources.

   ![Select Business View or Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905903942551/lrstudio_slctdtst.gif)

   If you are inserting the table in another data component, by default it will inherit the dataset of the parent data component. In this case, if you want to use a new business view or dataset, clear **Data Inherit** in the Format Summary Table panel, and then you can select a business view or dataset in the Resources panel.
3. You can add group and aggregation objects in summary tables. Drag a group or aggregation object to a Columns line in the Format Summary Table panel.
4. Drag more group and aggregation objects to the Format Summary Table panel.
5. Adjust the order of the group and aggregation fields by dragging one field to above or below another.
6. To sort a group field, select the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905880561047/btn_lrstd_sort.gif) and then select an order from the drop-down list. If you select **Custom Sort**, you can sort the group field according to other fields in the [Custom Sort dialog box](#CustomSort).
7. To remove a field that you added, drag it out of its line.
8. Select **OK**. Server adds the summary table to the template edit area and closes the Format Summary Table panel.

## Inserting a Group Type Table

1. Drag a group type table - **Table (Group Above)**, **Table (Group Left Above)**, or **Table (Group Left)** - in the **Grid** category from the [Components panel](#ComponentsPanel) to the template edit area. Server displays the Format Table panel on the left of the template edit area.

   ![Format Group Table panel](https://devnet.logianalytics.com/hc/article_attachments/9905932278167/lrstudio_fmtgrptbl.gif)
2. From the drop-down menu in the Resources panel, select a business view or dataset from which you want to add data to the table. Server displays the business view or dataset with its resources.

   ![Select Business View or Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905903942551/lrstudio_slctdtst.gif)

   If you are inserting the table in another data component, by default it will inherit the dataset of the parent data component. In this case, if you want to use a new business view or dataset, clear **Data Inherit** in the Format Table panel, and then you can select a business view or dataset in the Resources panel.
3. Drag a group or detail object from the Resources panel to a Detail line in the Format Table panel as a detail field.
4. Follow the previous step to add more detail fields if you want.
5. Adjust the order of the detail fields by dragging one field to above or below another.
6. To sort the added detail fields in the table by the values of other fields, select the **Custom Sort** button ![Custom Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905880519319/btn_lrstd_customsort.gif) and set the sort manner in the [Custom Sort dialog box](#CustomSort).
7. Drag a group object from the Resources panel to a Group line as a group field.
8. Drag more groups if you want.
9. Drag an aggregation object from the Resources panel to a Group line as an aggregation field. To add an aggregation in a group, drag the aggregation under the group field.
10. Add more aggregation fields if you want.
11. By default, Server places aggregations in the table footer if the aggregations are not under any group or in the group footer if the aggregations are under a group. You can change the position between the footer panel and the header panel by selecting between the Footer button ![Footer button](https://devnet.logianalytics.com/hc/article_attachments/9905903990807/btn_lrstd_footer.gif) and header button ![Header button](https://devnet.logianalytics.com/hc/article_attachments/9905904005399/btn_lrstd_header.gif).
12. Adjust the order of the group and aggregation fields by dragging one field to above or below another.
13. To sort a group field in the table, select the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905880561047/btn_lrstd_sort.gif) and then select an order from the drop-down list. If you select **Custom Sort**, you can sort the group field according to other fields in the [Custom Sort dialog box](#CustomSort).
14. To remove a field that you added, drag it out of its line.
15. Select **OK** in the Format Table panel. Server adds the table with the data you selected in the template edit area and closes the Format Table panel.

## Working with Tables

After you add a table in the template edit area, you can drag data fields from the Resources panel to it directly, open the format table panel to update fields, and insert or remove table panels.

**Selecting a table, column, or panel**

Select anywhere in the table. Server displays the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905932356503/btn_lrstd_slctcmpnt_14x14.gif) at the top left of the table, labels for each column (GC/DC/SC/CC), and labels for each panel (TH/GH/TD/GF/TF).

![Display Table Labels](https://devnet.logianalytics.com/hc/article_attachments/9905904044567/lrstudio_tbllbl.gif)

Select ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905904064151/btn_lrstd_slctcmpnt_15x15.gif) to select the table. This also applies to selecting other components when they have the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905932356503/btn_lrstd_slctcmpnt_14x14.gif).

You can select a column by selecting the label of the column. Column labels include GC/DC/SC/CC. **GC** is group column, **DC** detail column, **SC** summary column, and **CC** common column. You can right-click the label of a column to access the shortcut menu of the column.

![Right-click a Table Column](https://devnet.logianalytics.com/hc/article_attachments/9905904077719/lrstudio_rtclcktblclmn.gif)

You can select a panel by selecting the label of the panel. Panel labels include TH/GH/TD/GF/TF. **TH** is table header, **GH** group header, **TD** table detail panel, **GF** group footer, and **TF** table footer. You can right-click the label of a panel to access the shortcut menu of the panel.

**Accessing the format table panel**

[Right-click the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905904099095/btn_lrstd_slctcmpnt.gif) of the table, the label of a panel, or the label of a column](#SelectTable), and then select **Format Data**. Server displays the format table panel. Except that you cannot change the dataset of the table, you can follow the [Inserting a Summary Table](#InsertSummaryTable) or [Inserting a Group Type Table](#InsertGroupTable) section to use the format table panel for a summary table or group table.

![Right-click the Group Table and Select Format Data](https://devnet.logianalytics.com/hc/article_attachments/9905932461335/lrstudio_grptblfmtdt.gif)

**Adding and removing table panels**

To insert a new panel of the same type before or after a panel, or remove a panel, right-click the label of the panel (TH/GH/TD/GF/TF), and then select the corresponding item from the shortcut menu.

![Right-click a Table Panel and Select an Item](https://devnet.logianalytics.com/hc/article_attachments/9905932481559/lrstudio_tblpnl.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)You cannot remove a detail panel (DT) when it is the only detail panel in a table.

When a table has one or more groups, you can add new groups by dragging group fields from the Resources panel. To do this:

1. Select a group header label **GH** in the table to select the group header panel.
2. Drag a group object from the Resources panel to the upper or lower section in the **GH** label until Server displays double green lines above the top border of the panel or below the bottom border of the panel, and then release the mouse.

   ![Drag to Add a Table Group Field](https://devnet.logianalytics.com/hc/article_attachments/9905932509207/lrstudio_drgtblgrp.gif)

   Server displays the new group at a higher level than the selected group.

**Resizing table columns or panels**

You can change the width of a column and the height of a panel in tables by dragging or using the shortcut menu commands.

To adjust the width of a table column, do either:

* Select the label of the column to select the column, hover over the right border of the column until the mouse pointer turns to a double-headed arrow, and then drag the border to adjust the column width.
* Right-click the label of the column, and then select **Column Width**. Server displays the Column Width dialog box. Change the width to a bigger or smaller number to widen or narrow the column.

![Drag a Table Column](https://devnet.logianalytics.com/hc/article_attachments/9905932535191/lrstudio_drgtblclmn.gif)

To adjust the height of a table panel, do either:

* Select the label of the panel to select the panel, hover over the bottom border of the panel until the mouse pointer turns to a double-headed arrow, and then drag the border to adjust the panel height.
* Right-click the label of the panel, and then select **Row Height**. Server displays the Row Height dialog box. Change the height to a bigger or smaller number to increase or decrease the panel height.

![Drag a Table Panel](https://devnet.logianalytics.com/hc/article_attachments/9905932563351/lrstudio_drgtblpnl.gif)

## Inserting Columns in a Table

A table can contain four types of columns: detail column, summary column, group column, and common column. You can insert table columns by either dragging fields from the Resources panel or using shortcut menu commands.

**Inserting table columns by dragging fields**

* To insert a group column in a table, drag a group field from the Resources panel to near the left or right border of a group column label **GC** until Server displays double green lines beside the left or right border of the column, and then release the mouse.

  ![Drag a Group Column into a Summary Table](https://devnet.logianalytics.com/hc/article_attachments/9905904255383/lrstudio_drgsmrytblgrpclmn.gif)

  Server adds the new group column as the top-level group column in the table.

  ![The Result after Dragging a Group Column into a Summary Table](https://devnet.logianalytics.com/hc/article_attachments/9905932636055/lrstudio_drgsmrytblgrpclmnrst.gif)
* To insert a summary column in a summary table, drag an aggregation field from the Resources panel to near the left or right border of a summary column label **SC** until Server displays double green lines beside the left or right border of the column, and then release the mouse. Server adds the new summary column in the table.
* To insert a detail column in a group type table, drag a group/detail/aggregation field from the Resources panel to near the left or right border of a detail column label **DC** until Server displays double green lines beside the left or right border of the column, and then release the mouse. Server adds the new detail column on the left or right of the current column in the table.

**Inserting a blank common column as the last column**

1. Right-click the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905904099095/btn_lrstd_slctcmpnt.gif) of the table and select **Insert** > **Common Column** from the shortcut menu. Server adds a blank common column as the rightmost column in the table.
2. Drag a data field from the Resources panel to the column header to add it in the new column.

**Inserting a blank common column before or after a specific column**

1. [Right-click the label of the column](#SelectTable) and select **Insert** > **Common Column Before**/**Common Column After** from the shortcut menu. Server adds a blank common column before/after the selected column.
2. Drag a data field from the Resources panel to the column header to add it in the new column.

**Inserting a detail or summary column as the last column**

1. Right-click the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905904099095/btn_lrstd_slctcmpnt.gif) of the table, then select **Insert** > **Detail Column**/**Summary Column** from the shortcut menu. Server displays corresponding insert column dialog box.
2. Select the resource you want to use for the new column.

   ![Insert Detail Column dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905904315031/insrtdtlclmn1.gif)
3. Select **OK**.
   Server displays the detail/summary column as the rightmost column in the table.

**Inserting a detail or summary column before or after a specific column**

1. [Right-click the label of the column](#SelectTable) and select **Insert** > **Detail Column**/**Summary Column** from the shortcut menu. Server displays the corresponding insert column dialog box.

   ![Insert Detail Column dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905931041303/insrtdtlclmn.gif)
2. By default, Server selects **Insert Before** which means to place the new column before the selected column. If you want to place the new column after the selected column, select **Insert After**.
3. Select the resource you want to use for the new column.
4. Select **OK**. Server displays the detail/summary column before or after the selected column in the table as you want.

**Updating group columns using the shortcut menu**

1. Right-click [the label of any column](#SelectTable) or the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905904099095/btn_lrstd_slctcmpnt.gif) of the table, then select **Insert** > **Group Column** from the shortcut menu. Server displays the [Insert Group Column dialog box](https://devnet.logianalytics.com/hc/en-us/articles/9905923363479-Insert-Group-Column-Dialog-Box-Properties), with the existing groups the table contains listed in an indented structure in the right box. You can edit the groups if you want.

   ![Insert Group Column dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905902697367/insrtgrpclmn.gif)
2. From the Resource box on the left, select the group object you want to use for the new group column and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905880605463/btn_lrstd_add_29x29.gif) to add it to the right box as the group-by field.
3. Specify the sort direction of the new group in the **Sort** column.
4. Repeat the preceding steps to add more group columns if you want.
5. You can make use of the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905880649751/btn_lrstd_mvup.gif) and **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905880677911/btn_lrstd_mvdown_29x29.gif) to adjust the group levels.
6. Select **OK** to update the group columns.

## Inserting a Banded Object

1. Drag **Banded Object** in the **Grid** category from the [Components panel](#ComponentsPanel) to the template edit area. Server displays the Format Banded panel on the left of the template edit area.

   ![Format Banded panel](https://devnet.logianalytics.com/hc/article_attachments/9905904330775/lrstudio_fmtbanded.gif)
2. From the drop-down menu in the Resources panel, select a business view or dataset from which you want to add data to the banded object. Server displays the business view or dataset with its resources.

   ![Select Business View or Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905903942551/lrstudio_slctdtst.gif)

   If you are inserting the banded object in another data component, by default it will inherit the dataset of the parent data component. In this case, if you want to use a new business view or dataset, clear **Data Inherit** in the Format Banded panel, and then you can select a business view or dataset in the Resources panel.
3. Drag a group or detail object from the Resources panel to a Detail line as a detail field.

   ![Add Detail Field to Banded Object](https://devnet.logianalytics.com/hc/article_attachments/9905904344983/lrstudio_bnddetail.gif)
4. Follow the previous step to add more detail fields if you want.
5. Adjust the order of the detail fields by dragging one field to above or below another.
6. To sort the added detail fields in the banded object by the values of specified fields, select the **Custom Sort** button ![Custom Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905880519319/btn_lrstd_customsort.gif) and set the sort manner in the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/9905923257239-Custom-Sort-Dialog-Box-Properties).

   ![Custom Sort dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905880579223/cstmsrt.gif)

   1. From the Resource box select a field and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905880605463/btn_lrstd_add_29x29.gif) to add it to the right box as the sort-by field. You can remove an added sort-by field by selecting it and then selecting the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9905880622487/btn_lrstd_remove_29x29.gif).
   2. Select a sort order from the **Sort** column. Server sorts the detail fields in the banded object based on the values of the sort-by field in ascending or descending order.
   3. Repeat the preceding two steps to add more sort-by fields.
   4. Select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905880649751/btn_lrstd_mvup.gif) or **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905880677911/btn_lrstd_mvdown_29x29.gif) to adjust the order of the sort-by fields, which defines the sort priority of the fields.
   5. Select **OK** to accept the sort settings.
7. Drag a group object from the Resources panel to a Group line as a group field in the banded object.

   ![Add Group Field to Banded Object](https://devnet.logianalytics.com/hc/article_attachments/9905932720407/lrstudio_bndgrp.gif)
8. Drag more groups if you want.
9. Drag an aggregation object from the Resources panel to a Group line as an aggregation field in the banded object. To add an aggregation in a group, drag the aggregation under the group field.
10. Add more aggregation fields if you want.
11. By default, Server places aggregations in the banded footer if the aggregations are not under any group or in the group footer if the aggregations are under a group. You can change the position between the footer panel and the header panel by selecting between the Footer button ![Footer button](https://devnet.logianalytics.com/hc/article_attachments/9905903990807/btn_lrstd_footer.gif) and header button ![Header button](https://devnet.logianalytics.com/hc/article_attachments/9905904005399/btn_lrstd_header.gif).
12. Adjust the order of the group and aggregation fields by dragging one field to above or below another.
13. To sort a group field in the banded object, select the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905880561047/btn_lrstd_sort.gif) and then select an order from the drop-down list. If you select **Custom Sort**, you can sort the group field according to other fields in the [Custom Sort dialog box](#CustomSort).
14. To remove a field that you added, drag it out of its line.
15. Select **OK** in the Format Banded panel. Server adds the banded object with the data you selected in the template edit area and closes the Format Banded panel.

    ![Display Banded Object](https://devnet.logianalytics.com/hc/article_attachments/9905904384407/lrstudio_bnddsply.gif)

## Working with Banded Objects

After you add a banded object in the template edit area, you can drag data fields from the Resources panel to it directly, open the Format Banded panel to update fields, and hide or insert banded panels.

To access the Format Banded panel, right-click the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905904099095/btn_lrstd_slctcmpnt.gif) at the top left of the banded object or the label of a panel (BH/BPH/GH/DT/GF/BPF/BF), and then select **Format Data**. Server displays the Format Banded panel. Except that you cannot change the dataset of the banded object, you can follow the [Inserting a Banded Object](#InsertBanded) section to use the Format Banded panel.

![Right-click the Banded Object and Select Format Data](https://devnet.logianalytics.com/hc/article_attachments/9905932772247/lrstudio_bndfmtdt.gif)

To hide or remove a panel, or insert a new panel of the same type before or after the panel, right-click the label of the panel (BH/BPH/GH/DT/GF/BPF/BF), and then select the corresponding item from the shortcut menu.

![Right-click a Panel and Select an Item](https://devnet.logianalytics.com/hc/article_attachments/9905932801687/lrstudio_bndpnl.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)You cannot remove a detail panel (DT) when it is the only detail panel in a banded object.

## Inserting a Crosstab

1. Drag **Crosstab** in the **Grid** category from the [Components panel](#ComponentsPanel) to the template edit area. Server displays the Format Crosstab panel on the left of the template edit area.

   ![Format Crosstab panel](https://devnet.logianalytics.com/hc/article_attachments/9905932816663/lrstudio_fmtcrstb.gif)
2. From the drop-down menu in the Resources panel, select a business view or dataset from which you want to add data to the crosstab. Server displays the business view or dataset with its resources.

   ![Select Business View or Dataset](https://devnet.logianalytics.com/hc/article_attachments/9905903942551/lrstudio_slctdtst.gif)

   If you are inserting the crosstab in another data component, by default it will inherit the dataset of the parent data component. In this case, if you want to use a new business view or dataset, clear **Data Inherit** in the Format Crosstab panel, and then you can select a business view or dataset in the Resources panel.
3. Drag group objects one by one to a Column or Row line as the column or row headers.
4. When you see the **Show Total** button ![Show Total button](https://devnet.logianalytics.com/hc/article_attachments/9905932840983/btn_lrstd_shwttl.gif) in a Column or Row line, you can select the button if you want to display the total of the group field. Then, Server changes the button to the **Suppress Total** button ![Suppress Total button](https://devnet.logianalytics.com/hc/article_attachments/9905932869143/btn_lrstd_sprsttl.gif). Later you can select the **Suppress Total** button to not display the total of the group field.
5. To sort a group field, select the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9905880561047/btn_lrstd_sort.gif) and then select an order from the drop-down list. If you select **Custom Sort**, you can sort the group field according to other fields in the [Custom Sort dialog box](#CustomSort).
6. Drag aggregation objects one by one to a Summary line as the summary fields.
7. Adjust the order of the group or aggregation fields by dragging one field to above or below another.
8. To remove a field that you added, drag it out of its line.
9. You can customize the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/5741445839383-Insert-Crosstab-Dialog-Box-Properties#Layout) of the crosstab. Select the double arrow button ![More Options button](https://devnet.logianalytics.com/hc/article_attachments/9905904532375/btn_more.gif) in the Layout line to expand the properties.
10. By default, the crosstab uses vertical layout. You can specify the number of rows to hold the aggregate fields.
11. If you want to use horizontal layout for the crosstab, select **Horizontal Layout**. Then, specify the number of columns to hold the aggregate fields.
12. To hide the grand total row in the crosstab, select **Suppress Row Grand Totals**.
13. To hide the grand total column, select **Suppress Column Grand Totals**.
14. To position the subtotal and grand total columns on the left of the detail aggregations, select **Column Totals On Left**.
15. To position the subtotal and grand total rows on the top of the detail aggregations, select **Row Totals On Top**.
16. Select **OK**. Server adds the crosstab to the template edit area and closes the Format Crosstab panel.

## Working with Crosstabs

After you add a crosstab in the template edit area, you can drag data fields from the Resources panel to it directly, open the Format Crosstab panel to update fields, and more.

To access the Format Crosstab panel, right-click the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905904099095/btn_lrstd_slctcmpnt.gif) at the top left of the crosstab, and then select **Format Data**. Server displays the Format Crosstab panel. Except that you cannot change the dataset of the crosstab, you can follow the [Inserting a Crosstab](#InsertCrosstab) section to use the Format Crosstab panel.

![Right-click the Crosstab and Select Format Data](https://devnet.logianalytics.com/hc/article_attachments/9905932909335/lrstudio_crstbfmtdt.gif)

**Inserting groups and aggregations in a crosstab by dragging fields**

Before inserting fields in crosstabs, first select the crosstab so that Server displays the dataset of the crosstab in the Resources panel for you to select fields from. Also, the row and column labels are available to help you insert row and column headers.

* To insert a column header in a crosstab, drag a group field from the Resources panel to near the left or right border of a group column label **Cn** (n is a number) until Server displays double green lines at the left or right border of the column, and then release the mouse. Server adds the new group column on the left or right of the column.

  ![Drag a Group Column into a Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9905932926231/lrstudio_drgcrstbclmnhdr.gif)
* To insert a row header in a crosstab, drag a group field from the Resources panel to near the top or bottom border of a group row label **Rn** (n is a number) until Server displays double green lines at the top or bottom border of the row, and then release the mouse. Server adds the new group row above or below the row.

  ![Drag a Group Row into a Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9905932945047/lrstudio_drgcrstbrwhdr.gif)
* To insert an aggregation in a crosstab, drag an aggregation field from the Resources panel to an aggregation cell until Server displays double green lines, and then release the mouse. Server adds the new summary where the double green lines was.

  ![Drag an Aggregation into a Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9905932962071/lrstudio_drgcrstbagg.gif)

**Resizing crosstab rows or columns**

You can change the width of a column and the height of a row in crosstabs by dragging.

To adjust the width of a crosstab column, select the label of the column to select the column, hover over the right border of the column until the mouse pointer turns to a double-headed arrow, and then drag the border to adjust the column width.

![Drag a Crosstab Column](https://devnet.logianalytics.com/hc/article_attachments/9905932985495/lrstudio_drgcrstbclmn.gif)

To adjust the height of a crosstab row, select the label of the row to select the row, hover over the bottom border of the row until the mouse pointer turns to a double-headed arrow, and then drag the border to adjust the row height.

![Drag a Crosstab Row](https://devnet.logianalytics.com/hc/article_attachments/9905933006103/lrstudio_drgcrstbrw.gif)

## Inserting a Blank Data Component

You can add a blank data component into your report and then drag data fields into it directly, without using the corresponding Format XXX panel.

1. Follow step 1 and 2 in the [Inserting a Summary Table](#InsertSummaryTable) section to drag a data component and select a dataset for it.
2. Select **OK** in the Format XXX panel. Server adds the data component in the template edit area without data.
3. Drag resources from the Resources panel to the data component as you want.

## Inserting a Label

You can add labels in your report.

1. Drag **Label** in the **Basic** category from the Components panel to the template edit area. Server adds a label.
2. Double-click the label. Server selects the text in the label.
3. Type the text you want.
4. Select outside of the label to accept the new text.
5. Update the font face, font size, font style, background/foreground color, and alignment for the label [using the toolbar](#Toolbar).
6. Update more properties [using the Inspector panel](#Inspector).

## Inserting an Image

You can add images in your report.

1. Drag **Image** in the **Basic** category from the Components panel to the template edit area. Server displays the [Insert Image dialog box](https://devnet.logianalytics.com/hc/en-us/articles/9905923441303-Insert-Image-Dialog-Box-Properties).

   ![Insert Image dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905931086615/insrtimg.gif)
2. Specify the image you want to insert.
   * To use an image in the local file system, select **Local File**. Then select **Browse** to find the image.
   * To use an image on a website, select **Web URL**. Then type or paste the image URL in the **File URL** text box.
   * To use an image in the image library of Server, select **Library**. Then select the image in the **My Pictures** box.
3. Select **OK** to insert the image.

## Inserting a Tabular

You can add tabulars in your report. Drag **Tabular** in the **Basic** category from the Components panel to the template edit area. Server displays a one-cell tabular. Select it and you can then split the tabular using the [Split button ![Split button](https://devnet.logianalytics.com/hc/article_attachments/9905903716631/btn_lrstd_split.gif)](#Split) on the toolbar.

After you select adjacent tabular cells that form a rectangular, you can select the **Merge** button ![Merge button](https://devnet.logianalytics.com/hc/article_attachments/9905903666455/btn_lrstd_merge.gif) to combine the cells into one cell.

## Updating Object Properties Using Inspector

You can update the properties of report objects using the Inspector panel. For more information about the properties, refer to [Setting Report Object Properties Using the Inspector Panel](https://devnet.logianalytics.com/hc/en-us/articles/5741476174999-Setting-Web-Report-Object-Properties-Using-the-Inspector-Panel).

![Inspector panel](https://devnet.logianalytics.com/hc/article_attachments/9905933026199/lrstudio_inspector.gif)

The Inspector panel contains an objects box displaying the objects in the template edit area and a Properties table that has two columns： in the left column are the names of the properties available to the selected object, and in the right column are the values of the properties.

Select an object in the template edit area or an item in the objects box of Inspector, and then specify the values of the properties you want in the Properties table of Inspector. You can use these methods to specify property values:

* Type values manually.
* Select values from the value drop-down lists. When you are specifying a color, Server displays the [Color Picker dialog box](https://devnet.logianalytics.com/hc/en-us/articles/9905934902295-Color-Picker-Dialog-Box-Properties) after you select **Custom**. You can then define a color within a wider range in the dialog box.
* For a Boolean type property, select the left/right end of the radio button in the value field to set the value to false/true.
* Select the formula button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/9905933045655/btn_lrstd_formula.gif), and then select a field from the drop-down list.

In Inspector, you can search for report objects and properties easily using respective search bars. Type the keyword. Server displays the objects or properties that contain the keyword. To clear the keyword, remove it or select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905880426903/btn_lrstd_delete.gif) in the search bar.

You can expand or collapse the report objects in Inspector by selecting the **More Options** button ![More Options button](https://devnet.logianalytics.com/hc/article_attachments/9905904743703/btn_lrstd_ellipsis.gif) on the right of the first search bar and selecting **Expand All** or **Collapse All**.

## Setting Up Data Container Links

When two data containers in a parent-child relationship apply different datasets, you can use a data container link to set up data relation between them.

A data container includes:

* A set of link conditions that dynamically filters data in child data containers.
* A set of parameter links that assign fixed values to parameters of both data containers, so you do not need to specify values for the parameters at runtime.

Generally, a data container link functions the same as a subreport link. The only difference is that you do not need to specify the child component in a data container link, because you have already selected the child data container as the target of the link at the very beginning.

Assume that you have a banded object showing the customer information, then you insert a table into the detail panel of the banded object using another dataset, which displays the order information. Now you want to set up a data link between the banded object and the table, so that when you view the report, you can get a table according to the customer name.

![Data Container Link Example](https://devnet.logianalytics.com/hc/article_attachments/9905904769175/lrstudio_cntnrlnk1.gif)

You can achieve this by taking the steps:

1. Select the table and right-click it.
2. On the shortcut menu, select **Data Container Link**. Server displays the [Link Data Container dialog box](https://devnet.logianalytics.com/hc/en-us/articles/9905935219607-Link-Data-Container-Dialog-Box-Properties).
3. In the **Condition** tab, select the **Customer Name** field from the dataset of the banded object in the left box.
4. Select the Add button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905931174039/btn_lrstd_add.gif).
5. In the right box, Server applies the "=" operator by default.
6. Select **Customer Name** from the drop-down list in the **Fields (Child)** column. A link condition based on the Customer Name field is now created between the two data components.

   ![Set Data Container Link Condition Based on Customer Name](https://devnet.logianalytics.com/hc/article_attachments/9905904794391/lrstudio_cntnrlnk2.gif)
7. Select **OK** to apply the link.

## Changing Component Position

Report templates use a flow layout model. That is, paragraphs and components in the report body can flow from one page to another, maintaining their sequence, and the Position property controls whether a component is a part of the flow or separates from it. Besides the report body, tabular cells, text boxes, and KPIs can also act as flow layout containers.

In a flow layout container, Server positions objects relative to one another or absolutely based on their Position property values. The **Position** property controls the position of components in the flow layout container. It does not affect components in other areas such as table cells.

You can set the Position property to one of these values:

* **Static**  
   Server positions the component at the location where you insert it. It disables the X and Y coordinate properties. You cannot move the component other than by moving its insertion point. This can happen when the text flow preceding the insertion point expands.
* **Relative**  
  Server positions the component at an offset to the position where you insert it. Server defines the offset by the X and Y coordinate property values. The Relative value is not available for some types of components.
* **Absolute**  
   Server locates the component at the position that you specify by dragging or by setting its X and Y coordinate property values. The component insertion point does not change, for instance by inserting text before it.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)The position of an object in a banded object can only be absolute.

To change the position property of a component, select the component, then:

* Right-click the component and on the shortcut menu, select an item from the **Position** submenu.
* In the Inspector panel, set its **Position** property value.

## Moving Objects by Dragging

You can move objects in the template edit area conveniently by dragging them to a new position. When a component has the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905933181335/btn_lrstd_slctcmpnt_13x13.gif) at the top left, you can drag ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905933181335/btn_lrstd_slctcmpnt_13x13.gif) to move the component.

## Resizing Objects

To resize an independent object, such as a table, a label, and a special field, select it, hover over the right/bottom border or the bottom right corner of the object until Server displays a double-headed arrow, drag the arrow, and then release the mouse.

## Removing Objects

You can remove objects using the Delete button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905880426903/btn_lrstd_delete.gif) on the toolbar. For a data component, you can also do this to remove it: select it, right-click the plus button ![select Component button](https://devnet.logianalytics.com/hc/article_attachments/9905904099095/btn_lrstd_slctcmpnt.gif) at the top left, and then select **Delete** from the shortcut menu.

## Returning to Page Report Studio

You can return to Page Report Studio with the updates you made to the report by selecting the **Return** button ![Return button](https://devnet.logianalytics.com/hc/article_attachments/9905902325911/btn_lrstd_return.gif). Server displays the [Back to Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/9905934866071-Back-to-Report-Dialog-Box-Properties). Specify whether you want to view full or partial data of the report. If you select **Partial Data**, you can then specify the number of records you want to display in the report. Then select **OK**. Server returns to Page Report Studio and displays the number of report data as you want.

![Back to Report dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905902351127/bck2rpt.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741463138711-Page-Report-Studio-Tag-Library)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741387513879-Introduction-to-the-Logi-Report-JDashboard-Logi-Report-Server-v19)
