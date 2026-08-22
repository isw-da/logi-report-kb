---
title: "Lesson 1: Starting Logi JReport Server"
id: 1500011431562
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011431562-Lesson-1-Starting-Logi-JReport-Server
updated_at: 2021-07-24T10:39:43Z
---

# Lesson 1: Starting Logi JReport Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011431582-Track-5-Publishing-Running-and-Administering-Resources) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901097111/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431542-Lesson-2-Publishing-Resources)

# Lesson 1: Starting Logi JReport Server

In this lesson, you will learn how to start Logi JReport Server, open the Logi JReport Server console, and learn the other resource control commands available on the server console.

The Logi JReport Server console has an easy-to-use web-based interface for selecting, viewing and editing resources. Internet Explorer, Firefox, Google Chrome, Edge, and Safari are browsers that have been certified to work with Logi JReport products. Other browsers should also work fine.

The lesson assumes that you have installed Logi JReport Server with its default configuration. If you changed the default locations or port numbers using Custom Installation, then you will need to adjust the instructions in this lesson accordingly.

To start Logi JReport Server and access the server console locally, follow these steps:

1. Select **Start Server** in the JReport folder on the Start menu to start Logi JReport Server.
2. A welcome page is automatically displayed in your default web browser, prompting you to provide your user name and password. Enter **admin** for the user name and **admin** for the password, then select **LOGIN**.

   These are the initial user credentials built-in to Logi JReport Server. One of the first things an administrator should do is to set up the correct user credentials so that appropriate reports can be accessed by each user.
3. The Logi JReport Server Start Page is displayed which provides quick entries to some key functions of Logi JReport Server.

   ![Server Start Page](https://devnet.logianalytics.com/hc/article_attachments/4404901107351/admin_lsn1_startpg.gif)
4. Select **Public Folder**  in the Open category to go to the public report directory in the server console.

   By default, the User Directory panel is hidden on the left showing the folders of published resources that are available to the current login user.

   ![Server Console](https://devnet.logianalytics.com/hc/article_attachments/4404901107607/admin_lsn1_cnsl.gif)
5. Select **SampleReports**. The resource list, along with pertinent information, is displayed.
6. Focus on any of the resource rows, a floating toolbar is then displayed, which would contain all or some of the following commands, depending on the type of the resource:

   ![Resource Commands](https://devnet.logianalytics.com/hc/article_attachments/4404901107863/admin_lsn1_cntrl.gif)

   **Run**![Run button](https://devnet.logianalytics.com/hc/article_attachments/4404909108247/btn_run.gif)

   * Runs the report in the default format. If Web/Page Studio is the default format, a web report will be opened in the View Mode of Web Report Studio and a page report in the Basic View of Page Report Studio.
   * Runs the dashboard in the view mode of JDashboard.
   * Runs the Visual Analysis template.

   **Advanced Run**![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4404901106327/btn_advrun.gif)  
    Runs the report immediately after collecting additional specifications from you, including which report tab to run for a page report, what output format to use, which style group to apply, and any encoding options.

   **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404909109783/btn_edit.gif)

   * Runs the report in the default format. If Web/Page Studio is the default format, a web report will be opened in the Edit Mode of Web Report Studio and a page report in the Interactive View of Page Report Studio.
   * Runs the dashboard in the edit mode of JDashboard.

   **Schedule**![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404909107735/btn_schdl.gif)  
    Runs the report based on a schedule. When you use Schedule to run a report, the request is placed into a queue and processed in the order submitted. The size of the queue and priority of the queue can be configured to make the most efficient use of resources. [Lesson 4](https://devnet.logianalytics.com/hc/en-us/articles/1500011463561-Lesson-4-Scheduling-Reports) describes scheduled reports.

   **Version**![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404901104791/btn_vrsn.gif)  
    Views the resource version and scheduled/advanced run result version information.

   **Properties**![Properties button](https://devnet.logianalytics.com/hc/article_attachments/4404909107479/btn_prpty.gif)  
    Allows you to define the archive policy, security, and a description associated with the resource. [Lesson 6](https://devnet.logianalytics.com/hc/en-us/articles/1500011463541-Lesson-6-Security) describes security.

   **Parameter Settings**![Parameter Settings button](https://devnet.logianalytics.com/hc/article_attachments/4404909110039/btn_prm.gif)  
    Customizes the default parameter values for the report.

   **NLS Editor**![Parameter Settings button](https://devnet.logianalytics.com/hc/article_attachments/4404901108119/btn_nlsedtr.gif)  
    Translates a report or dashboard into another language.

   **Share**![Share button](https://devnet.logianalytics.com/hc/article_attachments/4404909110295/btn_share.gif)  
    Shares a web report added by you in the server resource tree with other users.

   **Delete**![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404901108375/btn_delete.gif)  
    Deletes the resource.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011431582-Track-5-Publishing-Running-and-Administering-Resources) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901097111/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431542-Lesson-2-Publishing-Resources)
