---
title: "Inserting a Banded Object"
id: 1500009583281
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583281-Inserting-a-Banded-Object
updated_at: 2021-07-24T05:56:11Z
---

# Inserting a Banded Object

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562842-Banded-Objects)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583341-Modifying-a-Banded-Object)

# Inserting a Banded Object

You can insert a banded object into a page report either with the wizard or by dragging and dropping. With the banded object wizard, it is easy to create banded objects, however, the wizard varies with the data resource type used to create the banded object: query resource or business view.

The data resource type a page report can use is determined at the time when  [the page report is created](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component)  by the Create Using Business View option[.](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component) Once defined, all the data components in the page report can only be created on the specified data resource type.

A banded object can be inserted in the report areas listed in [Component placement](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports#Relationship).

Below is a list of the sections covered in this topic:

> * [Inserting a Banded Object Based on a Business View](#Web)
> * [Inserting a Banded Object Based on a Query Resource](#Page)

## Inserting a Banded Object Based on a Business View

1. Position the mouse pointer at the destination where you want to insert the banded object. It can be in an empty area of the page report or inside another banded object.
2. Select **Insert** > **Banded Object** or **Home** > **Insert** > **Banded Object****.**
   The [Create Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009585961-Create-Banded-Object-Dialog#BV) wizard appears.
3. In the Data screen, select a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) on which to create the banded object.

   ![Create Banded Object wizard  - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889384215/crtbdobj_dt-bv.gif)
4. In the Display screen, add group and detail objects to be displayed in the banded object. To add an object, select it in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it from the Resources box to the display field box on the right. You can add only one object at a time. If an object is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the objects. If required, modify the display name of any added object by selecting its Display Name text box. You can also select the **Sort Fields By** button to specify the objects on which the sorting will be based and the sorting manner as required (for details, refer to [Sorting the Data)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data).

   ![Create Banded Object wizard - Display screen](https://devnet.logianalytics.com/hc/article_attachments/4404889384471/crtbdobj_dsply-bv.gif)
5. In the Group screen, add group objects as the grouping criteria. For more information about data grouping, see [Grouping the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data).

   ![Create Banded Object wizard - Group screen](https://devnet.logianalytics.com/hc/article_attachments/4404893945111/crtbdobj_grp-bv.gif)
6. In the Summary screen, add the aggregations to be displayed in the banded object. In the right box, specify the group to which the aggregation will be applied (if you select Banded Object, the aggregation will be based on the whole business view), select an aggregation in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the right box. You can add several aggregations for any level. Logi JReport will automatically give the aggregations proper name labels to help you clarify the meaning of the numbers. If an aggregation is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the aggregations in the current group or move an aggregation to another level if needed.

   ![Create Banded Object wizard - Summary screen](https://devnet.logianalytics.com/hc/article_attachments/4404893945367/crtbdobj_sum-bv.gif)
7. To apply filters to the banded object so as to reduce the data displayed in the banded object, go to the Filter screen and define the filter conditions. For how to define a filter, refer to [Filtering the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).

   ![Create Banded Object wizard - Filter screen](https://devnet.logianalytics.com/hc/article_attachments/4404889384855/crtbdobj_fltr-bv.gif)
8. In the Style screen, specify the style of the banded object.

   ![Create Banded Object wizard - Style screen](https://devnet.logianalytics.com/hc/article_attachments/4404893944855/crtbdobj_sty.gif)

   If you have specified to insert the banded object into another banded object, by default the banded object will inherit its parent's style. If you want to apply another style to the banded object, uncheck the **Inherit Style** option and then select the required style from the Style box. For more information, see [Inheriting Styles](https://devnet.logianalytics.com/hc/en-us/articles/1500009593241-Inheriting-Styles).
9. Select **Finish** to insert the banded object.

   If you have specified to insert the banded object in the report body or tabular cell, the banded object will be inserted there upon selecting the Finish button; otherwise, select the mouse button in the location to insert the banded object.

Besides using the wizard, you can also drag a blank banded object to the report. To do this:

1. From the Basic category of the Components panel, drag the **Banded Object** button ![Banded Object button](https://devnet.logianalytics.com/hc/article_attachments/4404894006551/btn_instbdobj.gif) to a destination in the report which allows the insertion of a banded object. A blank banded object is then created.
2. All the business views used in the current page report can provide data resources to the banded object. To locate a business view, select the component that uses the business view. The business view will be displayed in the Data panel.
3. Drag the required fields from the Data panel into the banded panels.

## Inserting a Banded Object Based on a Query Resource

1. Position the mouse pointer at the destination where you want to insert the banded object. It can be in an empty area of the page report or inside another banded object.
2. Select **Insert** > **Banded Object** or **Home** > **Insert** > **Banded Object****.** The [Create Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009585961-Create-Banded-Object-Dialog) wizard appears.
3. In the Data screen, select the data resource on which to create the banded object. If the given data resources are not what you want, select the first item  in the corresponding resource node to create one. When a query is selected, select the **Edit** button to [modify the query](https://devnet.logianalytics.com/hc/en-us/articles/1500009570662-Editing-a-Query) if required. Then a new [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets) based on the selected data resource is created in the page report.

   If you want to use an existing dataset in the current report to create the banded object, select the **More Options** button and then:

   * Check the **Existing Dataset** radio button and select a dataset. You can select the **Edit** button to modify the selected dataset in the [Dataset Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586301-Dataset-Editor-Dialog) if necessary, or select the **<New Dataset...>** item to create a new dataset in the page report to use. It is always better to use an existing dataset rather than create a new one. Even when the two datasets are based on the same query, Logi JReport will still run the query separately for each dataset.
   * Check the **Current Dataset** radio button to make the banded object inherit the dataset from its parent.

![Create Banded Object wizard - Data screen](https://devnet.logianalytics.com/hc/article_attachments/4404889383191/crtbdobj_dt.gif)

4. In the Display screen, add the fields to be displayed in the banded object. To add a field, select it in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it from the Resources box to the display field box on the right. You can add only one field at a time. If a field is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the fields. If required, modify the display name of any added field by selecting its Display Name text box. You can also select the **Sort Fields By** button to specify the fields on which the sorting will be based and the sorting manner as required (for details, refer to [Sorting the Data)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data).

   ![Create Banded Object wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404893944343/crtbdobj_dsply.gif)
5. In the Group screen, add the fields as the grouping criteria. For more information about data grouping, see [Grouping the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data).

   ![Create Banded Object wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404893944599/crtbdobj_grp.gif)
6. To add summaries, go to the Summary screen. In the sum on box on the right, specify the group to which the summary will be applied (if you select Banded Object, the summary will be based on the whole dataset), select a field in the Resources box as the summary field and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the box, then select the function for the summary from the Aggregate Function column. You can add several summaries for any group level. Logi JReport will automatically give the summaries proper name labels to help you clarify the meaning of the numbers. If a field is not required, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box. Select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) to adjust the order of the summary fields in the current group or move a summary field to another group if needed.

   The summaries created from the Summary screen will be added to the current catalog data source as [static summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009589741-Creating-a-Summary) even when identical summaries already exist. Therefore, it is better not to create summaries here, instead you can add dynamic summaries to the catalog and [drag and drop the dynamic summaries](https://devnet.logianalytics.com/hc/en-us/articles/1500009563602-Summary-Fields) into the banded object after it is created.

   ![Create Banded Object wizard - Summary](https://devnet.logianalytics.com/hc/article_attachments/4404889383703/crtbdobj_sum.gif)
7. To apply filters to the banded object so as to reduce the data displayed in the banded object, go to the Filter screen and define the filter conditions. For how to define a filter, refer to [Filtering the Data](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data).

   ![Banded Wizard - Filter](https://devnet.logianalytics.com/hc/article_attachments/4404889383959/crtbdobj_fltr.gif)
8. In the Style screen, specify the style of the banded object.

   ![Banded Wizard - Style](https://devnet.logianalytics.com/hc/article_attachments/4404893944855/crtbdobj_sty.gif)

   If you have specified to insert the banded object into another banded object, by default the banded object will inherit its parent's style. If you want to apply another style to the banded object, uncheck the **Inherit Style** option and then select the required style from the Style box. For more information, see [Inheriting Styles](https://devnet.logianalytics.com/hc/en-us/articles/1500009593241-Inheriting-Styles).
9. Select **Finish** to insert the banded object.

   If you have specified to insert the banded object in the report body or tabular cell, the banded object will be inserted there upon selecting the Finish button; otherwise, select the mouse button in the location to insert the banded object.

Besides using the wizard, you can also drag a blank banded object to the report. To do this:

1. From the Basic category of the Components panel, drag **Banded Object** button ![Banded Object button](https://devnet.logianalytics.com/hc/article_attachments/4404894006551/btn_instbdobj.gif) to a destination in the report which allows the insertion of a banded object. A blank banded object is then created.
2. In the Data panel, select the dataset in the current page report with which you want to create the banded object from the dataset drop-down list, or select **<Choose Data from...>** from the list to [create a new a dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets#View) for the banded object.
3. Drag the required fields in the specified dataset from the Data panel into the banded panels.

When a banded object is inserted into another banded object, you can [set up data container link](https://devnet.logianalytics.com/hc/en-us/articles/1500009583301-Setting-Up-a-Data-Container-Link) between the banded object and its parent.

**Notes:**

* When inserting a banded object using wizard,
  + Groups in the banded object will be indented according to the [Customize group indent](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog#Indent) option setting in the Options dialog.
  + By default all the summaries will be aligned horizontally in the banded object. If you want to align them vertically, check the option [Align summaries vertically](https://devnet.logianalytics.com/hc/en-us/articles/1500009588081-Options-Dialog#Align) in the Options dialog in advance.
* When you insert an object whose height is determined at runtime into the BandedPageFooter panel (for example, a subreport), but do not set the height of the panel high enough to hold this object, the object might get overlapped with the ones that are in the panel which is above the BPF panel at runtime.

**See also:**

* [Horizontal Banded Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009587521-Horizontal-Banded-Wizard-Dialog) for detailed explanation about options in this wizard.
* [Mailing Label Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009566682-Mailing-Label-Wizard-Dialog) for detailed explanation about options in this wizard.
* **An example:** The SampleComponents catalog, included with Logi JReport Designer, contains reports that have examples of report component types. For the banded object component example, open `<install_root>\Demo\Reports\SampleComponents\BandedObjectReport.cls`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562842-Banded-Objects)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583341-Modifying-a-Banded-Object)
