---
title: "Managing Resources"
id: 1500009648782
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648782-Managing-Resources
updated_at: 2021-07-24T20:54:04Z
---

# Managing Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673361-Managing-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673621-Publishing-Resources)

# Managing Resources

Logi JReport Server provides a resource system for managing a group of archive versions that can be processed or organized. Generally, a resource refers to report or dashboard related material. To be exact, a resource in the Logi JReport Server reporting system is a conceptual node. There are different types of resources, such as catalogs, reports, dashboards, library components, and their results. A resource can only hold [versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009673701-Managing-Versions) of the same type.

**Logi JReport Server resource tree**

Resources on Logi JReport Server are organized into a folder-tree structure called the resource tree. Only the resources that are organized in the resource tree can be accessed and queried by a client. Logi JReport Server defines an XML file called admin.xml, and the resource tree conforms to this file. This file is maintained automatically by Logi JReport Server.

The following diagram shows the structure of the server resource tree.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926693783/mng_rsrc.gif)

The resource tree consists of the following three layers:

* **Folder layer:** Basic resource tree element that builds the main framework for the resource tree. There are four built-in folders in the root of the resource tree - My Components, Public Components, My Reports, and Public Reports. A folder can be mapped to a real file path.

  Public Reports and My Reports are two built-in folders in the resource tree root for storing resources such as reports, dashboards and analysis templates. You can create your own folders in either of them. The Public Reports folder and the My Reports folder cannot be deleted.

  The Public Reports folder contains public resources, and can be accessed by everyone. The My Reports folder is a personal folder. It contains personal resources. Each user has one personal folder, specified by the administrator when the user account is created. The My Reports folder can only be accessed by its owner, and the user has full control over his/her personal folder. This folder is the default output location for resources run by the user.

  Public Components and My Components are two built-in folders in the resource tree root for storing library components. Their behaviors resemble the Public Reports and My Reports folders.
* **Resource layer:** An abstract layer, based on the folder layer that hosts various types of archive versions and provides user access to the versions. In the Logi JReport Server resource tree, there are the following resource types:
  + **Catalogs**  
     A catalog stores all of the object definitions that are created while developing reports and library components, which include data source definitions, component customizations, style definitions, and more. Every report and library component must exist within the context of a catalog.
  + **Reports**There are two types of reports in Logi JReport: [page reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009649242-Page-Report-Studio) and [web reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009675101-Web-Report-Studio). A page report is a collection of report tabs and each report tab can have multiple pages. A web report is always displayed as a web layout report with just one page in a browser but can be printed with multiple pages. Logi JReport Server supports [running, advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009674661-Running-Reports) and [scheduling of reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009674681-Scheduling-Reports).
  + **Results**  
     When advanced running or scheduling a report to publish to the versioning system, you can choose an archive location to generate the report result. You can generate the report result in the built-in version folder, or in the resource tree. The report results generated in the resource tree are standalone results while those generated in the built-in version folder can only be bound with their respective reports.
  + **Library components**Library components are used to [build dashboards in JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009644602-JDashboard). They are able to present data via intuitive components such as charts, crosstabs, tables, and geographic maps. Library components are created and edited using Logi JReport Designer, and then are published to the component library on Logi JReport Server for use in dashboards.
  + **Dashboards**Dashboards created in JDashboard allow you to see the big picture by comparing charts, tables, and other components side-by-side.
  + **Analysis templates**Analysis templates are the data status saved via [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009667781-Visual-Analysis).
* **Archive layer:** A physical file layer, where the archive versions reside for executable resources, which function as the leaves of the resource tree. By default these archive version files are stored in the `<install_root>\history` folder. The structure of the resource tree is stored in the Logi JReport Server DBMS but only as pointers to the physical files located in the history folder. For more information, see [Managing Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009673701-Managing-Versions).

You can perform basic resource tasks such as publishing, deleting resources and changing resource properties, and more advanced tasks such as getting resources from a real path and using custom fields for the resources. Moreover, you can [secure your resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) by granting users different permissions.

**Note:** Catalogs are by default not displayed in the server resource tree on the Logi JReport Console page. In order to perform operations on catalogs published to Logi JReport Server on the Logi JReport Console page, you need to enable them to be displayed first by setting the web.page.option.show\_catalog property to true in the server.properties file. The recommended way is to use the Logi JReport Administration page. There are no operations you can do on a catalog other than setting permissions and deleting it.

This section includes the following topics:

* [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009673621-Publishing-Resources)
* [Searching for Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009673661-Searching-for-Resources)
* [Converting Resources of Earlier Versions into Current Version](https://devnet.logianalytics.com/hc/en-us/articles/1500009673581-Converting-Resources-of-Earlier-Versions-into-Current-Version)
* [Getting and Using Resources from a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/1500009648902-Getting-and-Using-Resources-from-a-Real-Path)
* [Customizing TTF Font Location for Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009648842-Customizing-TTF-Font-Location-for-Resources)
* [Working With Custom Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009648802-Working-with-Custom-Fields)
* [Changing Resource Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009673641-Changing-Resource-Properties)
* [Linking Resources and Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009648862-Linking-Resources-and-Catalogs)
* [Managing Dynamic Display Names of Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009648822-Managing-Dynamic-Display-Names-of-Business-View-Elements)
* [Deleting Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009673601-Deleting-Resources)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673361-Managing-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673621-Publishing-Resources)
