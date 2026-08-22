---
title: "Saving a Catalog"
id: 1500009583221
section: "Creating and Managing Catalogs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583221-Saving-a-Catalog
updated_at: 2021-07-24T05:56:13Z
---

# Saving a Catalog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog)

# Saving a Catalog

To save a catalog, select **Save Catalog** on the Catalog Manager toolbar. The type, name, and location were specified when you [created the catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog).

You can also select either of the following on the File menu tab to save a catalog:

* **Save Catalog**  
   Saves the open catalog.
* **Save Catalog As**  
   Saves the open catalog in the selected alternate format. Options are .cat or .cat.xml. The .cat.xml file can be in the same directory as the .cat file. When you open the catalog in Designer, you can select either the .cat or the .cat.xml version; however, only the open one will be updated. If you publish the report to Logi JReport Server, be sure to publish only the updated one as the out of date one will likely produce errors when the user runs the report with the outdated catalog. It is best practice to keep only one version of the catalog once you decide which format you will use to publish.

A directory can contain only one catalog file other than the .cat and .cat.xml of the same catalog. To merge multiple catalog files, see [Merging Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009562762-Merging-Catalogs).

## Sharing Catalog Files Among Multiple Report Developers

By default, the report file and resources referenced by this report are created and saved in the current catalog. You can also save a report or other resource to a catalog other than the one in which it is created. All the catalog resources related to this report will then be merged into the catalog in the specified folder. This can allow a team of report developers to share resources. Each report developer can work on a local version of the catalog, and then use the Save To command to have his catalog merged into a universal catalog. The universal catalog must have the same name as the current catalog. The Save To command saves not only the report files, but also the resources (query, formulas, and parameters) that are referenced by this report. When there is a conflict, the report developer must decide which version to keep or modify has catalog to rename the conflicting resources and try the Save To again.

For details about how to share catalog files, see [Merging Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009562762-Merging-Catalogs) and [Saving a Page Report to a Different Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009571042-Saving-a-Page-Report#SaveTo).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog)
