---
title: "Creating Page Reports"
id: 1500009748862
section: "Page Report Studio Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748862-Creating-Page-Reports
updated_at: 2021-07-24T00:47:55Z
---

# Creating Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749082-Page-Report-Studio-Window-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777521-Editing-Page-Reports-in-Page-Report-Studio)

# Creating Page Reports

In Page Report Studio, you can create page reports or add new report tabs to the current page report if the corresponding catalog contains predefined [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009749982-An-Introduction-to-Business-Views). This topic describes how you can create page reports and report tabs.

Before you can create page reports, you should make sure that the Pop-up Blocker is not enabled on your web browser.

You need a [Logi Report Live license for Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009776661-Logi-Report-Licenses#ServerLive) to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

This topic contains the following sections:

* [Creating a Page Report](#Page)
* [Creating a Banded Report](#Banded)
* [Creating a Table Report](#Table)
* [Creating a Chart Report](#Chart)
* [Creating a Crosstab Report](#Crosstab)

## Creating a Page Report

1. Do any of the following:
   * In the [Logi Report Server Start page](https://devnet.logianalytics.com/hc/en-us/articles/1500009777061-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Page Report** in the Create category. Server displays a page. Specify the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
   * In the Server Console, go to the Resources page, then:
     + Select **New** > **Page Report** on the task bar. Server displays a page. Specify the folder in which to create the report, then the catalog that contains the required business view. Select **OK**.
     + Open a folder that contains catalogs, select the catalog for the new report from the Catalog drop-down list, then select **New** > **Page Report** on the task bar.
   * In Page Report Studio, select **Menu** > **File** > **New Page Report**.

   Server displays the [New Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009772781-New-Page-Report-Dialog-Box-Properties) dialog box for you to create a page report with the first report tab in it.

   ![New Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880275863/newrpt.gif)
2. Specify the title of the report tab in the **Report Title** text box.
3. In the **Choose Report Layout** box, select the layout with which you want to create the report tab.
4. Select **OK** to create the report tab.
   * If you selected **Blank** as the layout, Server creates a blank report tab. You can then use the Toolbox and the Resource View panels to [add objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009748902-Adding-Objects-in-Page-Report) and view elements to the report tab.
   * If you select the layout as Banded, Table, Chart, or Crosstab, Server displays the corresponding report wizard. Specify the settings according to your requirements.

     **Tip:** In the report wizard, if there is only one business view in the current catalog, Server uses this business view to create the report tab by default, and hides the Data screen from the wizard. This is the same case when there is only one style available to apply to the report tab.

You can also use [URL command](https://devnet.logianalytics.com/hc/en-us/articles/1500009750322-Creating-Reports-via-URL#Page) to directly open the New Page Report dialog box to create a page report.

To create a report tab in an existing page report, in Page Report Studio, select **Menu** > **File** > **New Page Report Tab** or the button ![New Report Tab button](https://devnet.logianalytics.com/hc/article_attachments/4404885307031/btn_newobj.gif) on the toolbar. Server displays the [New Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009744822-New-Report-Tab-Dialog-Box-Properties) dialog box. Specify the title and layout of the report tab, then select **OK**.

The following shows in detail how to create a report tab from a particular layout.

## Creating a Banded Report

A banded object is a kind of component that can present grouped data and detailed data, and is composed of several banded panels with which you can easily organize data fields and other elements.

**To create a banded report:**

1. In the New Page Report dialog box, select **Banded** as the layout and select **OK**. Server displays the [Banded Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009744062-Banded-Wizard-Properties).
2. In the Data screen, select the business view in the current catalog, on which to create the banded object.

   ![Banded Wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404880276503/bdwzd_data.gif)
3. In the Display screen, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) from the Resources box to display as detail fields in the banded object.

   ![Banded Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404880276759/bdwzd_dsply.gif)
4. To edit the display order of the objects, select one and then select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
5. By default, Server uses the display names of the added objects to label the corresponding detail columns. To edit the label text for a detail column, select in the **Display Name** text box and type a new one. If you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.
6. In the Group screen, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) as the grouping criteria, then specify the sort direction of each group in the **Sort** column.
   To adjust the group levels, select a group and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).

   ![Banded Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404885402519/bdwzd_grp.gif)
7. In the Summary screen, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) to summarize data in the banded object as follows: in the right box, specify the group to which you want to apply the aggregation, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)to adjust the order of the aggregations in the current group or move an aggregation to another group. By default, Server uses the display names of the added objects to label the corresponding summaries; to edit the label text for a summary, select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.

   ![Banded Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404880277399/bdwzd_sum.gif)
8. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009777561-Applying-Filters-to-Page-Report#BV). If the selected business view contains parameters, Server displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify values to the parameters before it displays the Query Filter screen.

   ![Banded Wizard - Query Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404880277911/bdwzd_qryfltr.gif)
9. In the Style screen, apply a style to the banded object.
10. Select **Finish** to create the report.

## Creating a Table Report

Tables give you great control over how to present data, including placing fields, grouping them, and sorting them.

**To create a table report:**

1. In the New Page Report dialog box, select the desired table type in the Choose Report Layout box, then select **OK**. Server displays the [Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009773181-Table-Wizard-Properties).
   * **Table (Group Above)**  
      Select if you want to create a table with group information above the detail row.
   * **Table (Group Left)**  
      Select if you want to create a table with group information left to the detail row.
   * **Table (Group Left Above)**  
      Select if you want to create a table with group information left above the detail row.
   * **Summary Table**  
      Select if you want to create a table with only group and summary information. In a summary table, all the group names are in the group header of the innermost group.
2. In the Data screen, select the business view in the current catalog, on which you want to build the table.
3. In the Display screen, add detail objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404885323799/btn_bvdtl.gif) or group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) from the Resources box to display as detail fields in the table. To edit the display order of the objects, select one and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif). By default, Server uses the display names of the added objects to label the corresponding detail columns; to edit the label text for a detail column, select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)For a summary table, Server does not display the detail fields that you specified on the Display screen, in the generated table by default.

   ![Table Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404880278167/tblwzd_dsply.gif)
4. In the Group screen, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) as the grouping criteria, then specify the sort direction of each group in the Sort column. To adjust the group levels, select a group and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).

   ![Table Wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404880278679/tblwzd_grp.gif)
5. In the Summary screen, add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) to summarize data in the table as follows: in the right box, specify the group to which you want to apply the aggregation, then select an aggregation object in the Resources box and add it to the right box. You can add several aggregations for any group level. You can select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)to adjust the order of the aggregations in the current group or move an aggregation to another group. For the Group Left table, you can use the Row and Column columns to control the position of the aggregations in the table. By default, Server uses the display names of the added objects to label the corresponding summaries. If the table is not Group Left type, you can edit the label text for a summary: select in the Display Name text box and type a new one; if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the object, select the **Auto Map Field Name** check box beside the text box.

   ![Table Wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404880279191/tblwzd_sum.gif)
6. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009777561-Applying-Filters-to-Page-Report#BV). If the selected business view contains parameters, Server displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify values to the parameters before it displays the Query Filter screen.
7. In the Style screen, apply a style to the table.
8. Select **Finish** to create the report.

## Creating a Chart Report

A chart organizes and graphically presents data in a way that makes you easily see comparisons, trends, and patterns in data. It represents the report data in a visually straightforward form.

For more information, select the following links to view topics in the *Logi Report Designer Guide*:

* Chart Types
* How Data Is Represented in a Chart
* Chart Elements

**To create a chart report in Page Report Studio:**

1. In the New Page Report dialog box, select **Chart** as the layout and select **OK**. Server displays the [Chart Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009772001-Chart-Wizard-Properties).

1. In the Data screen, select the business view in the current catalog, on which you want to build the chart.
2. In the Type screen, specify the chart type.

   ![Chart Wizard - Type screen](https://devnet.logianalytics.com/hc/article_attachments/4404880279575/chtwzd_type.gif)

   A default chart type exists in the Chart Type Groups box. To replace it with another one, select a chart type from the **Chart Type** box. Server displays the thumbnails of the subtypes in this type, in the **Subtype** box. Select the required subtype to replace the default chart type.

   If you want to create a combo chart, select **<Add Combo Type>** of **Primary Axis** or **Secondary Axis** in the Chart Type Groups box. Server adds an additional subtype. To replace the additional subtype, select it, then specify the required type and subtype respectively in the Chart Type and Sub Type boxes.

   To add more subtypes, repeat the procedures. To remove a subtype, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif).
3. In the Display screen, select a group object ![](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) in the Resources box and add it to the Category or **Series** box, the data of which Server displays on the corresponding axis. Select a subtype in the Show Values box, then add an aggregation object ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) or an [additional value](#AValue)![Additional Value](https://devnet.logianalytics.com/hc/article_attachments/4404880175511/btn_wbrpt_adtnl.gif) as the data of the subtype. You can add more than one aggregation object or additional value to a subtype. Each added subtype shall have at least one aggregation object or additional value.
   For a subtype that is a bubble chart, you can add two or three aggregation objects
   to the subtype.

   ![Chart Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404885403927/chtwzd_dsply.gif)

   **To add an additional value to a subtype:**

   1. Select the subtype in the **Show Values** box.
   2. In the Resources box, expand the **Additional Values** node, then select **Constant Value**/**Average Value**.
   3. Select ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/4404880170519/btn_additem.gif) beside the Show Values box. Server displays the [Edit Additional Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009772081-Edit-Additional-Values-Dialog-Box-Properties) dialog box.
   4. In the **Name** text box, specify the display name for the constant/average value.
   5. Type the constant value with numeric type in the **Value** text box, or select a field based on which Server calculates the average value, from the **Based On** drop-down list.
   6. Select **OK**. Server adds the defined constant/average value to the subtype.

      If you want to further modify a constant/average value, select the value in the **Show Values** box, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404880196759/btn_pgrpt_edit.gif). Server displays the Edit Additional Value dialog box for you to edit the value.
4. If you want to customize the sort order and define Select N condition for values on the category/series axis of the chart, select the **Order/Select N** button below the Category/Series box in the Display screen, then define the condition in the [Order/Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009772821-Order-Select-N-Dialog-Box-Properties) dialog box as follows:

   ![Order/Select N dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885404311/ordrslctn.gif)

   1. In the Order box, specify in which order you want to sort values on the category/series axis.
   2. In the Select N box, specify the Select N condition to All, Top, or Bottom. If you selected **All**, Server displays all category/series values in the chart; if you selected Top or Bottom, Server enables the text box next to it and you can specify an integer here, which means that Server displays the first or last N category/series values in the chart.
   3. Select the **Based On** check box and specify values for the two drop-down lists that follow.

      If you do not select **Based On**, the order of the first or last N category/series values bases on what you specified in the Order box; if you select it, the order bases on values of a field on the value axis and the sort direction you specified in the drop-down lists next to the **Based On** check box.
   4. If you selected Top or Bottom from the Select N drop-down list, you can select the **Other** check box and then type a string in the next text box, so that the category/series values beyond the first or last N range will merge into the group with the name as that string.
   5. Select **OK** to accept the settings.
5. In the Query Filter screen, specify the filter that you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009777561-Applying-Filters-to-Page-Report#BV). If the selected business view contains parameters, Server displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify values to the parameters before it displays the Query Filter screen.
6. In the Style screen, apply a style to the chart.
7. Select **Finish** to create the report.

## Creating a Crosstab Report

A crosstab summarizes data and presents the summaries in a compact row and column format. Logi Report also supports a unique compound crosstab that enables you to put multiple compound row groups and column groups together and define summaries for every combination of a compound row group and column group. This makes far more sophisticated crosstab analysis possible.

1. In the New Page Report dialog box, select **Crosstab** as the layout and select **OK**. Server displays the [Crosstab Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009744202-Crosstab-Wizard-Properties).
2. In the Data screen, select the business view in the current catalog, on which you want to build the crosstab.
3. In the Display screen, specify the fields you want to display in the crosstab.

   ![Crosstab Wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404885404823/crstbwzd_dsply.gif)

   From the Resources box, add group objects ![Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151447/btn_bvgrp.gif) to the Columns/Rows box to display on the column/row headers of the crosstab. If you want to display compound column/row groups in the crosstab, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404885405079/btn_pgrpt_addparal.gif) under the bottom right corner of the Columns/Rows box to create the groups, then select each group and add the group objects to it. You can specify a sort manner on each group object in the **Sort** column. Add aggregation objects ![Aggregation Object](https://devnet.logianalytics.com/hc/article_attachments/4404880151959/btn_bvaggrgtn.gif) from the Resources box to the **Summaries** box to create aggregations in the crosstab. If you have created compound column/row groups in the crosstab, you can create aggregations for each combination of the compound groups by selecting a compound column group and a compound row group and then adding the required aggregation objects.

   For each column/row/summary field, you can select in the **Display Name** text box and type a name to label the corresponding column header/row header/summary, or select the **Auto Map Field Name** check box beside the text box if you want to automatically map the label text to the [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) of the field (when the text box is blank and you did not select the check box, Server does not create the label).

   If you want to remove a group object, an aggregation object, or a compound column/row group, select it and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif). To adjust the order of them, select one and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
4. In the Query Filter screen, specify the filter you want to [apply to the business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009777561-Applying-Filters-to-Page-Report#BV). If the selected business view contains parameters, Server displays the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009772161-Enter-Parameter-Values-Dialog-Box-Properties) dialog box for you to specify values to the parameters before it displays the Query Filter screen.
5. In the Style screen, apply a style to the crosstab.
6. Select **Finish** to create the report.

**Tip:** When you create a crosstab with wizard, by default there will be no labels for its columns, rows, and summaries (the **Display Name** columns in the Columns, Rows, and Summaries boxes of the wizard are blank by default). You can make Page Report Studio automatically provide the display names of the added objects in the wizard by setting the [profile options](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#Crosstab)**Add Labels for Crosstab Rows and Columns** and **Add Labels for Crosstab Summaries**. You can also customize the profile option **Display Crosstab Summaries Vertically** to make the summaries in crosstabs display horizontally in Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749082-Page-Report-Studio-Window-Elements)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777521-Editing-Page-Reports-in-Page-Report-Studio)
