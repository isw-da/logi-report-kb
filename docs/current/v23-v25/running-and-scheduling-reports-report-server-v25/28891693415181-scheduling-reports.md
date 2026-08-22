---
title: "Scheduling Reports"
id: 28891693415181
section: "Running and Scheduling Reports Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891693415181-Scheduling-Reports
updated_at: 2026-02-26T02:13:43Z
source_host: docs-report.zendesk.com
---
# 
Scheduling Reports

Report Server provides a schedule system with which you can schedule tasks to run reports automatically at one or more designated dates and times, publish reports to different destinations in various formats such as PDF, HTML, and Excel, and customize notification messages to notify others of whether the tasks run successfully. This topic describes the server scheduling system, user task, and quick schedule.

You can submit a scheduled task from web page, via URL, or by calling the Server API methods. Server records the scheduled tasks according to their different running status (for more information, see Managing Report-Running Tasks).

In order to provide the means to run tasks defined outside of Report on Server, and to only use Server's Schedule function, Report provides a task named User Task, using which developer users can implement a customized task with the schedule properties. For more information, see Scheduling a Customized Task Using User Task.

Developer users can also specify a Java class to monitor the task event when setting up a schedule task. For more information, see Applying TaskListener.

In addition, Web Report Studio and Page Report Studio provide the Quick Schedule feature to enable end users to submit simple schedule tasks from the studio UI.

Select the following links to view the topics:

- Scheduling Tasks to Run Reports
                

- Scheduling Bursting Reports                

- Applying Dynamic Names for Published Report Files
                

- Viewing Scheduled Reports
                

- Importing and Exporting Scheduled Tasks
                

- When you schedule to publish a report to the Page Report Result format, if the report links to another report, Server no longer supports the link in the page report result. If you schedule to publish the report to several formats including the Page Report Result format, the link is not available in the other format outputs either.

- When you schedule to publish a report to the HTML format, you can localize the names of page navigation links in the report, such as First, Previous, Next, and Last. For more information, see Localizing the Page Navigation Links in HTML Report Outputs. 

- By enabling the 'Attempt to Run Misfired Periodical Schedule Once' option under Administration > Configuration > Advanced, customers can decide whether to execute a scheduled task when Quartz fails to trigger it on time. For instance, if there is a daily email schedule, enabling this option ensures that the customer receives the email every day, even if the schedule misfires. Without this option, the customer might miss emails on some days.
