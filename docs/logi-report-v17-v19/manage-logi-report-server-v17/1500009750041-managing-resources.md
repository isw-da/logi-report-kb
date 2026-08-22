---
title: "Managing Resources"
id: 1500009750041
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750041-Managing-Resources
updated_at: 2021-07-25T07:18:59Z
---

# Managing Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722982-Managing-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources)

# Managing Resources

Logi Report Server provides a resource system for managing a group of archive versions that can be processed or organized. Generally, a resource in the Logi Report Server reporting system is a conceptual node. It refers to report related material. There are different types of resources, such as catalogs, reports, library components, dashboards and analysis templates.

**Logi Report Server resource tree**

Resources on Logi Report Server are organized into a folder-tree structure called the resource tree. Only the resources that are organized in the resource tree can be accessed and queried by a client. Logi Report Server defines an XML file called admin.xml, and the resource tree conforms to this file. This file is maintained automatically by Logi Report Server.

The following diagram shows the structure of the server resource tree.

![Server Resource Tree](https://devnet.logianalytics.com/hc/article_attachments/4404942506903/mng_rsc.gif)

The resource tree consists of the following three layers:

* **Folder layer:** Basic resource tree element that builds the main framework for the resource tree. Logi Report Server has built-in folders in the root of the resource tree - My Components, Public Components, My Reports, Public Reports and My Shared. For [organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations) users, there are two additional built-in folders, Organization Components and Organization Reports. A folder can be mapped to a real file path.

  Public Reports, Organization Reports and My Reports are built-in folders in the resource tree root for storing resources such as reports, dashboards and analysis templates. You can create your own folders in any of them. The Public Reports folder contains public resources, and can be accessed by everyone. The Organization Reports folder is a public folder to organization users. The My Reports folder is a personal folder. It contains personal resources that can be accessed by its owner only. Each user has one personal folder, specified by the administrator when the user account is created. A user has full control over his/her personal folder and it is the default output location for resources run by the user.

  Public Components, Organization Components and My Components are built-in folders in the resource tree root for storing library components. Their behaviors resemble the Public Reports, Organization Reports and My Reports folders. However within the three folders and their subfolders only one catalog file can be stored.

  My Shared is a built-in folder in the resource tree root for managing personal web reports that are shared.
* **Resource layer:** An abstract layer, based on the folder layer that hosts various types of archive versions and provides user access to the versions. In the Logi Report Server resource tree, there are the following resource types:
  + **Catalogs**  
     A catalog stores all of the object definitions that are created while developing reports and library components, which include data source definitions, component customizations, style definitions, and more. Every report and library component must exist within the context of a catalog.
  + **Reports**  
    There are two types of reports in Logi Report: [page reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009723302-Page-Report-Studio) and [web reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009724642-Web-Report-Studio). A page report is a collection of report tabs and each report tab can have multiple pages. A web report is always displayed as a web layout report with just one page in a browser but can be printed with multiple pages. Logi Report Server supports [running, advanced running](https://devnet.logianalytics.com/hc/en-us/articles/1500009724222-Running-Reports) and [scheduling of reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009751081-Scheduling-Reports).
  + **Results**  
     When advanced running or scheduling a report to publish to the versioning system, you can choose an archive location to generate the report result. You can generate the report result in the built-in version folder, or in the resource tree. The report results generated in the resource tree are standalone results while those generated in the built-in version folder can only be bound with their respective reports.
  + **Library components**  
    Library components are used to [build dashboards in JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009744981-JDashboard). They are able to present data via intuitive components such as charts, crosstabs, tables, and geographic maps. Library components are created and edited using Logi Report Designer, and then are published to the component library on Logi Report Server for use in dashboards.
  + **Dashboards**  
    Dashboards created in JDashboard allow you to see the big picture by comparing charts, tables, and other components side-by-side.
  + **Analysis templates**  
    Analysis templates are the data status saved via [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009718222-Using-Visual-Analysis-to-Analyze-Data-Intuitively-and-Instantly-Logi-Report-Server-v17).
* **Archive layer:** A physical file layer, where the archive versions reside for executable resources, which function as the leaves of the resource tree. By default these archive version files are stored in the `<install_root>\history` folder. The structure of the resource tree is stored in the Logi Report Server DBMS but only as pointers to the physical files located in the history folder. For more information, see [Managing Versions](https://devnet.logianalytics.com/hc/en-us/articles/1500009750181-Managing-Versions).

This section details the following resource topics:

* [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources)
* [Converting Resources of Earlier Versions Into Current Version](https://devnet.logianalytics.com/hc/en-us/articles/1500009750061-Converting-Resources-of-Earlier-Versions-into-Current-Version)
* [Getting and Using Resources From a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path)
* [Customizing TTF Font Location for Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009723102-Customizing-TTF-Font-Location-for-Resources)
* [Working With Custom Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009723042-Working-with-Custom-Fields)
* [Changing Resource Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009723122-Changing-Resource-Properties)
* [Linking Resources and Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009750081-Linking-Resources-and-Catalogs)
* [Sharing Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports)
* [Automatically Recompiling Dynamic Resources in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009750121-Automatically-Recompiling-Dynamic-Resources-in-Reports)
* [Managing Dynamic Display Names of Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements)
* [Deleting Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009723062-Deleting-Resources)

In addition to the above tasks that you can perform when managing resources, you can also [secure your resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) by granting users different permissions.

**Tips:**

* In the Resources page of the Logi Report Server console, you can use the Search box to easily locate any resources including reports, catalogs, library components, dashboards and folders in the server resource tree. To do this, browse to the desired folder in the server resource tree, then in the Search box type the text you want to search for and the resources containing the matched text will be listed.
  Logi Report Server searches in the Name and Description columns of the Resources page. After typing text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404936733463/btn_mvdown1.gif) that appears in the box to specify the following search options: Highlight All, Match Case and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404942446871/btn_dltobj.gif).
* The order and view mode in which the resources in the Resources page of the Logi Report Server console can be customized. To do this, put the mouse over the corresponding button on the right of the Search box and select the required order or view mode from the drop-down menu.
* By default, catalogs are not displayed in the server resource tree for non-admin users. To make them shown for all users, the property web.page.option.show\_catalog in the server.properties file located in `<install_root>\bin` should be set to true.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722982-Managing-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources)
