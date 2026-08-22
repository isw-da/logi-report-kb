---
title: "Creating Page Reports"
id: 5741469017879
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741469017879-Creating-Page-Reports
updated_at: 2022-10-31T17:18:14Z
---

# Creating Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483215255-Page-Report-Studio-Window-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741482707223-Editing-Page-Reports-in-Page-Report-Studio)

# Creating Page Reports

In Page Report Studio, you can create page reports or add new report tabs to the current page report if the corresponding catalog contains predefined [business views](https://devnet.logianalytics.com/hc/en-us/articles/5741484450455-An-Introduction-to-Business-Views). This topic describes how you can create page reports and report tabs.

Before you can create page reports, you should make sure that the Pop-up Blocker is not enabled on your web browser.

You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/5741452341143-Logi-Report-Licenses#ServerLive) to use this feature. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

This topic contains the following sections:

* [Creating a Page Report](#Page)
* [Creating a Banded Report](#Banded)
* [Creating a Table Report](#Table)
* [Creating a Chart Report](#Chart)
* [Creating a Crosstab Report](#Crosstab)

## Creating a Page Report

1. Do any of the following:
   * In the [Server Start page](https://devnet.logianalytics.com/hc/en-us/articles/5741461387031-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Page Report** in the Create category. Server displays a page. Specify the folder in which you want to create the report, then the catalog that contains the business view you want. Select **OK**.
   * On the Server Console, go to the Resources page, then:
     + Select **New** > **Page Report** on the task bar. Server displays a page. Specify the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
     + Open a folder that contains catalogs, select the catalog for the new report from the **Catalog** button ![Catalog button](https://devnet.logianalytics.com/hc/article_attachments/9905655585943/btn_srv_catalog.gif) drop-down list, then select **New** > **Page Report** on the task bar.
   * In Page Report Studio, navigate to **Menu** > **File** > **New Page Report**.

   Server displays the [New Page Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741398131991-New-Page-Report-Dialog-Box-Properties) for you to create a page report with the first report tab in it.

   ![New Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/9905674749719/newrpt.gif)
2. Specify the title of the report tab in the **Report Title** text box.
3. In the **Choose Report Layout** box, select the layout with which you want to create the report tab.
4. Select **OK** to create the report tab.
   * If you selected **Blank** as the layout, Server creates a blank report tab. You can then use the Toolbox and the Resource View panels to [add objects](https://devnet.logianalytics.com/hc/en-us/articles/5741474851991-Adding-Objects-in-Page-Report) and view elements to the report tab.
   * If you have enabled the [template editor](https://devnet.logianalytics.com/hc/en-us/articles/9905923782039-Enabling-and-Accessing-Template-Editor-Logi-Report-Studio), you can select **Blank Template** to open Logi Report Studio.
   * If you select the layout as Banded, Table, Chart, or Crosstab, Server displays the corresponding report wizard. Specify the settings according to your requirements.

     **Tip:** In the report wizard, if there is only one business view in the current catalog, Server uses this business view to create the report tab by default, and hides the Data screen from the wizard. This is the same case when there is only one style available to apply to the report tab.

You can also use [URL command](https://devnet.logianalytics.com/hc/en-us/articles/5741464908183-Creating-Reports-via-URL#Page) to directly open the New Page Report dialog box to create a page report.

To create a report tab in an existing page report, in Page Report Studio, select **Menu** > **File** > **New Page Report Tab** or the Add button ![New Report Tab button](https://devnet.logianalytics.com/hc/article_attachments/9905577927831/btn_newobj.gif) on the toolbar. Server displays the [New Report Tab dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389145751-New-Report-Tab-Dialog-Box-Properties). Specify the title and layout of the report tab, then select **OK**.

The following shows in detail how to create a report tab from a particular layout.

## Creating a Banded Report

A banded object is a kind of component that can present grouped data and detailed data, and is composed of several banded panels with which you can easily organize data fields and other elements.

**To create a banded report:**

1. In the New Page Report dialog box, select **Banded** as the layout and select **OK**. Server displays the [Banded Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741416829079-Banded-Wizard-Properties).
2. In the Data screen, select the business view or dataset in the current catalog, on which you want to create the banded object.

   ![Banded Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/9905674786071/bdwzd_data.gif)
3. In the Display screen, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905630361111/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) from the Resources box to display as detail fields in the banded object.

   ![Banded Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/9905674805655/bdwzd_dsply.gif)
4. To edit the display order of the objects, select one and then select the **Move Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or **Move Down** button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif).
5. By default, Server uses the display names of the added objects to label the corresponding detail columns. To edit the label text for a detail column, select in the **Display Name** text box and type a new one. If you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/5741468400151-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** checkbox beside the text box.
6. In the Group screen, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) as the grouping criteria, then specify the sort direction of each group in the **Sort** column.
   To adjust the group levels, select a group and then select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif).

   ![Banded Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/9905674834967/bdwzd_grp.gif)
7. In the Summary screen, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/9905618017943/btn_bvaggrgtn.gif) to summarize data in the banded object: in the right box, specify the group to which you want to apply the aggregation, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)to adjust the order of the aggregations in the current group or move an aggregation to another group. By default, Server uses the display names of the added objects to label the corresponding summaries; to edit the label text for a summary, select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/5741468400151-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** checkbox beside the text box.

   ![Banded Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/9905674864279/bdwzd_sum.gif)
8. In the Dataset Filter screen, specify the filter you want to [apply to the dataset of the data component](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report#BV). If the selected business view or dataset contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741410399895-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify values to the parameters before it displays the Dataset Filter screen.

   ![Banded Wizard - Dataset Filter screen](https://devnet.logianalytics.com/hc/article_attachments/9905674888343/bdwzd_dtstfltr.gif)
9. In the Style screen, apply a style to the banded object.
10. Select **Finish** to create the report.

## Creating a Table Report

Tables give you great control over how to present data, including placing fields, grouping them, and sorting them.

**To create a table report:**

1. In the New Page Report dialog box, select the table type you want in the Choose Report Layout box, then select **OK**. Server displays the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741425746199-Table-Wizard-Properties).
   * **Table (Group Above)**  
      Select if you want to create a table with group information above the detail row.
   * **Table (Group Left)**  
      Select if you want to create a table with group information left to the detail row.
   * **Table (Group Left Above)**  
      Select if you want to create a table with group information left above the detail row.
   * **Summary Table**  
      Select if you want to create a table with only group and summary information. In a summary table, all the group names are in the group header of the innermost group.
2. In the Data screen, select the business view or dataset in the current catalog, on which you want to build the table.
3. In the Display screen, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905630361111/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) from the Resources box to display as detail fields in the table. To edit the display order of the objects, select one and select the Move Up button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or Move Down button ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif). By default, Server uses the display names of the added objects to label the corresponding detail columns; to edit the label text for a detail column, select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/5741468400151-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** checkbox beside the text box.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) For a summary table, Server does not display the detail fields that you specified on the Display screen, in the generated table by default.

   ![Table Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/9905674910103/tblwzd_dsply.gif)
4. In the Group screen, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) as the grouping criteria, then specify the sort direction of each group in the Sort column. To adjust the group levels, select a group and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif).

   ![Table Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/9905713390487/tblwzd_grp.gif)
5. In the Summary screen, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/9905618017943/btn_bvaggrgtn.gif) to summarize data in the table: in the right box, specify the group to which you want to apply the aggregation, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif)to adjust the order of the aggregations in the current group or move an aggregation to another group. For the Group Left table, you can use the Row and Column columns to control the position of the aggregations in the table. By default, Server uses the display names of the added objects to label the corresponding summaries. If the table is not Group Left type, you can edit the label text for a summary: select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/5741468400151-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** checkbox beside the text box.

   ![Table Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/9905713418519/tblwzd_sum.gif)
6. In the Dataset Filter screen, specify the filter you want to [apply to the dataset of the data component](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report#BV). If the selected business view or dataset contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741410399895-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify values to the parameters before it displays the Dataset Filter screen.
7. In the Style screen, apply a style to the table.
8. Select **Finish** to create the report.

## Creating a Chart Report

A chart organizes and graphically presents data in a way that makes you easily see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form.

For more information, select the following links to view topics in the *Logi Report Designer Guide*:

* Chart Types
* How Data Is Represented in a Chart
* Chart Elements

**To create a chart report in Page Report Studio:**

1. In the New Page Report dialog box, select **Chart** as the layout and select **OK**. Server displays the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741402177047-Chart-Wizard-Properties).

1. In the Data screen, select the business view or dataset in the current catalog, on which you want to build the chart.
2. In the Type screen, specify the chart type.

   ![Chart Wizard - Type screen](https://devnet.logianalytics.com/hc/article_attachments/9905713442711/chtwzd_type.gif)

   A default chart type exists in the Chart Type Groups box. To replace it with another one, select a chart type from the **Chart Type** box. Server displays the thumbnails of the subtypes in this type, in the **Subtype** box. Select the required subtype to replace the default chart type.

   If you want to create a combo chart, select **<Add Combo Type>** of **Primary Axis** or **Secondary Axis** in the Chart Type Groups box. Server adds an additional subtype. To replace the additional subtype, select it, then specify the required type and subtype respectively in the Chart Type and Sub Type boxes.

   To add more subtypes, repeat the procedures. To remove a subtype, select it and then select the **Remove** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif).
3. In the Display screen, select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) in the Resources box and add it to the **Category** or **Series** box, the data of which Server displays on the corresponding axis. Select a subtype in the Show Values box, then add an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/9905618017943/btn_bvaggrgtn.gif) or an [additional value](#AValue)![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/9905620414103/btn_wbrpt_adtnl.gif) as the data of the subtype. You can add more than one aggregation object or additional value to a subtype. Each added subtype shall have at least one aggregation object or additional value.
   For a subtype that is a bubble chart, you can add two or three aggregation objects
   to the subtype.

   ![Chart Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/9905713463959/chtwzd_dsply.gif)

   **To add an additional value to a subtype:**

   1. Select the subtype in the **Show Values** box.
   2. In the Resources box, expand **Additional Values**, then select **Constant Value**/**Average Value**.
   3. Select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif) beside the Show Values box. Server displays the [Edit Additional Value dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741417094423-Edit-Additional-Values-Dialog-Box-Properties).
   4. In the **Name** text box, specify the display name for the constant/average value.
   5. Type the constant value with numeric type in the **Value** text box, or select a field based on which Server calculates the average value, from the **Based On** drop-down list.
   6. Select **OK**. Server adds the defined constant/average value to the subtype.

      If you want to further modify a constant/average value, select the value in the **Show Values** box, then select the **Edit** button ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9905655522327/btn_pgrpt_edit.gif). Server displays the Edit Additional Value dialog box for you to edit the value.
4. If you want to customize the sort order and define the Select N condition for values on the category/series axis of the chart, select **Order/Select N** in the Display screen, then define the condition in the [Order/Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741411534871-Order-Select-N-Dialog-Box-Properties):

   ![Order/Select N dialog](https://devnet.logianalytics.com/hc/article_attachments/9905713483159/ordrslctn.gif)

   1. In the Order box, specify in which order you want to sort values on the category/series axis.
   2. In the Select N box, specify the Select N condition to All, Top, or Bottom. If you selected **All**, Server displays all category/series values in the chart; if you selected **Top** or **Bottom**, Server enables the text box next to it and you can specify an integer here, which means that Server displays the first or last N category/series values in the chart.
   3. Select **Based On** and specify values for the two drop-down lists that follow.

      If you do not select **Based On**, the order of the first or last N category/series values bases on what you specified in the Order box; if you select it, the order bases on values of a field on the value axis and the sort direction you specified in the drop-down lists next to **Based On**.
   4. If you selected Top or Bottom from the Select N drop-down list, you can select **Other** and then type a string in the next text box, so that the category/series values beyond the first or last N range will merge into the group with the name as that string.
   5. Select **OK** to accept the settings.
5. In the Dataset Filter screen, specify the filter you want to [apply to the dataset of the data component](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report#BV). If the selected business view or dataset contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741410399895-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify values to the parameters before it displays the Dataset Filter screen.
6. In the Style screen, apply a style to the chart.
7. Select **Finish** to create the report.

## Creating a Crosstab Report

A crosstab summarizes data and presents the summaries in a compact row and column format. Logi Report also supports a unique compound crosstab that enables you to put multiple compound row groups and column groups together and define summaries for every combination of a compound row group and column group. This makes far more sophisticated crosstab analysis possible.

1. In the New Page Report dialog box, select **Crosstab** as the layout and select **OK**. Server displays the [Crosstab Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741424076567-Crosstab-Wizard-Properties).
2. In the Data screen, select the business view or dataset in the current catalog, on which you want to build the crosstab.
3. In the Display screen, specify the fields you want to display in the crosstab.

   ![Crosstab Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/9905675047959/crstbwzd_dsply.gif)

   From the Resources box, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/9905617901719/btn_bvgrp.gif) to the Columns/Rows box to display on the column/row headers of the crosstab. If you want to display compound column/row groups in the crosstab, select the **Add Compound Group** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905713527831/btn_pgrpt_addparal.gif) under the bottom right corner of the Columns/Rows box to create the groups, then select each group and add the group objects to it. You can specify a sort manner on each group object in the **Sort** column. Add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/9905618017943/btn_bvaggrgtn.gif) from the Resources box to the **Summaries** box to create aggregations in the crosstab. If you have created compound column/row groups in the crosstab, you can create aggregations for each combination of the compound groups by selecting a compound column group and a compound row group and then adding the required aggregation objects.

   For each column/row/summary field, you can select in the **Display Name** text box and type a name to label the corresponding column header/row header/summary, or select the **Auto Map Field Name** checkbox beside the text box if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/5741468400151-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field (when the text box is blank and you did not select the checkbox, Server does not create the label).

   If you want to remove a group object, an aggregation object, or a compound column/row group, select it and then select the **Remove** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif). To adjust the order of them, select one and then select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9905613125783/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9905575169431/btn_mvdown.gif).
4. In the Dataset Filter screen, specify the filter you want to [apply to the dataset of the data component](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report#BV). If the selected business view or dataset contains parameters, Server displays the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741410399895-Enter-Parameter-Values-Dialog-Box-Properties) for you to specify values to the parameters before it displays the Dataset Filter screen.
5. In the Style screen, apply a style to the crosstab.
6. Select **Finish** to create the report.

**Tip:** When you create a crosstab with a wizard, by default, Server does not create labels for its columns, rows, or summaries (the **Display Name** columns in the Columns, Rows, and Summaries boxes of the wizard are blank by default). You can make Page Report Studio automatically provide the display names of the added objects in the wizard, by setting the [profile properties](https://devnet.logianalytics.com/hc/en-us/articles/7985371543191-Customize-Profile-Dialog-Box-Properties#Crosstab)**Add Labels for Crosstab Rows and Columns** and **Add Labels for Crosstab Summaries**. You can also customize the profile property **Display Crosstab Summaries Vertically** to make the summaries in crosstabs display horizontally in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483215255-Page-Report-Studio-Window-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741482707223-Editing-Page-Reports-in-Page-Report-Studio)
