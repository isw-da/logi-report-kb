---
title: "Creating Page Reports"
id: 1500009673901
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673901-Creating-Page-Reports
updated_at: 2021-07-24T20:53:57Z
---

# Creating Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674061-Page-Report-Studio-Window-Elements)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673921-Editing-Page-Reports-in-Page-Report-Studio)

# Creating Page Reports

In Page Report Studio, you can create page reports or add new report tabs to the current page report if the corresponding catalog contains predefined [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009675121-An-Introduction-to-Business-Views). Before you can create page reports, you should make sure that the Pop-up Blocker is not enabled on your web browser.

A [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648262-Logi-JReport-Licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Jinfonet Software account manager to obtain it.

**To create a page report:**

1. Do any of the following:
   * On the [Logi JReport Server Start page](https://devnet.logianalytics.com/hc/en-us/articles/1500009648602-Accessing-Logi-JReport-Server-Guide-v15-Server-via-a-Web-Browser#Local), select **Page Reports** in the Create category. In the displayed page, specify the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
   * On the Logi JReport Console > Resources page**,** open the folder and select the catalog for the new page report from the Catalog drop-down list, then select **New** > **Page Report** on the task bar.
   * In Page Report Studio, select **Menu** > **File** > **New Page Report**.

   The [New Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009645422-New-Page-Report) dialog appears for you to create a page report with the first report tab in it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926689559/newrpt.gif)
2. Specify the title of the report tab as required in the Report Title text box.
3. In the Choose Report Layout box, select the required layout with which you want to create the report tab.
4. Select **OK** to create the report tab.
   * If Blank is selected as the layout, a report tab which is blank will be created. You can then use the Toolbox and the Resource View panels to [add objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009649262-Adding-Report-Objects) and [view elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009649282-Using-View-Elements) to the report tab.
   * If you select the layout as Banded, Table, Chart, or Crosstab, the corresponding report wizard will then be displayed. Specify the settings according to your requirements.

     **Tip:** In the report wizard, if there is only one business view in the current catalog, this business view will be used to create the report tab by default, and the Data screen will be hidden from the wizard. This is the same case when there is only one style available to be applied to the report tab.

You can also use [URL command](https://devnet.logianalytics.com/hc/en-us/articles/1500009650402-Creating-Reports#Page) to directly open the New Page Report dialog to create a page report.

To create a report tab in an existing page report, in Page Report Studio, select **Menu** > **File** > **New Page Report Tab** or the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920357527/btn_newobj.gif) on the toolbar. In the [New Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009645442-New-Report-Tab) dialog, specify the title and layout of the report tab, then select **OK**.

The following shows in detail how to create a report tab from a particular layout:

* [Creating a Banded Report](#Banded)
* [Creating a Table Report](#Table)
* [Creating a Crosstab Report](#Crosstab)
* [Creating a Chart Report](#Chart)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating a Banded Report

A banded object is a kind of component that can present grouped data and detailed data, and is composed of several banded panels with which you can easily organize data fields and other elements.

**To create a banded report:**

1. In the New Page Report dialog, select  **Banded**  as the layout and select **OK** to display the [Banded Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009669421-Banded-Wizard).
2. In the Data screen, select the business view in the current catalog, on which the banded object will be built.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926689815/bdwzd_data.gif)
3. In the Display screen, add the required fields from the Resources box to be displayed in the banded object. Modify the display name of any added field if necessary.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920480663/bdwzd_dsply.gif)
4. In the Group screen, add the group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) as the grouping criteria, then specify the sorting direction of each group in the Sort column.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926690071/bdwzd_grp.gif)
5. To add summaries, go to the Summary screen. Select the group to which the summary will be applied, then add an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) as the summary field.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926690327/bdwzd_sum.gif)
6. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009673941-Applying-Filters#QueryFilter). If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009669621-Enter-Parameter-Values) dialog to specify values to the parameters before the Query Filter screen is displayed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926690583/bdwzd_qryfltr.gif)
7. In the Style screen, apply a style to the banded object.
8. Select **Finish** to create the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating a Table Report

Tables give you great control over how to present data, including placing fields, grouping them, and sorting them. A table is composed of row and columns, and each contains several cells. With such a structure a table is a good way to show any two-dimensional dataset.

**To create a table report:**

1. In the New Page Report dialog, select the desired table type in the Choose Report Layout box, then select **OK** to display the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009645882-Table-Wizard).
   * **Table (Group Above)**  
      Creates a table with group information above the detail row.
   * **Table (Group Left)**  
      Creates a table with group information left to the detail row.
   * **Table (Group Left Above)**  
      Creates a table with group information left above the detail row.
   * **Summary Table**  
      Creates a table with only group and summary information. In a summary table, all the group names will be put in the group header of the innermost group.
2. In the Data screen, select the business view in the current catalog, on which the table will be built.
3. In the Display screen, add the required fields from the Resources box to be displayed in the table. Modify the display name of any added field if necessary.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920481303/tblwzd_dsply.gif)
4. In the Group screen, add the group objects ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) as the grouping criteria, then specify the sorting direction of each group in the Sort column.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920481815/tblwzd_grp.gif)
5. To add summaries, go to the Summary screen. Select the group to which the summary will be applied, then add an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) as the summary field. For the Group Left table, you can use the Row and Column columns to control the position of the summary field in the table.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920482071/tblwzd_sum.gif)
6. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009673941-Applying-Filters#QueryFilter). If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009669621-Enter-Parameter-Values) dialog to specify values to the parameters before the Query Filter screen is displayed.
7. In the Style screen, apply a style to the table.
8. Select **Finish** to create the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating a Crosstab Report

A crosstab summarizes data and presents the summaries in a compact row and column format. Logi JReport also supports a unique compound crosstab that allows you to put multiple compound row groups and column groups together and define summaries for every combination of a compound row group and column group. This makes far more sophisticated crosstab analysis possible.

1. In the New Page Report dialog, select **Crosstab**  as the layout and select **OK** to display the [Crosstab Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009669541-Crosstab-Wizard).
2. In the Data screen, select the business view in the current catalog, on which the crosstab will be built.
3. In the Display screen, specify the fields you want to display in the crosstab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920482327/crstbwzd_dsply.gif)

   In the Columns/Rows box, add the group objects ![Group Object button](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) from the Resources box to be displayed on the columns/rows of the crosstab. If you want to display compound column/row groups in the crosstab, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404920482839/btn_pgrpt_addparal.gif) under the bottom right corner of the Columns/Rows box to create the column/row groups, then select each column/row group and add the required objects to it. You can specify a sort manner on a group object in the Sort column. In the Summaries box, add the aggregation objects ![Aggregation Objects button](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) from the Resources box to summarize data in the crosstab. If you have created compound column/row groups in the crosstab, you can add aggregations for each combination of the compound groups by selecting a compound column group and a compound row group and then adding the required aggregation objects.

   In the Display Name column, edit the display names of the added group and aggregation objects to label the columns/rows/summaries in the generated crosstab.

   If you want to remove a group object, an aggregation object, a compound column/row group, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif). To adjust the order of them, select one and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).
4. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009673941-Applying-Filters#QueryFilter). If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009669621-Enter-Parameter-Values) dialog to specify values to the parameters before the Query Filter screen is displayed.
5. In the Style screen, apply a style to the crosstab.
6. Select **Finish** to create the report.

**Tip:** When you create a crosstab with wizard, by default there will be no labels generated for its columns, rows and summaries (the Display Name columns in the Columns, Rows and Summaries boxes of the wizard are blank by default). You can make Logi JReport automatically provide the display names of the added objects in the wizard by setting the [profile options](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Crosstab) Add Labels for Crosstab Rows and Columns and Add Labels for Crosstab Summaries. You can also customize the profile option Display Crosstab Summaries Vertically to make the summaries in crosstabs displayed horizontally in Page Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating a Chart Report

A chart organizes and graphically presents data in a way that makes it easy for end users to see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form. A chart is based on the chart platform. On the platform, the chart paper, the legend, and labels make up the chart. You can create a chart that contains only simple DBFields or summaries, or a complicated chart that contains DBFields, groups, summaries, and even formulas. Normally, DBFields, summaries, and formulas in a report are represented in a chart using chart data markers, and groups are used to produce category names and data series names. DBFields can also be used as category names.

For details about the chart types Logi JReport supports, see "Chart Types" in the *Logi JReport Designer User's Guide*.

For how charts present data, see "How Data Is Represented in a Chart" in the *Logi JReport Designer User's Guide*.

For the elements that compose a chart, see "Chart Elements" in the *Logi JReport Designer User's Guide*.

**To create a chart report:**

1. In the New Page Report dialog, select **Chart** as the layout and select **OK** to display the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009669501-Chart-Wizard).

1. In the Data screen, select the business view in the current catalog, on which the chart will be built.
2. In the Type screen, specify the chart type as required.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920483095/chtwzd_type.gif)

   A default chart type exists in the Chart Type Groups box. To replace it with another one, select a chart type from the Chart Type box. The thumbnails of the subtypes in this type will then be displayed in the Subtype box. Select the required subtype to replace the default chart type.

   If you want to create a combo chart, select **<Add Combo Type>** of Primary Axis or Secondary Axis in the Chart Type Groups box, and an additional subtype will be added. To replace the additional subtype, select it, then specify the required type and subtype respectively in the Chart Type and Sub Type boxes.

   To add more subtypes, repeat the procedures. To remove a subtype, select it and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif).
3. In the Display screen, select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404920356887/btn_bvgrp.gif) in the Resources box and add it to the Category or Series box, the data of which will be displayed on the corresponding axis. Select a subtype in the Show Values box, then add an aggregation object ![](https://devnet.logianalytics.com/hc/article_attachments/4404926627351/btn_bvaggrgtn.gif) or an additional value ![](https://devnet.logianalytics.com/hc/article_attachments/4404920392599/btn_wbrpt_adtnl.gif) as the data of the subtype. You can add more than one aggregation object or additional value to a subtype. Each added subtype shall have at least one aggregation object or additional value.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920483479/chtwzd_dsply.gif)

   **To add an additional value to a subtype:**

   1. Select the subtype in the Show Values box.
   2. In the Resources box, expand the **Additional Values** node, then select **Constant Value**/**Average Value**.
   3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920379543/btn_additem.gif) beside the Show Values box. The [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009669561-Edit-Additional-Values) dialog appears.
   4. In the Name text box, specify the display name for the constant/average value.
   5. Input the constant value with numeric type in the Value text box, or select a field based on which the average value will be calculated from the Based On drop-down list.
   6. Select **OK**, and the defined constant/average value will be added to the subtype.

      If you want to further modify a constant/average value, select the value in the Show Values box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401943/btn_pgrpt_edit.gif). In the Edit Additional Value dialog, edit the value as required.
4. If you want to define the sort order and Select N condition on the category/series axis of the chart, select the **Order/Select N** button below the Category/Series box in the Display screen, then define the condition in the [Order/Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009645502-Order-Select-N) dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920483735/ordrslctn.gif)

   **To define a sort order and Select N condition on the category/series axis:**

   1. In the Order box of the Order/Select N dialog, specify in which order values on the category/series axis will be sorted.
   2. In the Select N box, specify the Select N condition to All, Top or Bottom. If All is selected, all category/series values will be shown in the chart; if Top or Bottom is selected, the text field next to it will be enabled and you can specify an integer here, which means that the first or last N category/series values will be shown in the chart.
   3. Check the **Based On** checkbox and specify values for the two drop-down lists that follow according to your requirement.

      If Based On is unchecked, the order of the first or last N category/series values will be based on what you specify in the Order box of the dialog; if you check it, the order will be based on values of the summary field and the sort direction you specify in the drop-down lists next to the Based On checkbox.
   4. If you have selected Top or Bottom from the Select N drop-down list, you can check the **Other** checkbox and the type a character string in the next text field, so that the category/series values beyond the first or last N range will be merged into the group with the name as that character string.
   5. Select **OK** to accept the settings.
5. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009673941-Applying-Filters#QueryFilter). If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009669621-Enter-Parameter-Values) dialog to specify values to the parameters before the Query Filter screen is displayed.
6. In the Style screen, apply a style to the chart.
7. Select **Finish** to create the report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674061-Page-Report-Studio-Window-Elements)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673921-Editing-Page-Reports-in-Page-Report-Studio)
