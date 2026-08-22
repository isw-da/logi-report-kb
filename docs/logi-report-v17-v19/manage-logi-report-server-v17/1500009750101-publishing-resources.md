---
title: "Publishing Resources"
id: 1500009750101
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources
updated_at: 2021-07-25T07:18:58Z
---

# Publishing Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750041-Managing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750061-Converting-Resources-of-Earlier-Versions-into-Current-Version)

# Publishing Resources

Before you can perform any tasks on Logi Report Server, you first need to have your resources published and organized in the server resource tree. You can publish resources using Logi Report Designer, from the server machine, from a local directory, or from another Logi Report Server. This topic describes publishing resources to Logi Report Server in different ways.

Select the following links to view the topics:

* [Basic Publishing Rules](#Rule)
* [Publishing Resources from Logi Report Designer](#Designer)
* [Publishing Resources from a Server Machine](#SrvMachine)
* [Publishing Resources from a Local Directory](#LocalDir)
* [Publishing Resources to Another Server](#ToServer)

**Tip:** After resources have been delivered to Logi Report Server, you may find that the publishing time shown on the server UI is different from the client time. That is because the publishing time takes the server time instead of the client time.

## Basic Publishing Rules

You can publish the following resources to folders in the Logi Report Server resource tree: catalogs, reports, library components, dashboards, and folders. However you are not able to publish resources to or from folders that come from [real paths](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path).

The built-in folders and the subfolders within them in the server resource tree can only store resources of specific types:

* My Reports, Public Reports, and Organization Reports store reports, dashboards and analysis templates with catalogs.
* My Components, Public Components, and Organization Components store library components with catalogs. In folders where library components can be published, only one catalog file is allowed.

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")In Logi Report, catalogs and page reports can be saved in either binary or XML format if your license permits. For performance concern, when you publish catalog and page report files of the XML format, Logi Report Server will parse the XML files, convert them to binary files, and then save the converted binary files in the server resource tree instead of the XML files. In this way Logi Report Server does not have to go through parsing of the XML files each time the catalogs and page reports are executed and the server performance can be greatly improved. In the meantime, catalogs and page reports saved in the server resource tree can be downloaded to Logi Report Designer in the XML format if you prefer this format for checking into source code control systems.

## Publishing Resources from Logi Report Designer

After creating catalogs, reports, and library components in Logi Report Designer, you can publish them from Logi Report Designer to Logi Report Server directly. For detailed information, refer to Publishing Resources Remotely in the *Logi Report Designer Guide*.

## Publishing Resources from Server Machine

The resources including reports, library components, catalogs, and folders that are saved in the machine where Logi Report Server runs can be easily published to the server resource tree. However if you are not an admin user of the server, you will be able to perform the task only when you are given the [Publish privilege](https://devnet.logianalytics.com/hc/en-us/articles/1500009724562-Managing-Privileges) and have the [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) on the folder where you want to publish the resources.

1. In the Logi Report Server console, open the Resources page and navigate to the folder in which to publish the resources.
2. Select **Publish** > **From Server Machine** on the task bar.

   Report Server displays the [Publish from Server Machine](https://devnet.logianalytics.com/hc/en-us/articles/1500009720902-Publish-from-Server-Machine) dialog box.

   ![Publish from Server Machine dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942502551/pubfrmsrv.gif)
3. Select a type from the Resource Type drop-down list.
4. Specify properties for the to-be-published resources as required.
   * **If the Page Report or Web Report resource type is selected:**
     1. In the From File text box, specify the report you want to publish with its full path.
     2. In the Resource Node Name field, specify a name for the report. This name is required and is used as the display name of the report in the server resource tree.
     3. Type a brief description to describe the report in the Resource Description field.
     4. From the Status drop-down list, select the status of the report.
     + **Active**  
        The report can be run, advanced run and scheduled on Logi Report Server.
     + **Inactive**  
        The report cannot be run, advanced run or scheduled on Logi Report Server.
     + **Incomplete**  
        The report is not completely designed and cannot be run, advanced run or scheduled Logi Report Server.5. Specify values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009723042-Working-with-Custom-Fields) for the report if there are custom fields.
     6. Specify the font/style/geographic information directory for the report if it uses special font, applies style group or contains geographic information.
   * **If the Catalog resource type is selected:**
     1. In the From File text box, specify the catalog you want to publish with its full path.
     2. In the Resource Node Name field, specify a name for the catalog. This name is required and is used as the display name of the catalog in the server resource tree.
     3. Type a brief description to describe the catalog in the Resource Description field.
     4. Specify values of the custom fields for the catalog if there are custom fields.
   * **If the Component resource type is selected,**
     1. In the From File text box, specify the library component you want to publish with its full path.
     2. In the Resource Node Name field, specify a name for the library component. This name is required and is used as the display name of the library component in the server resource tree.
     3. Type a brief description to describe the library component in the Resource Description field.
     4. Specify values of the custom fields for the library component if there are custom fields.
     5. Specify the font/style/geographic information directory for the library component if it uses special font, applies style group or contains geographic information.
   * **If the Folder resource type is selected:**
     1. In the Resource Node Name field, specify a name for the folder. This name is required and is used as the display name of the folder in the server resource tree.
     2. Type a brief description to describe the folder in the Resource Description field.
     3. In the Resource Real Path text box, type a local disk path as the real path of the folder. If Enable Resources from Real Paths is available, you can select it to [enable getting resources from this real path](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path). The local disk path will then be mapped into the resource node of the folder in the server resource tree and Logi Report Server can always get resources and updates from the real path.

        If this step is skipped, the publish job will simply create a new blank directory node in the server resource tree.
     4. Specify values of the custom fields for the folder if there are custom fields.
   * **If the Folder with Contents resource type is selected:**
     1. Select the **Browse** button next to the From Folder text box to specify the folder where the resources you want to publish are saved.
     2. In the Resource Node Name field, specify a name for the folder. This name is required and is used as the display name of the folder in the server resource tree.
     3. Type a brief description to describe the folder in the Resource Description field.
     4. In the Resource Real Path text box, type a local disk path as the real path of the folder. If Enable Resources from Real Paths is available, you can select it to [enable getting resources from this real path](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path). The local disk path will then be mapped into the resource node of the folder in the server resource tree and Logi Report Server can always get resources and updates from the real path.
     5. Specify values of the custom fields for the folder if there are custom fields.
     6. Specify the font/style/geographic information directory for the resources in the folder if they use special font, apply style group or contain geographic information.
     7. To publish the resources in an advanced way, select the **Advanced Publish** button and all resources contained within the specified folder will then be listed. Select the resources you want to publish and specify the properties for each resource as required.
   * **If the Catalogs, Reports and Folders in Folder or Catalogs and Reports in Folder resource type is selected:**
     1. Select the **Browse** button next to the From Folder text box to specify the folder where the resources you want to publish are saved.
     2. Specify the font/style/geographic information directory for the resources if they use special font, apply style group or contain geographic information.
     3. To publish the resources in an advanced way, select the **Advanced Publish** button and all resources contained within the specified folder will then be listed. Select the resources you want to publish and specify the properties for each resource as required.
5. When the resources you specify to publish contain reports created in earlier versions, select **Automatically Convert Old Report Schemas**, then the reports will be automatically converted into current version Logi Report reports when publishing finishes.
6. To apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy) to the resources that you are publishing,
   * For resources published to the My Reports or Public Reports folder, select the **Apply Archive Policy** option, then specify the archive policy as required: Archive as New Version or Replace Old Version.
   * For resources published to the My Components or Public Components folder, specify the maximum number of versions that will be listed in the version table of the resources.

   Note that a folder itself does not have versions. The archive policy specified for a folder applies to the folder content.
7. If you have located a public folder in [step 1](#Step1) to publish the resources and you have the Grant permission on the folder, the Set Permissions link is shown. Select the link to specify user [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) on the resources.
8. Select **OK** to start publishing the resources.

## Publishing Resources from Local Directory

In the case when you are accessing Logi Report Server from a remote computer, you can also publish the resources including reports, library components, catalogs, and folders saved in your local directories to the server resource tree, that is you can publish the resources from your local machine using a web browser to the machine where the server runs. However if you are not an admin user of the server, you will be able to perform the task only when you are given the [Publish privilege](https://devnet.logianalytics.com/hc/en-us/articles/1500009724562-Managing-Privileges) and have the [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) on the folder where you want to publish the resources.

The resource type when publishing from a local directory can ONLY be a compressed file. You should compress the resources in advance, and if special fonts are used in the reports or library components, add the corresponding font files into the compressed file as well. There are two approaches to building a compressed file.

* You can compress the resources manually using a third-party tool, such as Winzip and gzip.
* You can use jar.exe that the JSDK provides to build a compressed jar file directly. Use the command as follows:

  | Parameter | Description |
  | --- | --- |
  | %JAVAHOME% | The Java SDK install root. |
  | %DEST\_JAR\_FILE% | The destination file path and file name. The .jar file will be generated to the path you specify here, using the file name you provide. |
  | %SOURCE\_RESOURCES% | The source file path and file name. Note that specifying a path for this parameter will cause the generated jar file to contain the same path information. For example, when you extract a jar file compressed using `myReports\*.*` for this parameter, the files will be extracted to a folder called `myReports`. Logi Report Server is not able to import a compressed file which contains the path information, so do not specify a path for this parameter. |

  `%JAVAHOME%\bin\jar.exe -cvfM %DEST_JAR_FILE% %SOURCE_RESOURCES%`

  To generate a jar file containing no path information, switch to the source folder, and then carry out the compression. For example,

  `C:\myReports>C:\jdk1.8.0\bin\jar -cvfM C:\temp\aa.jar.`

  The jar file will be generated to `C:\temp`, as aa.jar, compressing all the files in `C:\myReports`, and containing no path information.

  Always use this method if the folder you are compressing contains reports or library components with Chinese, Korean, or Japanese names.

**To publish resources from a local directory to the server resource tree:**

1. In the Logi Report Server console, open the Resources page and navigate to the folder in which to publish the resources.
2. Select **Publish** > **From Local Directory** on the task bar.

   Report Server displays the [Publish from Local Directory](https://devnet.logianalytics.com/hc/en-us/articles/1500009720882-Publish-to-Remote-Server-) dialog box.

   ![Publish from Local Directory dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936799383/pubfrmdir.gif)
3. Select the **Browse** button to specify the zipped file in the local directory which contains the resources you want to publish.
4. Specify where the resources will be published.
   * If you want to publish the resources directly to the current open folder, select the **Publish files and folders in the zipped file to /XXX** check box.
   * If you want to create a new folder in the current open folder to locate the resources,
     1. Make sure the Publish files and folders in the zipped file to /XXX check box is not selected.
     2. In the Resource Node Name box, specify the name of the folder. The name will be used as the display name of the folder in the server resource tree.
     3. Type a brief description to describe the folder in the Resource Description box.
     4. Specify values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009723042-Working-with-Custom-Fields) for the folder if there are custom fields.
     5. In the Resource Real Path text box, type a local disk path as the real path of the folder. If Enable Resources from Real Paths is available, you can select it to [enable getting resources from this real path](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path). The local disk path will then be mapped into the resource node of the folder in the server resource tree and Logi Report Server can always get resources and updates from the real path.
5. When the resources you specify to publish contain reports created in earlier versions, select **Automatically Convert Old Report Schemas**, then the reports will be automatically converted into current version Logi Report reports when publishing finishes.
6. To apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy) to the resources that you are publishing,
   * For resources published to the My Reports or Public Reports folder, select the **Apply Archive Policy** option, then specify the archive policy as required: Archive as New Version or Replace Old Version.
   * For resources published to the My Components or Public Components folder, specify the maximum number of versions that can be listed in the version table of the resources.
7. If you have located a public folder in [step 1](#LocalStep1) to publish the resources and you have the Grant permission on the folder, the Set Permissions link is shown. Select the link to specify user [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) on the resources.
8. To publish the resources in an advanced way, select the **Advanced Publish** button and all resources contained within the zip file will then be listed. Select the resources you want to publish and specify the properties for each resource as required.
9. Select **OK** to start publishing the resources.

## This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Publishing Resources to Another Server

You can publish the resources including catalogs, reports, library components, dashboards, and folders in the resource tree of a Logi Report Server to another Logi Report Server, provided that you are a user of both servers and have the [Publish privilege](https://devnet.logianalytics.com/hc/en-us/articles/1500009724562-Managing-Privileges) on both servers. For easy explanation, in the following content, source server is used to referred to the Logi Report Server from which resources will be published and target server to the Logi Report Server to which resources will be published.

When you publish resources from one server to another, Logi Report tries to replicate the resources on the target server as precisely as possible, but there are still some rules and limitations you should be aware of:

* Reports with the Inactive or Incomplete status and [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports) cannot be published.
* To publish library components and dashboards, you should make sure the target server has the [JDashboard license](https://devnet.logianalytics.com/hc/en-us/articles/1500009749561-Logi-Report-licenses#JDashboard).
* The [custom field values](https://devnet.logianalytics.com/hc/en-us/articles/1500009723042-Working-with-Custom-Fields) defined on resources on the source server will not be copied to the target server.
* Plug-ins and customized controls cannot be published to the target server.
* When a to-be-published resource references other resources, for example a report is linked to other reports, the referenced resources will also be published automatically to the same location on the target server as in the source server. However, if you do not have the [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) on the target location or the target location [enables getting resources from path path](https://devnet.logianalytics.com/hc/en-us/articles/1500009750141-Getting-and-Using-Resources-from-a-Real-Path), neither the resource nor the referenced resources will be published. When the target location already contains resources that are of the same names as the referenced resources, they will be overwritten directly.
* In the case when a source server resource is to overwrite the same target server resource, the source server resource will follow the [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009723202-Applying-an-Archive-Policy) of the target server resource.
* By default, the latest [version](https://devnet.logianalytics.com/hc/en-us/articles/1500009750181-Managing-Versions) of the resources (including referenced resources) on the source server will be published. When the latest version of a resource is enabled with [NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level) on the source server, its NLS setting will also be copied to the target server and overwrite the NLS on the target server directly if conflict occurs.
* When a catalog on the source server contains [dynamic connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009718782-Creating-and-Using-Dynamic-Connections), [dynamic security](https://devnet.logianalytics.com/hc/en-us/articles/1500009724442-Dynamic-Security) and [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/1500009723082-Managing-Dynamic-Display-Names-of-Business-View-Elements) settings, these dynamic settings will also be copied to the target server while you publish the catalog and overwrite those on the target server directly if conflict occurs.

**To publish resources from one server to another:**

1. Open the console of the source server and access its Resources page.
2. Select **Publish** > **To Server** on the task bar. If it remembers your login information, the source server displays the [Publish to Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009720862-Publish-to-Local-Server) dialog box; otherwise it displays the [Login Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009747461-Login-Server) dialog box, prompting you to log in.

   **To log onto the target server:**

   1. In the Host text box of the Login Server dialog box, type the host of the target Logi Report Server. You can use the host name or the IP address of the target server.

      ![Login Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936799639/loginsrv.gif)
   2. In the Post text box, type the port that the target server listens to.
   3. In the Servlet Path text box, specify the servlet path of the target server which will be used in the URL to access the servlet. The servlet path is /jrserver when the target server is a standalone server. If the target Logi Report Server is an embedded server, for example jreport.jar the servlet path would be /jreport/jrserver.
   4. You can select **SSL** to create an SSL (Security Socket Layer) connection when the target server is integrated with another web server which supports SSL.
   5. In the User Name text box, type the user name used to access the target server. If you log onto the source server as an [organization user](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations), the same organization name will be used to log you onto the target server by default, therefore if the target server does not have the same organization, your login will be denied.
   6. Select **Remember Me** to have the source server remember the login information, so that you can log onto the target server automatically when you want to publish resources to it. The login information can be remembered till the source server is restarted.
   7. Select **Connect** to set up the connection with the target server and log in.

      After logging in successfully, Report Server displays the Publish to Server dialog box.
3. The Publish To
   option in the Publish to Server dialog box shows the URL using which you have logged onto the target server. You can select **Change Login Settings**
   to edit the [login information](#Login).

   ![Publish to Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936799895/pub2srv.gif)
4. Select the **Browse** button next to the Target Path text box, then in the [Select Folder](https://devnet.logianalytics.com/hc/en-us/articles/1500009747961-Select-Folder) dialog box, select the folder in the target server where the resources will be published. You can select from the folders on which you have the [Visible and Write permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) (an organization user can select from folders in his organization that match the same prerequisites). The target folder you select determines which kind of resources you can publish from the source server. For example, if you select the built-in folder My Components as the target folder, you will only be able to publish library component and catalog resources from the source server.
5. Select the **Browse** button next to the Source Path text box to select the folder in the source server where to get the resources. Based on your selection for the target folder, only the folders that function the same as the target folder and on which you have the Visible permission will be listed for you to select as the source folder.
6. All the available resources on which you have the Visible permission in the specified source folder are now displayed in the Resources box. Select the resources you want to publish and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404942476823/btn_add.gif) to add them to the Selected box. If a folder is selected, the folder with all available resources in it will be added. To remove a resource from the Selected box, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404936763159/btn_rmv.gif).
7. Select **Publish** to publish the selected resources to the target server.

   When resources with the same names already exist in the target server, you will be prompted to deal with the conflicts. Make the choice accordingly.

Developer users can also publish resources from one server to another using [API methods](https://devnet.logianalytics.com/hc/en-us/articles/1500009718562-Publishing-Resources-from-One-Server-to-Another).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750041-Managing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750061-Converting-Resources-of-Earlier-Versions-into-Current-Version)
