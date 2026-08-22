---
title: "Managing Resource Versions"
id: 5741462048023
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741462048023-Managing-Resource-Versions
updated_at: 2022-10-31T17:18:08Z
---

# Managing Resource Versions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741468382359-Deleting-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions)

# Managing Resource Versions

These resources in the server resource tree have versions: reports, report results, dashboards, library components, analysis templates, and catalogs. A large portion of resource management tasks concerns managing resource versions. This topic describes how you can manage resource version.

A version is the fundamental unit of the serve resource tree. Your resources might change over time. Server uses a versioning system to create and manage resources that have changed in content and properties owing to updates issued upon them.

To understand what the versioning system is, you have to understand the [resource mechanism](https://devnet.logianalytics.com/hc/en-us/articles/5741438016279-Managing-Resources) in Server as well. A resource in the Logi Report reporting system is a conceptual node, which holds a group of archive versions that you can process and organize in Server. Server saves information of these versions in the server system DB database, and saves version files in the `<install_root>\history` directory.

The versions in Server fall into the following major categories:

* **Catalog Version**  
   The versions of a catalog file.
* **Report Version**  
   The versions of a report file.
* **Report Result Version**  
   The versions of a report result file.
* **Dashboard Version**  
   The versions of a dashboard file.
* **Library Component Version**  
   The versions of a library component file.
* **Analysis Version**  
   The versions of an analysis template file.

Folders do not have versions.

If you check the property of a version, you can find its real path. For the report **Shipment Status Report.wls**, the report version's real path is  `<install_root>\history\1\Logi Report_System_User986775477\Shipment Status Report.wls`, which is the actual report result path on disk and stored in the server database. That is, when you select the **Shipment Status Report.wls** report resource in the server resource tree, you are accessing it on the disk, only Server stores its path in the database.
And this works the same for the other types of versions.

In addition, Server uses an archive policy to control the resource versions. You can control whether to use multiple versions for a specific resource. Also, you can define the maximum number of versions that can list in the version table. You can apply the archive policy to a single resource individually, or to many resources in a folder as a whole.

Select the following links to view the topics:

* [Creating Versions](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions)
* [Browsing Versions](https://devnet.logianalytics.com/hc/en-us/articles/5741462114583-Browsing-Versions)
* [Checking Version Properties](https://devnet.logianalytics.com/hc/en-us/articles/5741482415639-Checking-Version-Properties)
* [Applying an Archive Policy](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy)
* [Deleting Versions](https://devnet.logianalytics.com/hc/en-us/articles/5741468720791-Deleting-Versions)
* [Advanced Version Topics About Version Structure and Storage](https://devnet.logianalytics.com/hc/en-us/articles/5741462230423--Advanced-Version-Topics-About-Version-Structure-and-Storage)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741468382359-Deleting-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741462158487-Creating-Versions)
