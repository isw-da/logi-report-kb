---
title: "Publishing Resources"
id: 5741453495191
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741453495191-Publishing-Resources
updated_at: 2022-10-31T17:18:08Z
---

# Publishing Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741438016279-Managing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741474096919-Converting-Resources-of-Earlier-Versions-to-the-Current-Version)

# Publishing Resources

You need to publish and organize your resources in the server resource tree before performing tasks on them. This topic describes how you can publish resources using Logi Report Designer, from the server computer, from a local directory, or from another Logi Report Server.

This topic contains the following sections:

* [Basic Publishing Rules](#Rule)
* [Publishing Resources from Designer](#Designer)
* [Publishing Resources from Server Machine](#SrvMachine)
* [Publishing Resources from Local Directory](#LocalDir)
* [Publishing Resources to Another Server](#ToServer)

**Tip:** After you have delivered resources to Server, you may find that the publishing time shown on the server UI is different from the client time. That is because the publishing time takes the server time instead of the client time.

## Basic Publishing Rules

You can publish the following resources to folders in the server resource tree: catalogs, reports, library components, dashboards, and folders. However, you are not able to publish resources to or from folders that come from [real paths](https://devnet.logianalytics.com/hc/en-us/articles/5741482166807-Getting-and-Using-Resources-From-a-Real-Path).

The built-in folders and the sub folders within them in the server resource tree can only store resources of specific types:

* My Reports, Public Reports, and Organization Reports store reports, dashboards, and analysis templates with catalogs.
* My Components, Public Components, and Organization Components store library components with catalogs. In folders where you can publish library components, Server allows only one catalog file.

In Logi Report, you can save catalogs and page reports in either binary or XML format if your license permits. For performance concern, when you publish catalog and page report files of the XML format, Server parses the XML files, converts them to binary files, and then saves the converted binary files in the server resource tree instead of the XML files. In this way, Server does not have to go through parsing of the XML files each time the catalogs and page reports run and therefore it can greatly improve the server performance. In the meantime, you can download catalogs and page reports from the server resource tree to Logi Report Designer in the XML format if you prefer this format for checking into source code control systems.

## Publishing Resources from Designer

After creating catalogs, reports, and library components in Logi Report Designer, you can publish them from Logi Report Designer to Logi Report Server directly. For more information, see Publishing Resources Remotely in the *Logi Report Designer Guide*.

## Publishing Resources from Server Machine

You can easily publish resources, including reports, library components, catalogs, and folders, in the computer where Logi Report Server runs, to the server resource tree. However, if you are not a Server administrator, you will be able to perform the task only when you have the [Publish privilege](https://devnet.logianalytics.com/hc/en-us/articles/5741455284119-Managing-Privileges) and have the [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) on the folder where you want to publish the resources.

1. On the Server Console, open the Resources page and navigate to the folder in which to publish the resources.
2. Select **Publish** > **From Server Machine** on the task bar.

   Server displays the [Publish from Server Machine dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741421379351-Publish-from-Server-Machine-Dialog-Box-Properties).

   ![Publish from Server Machine dialog](https://devnet.logianalytics.com/hc/article_attachments/9905714441879/pubfrmsrv.gif)
3. Select a type from the **Resource Type** list.
4. Specify properties for the resources you are to publish.
   * If you selected the **Page Report or Web Report** resource type,
     1. In the **From File** text box, type the path of the report you want to publish. System administrators can select **Browse** to specify the file.
     2. In the **Resource Node Name** text box, you need to provide the display name of the report in the server resource tree.
     3. Type a brief description to describe the report in the **Resource Description** text box.
     4. From the **Status** list, select the status of the report.
     + **Active**  
        You can run, advanced run, and schedule to run the report on the server.
     + **Inactive**  
        You cannot run, advanced run, or schedule to run the report on the server.
     + **Incomplete**  
        You haven't finished designing the report. You cannot run, advanced run, or schedule to run it on the server.5. Specify the values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/5741461739671-Working-with-Custom-Fields) for the report if you see them.
     6. Specify the font/style/geographic information directory for the report if it uses special font, applies style group, or contains geographic information.
   * If you selected the **Catalog** resource type,
     1. In the **From File** text box, type the path of the catalog you want to publish. System administrators can select **Browse** to specify the file.
     2. In the **Resource Node Name** text box, you need to provide the display name of the catalog in the server resource tree.
     3. Type a brief description to describe the catalog in the **Resource Description** text box.
     4. Specify the values of the custom fields for the catalog if you see them.
   * If you selected the **Component** resource type,
     1. In the **From File** text box, type the path of the library component you want to publish. System administrators can select **Browse** to specify the file.
     2. In the **Resource Node Name** text box, you need to provide the display name of the library component in the server resource tree.
     3. Type a brief description to describe the library component in the **Resource Description** text box.
     4. Specify the values of the custom fields for the library component if you see them.
     5. Specify the font/style/geographic information directory for the library component if it uses special font, applies style group, or contains geographic information.
   * If you selected the **Folder** resource type,
     1. In the **Resource Node Name** text box, you need to provide the display name of the folder in the server resource tree.
     2. Type a brief description to describe the folder in the **Resource Description** text box.
     3. In the **Resource Real Path** text box, type a path in the hard drive as the real path of the folder. If you see **Enable Resources from Real Paths**, you can select it to [enable getting resources from this real path](https://devnet.logianalytics.com/hc/en-us/articles/5741482166807-Getting-and-Using-Resources-From-a-Real-Path). Server maps the hard drive path to the resource node of the folder in the server resource tree and can always get resources and updates from the real path.

        If you skip this step, Server will just create a new blank directory node in the server resource tree.
     4. Specify the values of the custom fields for the folder if you see them.
   * If you selected the **Folder with Contents** resource type,
     1. In the **From Folder** text box, specify the path of a folder containing the resources you want to publish. System administrators can select **Browse** to specify the folder.
     2. In the **Resource Node Name** text box, you need to provide the display name of the folder in the server resource tree.
     3. Type a brief description to describe the folder in the **Resource Description** text box.
     4. In the **Resource Real Path** text box, type a hard drive path as the real path of the folder. If you see **Enable Resources from Real Paths**, you can select it to [enable getting resources from this real path](https://devnet.logianalytics.com/hc/en-us/articles/5741482166807-Getting-and-Using-Resources-From-a-Real-Path). Server maps the hard drive path to the resource node of the folder in the server resource tree and can always get resources and updates from the real path.
     5. Specify the values of the custom fields for the folder if you see them.
     6. Specify the font/style/geographic information directory for the resources in the folder if they use special font, apply style group, or contain geographic information.
     7. To publish the resources in an advanced way, select **Advanced Publish**. Server lists the resources that the specified folder contains. Select the resources you want to publish and specify the properties for them.
   * If you selected the **Catalogs Reports and Folders in Folder** or **Catalogs and Reports in Folder** resource type,
     1. In the **From Folder** text box, specify the path of a folder containing the resources you want to publish. System administrators can select **Browse** to specify the folder.
     2. Specify the font/style/geographic information directory for the resources if they use special font, apply style group, or contain geographic information.
     3. To publish the resources in an advanced way, select **Advanced Publish**. Server lists the resources that the specified folder contains. Select the resources you want to publish and specify the properties for them.
5. When the resources you select to publish contain reports that you created in earlier versions, select **Automatically Convert Old Report Schema**. Server automatically converts the reports to the current version when it finishes publishing the resources.
6. To apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy) to the resources that you are publishing,
   * For resources that you publish to the My Reports or Public Reports folder, select **Apply Archive Policy**, then specify the archive policy: **Archive as New Version** or **Replace Old Version**.
   * For resources that you publish to the My Components or Public Components folder, specify the maximum number of versions that the resources can have.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)A folder itself does not have versions. The archive policy for a folder applies to the resources in the folder.
7. If you have located a public folder in [step 1](#Step1) to publish the resources to and you have the **Grant** permission on the folder, you can select **Set Permissions** to specify user [permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) on the resources.
8. Select **OK** to start publishing the resources.

## Publishing Resources from Local Directory

In the case when you are accessing Server from a remote computer, you can also publish resources including reports, library components, catalogs, and folders from your local directories to the server resource tree, that is you can publish resources from your local computer using a web browser to the computer where the server runs. However, if you are not an administrator, you will be able to perform the task only when you have the [Publish privilege](https://devnet.logianalytics.com/hc/en-us/articles/5741455284119-Managing-Privileges) and have the [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) on the folder where you want to publish the resources.

The resource type when publishing from a local directory can ONLY be a compressed file. You should compress the resources in advance. If the reports or library components use special fonts, add the corresponding font files into the compressed file as well. You have two approaches to building a compressed file.

* You can compress the resources manually using a third-party tool, such as Winzip and gzip.
* You can use **jar.exe** that the JSDK provides to build a compressed jar file directly. Use the commands:

  | Parameter | Description |
  | --- | --- |
  | %JAVAHOME% | The Java SDK install root. |
  | %DEST\_JAR\_FILE% | The destination file path and file name. Server generates the .jar file to the path you specify here, using the file name you provide. |
  | %SOURCE\_RESOURCES% | The source file path and file name. Note iconSpecifying a path for this parameter will cause the generated jar file to contain the same path information. For example, when you extract a jar file compressed using `myReports\*.*` for this parameter, Server extracts the files to a folder called myReports. Server cannot import a compressed file that contains the path information, so do not specify a path for this parameter. |

  `%JAVAHOME%\bin\jar.exe -cvfM %DEST_JAR_FILE% %SOURCE_RESOURCES%`

  To generate a jar file containing no path information, switch to the source folder, and then carry out the compression. For example,

  `C:\myReports>C:\jdk1.8.0\bin\jar -cvfM C:\temp\aa.jar.`

  Server compresses all the files in `C:\myReports` and generates the jar file to `C:\temp`, as aa.jar which contains no path information.

  Always use this method if the folder you are compressing contains reports or library components with Chinese, Korean, or Japanese names.

**To publish resources from a local directory to the server resource tree:**

1. On the Server Console, open the Resources page and navigate to the folder that you want to publish the resources to.
2. Select **Publish** > **From Local Directory** on the task bar.

   Server displays the [Publish from Local Directory dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741427653783-Publish-from-Local-Directory-Dialog-Box-Properties).

   ![Publish from Local Directory dialog](https://devnet.logianalytics.com/hc/article_attachments/9905676071703/pubfrmdir.gif)
3. Select **Browse** to specify the zipped file in the local directory which contains the resources you want to publish.
4. Specify where you want to publish the resources.
   * If you want to publish the resources directly to the current open folder, select **Publish files and folders in the zipped file to /XXX**.
   * If you want to create a new folder in the current open folder to hold the resources,
     1. Do not select **Publish files and folders in the zipped file to /XXX**.
     2. In the **Resource Node Name** text box, provide the display name of the folder in the server resource tree.
     3. Type a brief description to describe the folder in the **Resource Description** text box.
     4. Specify the values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/5741461739671-Working-with-Custom-Fields) for the folder if you see them.
     5. In the **Resource Real Path** text box, type a hard drive path as the real path of the folder. If you see **Enable Resources from Real Paths**, you can select it to [enable getting resources from this real path](https://devnet.logianalytics.com/hc/en-us/articles/5741482166807-Getting-and-Using-Resources-From-a-Real-Path). Server maps the hard drive path to the folder in the server resource tree and can get resources and updates from the real path.
5. When the resources you specify to publish contain reports that you created in earlier versions, select **Automatically Convert Old Report Schemas**. Server automatically converts the reports to current version when it finishes publishing.
6. To apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy) to the resources that you are publishing,
   * For resources that you want to publish to the My Reports or Public Reports folder, select **Apply Archive Policy**, then specify the archive policy: **Archive as New Version** or **Replace Old Version**.
   * For resources that you want to publish to the My Components or Public Components folder, specify the maximum number of versions that the resources can have.
7. If you have located a public folder in [step 1](#LocalStep1) to publish the resources to and you have the **Grant** permission on the folder, you can select **Set Permissions** to specify user [permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) on the resources.
8. To publish the resources in an advanced way, select **Advanced Publish**. Server lists the resources that the zip file contains. Select the resources you want to publish and specify their properties.
9. Select **OK** to start publishing the resources.

## Publishing Resources to Another Server

You can publish the resources including catalogs, reports, library components, dashboards, and folders in the resource tree of a Logi Report Server to another Logi Report Server, provided that you are a user of both servers and have the [Publish privilege](https://devnet.logianalytics.com/hc/en-us/articles/5741455284119-Managing-Privileges) on both servers. Developer users can also publish resources from one server to another using [API methods](https://devnet.logianalytics.com/hc/en-us/articles/5741400553623-Publishing-Resources-from-One-Server-to-Another).

For easy explanation, in the following contents, we publish resources from the source server to the target server.

When you publish resources from one server to another, Logi Report tries to replicate the resources on the target server as precisely as possible, but there are still some rules and limitations you should be aware of:

* You cannot publish reports whose status are Inactive or Incomplete or [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports).
* To publish library components and dashboards, you should make sure the target server has [JDashboard license](https://devnet.logianalytics.com/hc/en-us/articles/5741452341143-Logi-Report-Licenses#JDashboard).
* Server does not copy the [custom field values](https://devnet.logianalytics.com/hc/en-us/articles/5741461739671-Working-with-Custom-Fields) that you defined on resources on the source server to the target server.
* You cannot publish plug-ins and customized controls to the target server.
* When a resource that you are to publish references other resources, for example you linked a report to other reports, Server automatically publishes the referenced resources to the same location on the target server as in the source server. However, if you do not have the [Write permission](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) on the target location or the target location [enables getting resources from path](https://devnet.logianalytics.com/hc/en-us/articles/5741482166807-Getting-and-Using-Resources-From-a-Real-Path), Server publishes neither the resource nor the referenced resources. When the target location already contains resources that are of the same names as the referenced resources, Server replaces them with the referenced resources directly.
* In the case when a source server resource is to replace the same target server resource, the source server resource follows the [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/5741482308887-Applying-an-Archive-Policy) of the target server resource.
* By default, Server publishes the latest [version](https://devnet.logianalytics.com/hc/en-us/articles/5741462048023-Managing-Resource-Versions) of the resources (including referenced resources) on the source server. When the latest version of a resource enables [NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741482629911-NLS-at-Report-Level) on the source server, Server also copies its NLS setting to the target server and replaces the NLS on the target server directly if conflict occurs.
* When a catalog on the source server contains [dynamic connection](https://devnet.logianalytics.com/hc/en-us/articles/5741395796375-Creating-and-Using-Dynamic-Connections), [dynamic security](https://devnet.logianalytics.com/hc/en-us/articles/5741483705367-Dynamic-Security), or [dynamic display name](https://devnet.logianalytics.com/hc/en-us/articles/5741468400151-Managing-Dynamic-Display-Names-of-Business-View-Elements) setting, Server also copies these dynamic settings to the target server while you publish the catalog and replaces those on the target server directly if conflict occurs.

**To publish resources from one server to another:**

1. Open the Console of the source server and access its Resources page.
2. Select **Publish** > **To Server** on the task bar. If it remembers your signing in information, the source server displays the [Publish to Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741421317271-Publish-to-Server-Dialog-Box-Properties); otherwise it displays the [Login Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741420798871-Login-Server-Dialog-Box-Properties), prompting you to sign in.

   **To sign in to the target server:**

   1. In the **Host** text box of the Login Server dialog box, type the host of the target server. You can use the host name or IP address of the target server.

      ![Login Server dialog](https://devnet.logianalytics.com/hc/article_attachments/9905714478743/loginsrv.gif)
   2. In the **Post** text box, type the port that the target server listens to.
   3. In the **Servlet Path** text box, specify the servlet path of the target server for accessing the servlet via URL. The servlet path is **/jrserver** when the target server is a standalone server. If the target server is an embedded server, for example jreport.jar, the servlet path will be **/jreport/jrserver**.
   4. You can select **SSL** to create an SSL (Security Socket Layer) connection when the target server integrates with another web server which supports SSL.
   5. In the **User Name** text box, type the username to access the target server. If you sign in to the source server as an [organization user](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations), Server uses the same organization name to sign you in to the target server by default. Therefore, if the target server does not have the same organization, server denies your signing in.
   6. Select **Remember Me** to have the source server remember your information, so that you can sign in to the target server automatically when you want to publish resources to it. Server remembers your information till the source server restarts.
   7. Select **Connect** to set up the connection with the target server and sign in.

      After you sign in, Server displays the Publish to Server dialog box.
3. The **Publish To**
   option in the Publish to Server dialog box shows the URL using which you have signed in to the target server. You can select **Change Login Settings**
   to edit the [signing in information](#Login).

   ![Publish to Server dialog](https://devnet.logianalytics.com/hc/article_attachments/9905676112279/pub2srv.gif)
4. Select **Browse** next to the **Target Path** text box. Server displays the [Select Folder dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741443524503-Select-Folder-Dialog-Box-Properties).
5. Select the folder in the target server that you want to publish the resources to. You can select from the folders on which you have the [Visible and Write permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) (an organization user can select from folders in his organization that match the same prerequisites). The target folder you select determines which kind of resources you can publish from the source server. For example, if you select the built-in folder My Components as the target folder, you will only be able to publish library component and catalog resources from the source server.
6. Select **Browse** next to the **Resources From** text box to select the folder in the source server where you get the resources. Based on your selection for the target folder, you can only select the folders that function the same as the target folder and on which you have the Visible permission as the source folder.
7. Server displays the available resources on which you have the Visible permission in the specified source folder, in the **Resources** box. Select the resources you want to publish and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905636390807/btn_add.gif) to add them to the **Selected** box. If you selected a folder, Server adds the folder with all its resources. To remove a resource from the Selected box, select it and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/9905657793175/btn_rmv.gif).
8. Select **Publish** to publish the selected resources to the target server.

   When resources with the same names already exist in the target server, Server prompts you to deal with the conflicts. Make the choice accordingly.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741438016279-Managing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741474096919-Converting-Resources-of-Earlier-Versions-to-the-Current-Version)
