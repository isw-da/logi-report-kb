---
title: "Inserting Tables in a Report"
id: 5735521199255
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735521199255-Inserting-Tables-in-a-Report
updated_at: 2022-11-02T04:13:21Z
---

# Inserting Tables in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735512509719-Working-with-Tables)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507432983-Modifying-Tables)

# Inserting Tables in a Report

You can create tables in a report easily using the table wizard. However, the procedure you use with the wizard varies with the data resource type: business view or query resource. This topic introduces how you can create a table using the table wizard when you have different data resources.

This topic contains the following sections:

* [Creating a Table Based on a Business View](#BV)
* [Creating a Table Based on a Query Resource](#Query)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) A page report can apply either query resources or business views, which is determined by the Create Using Business View option at the time when [you create the page report](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports#Page). Once defined, all data components in the page report can only use the specified data resource type.

## Creating a Table Based on a Business View

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the table.
2. Do either of the following:
   * From the **Components** panel, drag the required table type icon in the **Grid** category to the destination.
   * Navigate to **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the [Table Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735525106967-Table-Type-Dialog-Box) choose a type for the table and select **OK**.

     ![Table Type dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898518022679/tbltype.gif)

   Designer displays the [Create Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508437271-Create-Table-Dialog-Box#BV). You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens. When creating a table in a web report or library component, you get different screens according to the table type: group table or summary table.
3. In the **Data** screen, [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to use to create the
   table.

   ![Create Table wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/9898515688855/crttbl_dt_bv1.gif)
4. Specify the data to display in the table.

   **To define data for a group table in a web report/library component, or for a table in a page report**

   1. In the **Display** screen, add the detail fields you want to display in the table. You can specify a title for the table in the **Title** text box.

      ![Create Table wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/9898515699607/crttbl_dsply_bv.gif)

      The Resources box lists the data objects that you can use as detail fields in the table. These objects include: group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898534261399/bv_grp.gif) and detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/9898517937943/bv_detail.gif) in the business view from which the dataset the table applies is created, and [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898517940503/bv_dynfmla_grp.gif) and dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/9898517944087/bv_dynfmla_dtl.gif) that you have added for the business view in the current report.

      * To add a detail field, select an object in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the object from the Resources box to the right box.
      * In the **Display Name** column, select in the text box to edit the label for each detail column in the table. When you select the **Auto Map Field Name** checkbox in the text box, Designer applies the field's display name to label the detail column, and at runtime, Server maps the label to the dynamic display name of the field if the administrator defines it.
      * Select a field in the right box and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the detail fields in the table.
      * Select **Sort Fields By** to specify how to [sort the detail values](https://devnet.logianalytics.com/hc/en-us/articles/5735507432983-Modifying-Tables#Sort).
   2. In the **Group** screen, specify the criteria for [grouping data in the table](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables).

      ![Create Table wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/9898515705367/crttbl_grp_bv.gif)
   3. In the **Summary** screen, add summaries to calculate data in the table.

      ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898515717655/crttbl_sum_bv1.gif)

      The Resources box lists the aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/9898534371351/bv_agg.gif) in the business view from which the dataset the table applies is created, and the [dynamic formulas used as Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Formula)![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/9898518034071/bv_dynfmla_agg.gif) and [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Agg)![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/9898534371351/bv_agg.gif) that you have created for the business view in the current report. You can add them as summaries to calculate data in the table.

      * To add a summary in the table, in the right box, select the group to which to apply the summary (if you select **Table**, it is based on the whole business view), select an object in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the object from the Resources box to the right box. You can add several summaries for any group level.
      * Use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the summaries in a group or move a summary to another group.
      * The **Position** and **Column** options work together to determine the positions of the summaries in the table.
        + For a Group Above table, Designer places a summary added for the Table level in the intersection of the table footer panel and the first two detail columns with its name label which is the display name of the field used for the summary by default; Designer places a summary added for a specific group in the intersection of the group's footer panel and the first two detail columns with its name label.
        + For a table of any other type, you can customize the position of the summaries. When a summary is added for the Table level, you can place it and its name label in the intersection of the table footer panel (**Footer**)/table header panel (**Header**) and the first two detail columns (**Detail**)/a new summary column (**Summary**); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column.

   **To define data for a summary table in a web report/library component**

   1. In the **Columns** screen, specify the columns you want to display in the table.

      ![Create Table wizard - Columns](https://devnet.logianalytics.com/hc/article_attachments/9898465095831/crttbl_clmn.gif)

      The Resources box lists the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898534261399/bv_grp.gif) and aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/9898534371351/bv_agg.gif) in the business view from which the dataset the table applies is created, and the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Formula) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898517940503/bv_dynfmla_grp.gif), dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/9898518034071/bv_dynfmla_agg.gif), and [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Agg)![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/9898534371351/bv_agg.gif) that you have added for the business view in the current report. You can create columns in the table from these objects.

      * To add a column, select an object in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the object from the Resources box to the right box. Designer automatically groups the table by the added group objects and the position of the group objects in the right box determines the group level: the topmost group object the highest group level and the lowest group object the innermost group level. All the aggregation objects are parallel and calculate based on the innermost group.
      * Select an object in the right box and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif).to adjust the display order of the columns in the table.
      * For any group level, you can [customize its sort manner](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables#Sort) and [define Select N condition](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables#SelectN) to show data of certain range in its groups.
   2. In the **Summary** screen, insert the aggregation objects selected in the Columns screen to the table header/footer and to the group headers/footers of existing groups as summaries: first select an aggregation object in the **Resources** box, then select the checkboxes representing the required locations. Designer places the summary in the intersection of the corresponding summary column and the table/group header/footer panel.

      ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898465100695/crttbl_sum_bv2.gif)
5. In the **Dataset Filter** screen, ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")[filter the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report) the table applies. If you have added filter conditions to the dataset somewhere else, Designer displays the conditions in the screen. You can further edit the conditions. Be aware that a filter on a dataset applies to all data components in the same report that use this dataset.

   ![Create Table wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898465079191/crttbl_fltr_bv1.gif)
6. In the **Style** screen, specify the layout and style of the table.

   ![Create Table wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/9898515894423/crttbl_sty.gif)

   * By default, Designer places the table vertically. If you are creating the table in a page report, you can select **Horizontally** in the **Grow Report** box to create a horizontal table.
   * In the **Style** box, select the style of the table. If you have specified to insert the table into a banded object, the table [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports#Inherit) by default; to apply another style to the table, clear **Inherit Style** and select the required style from the Style box.
7. Select **Finish** to insert the table.
8. If you have selected a panel in a banded object as the destination and used the ribbon option to insert the table, after finishing the Create Table dialog box, you need to select in the destination once again to insert the table there.

## Creating a Table Based on a Query Resource

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the table.
2. Do either of the following:
   * From the **Components** panel, drag the icon representing the required table type in the **Grid** category to the destination.
   * Navigate to **Insert** > **Table** or **Home** > **Insert** > **Table**, then in the [Table Type dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735525106967-Table-Type-Dialog-Box) choose a type for the table.

   Designer displays the [Create Table dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508437271-Create-Table-Dialog-Box#Query). You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to use to create the
   table.

   ![Create Table wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/9898515843735/crttbl_dt.gif)
4. In the **Display** screen, add data fields to display as detail fields in the table.

   ![Create Table wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/9898515850647/crttbl_dsply.gif)

   The Resources box lists all DBFields in the query resource from which the dataset the table applies is created, and the formulas and parameters that are valid to these DBFields in the current catalog. You can use them as detail fields in the table.

   * To add a detail field, select a field in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the field from the Resources box to the right box.
   * By default, Designer applies the display names of the added fields to label the corresponding detail columns. To edit the label for a detail column, select in the **Display Name** text box and type a new name.
   * Select a detail field in the right box and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the detail fields in the table.
   * Select **Sort Fields By** to specify how to [sort the detail values](https://devnet.logianalytics.com/hc/en-us/articles/5735507432983-Modifying-Tables#Sort).

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When you are creating a summary table, by default, Designer does not show the detail columns for the added detail fields after the table is generated. If you want to show the detail columns in a summary table, take the following steps after the table is created：

   1. Select the table, right-click it and select **Show Column** on the shortcut menu.
   2. In the Show Column dialog box, select the column names for the detail columns you want to show and select **OK**.
   3. In the Report Inspector, select the **Table Detail** node of the table, set the **Invisible** property to **false**.
5. In the **Group** screen, specify the criteria for [grouping data in the table](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables).

   ![Create Table wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/9898515868823/crttbl_grp.gif)
6. In the **Summary** screen, add summaries to calculate data in the table.

   ![Create Table wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898532287255/crttbl_sum.gif)

   The Resources box lists all DBFields in the query resource from which the dataset the table applies is created, and the formulas that are valid to these DBFields in the current catalog. You can create summaries based on these fields in the table.

   * To add a summary, select the group in the right box to which to apply the summary (if you select **Table**, it is based on the whole dataset), select a field in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the field from the Resources box to the right box. You can add several summaries for any group level.
   * Specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) of each summary. If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box) dialog box. After the table is created, Designer automatically gives the summaries proper name labels to help you clarify the meaning of the numbers.
   * Use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the summaries in the current group or move a summary to another group.
   * The **Position** and **Column** options work together to determine the positions of the summaries in the table.
     + For a Group Above table, Designer places a summary added for the Table level in the intersection of the table footer panel and the first two detail columns with its name label which is the display name of the field used for the summary; Designer places a summary added for a specific group in the intersection of the group's footer panel and the first two detail columns with its name label.
     + For a table of any other type, you can customize the position of the summaries. For a summary added for the Table level, you can place it and its name label in the intersection of the table footer panel (**Footer**)/table header panel (**Header**) and the first two detail columns (**Detail**)/a new summary column (**Summary**); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column.

   Designer automatically adds the summaries created from the Summary screen to the current catalog as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Create) even when identical summaries already exist. Therefore, it is better not to create summaries here, instead, you can add dynamic summaries to the catalog and [drag and drop the dynamic summaries](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields) into the table after you finish creating it.
7. In the **Filter** screen, filter the table by adding conditions based on the fields it contains. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Table wizard - Fliter](https://devnet.logianalytics.com/hc/article_attachments/9898515890455/crttbl_fltr.gif)
8. In the **Style** screen, specify the layout and style of the table.

   ![Create Table wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/9898515894423/crttbl_sty.gif)

* In the **Grow Report** box, select whether to place the table vertically or horizontally.
* In the **Style** box, select the style of the table. If you have specified to insert the table into a banded object, the table [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports#Inherit) by default; to apply another style to the table, clear **Inherit Style** and select the required style from the Style box.

9. Select **Finish** to insert the table.
10. If you have selected a panel in a banded object as the destination and used the ribbon option to insert the table, after finishing the Create Table dialog box, you need to select in the destination once again to insert the table there.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Logi Report Engine cuts the table content in some pages that cannot display when the height of the table is higher than that of the page. However, when you export the table to Excel using Column Format or Data Format, or to Text with Delimited Format, or to XML, the table can display completely in the output.
* When you create a table of the Group Above or Group Left type, by default, Designer aligns all the summaries of the same functions horizontally in the table. If you want to align them vertically, select [Align summaries vertically](https://devnet.logianalytics.com/hc/en-us/articles/5735524192535-Options-Dialog-Box#Align) in the Component category of the Options dialog box in advance.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735512509719-Working-with-Tables)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507432983-Modifying-Tables)
