---
title: "Publishing Resources"
id: 1500009717841
section: "Managing Resources"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717841-Publishing-Resources
updated_at: 2021-11-03T06:56:53Z
---

# Publishing Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717721-Managing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717741-Converting-Resources-of-Earlier-Versions-into-Current-Version)

# Publishing Resources

Before you can perform any tasks on Logi JReport Server, you first need to have your resources published and organized in the server resource tree. The resources are reports, library components, catalogs and folders.

The Logi JReport Server resource tree contains four built-in folders: My Components and Public Components are used to store library components with catalogs, while My Reports and Public Reports store reports with catalogs.

Below is a list of the sections covered in this topic:

* [Publishing Resources from Logi JReport Designer](#Designer)
* [Publishing Resources from a Local Computer](#Locally)
* [Publishing Resources from a Remote Computer](#Remotely)

## Publishing Resources from Logi JReport Designer

You can directly publish your reports, library components, or catalogs from Logi JReport Designer to Logi JReport Server. For more information, see Publishing resources remotely in the *Logi JReport Designer User's Guide*.

## Publishing Resources from a Local Computer

You can publish resources including reports, library components, catalogs and folders from a local computer to the server resource tree via the Resources page in the server console.

1. Browse to the folder in which to publish the resources, then select **Publish** > **To Local Server** on the task bar.

   ![Publish Link on Console Page](https://devnet.logianalytics.com/hc/article_attachments/4412131437207/mng_rsc_pblsh.gif)

   The [Publish to Local Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009714881-Publish-to-Local-Server) dialog appears.

   ![Publish to Local Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131437463/pblclsrv.gif)
2. Select a type from the Resource Type drop-down list.
3. Specify properties for the to-be-published resources as required.
   * **If the Page Report or Web Report resource type is selected:**
     1. In the From File text box, specify the report you want to publish with its full path.
     2. In the Resource Node Name field, specify a name for the report. This name is required and is used as the display name of the report in the server resource tree.
     3. Type a brief description to describe the report in the Resource Description field.
     4. From the Status drop-down list, select the status of the report.
     + **Active**  
        The report can be run, advanced run and scheduled on Logi JReport Server.
     + **Inactive**  
        The report cannot be run, advanced run or scheduled on Logi JReport Server.
     + **Incomplete**  
        The report is not completely designed and cannot be run, advanced run or scheduled Logi JReport Server.5. Specify values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009717761-Working-with-Custom-Fields) for the report if there are custom fields.
     6. Select the **Browse** button to specify a font directory for the report.
     7. Select the **Browse** button to specify a style directory for the report.
     8. Select the **Browse** button to specify a geographic information directory for the report.
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
     5. Select the **Browse** button to specify a font directory for the library component.
     6. Select the **Browse** button to specify a style directory for the library component.
     7. Select the **Browse** button to specify a geographic information directory for the library component.
   * **If the Folder resource type is selected:**
     1. In the Resource Node Name field, specify a name for the folder. This name is required and is used as the display name of the folder in the server resource tree.
     2. Type a brief description to describe the folder in the Resource Description field.
     3. In the Resource Real Path text box, type a local disk path as the real path of the folder. If you want to enable getting resources from the real path, check **Enable Resources from Real Paths**. The local disk resources will be mapped into the resource node of the folder in the server resource tree and the server will be able to always get resources and updates from the real path. For details, see [Getting and Using Resources from a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/1500009717881-Getting-and-Using-Resources-from-a-Real-Path).

        If this step is skipped, the publish job will simply create a new blank directory node in the server resource tree.
     4. Specify values of the custom fields for the folder if there are custom fields.
   * **If the Folder with Contents resource type is selected:**
     1. Select the **Browse** button next to the From Folder text box to specify the folder where the resources you want to publish are saved.
     2. In the Resource Node Name field, specify a name for the folder. This name is required and is used as the display name of the folder in the server resource tree.
     3. Type a brief description to describe the folder in the Resource Description field.
     4. In the Resource Real Path text box, type a local disk path as the real path of the folder. If you want to enable getting resources from the real path, check **Enable Resources from Real Paths**. The local disk resources will be mapped into the resource node of the folder in the server resource tree and the server will be able to always get resources and updates from the real path.
     5. Specify values of the custom fields for the folder if there are custom fields.
     6. Select the **Browse** button to specify a font directory for the resources.
     7. Select the **Browse** button to specify a style directory for the resources.
     8. Select the **Browse** button to specify a geographic information directory for the resources.
     9. If you want to use Advanced Publish, select the **Advanced Publish** button. All resources contained within the specified folder will then be displayed. Check the resources you want to publish and specify the properties for each resource as required.
   * **If the Catalogs, Reports and Folders in Folder or Catalogs and Reports in Folder resource type is selected:**
     1. Select the **Browse** button next to the From Folder text box to specify the folder where the resources you want to publish are saved.
     2. Select the **Browse** button to specify a font directory for the resources.
     3. Select the **Browse** button to specify a style directory for the resources.
     4. Select the **Browse** button to specify a geographic information directory for the resources.
     5. If you want to use Advanced Publish, select the **Advanced Publish** button. All resources contained within the specified folder will then be displayed. Check the resources you want to publish and specify the properties for each resource as required.
4. If the resources you specify to publish contain reports created in earlier versions, check **Automatically Convert Old Report Schemas**, the reports will then be automatically converted into current version Logi JReport reports when publishing finishes.
5. To apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009717941-Applying-an-Archive-Policy) to the resources that you are publishing,
   * For resources published to the My Reports or Public Reports folder, check the **Apply Archive Policy** option, then specify the archive policy as required: Archive as New Version or Replace Old Version.
   * For resources published to the My Components or Public Components folder, specify the maximum number of versions that will be listed in the version table of the resources.

   Note that a folder by itself does not have versions; the archive policy specified for a folder applies to the folder content.
6. If the resources are to be published to a public folder and you have the Grant permission on the folder, select the **Set Permissions** link to specify user [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) to the resources according to your requirement.
7. Select **OK**  to start publishing the resources.

## Publishing Resources from a Remote Computer

Before publishing resources remotely, you must have the resources compressed in any of the following formats in the remote computer: .zip, .jar, .gzip, .gz, .tar.gz, .tar or .tgz.

1. In the Resources page of the Logi JReport Server console, browse to the folder in which to publish the resources, then on the task bar of the Resources page, select **Publish** > **To Remote Server**.

   The [Publish to Remote Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009688922-Publish-to-Remove-Server-) dialog appears.

   ![Publish to Remote Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4412112561815/pbrmtsrv.gif)
2. Select the **Browse** button to specify the zipped file which contains the resources you want to publish.
3. Specify where the resources will be published.
   * If you want to publish the resources directly to the current open folder, check the **Publish files and folders in the zipped file to /XXX** checkbox.
   * If you want to create a new folder in the current open folder to locate the resources,
     1. Make sure the Publish files and folders in the zipped file to /XXX checkbox is not selected.
     2. In the Resource Node Name box, specify the name of the folder. The name will then be used as the display name of the folder in the server resource tree.
     3. Type a brief description to describe the folder in the Resource Description box.
     4. Specify values of the [custom fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009717761-Working-with-Custom-Fields) for the folder if there are custom fields.
     5. In the Resource Real Path text box, type a local disk path as the real path of the folder. If you want to enable getting resources from the real path, check **Enable Resources from Real Paths**. The local disk resources will be mapped into the resource node of the folder in the server resource tree and the server will be able to always get resources and updates from the real path. For details, see [Getting and Using Resources from a Real Path](https://devnet.logianalytics.com/hc/en-us/articles/1500009717881-Getting-and-Using-Resources-from-a-Real-Path).
4. If the resources you specify to publish contain reports created in earlier versions, check **Automatically Convert Old Report Schemas**, the reports will then be automatically converted into current version Logi JReport reports when publishing finishes.
5. To apply an [archive policy](https://devnet.logianalytics.com/hc/en-us/articles/1500009717941-Applying-an-Archive-Policy) to the resources that you are publishing,
   * For resources published to the My Reports or Public Reports folder, check the **Apply Archive Policy** option, then specify the archive policy as required: Archive as New Version or Replace Old Version.
   * For resources published to the My Components or Public Components folder, specify the maximum number of versions that will be listed in the version table of the resources.
6. If the resources are to be published to a public folder and you have the Grant permission on the folder, select the **Set Permissions** link to specify user [permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009718881-Managing-Permissions) to them according to your requirement.
7. If you want to use Advanced Publish, select the **Advanced Publish** button. All resources contained within the zip file will then be displayed. Check the resources you want to publish and specify the properties for each resource as required.
8. Select **OK** to start publishing the resources.

When publishing resources from a remote computer, the process is similar to that for a local publish. However there are some differences:

* Local Publish publishes resources from the machine where the server runs, while a Remote Publish publishes resources from a client machine using a web browser to the machine where the server runs.
* The resource type of Remote Publish can ONLY be a compressed file. You should compress the reports, library components, and catalog files in advance, and if special fonts are used in the reports or library components, add the corresponding font files into the compressed file as well. There are two approaches to building a compressed file.
  + You can compress the resources manually using a third-party tool, such as Winzip and gzip.
  + You can use jar.exe that the JSDK provides to build a compressed jar file directly. Use the command as follows:

    `%JAVAHOME%\bin\jar.exe -cvfM %DEST_JAR_FILE% %SOURCE_RESOURCES%`

    | Parameter | Description |
    | --- | --- |
    | %JAVAHOME% | The Java SDK install root. |
    | %DEST\_JAR\_FILE% | The destination file path and file name. The .jar file will be generated to the path you specify here, using the file name you provide. |
    | %SOURCE\_RESOURCES% | The source file path and file name. Note that specifying a path for this parameter will cause the generated jar file to contain the same path information. For example, when you extract a jar file compressed using `myReports\*.*` for this parameter, the files will be extracted to a folder called `myReports`. Logi JReport Server is not able to import a compressed file which contains the path information, so do not specify a path for this parameter. |

    To generate a jar file containing no path information, switch to the source folder, and then carry out the compression. For example,

    `C:\myReports>C:\jdk1.8.0\bin\jar -cvfM c:\temp\aa.jar.`

    The jar file will be generated to `c:\temp`, as aa.jar, compressing all the files in `c:\myReports`, and containing no path information.

    Always use this method if the folder you are compressing contains reports or library components with Chinese, Korean, or Japanese names.

**Notes:**

* In folders where library components can be published, only one catalog file is allowed.
* The Enable Resources from Real Paths option in the publish dialog can only be checked when the same option in the Administration > Configuration > Advanced page in the server console has also been checked.
* The Publish to Local Server option is always available to administrators in the Logi JReport Server console. For end users, the option is displayed only when they have the privilege of publishing resources and have logged onto Logi JReport Server from a local browser.
* After resources have been delivered to Logi JReport Server, you may find that the publish time shown in the server UI is different from the client time. That is because the publish time takes the server time instead of the client time.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717721-Managing-Resources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717741-Converting-Resources-of-Earlier-Versions-into-Current-Version)
