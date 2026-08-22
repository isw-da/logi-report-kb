---
title: "Inserting a Banded Object"
id: 1500010094301
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094301-Inserting-a-Banded-Object
updated_at: 2022-03-28T07:17:54Z
---

# Inserting a Banded Object

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094281-Working-with-Banded-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094321-Modifying-Banded-Objects)

# Inserting a Banded Object

You can create banded objects in a report easily using the banded object wizard, however, the wizard varies with the data resource type used for the banded object: business view or query resource. This topic introduces how you can create a banded object with the banded object wizard using different data resource.

You can insert banded objects in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship). When you insert a banded object into another banded object in a page report, you can [set up data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500010056782-Setting-Up-Data-Container-Links-in-Banded-Objects) between the banded object and its parent.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) A page report can use either query resources or business views, which is determined at the time when [you create the page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) by the **Create Using Business View** option. Once defined, all the data components in the page report can only use the specified data resource type.

This topic contains the following sections:

* [Creating a Banded Object Based on a Business View](#BV)
* [Creating a Banded Object Based on a Query Resource](#Query)

## Creating a Banded Object Based on a Business View

1. Position the mouse pointer at the destination where you want to insert the banded object.
2. Select **Insert** > **Banded Object** or **Home** > **Insert** > **Banded Object**.

   Designer displays the [Create Banded Object dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058322-Create-Banded-Object-Dialog-Box#BV), which contains a set of screens for helping you to define a banded object easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the business view in the current catalog using which to create the banded object.

   If you have specified to insert the banded object into any of the following panels in a banded object: banded header panel, banded footer panel, group header panel, or group footer panel, Designer displays the **Inherit from the Parent** option. Select it if you want the banded object to inherit the business view that its parent uses.

   ![Create Banded Object - Data](https://devnet.logianalytics.com/hc/article_attachments/4404856998807/crtbdobj_dt_bv.gif)
4. In the **Display** screen, add data fields to display as detail fields in the banded object.

   ![Create Banded Object - Display](https://devnet.logianalytics.com/hc/article_attachments/4404856999191/crtbdobj_dsply_bv.gif)

   The Resources box lists the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404848663831/bv_grp.gif) and detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664087/bv_detail.gif) in the specified business view, as well as the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404857035543/bv_dynfmla_grp.gif) and dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404848664343/bv_dynfmla_dtl.gif) that you have created for the business view in the current report. You can use them as detail fields in the banded object.

   To add a detail field, select a field in the Resources box, then select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box; to remove an unwanted detail field, select it and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. You can make use of the **Move Up**![Move up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to adjust the display order of the detail fields in the banded object. By default, Designer uses the display names of the added fields to label the corresponding detail columns; to edit the label text for a detail column, select in the **Display Name** text box and type a new one; if you want to automatically map the label text to the dynamic display name of the field at runtime, select the **Auto Map Field Name** checkbox in the text box. You can also select the **Sort Fields By** button to specify in which manner to sort the detail values [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables#Sort).
5. In the **Group** screen, specify the criteria for grouping data in the banded object [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables).

   ![Create Banded Object - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404856999575/crtbdobj_grp_bv.gif)
6. In the **Summary** screen, add summaries to calculate data in the banded object.

   ![Create Banded Object - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404848614295/crtbdobj_sum_bv.gif)

   The Resources box lists the aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404857037591/bv_agg.gif) in the specified business view, as well as the [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Agg) that you have created for the business view in the current report. You can add them as summaries to calculate data in the banded object.

   To add a summary, in the right box, select the group to which you want to apply the summary (if you select **Banded Object**, it is based on the whole business view), select a field in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box. You can add several summaries for any group level, and if a summary is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. Make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) to adjust the display order of the summaries in the current group or move a summary to another group. Designer determines the position of the summaries in the banded object by the **Position** and **Column** options and you cannot change it: Designer places a summary added for the Banded Object level in the intersection of the banded footer panel and the first two detail columns with its name label which is the display name of the field used for the summary by default; Designer places a summary added for a specific group in the intersection of the group's footer panel and the first two detail columns with its name label.
7. In the **Filter** screen, apply a filter to reduce the data to display in the banded object. You can select a [predefined filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Filter) of the specified business view from the **Filter** drop-down list to apply, or select **User Defined** in the list to define a new filter as required.

   ![Create Banded Object - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404856999959/crtbdobj_fltr_bv.gif)
8. In the **Style** screen, specify the style of the banded object.

   If you have specified to insert the banded object into another banded object, by default, the banded object [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062802-Applying-Styles-to-Reports#Inherit); to apply another style to the banded object, clear the **Inherit Style** option and then select the required style from the **Style** box.

   ![Create Banded Object - Style](https://devnet.logianalytics.com/hc/article_attachments/4404857000215/crtbdobj_sty_bv.gif)
9. Select **Finish** to insert the banded object.

   If you have selected a panel in another banded object as the banded object destination, after finishing the dialog box, you need to select the mouse button in the destination once again in order to insert the banded object there.

Besides using the wizard, you can also drag a blank banded object to the report.

1. From the **Components** panel, drag the **Banded Object** icon ![Banded Object icon](https://devnet.logianalytics.com/hc/article_attachments/4404857066007/icon_bdobj.gif) in the Basic category to a destination in the report which allows the insertion of a banded object. Designer creates a blank banded object.
2. You can use all the business views applied in the current report as the data resource of the banded object. To locate a business view, select the data component that uses the business view. Designer then displays the business view in the **Data** panel.
3. Drag the required view elements and dynamic resources from the Data panel into the banded panels.

## Creating a Banded Object Based on a Query Resource

1. Position the mouse pointer at the destination where you want to insert the banded object.
2. Select **Insert** > **Banded Object** or **Home** > **Insert** > **Banded Object**.

   Designer displays the [Create Banded Object dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058322-Create-Banded-Object-Dialog-Box#Query), which contains a set of screens for helping you define a banded object easily. You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, select the data resource in the current catalog using which to create the banded object.

   ![Create Banded Object wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404848614679/crtbdobj_dt.gif)

   If the predefined data resources are not what you want, you can select the first item in the corresponding resource node to create one in the current catalog to use. When you select a query, you can select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500010062582-Creating-Queries-in-a-Catalog). Designer then automatically creates a [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500010062542-Creating-and-Managing-Datasets) based on the selected data resource in the page report.

   If you want to use an existing dataset in the current page report to create the banded object, select the **More Options** button and then:

   * Select the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the specified dataset in the [Dataset Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058622-Dataset-Editor-Dialog-Box), or select the **<New Dataset...>** item to create a dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi Report Engine still runs the query separately for each dataset.
   * If you have specified to insert the banded object into an object that already applies a dataset, such as a banded panel, Designer enables the **Current Dataset** radio button. Select it if you want the banded object to inherit the dataset from the parent object.
4. In the **Display** screen, add data fields to display as detail fields in the banded object.

   ![Create Banded Object wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404857000727/crtbdobj_dsply.gif)

   The Resources box lists all the DBFields in the specified data resource, as well as the formulas and parameters that are valid to these DBFields in the current catalog. You can use them as detail fields in the banded object.

   To add a detail field, select a field in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it from the Resources box to the right box; to remove an unwanted detail field, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. You can make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) to adjust the display order of the detail fields in the banded object. By default, Designer applies the display names of the added fields to label the corresponding detail columns; to edit the label for a detail column, select in the **Display Name** text box and type a new name. You can also select the **Sort Fields By** button to specify in which manner to sort the detail values [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables#Sort).
5. In the **Group** screen, specify the criteria for grouping the data in the banded object [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables).
6. In the **Summary** screen, add summaries to calculate data in the banded object.

   ![Create Banded Object wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404848614935/crtbdobj_sum.gif)

   The Resources box lists all the DBFields in the specified data resource, as well as the formulas that are valid to these DBFields in the current catalog. You can create summaries based on these fields in the banded object.

   To add a summary, in the right box, select the group to which you want to apply the summary (if you select **Banded Object**, the summary is based on the whole dataset), select a field in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box, then specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) as required. If you select **DistinctSum**, you should select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box) dialog box. From the **Position** and **Column** drop-down lists, select the position of the summary: when you add a summary for the Banded Object level, you can place it and its name label in the intersection of the banded footer panel (Footer)/banded header panel (Header) and the first two detail columns (Detail)/a new summary column (Summary); for a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column. You can add several summaries for any group level and if a summary is not required, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box. Make use of ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) to adjust the display order of the summaries in the current group or move a summary to another group. After the banded object is created, Designer automatically gives the summaries proper name labels to help you clarify the meaning of the numbers.

   Designer adds the summaries created from the Summary screen to the current catalog as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Create) even when identical summaries already exist. Therefore, it is better not to create summaries here, instead you can add dynamic summaries to the catalog and [drag and drop the dynamic summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500010094901-Working-with-Summary-Fields) into the banded object after you have created it.
7. In the **Filter** screen, add filter conditions based on the fields that you have added to the banded object to reduce the data. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/1500010101241-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Banded Object wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404857001495/crtbdobj_fltr.gif)
8. In the **Style** screen, specify the layout and style of the banded object.

   In the **Grow Report** box, specify whether to create a vertical banded object, horizontal banded object, or mailing label banded object. In the **Style** box, select the style of the banded object. If you have specified to insert the banded object into another banded object, by default, the banded object [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/1500010062802-Applying-Styles-to-Reports#Inherit); to apply another style to the banded object, clear the **Inherit Style** option and then select the required style from the Style box.

   ![Create Banded Object wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404857001751/crtbdobj_sty.gif)
9. Select **Finish** to insert the banded object.

   If you have selected a panel in another banded object as the banded object destination, after finishing the dialog box, you need to select the mouse button in the destination once again in order to insert the banded object there.

Besides using the wizard, you can also drag a blank banded object to the report.

1. From the **Components** panel, drag the **Banded Object** icon ![Banded Object icon](https://devnet.logianalytics.com/hc/article_attachments/4404857066007/icon_bdobj.gif) in the Basic category to a destination in the report which allows the insertion of a banded object. Designer creates a blank banded object.
2. In the **Data** panel, select the dataset in the current page report with which you want to create the banded object from the dataset drop-down list, or select **<Choose Data from...>** from the list to create a new a dataset for the banded object.
3. Drag the required data fields in the specified dataset from the Data panel into the banded panels.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* When you insert a banded object using wizard,
  + Designer indents the groups in the banded object according to the [Customize group indent](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Indent) option setting in the Options dialog box.
  + By default, Designer aligns all the summaries horizontally in the banded object. If you want to align them vertically, select the option [Align summaries vertically](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Align) in the Options dialog box in advance.
* When you insert an object whose height is determined at runtime into the banded page footer panel (BPF), for example a subreport, but do not set the height of the panel high enough to hold this object, the object might get overlapped with the ones that are in the panel which is above the BPF panel at runtime.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094281-Working-with-Banded-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094321-Modifying-Banded-Objects)
