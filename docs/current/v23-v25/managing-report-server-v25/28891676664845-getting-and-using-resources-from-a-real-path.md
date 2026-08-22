---
title: "Getting and Using Resources From a Real Path"
id: 28891676664845
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891676664845-Getting-and-Using-Resources-From-a-Real-Path
updated_at: 2026-02-26T02:13:31Z
source_host: docs-report.zendesk.com
---
# 
Getting and Using Resources From a Real Path

You can obtain resources from real paths to Report Server, in addition to publishing resources to Server. This topic describes how you can get resources from real paths and set the default real paths for the Public Reports and Public Components folders.

The difference between real path resources and published resources lies in the way of managing them: you can only manage published resources on Server, while you can manage real path resources on both Server and the operating system. On Server, when you access a resource node that links with a real path, Server loads the local resources in the real path to the node and displays them together with other server resources (including the published resources) in the node. You cannot delete the real path resources directly from the server UI. You can only delete them from the local disk.

To use real path resources, you should specify a real path for a virtual folder. You can then add or remove resources into or from Server by adding or removing them into or from the real path. If you do not want to add resources to the server using the Publish feature, set a real path instead.

By default, Server disables real path resources. To enable using real path resources, administrators need to select the Enable Resources from Real Paths option on the Server Console > Administration > Configuration > Advanced page and then restart Server.

See the following example about obtaining resources from the real path of the Public Reports folder:

- In the Resources page of the Server Console, browse to the Public Reports folder, put the mouse pointer over the folder row and select the Properties button  on the floating toolbar.

- In the General tab of the Folder Properties dialog box, select Enable Resources from Real Paths. 

- Specify the real path for the virtual folder as C:\LogiReport\Server\reportbak.

- Select OK to save the changes.
    

- Create the folder reportbak in C:\LogiReport\Server. 

- Create two sub folders report1 and  report2 in the folder reportbak.

- Copy some reports and catalogs into the two folders report1 and  report2. 

- In the server resource tree, open the virtual folder Public Reports. You can see the sub folders report1 and  report2 within it, including the reports and catalogs.

Now you can perform operations on the real path resources, including viewing versions, setting properties, and report-based operations such as running, advanced running, and scheduling.

- You cannot publish resources to a folder that comes from a real path.

- Real path resources themselves can only have one version in the server resource tree, so they do not support the  Archive Policy feature for managing multiple versions. 

- The relationships of folder real paths do not need to be consistent with that of the resource tree folders. That is, they are independent of each other. For example, in the resource tree, the folder ABC, whose real path is C:\FolderABC, has a sub folder DEF. The real path of DEF need not necessarily be a folder in C:\FolderABC. It can be any folder. However, if you put DEF under the folder ABC it will be visible on Server.

- After you use the real path resources, under certain special conditions Server generates some invalid nodes in the server databases. To delete the invalid nodes, administrators can clear invalid nodes from the internal server database on the Server Console. For more information, see Clearing invalid nodes from the realm database.

## Setting Default Real Paths for Public Folders Before Server Starts

You can set the default real paths for the Public Reports and Public Components folders without having to sign in to the server. There are two ways to achieve this goal: setting the real path during or after installation.

- 
Setting default real paths during installation
- When you are installing Server using the Installation Wizard, select the installation type Custom Installation for Standalone Server. and select Next. The Configure System Environment screen is then available.

- Select the Advanced tab.

- Select Enable Resources from Real Paths, and then type the paths separately in the Public Reports Real Path and Public Components Real Path text boxes, or specify the paths using the Browse button. 

- Upon completion of the installation, Server creates an install.server.properties file in the <install_root>\bin directory. When it starts, Server loads the file contents, sets the real paths for the Public Reports and Public Components folders, and then deletes the file. 

- 
Setting default real paths after installation
- 	If you want to set the default real paths for the Public Reports and Public Components folders after installation, you can create an install.server.properties file in the <install_root>\bin directory manually and add the following contents in the file. For example:
                server.publicReportsRealPath=C:\LogiReport\Realpath\Reports server.publicComponentsRealPath=C:\LogiReport\Realpath\Components

- If you want to turn on/off “resource from real path“ function and set the default real paths for the Public Reports and Public Components folders after installation, you can add -D parameters in JRServer.sh/bat manually. For example: -Djreport.enableDynamicResource=true -Djreport.publicReportsRealPath=C:\LogiReport\Realpath\Reports -Djreport.publicComponentsRealPath=:\LogiReport\Realpath\Components
