---
title: "Managing Resources"
id: 4405683925143
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683925143-Managing-Resources
updated_at: 2022-01-27T07:59:38Z
---

# Managing Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683921559-Managing-Logi-Report-Server-v18)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources)

# Managing Resources

Logi Report Server provides a resource system for managing a group of archive versions that you can process or organize. This topic describes the server resource tree and server resources.

Generally, a resource in the Logi Report Server reporting system is a conceptual node. It refers to report related material. There are different types of resources, such as catalogs, reports, library components, dashboards, and analysis templates.

**Logi Report Server resource tree**

Server organizes resources into a folder-tree structure called the resource tree. You can only access and query the resources in the resource tree. Server defines an XML file called admin.xml and automatically maintains it, and the resource tree conforms to this file.

The following diagram shows the structure of the server resource tree.

![Server Resource Tree](https://devnet.logianalytics.com/hc/article_attachments/4420453525399/mng_rsc.gif)

The resource tree consists of the following three layers:

* **Folder layer:** Basic resource tree element that builds the main framework for the resource tree. Server has built-in folders in the root of the resource tree - My Components, Public Components, My Reports, Public Reports, and My Shared. For [organization](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations) users, there are two additional built-in folders, Organization Components and Organization Reports. You can map a folder to a real file path.

  Public Reports, Organization Reports, and My Reports are built-in folders in the resource tree root for storing resources such as reports, dashboards, and analysis templates. You can create your own folders in any of them. The Public Reports folder contains public resources and can be accessed by everyone. The Organization Reports folder is a public folder to organization users. The My Reports folder is a personal folder and contains personal resources that can be accessed by its owner only. Each user has one personal folder, specified by the administrator when the user account is created. A user has full control over his/her personal folder, and it is the default output location for resources run by the user.

  Public Components, Organization Components, and My Components are built-in folders in the resource tree root for storing library components. Their behaviors resemble the Public Reports, Organization Reports, and My Reports folders. However, within the three folders and their sub folders Server allows only one catalog file.

  My Shared is a built-in folder in the resource tree root for managing personal web reports that you share with others.
* **Resource layer:** An abstract layer, based on the folder layer that hosts various types of archive versions and provides user access to the versions. In the server resource tree, there are the following resource types:
  + **Catalogs**  
     A catalog stores all the object definitions that you created while developing reports and library components, which include data source definitions, component customizations, style definitions, and more. Every report and library component must exist within the context of a catalog.
  + **Reports**  
    There are two types of reports in Logi Report: [page reports](https://devnet.logianalytics.com/hc/en-us/articles/4405683949591-Page-Report-Studio-Server-v18) and [web reports](https://devnet.logianalytics.com/hc/en-us/articles/4405684031639-Web-Report-Studio-Server-v18). A page report is a collection of report tabs and each report tab can have multiple pages. A web report is a web layout report with just one page in a browser but can print multiple pages. Server supports [running, advanced running](https://devnet.logianalytics.com/hc/en-us/articles/4405690675223-Running-Reports), and [scheduling of reports](https://devnet.logianalytics.com/hc/en-us/articles/4405690676119-Scheduling-Reports).
  + **Results**  
     When advanced running or scheduling a report to publish to the versioning system, you can choose an archive location to generate the report result. You can generate the report result in the built-in version folder or in the resource tree. The report results generated in the resource tree are standalone results while those generated in the built-in version folder can only be bound with their respective reports.
  + **Library components**  
    Library components are primary components to [build dashboards in JDashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405683592471-Introduction-to-the-Logi-Report-JDashboard-Logi-Report-Server-v18). They are able to present data via intuitive components such as charts, crosstabs, tables, and geographic maps. You can create and edit library components using Logi Report Designer, and then publish them to the component library on Logi Report Server for use in dashboards.
  + **Dashboards**  
    Dashboards that you created in JDashboard enable you to see the big picture by comparing charts, tables, and other components side-by-side.
  + **Analysis templates**  
    Analysis templates are the data status you saved via [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/4405683536023-Using-Visual-Analysis-to-Analyze-Data-Intuitively-and-Instantly-Server-v18).
* **Archive layer:** A physical file layer, where the archive versions reside for executable resources, which function as the leaves of the resource tree. By default, Server stores these archive version files in the `<install_root>\history` folder. Server stores the structure of the resource tree in the Server DBMS but only as pointers to the physical files in the history folder. For more information, see [Managing Resource Versions](https://devnet.logianalytics.com/hc/en-us/articles/4405683938455-Managing-Resource-Versions).

Select the following links to view the topics:

* [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources)
* [Converting Resources of Earlier Versions to the Current Version](https://devnet.logianalytics.com/hc/en-us/articles/4405683926807-Converting-Resources-of-Earlier-Versions-to-the-Current-Version)
* [Getting and Using Resources From a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/4405690643479-Getting-and-Using-Resources-From-a-Real-Path)
* [Customizing TTF Font Location for Resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683930903-Customizing-TTF-Font-Location-for-Resources)
* [Working With Custom Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405683927831-Working-with-Custom-Fields)
* [Changing Resource Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties)
* [Linking Resources and Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/4405683931927-Linking-Resources-and-Catalogs)
* [Sharing Web Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405683936279-Sharing-Web-Reports)
* [Automatically Recompiling Dynamic Resources in Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405683934999-Automatically-Recompiling-Dynamic-Resources-in-Reports)
* [Customizing Business Views for Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405690642327-Customizing-Business-Views-for-Reports)
* [Managing Dynamic Display Names of Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/4405683929879-Managing-Dynamic-Display-Names-of-Business-View-Elements)
* [Deleting Resources](https://devnet.logianalytics.com/hc/en-us/articles/4405683928855-Deleting-Resources)

In addition to the preceding tasks that you can perform when managing resources, you can also [secure your resources](https://devnet.logianalytics.com/hc/en-us/articles/4405684023831-Managing-Permissions) by granting users different permissions, if you are an administrator.

**Tips:**

* In the Resources page of the Server Console, you can use the Search box to easily locate any resources including reports, catalogs, library components, dashboards, and folders in the server resource tree. To do this, browse to the desired folder in the server resource tree, then in the Search box type the text you want to search for, and Server lists the resources that contain the matched text.
  Server searches in the Name and Description columns of the Resources page. After typing text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4420453419415/btn_mvdown1.gif) that appears in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4420461456151/btn_dltobj.gif).
* You can customize the order and view mode of the resources in the Resources page of the Server Console. To do this, put the mouse over the corresponding button on the right of the Search box and select the required order or view mode from the drop-down menu.
* By default, Server does not display catalogs in the server resource tree for non-administrators. To show them for all users, set the property **web.page.option.show\_catalog** in the **server.properties** file in `<install_root>\bin` to **true**.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683921559-Managing-Logi-Report-Server-v18)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683932951-Publishing-Resources)
