---
title: "Creating Versions"
id: 28891688877197
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891688877197-Creating-Versions
updated_at: 2026-02-26T02:13:33Z
source_host: docs-report.zendesk.com
---
# 
Creating Versions 

Generally, Server creates report result versions when you run a report using Advanced Run or Schedule Run. This topic describes how you can create versions into resources.

You can create versions for a report, library component, or catalog by publishing them respectively from Server or Designer into the existing resource node. You can create versions of a report, dashboard, or analysis template by saving them as new versions. 

This topic contains the following sections:

- 
                    Creating Report/Library Component/Catalog Versions by Publishing Resources 
                

- 
                    Creating Report/Dashboard/Library Component/Analysis Versions by Saving as New Version
                

- 
                    Creating Report Result Versions
                

## 
Creating Report/Library Component/Catalog Versions by Publishing Resources 

The method for creating a new version to a report, library component, or catalog is by publishing a resource of the same type with exactly the same name to the same location in the server resource tree. For more information, see Publishing Resources. 

When publishing resources, you need to apply an archive policy to save the published resources into the existing resources as a new version.

## 
Creating Report/Dashboard/Library Component/Analysis Versions by Saving as New Version

You can save reports, dashboards, library components, and analysis templates as new versions into existing resources of the same type using the Save As feature. However, the existing resources should not be real path resources so that they can have versions. 

The most possible usage is to save a new version into the current resource:

- Open the Save As dialog box.

- Do not change the default location or file name.

- Configure the other settings.

- Select OK.

- Server displays the Confirm dialog box. Select As Version to save as a new version.
    

If you want to save a new version into another existing resource of the same type, in the Save As dialog box, specify the location and file name of the existing resource and then follow the other steps as above.

## 
Creating Report Result Versions

You can create a report result version  through any of the following operations: 

- When you advanced run a report, in the Archive tab of the Advanced Run dialog box, do the following:
    

- Specify where to save the result version by setting the Archive Location option.
        
- To generate the report result version as a built-in version of the report, select Built-in Version Folder. However, if you are an organization user and the report is in the Public Reports folder, or the report is a shared report, you cannot use the built-in version folder to generate the report result version. 

- To generate report result version in a standalone resource node in the resource tree, select My Reports Folder or Public Reports Folder (unavailable to organization users) or Organization Reports Folder (available to organization users only), and then provide the path and resource name information in the corresponding box.

- Apply an archive policy to the version.

- Submit the task.

Then when the report finishes running, Server generates a report result version to the specified location.

- When you schedule a report to publish it to the versioning system, in the Publish > To Version tab of the Schedule dialog box, do the following:
    
- Specify where to save the result version by setting the Archive Location option.
		
- To generate the report result version as a built-in version of the report, select Built-in Version Folder. This option is not available to a shared report, and to organization users when the report is in the Public Reports folder.

- To generate report result version in a standalone resource node in the resource tree, select My Reports Folder or Public Reports Folder (unavailable to organization users) or Organization Reports Folder (available to organization users only), and then provide the path and resource name information in the corresponding box.

- Apply an archive policy to the version.

- Submit the task.

Then when the schedule task finishes, Server generates a report result version to the specified location. If you schedule to run the report in multiple formats, Server saves the multiple report results as one version.

- When you export a page report or web report, in the Export dialog box, select the Save to Version System option, configure the other settings, and then select OK. Server generates a report result version to the report file in the server resource tree. 

- The resource path and name refer to the resource path and name in the resource tree. For instance, /foldername/filename.
      
- For the Public Reports Folder option, the first slash mark (/) refers to the Public Reports folder in the resource tree, and the folder name (foldername) refers to an existing folder in the resource tree.

- For the My Reports Folder option, /My Reports/ refers to the My Reports folder in the resource tree, and the folder name (foldername) refers to an existing folder in the resource tree.

- For the Organization Reports Folder option, /Organization Reports/ refers to the Organization Reports folder in the resource tree, and the folder name (foldername) refers to an existing folder in the resource tree.

- When generating report result versions in an existing standalone resource node in the resource tree, for example, creating a new version for a resource node, you should provide the path and name of the existing resource for the Public Reports Folder or My Reports Folder or Organization Reports Folder option.
