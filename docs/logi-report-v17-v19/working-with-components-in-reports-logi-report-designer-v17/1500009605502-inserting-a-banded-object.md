---
title: "Inserting a Banded Object"
id: 1500009605502
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009605502-Inserting-a-Banded-Object
updated_at: 2021-07-24T16:05:24Z
---

# Inserting a Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628361-Banded-Objects) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628441-Modifying-Banded-Objects)

# Inserting a Banded Object

With the banded object wizard, it is easy to create banded objects in a report, however the wizard varies with the data resource type used for the banded object: business view or query resource.

A web report can only use business views. For a page report it can be created either based on query resources or business views, which is determined at the time when  [the page report is created](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page)  by the Create Using Business View option. Once defined, all the data components in the page report can only be created on the specified data resource type.

A banded object can be inserted in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009605422-Working-with-Components-in-Reports#Relationship). When a banded object is inserted into another banded object in a page report, you can [set up data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500009628401-Setting-Up-Data-Container-Links-in-Banded-Objects) between the banded object and its parent.

This topic shows creating banded objects using different data resources in detail:

* [Creating a Banded Object Based on a Business View](#BV)
* [Creating a Banded Object Based on a Query Resource](#Query)

## Creating a Banded Object Based on a Business View

1. Position the mouse pointer at the destination where you want to insert the banded object.
2. Select **Insert** > **Banded Object** or **Home** > **Insert** > **Banded Object**.

   The [Create Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009630201-Create-Banded-Object-Dialog#BV) wizard appears, which contains a set of screens for helping you define a banded object easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select the business view in the current catalog using which to create the banded object.

   ![Create Banded Object - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916813079/crtbdobj_dt_bv.gif)
4. In the Display screen, add data fields to display as detail fields in the banded object.

   ![Create Banded Object - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904380183/crtbdobj_dsply_bv.gif)

   The Resources box lists the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif) and detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425495/bv_detail.gif) in the specified business view, as well as the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif) and dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828823/bv_dynfmla_dtl.gif) created for the business view in the current report. You can use them as detail fields in the banded object.

   To add a detail field, select a field in the Resources box, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it to the right box; to remove an unwanted detail field, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. You can make use of ![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) and ![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the display order of the detail fields in the banded object. By default the display names of the added fields will be used to label the corresponding detail columns; to edit the label text for a detail column, select in the Display Name text box and type a new one; if you want to automatically map the label text to the dynamic display name of the field at runtime, select the **Auto Map Field Name** checkbox in the text box. You can select the **Sort Fields By** button to specify in which manner to sort the detail values [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009629301-Modifying-Tables#Sort).
5. In the Group screen, specify the criteria for grouping data in the banded object [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables).

   ![Create Banded Object - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404916813335/crtbdobj_grp_bv.gif)
6. In the Summary screen, add summaries to calculate data in the banded object.

   ![Create Banded Object - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904380695/crtbdobj_sum_bv.gif)

   The Resources box lists the aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) in the specified business view, as well as the [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg) created for the business view in the current report. You can add them as summaries to calculate data in the banded object.

   To add a summary, in the right box select the group to which the summary will be applied (if you select Banded Object, it will be based on the whole business view), select a field in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it to the right box. You can add several summaries for any group level, and if a summary is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. To adjust the display order of the summaries in the current group or move a summary to another group, make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) . The position of the summaries in the banded object is determined by the Position and Column options and cannot be changed: a summary added for the Banded Object level is placed in the intersection of the banded footer panel and the first two detail columns with its name label which is the display name of the field used for the summary by default; a summary added for a specific group is placed in the intersection of the group's footer panel and the first two detail columns with its name label.
7. In the Filter screen, apply a filter to reduce the data displayed in the banded object. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the Filter drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   ![Create Banded Object - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404916813719/crtbdobj_fltr_bv.gif)
8. In the Style screen, specify the style of the banded object.

   ![Create Banded Object - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904380951/crtbdobj_sty_bv.gif)

   When you have specified to insert the banded object into another banded object in a page report, by default the banded object will [inherit its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613462-Applying-Styles#Inherit). If you want to apply another style to the banded object, clear the **Inherit Style** option and then select the required style from the Style box.
9. Select **Finish** to insert the banded object.

   If you have selected a panel in another banded object as the banded object destination in a page report, after finishing the wizard you need to select the mouse button in the destination once again in order to insert the banded object there.

Besides using the wizard, you can also drag a blank banded object to the report.

1. From the Basic category of the Components panel, drag ![Banded Object button](https://devnet.logianalytics.com/hc/article_attachments/4404916839959/btn_instbdobj.gif) to a destination in the report which allows the insertion of a banded object. A blank banded object is then created.
2. All the business views used in the current report can be used as the data source of the banded object. To locate a business view, select the data component that uses the business view. The business view is then displayed in the Data panel.
3. Drag the required view elements and dynamic resources from the Data panel into the banded panels.

## Creating a Banded Object Based on a Query Resource

1. Position the mouse pointer at the destination where you want to insert the banded object.
2. Select **Insert** > **Banded Object** or **Home** > **Insert** > **Banded Object**.

   The [Create Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009630201-Create-Banded-Object-Dialog#Query) wizard appears, which contains a set of screens for helping you define a banded object easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the Data screen, select the data resource in the current catalog using which to create the banded object.

   ![Create Banded Object wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404916813975/crtbdobj_dt.gif)

   If the predefined data resources are not what you want, select the first item in the corresponding resource node to create one. When a query is selected, you can select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog). Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009635941-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current page report to create the banded object, select the **More Options** button and then:

   * Select the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607762-Dataset-Editor-Dialog), or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report will still run the query separately for each dataset.
   * Select the **Current Dataset** radio button to make the banded object inherit the dataset from its parent.
4. In the Display screen, add data fields to display as detail fields in the banded object.

   ![Create Banded Object wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404904381207/crtbdobj_dsply.gif)

   The Resources box lists all the DBFields in the specified data resource, as well as the formulas and parameters that are valid to these DBFields in the current catalog. You can use them as detail fields in the banded object.

   To add a detail field, select a field in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it from the Resources box to the right box; to remove an unwanted detail field, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. You can make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) to adjust the display order of the detail fields in the banded object. By default the display names of the added fields will be used to label the corresponding detail columns; to edit the label for a detail column, select in the Display Name text box and type a new name. You can select the **Sort Fields By** button to specify in which manner to sort the detail values [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009629301-Modifying-Tables#Sort).
5. In the Group screen, specify the criteria for grouping the data in the banded object [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/1500009606502-Grouping-the-Data-in-Tables).
6. In the Summary screen, add summaries to calculate data in the banded object.

   ![Create Banded Object wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404904381719/crtbdobj_sum.gif)

   The Resources box lists all the DBFields in the specified data resource, as well as the formulas that are valid to these DBFields in the current catalog. You can create summaries based on these fields in the banded object.

   To add a summary, in the right box, select the group to which the summary will be applied (if you select Banded Object, it will be based on the whole dataset), select a field in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904175639/btn_addarrow.gif) or drag and drop it to the right box, then specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) as required. When DistinctSum is selected as the aggregate function, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) in the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog. From the Position and Column drop-down lists select the position of the summary: when a summary is added for the Banded Object level, you can place it and its name label in the intersection of the banded footer panel (Footer)/banded header panel (Header) and the first two detail columns (Detail)/a new summary column (Summary); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column. You can add several summaries for any group level and if a summary is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404911602327/btn_rmvarrow.gif)** or drag and drop it to the Resources box. To adjust the display order of the summaries in the current group or move a summary to another group, make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif). After the banded object is created, Logi Report will automatically give the summaries proper name labels to help you clarify the meaning of the numbers.

   The summaries created from the Summary screen will be added to the current catalog as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Create) even when identical summaries already exist. Therefore, it is better not to create summaries here, instead you can add dynamic summaries to the catalog and [drag and drop the dynamic summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009629241-Summary-Fields-) into the banded object after it is created.
7. In the Filter screen, add filter conditions on the fields that have been added to the banded object to reduce the data. For how to define a filter, [go here](https://devnet.logianalytics.com/hc/en-us/articles/1500009636161-Filtering-Reports#DefineFilter).

   ![Create Banded Object wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404916814231/crtbdobj_fltr.gif)
8. In the Style screen, specify the layout and style of the banded object.

   ![Create Banded Object wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404904382231/crtbdobj_sty.gif)

   In the Grow Report box, specify whether to create a vertical banded object, horizontal banded object, or mailing label banded object. In the Style box select the style of the banded object. When you have specified to insert the banded object into another banded object, by default the banded object will [inherit its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500009613462-Applying-Styles#Inherit). If you want to apply another style to the banded object, clear the **Inherit Style** option and then select the required style from the Style box.
9. Select **Finish** to insert the banded object.

   If you have selected a panel in another banded object as the banded object destination, after finishing the wizard you need to select the mouse button in the destination once again in order to insert the banded object there.

Besides using the wizard, you can also drag a blank banded object to the report.

1. From the Basic category of the Components panel, drag ![Banded Object button](https://devnet.logianalytics.com/hc/article_attachments/4404916839959/btn_instbdobj.gif) to a destination in the report which allows the insertion of a banded object. A blank banded object is then created.
2. In the Data panel, select the dataset in the current page report with which you want to create the banded object from the dataset drop-down list, or select **<Choose Data from...>** from the list to create a new a dataset for the banded object.
3. Drag the required data fields in the specified dataset from the Data panel into the banded panels.

**Notes:**

* When inserting a banded object using wizard,
  + Groups in the banded object will be indented according to the [Customize group indent](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Indent) option setting in the Options dialog.
  + By default all the summaries will be aligned horizontally in the banded object. If you want to align them vertically, select the option [Align summaries vertically](https://devnet.logianalytics.com/hc/en-us/articles/1500009609482-Options-Dialog#Align) in the Options dialog in advance.
* When you insert an object whose height is determined at runtime into the banded page footer panel (BPF), for example a subreport, but do not set the height of the panel high enough to hold this object, the object might get overlapped with the ones that are in the panel which is above the BPF panel at runtime.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009628361-Banded-Objects) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628441-Modifying-Banded-Objects)
