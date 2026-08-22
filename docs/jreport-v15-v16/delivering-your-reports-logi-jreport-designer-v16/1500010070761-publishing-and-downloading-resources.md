---
title: "Publishing and Downloading Resources"
id: 1500010070761
section: "Delivering Your Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources
updated_at: 2021-07-24T10:37:45Z
---

# Publishing and Downloading Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033102-Exporting-to-Fax) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063001-Working-with-APIs)

# Publishing and Downloading Resources

Logi JReport Designer, as a report design tool, allows you to publish your resources from it to your local computer or to Logi JReport Server. When you publish a resource such as a report template, all of the referenced report templates and additional resources such as images will also be published although they will not be visible. This ensures that images and linked reports will be available at runtime.

Reports created on Logi JReport Sever can also be downloaded to a specified folder on your local computer, and further modified in Logi JReport Designer.

**Tip:** Before you can publish or download resources from a Logi JReport Server, you need to make sure the server is started. You can pre-set the properties for connecting with the server and user information to login via the [Options](https://devnet.logianalytics.com/hc/en-us/articles/1500010031962-Options-Dialog#Server) dialog to avoid repeated connecting and logging.

Below is a list of the sections covered in this topic:

* [Publishing Resources Remotely](#Remotely)
  + [Publishing Reports](#PubReport)
  + [Publishing Additional Resources](#Additional)

* [Publishing Resources Locally](#Locally)
* [Downloading Reports](#DownReport)
* [Downloading Customized Controls](#DownCtrl)

## Publishing Resources Remotely

You can publish different resources to Logi JReport Server, which include [reports](#PubReport)  and [additional resources](#Additional).

### Publishing Reports

When publishing reports to Logi JReport Server you are actually copying the files into a subfolder in the `<server_install_root>/history` folder. The Logi JReport Server database keeps track of physical disk locations and maps those to logical folders shown in the server resource tree.

1. Do either of the following:
   * Select **File** > **Publish** > **Publish Report to Server** if you want to publish reports.
   * Select **File** > **Publish** > **Publish Component to Server** if you want to publish library components.

   If Logi JReport Designer can automatically connect to the server and log you in, you will be shown the [Publish to JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010032182-Publish-to-JReport-Server-Dialog) dialog, otherwise you will be prompted with the [Connect to JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010029982-Connect-to-JReport-Server-Dialog) dialog to specify the properties for connecting with the server first.

   ![Publish to JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909128855/pubjrsrv.gif)
2. Select the **Browse** button next to the Publish Resource From text box to find the directory where your resources are located, and the resources in the specified directory will be loaded automatically. If you choose to type in the directory in the text box directly, you need to press Enter on the keyboard to load the resources in that directory.
3. In the resource tree box, check the checkboxes in front of the resources that you want to publish. To publish all the resources in the specified directory, check **Select All**.
4. In the Publish Resource To text box, select the **Browse** button to specify the folder in the server resource tree where the resources are to be published.
5. Select a to-be-published resource in the resource tree box and then select the **More Options** button to set properties for the resource.
6. In the Properties tab,
   1. In the Resource Node Name text box, specify a name to be displayed in the server resource tree for the resource. You can type a name in the text box or use the Browse button to select a resource name from the Select Resource Name dialog, where all resource names of the same type as the selected resource, which are contained in the Publish Resource To path, are displayed.
   2. In the Resource Description text box, type a brief description to describe the resource.
   3. If a report is selected, specify the status of the report by selecting the required item from the Status drop-down list:
      * **Active**  
         The report can be run, advanced run and scheduled on Logi JReport Server.
      * **Inactive**  
         The report cannot be run, advanced run or scheduled on Logi JReport Server.
      * **Incomplete**  
         The report is not completely designed and cannot be run, advanced run or scheduled on Logi JReport Server.
   4. If a folder is selected, type a local disk path in the Resource Real Path text box as the real path of the folder. If you would like to map the real path resources into the new node created for the folder in the server resource tree so that the server will always be able to get the resources and updates from the real path, check the option **Enable Resources from Real Paths**. However once you create a real path folder you can no longer publish reports to it from Logi JReport Designer. You need to physically copy the files you want to publish into the specified folder on the server.
   5. In the Custom Field box, specify custom field values for the resource if there are custom fields enabled on Logi JReport Server.
   6. Check **Apply Archive Policy** to apply an archive policy to the resource.
      * To use multiple versions for the selected resource, check **Archive as New Version**, then in the **Max Number of Versions** text box enter the maximum number of versions that will be listed in the version table of the selected resource. The default value is 0, which means that the version amount is unlimited.
      * To replace the old version when the new version is generated, check **Replace Old Version.**
7. In the Permissions tab, check the **Enable Setting Permissions** option to specify permissions for the selected resource (this tab is available only when you have specified to publish the resources to a public folder on the server). For detailed information about the permissions, see Managing Permissions in the *Logi JReport Server User's Guide*.

   The roles, users, and groups that are created in the Logi JReport Server security system are listed in the Role, User and Group boxes. From one box, select a principal then check the checkboxes ahead of the required permissions. You can remove the principals in any box by selecting it and selecting the Remove button. To add the deleted principal back, use the Add button.

   ![Publish to Logi JReport Server dialog - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4404901138839/pblsh_pub_rpt1.gif)
8. If the selected resource is a catalog, the Connection tab is activated. Select a data source from the Catalog Data Source drop-down list and the connection properties of the selected data source are displayed. If the data source contains multiple connections only properties of the first connection are listed. When the connection is a JDBC connections the Modify button is activated. You can select it to modify [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010064401-Setting-Up-JDBC-Connections-in-a-Catalog) of the JDBC connection in the Get JDBC Connection Information dialog. This is very useful when the database you use for report development is different from the one you use for production reports. Another alternative is to override the details of the connection by using the datasource.xml file in Logi JReport Server.

   ![Publish to Logi JReport Server dialog - Connection tab](https://devnet.logianalytics.com/hc/article_attachments/4404901139095/pblsh_pub_rpt2.gif)
9. Repeat steps 11 - 13 to set properties for other resources as required.
10. Select **OK** to publish the resources. If the reports or library components use special fonts, style groups, geographic information, or customized control files, the [Publish Additional Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010067461-Publish-Additional-Resources-Dialog) dialog appears for you to specify them.

**Notes****:**

* Only one catalog file is allowed in folders in the server resource tree where library components can be published.
* The Enable Resources from Real Paths option can only be checked when the same option on the Logi JReport Server console > Administration > Configuration > Advanced page has also been checked.
* If you have made some changes to the to-be-published resources, but have not saved them, before publishing starts, Logi JReport will save the changes automatically to ensure the resources published to the server are the latest.
* After resources have been published to Logi JReport Server, you may find that the publish time shown on the server UI is different from the client time. That is because the publish time takes the server time instead of the client time.
* If the resource you publish to on the server is already a real path resource, you will get a permission denied error since real path resources can only be published by copying the files physically using FTP or OS copy file utilities.

### Publishing Additional Resources

Additional resources used by reports can also be published to Logi JReport Server. These resources include special fonts, [geographic information](https://devnet.logianalytics.com/hc/en-us/articles/1500010029122-Geographic-Maps), [style groups](https://devnet.logianalytics.com/hc/en-us/articles/1500010071001-XSD-Styles), and [customized control files](https://devnet.logianalytics.com/hc/en-us/articles/1500010029282-Using-Customized-Controls-in-Tables).

1. Select **File** > **Publish** > **Publish Other Files to Server**.

   If Logi JReport Designer can automatically connect to the server and log you in, you will be shown the [Publish Additional Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500010067461-Publish-Additional-Resources-Dialog) dialog, otherwise you will be prompted with the [Connect to JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010029982-Connect-to-JReport-Server-Dialog) dialog to specify the properties for connecting with the server first.

   ![Publish Additional Resources dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901139351/pubadtnlrsc.gif)
2. If special fonts are available, select ![Chooser button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) to specify the folder containing the special fonts.
3. In the Style tab, select the style groups you need and then select the right-headed single arrow button to add them to the right box.
4. In the Geographic Information tab, select the desired xml file where geographic information is stored and select the right-headed single arrow button to add them to the right box.

   ![Publish Additional Resources dialog - Geographic Information tab](https://devnet.logianalytics.com/hc/article_attachments/4404901139607/pblsh_pub_adtn1.gif)
5. In the Customized Control tab, select the customized control files you need and select the right-headed single arrow button to add them to the right box.

   ![Publish Additional Resources dialog - Customized Control tab](https://devnet.logianalytics.com/hc/article_attachments/4404901139863/pblsh_pub_adtn2.gif)
6. Select **OK** to publish the resources.

## Publishing Resources Locally

Logi JReport Designer supports publishing resources locally. That is, publishing resources to any directory on your computer or across your intranet.

1. Select **File** > **Publish** > **Publish to Local Directory**. The [Publish to Local Directory](https://devnet.logianalytics.com/hc/en-us/articles/1500010067481-Publish-to-Local-Directory-Dialog) dialog appears.

   ![Publish to Local Directory dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909129111/publocal.gif)
2. Select the **Browse** button to select a catalog, or type the catalog name with its full path directly into the From Catalog text box, and then press **Enter** to specify the catalog. All the reports in the specified catalog will then be displayed in the Select Report box.
3. Select the reports that you want to publish from the Select Report box and select the arrow button to add them to the box on the right, or directly drag the reports you want to publish from the Select Report box to the box on the right. If no report is selected here, only the catalog will be published.
4. Specify a directory for the catalog and reports that are to be published.

   Select the **Browse** button to the right of the To Local Directory text box, and locate a directory in the Get Directory dialog. Or you can type a directory in the text box directly. If you type in a directory which does not exist, Logi JReport Designer will automatically create it for you.
5. Select **Next** to view or modify properties of the data source connection.

   ![Publish to Local Directory dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901140119/pblsh_pub_local.gif)

   First, select a data source from the Catalog Data Source drop-down list, and then the connection properties of the selected data source will be displayed. If the selected data source is built on a JDBC connection, you can select the **Modify** button to modify [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog) of the data source connection in the Get JDBC Connection Information dialog.
6. Select the **Finish** button to publish the catalog and reports.

## Downloading Reports

Reports created on Logi JReport Server can be downloaded to your local computer and further modified using Logi JReport Designer. The same as with publishing, all resources used by the reports will also be downloaded such as other linked reports and images.

1. Do either of the following:
   * Select **File** >  **Download** > **Download Report from Server** if you want to download reports.
   * Select **File** > **Download** > **Download Component from Server** if you want to download library components.

   If Logi JReport Designer can automatically connect to the server and log you in, you will be shown the [Download from JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010065441-Download-from-JReport-Server-Dialog) dialog, otherwise you will be prompted with the [Connect to JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010029982-Connect-to-JReport-Server-Dialog) dialog to specify the properties for connecting with the server first.

   ![Download from JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901140375/dwldjrsrv.gif)
2. In the Download Resource From text box, select the **Browse** button to specify the folder on the server where to download resources. The resources in the specified folder will then be loaded automatically in the resource tree box.
3. In the resource tree box, check the checkboxes in front of the resources that you want to download.
4. Select the **Browse** button next to the Download Resource To text box to specify the path to which resources will be downloaded, or type in the directory in the text box directly.
5. Select **OK**. The selected resources and all additional resources referenced by them such as linked reports and images will then be downloaded from Logi JReport Server.

When the resources are successfully downloaded from Logi JReport Server, you can open them in Logi JReport Designer, and further edit them if required.

**Notes:**

* Resources in the Public Reports folder of Logi JReport Server are protected by permissions. If you specify to download resources from that folder, which resources you can see in the resource tree box and which resources you can download are determined by the user name with which you use to connect to the server. You can only view the resources on which you have the Visible permission in this box and download resources on which you are assigned the Read permission. .For more information, refer to Managing Permissions in the *Logi JReport Server User's Guide*.
* Downloading reports which use business views as data source from Logi JReport Server requires that Logi JReport Designer and Logi JReport Server each has its own [Live license](https://devnet.logianalytics.com/hc/en-us/articles/1500010068641-Logi-JReport-Licenses#Live).

## Downloading Customized Controls

[Customized controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010029282-Using-Customized-Controls-in-Tables) on Logi JReport Server can be downloaded to the customized control library of Logi JReport Designer which is the Customized Control folder under the installation root and further modified using Logi JReport Designer.

1. Select **File** > **Download** > **Download Customized Control from Server**.

   If Logi JReport Designer can automatically connect to the server and log you in, you will be shown the [Download Customized Control](https://devnet.logianalytics.com/hc/en-us/articles/1500010065421-Download-Customized-Control-Dialog) dialog, otherwise you will be prompted with the [Connect to JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500010029982-Connect-to-JReport-Server-Dialog) dialog to specify the properties for connecting with the server first.

   ![Download Customized Control dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909129367/dwldcstmzdctrl.gif)
2. Select the customized control files you need, select the right-headed single arrow button to add them to the right box.
3. Select **OK** to download the selected control files.

   If the local control library contains control files that have the same names with the downloaded control files, the local files will be replaced directly without warning.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033102-Exporting-to-Fax) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063001-Working-with-APIs)
