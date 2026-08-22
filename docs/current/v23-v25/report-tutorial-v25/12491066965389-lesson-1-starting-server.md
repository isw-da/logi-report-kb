---
title: "Lesson 1: Starting Server"
id: 12491066965389
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491066965389-Lesson-1-Starting-Server
updated_at: 2025-05-30T02:58:11Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Lesson 1: Starting Server

In this lesson, you learn how to start Server, open the Server Console, and learn the other resource control commands available on the Server Console.

The Server Console has an easy-to-use web-based interface for selecting, viewing, and editing resources. Firefox, Google Chrome, Edge, and Safari are browsers that have been certified to work with the Report products. Other browsers should also work fine.

The lesson assumes that you have installed  Server with its default configuration. If you changed the default location or port numbers using Custom Installation, you need to adjust the instructions accordingly.

To start Server and access the Server Console locally, follow these steps: 

- Select Start Server in the Logi Report folder on the Start menu to open Server.

- Server displays a welcome page automatically in your default web browser, and prompts you to provide your user name and password. 

- Type admin for the user name and admin for the password, then select LOGIN. 
   These are the initial built-in user credentials on Server. One of the first things an administrator should do is to set up the correct user credentials, so each user can access the appropriate reports. 

- Server displays the Start Page which provides quick entries to some key functions.
    

- Select Public Folder in the Open category to go to the public report directory on the Server Console. By default, Server hides the User Directory panel on the left, which shows the folders of the published resources available to the current user.
    

- Select SampleReports. Server displays the resource list, along with pertinent information.

- Focus on any of the resource rows. Server displays a floating toolbar, which would contain all or some of the following commands, depending on the type of the resource.

- 
Run

- For a report, you can use this command to run the report in the default format. If Web Studio/Page Studio is the default format, Server opens a web report in the View Mode of Web Report Studio and a page report in the Basic View of Page Report Studio.

- For a dashboard, you can use this command to run the dashboard in the view mode of JDashboard.

- For a Visual Analysis template, you can use this command to run the template.

- Advanced Run
You can use this command to run the report immediately after collecting additional specifications from you, including which report tab to run for a page report, what output format to use, which style group to apply, and any encoding options.

- 
Edit

- For a report, you can use this command to run the report in the default format. If Web Studio/Page Studio is the default format, Server opens a web report in the Edit Mode of Web Report Studio and a page report in the Interactive View of Page Report Studio.

- For a dashboard, you can use this command to run the dashboard in the edit mode of JDashboard.

- Schedule
You can use this command to run the report based on a schedule. When you use Schedule to run a report, Server places the request into a queue and processes it in the submitted order. You can configure the size of the queue and priority of the queue to make the most efficient use of resources. Lesson 4 describes scheduled reports.

- Version
You can use this command to view the resource version and scheduled/advanced run result version information.

- Properties
You can use this command to define the archive policy, security, and a description associated with the resource. Lesson 6 describes security.

- Parameter Settings
You can use this command to customize the default parameter values for the report.

- NLS Editor
You can use this command to translate a report or dashboard into another language.

- Share
You can use this command to share a web report added by you in the server resource tree with other users.

- Delete
You can use this command to delete the resource.

Previous Topic  Next Topic
