---
title: "Inserting Banded Objects in a Report"
id: 5735511901079
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735511901079-Inserting-Banded-Objects-in-a-Report
updated_at: 2022-11-02T04:12:40Z
---

# Inserting Banded Objects in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520497431-Modifying-Banded-Objects)

# Inserting Banded Objects in a Report

You can create banded objects in a report easily using the banded object wizard. However, the procedure you use with the wizard varies with the data resource type: business view or query resource. This topic introduces how you can create a banded object using the banded object wizard when you have different data resources.

This topic contains the following sections:

* [Creating a Banded Object Based on a Business View](#BV)
* [Creating a Banded Object Based on a Query Resource](#Query)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) A page report can apply either query resources or business views, which is determined by the Create Using Business View option at the time when [you create the page report](https://devnet.logianalytics.com/hc/en-us/articles/5735569787671-Creating-Reports#Page). Once defined, all data components in the page report can only use the specified data resource type.

## Creating a Banded Object Based on a Business View

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the banded object.
2. Navigate to **Insert** > **Banded Object** or **Home** > **Insert** > **Banded Object**. Designer displays the [Create Banded Object dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500075543-Create-Banded-Object-Dialog-Box#BV). You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to use to create the
   banded object.

   ![Create Banded Object - Data](https://devnet.logianalytics.com/hc/article_attachments/9898516311831/crtbdobj_dt_bv.gif)
4. In the **Display** screen, add data fields to display as detail fields in the banded object.

   ![Create Banded Object - Display](https://devnet.logianalytics.com/hc/article_attachments/9898532760471/crtbdobj_dsply_bv.gif)

   The Resources box lists the group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898534261399/bv_grp.gif) and detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/9898517937943/bv_detail.gif) in the business view from which the dataset the banded object applies is created, and the [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/9898517940503/bv_dynfmla_grp.gif) and dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/9898517944087/bv_dynfmla_dtl.gif) that you have added for the business view in the current report. You can use them as detail fields in the banded object.

   * To add a detail field, select a field in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the field from the Resources box to the right box.
   * In the **Display Name** column, select in the text box to edit the label for each detail column in the banded object. When you select the **Auto Map Field Name** checkbox in the text box, Designer applies the field's display name to label the detail column, and at runtime, Server maps the label to the dynamic display name of the field if the administrator defines it.
   * Use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the detail fields in the banded object.
   * Select **Sort Fields By** to specify how to sort the detail values [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/5735507432983-Modifying-Tables#Sort).
5. In the **Group** screen, specify the criteria for grouping data in the banded object [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables).

   ![Create Banded Object - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898532766359/crtbdobj_grp_bv.gif)
6. In the **Summary** screen, add summaries to calculate data in the banded object.

   ![Create Banded Object - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898532784535/crtbdobj_sum_bv.gif)

   The Resources box lists the aggregation objects ![Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/9898534371351/bv_agg.gif) in the business view from which the dataset the banded object applies is created, and the [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Agg) that you have created for the business view in the current report. You can add them as summaries to calculate data in the banded object.

   * To add a summary, in the right box, select the group to which you want to apply the summary (if you select **Banded Object**, it is based on the whole business view), then select a field in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the field from the Resources box to the right box. You can add several summaries for any group level.
   * Use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the summaries in the current group or move a summary to another group.
   * Designer determines the position of the summaries in the banded object by the **Position** and **Column** options and you cannot change it.
     + Designer places a summary added for the Banded Object level in the intersection of the banded footer panel and the first two detail columns with its name label which is the display name of the field used for the summary by default.
     + Designer places a summary added for a specific group in the intersection of the group's footer panel and the first two detail columns with its name label.
7. In the **Dataset Filter** screen, ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")[filter the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report) the banded object applies. If you have added filter conditions to the dataset somewhere else, Designer displays the conditions in the screen. You can further edit the conditions. Be aware that a filter on a dataset applies to all data components in the same report that use this dataset.

   ![Create Banded Object - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898532787223/crtbdobj_fltr_bv.gif)
8. In the **Style** screen, specify the style of the banded object. If you have specified to insert the banded object into another banded object, the banded object [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports#Inherit) by default; to apply another style to the banded object, clear **Inherit Style** and select the required style from the **Style** box.

   ![Create Banded Object - Style](https://devnet.logianalytics.com/hc/article_attachments/9898532797975/crtbdobj_sty_bv.gif)
9. Select **Finish** to insert the banded object.
10. If you have selected a panel in another banded object as the banded object destination, after finishing the Create Banded Object dialog box, you need to select in the destination once again to insert the banded object there.

Besides using wizard, you can also drag a blank banded object to a report.

1. From the **Components** panel, drag the **Banded Object** icon ![Banded Object icon](https://devnet.logianalytics.com/hc/article_attachments/9898519692183/icon_bdobj.gif) in the **Basic** category to the destination in the report, which allows the insertion of a banded object. Designer creates a blank banded object.
2. ![This image notes any new content for version 19 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898421749655/___newv19.png "New for version 19.")From the dataset drop-down list in the **Data** panel, select a dataset from the ones you have created in the report to use for the banded object, or select **<Choose Data from...>** to [create a dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735576548887-Managing-Datasets-in-a-Report#NewDataset) and apply it to the banded object. Designer then displays the data fields available to the specified dataset in the panel.
3. Drag fields from the Data panel into the banded panels.

## Creating a Banded Object Based on a Query Resource

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the banded object.
2. Navigate to **Insert** > **Banded Object** or **Home** > **Insert** > **Banded Object**. Designer displays the [Create Banded Object dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735500075543-Create-Banded-Object-Dialog-Box#Query). You can use the Back and Next buttons or select the screen name on the screen navigation bar to switch between the screens.
3. In the **Data** screen, [specify the dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735586128791-Applying-Datasets-in-a-Report#DC) you want to use to create the
   banded object.

   ![Create Banded Object wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/9898516345111/crtbdobj_dt.gif)
4. In the **Display** screen, add data fields to display as detail fields in the banded object.

   ![Create Banded Object wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/9898532826903/crtbdobj_dsply.gif)

   The Resources box lists all DBFields in the query resource from which the dataset the banded object applies is created, and the formulas and parameters that are valid to these DBFields in the current catalog. You can use them as detail fields in the banded object.

   * To add a detail field, select a field in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the field from the box to the right box.
   * Designer applies the display names of the added fields to label the detail columns in the banded object by default. To edit the label for a detail column, select in the **Display Name** text box and type a new name.
   * Use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the detail fields in the banded object.
   * Select **Sort Fields By** to specify how to sort the detail values [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/5735507432983-Modifying-Tables#Sort).
5. In the **Group** screen, specify the criteria for grouping data in the banded object [the same as you do for a table](https://devnet.logianalytics.com/hc/en-us/articles/5735527697943-Grouping-Data-in-Tables).
6. In the **Summary** screen, add summaries to calculate data in the banded object.

   ![Create Banded Object wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/9898532856983/crtbdobj_sum.gif)

   The Resources box lists all DBFields in the query resource from which the dataset the banded object applies is created, and the formulas that are valid to these DBFields in the current catalog. You can create summaries based on these fields in the banded object.

   * To add a summary, in the right box, select the group to which you want to apply the summary (if you select **Banded Object**, the summary is based on the whole dataset), then select a field in the **Resources** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) or drag the field from the Resources box to the right box. You can add several summaries for any group level. After the banded object is created, Designer automatically gives the summaries proper name labels to help you clarify the meaning of the numbers.
   * Specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) for each summary. If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) in the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box) dialog box.
   * From the **Position** and **Column** drop-down lists, select the position of each summary.
     + For a summary added to the Banded Object level, you can place it and its name label in the intersection of the banded footer panel (Footer)/banded header panel (Header) and the first two detail columns (Detail)/a new summary column (Summary).
     + For a summary added to a specific group, you can place it and its name label in the intersection of the group footer panel/group header panel and the first two detail columns/a new summary column. You can add several summaries for any group level.
   * Use **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif) to adjust the display order of the summaries in the current group or move a summary to another group.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Designer adds the summaries created from the Summary screen to the current catalog as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Create) even when identical summaries already exist. If you can, you should not create summaries here, instead you can add dynamic summaries to the catalog and [drag the dynamic summaries](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields) to the banded object after you have created it.
7. In the **Filter** screen, filter the banded object by adding conditions based on the fields it contains. [Select here](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports#DefineFilter) for how to define a filter.

   ![Create Banded Object wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/9898532862231/crtbdobj_fltr.gif)
8. In the **Style** screen, specify the layout and style of the banded object.

   ![Create Banded Object wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/9898532869143/crtbdobj_sty.gif)

   * In the **Grow Report** box, specify whether to create a vertical banded object, horizontal banded object, or mailing label banded object.
   * In the **Style** box, select the style of the banded object. If you have specified to insert the banded object into another banded object, the banded object [inherits its parent's style](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports#Inherit) by default. To apply another style to the banded object, clear **Inherit Style** and select the required style from the Style box.
9. Select **Finish** to insert the banded object.
10. If you have selected a panel in another banded object as the banded object destination, after finishing the Create Banded Object dialog box, you need to select in the destination once again to insert the banded object there.

Besides using wizard, you can also drag a blank banded object to the report and define its data using a query-based dataset [as seen earlier in this topic](#Drag).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* When you insert a banded object using wizard,
  + Designer indents the groups in the banded object according to the [Customize group indent](https://devnet.logianalytics.com/hc/en-us/articles/5735524192535-Options-Dialog-Box#Indent) option setting in the Options dialog box.
  + By default, Designer aligns all the summaries horizontally in the banded object. If you want to align them vertically, select [Align summaries vertically](https://devnet.logianalytics.com/hc/en-us/articles/5735524192535-Options-Dialog-Box#Align) in the Component category of the Options dialog box in advance.
* When you insert an object whose height is determined at runtime into the banded page footer panel (BPF), for example a subreport, but do not set the height of the panel high enough to hold this object, the object might get overlapped with the ones that are in the panel which is above the BPF panel at runtime.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735520497431-Modifying-Banded-Objects)
