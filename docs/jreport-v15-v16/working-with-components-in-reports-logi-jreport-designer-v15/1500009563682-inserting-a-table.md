---
title: "Inserting a Table"
id: 1500009563682
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table
updated_at: 2021-07-24T05:55:55Z
---

# Inserting a Table

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584261-Tables)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584421-Modifying-a-Table)

# Inserting a Table

With the table wizard, it is easy to create tables in a report, however, the wizard varies slightly with different report types: web report/library component, and page report.

A table can be inserted in the report areas listed in [Component placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports#Relationship).

Below is a list of the sections covered in this topic:

> * [Inserting a Table into a Web Report or Library Component](#Web)
> * [Inserting a Table into a Page Report](#Page)

## Inserting a Table into a Web Report or Library Component

1. Position the mouse pointer at the destination where you want to insert the table.
2. Do either of the following:
   * Drag the required table type button from the Grid category of the Components panel to the destination.
   * Select **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the [Table Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009567762-Table-Type-Dialog) dialog choose a [type](#Type) for the table.The [Create Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009586101-Create-Table-Dialog-for-Web-Report-and-Library-Component-) wizard appears.
3. In the Data screen, select a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) in the current catalog on which to create the table.
4. Specify the data displayed in the table. Depending on the table type selected in step 2, the screens for defining the data vary:
   * [Group Left, Group Above, or Group Left Above](#Group)
   * [Summary Table](#Summary)

   **To define the data for a group left, group above, or group left above table:**

   1. In the Display screen, specify a title for the table in the Title text field, then add the business view elements or [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) to be displayed in the table. To add a field, select it in the Resources box, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the display field box on the right. You can add only one field at a time. If a field is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. You can add or remove only one field at a time. Select ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the fields. If required, modify the display name of any added field by selecting its Display Name text box. You can also select the **Sort Fields By** button to specify how to [sort data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data) in the table.

      ![Create Table wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404893936023/crttbl_dsply_wb.gif)
   2. In the Group screen, add the group objects or dynamic formulas as the [grouping criteria](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data).
   3. To add summaries, go to the Summary screen. In the sum on box on the right, specify the group to which the summary will be applied (if you select Table, it will be based on the whole dataset), select an aggregation object or [dynamic resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) in the Resources box as the summary field and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the right box, then specify where to place the summary in the table from the Position and Column columns. You can add several summaries for any group level. If a summary is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the summaries in the current group or move a summary to another group if needed.

      ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404893936407/crttbl_sum_wb.gif)

   **To define the data for a summary table:**

   1. In the Columns screen, specify the columns you want to display in the table. Only aggregation and group objects in the specified business view and [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) can be added to the table. To add a column, select a field in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the column box on the right. You can add only one field at a time. If a field is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the fields. The table will then be automatically grouped by the added group objects and the position of the group objects in the right box determines the group level: the topmost group object the highest group level and the lowest group object the innermost group level. All the aggregation objects are parallel and calculate based on the lowest group. For a group, you can specify the [sorting manner](https://devnet.logianalytics.com/hc/en-us/articles/1500009584401-Setting-the-Sort-Manner) of the group and [define the Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009584381-Specifying-the-Select-N-Condition) to show data of certain range in the group.

      ![Create Table wizard for Summary table in Web Report - Columns](https://devnet.logianalytics.com/hc/article_attachments/4404893936919/crttbl_clmn_wb.gif)
   2. In the Summary screen, you can insert the aggregation objects selected in the Columns screen to the table header/footer and to the group headers/footers of existing groups as summaries. First select an aggregation object in the Resources box, then select the checkboxes representing the required locations. The summary will be placed in the intersection of its summary column and the table/group header/footer row.

      ![Create Table wizard for Summary Table in Web Report - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404889375639/crttbl_sum_wb1.gif)
5. In the Filter screen, define filter conditions to [filter the data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data) displayed in the table.
6. In the Style screen, specify the style of the table.
7. Select **Finish** to insert the table.

   If you have used the menu tab command to insert the table and specified to insert it to position other than the report body or tabular cell, after selecting Finish in the wizard, you need to select the mouse button in the destination once again in order to insert the table there.

## Inserting a Table into a Page Report

A page report can be created either based on query resources or business views, which is determined at the time when  [the page report is created](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component)  by the Create Using Business View option[.](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component) Once defined, all the data components in the page report can only be created on the specified data resource type. The procedure for creating a table in a page report varies with the data resource type specified for the page report: [query resource](#Query) or [business view](#BV).

**To insert a table in a page report that is based on query resources:**

1. Position the mouse pointer at the destination where you want to insert the table. It can be in an empty area of the page report or inside a [banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009562842-Banded-Objects).
2. Do either of the following:
   * Drag the required table type button from the Grid category of the Components panel to the destination.
   * Select **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the [Table Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009567762-Table-Type-Dialog) dialog choose a type for the table.

     ![Table Type dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889318935/tbltype.gif)

     + **Table (Group Above)**  
        Creates a table with group information above the detail row.
     + **Table (Group Left)**  
        Creates a table with group information left to the detail row.
     + **Table (Group Left Above)**  
        Creates a table with group information left and above the detail row.
     + **Summary Table**  
        Creates a table with only group and summary information.

   The [Create Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009564962-Create-Table-Dialog-for-Page-Report-) wizard appears.
3. In the Data screen, select the data resource on which to create the table. If the given data resources are not what you want, select the first item  in the corresponding resource node to create one. When a query is selected, select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009570662-Editing-a-Query) if required. Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current page report to create the table, select the **More Options** button and then:

   * Check the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if necessary, or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi JReport will still run the query separately for each dataset.
   * Check the **Current Dataset** radio button to make the table inherit the dataset from its parent.

   ![Create Table wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404893934231/crttbl_dt.gif)
4. In the Display screen, add the fields to be displayed in the table. To add a field, select it in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it from the Resources box to the display field box on the right. You can add only one field at a time. If a field is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the fields. If required, modify the display name of any added field by selecting its Display Name text box. You can also select the **Sort Fields By** button to specify how to [sort data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data) in the table.

   ![Create table wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404893934487/crttbl_dsply.gif)
5. In the Group screen, add the fields as the [grouping criteria](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data).

   ![Create table wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893934743/crttbl_grp.gif)
6. To add summaries, go to the Summary screen. In the sum on box on the right, specify the group to which the summary will be applied (if you select Table, it will be based on the whole dataset), select a field in the Resources box as the summary field and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the right box, then select the function for the summary from the Aggregate Function column. You can add several summaries for any group level. Logi JReport will automatically give the summaries proper name labels to help you clarify the meaning of the numbers. If a summary is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the summary fields in the current group or move a summary field to another group if needed.

   The summaries created from the Summary screen will be added to the current catalog data source as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009589741-Creating-a-Summary) even when identical summaries already exist. Therefore, it is better not to create summaries here, instead you can add dynamic summaries to the catalog and [drag and drop the dynamic summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009563602-Summary-Fields) into the table after it is created.

   ![Create table wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404889372951/crttbl_sum.gif)
7. To apply filters to the table so as to reduce the data displayed in the table, go to the Filter screen and [define the filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).

   ![Create table wizard - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893934999/crttbl_fltr.gif)
8. In the Style screen, specify the layout and style of the table.

   ![Create table wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404889373207/crttbl_sty.gif)

   When you have specified to insert the table into a banded object, by default the table will inherit its parent's style. If you want to apply another style to the table, uncheck the **Inherit Style** option and then select the required style from the Style box. For more information, see [Inheriting Styles](https://devnet.logianalytics.com/hc/en-us/articles/1500009593241-Inheriting-Styles).
9. Select **Finish** to insert the table.

   If you have used the menu tab command to insert the table and specified to insert it to position other than the report body or tabular cell, after selecting Finish in the wizard, you need to select the mouse button in the destination once again in order to insert the table there.

When the table is inserted into a banded object, you can set up [data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500009583301-Setting-Up-a-Data-Container-Link) between the table and its parent.

**To insert a table in a page report that is based on business views:**

1. Position the mouse pointer at the destination where you want to insert the table. It can be in an empty area of the page report or inside a [banded object](https://devnet.logianalytics.com/hc/en-us/articles/1500009562842-Banded-Objects).
2. Do either of the following:
   * Drag the required table type button from the Grid category of the Components panel to the destination.
   * Select **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the [Table Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009567762-Table-Type-Dialog) dialog choose a type for the table.

   The [Create Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009564962-Create-Table-Dialog-for-Page-Report-#BV) wizard appears.
3. In the Data screen, select a business view on which to create the table.

   ![Create Table wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404889373463/crttbl_dt-bv.gif)
4. In the Display screen, provide the title of the table if needed and add the fields to be displayed in the table. To add a field, select it in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it from the Resources box to the display field box on the right. You can add only one field at a time. If a field is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the fields. If required, modify the display name of any added field by selecting its Display Name text box. You can also select the **Sort Fields By** button to specify how to [sort data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data) in the table.

   ![Create table wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404889373719/crttbl_dsply-bv.gif)
5. In the Group screen, add the fields as the [grouping criteria](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data).

   ![Create table wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893935255/crttbl_grp-bv.gif)
6. In the Summary screen, add aggregations to summarize data in the table. In the right box, specify the group to which the aggregation will be applied (if you select Table, the aggregation will be based on the whole dataset), select an aggregation in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the right box. You can add several aggregations for any level. Logi JReport will automatically give the aggregations proper name labels to help you clarify the meaning of the numbers. If an aggregation is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the aggregations in the current group or move an aggregation to another level if needed.

   ![Create table wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404893935511/crttbl_sum-bv.gif)
7. To apply filters to the table so as to reduce the data displayed in the table, go to the Filter screen and [define the filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).

   ![Create table wizard - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404893935767/crttbl_fltr-bv.gif)
8. In the Style screen, specify the layout and style of the table.

   ![Create table wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404889374231/crttbl_sty-bv.gif)

   When you have specified to insert the table into a banded object, by default the table will inherit its parent's style. If you want to apply another style to the table, uncheck the **Inherit Style** option and then select the required style from the Style box. For more information, see [Inheriting Styles](https://devnet.logianalytics.com/hc/en-us/articles/1500009593241-Inheriting-Styles).
9. Select **Finish** to insert the table.

   If you have used the menu tab command to insert the table and specified to insert it to position other than the report body or tabular cell, after selecting Finish in the wizard, you need to select the mouse button in the destination once again in order to insert the table there.

**Notes:**

* The content of the table in some pages that cannot be displayed will be cut off if the height of the table is higher than that of the page, however, when exporting the table to an Excel file with column format or data format, or to text with delimited format, or to XML, no content will be cut off.
* When creating a table of the Group Above or Group Left type, by default all the summaries of the same functions will be aligned horizontally in the table. If you want to align them vertically, check the option [Align summaries vertically](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog#Align) in the Options dialog in advance.

**See also:**

* **An example:** The SampleComponents catalog, included with Logi JReport Designer, contains reports that have examples of report component types. For the table component example, open `<install_root>\Demo\Reports\SampleComponents\TableReport.cls`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584261-Tables)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584421-Modifying-a-Table)
