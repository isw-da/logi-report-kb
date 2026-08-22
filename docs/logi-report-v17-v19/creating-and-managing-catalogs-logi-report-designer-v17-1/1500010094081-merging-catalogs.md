---
title: "Merging Catalogs"
id: 1500010094081
section: "Creating and Managing Catalogs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094081-Merging-Catalogs
updated_at: 2021-07-23T19:14:32Z
---

# Merging Catalogs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056662-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094101-Maintaining-Catalogs-with-the-Catalog-Doctor)

# Merging Catalogs

You can make two catalogs that have the same name merged by saving reports of one catalog to another directory in which a catalog of the same name already exists. This topic describes how you can merge two catalogs and deal with the differences between the catalogs.

When merging catalogs, Designer checks for the differences between the two catalogs, for example, resources that have the same mapping names in the two catalogs may conflict with each other because they have different property values. If there are differences between the two catalogs, based on the [Merge Catalog Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#MergeCat) setting in the Options dialog box, Designer either identifies them and prompts the Merge dialog box or ignores them and remains them in the target catalog. By default, Designer identifies the critical differences that can cause Logi Report Engine to fail in running reports and marks them in the Merge dialog box.

**To merge catalogs:**

1. Open a report in the catalog that you want to merge with another catalog.
2. Select **File** > **Save To**.
3. In the Save To dialog box, choose a directory to save the report, where a catalog with the same name as the current catalog already exists.

   If you set Merge Catalog Options as **Identify All Differences** or **Identify Critical Differences** in the Options dialog box and there are conflicting resources between the two catalogs, Designer displays the [Merge dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059742-Merge-Dialog-Box). The dialog box lists all the resources referenced by the report with the conflicting resources marked.

   ![Merge dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848513175/merge.gif)
4. Select a conflicting resource, then select the **Differences** button to view the differences of the resource between the source catalog and target catalog in the Property Differences dialog box.

   ![Property Differences dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857081367/ctlg_merge_prptydif.gif)

   Designer lists the property values of the conflicting resource from the two catalogs in the dialog box with any differences highlighted. You can use the Previous/Next button to go to the previous/next conflicting resource between the two catalogs.
5. To view the parent resources of the selected conflicting resource in the target catalog, select the **Target Relation** button. The Target Relation dialog box then appears showing the relation.

   ![Target Relation dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857081623/ctlg_merge_target.gif)

   Sometimes, a resource is marked in the Merge dialog box, but the Property Differences dialog box shows no difference. In this case, you can make use of the Target Relation dialog box to get its parent resources and check whether the differences exist in the parent resources.
6. Select any of the following buttons to deal with the selected conflicting resource.
   Certain button is not activated for specific resource type.
   * **Rename** - Renames the resource and copies it to the target catalog with the new name.
   * **Replace** - Uses the resource from the source catalog to replace that in the target catalog. This impacts the reports that use this resource in the target catalog.
   * **Skip** - Keeps the values in the target catalog for the resource. This impacts the report that uses this resource in the source catalog.
7. Select the **Merge** button after you settle all conflicts. Designer then saves the report according to the changes you have made.

After you merge two catalogs via the Merge dialog box, you may need to test all the reports in both catalogs to ensure they can work properly.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Designer checks parameters based on the whole catalog. For example, assume that there is a parameter named "Param1" in Data Source 1 of the source catalog, and there is also a parameter named "Param1" in Data Source 2 in the target catalog. Designer checks these two parameters in different data sources as a conflicting resource. You must rename the parameter in order to get a correct result.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010056662-Clarifying-the-Reference-Relationships-Between-Resources-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094101-Maintaining-Catalogs-with-the-Catalog-Doctor)
