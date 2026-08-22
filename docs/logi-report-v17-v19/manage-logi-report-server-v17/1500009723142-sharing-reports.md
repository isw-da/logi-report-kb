---
title: "Sharing Reports"
id: 1500009723142
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports
updated_at: 2021-07-25T07:18:57Z
---

# Sharing Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750081-Linking-Resources-and-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750121-Automatically-Recompiling-Dynamic-Resources-in-Reports)

# Sharing Reports

Logi Report Server supports tenant level report sharing for web reports, which allows the web report owners to share their reports to a public folder so that other users can work on the shared copy without touching the original reports. The owner of a report is the user who added the report in the server resource tree, for instance the creator of the report. The report owner can create multiple shared reports from one web report.

Shared reports are linked to the original report. When users view a shared report, they can only access the business view that are referenced by the shared report and edit the shared report based on the business views. Once all the components that reference a business view are removed from a shared report, the business view will not be available after the shared report is saved.

Select the following links to view the topics:

* [Sharing a Web Report](#Share)
* [Managing Shared Web Reports](#Manage)

## Sharing a Web Report

A web report can be shared either in the Logi Report Server console or [in Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/1500009724782-General-Operations-in-a-Report#Share). The following shows sharing a web report from the server console.

1. In the Resources page of the Logi Report Server console, locate the report in the resource tree, then select the **Share** button ![Share button](https://devnet.logianalytics.com/hc/article_attachments/4404936716055/btn_share.gif) on the floating toolbar, or select the report row, right-click in the row and select **Share** from the shortcut menu. Report Server displays the [Share Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009747881-Share-Report) dialog box.

   ![Share Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936797847/shrpt.gif)
2. Select the folder in which to save the shared report.
3. In the File Name text box, provide the file name of the shared report.
4. In the Description text box, you can type text to describe the shared report.
5. By default the Allow Edit check box is selected. If you don't want anyone else to edit the shared report, clear it.

   When a shared report is editable, users who have the Edit permission on the shared report will be able to [run it using the Edit option](https://devnet.logianalytics.com/hc/en-us/articles/1500009724222-Running-Reports#Edit), edit it in Web Report Studio and [save the modified report as a finished or unfinished version](https://devnet.logianalytics.com/hc/en-us/articles/1500009751541-Saving-the-Report#Shared). The versions saved from a shared report will be stored into the original report so they are available in the [original report's version table](https://devnet.logianalytics.com/hc/en-us/articles/1500009750201-Browsing-Versions). If a user saves an unfinished version for a shared report and then runs the report, the unfinished version will be displayed for the user to continue working on it. In other cases, running a shared report always means accessing its latest finished version which could be created by any user.
6. Select **OK** to accept the settings. The shared report is then added in the specified folder.

## Managing Shared Web Reports

After you have shared your reports, you are able to view and manage them in the My Shared folder in the server resource tree root.

![My Shared Folder](https://devnet.logianalytics.com/hc/article_attachments/4404936798103/mng_rsc_shrpt1.gif)

You can view information such as which web reports have been used to create shared reports, where the reports are shared and under what names, the descriptions added to introduce the shared reports, and at what time the reports were shared and last modified.

You can also edit the sharing properties of the reports and delete them.

* **To edit the sharing properties of a shared report:**
  1. In the My Shared folder, do any of the following:
     + Put the mouse pointer over the report row and select the **Properties** button ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/4404942500503/btn_srv_prpty.gif) on its floating toolbar.
     + Select the report row, right-click in the report row and select **Properties** from the shortcut menu.
     + Select the report row and select **Tools** > **Properties** on the task bar.

     Report Server displays the [Sharing Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009747861-Sharing-Properties) dialog box.

     ![Sharing Properties dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936798359/shrprpty.gif)
  2. Specify the values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009723042-Working-with-Custom-Fields) if there are any.
  3. To move the shared report to another directory in the server resource tree, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404936798615/btn_chsr4.gif) next to the Shared To option, then in the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009747961-Select-Folder) dialog box select a different folder in the server resource tree.
  4. In the Shared Resource Description text box, you can edit the description.
  5. Specify whether the shared report is editable.
  6. Select **OK** to save the changes.
* To delete a shared report from the My Shared folder, take the steps as described in
  [Deleting Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009723062-Deleting-Resources).

**Notes:**

* Shared web reports cannot be used as [linked reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009724822-Adding-Links-in-a-Report#Report).
* No user including the report owner can [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level#Local) for shared reports. Shared reports will take the NLS settings of their original reports by default.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750081-Linking-Resources-and-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750121-Automatically-Recompiling-Dynamic-Resources-in-Reports)
