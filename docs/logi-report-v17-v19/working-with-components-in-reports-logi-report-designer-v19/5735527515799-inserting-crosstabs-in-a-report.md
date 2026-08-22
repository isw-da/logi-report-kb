---
title: "Inserting Crosstabs in a Report"
id: 5735527515799
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735527515799-Inserting-Crosstabs-in-a-Report
updated_at: 2022-11-02T04:28:13Z
---

# Inserting Crosstabs in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735498924183-Working-with-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs)

# Inserting Crosstabs in a Report

You can create crosstabs in a report easily using the crosstab wizard. However, the procedure you use with the wizard varies with the data resource type: business view or query resource. This topic introduces how you can create a crosstab using the crosstab wizard when you have different data resources. It also presents an example about creating a compound crosstab using a query resource in a page report.

This topic contains the following sections:

* [Creating a Crosstab Based on a Business View](#BV)
* [Creating a Crosstab Based on a Query Resource](#Query)
  + [Example: Creating a Compound Crosstab](#Compound)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) A page report can apply either query resources or business views, which is determined by the Create Using Business View option at the time when [you create the page report](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports#Page). Once defined, all data components in the page report can only use the specified data resource type.

## Creating a Crosstab Based on a Business View

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the crosstab.
2. Do one of the following:
   * From the **Components** panel, drag the **Crosstab** icon ![Crosstab icon](https://devnet.logianalytics.com/hc/article_attachments/9898532400023/icon_crstb.gif) in the **Grid** category to the report.
   * Navigate to **Insert** > **Crosstab**.
   * Navigate to **Home** > **Insert** > **Crosstab**.

   Designer displays the [Create Crosstab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522178583-Create-Crosstab-Dialog-Box#BV). You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to use to create the
   crosstab.

   ![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/9898532404247/crtcrstab_dt_bv.gif)
4. In the **Display** screen, specify the fields to display in the crosstab. You can specify a title for the crosstab in the **Title** text box.

   ![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/9898532409239/crtcrstab_dsply_bv.gif)

   The Resources box lists all view elements in the business view from which the dataset the crosstab applies is created, and the [dynamic formulas and aggregations](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report) that you have added for the business view in the current report. You can use these objects to create the crosstab.

   * In the **Columns** and **Rows** boxes, add group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898534261399/bv_grp.gif) or dynamic formulas used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898517940503/bv_dynfmla_grp.gif) as the column/row fields to display on the column and row headers of the crosstab. You can add an object using either the arrow button beside the target box or by dragging it from the Resources box to the target box.

     For the column/row fields, you can specify the following:

     + Double-click in the **Label** text box and type a name to label the corresponding column/row header (the Label text box is blank by default so the crosstab shows no label for the column/row header). When you select the **Auto Map Field Name** checkbox in the text box, Designer applies the field's display name as the label, and at runtime, Server maps the label to the dynamic display name of the field if the administrator defines it.
     + Double-click in the **Color** text box to specify background color of the field. However, to make the color take effect, you need to edit the Background property of the field to "Transparent" in the Report Inspector after you finish creating the crosstab.
     + Select a field and select **Sort**![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9898516023063/btn_sort1.gif) to change the sort manner of its values between Ascend, Descend, and No Sort.
     + Select a field and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the field on the column/row header.
     + Select an unwanted field and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif) or drag it to the Resources box to remove the field from the crosstab.
   * In the **Summaries** box, add aggregation objects ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/9898534371351/bv_agg.gif), detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/9898517937943/bv_detail.gif), dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/9898518034071/bv_dynfmla_agg.gif), dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/9898517944087/bv_dynfmla_dtl.gif), or dynamic aggregations ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/9898534371351/bv_agg.gif) as aggregate fields to create aggregations in the crosstab. You can add an object by either selecting **Add**![Add Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/9898516016791/btn_addsum.gif) or dragging it from the Resources box to the Summaries box.

     For the aggregate fields, you can specify the following:

     + When you add a detail object as the aggregate field, you need to double-click in its **Aggregate** text box to specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function). If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box) dialog box.
     + Double-click in the **Label** text box and type a name to label the corresponding aggregations in the crosstab (the Label text box is blank by default so the crosstab shows no label for the aggregations). When you select the **Auto Map Field Name** checkbox in the text box, Designer applies the field's display name as the label, and at runtime, Server maps the label to the dynamic display name of the field if the administrator defines it.
     + Select a field and select **Comparison Function** to define [a comparison function](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs#Comparison) for it.
     + Select a field and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the aggregate fields.
     + Select an unwanted field and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif) or drag it to the Resources box to remove the field from the crosstab.

     An aggregate field can generate detail aggregations, aggregations for subtotals, and aggregation for grand total.
5. In the **Dataset Filter** screen, ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")[filter the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report) the crosstab applies. If you have added filter conditions to the dataset somewhere else, Designer displays the conditions in the screen. You can further edit the conditions. Be aware that a filter on a dataset applies to all data components in the same report that use this dataset.

   ![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898516053911/crtcrstab_fltr_bv.gif)
6. In the **Layout** screen, specify the [layout](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs#Layout) of the crosstab.

   ![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/9898516169751/crtcrstab_layout.gif)
7. In the **Style** screen, specify the style of the crosstab. If you have specified to insert the crosstab into a banded object, the crosstab [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports#Inherit) by default; to apply another style to the crosstab, clear **Inherit Style** and select the required style from the **Style** box.

   ![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/9898516175895/crtcrstab_sty.gif)
8. Select **Finish** to insert the crosstab.
9. If you have selected a panel in a banded object as the destination, after finishing the Create Crosstab dialog box, you need to select in the destination once again to insert the crosstab there.

## Creating a Crosstab Based on a Query Resource

Using query resources, you can create compound crosstabs. A compound crosstab contains multiple crosstabs that are mashed up together in a flexible way. You can create aggregations based on any combinations of the row and column compound groups, making more complex analysis possible.

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the crosstab.
2. Navigate to **Insert** > **Crosstab** or **Home** > **Insert** > **Crosstab**. Designer displays the [Create Crosstab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522178583-Create-Crosstab-Dialog-Box#Query). You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to use to create the
   crosstab.

   ![Create Crosstab - Data](https://devnet.logianalytics.com/hc/article_attachments/9898532549911/crtcrstab_dt.gif)
4. In the **Display** screen, specify the fields to display in the crosstab.

   ![Create Crosstab - Display](https://devnet.logianalytics.com/hc/article_attachments/9898532577303/crtcrstab_dsply.gif)

   The Resources box lists all DBFields in the query resource from which the dataset the crosstab applies is created, and the formulas that are valid to these DBFields in the current catalog. You can create the crosstab using these fields. If the predefined formulas cannot meet your requirement, you can select **<New Formula...>** in the Formulas node to [create the formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735525453207-Creating-Formulas-in-a-Catalog) you want.

   * In the **Columns** and **Rows** boxes, add column/row fields to display on the column and row headers of the crosstab. To add a column/row field, select a DBField or formula in the Resources box and select the arrow button beside the target box, or drag it from the Resources box to the target box. If you want to display compound column/row groups in the crosstab, select **Add Compound Group**![](https://devnet.logianalytics.com/hc/article_attachments/9898532597911/btn_addparal.gif) at the right bottom corner of the Columns/Rows box to create them, then select each compound group and add the required fields to it.

     For the column/row fields, you can specify the following:

     + Double-click in the **Label** text box and type a name to label the corresponding column/row header (the Label text box is blank by default so the crosstab shows no label for the column/row header).
     + Double-click in the **Color** text box to specify background color of the field. However, to make the color take effect, you need to edit the Background property of the field to "Transparent" in the Report Inspector after you finish creating the crosstab.
     + Select a field and select ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/9898516023063/btn_sort1.gif) to change the sort manner of its values between Ascend, Descend, and No Sort.
     + Select a field and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the column/row fields on the column/row headers. You can also adjust the display order of the compound groups in the same way.
     + Select an unwanted field and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif) or drag it to the Resources box to remove the field from the crosstab. You can also delete any unwanted compound group in the same way.
   * In the **Summaries** box, add aggregate fields to create aggregations in the crosstab. To add an aggregate field, select a DBField or formula in the Resources box and select **Add**![Add Aggregation button](https://devnet.logianalytics.com/hc/article_attachments/9898516016791/btn_addsum.gif) or drag the field from the Resources box to the Summaries box. You can also select **<New Crosstab Formula...>** in the **Crosstab Formulas** node to [create crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735520960151-Using-Crosstab-Formulas) to use as the aggregate field. If you have created compound column and row groups in the crosstab, you can add aggregate fields for each combination of the compound groups by selecting a row/column group and a column/row group and then adding the required fields. An aggregate field can generate detail aggregations, aggregations for subtotals, and aggregations for grand totals for each combination of the column and row fields.

     For the aggregate fields, you can specify the following:

     + When you add a DBField or formula as the aggregate field, you need to double-click in the **Aggregate** text box to specify its [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function). If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box) dialog box.
     + Double-click in the **Label** text box and type a name to label the corresponding aggregations in the crosstab. The Label text box is blank by default so the crosstab shows no label for the aggregations.
     + Select a field and select **Comparison Function** to define [a comparison function](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs#Comparison) for it.
     + Select a field and select **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the aggregate fields.
     + Select an unwanted field and select **Remove**![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif) or drag it to the Resources box to remove the field from the crosstab.
5. In the **Filter** screen, filter the crosstab by adding conditions based on the fields it contains. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Crosstab - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898516163095/crtcrstab_fltr.gif)
6. In the **Layout** screen, specify the [layout](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs#Layout) of the crosstab.

   ![Create Crosstab - Layout](https://devnet.logianalytics.com/hc/article_attachments/9898516169751/crtcrstab_layout.gif)
7. In the **Style** screen, specify the style of the crosstab. If you have specified to insert the crosstab into a banded object, the crosstab [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports#Inherit) by default; to apply another style to the crosstab, clear **Inherit Style** and select the required style from the **Style** box.

   ![Create Crosstab - Style](https://devnet.logianalytics.com/hc/article_attachments/9898516175895/crtcrstab_sty.gif)
8. Select **Finish** to insert the crosstab.
9. If you have selected a panel in a banded object as the destination, after finishing the Create Crosstab dialog box, you need to select in the destination once again to insert the crosstab there.

Besides using wizard, you can also drag a blank crosstab to a page report that uses query resources.

1. From the **Components** panel, drag the **Crosstab** icon **![Crosstab button](https://devnet.logianalytics.com/hc/article_attachments/9898532400023/icon_crstb.gif)** in the **Grid** category to the destination in the page report which allows the insertion of a crosstab. Designer creates a blank crosstab.
2. From the dataset drop-down list in the **Data** panel, select a dataset from the ones you have created in the page report to use for the crosstab, or select **<Choose Data from...>** to [create a dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report#NewDataset) and apply it to the crosstab. Designer then displays the data fields available to the specified dataset in the panel.
3. [Drag the required fields](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs#Add) from the Data panel to create the column headers, row headers, and aggregations in the crosstab.

### Example: Creating a Compound Crosstab

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog box, select **Crosstab** and select **OK**. Designer displays the Crosstab Wizard dialog box.
4. In the **Data** screen, select the query **WorldWideSales** in Data Source 1 of the catalog.
5. In the **Display** screen, select **Add Compound Group**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898532597911/btn_addparal.gif) in the **Rows** box and Designer adds two compound row groups in the box.

   ![Add Compound Row Groups](https://devnet.logianalytics.com/hc/article_attachments/9898534749463/cmpnt_crstb_inst_cmpd1.gif)
6. Select **Row Compound Group**, drag the formula **year** and the field **Category** from the Resources box to the compound row group one by one, double-click in the **Label** text box of each field and type **Year** and **Category** to label the row headers.
7. Select **Row Compound Group 1** and add the field **Country** to it and edit its label to **Country**.

   ![Add Fields to Compound Row Groups](https://devnet.logianalytics.com/hc/article_attachments/9898518463383/cmpnt_crstb_inst_cmpd2.gif)
8. Select **Add Compound Group**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898532597911/btn_addparal.gif) in the **Columns** box, then add the formula **Quarter** to **Column Compound Group** and the field **Order ID** to **Column Compound Group 1**, specify their labels as **Quarter** and **Order ID**.
9. Select **Row Compound Group** in the Rows box and **Column Compound Group** in the Columns box, drag the field **Quantity** from the Resources box to the **Summaries** box as the aggregate field of the compound groups. Double-click in the **Aggregate** text box and select **Sum** from the drop-down list, then double-click in the **Label** text box and type **Quantity** to label the aggregations.

   ![Add Aggreagate Field to Compound Groups](https://devnet.logianalytics.com/hc/article_attachments/9898534762007/cmpnt_crstb_inst_cmpd3.gif)
10. Repeat the preceding step to add the following fields with the specified aggregate functions as the aggregate fields for the combinations of the following compound groups. Use the fields' display names as the labels.
    * Row Compound Group and Column Compound Group 1: **Price**, **Average**
    * Row Compound Group 1 and Column Compound Group: **Cost**, **Sum**
    * Row Compound Group 1 and Column Compound Group 1: **Unit Price**, **Average**
11. Switch to the **Filter** screen and specify the filter conditions.

    ![Specify Filter Conditions](https://devnet.logianalytics.com/hc/article_attachments/9898534776215/cmpnt_crstb_inst_cmpd4.gif)
12. Select **Finish** to create the crosstab.
13. In the Report Inspector, select **Label**, **Label 1**, **QUARTER**, **Label 4**, **Label 5**, **YEAR**, **Label 6**, **Label 7**, **CATEGORY**, **Label 10**, **Label 11**, **Label 12**, **QUANTITY**, **QUANTITY 1**, **QUANTITY 2**, **QUANTITY 3**, **QUANTITY 4**, and **QUANTITY 5**, specify the **Background** property to **Lightgray**.

    ![Set the Background Property for Objects](https://devnet.logianalytics.com/hc/article_attachments/9898534782999/cmpnt_crstb_inst_cmpd5.gif)
14. Repeat the preceding step to specify the Background property of Label 2, Label 3, Order ID, Label 15, Label 16, Label 17, PRICE, PRICE 1, PRICE 2, PRICE 3, PRICE 4, and PRICE 5 to **Pink**; specify the Background property of Label 8, Label 9, COUNTRY, Label 13, Label 14, COST, COST 1, COST 2, and COST 3 to **Orange**; specify the Background property of Label 18, Label 19, UNIT PRICE, UNIT PRICE 1, UNIT PRICE 2, and UNIT PRICE 3 to **Gray**.
15. Save the report.
16. Navigate to **View** > **Preview As** > **Page Report Result** to run the report in Page Report Studio. The crosstab contains four parts, showing different summary information for different combinations of row compound groups and column compound groups.

    ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/9898518534935/cmpnt_crstb_inst_cmpd6.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735498924183-Working-with-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs)
