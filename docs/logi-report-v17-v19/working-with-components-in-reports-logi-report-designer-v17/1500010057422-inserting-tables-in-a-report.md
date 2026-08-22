---
title: "Inserting Tables in a Report"
id: 1500010057422
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057422-Inserting-Tables-in-a-Report
updated_at: 2022-03-28T07:16:42Z
---

# Inserting Tables in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094921-Working-with-Tables)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables)

# Inserting Tables in a Report

You can create tables in a report easily using the table wizard, however, the wizard varies with the data resource type used for the table: business view or query resource. This topic introduces how you can create a table with the table wizard using different data resource.

You can insert tables in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship). When you insert a table into a banded object in a page report, you can use a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500010056782-Setting-Up-Data-Container-Links-in-Banded-Objects) to define the relationship between the table and its parent.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) A page report can use either query resources or business views, which is determined at the time when [you create the page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) by the **Create Using Business View** option. Once defined, all the data components in the page report can only use the specified data resource type.

This topic contains the following sections:

* [Creating a Table Based on a Business View](#BV)
* [Creating a Table Based on a Query Resource](#Query)

## Creating a Table Based on a Business View

1. Position the mouse pointer at the destination where you want to insert the table.
2. Do either of the following:
   * From the **Components** panel, drag the required table type icon in the Grid category to the destination.
   * Select **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the [Table Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099021-Table-Type-Dialog-Box) choose a type for the table.

     ![Table Type dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856891287/tbltype.gif)

     + **Table (Group Above)**  
       Select to create a table which displays the group information above the detail row.
     + **Table (Group Left)**  
       Select to create a table which displays the group information left to the detail row.
     + **Table (Group Left Above)**  
       Select to create a table which displays the group information left and above the detail row.
     + **Summary Table**  
       Select to create a table which displays only the group and summary information.

   Designer displays the [Create Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095941-Create-Table-Dialog-Box#BV), which contains a set of screens for helping you define a table easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens. When creating a table in a web report or library component, you get different screens according to the selected table type: group table or summary table.
3. In the **Data** screen, select the business view in the current catalog using which to create the table.

   If you have specified to insert the table into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel, Designer displays the **Inherit from the Parent** option. Select it if you want the table to inherit the business view that its parent banded object uses.

   ![Create Table wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856986775/crttbl_dt_bv1.gif)
4. Specify the data to display in the table.

   **To define the data for a group table in a web report/library component, or for a table in a page report:**

   1. In the **Display** screen, add the detail fields you want to display in the table. You can specify a title for the table in the **Title** text box.

      ![Create Table wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404856987031/crttbl_dsply_bv.gif)

      The Resources box lists the data objects that you can use as detail fields in the table. These objects include: group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404848663831/bv_grp.gif) and detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664087/bv_detail.gif) in the specified business view, and [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404857035543/bv_dynfmla_grp.gif) and dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664343/bv_dynfmla_dtl.gif) that you have created for the business view in the current report.

      To add a detail field, select an object in the Resources box, then select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box; to remove an unwanted detail field, select it and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. To adjust the display order of the detail fields in the table, select a field and select the **Move Up**![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button. By default, Designer applies the display names of the added objects to label the corresponding detail columns; to edit the label text for a detail column, select in the **Display Name** text box and type a new one; if you want to automatically map the label text to the dynamic display name of the field at runtime, select the **Auto Map Field Name** checkbox in the text box. You can select the **Sort Fields By** button to specify in which manner to [sort the detail values](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables#Sort).
   2. In the **Group** screen, specify the criteria for [grouping data in the table](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables).

      ![Create Table wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848594327/crttbl_grp_bv.gif)
   3. In the **Summary** screen, add summaries to calculate data in the table.

      ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404856987415/crttbl_sum_bv1.gif)

      The Resources box lists the aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404857037591/bv_agg.gif) in the specified business view, as well as the [dynamic formulas used as Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula)![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664855/bv_dynfmla_agg.gif) and [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg)![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404857037591/bv_agg.gif) that you have created for the business view in the current report. You can add them as summaries to calculate data in the table.

      To add a summary in the table, in the right box, select the group to which to apply the summary (if you select **Table**, it is based on the whole business view), select an object in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box. You can add several summaries for any group level; to remove an unwanted summary, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. Make use of ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) to adjust the display order of the summaries in a group or move a summary to another group. The **Position** and **Column** options work together to determine the positions of the summaries in the table.

      * If the table is of the Group Above type, Designer places a summary added for the Table level in the intersection of the table footer panel and the first two detail columns with its name label which is the display name of the field used for the summary by default; Designer places a summary added for a specific group in the intersection of the group's footer panel and the first two detail columns with its name label.
      * If the table is of the other types, you can customize the position of the summaries. When a summary is added for the Table level, you can place it and its name label in the intersection of the table footer panel (**Footer**)/table header panel (**Header**) and the first two detail columns (**Detail**)/a new summary column (**Summary**); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column.

   **To define the data for a summary table in a web report/library component:**

   1. In the **Columns** screen, specify the columns you want to display in the table.

      ![Create Table wizard - Columns](https://devnet.logianalytics.com/hc/article_attachments/4404856988183/crttbl_clmn.gif)

      The Resources box lists the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404848663831/bv_grp.gif) and aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404857037591/bv_agg.gif) in the specified business view, as well as the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404857035543/bv_dynfmla_grp.gif), dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664855/bv_dynfmla_agg.gif) and [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg)![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404857037591/bv_agg.gif) that you have created for the business view in the current report. You can create columns in the table from these objects.

      To add a column, select an object in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box; to remove an unwanted column, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. You can make use of ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) to adjust the display order of the columns. Designer automatically groups the table by the added group objects and the position of the group objects in the right box determines the group level: the topmost group object the highest group level and the lowest group object the innermost group level. All the aggregation objects are parallel and calculate based on the innermost group. For any group level, you can [customize its sort manner](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Sort) and [define Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#SelectN) to show data of certain range in its groups.
   2. In the **Summary** screen, insert the aggregation objects selected in the Columns screen to the table header/footer and to the group headers/footers of existing groups as summaries: first select an aggregation object in the Resources box, then select the checkboxes representing the required locations. Designer places the summary in the intersection of the corresponding summary column and the table/group header/footer panel.

      ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404856988439/crttbl_sum_bv2.gif)
5. In the **Filter** screen, apply a filter to reduce the data to display in the table. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the **Filter** drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   ![Create Table wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856987671/crttbl_fltr_bv1.gif)
6. In the **Style** screen, specify the style of the table.

   If you have specified to insert the table into a banded object, by default, the table [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062802-Applying-Styles-to-Reports#Inherit); to apply another style to the table, clear the **Inherit Style** option and then select the required style from the **Style** box.

   ![Create Table wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848594839/crttbl_sty_bv1.gif)
7. Select **Finish** to insert the table.

   If you have used the menu tab command to insert the table and selected a panel in a banded object as the table destination, after finishing in the dialog box, you need to select the mouse button in the destination once again in order to insert the table there.

## Creating a Table Based on a Query Resource

1. Position the mouse pointer at the destination where you want to insert the table.
2. Do either of the following:
   * From the **Components** panel, drag the icon representing the required table type in the Grid category to the destination.
   * Select **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the Table Type dialog box choose a [type](#Type) for the table.

   Designer displays the [Create Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095941-Create-Table-Dialog-Box#Query), which contains a set of screens for helping you define a table easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the data resource in the current catalog using which to create the table.

   ![Create Table wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848595351/crttbl_dt.gif)

   If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one in the current catalog to use. When you select a query, you can select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog). Designer then automatically creates a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets) based on the selected data resource in the page report.

   If you want to use an existing dataset in the current page report to create the table, select the **More Options** button and then:

   * Select the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select the **<New Dataset...>** item to create a dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.
   * If you have specified to insert the table into an object that already applies a dataset, such as a banded panel, Designer enables the **Current Dataset** radio button. Select it if you want the table to inherit the dataset from the parent object.
4. In the **Display** screen, add the data fields you want to display as detail fields in the table.

   ![Create Table wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848595607/crttbl_dsply.gif)

   The Resources box lists all the DBFields in the specified data resource, as well as the formulas and parameters that are valid to these DBFields in the current catalog. You can use them as detail fields in the table.

   To add a detail field, select an object in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it from the Resources box to the right box; to remove an unwanted detail field, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. You can make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) to adjust the display order of the detail fields in the table. By default, Designer applies the display names of the added objects to label the corresponding detail columns; to edit the label for a detail column, select in the **Display Name** text box and type a new name. You can select the **Sort Fields By** button to specify in which manner to [sort the detail values](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables#Sort).

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you are creating a summary table, by default, Designer does not show the detail columns for the added detail fields after the table is generated. If you want to show the detail columns in a summary table, when the table is created：

   1. Select the table, right-click it and select **Show Column** on the shortcut menu.
   2. In the Show Column dialog box, select the column names for the detail columns you want to show and select **OK**.
   3. Go to the Report Inspector, select the **Table Detail** node of the table, set the **Invisible** property to **false**.
5. In the **Group** screen, specify the criteria for [grouping data in the table](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables).

   ![Create Table wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848595863/crttbl_grp.gif)
6. In the **Summary** screen, add summaries to calculate data in the table.

   ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404856989719/crttbl_sum.gif)

   The Resources box lists all the DBFields in the specified data resource, as well as the formulas that are valid to these DBFields in the current catalog. You can create summaries based on these objects in the table.

   To add a summary, in the right box, select the group to which to apply the summary (if you select **Table**, it is based on the whole dataset), select an object in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box, then specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) as required. If you select **DistinctSum**, you should select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box) dialog box. You can add several summaries for any group level. When the table is created, Designer automatically gives the summaries proper name labels to help you clarify the meaning of the numbers. If a summary is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. You can make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) to adjust the display order of the summaries in the current group or move a summary to another group. The **Position** and **Column** options work together to determine the positions of the summaries in the table.

   * If the table is of the Group Above type, Designer places a summary added for the Table level in the intersection of the table footer panel and the first two detail columns with its name label which is the display name of the field used for the summary; Designer places a summary added for a specific group in the intersection of the group's footer panel and the first two detail columns with its name label.
   * If the table is of the other types, you can customize the position of the summaries. When a summary is added for the Table level, you can place it and its name label in the intersection of the table footer panel (**Footer**)/table header panel (**Header**) and the first two detail columns (**Detail**)/a new summary column (**Summary**); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column.

   Designer automatically adds the summaries created from the Summary screen to the current catalog as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Create) even when identical summaries already exist. Therefore, it is better not to create summaries here, instead, you can add dynamic summaries to the catalog and [drag and drop the dynamic summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields) into the table after you finish creating it.
7. In the **Filter** screen, add filter conditions based on the fields that you have added to the table to reduce the data. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010101241-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Table wizard - Fliter](https://devnet.logianalytics.com/hc/article_attachments/4404848596119/crttbl_fltr.gif)
8. In the **Style** screen, specify the layout and style of the table.

   In the **Grow Report** box, select whether to place the table vertically or horizontally. In the **Style** box, select the style of the table. If you have specified to insert the table into a banded object, by default, the table [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062802-Applying-Styles-to-Reports#Inherit); to apply another style to the table, clear the **Inherit Style** option and then select the required style from the Style box.

   ![Create Table wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404856989975/crttbl_sty.gif)
9. Select **Finish** to insert the table.

   If you have used the menu tab command to insert the table and selected a panel in a banded object as the table destination, after finishing the dialog box, you need to select the mouse button in the destination once again in order to insert the table there.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* Designer cuts the content of the table in some pages that cannot display if the height of the table is higher than that of the page; however, when you export the table to Excel with column format or data format, or to Text with delimited format, or to XML, Designer does not cut off any no content.
* When you create a table of the Group Above or Group Left type, by default, Designer aligns all the summaries of the same functions horizontally in the table. If you want to align them vertically, select the option [Align summaries vertically](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Align) in the Options dialog box in advance.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094921-Working-with-Tables)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables)
