---
title: "Lesson 2: Publishing Resources"
id: 12491067016589
section: "Report Tutorial v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491067016589-Lesson-2-Publishing-Resources
updated_at: 2025-05-30T02:58:10Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Lesson 2: Publishing Resources 

Report Server is only able to run reports and use library components that have been published to it. As you saw in the previous lesson, some reports have automatically been published to Report Server in the Public Reports folder. In this lesson, we publish the reports and library components in the JinfonetGourmetJava.cat catalog which were created in the previous tracks. If you haven't completed those tracks or do not want to use your own, you can use the version of the JinfonetGourmetJava catalog offered by Report Server, which is located at <install_root>\help\samples\JinfonetGourmetJava.

A report or library component must initially be published along with its catalog. Updates to the resource can be published independently, as long as the catalog associated with the resource remains published and has not changed. This enables you to quickly and easily install a change to a resource in the runtime environment.

This lesson contains the following tasks:

- Task 1: Publish Reports

- Task 2: Publish Library Components

## 
Task 1: Publish Reports

- In the Resources page of the server console, open the Public Reports folder.

- Select Publish >  From Server Machine on the task bar of the Resources page.
    

The Publish from Server Machine dialog box is displayed:

- Keep the default selected resource type Folder with Contents in the Resource Type drop-down list.
    The Resource Type list enables you to specify the resource, the catalog, report, or folder with these objects, to be published to Report Server.

- Select the Browse button next to the From Folder field, and then browse to select the <install_root>\help\samples\JinfonetGourmetJava directory.

- In the Resource Node Name field type JinfonetGourmetJava.

- In the Resource Description field type Jinfonet Gourmet Java catalog and reports.

- Select OK to publish the resources.    After the resources have been successfully published, the JinfonetGourmetJava folder is displayed in the resource tree.

- Select the folder name JinfonetGourmetJava and the reports in the folder are listed:
    

## 
Task 2: Publish Library Components

- In the Resources page of the server console, open the My Components folder.

- Select Publish > From Server Machine on the task bar of the Resources page. The Publish Resources page is displayed.

- Keep the default selected resource type Folder with Contents in the Resource Type drop-down list. 

- Select the Browse button next to the From Folder field, and then browse to select the <install_root>\help\samples\JinfonetGourmetJava directory.

- In the Resource Node Name field type JinfonetGourmetJava.

- In the Resource Description field type Jinfonet Gourmet Java catalog and library components.

- Select OK to publish the resources.
    After the resources have been successfully published, the JinfonetGourmetJava folder is displayed in the resource tree.

- Select the folder name JinfonetGourmetJava and the library components in the folder will be listed.
    

Previous Topic  Next Topic
