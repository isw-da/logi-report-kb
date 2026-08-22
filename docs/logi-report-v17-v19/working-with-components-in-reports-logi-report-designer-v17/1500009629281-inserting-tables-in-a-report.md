---
title: "Inserting Tables in a Report "
id: 1500009629281
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629281-Inserting-Tables-in-a-Report
updated_at: 2021-07-24T16:05:12Z
---

# Inserting Tables in a Report 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629261-Tables) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629301-Modifying-Tables)

# Inserting Tables in a Report

With the table wizard, it is easy to create tables in a report, however the wizard varies with the data resource type used for the table: business view or query resource. This topic introduces how to insert tables into different report types using different data sources.

A web report and library component can only use business views. For a page report it can be created either based on query resources or business views, which is determined at the time when  [the page report is created](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page)  by the Create Using Business View option. Once defined, all the data components in the page report can only be created on the specified data resource type.

A table can be inserted in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports#Relationship). When a table is inserted into a banded object in a page report, you can use a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500009628401-Setting-Up-Data-Container-Links-in-Banded-Objects) to define the relationship between the table and its parent.

This topic shows creating tables using different data resources in detail:

* [Creating a Table Based on a Business View](#BV)
* [Creating a Table Based on a Query Resource](#Query)

## Creating a Table Based on a Business View

1. Position the mouse pointer at the destination where you want to insert the table.
2. Do either of the following:
   * Drag the required table type button from the Grid category of the Components panel to the destination.
   * Select **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the [Table Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009610642-Table-Type-Dialog) dialog choose a type for the table.

     ![Table Type dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911679639/tbltype.gif)

     + **Table (Group Above)**  
        Creates a table with group information above the detail row.
     + **Table (Group Left)**  
        Creates a table with group information left to the detail row.
     + **Table (Group Left Above)**  
        Creates a table with group information left and above the detail row.
     + **Summary Table**  
        Creates a table with only group and summary information.

   The [Create Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009630281-Create-Table-Dialog#BV) wizard appears, which contains a set of screens for helping you define a table easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens. When creating a table in a web report or library component, you will get different screens according to the selected table type: group table or summary table.
3. In the Data screen, select the business view in the current catalog using which to create the table. When the table is to be inserted into the banded header, banded footer, group header, group footer panel of a banded object in a web report, you can also select **Inherit from the Parent** to inherit data from the business view used by the parent banded object.

   ![Create Table wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904363031/crttbl_dt_bv1.gif)
4. Specify the data to display in the table.

   **To define the data for a group table in a web report/library component, or for a table in a page report:**

   1. In the Display screen, add the detail fields you want to display in the table. You can specify a title for the table in the Title text box.

      ![Create Table wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904363415/crttbl_dsply_bv.gif)

      The Resources box lists the data objects that can be used as detail fields in a table. These objects include: group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif) and detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425495/bv_detail.gif) in the specified business view, [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif) and dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828823/bv_dynfmla_dtl.gif) created for the business view in the current report.

      To add a detail field, select an object in the Resources box, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it to the right box; to remove an unwanted detail field, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. To adjust the display order of the detail fields in the table, make use of ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) and ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif). By default the display names of the added objects will be used to label the corresponding detail columns; to edit the label text for a detail column, select in the Display Name text box and type a new one; if you want to automatically map the label text to the dynamic display name of the field at runtime, select the **Auto Map Field Name** checkbox in the text box. You can select the **Sort Fields By** button to specify in which manner to [sort the detail values](https://devnet.logianalytics.com/hc/en-us/articles/1500009629301-Modifying-Tables#Sort).
   2. In the Group screen, specify the criteria for [grouping data in the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables).

      ![Create Table wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404916808215/crttbl_grp_bv.gif)
   3. In the Summary screen, add summaries to calculate data in the table.

      ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404916808471/crttbl_sum_bv1.gif)

      The Resources box lists the aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) in the specified business view, as well as the [dynamic formulas used as Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula)![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427799/bv_dynfmla_agg.gif) and [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg)![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) created for the business view in the current report. You can add them as summaries to calculate data in the table.

      To add a summary in the table, in the right box select the group to which the summary will be applied (if you select Table, it will be based on the whole business view), select an object in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it to the right box. You can add several summaries for any group level; to adjust the display order of the summaries in a group or move a summary to another group, make use of ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif). The Position and Column options work together to determine the positions of the summaries in the table.

      * If the table is of the Group Above type, a summary added for the Table level is placed in the intersection of the table footer panel and the first two detail columns with its name label which is the display name of the field used for the summary by default; a summary added for a specific group is placed in the intersection of the group's footer panel and the first two detail columns with its name label.
      * If the table is of the other types, you can customize the position of the summaries. When a summary is added for the Table level, you can place it and its name label in the intersection of the table footer panel (Footer)/table header panel (Header) and the first two detail columns (Detail)/a new summary column (Summary); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column.

   **To define the data for a summary table in a web report/library component:**

   1. In the Columns screen, specify the columns you want to display in the table.

      ![Create Table wizard - Columns](https://devnet.logianalytics.com/hc/article_attachments/4404904364823/crttbl_clmn.gif)

      The Resources box lists the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif) and aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) in the specified business view, as well as the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif), dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427799/bv_dynfmla_agg.gif) and [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg)![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) created for the business view in the current report. You can create columns in the table from these objects.

      To add a column, select an object in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it to the right box; to remove an unwanted column, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the display order of the columns. The table will be automatically grouped by the added group objects and the position of the group objects in the right box determines the group level: the topmost group object the highest group level and the lowest group object the innermost group level. All the aggregation objects are parallel and calculate based on the innermost group. For any group level, you can [customize its sort manner](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables#Sort) and [define Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables#SelectN) to show data of certain range in its groups.
   2. In the Summary screen, insert the aggregation objects selected in the Columns screen to the table header/footer and to the group headers/footers of existing groups as summaries. First select an aggregation object in the Resources box, then select the checkboxes representing the required locations. The summary will be placed in the intersection of the corresponding summary column and the table/group header/footer panel.

      ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904365079/crttbl_sum_bv2.gif)
5. In the Filter screen, apply a filter to reduce the data displayed in the table. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the Filter drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   ![Create Table wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404916808727/crttbl_fltr_bv1.gif)
6. In the Style screen, specify the style of the table.

   ![Create Table wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904364311/crttbl_sty_bv1.gif)

   When you have specified to insert the table into a banded object, by default the table will [inherit its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613462-Applying-Styles#Inherit). If you want to apply another style to the table, clear the **Inherit Style** option and then select the required style from the Style box.
7. Select **Finish** to insert the table.

   If you have used the menu tab command to insert the table and selected a panel in a banded object as the table destination, after selecting Finish in the wizard, you need to select the mouse button in the destination once again in order to insert the table there.

## Creating a Table Based on a Query Resource

1. Position the mouse pointer at the destination where you want to insert the table.
2. Do either of the following:
   * Drag the button representing the required table type from the Grid category of the Components panel to the destination.
   * Select **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the Table Type dialog choose a [type](#Type) for the table.

   The [Create Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009630281-Create-Table-Dialog#Query) wizard appears, which contains a set of screens for helping you define a table easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select the data resource using which to create the table.

   ![Create Table wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904366359/crttbl_dt.gif)

   If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one. When a query is selected, you can select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog). Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current page report to create the table, select the **More Options** button and then:

   * Select the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog), or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report will still run the query separately for each dataset.
   * Select the **Current Dataset** radio button to make the table inherit the dataset from its parent.
4. In the Display screen, add the data fields you want to display as detail fields in the table.

   ![Create Table wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404916809367/crttbl_dsply.gif)

   The Resources box lists all the DBFields in the specified data resource, as well as the formulas and parameters that are valid to these DBFields in the current catalog. You can use them as detail fields in the table.

   To add a detail field, select an object in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it from the Resources box to the right box; to remove an unwanted detail field, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. You can make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the display order of the detail fields in the table. By default the display names of the added objects will be used to label the corresponding detail columns; to edit the label for a detail column, select in the Display Name text box and type a new name. You can select the **Sort Fields By** button to specify in which manner to [sort the detail values](https://devnet.logianalytics.com/hc/en-us/articles/1500009629301-Modifying-Tables#Sort).

   **Tip:** If you are creating a summary table, the detail columns for the added detail fields will not be shown after the table is generated by default. If you want to show the detail columns in a summary table, when the table is created：

   1. Select the table, right-click it and select **Show Column** on the shortcut menu.
   2. In the Show Column dialog, select the column names for the detail columns you want to show and select **OK**.
   3. Go to the Report Inspector, select the **Table Detail** node of the table, set the Invisible property to **false**.
5. In the Group screen, specify the criteria for [grouping data in the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables).

   ![Create Table wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404904367127/crttbl_grp.gif)
6. In the Summary screen, add summaries to calculate data in the table.

   ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904367383/crttbl_sum.gif)

   The Resources box lists all the DBFields in the specified data resource, as well as the formulas that are valid to these DBFields in the current catalog. You can create summaries based on these objects in the table.

   To add a summary, in the right box, select the group to which the summary will be applied (if you select Table, it will be based on the whole dataset), select an object in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it to the right box, then specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) as required. When DistinctSum is selected as the function, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog. You can add several summaries for any group level. When the table is created, Logi Report will automatically give the summaries proper name labels to help you clarify the meaning of the numbers. If a summary is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. You can make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the display order of the summaries in the current group or move a summary to another group. The Position and Column options work together to determine the positions of the summaries in the table.

   * If the table is of the Group Above type, a summary added for the Table level is placed in the intersection of the table footer panel and the first two detail columns with its name label which is the display name of the field used for the summary; a summary added for a specific group is placed in the intersection of the group's footer panel and the first two detail columns with its name label.
   * If the table is of the other types, you can customize the position of the summaries. When a summary is added for the Table level, you can place it and its name label in the intersection of the table footer panel (Footer)/table header panel (Header) and the first two detail columns (Detail)/a new summary column (Summary); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column.

   The summaries created from the Summary screen will be added to the current catalog as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Create) even when identical summaries already exist. Therefore, it is better not to create summaries here, instead you can add dynamic summaries to the catalog and [drag and drop the dynamic summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009629241-Summary-Fields-) into the table after it is created.
7. In the Filter screen, add filter conditions on the fields that have been added to the table to reduce the data. [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009636161-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Table wizard - Fliter](https://devnet.logianalytics.com/hc/article_attachments/4404904367639/crttbl_fltr.gif)
8. In the Style screen, specify the layout and style of the table.

   ![Create Table wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904367895/crttbl_sty.gif)

   In the Grow Report box, select whether to place the table vertically or horizontally. In the Style box select the style of the table. When you have specified to insert the table into a banded object, by default the table will [inherit its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613462-Applying-Styles#Inherit). If you want to apply another style to the table, clear the **Inherit Style** option and then select the required style from the Style box.
9. Select **Finish** to insert the table.

   If you have used the menu tab command to insert the table and selected a panel in a banded object as the table destination, after finishing the wizard, you need to select the mouse button in the destination once again in order to insert the table there.

**Notes:**

* The content of the table in some pages that cannot be displayed will be cut off if the height of the table is higher than that of the page, however when exporting the table to an Excel file with column format or data format, or to text with delimited format, or to XML, no content will be cut off.
* When creating a table of the Group Above or Group Left type, by default all the summaries of the same functions will be aligned horizontally in the table. If you want to align them vertically, select the option [Align summaries vertically](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Align) in the Options dialog in advance.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629261-Tables) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629301-Modifying-Tables)
