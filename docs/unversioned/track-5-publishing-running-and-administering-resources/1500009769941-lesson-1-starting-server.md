---
title: "Lesson 1: Starting Server"
id: 1500009769941
section: "Track 5: Publishing, Running, and Administering Resources"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009769941-Lesson-1-Starting-Server
updated_at: 2021-07-24T00:49:52Z
---

# Lesson 1: Starting Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009769921-Track-5-Publishing-Running-and-Administering-Resources)  Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)

# Lesson 1: Starting Server

In this lesson, you learn how to start Server, open the Server Console, and learn the other resource control commands available in the Server Console.

The Server Console has an easy-to-use web-based interface for selecting, viewing, and editing resources. Internet Explorer, Firefox, Google Chrome, Edge, and Safari are browsers that have been certified to work with the Logi Report products. Other browsers should also work fine.

The lesson assumes that you have installed Server with its default configuration. If you changed the default locations or port numbers using Custom Installation, you need to adjust the instructions in this lesson accordingly.

To start Server and access the Server Console locally, follow these steps:

1. Select **Start Server** in the Logi Report folder on the Start menu to start Server.
2. Server displays a welcome page automatically in your default web browser, and prompts you to provide your user name and password.
3. Type **admin** for the user name and **admin** for the password, then select **LOGIN**.

   These are the initial built-in user credentials on Server. One of the first things an administrator should do is to set up the correct user credentials, so that each user can access the appropriate reports.
4. Server displays the Start Page which provides quick entries to some key functions.

   ![Server Start Page](https://devnet.logianalytics.com/hc/article_attachments/4404885699735/admin_lsn1_startpg.gif)
5. Select **Public Folder** in the **Open** category to go to the public report directory in the Server Console.

   By default, Server hides the User Directory panel on the left, which shows the folders of the published resources available to the current login user.

   ![Server Console](https://devnet.logianalytics.com/hc/article_attachments/4404880718359/admin_lsn1_cnsl.gif)
6. Select **SampleReports**. Server displays the resource list, along with pertinent information.
7. Focus on any of the resource rows. Server displays a floating toolbar, which would contain all or some of the following commands, depending on the type of the resource:

   ![Resource Commands](https://devnet.logianalytics.com/hc/article_attachments/4404885700375/admin_lsn1_cntrl.gif)

   **Run**![Run button](https://devnet.logianalytics.com/hc/article_attachments/4404880717079/btn_run.gif)

   * For a report, you can use this command to run the report in the default format. If Web/Page Studio is the default format, Server opens a web report in the View Mode of Web Report Studio and a page report in the Basic View of Page Report Studio.
   * For a dashboard, you can use this command to run the dashboard in the view mode of JDashboard.
   * For a Visual Analysis template, you can use this command to run the template.

   **Advanced Run**![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4404880717847/btn_advrun.gif)

   You can use this command to run the report immediately after collecting additional specifications from you, including which report tab to run for a page report, what output format to use, which style group to apply, and any encoding options.

   **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404885700631/btn_edit.gif)

   * For a report, you can use this command to run the report in the default format. If Web/Page Studio is the default format, Server opens a web report in the Edit Mode of Web Report Studio and a page report in the Interactive View of Page Report Studio.
   * For a dashboard, you can use this command to run the dashboard in the edit mode of JDashboard.

   **Schedule**![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880715799/btn_schdl.gif)

   You can use this command to run the report based on a schedule. When you use Schedule to run a report, Server places the request into a queue and processes it in the submitted order. You can configure the size of the queue and priority of the queue to make the most efficient use of resources. [Lesson 4](https://devnet.logianalytics.com/hc/en-us/articles/1500009769981-Lesson-4-Scheduling-Reports) describes scheduled reports.

   **Version**![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404880716311/btn_vrsn.gif)

   You can use this command to view the resource version and scheduled/advanced run result version information.

   **Properties**![Properties button](https://devnet.logianalytics.com/hc/article_attachments/4404880713879/btn_prpty.gif)

   You can use this command to define the archive policy, security, and a description associated with the resource. [Lesson 6](https://devnet.logianalytics.com/hc/en-us/articles/1500009770041-Lesson-6-Security) describes security.

   **Parameter Settings**![Parameter Settings button](https://devnet.logianalytics.com/hc/article_attachments/4404880718615/btn_prm.gif)

   You can use this command to customize the default parameter values for the report.

   **NLS Editor**![Parameter Settings button](https://devnet.logianalytics.com/hc/article_attachments/4404885700887/btn_nlsedtr.gif)

   You can use this command to translate a report or dashboard into another language.

   **Share**![Share button](https://devnet.logianalytics.com/hc/article_attachments/4404880719127/btn_share.gif)

   You can use this command to share a web report added by you in the server resource tree with other users.

   **Delete**![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404880719383/btn_delete.gif)

   You can use this command to delete the resource.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009769921-Track-5-Publishing-Running-and-Administering-Resources)  Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)
