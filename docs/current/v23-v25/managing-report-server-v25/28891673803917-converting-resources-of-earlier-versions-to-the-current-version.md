---
title: "Converting Resources of Earlier Versions to the Current Version"
id: 28891673803917
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891673803917-Converting-Resources-of-Earlier-Versions-to-the-Current-Version
updated_at: 2026-02-26T02:13:28Z
source_host: docs-report.zendesk.com
---
# 
Converting Resources of Earlier Versions to the Current Version 

This topic describes how you can convert resources earlier than V8 to adapt to the current version using the Server Console or a tool.

If your Report Server contains resources earlier than V8, such as reports, visual analysis, library components, dashboards, and catalogs, during each server runtime lifecycle when you run such a resource for the first time, Report Engine has to first convert the earlier version resource to the current version resource before running the resource. This may result in decreased performance. To avoid this, Server enables administrators to permanently convert resources earlier than V8 in the server resource tree to adapt to the current version.

You can use the two ways to convert resources:

- 
Converting resources via UIThe converting UI is available to administrators only. You can use it to convert the resources earlier than V8 in the My Reports folder or Public Reports folder. Server stores the converted resources in the same directory.

- On the system toolbar of the Server Console, navigate to Administration > Other > Converting. Server displays the Converting page.
        

- Select the folders that contain the resources you want to convert.

- Specify how you want to save the converted resources.
        
- 
Replace the Old Resource
            Server replaces the old resources with the converted resources.

- 
Save as New Versions
            Select if you want to save the converted resources as new resource versions in the resource tree.

- Select OK to start converting. 

- 
Converting resources using a toolYou can also use rptconv.bat/rptconv.sh in the <install_root>\bin directory to convert a resource, a type of resources, or all resources earlier than V8 in a directory to current version.
