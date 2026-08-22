---
title: "Inserting Crosstabs in a Report"
id: 4405664394775
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664394775-Inserting-Crosstabs-in-a-Report
updated_at: 2022-03-28T07:09:58Z
---

# Inserting Crosstabs in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664392727-Working-with-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs)

# Inserting Crosstabs in a Report

You can create crosstabs in a report easily using the crosstab wizard, however, the wizard varies with the data resource type used for the crosstab: business view or query resource. This topic introduces how you can create a crosstab with the crosstab wizard using different data resource.

You can insert crosstabs in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship). When you insert a crosstab into a banded object in a page report, you can use a [data container link](https://devnet.logianalytics.com/hc/en-us/articles/4405664367511-Setting-Up-Data-Container-Links-in-Banded-Objects) to define the relationship between the crosstab and its parent.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) A page report can use either query resources or business views, which is determined by the Create Using Business View option at the time when [you create the page report](https://devnet.logianalytics.com/hc/en-us/articles/4405661926423-Creating-Reports#Page). Once defined, all the data components in the page report can only use the specified data resource type.

This topic contains the following sections:

* [Creating a Crosstab Based on a Business View](#BV)
* [Creating a Crosstab Based on a Query Resource](#Query)
  + [Example of Creating a Compound Crosstab](#Compound)

## Creating a Crosstab Based on a Business View

1. Position the mouse pointer at the destination where you want to insert the crosstab.
2. Do one of the following:
   * From the **Components** panel, drag the **Crosstab** icon ![Crosstab icon](https://devnet.logianalytics.com/hc/article_attachments/4420402510231/icon_crstb.gif) in the **Grid** category to the report.
   * Navigate to **Insert** > **Crosstab**.
   * Navigate to **Home** > **Insert** > **Crosstab**.

   Designer displays the [Create Crosstab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664439575-Create-Crosstab-Dialog-Box#BV), which contains a set of screens for helping you define a crosstab easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the business view in the current catalog that you want to use to create the crosstab.

   If you have specified to insert the crosstab into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel, Designer displays the **Inherit from the Parent** option. Select it if you want the crosstab to inherit the business view that its parent banded object uses.

   ![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/4420402510487/crtcrstab_dt_bv.gif)
4. In the **Display** screen, specify the fields to display in the crosstab. You can specify a title for the crosstab in the **Title** text box.

   ![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/4420410817559/crtcrstab_dsply_bv.gif)

   The Resources box lists the view elements in the specified business view and the [dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/4405661937559-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) that you have created for the business view in the current report. You can use these objects to create the crosstab.

   * In the **Columns** and **Rows** boxes, add group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4420410873495/bv_grp.gif) or dynamic formulas used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4420402567703/bv_dynfmla_grp.gif) as the column/row fields to display on the column and row headers of the crosstab. You can add an object using either the arrow button beside the target box or by dragging it from the Resources box to the target box.

     For each column/row field, you can specify the following:

     + Double-click in the **Label** text box and type a name to label the corresponding column/row header; when you select the **Auto Map Field Name** checkbox in the text box, Designer applies the field's display name as the label, and at runtime, Server maps the label to the dynamic display name of the field if the administrator defines it (the Label text box is blank by default so the crosstab shows no label for the column/row header).
     + Double-click in the **Color** text box to specify its background color (to make the color take effect, you need to edit the Background property of the field to "Transparent" in the Report Inspector after you finish creating the crosstab).
     + Select **Sort**![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420402511383/btn_sort1.gif) to change the sort manner of its values between Ascend, Descend, and No Sort.
     + Select a field and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif) to adjust the display order of the field on the column/row header.
     + Select an unwanted field and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif) or drag it to the Resources box to remove it from the crosstab.
   * In the **Summaries** box, add aggregation objects ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4420394888471/bv_agg.gif), detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4420402567447/bv_detail.gif), dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4420410877719/bv_dynfmla_agg.gif), dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4420402567959/bv_dynfmla_dtl.gif), or dynamic aggregations ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4420394888471/bv_agg.gif) as aggregate fields to create aggregations in the crosstab. You can add an object by either selecting **Add**![Add Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/4420394843415/btn_addsum.gif) or dragging it from the Resources box to the Summaries box. When you add a detail object as the aggregate field, double-click in the **Aggregate** text box to specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Function) for it. If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420402297111/btn_ellipsis2.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405664572951-Select-Fields-Dialog-Box) dialog box.

     For each aggregate field, you can specify the following:

     + Double-click in the **Label** text box and type a name to label the corresponding aggregations in the crosstab; when you select the **Auto Map Field Name** checkbox in the text box, Designer applies the field's display name as the label, and at runtime, Server maps the label to the dynamic display name of the field if the administrator defines it (the Label text box is blank by default so the crosstab shows no label for the aggregations).
     + Select a field and select **Comparison Function** to define [a comparison function](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs#Comparison) for it.
     + Select a field and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif) to adjust the display order of the aggregate fields.
     + Select an unwanted field and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif) or drag it to the Resources box to remove it from the crosstab.

     An aggregate field can generate detail aggregations, aggregations for subtotals, and aggregation for grand total.
5. In the **Filter** screen, apply a filter to reduce the data to display in the crosstab. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/4405664681111-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the **Filter** drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   ![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420394843799/crtcrstab_fltr_bv.gif)
6. In the **Layout** screen, specify the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs#Layout) of the crosstab.

   ![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/4420402511895/crtcrstab_layout.gif)
7. In the **Style** screen, specify the style of the crosstab.

   If you have specified to insert the crosstab into a banded object, the crosstab [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports#Inherit) by default; to apply another style to the crosstab, clear **Inherit Style** and select the required style from the **Style** box.

   ![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/4420402512407/crtcrstab_sty.gif)
8. Select **Finish** to insert the crosstab in the report.

   If you have selected a panel in a banded object as the crosstab destination, after finishing the dialog box, you need to select in the destination once again in order to insert the crosstab there.

## Creating a Crosstab Based on a Query Resource

Using query resources, you can create compound crosstabs. A compound crosstab contains multiple crosstabs that are mashed up together in a flexible way. You can create aggregations based on any combinations of the row and column compound groups, making more complex analysis possible.

1. Position the mouse pointer at the destination where you want to insert the crosstab.
2. Navigate to **Insert** > **Crosstab** or **Home** > **Insert** > **Crosstab**.

   Designer displays the [Create Crosstab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664439575-Create-Crosstab-Dialog-Box#Query), which contains a set of screens for helping you define a crosstab easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the data resource in the current catalog that you want to use to create the crosstab.

   ![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/4420394844439/crtcrstab_dt.gif)

   If the predefined data resources are not what you want, you can select the first item under a resource node to create a data resource of the type in the current catalog to use. When you select a query, you can select **Edit** to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/4405661917975-Creating-Queries-in-a-Catalog). Designer then automatically creates a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets) based on the selected data resource in the page report.

   If you want to use an existing dataset in the current page report to create the crosstab, select **More Options** and then:

   * Select **Existing Dataset** and select a dataset. You can select **Edit** to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661501079-Dataset-Editor-Dialog-Box), or select **<New Dataset...>** to [create a dataset](https://devnet.logianalytics.com/hc/en-us/articles/4405661914263-Creating-and-Managing-Datasets#Create) in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.
   * If you have specified to insert the crosstab into an object that already applies a dataset, such as a banded panel, Designer enables the **Current Dataset** radio button. Select it if you want the crosstab to inherit the dataset from the parent object.
4. In the **Display** screen, specify the fields to display in the crosstab.

   ![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/4420402512919/crtcrstab_dsply.gif)

   The Resources box lists the DBFields in the specified data resource, and the formulas that are valid to these DBFields in the current catalog. You can create the crosstab using these fields. If the predefined formulas cannot meet your requirement, you can select **<New Formula...>** in the Formulas node to [create the formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405661763223-Creating-Formulas-in-a-Catalog) you want.

   * In the **Columns** and **Rows** boxes, add column/row fields to display on the column and row headers of the crosstab. To add a column/row field, select a DBField or formula in the Resources box and select the arrow button beside the target box, or drag it from the Resources box to the target box. If you want to display compound column/row groups in the crosstab, select **Add Compound Group**![](https://devnet.logianalytics.com/hc/article_attachments/4420410819223/btn_addparal.gif) at the right bottom corner of the Columns/Rows box to create them, then select each compound group and add the required fields to it.

     For each column/row field, you can double-click in the **Label** text box and type a name to label the corresponding column/row header (the Label text box is blank by default so the crosstab shows no label for the column/row header); double-click in the **Color** text box to specify its background color (to make the color take effect, you need to edit the Background property of the field to "Transparent" in the Report Inspector after you finish creating the crosstab); select ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4420402511383/btn_sort1.gif) to change the sort manner of its values between Ascend, Descend, and No Sort. To adjust the display order of the column/row fields on the column/row headers, select a field and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif); to delete an unwanted column/row field or compound group, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif) or drag it to the Resources box. You can also adjust the display order of the compound groups and delete any unwanted compound group in the same way.
   * In the **Summaries** box, add aggregate fields to create aggregations in the crosstab. To add an aggregate field, select a DBField or formula in the Resources box and select **Add**![Add Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/4420394843415/btn_addsum.gif) or drag the field from the Resources box to the Summaries box. You can also select **<New Crosstab Formula...>** in the **Crosstab Formulas** node to [create crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405664393751-Using-Crosstab-Formulas) to use as the aggregate field. When you add a DBField or formula as the aggregate field, double-click in the **Aggregate** text box to specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/4405661767063-Working-with-Summaries#Function) for it. If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420402297111/btn_ellipsis2.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405664572951-Select-Fields-Dialog-Box) dialog box. If you have created compound column and row groups in the crosstab, you can add aggregate fields for each combination of the compound groups by selecting a row/column group and a column/row group and then adding the required fields.

     For each aggregate field, you can also double-click in the **Label** text box and type a name to label the corresponding aggregations in the crosstab (the Label text box is blank by default so the crosstab shows no label for the aggregations); select **Comparison Function** to define [a comparison function](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs#Comparison) for it. To adjust the display order of the aggregate fields, select a field and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif); to delete an unwanted aggregate field, select it and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif) or drag it to the Resources box.

     An aggregate field can generate detail aggregations, aggregations for subtotals, and aggregations for grand totals for each combination of the column and row fields.
5. In the **Filter** screen, add filter conditions based on the fields you have added to the crosstab to reduce the data. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/4405664691735-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/4420410819863/crtcrstab_fltr.gif)
6. In the **Layout** screen, specify the [layout properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs#Layout) of the crosstab.

   ![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/4420402511895/crtcrstab_layout.gif)
7. In the **Style** screen, specify the style of the crosstab.

   If you have specified to insert the crosstab into a banded object, the crosstab [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports#Inherit) by default; to apply another style to the crosstab, clear **Inherit Style** and select the required style from the **Style** box.

   ![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/4420402512407/crtcrstab_sty.gif)
8. Select **Finish** to insert the crosstab.

   If you have selected a panel in a banded object as the crosstab destination, after finishing the dialog box, you need to select in the destination once again in order to insert the crosstab there.

Besides using the wizard, you can also drag a blank crosstab to a page report that uses query resources.

1. From the **Components** panel, drag the **Crosstab** icon **![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/4420402510231/icon_crstb.gif)** in the **Grid** category to the destination in the page report which allows the insertion of a crosstab. Designer creates a blank crosstab.
2. In the **Data** panel, select the dataset in the current page report with which you want to create the crosstab from the dataset drop-down list, or select **<Choose Data from...>** from the list to create a new a dataset for the crosstab.
3. [Drag the required fields](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs#Add) from the Data panel to create the column headers, row headers and aggregations in the crosstab.

### Example of Creating a Compound Crosstab

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog box, select **Crosstab** and select **OK**. Designer displays the Crosstab Wizard dialog box.
4. In the **Data** screen, select the query **WorldWideSales** in Data Source 1 of the catalog.
5. In the **Display** screen, select **Add Compound Group**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410819223/btn_addparal.gif) in the **Rows** box and Designer adds two compound row groups in the box.

   ![Add Compound Row Groups](https://devnet.logianalytics.com/hc/article_attachments/4420394893847/cmpnt_crstb_inst_cmpd1.gif)
6. Select **Row Compound Group**, drag the formula **year** and the field **Category** from the Resources box to the compound row group one by one, double-click in the **Label** text box of each field and type **Year** and **Category** to label the row headers.
7. Select **Row Compound Group 1** and add the field **Country** to it and edit its label to **Country**.

   ![Add Fields to Compound Row Groups](https://devnet.logianalytics.com/hc/article_attachments/4420402576791/cmpnt_crstb_inst_cmpd2.gif)
8. Select **Add Compound Group**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410819223/btn_addparal.gif) in the **Columns** box, then add the formula **Quarter** to **Column Compound Group** and the field **Order ID** to **Column Compound Group 1**, specify their labels as **Quarter** and **Order ID**.
9. Select **Row Compound Group** in the Rows box and **Column Compound Group** in the Columns box, drag the field **Quantity** from the Resources box to the **Summaries** box as the aggregate field of the compound groups. Double-click in the **Aggregate** text box and select **Sum** from the drop-down list, then double-click in the **Label** text box and type **Quantity** to label the aggregations.

   ![Add Aggreagate Field to Compound Groups](https://devnet.logianalytics.com/hc/article_attachments/4420402577431/cmpnt_crstb_inst_cmpd3.gif)
10. Repeat the preceding step to add the following fields with the specified aggregate functions as the aggregate fields for the combinations of the following compound groups. Use the fields' display names as the labels.
    * Row Compound Group and Column Compound Group 1: **Price**, **Average**
    * Row Compound Group 1 and Column Compound Group: **Cost**, **Sum**
    * Row Compound Group 1 and Column Compound Group 1: **Unit Price**, **Average**
11. Switch to the **Filter** screen and specify the filter conditions.

    ![Specify Filter Conditions](https://devnet.logianalytics.com/hc/article_attachments/4420394894103/cmpnt_crstb_inst_cmpd4.gif)
12. Select **Finish** to create the crosstab.
13. In the Report Inspector, select **Label**, **Label 1**, **QUARTER**, **Label 4**, **Label 5**, **YEAR**, **Label 6**, **Label 7**, **CATEGORY**, **Label 10**, **Label 11**, **Label 12**, **QUANTITY**, **QUANTITY 1**, **QUANTITY 2**, **QUANTITY 3**, **QUANTITY 4**, and **QUANTITY 5**, specify the **Background** property to **Lightgray**.

    ![Set the Background Property for Objects](https://devnet.logianalytics.com/hc/article_attachments/4420410891415/cmpnt_crstb_inst_cmpd5.gif)
14. Repeat the preceding step to specify the Background property of Label 2, Label 3, Order ID, Label 15, Label 16, Label 17, PRICE, PRICE 1, PRICE 2, PRICE 3, PRICE 4, and PRICE 5 to **Pink**; specify the Background property of Label 8, Label 9, COUNTRY, Label 13, Label 14, COST, COST 1, COST 2, and COST 3 to **Orange**; specify the Background property of Label 18, Label 19, UNIT PRICE, UNIT PRICE 1, UNIT PRICE 2, and UNIT PRICE 3 to **Gray**.
15. Save the report.
16. Navigate to **View** > **Preview As** > **Page Report Result** to preview the report in Page Report Studio.

    You can see that the crosstab contains four parts, showing different summary information for different combinations of row compound groups and column compound groups.

    ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4420410891671/cmpnt_crstb_inst_cmpd6.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664392727-Working-with-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661377559-Modifying-Crosstabs)
