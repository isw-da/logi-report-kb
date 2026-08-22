---
title: "Deleting Versions"
id: 45204037270925
section: "Managing Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204037270925-Deleting-Versions
updated_at: 2026-04-30T14:10:34Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Deleting Versions 

After creating versions, periodically you may want to delete some expired or unused versions. This topic describes how you can remove versions manually or configure Server to delete them automatically. 

When you remove the versions on the Server Console, Server also deletes the archive versions stored on disk in the history folder.

This topic contains the following sections:

- Deleting Versions of a Resource Manually

- Deleting Versions Automatically

## 
Deleting Versions of a Resource Manually

Open the version table of the resource, then:

- To delete a version of the resource:
			    
- Select the version row and select Edit > Delete on the task bar.

- Select the version row, right-click in the row, and select Delete on the shortcut menu.

- Put the mouse pointer over the version row and select the Delete button  on the floating toolbar.

- To delete multiple versions of the resource at a time, select the version rows, then select Edit > Delete on the task bar or right-click in any row and select Delete on the shortcut menu.

Server prompts you a message box, asking for your confirmation about the removal. Select Yes in the message box to remove the selected versions from the version table.

You can also use the Database Archive feature to remove versions older than a specified date or use URL commands to directly delete a specific version.

## 
Deleting Versions Automatically

There are two approaches to automatically deleting versions: 

- 
Apply Archive Policy
  You can use Archive Policy to control the number of versions to record in the version table of a resource.
    When creating a resource version, you can specify the maximum number of versions. If the number of versions exceeds the specified number, Server automatically removes the oldest version from the version list.

For example, if you specify Maximum Number of Versions as 5, when it creates the sixth version, Server automatically removes the first version.

- 
Result Auto-delete
  Result Auto-delete controls the duration of report result versions and result versions.
    When creating a report result version via Advanced Run or Schedule Run, or when modifying the properties of a result version, you can specify a certain period to keep the version. Server automatically removes the version from the corresponding version table after the number of days or the specified date.

For example, if you specify "Result Expires in 30 days" for a report result version, Server automatically removes the version 30 days after its creation.
