---
title: "Lesson 1: Starting Logi JReport Server"
id: 1500009582241
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582241-Lesson-1-Starting-Logi-JReport-Server
updated_at: 2021-07-24T05:56:28Z
---

# Lesson 1: Starting Logi JReport Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009561802-Track-5-Publishing-Running-and-Administering-Resources) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009561822-Lesson-2-Publishing-Resources)

# Lesson 1: Starting Logi JReport Server

In this topic, you will learn how to start Logi JReport Server, open the Logi JReport Server user console, and learn the other resource control commands available on the user console.

The Logi JReport Server user console has an easy-to-use web-based interface for selecting, viewing and editing resources. Internet Explorer, Firefox, Google Chrome, Edge, and Safari are browsers that have been certified to work with Logi JReport products. However other browsers should also work fine.

The lesson assumes that you have installed Logi JReport Server with its default configuration. If you changed the default locations or port numbers using Custom Installation, then you will need to adjust the instructions in this lesson accordingly.

To start Logi JReport Server and access the user console locally, follow these steps:

1. Select **Start** > **Logi JReport 15** > **Start Server** to start Logi JReport Server.
2. The Welcome to Logi JReport page is automatically displayed on your default web browser. Enter **admin** for the user name and **admin** for the password, then select **Login**.

   These are the initial user credentials built-in to Logi JReport Server. One of the first things an administrator should do is to set up the correct user credentials so that appropriate reports can be accessed by each user.
3. The Logi JReport Server Start Page is displayed which provides quick entries to some key functions of Logi JReport Server.

   ![Server Start Page](https://devnet.logianalytics.com/hc/article_attachments/4404889459095/admin_lsn1_startpg.gif)
4. Select **Public Reports** in the Open category to go to the public report directory on the user console.

   By default, the User Directory panel is hidden on the left showing the folders of published resources that are available to the current login user.

   ![User Console](https://devnet.logianalytics.com/hc/article_attachments/4404889459351/admin_lsn1_cnsl.gif)
5. Select **SampleReports**. The resource list, along with pertinent information, is displayed.
6. Focus on any of the resource rows, a floating toolbar is then displayed, which would contain all or some of the following commands, depending on the type of the resource:

   ![Resource Commands](https://devnet.logianalytics.com/hc/article_attachments/4404889459607/admin_lsn1_cntrl.gif)

   **Run**![Run button](https://devnet.logianalytics.com/hc/article_attachments/4404894053015/btn_run.gif)

   * Runs the report in the default format. If Report Studio is the default format, a web report will be opened in the View Mode of Web Report Studio and a page report in the Basic View of Page Report Studio.
   * Runs the dashboard in the view mode of JDashboard.
   * Runs the Visual Analysis template.

   **Advanced Run**![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4404894054551/btn_advrun.gif)  
    Runs the report immediately after collecting additional specifications from you, including which report tab to run for a page report, what output format to use, which style group to apply, and any encoding options.

   **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404889459863/btn_edit.gif)

   * Runs the report in the default format. If Report Studio is the default format, a web report will be opened in the Edit Mode of Web Report Studio and a page report in the Interactive View of Page Report Studio.
   * Runs the dashboard in the edit mode of JDashboard.

   **Schedule**![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404894051991/btn_schdl.gif)  
    Runs the report based on a schedule. When you use Schedule to run a report, the request is placed into a queue and processed in the order submitted. The size of the queue and priority of the queue can be configured to make the most efficient use of resources. [Lesson 4](https://devnet.logianalytics.com/hc/en-us/articles/1500009561862-Lesson-4-Scheduling-Reports) describes scheduled reports.

   **Version**![Version button](https://devnet.logianalytics.com/hc/article_attachments/4404894051479/btn_vrsn.gif)  
    Views the resource version and scheduled/advanced run result version information.

   **Properties**![Properties button](https://devnet.logianalytics.com/hc/article_attachments/4404894050967/btn_prpty.gif)  
    Allows you to define the archive policy, security, and a description associated with the resource. [Lesson 6](https://devnet.logianalytics.com/hc/en-us/articles/1500009582261-Lesson-6-Security) describes security.

   **Parameter Settings**![Parameter Settings button](https://devnet.logianalytics.com/hc/article_attachments/4404894055831/btn_prm.gif)  
    Customizes the default parameter values for the report.

   **Delete**![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404894051735/btn_delete.gif)  
    Deletes the resource.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009561802-Track-5-Publishing-Running-and-Administering-Resources) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009561822-Lesson-2-Publishing-Resources)
