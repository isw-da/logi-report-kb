---
title: "Merging Catalogs"
id: 1500010028542
section: "Creating and Managing Catalogs - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028542-Merging-Catalogs
updated_at: 2021-07-24T10:39:32Z
---

# Merging Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063201-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028562-Maintaining-Catalogs-with-the-Catalog-Doctor)

# Merging Catalogs

You can make two catalogs that have the same name merged by saving reports of one catalog to another directory in which a catalog of the same name already exists.

When merging catalogs, Logi JReport Designer will check for the differences between the two catalogs, for example, resources that have the same mapping names in the two catalogs may conflict with each other because they have different property values. If there are differences between the two catalogs, based on the [Merge Catalog Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010031962-Options-Dialog#MergeCat) setting in the Options dialog, Logi JReport Designer will either identify them and prompt the Merge dialog or ignore them and have them remained in the target catalog. By default, Logi JReport Designer identifies the critical differences that can cause the engine to fail in running reports and marks them in the Merge dialog.

**To merge catalogs:**

1. Open a report in the catalog that you want to merge with another catalog.
2. Select **File** > **Save To**.
3. In the Save To dialog, choose a directory to save the report, where a catalog with the same name as the current catalog already exists.

   If the Merge Catalog Options is specified as Identify All Differences or Identify Critical Differences in the Options dialog and there are conflicting resources between the two catalogs, the [Merge](https://devnet.logianalytics.com/hc/en-us/articles/1500010067081-Merge-Dialog) dialog appears. It lists all the resources referenced by the report with the conflicting resources marked.

   ![Merge dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901199511/merge.gif)
4. Select a conflicting resource, then select the **Differences** button to view the differences of the resource between the source catalog and target catalog in the Property Differences dialog.

   ![Property Differences dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909295127/ctlg_merge_prptydif.gif)

   The property values of the conflicting resource from the two catalogs are listed in the dialog with any differences highlighted. You can use the Previous/Next button to go to the previous/next conflicting resource between the two catalogs.
5. To view the parent resources of the selected conflicting resource in the target catalog, select the **Target Relation** button. The Target Relation dialog then appears showing the relation.

   ![Target Relation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901348119/ctlg_merge_target.gif)

   Sometimes a resource is marked in the Merge dialog, but in the Property Differences dialog no difference is shown. In this case you can make use of the Target Relation dialog to get its parent resources and check whether the differences exist in the parent resources.
6. Select any of the following buttons to deal with the selected conflicting resource.
   Certain button is not activated for specific resource type.
   * **Rename** - Renames the resource and copies it to the target catalog with the new name.
   * **Replace** - Uses the resource from the source catalog to replace that in the target catalog. In this case, the reports that use this resource in the target catalog will be impacted.
   * **Skip** - Keeps the values in the target catalog for the resource. In this case, the report that uses this resource in the source catalog will be impacted.
7. Select the **Merge** button when all conflicts are settled. Logi JReport Designer then saves the report according to the changes you have made.

When two catalogs are merged via the Merge dialog, you may need to test all the reports in both catalogs to ensure they can work properly.

**Note:**Logi JReport Designer checks parameters based on the whole catalog. For example, assume that there is a parameter named Param1 in Data Source1 of the source catalog, and there is also a parameter named Param1 in Data Source2 in the target catalog. These two parameters in different data sources will be checked as a conflicting resource. You must rename the parameter in order to get a correct result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063201-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028562-Maintaining-Catalogs-with-the-Catalog-Doctor)
