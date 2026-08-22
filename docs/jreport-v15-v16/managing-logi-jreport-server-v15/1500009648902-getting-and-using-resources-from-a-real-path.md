---
title: "Getting and Using Resources from a Real Path"
id: 1500009648902
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648902-Getting-and-Using-Resources-from-a-Real-Path
updated_at: 2021-07-24T20:54:02Z
---

# Getting and Using Resources from a Real Path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673581-Converting-Resources-of-Earlier-Versions-into-Current-Version)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648842-Customizing-TTF-Font-Location-for-Resources)

# Getting and Using Resources From a Real Path

Not only can you use the published resources described in section [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009673621-Publishing-Resources), but also those resources obtained from a real path. The difference between real path resources and published resources lies in the way of managing them. Published resources are managed in Logi JReport Server. Real path resources are managed in both the server and the operating system. In the server, when accessing a resource node which is linked with a real path, the local resources in the real path are loaded to the node and displayed together with other server resources (including the published resources) in the node. You cannot delete the real path resources directly from the server UI, but can only achieve it by removing the resources from the local disk.

To use real path resources, you should specify a real path for a virtual folder. You can then add or remove resources into or from Logi JReport Server by adding or removing them into or from the real path. Also, if you do not want to publish resources to the server by using the publish feature, you can set a real path instead.

The following example uses the resources in the folder Public Reports obtained from the real path:

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar, then select **Advanced** from the drop-down menu.
2. On the Configuration - Advanced page, check the **Enable Resources from Real Paths** option, save the changes and then restart the server.
3. On the Logi JReport Console page, open the Properties dialog of the folder /Public Reports by putting the mouse pointer over the folder row and selecting the Properties button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926692119/btn_srv_prpty.gif) on the floating toolbar, check **Enable Resources from Real Paths**, specify a real path for the demo virtual folder as `C:\Logi JReport\Server\reportbak`, then select **OK** to save the changes.
4. In the Windows directory `C:\Logi JReport\Server\reportbak`, create three sub directories report1, report2, and report3, and then copy some reports and catalogs into them.
5. On starting Logi JReport Server, select the virtual folder **/Public Reports**. You will then see the three sub folders: report1, report2, and report3 within it, including their reports and catalogs.

Now end users can perform operations on the real path resources, including viewing versions, setting properties, and report based operations such as running, advanced running, and scheduling.

**Notes:**

* You cannot publish resources to a folder that comes from a real path.
* You cannot use a real path resource as an archive location.
* Real path resources themselves can only have one version in the server resource tree, so they do not support the [Archive Policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009673721-Applying-an-Archive-Policy) feature for managing multiple versions.
* The relationships of folder real paths do not need to be consistent with that of the resource tree folders. That is, they are independent of each other. For example, in the resource tree, the folder ABC, whose real path is `C:\FolderABC`, has a sub folder DEF. The real path of DEF need not necessarily be a folder in `C:\FolderABC`. It can be any folder. However, if you put DEF under FolderABC it will be visible as published.
* After using the real path resources, under certain special conditions some invalid nodes will be generated in the server databases. In order to delete the invalid nodes, administrators can perform the corresponding option on the Logi JReport Administration page to clear invalid nodes from the internal Logi JReport Server database. For details, see [Clearing Invalid Nodes from the Realm Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009673521-Clearing-Invalid-Nodes-from-the-Server-Database).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Setting Default Real Paths for the Public Reports and Public Components Folders Before Server Starts

Logi JReport Server enables setting the default real paths for the Public Reports and Public Components folders without having to log onto the server. There are two ways to achieve this goal: setting the real path during or after installation.

* **Setting during installation**
  1. When installing Logi JReport Server using the Installation Wizard, select the installation type **Custom Installation for Standalone Server**. The Configure System Environment screen is then available.
  2. In the screen, select **Advanced** from the left panel.
  3. Check the **Enable Resources from Real Paths** option, and then type in the paths separately in the Public Reports Real Path and Public Components Real Path text fields or specify the paths using the Browse button.
  4. Upon completion of the installation, an install.server.properties file will be created in the `<install_root>\bin` directory. When the server starts, it retrieves the file contents, and then sets the real path for the Public Reports and Public Components folders. Note that the file is deleted after the server has loaded the file contents.
* **Setting after installation**

  If you want to set the default real paths for the Public Reports and Public Components folders after installation, you can create an install.server.properties file in the `<install_root>\bin` directory manually. Specify the content in the file as follows:

  `server.publicReportsRealPath=D:\Logi JReport\Realpath\Reports`  
  `server.publicComponentsRealPath=D:\Logi JReport\Realpath\Components`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673581-Converting-Resources-of-Earlier-Versions-into-Current-Version)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648842-Customizing-TTF-Font-Location-for-Resources)
