---
title: "Merging Catalogs"
id: 1500009562762
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562762-Merging-Catalogs
updated_at: 2021-07-24T05:56:13Z
---

# Merging Catalogs

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583101-Managing-Data-Resources-in-a-Catalog)

# Merging Catalogs

Two catalogs can be merged. The merge operation occurs when you save a report to another directory in which a catalog of the same name already exists.

Below is a list of the sections covered in this topic:

> * [Specifying the Checking Level](#Specify)
> * [Merging Catalogs](#Merge)

## Specifying the Checking Level

When merging catalogs, Logi JReport Designer will check for differences between the two catalogs. You can specify the checking level to suit your requirements.

**To specify the checking level:**

1. Select **File** > **Options**.
2. In the Options dialog, select **Catalog** in the Category box.

   ![Options dialog - Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404893862679/optn_ctlg.gif)
3. Select the required level in the Merge Catalog Options box. Options are:
   * **Identify All Differences**  
     Logi JReport Designer will check for all differences between the two catalogs. All the resources of the report will be displayed in the Merge dialog with all the conflicting resources marked.
   * **Identify Critical Differences**  
     Logi JReport Designer will check for differences that can cause the engine to fail when running the report. All the resources of the report will be displayed in the Merge dialog with any critical conflicting resources marked. As a result, when this option is selected, some different values may be returned when you run the saved report later.
   * **Ignore Differences**  
      Does not show differences between the two catalogs. If there are conflicts, they will remain in the resources of the target catalog. As a result, when this option is selected, a saved report might not run later.
4. Select **OK** in the Options dialog to accept the settings.

When you merge the two catalogs, resources that have the same mapping names in the two catalogs may conflict with each other (have different property values). Logi JReport Designer will check the differences for you according to the level specified.

## Merging Catalogs

With the checking level specified, you can then start to merge catalogs.

1. Open a report in the catalog that you want to merge with another catalog.
2. Select **File** > **Save To**. The Save To dialog appears.
3. Choose a directory where a catalog with the same name exists, and then save the report. If you specified the checking level as Identify All Differences or Identify Critical Differences and the selected resources conflict with those in the target catalog, the [Merge](https://devnet.logianalytics.com/hc/en-us/articles/1500009566662-Merge-Dialog) dialog appears for dealing with conflicting resources.

   ![Merge dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893869719/merge.gif)
4. Highlight one conflicting resource in the resources to be merged box, and then select the operations:
   * **Rename** - Renames the selected conflicting resource, and copies it to the target catalog with a new name.
   * **Replace** - Replaces the target catalog with the selected conflicting resource from the source catalog. In this case, the reports that use this object in the target catalog will be impacted.
   * **Skip** - Keeps the value in the target catalog for the selected conflicting resource. In this case, the report that uses this object in the source catalog will be impacted.
5. Select the **Differences** button and the Property Differences dialog appears.

   ![Property Differences dialog](https://devnet.logianalytics.com/hc/article_attachments/4404894010007/ctlg_merge_prptydif.gif)

   The properties values of the conflicting resource from the two catalogs will be displayed in this dialog with any differences highlighted. Select the **Previous**/**Next** button in the dialog, and it will go to the previous/next conflicting resource. Select **Close** to close the dialog.
6. Select the **Target Relation** button in the Merge dialog and the Target Relation dialog appears.

   ![Target Relation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404894010263/ctlg_merge_target.gif)

   The name of the resource and its parent node in the target catalog will then be displayed in this dialog.

   For example, sometimes a resource is marked in the Merge dialog, but in the Properties Differences dialog, no difference is shown between the two resources. In this case you can use this button to check whether the parent nodes of the two resources are different.
7. Select **Close** to close the Target Relation dialog box and return to the Merge dialog.
8. Select the **Merge** button when you are finished. Logi JReport Designer will save the report according to the changes that you have made.
9. Publish the catalog and the reports and test to ensure all the reports are working properly.

**Notes:**

* Sometimes, though some objects are marked in the Merge dialog, in the Properties Differences dialog, you will not find these differences. The reason is that some children of the two objects are different.
* Logi JReport Designer checks parameters based on the whole catalog. For example, assume that there is a parameter named Param1 in DataSource1 of the source catalog, and there is also a parameter named Param1 in DataSource2 in the target catalog. These two parameters in different connections will be checked as a conflicting resource. You must rename the parameter in order to get a correct result.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583101-Managing-Data-Resources-in-a-Catalog)
