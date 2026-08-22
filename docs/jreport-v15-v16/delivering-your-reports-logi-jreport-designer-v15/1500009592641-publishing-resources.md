---
title: "Publishing Resources"
id: 1500009592641
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources
updated_at: 2021-07-24T05:53:51Z
---

# Publishing Resources

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592601-Publishing-and-Downloading-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592621-Downloading-Resources-from-Logi-JReport-Server)

# Publishing Resources

Logi JReport Designer, as a report design tool, allows you to publish your resources from it to your local computer or to Logi JReport Server.

When you publish a resource such as a report template, all of the referenced report templates and additional resources such as images will also be published although they will not be visible. This ensures that images and linked reports will be available at runtime.

Below is a list of the sections covered in this topic:

> * [Publishing Resources Locally](#Locally)
> * [Publishing Resources Remotely](#Remotely)

## Publishing Resources Locally

Logi JReport Designer supports publishing resources locally. That is, publishing resources to any directory on your computer or across your intranet.

1. Select **File** > **Publish** > **Publish to Local Directory**. The [Publish to Local Directory](https://devnet.logianalytics.com/hc/en-us/articles/1500009567122-Publish-to-Local-Directory-Dialog) dialog appears.

   ![Publish to Local Directory dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893818007/publocal.gif)
2. Select the **Browse** button to select a catalog, or type the catalog name with its full path directly into the From Catalog text field, and then press **Enter** to specify the catalog. All the reports in the specified catalog will then be displayed in the Select Report box.
3. Select the reports that you want to publish from the Select Report box and select the arrow button to add them to the box on the right, or directly drag the reports you want to publish from the Select Report box to the box on the right. If no report is selected here, only the catalog will be published.
4. Specify a directory for the catalog and reports that are to be published.

   Select the **Browse** button to the right of the To Local Directory text field, and locate a directory in the Get Directory dialog. Or you can type a directory in the text box directly. If you type in a directory which does not exist, Logi JReport Designer will automatically create it for you.
5. Select **Next** to view or modify properties of the data source connection.

   ![Publish to Local Directory](https://devnet.logianalytics.com/hc/article_attachments/4404893818263/pblsh_pub_lcl.gif)

   First, select a data source from the Catalog Data Source drop-down list, and then the connection properties of the selected data source will be displayed. If the selected data source is built on a JDBC connection, you can select the **Modify** button to modify [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog) of the data source connection in the Get JDBC Connection Information dialog.
6. Select the **Finish** button to publish the catalog and reports.

## Publishing Resources Remotely

The following introduces how to publish different resources to Logi JReport Server, which include [reports, library components](#Report) and [additional resources](#Additional).

If the resource you publish to on the server is already a real path resource you will get a permission denied error since real path resources can only be published by copying the files physically using FTP or OS copy file utilities.

Make sure that Logi JReport Server is started before publishing resources.

### Publishing reports and library components

When publishing [reports and library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009592661-Designing-Your-Reports) to Logi JReport Server you are actually copying the files into a subfolder in the `<install_root>/history` folder. The Logi JReport Server database keeps track of physical disk locations and maps those to logical folders shown in the server resource tree.

1. In Logi JReport Designer:
   * Select **File** > **Publish** > **Publish Report to Server** if you want to publish reports.
   * Select **File** > **Publish** > **Publish Component to Server** if you want to publish library components.

   The [Connect to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009585921-Connect-to-JReport-Server-Dialog) dialog appears.

   ![Connect to Logi JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893818519/connect.gif)
2. Type in the host and port of the remote Logi JReport Server in the Host and Port text fields.
3. When using a standalone server, enter **/jrserver** in the Servlet Path text field or the context root of your web application if deployed as a war or ear file such as /Logi JReport/jrserver.
4. If the server has been integrated with another web server that supports SSL, select the **SSL** (Security Socket Layer) checkbox to create an SSL connection.
5. Check **Remember connection information**  to enable Logi JReport Designer to remember the connection information.
6. Provide the user name and password of the server. When the Organization feature is enabled and when the user is an organization user, User Name should include the organization name. Use \ to separate the organization name and the user name, for example, org1\user1.
7. Select **Connect**. The [Publish to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009588321-Publish-to-Logi-JReport-Server-Dialog) dialog appears.

   ![Publish to Logi JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893818775/pubjrsrv.gif)
8. Select the **Browse** button next to the Publish Resource From text field to find the directory where your resources are located, and the resources in the specified directory will be loaded automatically. If you choose to type in the directory in the text field directly, you need to press Enter on the keyboard to load the resources in that directory.
9. In the resource tree box, check the checkboxes in front of the resources that you want to publish. To publish all the resources in the specified directory, check **Select All**.
10. In the Publish Resource To text field, select the **Browse** button to specify the folder on the server where the resources are to be published. An organization user can publish resources to the My Reports/Components or Organization Reports/Components folder.
11. Select a to-be-published resource in the resource tree box and then select the **More Options** button to set properties for the resource.
12. In the Properties tab,
    1. In the Resource Node Name text field, specify a name to be displayed in the server resource tree for the resource. You can type a name in the text field or select the Browse button to select a resource name from the Select Resource Name dialog, where all resource names of the same type as the selected resource, which are contained in the Publish Resource To path, are displayed.
    2. In the Resource Description text box, type a brief description to describe the resource.
    3. If a report is selected, specify the status of the report by selecting the required item from the Status drop-down list:
       * **Active**  
          The report can be run, advanced run and scheduled on Logi JReport Server.
       * **Inactive**  
          The report cannot be run, advanced run or scheduled on Logi JReport Server.
       * **Incomplete**  
          The report is not completely designed and cannot be run, advanced run or scheduled on Logi JReport Server.
    4. If a folder is selected, type a local disk path in the Resource Real Path text field as the real path of the folder. If you would like to map the real path resources into the new node created for the folder in the server resource tree so that the server will always be able to get the resources and updates from the real path, check the option **Enable Resources from Real Paths**. However once you create a real path folder you can no longer publish reports to it from Logi JReport Designer. You need to physically copy the files you want to publish into the specified folder on the server.
    5. In the Custom Field box, specify custom field values for the resource if there are custom fields enabled on Logi JReport Server.
    6. Check **Apply Archive Policy** to apply an archive policy to the resource.
       * To use multiple versions for the selected resource, check **Archive as New Version**, then in the **Max Number of Versions** text box enter the maximum number of versions that will be listed in the version table of the selected resource. The default value is 0, which means that the version amount is unlimited.
       * To replace the old version when the new version is generated, check **Replace Old Version.**
13. In the Permissions tab, check the **Enable Setting Permissions** option to specify permissions for the selected resource (this tab is available only when you have specified to publish the resources to the Public Reports folder on the server). For detailed information about the permissions, see Managing Permissions in the *Logi JReport Server User's Guide*.

    The roles, users, and groups that are created in the Logi JReport Server security system are listed in the Role, User and Group boxes. From one box, select a principal then check the checkboxes ahead of the required permissions. You can remove the principals in any box by selecting it and selecting the Remove button. To add the deleted principal back, use the Add button.

    ![Publish to Logi JReport Server dialog - Permission](https://devnet.logianalytics.com/hc/article_attachments/4404893819159/pblsh_pub_rpt1.gif)
14. If the selected resource is a catalog, the Connection tab is activated. Select a data source from the Catalog Data Source drop-down list and the connection properties of the selected data source are displayed. If the data source contains multiple connections only properties of the first connection are listed. When the connection is a JDBC connections the Modify button is activated. You can select it to modify [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009584941-Setting-Up-a-JDBC-Connection) of the JDBC connection in the Get JDBC Connection Information dialog. This is very useful when the database you use for report development is different from the one you use for production reports. Another alternative is to override the details of the connection by using the datasource.xml file in Logi JReport Server.

    ![Publish to Logi JReport Server dialog - Connection](https://devnet.logianalytics.com/hc/article_attachments/4404889294359/pblsh_pub_rpt2.gif)
15. Repeat steps 11 - 13 to set properties for other resources as required.
16. Select **OK** to publish the resources. If the reports or library components use special fonts, style groups, geographic information, or customized control files, the [Publish Additional Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009588301-Publish-Additional-Resources-Dialog) dialog appears for you to specify them.

**Notes****:**

* The Enable Resources from Real Paths option can only be checked when the same option on the Logi JReport Server Administration > Configuration > Advanced page has also been checked.
* If you have made some changes to the to-be-published resources, but have not saved them, before publishing starts, Logi JReport will save the changes automatically to ensure the resources published to the server are the latest.
* After resources have been published to Logi JReport Server, you may find that the publish time shown on the server UI is different from the client time. That is because the publish time takes the server time instead of the client time.

### Publishing additional resources

Additional resources used by reports and library components can also be published to Logi JReport Server. These resources include special fonts, [geographic information](https://devnet.logianalytics.com/hc/en-us/articles/1500009563462-Geographic-Maps), [style groups](https://devnet.logianalytics.com/hc/en-us/articles/1500009593261-XSD-Styles), and [customized control files](https://devnet.logianalytics.com/hc/en-us/articles/1500009584281-Using-Customized-Controls-in-a-Table).

1. Select **File** > **Publish** > **Publish Other Files to Server**.
2. In the Connect to Logi JReport Server dialog, specify the information to [connect to a started Logi JReport Server](#Connect). The [Publish Additional Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009588301-Publish-Additional-Resources-Dialog) dialog is displayed.

   ![Publish Additional Resources dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893819415/pubadtnlrsc.gif)
3. If special fonts are available, select the **Browse** button to specify the folder containing the special fonts.
4. In the Style tab, select the style groups you need and then select the right-headed single arrow button to add them to the right box.
5. In the Geographic Information tab, select the desired xml file where geographic information is stored and select the right-headed single arrow button to add them to the right box.

   ![Publish Additional Resources dialog - Geographic Information](https://devnet.logianalytics.com/hc/article_attachments/4404889294615/pblsh_pub_adtn1.gif)
6. In the Customized Control tab, select the customized control files you need and select the right-headed single arrow button to add them to the right box.

   ![Publish Additional Resources dialog - Customized Control](https://devnet.logianalytics.com/hc/article_attachments/4404893819671/pblsh_pub_adtn2.gif)
7. Select **OK** to publish the resources.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592601-Publishing-and-Downloading-Resources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592621-Downloading-Resources-from-Logi-JReport-Server)
