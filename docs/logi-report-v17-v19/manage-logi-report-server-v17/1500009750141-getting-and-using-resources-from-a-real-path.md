---
title: "Getting and Using Resources from a Real Path"
id: 1500009750141
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path
updated_at: 2021-07-25T07:18:57Z
---

# Getting and Using Resources from a Real Path

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750061-Converting-Resources-of-Earlier-Versions-into-Current-Version)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723102-Customizing-TTF-Font-Location-for-Resources)

# Getting and Using Resources From a Real Path

In addition to the [published resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources), you can also use resources obtained from real paths on Logi Report Server. The difference between real path resources and published resources lies in the way of managing them: published resources are managed on Logi Report Server, while real path resources can be managed on both the server and the operating system. On the server, when accessing a resource node which is linked with a real path, the local resources in the real path are loaded to the node and displayed together with other server resources (including the published resources) in the node. You cannot delete the real path resources directly from the server UI. Real path resources can only be deleted by removing from the local disk.

To use real path resources, you should specify a real path for a virtual folder. You can then add or remove resources into or from Logi Report Server by adding or removing them into or from the real path. If you do not want to add resources to the server using the Publish feature, set a real path instead.

By default, real path resources are disabled on Logi Report Server. To enable using real path resources, administrators need to select the Enable Resources from Real Paths option in the server console > Administration > Configuration > Advanced page and then restart Logi Report Server.

The following example shows using resources obtained from the real path of the Public Reports folder:

1. In the Resources page of the server console, browse to the Public Reports folder, put the mouse pointer over the folder row and select the **Properties** button ![Properties button](https://devnet.logianalytics.com/hc/article_attachments/4404942500503/btn_srv_prpty.gif) on the floating toolbar.
2. In the General tab of the Folder Properties dialog box, select **Enable Resources from Real Paths**, specify the real path for the virtual folder as `C:\LogiReport\Server\reportbak`, then select **OK** to save the changes.

   ![Enable Real Path](https://devnet.logianalytics.com/hc/article_attachments/4404942502039/mng_rsc_rlpth1.gif)
3. Create the folder **reportbak** in `C:\LogiReport\Server\`, and the subfolders **report1** and **report2** in it, then copy some reports and catalogs into them.
4. In the server resource tree, open the virtual folder **Public Reports**. You can see the subfolders within it, including the reports and catalogs.

![Real Path Resources](https://devnet.logianalytics.com/hc/article_attachments/4404936798871/mng_rsc_rlpth2.gif)

Now you can perform operations on the real path resources, including viewing versions, setting properties, and report based operations such as running, advanced running, and scheduling.

**Notes:**

* You cannot publish resources to a folder that comes from a real path.
* Real path resources themselves can only have one version in the server resource tree, so they do not support the [Archive Policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy) feature for managing multiple versions.
* The relationships of folder real paths do not need to be consistent with that of the resource tree folders. That is, they are independent of each other. For example, in the resource tree, the folder ABC, whose real path is `C:\FolderABC`, has a subfolder DEF. The real path of DEF need not necessarily be a folder in `C:\FolderABC`. It can be any folder. However, if you put DEF under FolderABC it will be visible as published.
* After using the real path resources, under certain special conditions some invalid nodes will be generated in the server databases. In order to delete the invalid nodes, administrators can perform the corresponding option in the server console to clear invalid nodes from the internal Logi Report Server database. For details, see [Clearing invalid nodes from the realm database](https://devnet.logianalytics.com/hc/en-us/articles/1500009723022-Managing-Server-Data#Clear).

## Setting Default Real Paths for the Public Reports and Public Components Folders Before Server Starts

Logi Report Server enables setting the default real paths for the Public Reports and Public Components folders without having to log onto the server. There are two ways to achieve this goal: setting the real path during or after installation.

* **Setting during installation**
  1. When installing Logi Report Server using the Installation Wizard, select the installation type **Custom Installation for Standalone Server**. The Configure System Environment screen is then available.
  2. In the screen, select **Advanced** from the left panel.
  3. Select the **Enable Resources from Real Paths** option, and then type the paths separately in the Public Reports Real Path and Public Components Real Path text boxes or specify the paths using the Browse button.
  4. Upon completion of the installation, an install.server.properties file will be created in the `<install_root>\bin` directory. When the server starts, it retrieves the file contents, and then sets the real path for the Public Reports and Public Components folders. Note that the file is deleted after the server has loaded the file contents.
* **Setting after installation**

  If you want to set the default real paths for the Public Reports and Public Components folders after installation, you can create an install.server.properties file in the `<install_root>\bin` directory manually and add the following content in the file. For example:

  `server.publicReportsRealPath=C:\LogiReport\Realpath\Reports`  
  `server.publicComponentsRealPath=C:\LogiReport\Realpath\Components`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750061-Converting-Resources-of-Earlier-Versions-into-Current-Version)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009723102-Customizing-TTF-Font-Location-for-Resources)
