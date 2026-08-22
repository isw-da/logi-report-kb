---
title: "Sharing Web Reports"
id: 5741461964439
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports
updated_at: 2022-10-31T17:18:09Z
---

# Sharing Web Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741474194455-Linking-Resources-and-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741482130199-Automatically-Recompiling-Dynamic-Resources-in-Reports)

# Sharing Web Reports

Logi Report Server supports tenant level report sharing for web reports. This topic describes how you can share web reports to public folders and manage shared reports.

You can share your web reports that you created or added in the server resource tree, to public folders so that other users can work on the shared copies without touching the original reports. You can create multiple shared reports from one web report.

Server links a shared report to its original report. When you view a shared report, you can only access the business view that the shared report is referencing and edit the shared report based on the business views. Once you remove all the components that referenced a business view from a shared report and saved the shared report, the business view is no longer available.

![This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9905577570711/___newv19.2.png "New for version 19.2.")Administrators can view and remove other users' shared reports. For more information, see [Managing Users' Shared Reports](https://devnet.logianalytics.com/hc/en-us/articles/5741463728407-Managing-User-Accounts#SharedReport).

This topic contains the following sections:

* [Sharing a Web Report](#Share)
* [Managing Shared Web Reports](#Manage)

## Sharing a Web Report

You can share a web report either on the Server Console or [in Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741476487063-General-Operations-in-Web-Report#Share).

To share a web report from the Server Console.

1. In the Resources page of the Server Console, locate the web report in the resource tree, then select the **Share** button ![Share button](https://devnet.logianalytics.com/hc/article_attachments/9905616075543/btn_share.gif) on the floating toolbar. Or select the report row, right-click in the row, and select **Share** from the shortcut menu. Server displays the [Share Report dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741433695639-Share-Report-Dialog-Box-Properties).

   ![Share Report dialog](https://devnet.logianalytics.com/hc/article_attachments/9905714172311/shrpt.gif)
2. Select a public folder in which you want to save the shared report.
3. In the **File Name** text box, edit the file name of the shared report.
4. In the **Description** text box, you can type text to describe the shared report.
5. By default, Server selects **Allow Edit**. Clear it if you do not want anyone else to edit the shared report.

   When a shared report is editable, users who have the Edit permission on the shared report will be able to [run it using the Edit option](https://devnet.logianalytics.com/hc/en-us/articles/5741439314455-Running-Reports#Edit), edit it in Web Report Studio, and [save the modified report as a finished or unfinished version](https://devnet.logianalytics.com/hc/en-us/articles/5741464615703-Saving-a-Web-Report#Shared). Server stores the versions saved from a shared report into the original report so they are available in the [original report's version table](https://devnet.logianalytics.com/hc/en-us/articles/5741462114583-Browsing-Versions). If a user saves an unfinished version for a shared report and then runs the report, Server displays the unfinished version for the user to continue working on it. In other cases, running a shared report always means accessing its latest finished version which could be created by any user.
6. Select **OK** to accept the settings. Server adds the shared report in the specified folder.

## Managing Shared Web Reports

After you have shared your reports, you are able to view and manage them in the **My Shared** folder in the server resource tree root.

![My Shared Folder](https://devnet.logianalytics.com/hc/article_attachments/9905714213271/mng_rsc_shrpt1.gif)

You can view information such as which web reports you have used to create shared reports, where the reports are shared and under what names, the descriptions to introduce the shared reports, when you shared the reports, and when you modified them last time.

You can also edit the sharing properties of the reports and delete the shared reports.

To delete a shared report from the My Shared folder, take the steps as described in
[Deleting Resources](https://devnet.logianalytics.com/hc/en-us/articles/5741468382359-Deleting-Resources).

**To edit the sharing properties of a shared report:**

1. In the My Shared folder, do any of the following:
   * Put the mouse pointer over the report row and select the **Properties** button ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/9905657474071/btn_srv_prpty.gif) on its floating toolbar.
   * Select the report row, right-click in the report row and select **Properties** from the shortcut menu.
   * Select the report row and select **Tools** > **Properties** on the task bar.

   Server displays the [Sharing Properties dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741427772567-Sharing-Properties).

   ![Sharing Properties dialog](https://devnet.logianalytics.com/hc/article_attachments/9905714231063/shrprpty.gif)
2. Specify the values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/5741461739671-Working-with-Custom-Fields) if there are any.
3. To move the shared report to another directory in the server resource tree, select the ellipsis button ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/9905675890327/btn_chsr4.gif) next to the **Shared To** option.
4. Server displays the [Select Folder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741443524503-Select-Folder-Dialog-Box-Properties). Select a different folder in the server resource tree.
5. In the **Shared Resource Description** text box, you can edit the description.
6. Specify whether the shared report is editable.
7. Select **OK** to save the changes.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* You cannot use shared web reports as [linked reports](https://devnet.logianalytics.com/hc/en-us/articles/5741456004887-Adding-Links-in-Web-Report#Report).
* No one including the report owner can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741482629911-NLS-at-Report-Level#Local) for shared reports. Shared reports take the NLS settings of their original reports by default.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741474194455-Linking-Resources-and-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741482130199-Automatically-Recompiling-Dynamic-Resources-in-Reports)
