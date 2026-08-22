---
title: "Creating Page Reports"
id: 1500009750341
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750341-Creating-Page-Reports
updated_at: 2021-07-25T07:18:54Z
---

# Creating Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750561-Page-Report-Studio-Window-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750361-Editing-Page-Reports-in-Page-Report-Studio)

# Creating Page Reports

In Page Report Studio, you can create page reports or add new report tabs to the current page report if the corresponding catalog contains predefined [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009751441-An-Introduction-to-Business-Views). Before you can create page reports, you should make sure that the Pop-up Blocker is not enabled on your web browser.

A [Logi Report Live license for Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009749561-Logi-Report-licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

Select the following links to view the topics:

* [Creating a Banded Report](#Banded)
* [Creating a Table Report](#Table)
* [Creating a Chart Report](#Chart)
* [Creating a Crosstab Report](#Crosstab)

**To create a page report:**

1. Do any of the following:
   * In the [Logi Report Server Start page](https://devnet.logianalytics.com/hc/en-us/articles/1500009749881-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Page Report** in the Create category. In the displayed page, specify the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
   * In the Logi Report Server console, go to the Resources page, then:
     + Select **New** > **Page Report** on the task bar. In the displayed page, specify the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
     + Open a folder that contains catalogs, select the catalog for the new report from the Catalog drop-down list, then select **New** > **Page Report** on the task bar.
   * In Page Report Studio, select **Menu** > **File** > **New Page Report**.

   Report Server displays the [New Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009719662-New-Page-Report) dialog box for you to create a page report with the first report tab in it.

   ![New Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936790807/newrpt.gif)
2. Specify the title of the report tab as required in the Report Title text box.
3. In the Choose Report Layout box, select the required layout with which you want to create the report tab.
4. Select **OK** to create the report tab.
   * If Blank is selected as the layout, a report tab which is blank will be created. You can then use the Toolbox and the Resource View panels to [add objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009723322-Adding-Report-Objects) and view elements to the report tab.
   * If you select the layout as Banded, Table, Chart, or Crosstab, the corresponding report wizard will then be displayed. Specify the settings according to your requirements.

     **Tip:** In the report wizard, if there is only one business view in the current catalog, this business view will be used to create the report tab by default, and the Data screen will be hidden from the wizard. This is the same case when there is only one style available to be applied to the report tab.

You can also use [URL command](https://devnet.logianalytics.com/hc/en-us/articles/1500009751681-Creating-Reports#Page) to directly open the New Page Report dialog box to create a page report.

To create a report tab in an existing page report, in Page Report Studio, select **Menu** > **File** > **New Page Report Tab** or the button ![New Report Tab button](https://devnet.logianalytics.com/hc/article_attachments/4404936714519/btn_newobj.gif) on the toolbar. In the [New Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009719682-New-Report-Tab) dialog box, specify the title and layout of the report tab, then select **OK**.

The following shows in detail how to create a report tab from a particular layout.

## Creating a Banded Report

A banded object is a kind of component that can present grouped data and detailed data, and is composed of several banded panels with which you can easily organize data fields and other elements.

**To create a banded report:**

1. In the New Page Report dialog box, select  **Banded**  as the layout and select **OK** to display the [Banded Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009745241-Banded-Wizard).
2. In the Data screen, select the business view in the current catalog, on which to create the banded object.

   ![Banded Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404942498711/bdwzd_data.gif)
3. In the Display screen, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources box to be displayed as detail fields in the banded object. To edit the display order of the objects, select one and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif). By default the display names of the added objects will be used to label the corresponding detail columns; to edit the label text for a detail column, select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.

   ![Banded Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404936791063/bdwzd_dsply.gif)
4. In the Group screen, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) as the grouping criteria, then specify the sort direction of each group in the Sort column.
   To adjust the group levels, select a group and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif).

   ![Banded Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404942498967/bdwzd_grp.gif)
5. In the Summary screen, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) to summarize data in the banded object as follows: in the right box, specify the group to which the aggregation will be applied, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)to adjust the order of the aggregations in the current group or move an aggregation to another group. By default the display names of the added objects will be used to label the corresponding summaries; to edit the label text for a summary, select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.

   ![Banded Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404936791319/bdwzd_sum.gif)
6. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009750441-Applying-Filters#BV). If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009719302-Enter-Parameter-Values) dialog box to specify values to the parameters before Report Server displays the Query Filter screen.

   ![Banded Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404942499223/bdwzd_qryfltr.gif)
7. In the Style screen, apply a style to the banded object.
8. Select **Finish** to create the report.

## Creating a Table Report

Tables give you great control over how to present data, including placing fields, grouping them, and sorting them.

**To create a table report:**

1. In the New Page Report dialog box, select the desired table type in the Choose Report Layout box, then select **OK** to display the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009719962-Table-Wizard).
   * **Table (Group Above)**  
      Creates a table with group information above the detail row.
   * **Table (Group Left)**  
      Creates a table with group information left to the detail row.
   * **Table (Group Left Above)**  
      Creates a table with group information left above the detail row.
   * **Summary Table**  
      Creates a table with only group and summary information. In a summary table, all the group names will be put in the group header of the innermost group.
2. In the Data screen, select the business view in the current catalog, on which the table will be built.
3. In the Display screen, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936727575/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) from the Resources box to be displayed as detail fields in the table. To edit the display order of the objects, select one and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif). By default the display names of the added objects will be used to label the corresponding detail columns; to edit the label text for a detail column, select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box. Note that for a summary table, the detail fields specified on the Display screen will not be shown in the generated table by default.

   ![Table Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404936791575/tblwzd_dsply.gif)
4. In the Group screen, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) as the grouping criteria, then specify the sort direction of each group in the Sort column. To adjust the group levels, select a group and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif).

   ![Table Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404936791831/tblwzd_grp.gif)
5. In the Summary screen, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) to summarize data in the table as follows: in the right box, specify the group to which the aggregation will be applied, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif)to adjust the order of the aggregations in the current group or move an aggregation to another group. For the Group Left table, you can use the Row and Column columns to control the position of the aggregations in the table. By default the display names of the added objects will be used to label the corresponding summaries. If the table is not Group Left type, you can edit the label text for a summary: select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.

   ![Table Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404936792087/tblwzd_sum.gif)
6. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009750441-Applying-Filters#BV). If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009719302-Enter-Parameter-Values) dialog box to specify values to the parameters before Report Server displays the Query Filter screen.
7. In the Style screen, apply a style to the table.
8. Select **Finish** to create the report.

## Creating a Chart Report

A chart organizes and graphically presents data in a way that makes it easy for end users to see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form. You can refer to the following topics in the *Logi Report Designer Guide* for more information about the chart types Logi Report supports, how charts present data, and the elements that compose a chart.

* Chart Types
* How Data Is Represented in a Chart
* Chart Elements

**To create a chart report in Page Report Studio:**

1. In the New Page Report dialog box, select **Chart** as the layout and select **OK** to display the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009745261-Chart-Wizard).

1. In the Data screen, select the business view in the current catalog, on which the chart will be built.
2. In the Type screen, specify the chart type as required.

   ![Chart Wizard - Type screen](https://devnet.logianalytics.com/hc/article_attachments/4404936792343/chtwzd_type.gif)

   A default chart type exists in the Chart Type Groups box. To replace it with another one, select a chart type from the Chart Type box. The thumbnails of the subtypes in this type will then be displayed in the Subtype box. Select the required subtype to replace the default chart type.

   If you want to create a combo chart, select **<Add Combo Type>** of Primary Axis or Secondary Axis in the Chart Type Groups box, and an additional subtype will be added. To replace the additional subtype, select it, then specify the required type and subtype respectively in the Chart Type and Sub Type boxes.

   To add more subtypes, repeat the procedures. To remove a subtype, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).
3. In the Display screen, select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) in the Resources box and add it to the Category or Series box, the data of which will be displayed on the corresponding axis. Select a subtype in the Show Values box, then add an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) or an [additional value](#AValue)![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404936740759/btn_wbrpt_adtnl.gif) as the data of the subtype. You can add more than one aggregation object or additional value to a subtype. Each added subtype shall have at least one aggregation object or additional value.
   For a subtype that is a bubble chart, you can add two or three aggregation objects
   to the subtype.

   ![Chart Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404936792855/chtwzd_dsply.gif)

   **To add an additional value to a subtype:**

   1. Select the subtype in the Show Values box.
   2. In the Resources box, expand the **Additional Values** node, then select **Constant Value**/**Average Value**.
   3. Select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404936738839/btn_additem.gif) beside the Show Values box. Report Server displays the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009719222-Edit-Additional-Values) dialog box.
   4. In the Name text box, specify the display name for the constant/average value.
   5. Type the constant value with numeric type in the Value text box, or select a field based on which the average value will be calculated from the Based On drop-down list.
   6. Select **OK**, and the defined constant/average value will be added to the subtype.

      If you want to further modify a constant/average value, select the value in the Show Values box, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936751127/btn_pgrpt_edit.gif). In the Edit Additional Value dialog box, edit the value as required.
4. If you want to customize the sort order and define Select N condition for values displayed on the category/series axis of the chart, select the **Order/Select N** button below the Category/Series box in the Display screen, then define the condition in the [Order/Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009746101-Order-Select-N) dialog box.

   ![Order/Select N dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936793111/ordrslctn.gif)

   1. In the Order box of the Order/Select N dialog box, specify in which order values on the category/series axis will be sorted.
   2. In the Select N box, specify the Select N condition to All, Top or Bottom. If All is selected, all category/series values will be shown in the chart; if Top or Bottom is selected, the text box next to it will be enabled and you can specify an integer here, which means that the first or last N category/series values will be shown on the chart.
   3. Select the **Based On** check box and specify values for the two drop-down lists that follow according to your requirement.

      If Based On is unselected, the order of the first or last N category/series values will be based on what you specify in the Order box of the dialog box; if you select it, the order will be based values of a field on the value axis and the sort direction you specify in the drop-down lists next to the Based On check box.
   4. If you have selected Top or Bottom from the Select N drop-down list, you can select the **Other** check box and the type a string in the next text box, so that the category/series values beyond the first or last N range will be merged into the group with the name as that string.
   5. Select **OK** to accept the settings.
5. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009750441-Applying-Filters#BV). If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009719302-Enter-Parameter-Values) dialog box to specify values to the parameters before Report Server displays the Query Filter screen.
6. In the Style screen, apply a style to the chart.
7. Select **Finish** to create the report.

## Creating a Crosstab Report

A crosstab summarizes data and presents the summaries in a compact row and column format. Logi Report also supports a unique compound crosstab that allows you to put multiple compound row groups and column groups together and define summaries for every combination of a compound row group and column group. This makes far more sophisticated crosstab analysis possible.

1. In the New Page Report dialog box, select **Crosstab**  as the layout and select **OK** to display the [Crosstab Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009745321-Crosstab-Wizard).
2. In the Data screen, select the business view in the current catalog, on which the crosstab will be built.
3. In the Display screen, specify the fields you want to display in the crosstab.

   ![Crosstab Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404936793367/crstbwzd_dsply.gif)

   From the Resources box, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404936726423/btn_bvgrp.gif) to the Columns/Rows box to display on the column/row headers of the crosstab. If you want to display compound column/row groups in the crosstab, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936793623/btn_pgrpt_addparal.gif) under the bottom right corner of the Columns/Rows box to create the groups, then select each group and add the required group objects to it. You can specify a sort manner on each group object in the Sort column. Add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404942456215/btn_bvaggrgtn.gif) from the Resources box to the Summaries box to create aggregations in the crosstab. If you have created compound column/row groups in the crosstab, you can create aggregations for each combination of the compound groups by selecting a compound column group and a compound row group and then adding the required aggregation objects.

   For each column/row/summary field, you can select in the Display Name text box and type a name to label the corresponding column header/row header/summary, or select the **Auto Map Field Name** check box beside the text box if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field (when the text box is blank and the check box is not selected, no label will be created).

   If you want to remove a group object, an aggregation object, or a compound column/row group, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif). To adjust the order of them, select one and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif).
4. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009750441-Applying-Filters#BV). If the selected business view contains parameters, you would be prompted with the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009719302-Enter-Parameter-Values) dialog box to specify values to the parameters before Report Server displays the Query Filter screen.
5. In the Style screen, apply a style to the crosstab.
6. Select **Finish** to create the report.

**Tip:** When you create a crosstab with wizard, by default there will be no labels generated for its columns, rows and summaries (the Display Name columns in the Columns, Rows and Summaries boxes of the wizard are blank by default). You can make Page Report Studio automatically provide the display names of the added objects in the wizard by setting the [profile options](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#Crosstab) Add Labels for Crosstab Rows and Columns and Add Labels for Crosstab Summaries. You can also customize the profile option Display Crosstab Summaries Vertically to make the summaries in crosstabs displayed horizontally in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750561-Page-Report-Studio-Window-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750361-Editing-Page-Reports-in-Page-Report-Studio)
