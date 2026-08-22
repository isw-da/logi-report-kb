---
title: "Lesson 2: Publishing Resources"
id: 12479930163341
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479930163341-Lesson-2-Publishing-Resources
updated_at: 2026-02-25T23:51:07Z
source_host: docs-report.zendesk.com
---
# Lesson 2: Publishing Resources

Server is only able to run reports and use library components that have been published to it. As you saw in the previous lesson, some reports have automatically been published to Server in the Public Reports folder. In this lesson, we publish the reports and library components in the JinfonetGourmetJava.cat catalog that were created in the previous tracks. If you have not completed those tracks or do not want to use your own, you can use the version of the JinfonetGourmetJava catalog offered by Server, which is located at <install_root>\help\samples\JinfonetGourmetJava.

You must publish a report or library component along with its catalog initially. You can publish updates to the resource independently, as long as the catalog associated with the resource remains published and has not changed. This enables you to quickly and easily install a change to a resource in the runtime environment.

This lesson contains the following tasks:

- Task 1: Publish Reports

- Task 2: Publish Library Components

## 
Task 1: Publish Reports

- In the Resources page of the Server Console, open the Public Reports folder.

- Navigate to Publish >  From Server Machine on the task bar of the Resources page.
    

Server displays the Publish from Server Machine dialog box.

- Keep the default selected resource type Folder with Contents in the Resource Type drop-down list. From the Resource Type list, you can specify the resource, the catalog, report, or folder with these objects, to publish to Server.
    

- Select Browse next to the From Folder text box, and then browse to select the <install_root>\help\samples\JinfonetGourmetJava directory.

- In the Resource Node Name text box, type JinfonetGourmetJava.

- In the Resource Description text box, type Jinfonet Gourmet Java catalog and reports.

- Select OK to publish the resources.

- After Server publishes the resources successfully, it displays the JinfonetGourmetJava folder in the resource tree.
    Select the folder name and Server lists the reports in the folder. 

## 
Task 2: Publish Library Components

- In the Resources page of the Server Console, open the My Components folder.

- Navigate to Publish > From Server Machine on the task bar of the Resources page. Server displays the Publish Resources page.

- Keep the default selected resource type Folder with Contents in the Resource Type drop-down list. 

- Select Browse next to the From Folder text box, and then browse to select the <install_root>\help\samples\JinfonetGourmetJava directory.

- In the Resource Node Name text box, type JinfonetGourmetJava.

- In the Resource Description text box, type Jinfonet Gourmet Java catalog and library components.

- Select OK to publish the resources.

- After Server publishes the resources successfully, it displays the JinfonetGourmetJava folder in the resource tree. Select the folder name and Server lists the library components in the folder.
