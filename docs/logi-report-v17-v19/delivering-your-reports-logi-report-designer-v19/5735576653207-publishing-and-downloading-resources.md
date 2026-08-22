---
title: "Publishing and Downloading Resources"
id: 5735576653207
section: "Delivering Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735576653207-Publishing-and-Downloading-Resources
updated_at: 2022-11-10T06:08:09Z
---

# Publishing and Downloading Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735506410263-Working-with-APIs)

# Publishing and Downloading Resources

Designer, as a report design tool, enables you to publish your resources from it to your local computer or to Server. When you publish a resource such as a report template, Designer publishes all of the referenced report templates and additional resources such as images although they are not visible. This ensures that images and linked reports are available at runtime. In addition, you can download reports created on Sever to a specified folder on your local computer and further modify them in Designer. This topic describes publishing and downloading different resources using Designer.

In Designer, you can save catalogs and reports in either binary or [in XML](https://devnet.logianalytics.com/hc/en-us/articles/5735520312215-Knowing-About-Catalogs#Format). For performance concern, when you publish catalog and report files saved in XML to Server, Server parses the XML files, converts them to binary files, and then saves the converted binary files into its resource system instead of the XML files. In this way, Server does not have to go through parsing of the XML files each time the catalogs and page reports are executed, so that its performance can be greatly improved. In the meantime, when you download catalogs and reports from the resource system of Server to Designer, you can download them in XML if you prefer this format for checking into source code control systems.

This topic contains the following sections:

* [Publishing Resources Remotely](#Remotely)
  + [Publishing Reports](#PubReport)
  + [Publishing Additional Resources](#Additional)
* [Publishing Resources Locally](#Locally)
* [Downloading Reports](#DownReport)
* [Downloading Customized Controls](#DownCtrl)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Before you can publish or download resources from Server, you need to make sure it is started. You can preset the properties for connecting with a Server and the user information via the [Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524192535-Options-Dialog-Box#Server) to avoid repeated connecting and signing in.

## Publishing Resources Remotely

You can publish different resources to Server, which include [reports](#PubReport) and [additional resources](#Additional).

### Publishing Reports

When publishing reports to Server, you are actually copying the files into a subfolder in the `<server_install_root>/history` folder. The Server database keeps track of physical disk locations and maps those to logical folders shown in its resource tree.

1. Do either of the following:
   * Navigate to **File** > **Publish** > **Publish Report to Server** if you want to publish reports.
   * Navigate to **File** > **Publish** > **Publish Component to Server** if you want to publish library components.

   If Designer can automatically connect to a started Server and sign you in, it displays the [Publish to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735567050135-Publish-to-Logi-Report-Server-Dialog-Box); otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499997591-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the connection and user information first.

   ![Publish to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898457770647/pubjrsrv.gif)
2. Select **Browse** next to the **Publish Resource From** text box to find the directory where your resources are located, Designer then loads the resources in the specified directory automatically into the resource box. If you choose to type the directory in the text box, you need to select **Enter** on the keyboard to load the resources in that directory.
3. In the resource box, select the checkboxes in front of the resources that you want to publish. To publish all the resources in the specified directory, select **All**.
4. In the **Publish Resource To** text box, select **Browse** to specify the folder in the resource tree of Server where to publish the resources.
5. Select a to-be-published resource in the resource box and then select **More Options** to set its properties.
6. In the **Properties** tab,
   1. In the **Resource Node Name** text box, specify a name that displays in the resource tree of Server for the resource. You can type a name in the text box or select **Browse** to select a resource name using the Select Resource Name dialog box, which lists all the resource names of the same type as the selected resource stored in the path where you specify to publish the resources on Server.
   2. In the **Resource Description** text box, type a brief description to describe the resource.
   3. If the selected resource is a report, specify the status of the report by selecting the required item from the **Status** drop-down list:
      * **Active**  
        Select it and users can run, advanced run, and schedule the report on Server.
      * **Inactive**  
        Select it and users are not able to run, advanced run, or schedule the report on Server.
      * **Incomplete**  
        Select it if the report is not completely designed, then users are not able to run, advanced run, or schedule it on Server.
   4. If the selected resource is a folder, type a local disk path in the **Resource Real Path** text box as the real path of the folder. If you would like to map the real path resources into the new node created for the folder in the resource tree of Server, so that Server is always able to get the resources and updates from the real path, select **Enable Resources from Real Paths**. However, once you create a real path folder, you can no longer publish reports to it from Designer. You need to physically copy the files you want to publish into the specified folder on Server.
   5. In the **Custom Field** panel, specify custom field values for the resource if there are custom fields enabled on Server.
   6. Select **Apply Archive Policy** to apply an archive policy to the resource.
      * To use multiple versions for the selected resource, select **Archive as New Version**, then in the **Max Number of Versions** text box, type the maximum number of versions that Server maintains in the version table of the selected resource. The default value is 0, which means that the version amount is unlimited.
      * To replace the old version when a new version is generated, select **Replace Old Version.**
7. Designer enables the **Permissions** tab when you specify to publish the resources to a public folder on Server. Select **Enable Setting Permissions** to specify user permissions for the selected resource.

   ![Publish to Logi Report Server dialog box - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/9898474855319/pblsh_pub_rpt1.gif)

   * Select the **Role**, **User**, or **Group** tab, then select a role, user, or group from the principal box and select the checkboxes ahead of the required permissions.
   * The principal boxes by default contains all the roles, users, and groups in the security system of Server. You can remove a principal in any box by selecting it and selecting **Remove**. To add a deleted principal back, use **Add**.
   * For more information about the permissions, see Managing Permissions in the *Logi Report Server Guide*.
8. Designer enables the **Connection** tab when you select to publish a catalog. Select a data source of the catalog from the **Catalog Data Source** drop-down list, then select a connection in the specified data source from the **Connection** drop-down list. Designer displays the properties of the selected connection for your reference. When you select a JDBC connection, Designer enables the **Modify** button. You can select the button to modify information of the connection in the [Get JDBC Connection Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530237847-Get-JDBC-Connection-Information-Dialog-Box), which applies to the connection published to Server only, meaning, the connection in Designer still applies the original settings.

   ![Data Source Connection Properties](https://devnet.logianalytics.com/hc/article_attachments/9898457815319/pblsh_pub_rpt2.gif)
9. Repeat steps 5 - 7 to set properties for other resources.
10. Select **OK** to publish the resources to Server. If the reports or library components use special fonts, style groups, geographic information, or customized control files, Designer displays the [Publish Additional Resources dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524363159-Publish-Additional-Resources-Dialog-Box) for you to [specify them](#Additional).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Server only allows one catalog file in folders in its resource tree where you can publish library components.
* You can select the Enable Resources from Real Paths option only when the Server administrator has selected the same option in the Administration > Configuration > Advanced page of the Server Console.
* If you have made some changes to the to-be-published resources, but have not saved them, before publishing starts, Designer saves the changes automatically to ensure the resources published to Server are the latest.
* After you finish publishing resources to Server, you may find that the publishing time shown on the Server UI is different from the client time. That is because the publishing time takes the Server time instead of the client time.
* If the resource you publish to on Server is already a real path resource, you get a permission denied error. You can only publish real path resources by copying the files physically using FTP or OS copy file utilities.

### Publishing Additional Resources

You can also publish additional resources that your reports use to Server. These resources include [special fonts](https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports), [geographic information](https://devnet.logianalytics.com/hc/en-us/articles/5735499019543-Using-Geographic-Maps), [style groups](https://devnet.logianalytics.com/hc/en-us/articles/5735576944407-Working-with-XSD-Styles), and [customized control files](https://devnet.logianalytics.com/hc/en-us/articles/5735499153175-Using-Customized-Controls-in-Tables).

1. Navigate to **File** > **Publish** > **Publish Other Files to Server**. If Designer can automatically connect to a started Server and sign you in, it displays the [Publish Additional Resources dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524363159-Publish-Additional-Resources-Dialog-Box); otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499997591-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the connection and user information first.

   ![Publish Additional Resources dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898474904343/pubadtnlrsc.gif)
2. If special fonts are available, select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to specify the folder containing the special fonts.
3. In the **Style** tab, select the required style groups in the left box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add them to the right box. You can select **Add All**![Add All button](https://devnet.logianalytics.com/hc/article_attachments/9898422526743/btn_addall.gif) to add all the style groups at a time.
4. In the **Geographic Information** tab, add the XML files that store the geographic information your reports apply.

   ![Publish Additional Resources dialog box - Geographic Information tab](https://devnet.logianalytics.com/hc/article_attachments/9898474913303/pblsh_pub_adtn1.gif)
5. In the **Customized Control** tab, add the customized control files you need.

   ![Publish Additional Resources dialog box - Customized Control tab](https://devnet.logianalytics.com/hc/article_attachments/9898474925207/pblsh_pub_adtn2.gif)
6. Select **OK** to publish the resources to Server.

## Publishing Resources Locally

Designer supports publishing resources locally, that is, publishing resources to any directory on your computer or across your intranet.

1. Navigate to **File** > **Publish** > **Publish to Local Directory**. Designer displays the [Publish to Local Directory dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735515185175-Publish-to-Local-Directory-Dialog-Box).

   ![Publish to Local Directory dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898474941591/publocal.gif)
2. Select **Browse** to select a catalog, or type the catalog file name with its full path in the **From Catalog** text box and select **Enter** on the keyboard to specify the catalog. Designer then lists all the page reports and web reports in the specified catalog in the **Select Report** box.
3. Select the reports that you want to publish from the Select Report box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add them to the right box, or drag the required reports from the Select Report box to the right box. You can select **Add All**![Add All button](https://devnet.logianalytics.com/hc/article_attachments/9898422526743/btn_addall.gif) to add all the reports at a time. If you do not add any report, Designer only publishes the catalog.
4. Select **Browse** next to the **To Local Directory** text box to specify the directory where to publish the catalog and reports. You can also type a directory in the text box, and if you type a directory which does not exist, Designer automatically creates it for you.
5. Select **Next**. Designer displays properties of the data source connections in the catalog.

   ![Publish to Local Directory dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898457902615/pblsh_pub_local.gif)
6. From the **Catalog Data Source** drop-down list, select a data source of the catalog, then select a connection in the specified data source from the **Connection** drop-down list. Designer displays the properties of the selected connection for your reference. When you select a JDBC connection, Designer enables the **Modify** button. You can select the button to modify information of the connection in the [Get JDBC Connection Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735530237847-Get-JDBC-Connection-Information-Dialog-Box), which applies to the published connection only, meaning, the connection in Designer still applies the original settings.
7. Select **Finish** to publish the catalog and reports to the specified directory.

## Downloading Reports

You can download reports created on Server to your local computer and further modify them using Designer. The same as with publishing, Designer also downloads all resources used by the reports such as other linked reports and images.

1. Do either of the following:
   * Navigate to **File** >  **Download** > **Download Report from Server** if you want to download reports.
   * Navigate to **File** > **Download** > **Download Component from Server** if you want to download library components.

   If Designer can automatically connect to started Server and sign you in, it displays the [Download from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522490007-Download-from-Logi-Report-Server-Dialog-Box); otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499997591-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the connection and user information first.

   ![Download from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898474974999/dwldjrsrv.gif)
2. In the **Download Resource From** text box, select **Browse** to specify the folder on Server from which to download resources. Designer then loads the resources in the specified folder in the resource tree box.
3. In the resource tree box, select the checkboxes in front of the resources that you want to download.
4. Select **Browse** next to the **Download Resource To** text box to specify the path to which to download the resources, or type the directory in the text box directly.
5. Select **Download as XML Format** if you want to download the selected resources (excluding library components) in XML. Designer downloads catalogs and reports on Server that are in XML as XML resources no matter you select this checkbox or not.
6. Select **OK**. Designer then downloads the selected resources and all additional resources referenced by them such as linked reports and images from Server.

When Designer successfully downloads the resources from Server, you can open them in Designer, and further edit them.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* Server protects the resources in the Public Reports folder by permissions. If you specify to download resources from that folder, which resources you can see in the resource tree box and which resources you can download are determined by the user name with which you use to connect to Server. You can only view the resources on which you have the Visible permission in this box and download resources on which you are assigned the Read permission.
* Downloading business view-based reports from Server requires that Designer and Server each has its own [Live license](https://devnet.logianalytics.com/hc/en-us/articles/5735525627159-Logi-Report-Licenses#Live).

## Downloading Customized Controls

You can [download the customized controls](https://devnet.logianalytics.com/hc/en-us/articles/5735499153175-Using-Customized-Controls-in-Tables) on Server to the customized control library of Designer, which is the Customized Control folder under the installation root, and further modify them using Designer.

1. Navigate to **File** > **Download** > **Download Customized Control from Server**. If Designer can automatically connect to a started Server and sign you in, it displays the [Download Customized Control dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513670423-Download-Customized-Control-Dialog-Box); otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499997591-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the connection and user information first.

   ![Download Customized Control dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475001111/dwldcstmzdctrl.gif)
2. Select the customized control files you need and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add them to the right box. You can select **Add All**![Add All button](https://devnet.logianalytics.com/hc/article_attachments/9898422526743/btn_addall.gif) to add all the customized control files at a time.
3. Select **OK** to download the specified control files.
   When the local control library contains control files that have the same names with the downloaded control files, Designer replaces the local files directly without warning.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735506410263-Working-with-APIs)
