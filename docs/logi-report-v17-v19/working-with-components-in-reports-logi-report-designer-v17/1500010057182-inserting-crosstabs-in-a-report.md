---
title: "Inserting Crosstabs in a Report"
id: 1500010057182
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057182-Inserting-Crosstabs-in-a-Report
updated_at: 2022-03-28T07:17:05Z
---

# Inserting Crosstabs in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057162-Working-with-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs)

# Inserting Crosstabs in a Report

You can create crosstabs in a report easily using the crosstab wizard, however, the wizard varies with the data resource type used for the crosstab: business view or query resource. This topic introduces how you can create a crosstab with the crosstab wizard using different data resource.

You can insert crosstabs in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship). When you insert a crosstab into a banded object in a page report, you can use a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500010056782-Setting-Up-Data-Container-Links-in-Banded-Objects) to define the relationship between the crosstab and its parent.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) A page report can use either query resources or business views, which is determined at the time when [you create the page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) by the **Create Using Business View** option. Once defined, all the data components in the page report can only use the specified data resource type.

This topic contains the following sections:

* [Creating a Crosstab Based on a Business View](#BV)
* [Creating a Crosstab Based on a Query Resource](#Query)
  + [Example of Creating a Compound Crosstab](#Compound)

## Creating a Crosstab Based on a Business View

1. Position the mouse pointer at the destination where you want to insert the crosstab.
2. Do one of the following:
   * Drag the **Crosstab** icon ![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404848608023/btn_crstb.gif)from the Grid category of the Components panel to the report.
   * Select **Insert** > **Crosstab**.
   * Select **Home** > **Insert** > **Crosstab.**

   Designer displays the [Create Crosstab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058342-Create-Crosstab-Dialog-Box#BV), which contains a set of screens for helping you define a crosstab easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the business view in the current catalog using which to create the crosstab.

   If you have specified to insert the crosstab into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel, Designer displays the **Inherit from the Parent** option. Select it if you want the crosstab to inherit the business view that its parent banded object uses.

   ![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848608279/crtcrstab_dt_bv.gif)
4. In the **Display** screen, specify the fields to display in the crosstab. You can specify a title for the crosstab in the **Title** text box.

   ![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848608535/crtcrstab_dsply_bv.gif)

   The Resources box lists the view elements in the specified business view and the [dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) that you have created for the business view in the current report. You can use these objects to create the crosstab.

   * In the **Columns** and **Rows** boxes, add group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404848663831/bv_grp.gif) or dynamic formulas used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404857035543/bv_dynfmla_grp.gif) as the column/row fields to display on the column and row headers of the crosstab. You can add an object using either the button beside the target box or by dragging it from the Resources box to the target box.

     For each column/row field, you can double-click in the **Label** text box and type a name to label the corresponding column/row header, or select the **Auto Map Field Name** checkbox in the text box if you want to automatically map the label text to the dynamic display name of the field at runtime (the Label text box is blank by default so the crosstab shows no label for the column/row header); double-click in the **Color** text box to specify its background color (to make the color take effect, you need to edit the Background property of the field to "Transparent" in the Report Inspector after you finish creating the crosstab); select the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404856993559/btn_sort1.gif) to change the sort manner of its values between Ascend, Descend, and No Sort. To adjust the display order of the column/row fields on the column/row headers, select a field and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button; to delete an unwanted column/row field, select it and select the **Remove** button ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) or drag and drop it to the Resources box.
   * In the **Summaries** box, add aggregation objects ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404857037591/bv_agg.gif), detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664087/bv_detail.gif), dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664855/bv_dynfmla_agg.gif), dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664343/bv_dynfmla_dtl.gif), or dynamic aggregations ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404857037591/bv_agg.gif) as aggregate fields to create aggregations in the crosstab. You can add an object by either selecting ![Add Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/4404856993303/btn_addsum.gif) or dragging it from the Resources box to the Summaries box. When you add a detail object as the aggregate field, double-click in the **Aggregate** text box to specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function)  for it. If you select **DistinctSum**, you should select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box) dialog box.

     For each aggregate field, you can double-click in the **Label** text box and type a name to label the corresponding aggregations in the crosstab, or select the **Auto Map Field Name** checkbox in the text box if you want to automatically map the label text to the dynamic display name of the field at runtime (the Label text box is blank by default so the crosstab shows no label for the aggregations); select the **Comparison Function** button to define [a comparison function](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#Comparison) for it. To adjust the display order of the aggregate fields, select a field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif); to delete an unwanted aggregate field, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) or drag and drop it to the Resources box.

     An aggregate field can generate detail aggregations, aggregations for subtotals, and aggregations for grand totals for each combination of the column and row fields.
5. In the **Filter** screen, apply a filter to reduce the data to display in the crosstab. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the **Filter** drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   ![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856994071/crtcrstab_fltr_bv.gif)
6. In the **Layout** screen, specify the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#Layout) of the crosstab.

   ![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404856994455/crtcrstab_layout.gif)
7. In the **Style** screen. specify the style of the crosstab.

   If you have specified to insert the crosstab into a banded object, by default, the crosstab [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062802-Applying-Styles-to-Reports#Inherit); to apply another style to the crosstab, clear the **Inherit Style** option and then select the required style from the **Style** box.

   ![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848610071/crtcrstab_sty.gif)
8. Select **Finish** to insert the crosstab in the report.

   If you have selected a panel in a banded object as the crosstab destination, after finishing the dialog box, you need to select the mouse button in the destination once again in order to insert the crosstab there.

## Creating a Crosstab Based on a Query Resource

Using query resources, you can create compound crosstabs. A compound crosstab contains multiple crosstabs that are mashed up together in a flexible way. You can create aggregations based on any combinations of the row and column compound groups, making more complex analysis possible.

1. Position the mouse pointer at the destination where you want to insert the crosstab.
2. Select **Insert** > **Crosstab** or **Home** > **Insert** > **Crosstab.**

   Designer displays the [Create Crosstab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058342-Create-Crosstab-Dialog-Box#Query), which contains a set of screens for helping you define a crosstab easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the data resource in the current catalog using which to create the crosstab.

   ![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856995095/crtcrstab_dt.gif)

   If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one in the current catalog to use. When you select a query, you can select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog). Designer then automatically creates a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets) based on the selected data resource in the page report.

   If you want to use an existing dataset in the current page report to create the crosstab, select the **More Options** button and then:

   * Select the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select the **<New Dataset...>** item to create a dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.
   * If you have specified to insert the crosstab into an object that already applies a dataset, such as a banded panel, Designer enables the **Current Dataset** radio button. Select it if you want the crosstab to inherit the dataset from the parent object.
4. In the **Display** screen, specify the fields you want to display in the crosstab.

   ![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/4404848610839/crtcrstab_dsply.gif)

   The Resources box lists the DBFields in the specified data resource as well as the formulas that are valid to these DBFields in the current catalog. You can create the crosstab using these fields. If the predefined formulas cannot meet your requirement, you can select **<New Formula...>** in the Formulas node to [create the formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog) you want.

   * In the **Columns** and **Rows** boxes, add column/row fields to display on the column and row headers of the crosstab. To add a column/row field, select a DBField or formula in the Resources box and select the button beside the target box, or drag and drop it from the Resources box to the target box. If you want to display compound column/row groups in the crosstab, select the **Add Compound Group** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404848611095/btn_addparal.gif) at the right bottom corner of the Columns/Rows box to create them, then select each compound group and add the required fields to it.

     For each column/row field, you can double-click in the **Label** text box and type a name to label the corresponding column/row header (the Label text box is blank by default so the crosstab shows no label for the column/row header); double-click in the **Color** text box to specify its background color (to make the color take effect, you need to edit the Background property of the field to "Transparent" in the Report Inspector after you finish creating the crosstab); select ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404856993559/btn_sort1.gif) to change the sort manner of its values between Ascend, Descend, and No Sort. To adjust the display order of the column/row fields on the column/row headers, select a field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) ; to delete an unwanted column/row field or compound group, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) or drag and drop it to the Resources box. You can also adjust the display order of the compound groups by selecting a compound group and selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif); to delete a compound group, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif).
   * In the **Summaries** box, add aggregate fields to create aggregations in the crosstab. To add an aggregate field, select a DBField or formula in the Resources box and select ![Add Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/4404856993303/btn_addsum.gif) or drag and drop to the Summaries box. You can also select **<New Crosstab Formula...>** in the **Crosstab Formulas** node to [create crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010094701-Using-Crosstab-Formulas) to use as the aggregate field. When you add a DBField or formula as the aggregate field, double-click in the **Aggregate** text box to specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) for it. If you select **DistinctSum**, you should select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box) dialog box. If you have created compound column and row groups in the crosstab, you can add aggregate fields for each combination of the compound groups by selecting a row/column group and a column/row group and then adding the required fields.

     For each aggregate field, you can also double-click in the **Label** text box and type a name to label the corresponding aggregations in the crosstab (the Label text box is blank by default so the crosstab shows no label for the aggregations); select the **Comparison Function** button to define [a comparison function](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#Comparison) for it. To adjust the display order of the aggregate fields, select a field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif); to delete an unwanted aggregate field, select it and select ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif) or drag and drop it to the Resources box.

     An aggregate field can generate detail aggregations, aggregations for subtotals, and aggregations for grand totals for each combination of the column and row fields.
5. In the **Filter** screen, add filter conditions based on the fields that have been added to the crosstab to reduce the data. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010101241-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404848611607/crtcrstab_fltr.gif)
6. In the **Layout** screen, specify the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#Layout) of the crosstab.

   ![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404856994455/crtcrstab_layout.gif)
7. In the **Style** screen, specify the style of the crosstab.

   If you have specified to insert the crosstab into a banded object, by default, the crosstab [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062802-Applying-Styles-to-Reports#Inherit); to apply another style to the crosstab, clear the **Inherit Style** option and then select the required style from the Style box.

   ![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/4404848610071/crtcrstab_sty.gif)
8. Select **Finish** to insert the crosstab.

   If you have selected a panel in a banded object as the crosstab destination, after finishing the dialog box, you need to select the mouse button in the destination once again in order to insert the crosstab there.

Besides using the wizard, you can also drag a blank crosstab to a page report that is created using query resources. To do this:

1. From the **Components** panel, drag the **Crosstab** icon **![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404848608023/btn_crstb.gif)** in the Grid category to the destination in the page report which allows the insertion of a crosstab. Designer creates a blank crosstab.
2. In the **Data** panel, select the dataset in the current page report with which you want to create the crosstab from the dataset drop-down list, or select **<Choose Data from...>** from the list to create a new a dataset for the crosstab.
3. [Drag the required fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#Add) from the Data panel to create the column headers, row headers and aggregations in the crosstab.

### Example of Creating a Compound Crosstab

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog box, select **Crosstab** and select **OK**. Designer displays the Crosstab Wizard dialog box.
4. In the **Data** screen, select the query **WorldWideSales** in Data Source 1 of the catalog.
5. In the **Display** screen, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848611095/btn_addparal.gif) in the **Rows** box and Designer adds two compound row groups in the box.

   ![Add Compound Row Groups](https://devnet.logianalytics.com/hc/article_attachments/4404857044759/cmpnt_crstb_inst_cmpd1.gif)
6. Select **Row Compound Group**, drag and drop the formula **year** and the field **Category** in the Products table from the Resources box to the compound row group one by one, double-click in the **Label** text box of each field and type **Year** and **Category** to label the row headers.
7. Select **Row Compound Group 1** and add the field **Country** in the Customers table to it and edit its label to **Country**.

   ![Add Fields to Compound Row Groups](https://devnet.logianalytics.com/hc/article_attachments/4404857045015/cmpnt_crstb_inst_cmpd2.gif)
8. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848611095/btn_addparal.gif) in the **Columns** box, then add the formula **Quarter** to **Column Compound Group** and the field **Order ID** in the Orders table to **Column Compound Group 1**, specify their labels as **Quarter** and **Order ID.**
9. Select **Row Compound Group** in the Rows box and **Column Compound Group** in the Columns box, drag and drop the field **Quantity** in the Orders Detail table from the Resources box to the Summaries box as the aggregate field of the compound groups. Double-click in the **Aggregate** text box and select **Sum** from the drop-down list that appears, then double-click in the **Label** text box and type **Quantity** to label the aggregations.

   ![Add Aggreagate Field to Compound Groups](https://devnet.logianalytics.com/hc/article_attachments/4404857045399/cmpnt_crstb_inst_cmpd3.gif)
10. Repeat the above step to add the following fields with the specified aggregate functions as the aggregate fields for the combinations of the following compound groups. Use the fields' display names as the labels.
    * Row Compound Group and Column Compound Group 1: **Price**, **Average**
    * Row Compound Group 1 and Column Compound Group: **Cost**, **Sum**
    * Row Compound Group 1 and Column Compound Group 1: **Unit Price**, **Average**
11. Switch to the **Filter** screen and specify the filter conditions as follows:

    ![Specify Filter Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404848675479/cmpnt_crstb_inst_cmpd4.gif)
12. Select **Finish** to create the crosstab.
13. In the Report Inspector, select **Label**, **Label 1**, **QUARTER**, **Label 4**, **Label 5**, **YEAR**, **Label 6**, **Label 7**, **CATEGORY**, **Label 10**, **Label 11**, **Label 12**, **QUANTITY**, **QUANTITY 1**, **QUANTITY 2**, **QUANTITY 3**, **QUANTITY 4**, and **QUANTITY 5** at the same time by pressing the Ctrl key on the keyboard, specify the **Background** property to **Lightgray**.

    ![Set the Background Property for Objects](https://devnet.logianalytics.com/hc/article_attachments/4404848675735/cmpnt_crstb_inst_cmpd5.gif)
14. Repeat the above step to specify the Background property of Label 2, Label 3, Order ID, Label 15, Label 16, Label 17, PRICE, PRICE 1, PRICE 2, PRICE 3, PRICE 4, and PRICE 5 to **Pink**; specify the Background property of Label 8, Label 9, COUNTRY, Label 13, Label 14, COST, COST 1, COST 2, and COST 3 to **Orange**; specify the Background property of Label 18, Label 19, UNIT PRICE, UNIT PRICE 1, UNIT PRICE 2, and UNIT PRICE 3 to **Gray**.
15. Save the report.
16. Select **View** > **Preview As** > **Page Report Result**. You can see the crosstab contains four parts, showing different summary information for different combinations of row compound groups and column compound groups.

    ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404848676247/cmpnt_crstb_inst_cmpd6.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057162-Working-with-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs)
