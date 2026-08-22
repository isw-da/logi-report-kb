---
title: "Sharing Web Reports"
id: 1500009777281
section: "Managing Resources"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777281-Sharing-Web-Reports
updated_at: 2021-07-24T00:47:58Z
---

# Sharing Web Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777221-Linking-Resources-and-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748722-Automatically-Recompiling-Dynamic-Resources-in-Reports)

# Sharing Web Reports

Logi Report Server supports tenant level report sharing for web reports. This topic describes how you can share web reports to public folders and manage shared reports.

You can share your web reports that you created or added in the server resource tree, to public folders so that other users can work on the shared copies without touching the original reports. You can create multiple shared reports from one web report.

Server links a shared report to its original report. When you view a shared report, you can only access the business view that the shared report is referencing and edit the shared report based on the business views. Once you removed all the components that referenced a business view from a shared report and saved the shared report, the business view is no longer available.

This topic contains the following sections:

* [Sharing a Web Report](#Share)
* [Managing Shared Web Reports](#Manage)

## Sharing a Web Report

You can share a web report either in the Server Console or [in Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009778761-General-Operations-in-Web-Report#Share).

To share a web report from the Server Console.

1. In the Resources page of the Server Console, locate the web report in the resource tree, then select the **Share** button ![Share button](https://devnet.logianalytics.com/hc/article_attachments/4404880137879/btn_share.gif) on the floating toolbar, or select the report row, right-click in the row and select **Share** from the shortcut menu. Server displays the [Share Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009746362-Share-Report-Dialog-Box-Properties) dialog box.

   ![Share Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885410839/shrpt.gif)
2. Select a public folder in which you want to save the shared report.
3. In the **File Name** text box, edit the file name of the shared report.
4. In the **Description** text box, you can type text to describe the shared report.
5. By default, Server selects the **Allow Edit** check box. Clear it if you do not want anyone else to edit the shared report.

   When a shared report is editable, users who have the Edit permission on the shared report will be able to [run it using the Edit option](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports#Edit), edit it in Web Report Studio, and [save the modified report as a finished or unfinished version](https://devnet.logianalytics.com/hc/en-us/articles/1500009750182-Saving-a-Web-Report#Shared). Saves stores the versions saved from a shared report into the original report so they are available in the [original report's version table](https://devnet.logianalytics.com/hc/en-us/articles/1500009748762-Browsing-Versions). If a user saves an unfinished version for a shared report and then runs the report, Server displays the unfinished version for the user to continue working on it. In other cases, running a shared report always means accessing its latest finished version which could be created by any user.
6. Select **OK** to accept the settings. Server adds the shared report in the specified folder.

## Managing Shared Web Reports

After you have shared your reports, you are able to view and manage them in the **My Shared** folder in the server resource tree root.

![My Shared Folder](https://devnet.logianalytics.com/hc/article_attachments/4404880288023/mng_rsc_shrpt1.gif)

You can view information such as which web reports you have used to create shared reports, where the reports are shared and under what names, the descriptions to introduce the shared reports, when you shared the reports, and when you modified them last time.

You can also edit the sharing properties of the reports and delete them.

To delete a shared report from the My Shared folder, take the steps as described in
[Deleting Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009748682-Deleting-Resources).

**To edit the sharing properties of a shared report:**

1. In the My Shared folder, do any of the following:
   * Put the mouse pointer over the report row and select the **Properties** button ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/4404885407255/btn_srv_prpty.gif) on its floating toolbar.
   * Select the report row, right-click in the report row and select **Properties** from the shortcut menu.
   * Select the report row and select **Tools** > **Properties** on the task bar.

   Server displays the [Sharing Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009774621-Sharing-Properties) dialog box.

   ![Sharing Properties dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885411095/shrprpty.gif)
2. Specify the values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009748662-Working-with-Custom-Fields) if there are any.
3. To move the shared report to another directory in the server resource tree, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404885411479/btn_chsr4.gif) next to the **Shared To** option.
4. Server displays the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009746422-Select-Folder-Dialog-Box-Properties) dialog box. Select a different folder in the server resource tree.
5. In the **Shared Resource Description** text box, you can edit the description.
6. Specify whether the shared report is editable.
7. Select **OK** to save the changes.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* You cannot use shared web reports as [linked reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009778801-Adding-Links-in-Web-Report#Report).
* No user including the report owner can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009777481-NLS-at-Report-Level#Local) for shared reports. Shared reports take the NLS settings of their original reports by default.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777221-Linking-Resources-and-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748722-Automatically-Recompiling-Dynamic-Resources-in-Reports)
