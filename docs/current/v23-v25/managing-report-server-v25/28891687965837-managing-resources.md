---
title: "Managing Resources"
id: 28891687965837
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891687965837-Managing-Resources
updated_at: 2026-02-26T02:13:28Z
source_host: docs-report.zendesk.com
---
# 
Managing Resources 

Report Server provides a resource system for managing a group of archive versions that you can process or organize. This topic describes the server resource tree and server resources.

Generally, a resource in the Report Server reporting system is a conceptual node. It refers to report related material. There are different types of resources, such as catalogs, reports,  library components, dashboards, and analysis templates.

Report Server resource tree

Server organizes resources into a folder-tree structure called the resource tree. You can only access and query the resources in the resource tree. Server defines an XML file called admin.xml and automatically maintains it, and the resource tree conforms to this file.

The following diagram shows the structure of the server resource tree.

The resource tree consists of the following three layers:

- 
Folder layer: Basic resource tree element that builds the main framework for the resource tree. Server has built-in folders in the root of the resource tree - My Components, Public Components, My Reports, Public Reports, and My Shared. For organization users, there are two additional built-in folders, Organization Components and Organization Reports. You can map a folder to a real file path.
    Public Reports, Organization Reports, and My Reports are built-in folders in the resource tree root for storing resources such as reports, dashboards, and analysis templates. You can create your own folders in any of them. The Public Reports folder contains public resources and can be accessed by everyone. The Organization Reports folder is a public folder to organization users. The My Reports folder is a personal folder and contains personal resources that can be accessed by its owner only. Each user has one personal folder, specified by the administrator when the user account is created. A user has full control over his/her personal folder, and it is the default output location for resources run by the user.

Public Components, Organization Components, and My Components are built-in folders in the resource tree root for storing library components. Their behaviors resemble the Public Reports, Organization Reports, and My Reports folders. However, within the three folders and their sub folders Server allows only one catalog file.

My Shared is a built-in folder in the resource tree root for managing personal web reports that you share with others.

- 
Resource layer: An abstract layer, based on the folder layer that hosts various types of archive versions and provides user access to the versions. In the server resource tree, there are the following resource types:
    
- 
Catalogs
    A catalog stores all the object definitions that you created while developing reports and library components, which include data source definitions, component customizations, style definitions, and more. Every report and library component must exist within the context of a catalog.

- 
Reports
There are two types of reports in Report: page reports and web reports. A page report is a collection of report tabs and each report tab can have multiple pages. A web report is a web layout report with just one page in a browser but can print multiple pages. Server supports running, advanced running, and scheduling of reports.

- 
Results
  When advanced running or scheduling a report to publish to the versioning system, you can choose an archive location to generate the report result. You can generate the report result in the built-in version folder or in the resource tree. The report results generated in the resource tree are standalone results while those generated in the built-in version folder can only be bound with their respective reports.

- 
Library components
Library components are primary components to build dashboards in JDashboard. They are able to present data via intuitive components such as charts, crosstabs, tables, and geographic maps. You can create and edit library components using Report Designer, and then publish them to the component library on Report Server for use in dashboards.

- 
Dashboards
Dashboards that you created in JDashboard enable you to see the big picture by comparing charts, tables, and other components side-by-side.

- 
Analysis templates
Analysis templates are the data status you saved via Visual Analysis.

- 
Archive layer: A physical file layer, where the archive versions reside for executable resources, which function as the leaves of the resource tree. By default, Server stores these archive version files in the <install_root>\history folder. Server stores the structure of the resource tree in the Server DBMS but only as pointers to the physical files in the history folder. For more information, see Managing Resource Versions. 

Select the following links to view the topics:

- Publishing Resources

- Converting Resources of Earlier Versions to the Current Version

- Getting and Using Resources From a Real Path

- Customizing TTF Font Location for Resources

- Working With Custom Fields

- Changing Resource Properties

- Linking Resources and Catalogs

- Sharing Web Reports

- Managing Web Report Bookmarks

- Customizing Business Views for Reports

- Automatically Recompiling Dynamic Resources in Reports

- Managing Dynamic Display Names of Business View Elements

- Deleting Resources

In addition to the preceding tasks that you can perform when managing resources, you can also secure your resources by granting users different permissions, if you are an administrator.

Tips:

- In the Resources page of the Server Console, you can use the Search box to easily locate any resources including reports, catalogs, library components, dashboards, and folders in the server resource tree. To do this, browse to the folder you want in the server resource tree, then in the Search box type the text you want to search for, and Server lists the resources that contain the matched text.
 Server searches in the Name and Description columns of the Resources page. After typing text in the Search box, you can select  that appears in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select .

- You can customize the order and view mode of the resources in the Resources page of the Server Console. To do this, put the mouse over the corresponding button on the right of the Search box and select the required order or view mode from the drop-down menu.

- By default, Server does not display catalogs in the server resource tree for non-administrators. To show them for all users, set the property web.page.option.show_catalog in the server.properties file in <install_root>\bin to true.
