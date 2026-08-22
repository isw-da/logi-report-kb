---
title: "Linking Resources and Catalogs"
id: 28891688271501
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891688271501-Linking-Resources-and-Catalogs
updated_at: 2026-02-26T02:13:29Z
source_host: docs-report.zendesk.com
---
# 
Linking Resources and Catalogs 

You can link a resource, such as a report or a library component, with a catalog in Report, without the need of putting them in one folder. This topic describes the benefits of linking resources and catalogs and how you can set linked catalogs.

The benefits of a linked catalog compared to a copied catalog are:

- There is no need to also copy the catalog to the destination directory when you save a resource to a different location. 

- When you update the linked catalog, the resources that use the catalog can run with the updated version. However, Report does not automatically update the copied catalog if you update its original catalog since they are two independent versions.

- When the resource and its linked catalog are not in the same directory, the resource can still run with the catalog. You do not need to publish duplicate copies of the catalog that can lead to errors and inconsistencies as well as more memory and disk space usage. You can organize the reports into folders on the server without worrying about making copies of catalogs and maintaining multiple versions of the same catalog.

When you directly run a resource, the linked catalog has higher priority than the catalog in the same folder as the resource. Without linked catalog, the resource will run within the selected catalog in the same folder. As for Advanced Run and Schedule, the default selected catalog is the linked catalog if there is one, however, you can change it by the option Select Another Catalog.

## Setting Linked Catalog

You can set linked catalog at the server level, folder level, and resource level: 

- To set linked catalog at the server level (you need to be an administrator):
    
- On the system toolbar of the Server Console, navigate to Administration > Configuration > Advanced. Server displays the Advanced page. 

- Select Enable Linked Catalog.

- Select Select Another Catalog to specify the catalog as the linked catalog at the server level.

- Select Save to save the changes.

- Restart Server to make the settings take effect.

- To set linked catalog at the folder/resource level, go to the Properties dialog box of the folder/resource, select Enable Linked Catalog, then specify the linked catalog. You can specify a linked catalog for multiple resources at a time.
    
- 
Use Specified - You can specify a linked catalog which can be any catalog in the server resource tree for the folder/resource. 

- 
Use Inherited - If the parent level of the folder/resource has a linked catalog, you can use the parent-level linked catalog as the linked catalog of the folder/resource. For the built-in resource folder, Public Reports, the parent level is the server level.

- If you modified the linked catalog in use after you submitted a scheduled task, the task still uses the previous catalog until you update the task information.

- When saving a page report in Page Report Studio, or saving a web report in Web Report Studio, you can also save the original catalog as a linked catalog for the page report. 

- Server links the analysis templates that you saved with their original catalogs. You cannot change linked catalogs of analysis templates.
