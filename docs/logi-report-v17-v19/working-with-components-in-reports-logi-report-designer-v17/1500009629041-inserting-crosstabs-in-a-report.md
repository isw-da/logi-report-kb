---
title: "Inserting Crosstabs in a Report"
id: 1500009629041
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629041-Inserting-Crosstabs-in-a-Report
updated_at: 2021-07-24T16:05:16Z
---

# Inserting Crosstabs in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606202-Crosstabs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs)

# Inserting Crosstabs in a Report

With the crosstab wizard, it is easy to create crosstabs in a report, however the wizard varies with the data resource type used for the crosstab: business view or query resource.

A web report and library component can only use business views. For a page report it can be created either based on query resources or business views, which is determined at the time when  [the page report is created](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page)  by the Create Using Business View option. Once defined, all the data components in the page report can only be created on the specified data resource type.

A crosstab can be inserted in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports#Relationship). When it is inserted into a banded object, you can use a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500009628401-Setting-Up-Data-Container-Links-in-Banded-Objects) to define the relationship between the crosstab and its parent.

This topic shows creating crosstabs using different data resources in detail:

* [Creating a Crosstab Based on a Business View](#BV)
* [Creating a Crosstab Based on a Query Resource](#Query)
  + [Example of Creating a Compound Crosstab](#Compound)

## Creating a Crosstab Based on a Business View

1. Position the mouse pointer at the destination where you want to insert the crosstab.
2. Do one of the following:
   * Drag ![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404904436631/btn_crstb.gif)from the Grid category of the Components panel to the report.
   * Select **Insert** > **Crosstab**.
   * Select **Home** > **Insert** > **Crosstab.**

   The [Create Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009607522-Create-Crosstab-Dialog#BV) wizard appears, which contains a set of screens for helping you define a crosstab easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select the business view in the current catalog using which to create the crosstab. When the crosstab is to be inserted into the banded header, banded footer, group header, group footer panel of a banded object in a web report, you can also select **Inherit from the Parent** to inherit data from the business view used by the parent banded object.

   ![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/4404904371735/crtcrstab_dt_bv.gif)
4. In the Display screen, specify the fields to display in the crosstab. You can specify a title for the crosstab in the Title text box.

   ![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904371991/crtcrstab_dsply_bv.gif)

   The Resources box lists the view elements in the specified business view and the [dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) created for the business view in the current report. You can use these objects to create the crosstab.

   * In the Columns and Rows boxes, add group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif) or dynamic formulas used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif) as column/row fields to display on the column and row headers of the crosstab. You can add an object using either the button beside the target box or by dragging it from the Resources box to the target box.

     For each column/row field, you can double-click in the Label text box and type a name to label the corresponding column/row header, or select the **Auto Map Field Name** checkbox in the text box if you want to automatically map the label text to the dynamic display name of the field at runtime (by default the Label text box is blank and no label will be created for the column and row headers in a crosstab); double-click in the Color text box to specify its background color (to make the color take effect you need to edit the Background property of the field to Transparent in the Report Inspector after the crosstab is created); select ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404904373143/btn_sort1.gif) to change the sort manner of its values between Ascend, Descend and No Sort. To adjust the display order of the column/row fields on the column/row headers, select a field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif); to remove an unwanted column/row field, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)or drag and drop it to the Resources box.
   * In the Summaries box, add aggregation objects ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif), detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425495/bv_detail.gif), dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427799/bv_dynfmla_agg.gif), dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828823/bv_dynfmla_dtl.gif) or dynamic aggregations ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) as aggregate fields to create aggregations in the crosstab. You can add an object using either the button ![Add Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/4404904372631/btn_addsum.gif) or by dragging it from the Resources box to the Summaries box. When a detail object is added as aggregate field, double-click in the Aggregate text box to specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function)  for it.
     When DistinctSum is selected as the function, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

     For each aggregate field, you can double-click in the Label text box and type a name to label the corresponding aggregations in the crosstab, or select the **Auto Map Field Name** checkbox in the text box if you want to automatically map the label text to the dynamic display name of the field at runtime (by default the Label text box is blank and no label will be created for the aggregations in a crosstab); select the **Comparison Function** button to define [a comparison function](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Comparison) for it. To adjust the display order of the aggregate fields, select a field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif); to remove an unwanted aggregate field, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)or drag and drop it to the Resources box.

     An aggregate field can generate detail aggregations, aggregations for subtotals and aggregations for grand totals for each combination of the column and row fields.
5. In the Filter screen, apply a filter to reduce the data displayed in the crosstab. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the Filter drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   ![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904373655/crtcrstab_fltr_bv.gif)
6. In the Layout screen, specify the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Layout) of the crosstab.

   ![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904374167/crtcrstab_layout.gif)
7. In the Style screen. specify the style of the crosstab.

   ![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904374423/crtcrstab_sty.gif)

   When you have specified to insert the crosstab into a banded object, by default the crosstab will [inherit its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613462-Applying-Styles#Inherit). If you want to apply another style to the crosstab, clear the **Inherit Style** option and then select the required style from the Style box.
8. Select **Finish** to insert the crosstab in the report.

   If you have selected a panel in a banded object as the crosstab destination, after finishing the wizard you need to select the mouse button in the destination once again in order to insert the crosstab there.

## Creating a Crosstab Based on a Query Resource

Using query resources, you can create compound crosstabs. A compound crosstab contains multiple crosstabs that are mashed up together in a flexible way. Aggregations can be created based on any combinations of the row and column compound groups, making more complex analysis possible.

1. Position the mouse pointer at the destination where you want to insert the crosstab.
2. Select **Insert** > **Crosstab** or **Home** > **Insert** > **Crosstab.**

   The [Create Crosstab](https://devnet.logianalytics.com/hc/en-us/articles/1500009607522-Create-Crosstab-Dialog#Query) wizard appears, which contains a set of screens for helping you define a crosstab easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select the data resource in the current catalog using which to create the crosstab.

   ![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916811159/crtcrstab_dt.gif)

   If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one in the current catalog. When a query is selected, you can select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog). Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current page report to create the crosstab, select the **More Options** button and then:

   * Select the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog), or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report will still run the query separately for each dataset.
   * Select the **Current Dataset** radio button to make the crosstab inherit the dataset from its parent.
4. In the Display screen, specify the fields you want to display in the crosstab.

   ![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904374935/crtcrstab_dsply.gif)

   The Resources box lists the DBFields in the specified data resource as well as the formulas that are valid to these DBFields in the current catalog. You can create the crosstab using these fields. If the predefined formulas cannot meet your requirement, you can select **<New Formula...>** in the Formulas node to [create the formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009634201-Creating-Formulas-in-a-Catalog) you want.

   * In the Columns and Rows boxes, add column/row fields to display on the column and row headers of the crosstab. To add a column/row field, select a DBField or formula in the Resources box and select ![Add Column button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or ![Add Row button](https://devnet.logianalytics.com/hc/article_attachments/4404904372247/btn_addrow.gif) , or drag and drop it from the Resources box to the target box. If you want to display compound column/row groups in the crosstab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404904375447/btn_addparal.gif) at the right bottom corner of the Columns/Rows box to create them, then select each compound group and add the required fields to it.

     For each column/row field, you can double-click in the Label text box and type a name to label the corresponding column/row header (by default the Label text box is blank and no label will be created for the column and row headers in a crosstab); double-click in the Color text box to specify its background color (to make the color take effect you need to edit the Background property of the field to Transparent in the Report Inspector after the crosstab is created); select ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404904373143/btn_sort1.gif) to change the sort manner of its values between Ascend, Descend and No Sort. To adjust the display order of the column/row fields on the column/row headers, select a field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif); to remove an unwanted column/row field or compound group, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)or drag and drop it to the Resources box. The display order of the compound groups can also be adjusted by selecting a compound group and selecting ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif); to remove a compound group, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).
   * In the Summaries box, add aggregate fields to create aggregations in the crosstab. To add an aggregate field, select a DBField or formula in the Resources box and select ![Add Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/4404904372631/btn_addsum.gif) or drag and drop to the Summaries box. You can also select **<New Crosstab Formula...>** in the Crosstab Formulas node to [create crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009606222-Using-Crosstab-Formulas) to use as the aggregate field. When a DBField or formula is added as aggregate field, double-click in the Aggregate text box to specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function)  for it. When DistinctSum is selected as the function, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog. If you have created compound column and row groups in the crosstab, you can add aggregate fields for each combination of the compound groups by selecting a row/column group and a column/row group and then adding the required fields.

     For each aggregate field, you can also double-click in the Label text box and type a name to label the corresponding aggregations in the crosstab (by default the Label text box is blank and no label will be created for the aggregations in a crosstab); select the **Comparison Function** button to define [a comparison function](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Comparison) for it. To adjust the display order of the aggregate fields, select a field and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif); to remove an unwanted aggregate field, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)or drag and drop it to the Resources box.

     An aggregate field can generate detail aggregations, aggregations for subtotals and aggregations for grand totals for each combination of the column and row fields.
5. In the Filter screen, add filter conditions on the fields that have been added to the crosstab to reduce the data. For how to define a filter, [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009636161-Filtering-Reports#DefineFilter).

   ![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404904375703/crtcrstab_fltr.gif)
6. In the Layout screen, specify the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Layout) of the crosstab.

   ![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904374167/crtcrstab_layout.gif)
7. In the Style screen, specify the style of the crosstab.

   ![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904374423/crtcrstab_sty.gif)

   When you have specified to insert the crosstab into a banded object, by default the crosstab will [inherit its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613462-Applying-Styles#Inherit). If you want to apply another style to the crosstab, clear the **Inherit Style** option and then select the required style from the Style box.
8. Select **Finish** to insert the crosstab.

   If you have selected a panel in a banded object as the crosstab destination, after finishing the wizard you need to select the mouse button in the destination once again in order to insert the crosstab there.

Besides using the wizard, you can also drag a blank crosstab to a page report that is created using query resources. To do this:

1. From the Grid category of the Components panel, drag **![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4404904436631/btn_crstb.gif)** to the destination in the page report which allows the insertion of a crosstab. A blank crosstab is then created.
2. In the Data panel, select the dataset in the current page report with which you want to create the crosstab from the dataset drop-down list, or select **<Choose Data from...>** from the list to create a new a dataset for the crosstab.
3. [Drag the required fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#Add) from the Data panel to create the column headers, row headers and aggregations in the crosstab.

### Example of Creating a Compound Crosstab

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog, select **Crosstab** and select **OK**.
4. In the Data screen of the Crosstab Wizard, select the query **WorldWideSales** in Data Source 1 of the catalog.
5. In the Display screen, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904375447/btn_addparal.gif) in the Rows box and two compound row groups appear in the box.

   ![Add Compound Row Groups](https://devnet.logianalytics.com/hc/article_attachments/4404904436887/cmpnt_crstb_inst_cmpd1.gif)
6. Select **Row Compound Group**, drag and drop the formula **year** and the field **Category** in the Products table from the Resources box to the compound row group one by one, double-click in the Label text box of each field and type **Year** and **Category** to label the row headers.
7. Select **Row Compound Group 1** and add the field **Country** in the Customers table to it and edit its label to **Country**.

   ![Add Fields to Compound Row Groups](https://devnet.logianalytics.com/hc/article_attachments/4404904437399/cmpnt_crstb_inst_cmpd2.gif)
8. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904375447/btn_addparal.gif) in the Columns box, then add the formula **Quarter** to Column Compound Group and the field **Order ID** in the Orders table to Column Compound Group 1, specify their labels as **Quarter** and **Order ID.**
9. Select **Row Compound Group** in the Rows box and **Column Compound Group** in the Columns box, drag and drop the field **Quantity** in the Orders Detail table from the Resources box to the Summaries box as the aggregate field of the compound groups. double-click in the Aggregate text box and select **Sum** from the drop-down list that appears, then double-click in the Label text box and type **Quantity** to label the aggregations.

   ![Add Aggreagate Field to Compound Groups](https://devnet.logianalytics.com/hc/article_attachments/4404904437655/cmpnt_crstb_inst_cmpd3.gif)
10. Repeat the above step to add the following fields with the specified aggregate functions as the aggregate fields for the combinations of the following compound groups. Use the fields' display names as the labels.
    * Row Compound Group and Column Compound Group 1: **Price**, **Average**
    * Row Compound Group 1 and Column Compound Group: **Cost**, **Sum**
    * Row Compound Group 1 and Column Compound Group 1: **Unit Price**, **Average**
11. Switch to the Filter screen and specify the filter condition as *Category in Blends,Bold And Country in Australia,Belgium*. Select **Finish**.

    ![Specify Filter Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404916833431/cmpnt_crstb_inst_cmpd4.gif)
12. In the Report Inspector, select **Label**, **Label 1**, **QUARTER**, **Label 4**, **Label 5**, **YEAR**, **Label 6**, **Label 7**, **CATEGORY**, **Label 10**, **Label 11**, **Label 12**, **QUANTITY**, **QUANTITY 1**, **QUANTITY 2**, **QUANTITY 3**, **QUANTITY 4** and **QUANTITY 5** at the same time by pressing the Ctrl key on the keyboard, specify the Background property to **Lightgray**.

    ![Set the Background Property for Objects](https://devnet.logianalytics.com/hc/article_attachments/4404904437911/cmpnt_crstb_inst_cmpd5.gif)
13. Repeat the above step to specify the Background property of Label 2, Label 3, Order ID, Label 15, Label 16, Label 17, PRICE, PRICE 1, PRICE 2, PRICE 3, PRICE 4 and PRICE 5 to **Pink**, specify the Background property of Label 8, Label 9, COUNTRY, Label 13, Label 14, COST, COST 1, COST 2 and COST 3 to **Orange**, specify the Background property of Label 18, Label 19, UNIT PRICE, UNIT PRICE 1, UNIT PRICE 2 and UNIT PRICE 3 to **Gray**.
14. Save the report and select **View** > **Preview As** > **Page Report Result**. You can see the crosstab is composed of four parts, showing different summary information for different combinations of row compound groups and column compound groups.

    ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404904438167/cmpnt_crstb_inst_cmpd6.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606202-Crosstabs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs)
