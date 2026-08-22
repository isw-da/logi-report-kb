---
title: "Managing Versions"
id: 1500009673701
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673701-Managing-Versions
updated_at: 2021-07-24T20:54:00Z
---

# Managing Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673601-Deleting-Resources)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions)

# Managing Versions

All the resources in the server resource tree: reports, report results, dashboards, library components, analysis templates, and catalogs, are controlled by versions. A version is the fundamental unit of the resource tree, and your resources might change over time. Logi JReport Server uses a versioning system to create and manage resources that have changed in content and properties owing to updates issued upon them. All the resources in the resource tree have versions. A large portion of resource management tasks are done by managing resource versions.

To understand what the versioning system is, you have to understand the [resource mechanism](https://devnet.logianalytics.com/hc/en-us/articles/1500009648782-Managing-Resources) in Logi JReport Server as well. A resource in the Logi JReport reporting system is a conceptual node, which holds a group of archive versions that can be processed or organized in Logi JReport Server. Information of these versions is stored in the system DB database that Logi JReport Server uses, while version files are saved in the directory -  `<install_root>\history`.

The versions in Logi JReport Server fall into the following major categories:

* **Catalog Version**  
   The version of a catalog file.
* **Report Version**  
   The version of a report file.
* **Report Result Version**  
   The version of a report result file.
* **Dashboard Version**  
   The version of a dashboard file.
* **Library Component Version**  
   The version of a library component file.
* **Analysis Version**  
   The version of an analysis template file.

If you check the property of a version, you can find its real path. Remember that version information is stored to a database, and version files are stored in the directory  `<install_root>\history`. For the report InvoiceReport.cls, the report version's real path is  `<install_root>\history\1\Logi JReport_System_User894485281\InvoiceReport.cls`, which is the actual report result path on disk and stored in the server database. That is, when you select the InvoiceReport.cls report resource in the server resource tree, you are accessing it on the disk, only the path to it is stored in the database.
And this works the same for the other types of versions.

In addition, Logi JReport Server uses an archive policy to control the resource versions. You can control whether or not to use multiple versions for a specific resource. Also, you can define the maximum number of versions that can be listed in the version table. The archive policy can be applied to a single resource individually, or to many resources in a folder as a whole.

This section shows how to manage resource versions as follows:

* [Creating Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions)
* [Browsing Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions)
* [Checking Version Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009673781-Checking-Version-Properties)
* [Applying an Archive Policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy)
* [Deleting Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009673761-Deleting-Versions)
* [Advanced Version Topics](https://devnet.logianalytics.com/hc/en-us/articles/1500009673801-Advanced-Version-Topics)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673601-Deleting-Resources)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649002-Creating-Versions)
