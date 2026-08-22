---
title: "Publishing and Downloading Resources"
id: 1500010062722
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources
updated_at: 2021-07-23T19:16:48Z
---

# Publishing and Downloading Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099241-Exporting-Reports-to-Accessible-HTML-and-PDF)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093681-Working-with-APIs)

# Publishing and Downloading Resources

Designer, as a report design tool, enables you to publish your resources from it to your local computer or to Server. When you publish a resource such as a report template, Designer publishes all of the referenced report templates and additional resources such as images although they are not visible. This ensures that images and linked reports are available at runtime. In addition, you can download reports created on Sever to a specified folder on your local computer and further modify them in Designer. This topic describes publishing and downloading different resources using Designer.

In Designer, you can save catalogs and page reports in either binary or [in XML](https://devnet.logianalytics.com/hc/en-us/articles/1500010094061-Knowing-About-Catalogs#Format). For performance concern, when you publish catalog and page report files saved in XML to Server, Server parses the XML files, converts them to binary files, and then saves the converted binary files into its resource system instead of the XML files. In this way, Server does not have to go through parsing of the XML files each time the catalogs and page reports are executed, so that its performance can be greatly improved. In the meantime, when you download catalogs and page reports from the resource system of Server to Designer, you can download them in XML if you prefer this format for checking into source code control systems.

This topic contains the following sections:

* [Publishing Resources Remotely](#Remotely)
  + [Publishing Reports](#PubReport)
  + [Publishing Additional Resources](#Additional)

* [Publishing Resources Locally](#Locally)
* [Downloading Reports](#DownReport)
* [Downloading Customized Controls](#DownCtrl)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Before you can publish or download resources from Server, you need to make sure it is started. You can pre-set the properties for connecting with Server and user information to login via the [Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098161-Options-Dialog-Box#Server) to avoid repeated connecting and logging.

## Publishing Resources Remotely

You can publish different resources to Server, which include [reports](#PubReport) and [additional resources](#Additional).

### Publishing Reports

When publishing reports to Server, you are actually copying the files into a sub folder in the `<server_install_root>/history` folder. The Server database keeps track of physical disk locations and maps those to logical folders shown in its resource tree.

1. Do either of the following:
   * Select **File** > **Publish** > **Publish Report to Server** if you want to publish reports.
   * Select **File** > **Publish** > **Publish Component to Server** if you want to publish library components.

   If Designer can automatically connect to Server and log you in, it displays the [Publish to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098281-Publish-to-Logi-Report-Server-Dialog-Box); otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the information for connecting with Server first.

   ![Publish to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848420887/pubjrsrv.gif)
2. Select the **Browse** button next to the **Publish Resource From** text box to find the directory where your resources are located, Designer then loads the resources in the specified directory automatically into the resource box. If you choose to type the directory in the text box, you need to press Enter on the keyboard to load the resources in that directory.
3. In the resource box, select the checkboxes in front of the resources that you want to publish. To publish all the resources in the specified directory, select **All**.
4. In the **Publish Resource To** text box, select the **Browse** button to specify the folder in the resource tree of Server where to publish the resources.
5. Select a to-be-published resource in the resource box and then select the **More Options** button to set its properties.
6. In the **Properties** tab,
   1. In the **Resource Node Name** text box, specify a name that displays in the resource tree of Server for the resource. You can type a name in the text box or use the **Browse** button to select a resource name from the Select Resource Name dialog box, which lists all the resource names of the same type as the selected resource stored in the path where you specify to publish the resources on Server.
   2. In the **Resource Description** text box, type a brief description to describe the resource.
   3. If the selected resource is a report, specify the status of the report by selecting the required item from the **Status** drop-down list:
      * **Active**  
        Select it and end users can run, advanced run, and schedule the report on Server.
      * **Inactive**  
        Select it and end users are not able to run, advanced run, or schedule the report on Server.
      * **Incomplete**  
        Select it if the report is not completely designed, then end users are not able to run, advanced run, or schedule it on Server.
   4. If the selected resource is a folder, type a local disk path in the **Resource Real Path** text box as the real path of the folder. If you would like to map the real path resources into the new node created for the folder in the resource tree of Server, so that Server is always able to get the resources and updates from the real path, select **Enable Resources from Real Paths**. However, once you create a real path folder, you can no longer publish reports to it from Designer. You need to physically copy the files you want to publish into the specified folder on Server.
   5. In the **Custom Field** panel, specify custom field values for the resource if there are custom fields enabled on Server.
   6. Select **Apply Archive Policy** to apply an archive policy to the resource.
      * To use multiple versions for the selected resource, select **Archive as New Version**, then in the **Max Number of Versions** text box, type the maximum number of versions that Server maintains in the version table of the selected resource. The default value is 0, which means that the version amount is unlimited.
      * To replace the old version when a new version is generated, select **Replace Old Version.**
7. Designer enables the **Permissions** tab if you specify to publish the resources to a public folder on Server. You can specify user permissions for the selected resource.

   Select **Enable Setting Permissions**, then in the **Role**, **User**, or **Group** tab, select a role, user, or group from the principal box and select the checkboxes ahead of the required permissions. The principal boxes by default contains all the roles, users, and groups in the security system of Server. You can remove a principal in any box by selecting it and selecting the **Remove** button. To add the deleted principal back, use the **Add** button. For more information about the permissions, see Managing Permissions in the *Logi Report Server Guide*.

   ![Publish to Logi Report Server dialog box - Permission tab](https://devnet.logianalytics.com/hc/article_attachments/4404848421399/pblsh_pub_rpt1.gif)
8. Designer enables the **Connection** tab if the selected resource is a catalog. Select a data source of the catalog from the **Catalog Data Source** drop-down list, and then a connection in the selected data source from the **Connection** drop-down list. Designer displays the properties of the selected connection for your reference. If the selected connection is a JDBC connection, Designer enables the **Modify** button. You can select the button to modify information of the connection in the [Get JDBC Connection Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097761-Get-JDBC-Connection-Information-Dialog-Box), which applies to the connection published to Server only, meaning, the connection in Designer still applies the original settings.

   ![Data Source Connection Properties](https://devnet.logianalytics.com/hc/article_attachments/4404848421655/pblsh_pub_rpt2.gif)
9. Repeat steps 5 - 7 to set properties for other resources.
10. Select **OK** to publish the resources to Server. If the reports or library components use special fonts, style groups, geographic information, or customized control files, Designer displays the [Publish Additional Resources dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060202-Publish-Additional-Resources-Dialog-Box) for you to [specify them](#Additional).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* Server only allows one catalog file in folders in its resource tree where you can publish library components.
* You can select the Enable Resources from Real Paths option only when the Server administrator has selected the same option on the Server Console > Administration > Configuration > Advanced page.
* If you have made some changes to the to-be-published resources, but have not saved them, before publishing starts, Designer saves the changes automatically to ensure the resources published to Server are the latest.
* After you finish publishing resources to Server, you may find that the publishing time shown on the Server UI is different from the client time. That is because the publishing time takes the Server time instead of the client time.
* If the resource you publish to on Server is already a real path resource, you get a permission denied error. You can only publish real path resources by copying the files physically using FTP or OS copy file utilities.

### Publishing Additional Resources

You can also publish additional resources that your reports use to Server. These resources include [special fonts](https://devnet.logianalytics.com/hc/en-us/articles/1500010101401-Applying-True-Type-Fonts-in-Reports), [geographic information](https://devnet.logianalytics.com/hc/en-us/articles/1500010057302-Using-Geographic-Maps), [style groups](https://devnet.logianalytics.com/hc/en-us/articles/1500010101461-Working-with-XSD-Styles), and [customized control files](https://devnet.logianalytics.com/hc/en-us/articles/1500010057402-Using-Customized-Controls-in-Tables).

1. Select **File** > **Publish** > **Publish Other Files to Server**.

   If Designer can automatically connect to Server and log you in, it displays the [Publish Additional Resources dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060202-Publish-Additional-Resources-Dialog-Box); otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the properties for connecting with Server first.

   ![Publish Additional Resources dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848421911/pubadtnlrsc.gif)
2. If special fonts are available, select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to specify the folder containing the special fonts.
3. In the **Style** tab, select the required style groups in the left box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add them to the right box. You can select ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404848391575/btn_addall.gif) to add all the style groups at a time.
4. In the **Geographic Information** tab, add the XML files that store the geographic information your reports apply.

   ![Publish Additional Resources dialog box - Geographic Information tab](https://devnet.logianalytics.com/hc/article_attachments/4404856841111/pblsh_pub_adtn1.gif)
5. In the **Customized Control** tab, add the customized control files you need.

   ![Publish Additional Resources dialog box - Customized Control tab](https://devnet.logianalytics.com/hc/article_attachments/4404848422423/pblsh_pub_adtn2.gif)
6. Select **OK** to publish the resources to Server.

## Publishing Resources Locally

Designer supports publishing resources locally, that is, publishing resources to any directory on your computer or across your intranet.

1. Select **File** > **Publish** > **Publish to Local Directory**. Designer displays the [Publish to Local Directory dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060222-Publish-to-Local-Directory-Dialog-Box).

   ![Publish to Local Directory dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848422679/publocal.gif)
2. Select the **Browse** button to select a catalog, or type the catalog file name with its full path in the **From Catalog** text box and press Enter to specify the catalog. Designer then lists all the page reports and web reports in the specified catalog in the **Select Report** box.
3. Select the reports that you want to publish from the Select Report box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add them to the right box, or drag the required reports from the Select Report box to the box on the right. You can select ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404848391575/btn_addall.gif) to add all the reports at a time. If you do not add any report, Designer only publishes the catalog.
4. Select the **Browse** button to the right of the **To Local Directory** text box to specify the directory where to publish the catalog and reports. You can also type a directory in the text box, and if you type a directory which does not exist, Designer automatically creates it for you.
5. Select **Next** to view and modify properties of the data source connections in the catalog.

   ![Publish to Local Directory dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856841367/pblsh_pub_local.gif)

   Select a data source of the catalog from the **Catalog Data Source** drop-down list, and then a connection in the selected data source from the **Connection** drop-down list. Designer displays the properties of the selected connection for your reference. If the selected connection is a JDBC connection, Designer enables the **Modify** button. You can select the button to modify information of the connection in the [Get JDBC Connection Information dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097761-Get-JDBC-Connection-Information-Dialog-Box), which applies to the published connection only, meaning, the connection in Designer still applies the original settings.
6. Select **Finish** to publish the catalog and reports to the specified directory.

## Downloading Reports

You can download reports created on Server to your local computer and further modify them using Designer. The same as with publishing, Designer also downloads all resources used by the reports such as other linked reports and images.

1. Do either of the following:
   * Select **File** >  **Download** > **Download Report from Server** if you want to download reports.
   * Select **File** > **Download** > **Download Component from Server** if you want to download library components.

   If Designer can automatically connect to Server and log you in, it displays the [Download from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096141-Download-from-Logi-Report-Server-Dialog-Box); otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the properties for connecting with Server first.

   ![Download from Logi Report Server dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856841623/dwldjrsrv.gif)
2. In the **Download Resource From** text box, select the **Browse** button to specify the folder on Server from which to download resources. Designer then loads the resources in the specified folder in the resource tree box.
3. In the resource tree box, select the checkboxes in front of the resources that you want to download.
4. Select the **Browse** button next to the **Download Resource To** text box to specify the path to which to download the resources, or type the directory in the text box directly.
5. Select **Download as XML Format** if you want to download the selected resources in XML. You can only save catalogs and page reports in this format. Designer downloads catalogs and page reports on Server which are in XML as XML resources by default no matter you select this checkbox or not.
6. Select **OK**. Designer then downloads the selected resources and all additional resources referenced by them such as linked reports and images from Server.

When Designer successfully downloads the resources from Server, you can open them in Designer, and further edit them.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* Server protects the resources in the Public Reports folder by permissions. If you specify to download resources from that folder, which resources you can see in the resource tree box and which resources you can download are determined by the user name with which you use to connect to Server. You can only view the resources on which you have the Visible permission in this box and download resources on which you are assigned the Read permission.
* Downloading reports which use business views as data source from Server requires that Designer and Server each has its own [Live license](https://devnet.logianalytics.com/hc/en-us/articles/1500010061082-Logi-Report-Licenses#Live).

## Downloading Customized Controls

You can [download the customized controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010057402-Using-Customized-Controls-in-Tables) on Server to the customized control library of Designer, which is the Customized Control folder under the installation root, and further modify them using Designer.

1. Select **File** > **Download** > **Download Customized Control from Server**.

   If Designer can automatically connect to Server and log you in, it displays the [Download Customized Control dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058662-Download-Customized-Control-Dialog-Box); otherwise, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the properties for connecting with Server first.

   ![Download Customized Control dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848423575/dwldcstmzdctrl.gif)
2. Select the customized control files you need and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) to add them to the right box. You can select ![Add All button](https://devnet.logianalytics.com/hc/article_attachments/4404848391575/btn_addall.gif) to add all the customized control files at a time.
3. Select **OK** to download the selected control files.

   If the local control library contains control files that have the same names with the downloaded control files, Designer replaces the local files directly without warning.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099241-Exporting-Reports-to-Accessible-HTML-and-PDF)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093681-Working-with-APIs)
