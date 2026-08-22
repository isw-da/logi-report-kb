---
title: "Building a WAR/EAR File to Include a Self-contained Logi Report Server"
id: 5741473837719
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741473837719-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server
updated_at: 2022-10-31T17:17:59Z
---

# Building a WAR/EAR File to Include a Self-contained Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741460910103--Server-Integration-Server-v19)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741467928983-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)

# Building a WAR/EAR File to Include a Self-contained Logi Report Server

This topic describes how you can create a WAR or EAR file to include a self-contained Logi Report Server using the tool **makewar.bat**/**makewar.sh** after you have installed a Logi Report Server.

The self-contained Logi Report Server is based on a library. The library contains all class packages required by the Logi Report Server runtime, such as jrenv.jar, JRESServlets.jar, JREngine.jar, and JRWebDesign.jar. In the library, jrenv.jar contains the entire Logi Report runtime environment, and is the key to the self-contained integration solution. With the self-contained solution, you can deploy the WAR/EAR file to any Java EE compliant application server without having to specify a Logi Report Server installation root as the reporthome.

Before generating the WAR/EAR file, you can [customize the reporthome](https://devnet.logianalytics.com/hc/en-us/articles/5741467928983-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment) and data source for Logi Report Server, or use the default settings. For more information, see [Configuring Server Databases for Server Metadata in an Integrated Environment](https://devnet.logianalytics.com/hc/en-us/articles/5741395898263-Configuring-Server-Databases-for-Server-Metadata-in-an-Integrated-Environment).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)Logi Report Server uses a parameter **autoDetectServletPath** in the self-contained WAR/EAR, to dynamically detect and modify servlet path based on the context path of the self-contained WAR/EAR when you deploy the WAR/EAR to a J2EE application server. Server enables this property by default, and the actual servlet path will be concatenating "context path" with "default servlet path" set in server.properties. If you do not want this way, you can disable the feature using either of the following ways:

* Before making your WAR/EAR, set the parameter **autoDetectServletPath** to **false** in **makewar.xml** in `<install_root>\bin`.
* If you have already built the WAR/EAR, go to **web.xml**, set the **autoDetectServletPath**parameter to **false**.

## Building a Logi Report Server WAR/EAR by Tool

You can use the tool **makewar.bat**/**makewar.sh** in `<install_root>\bin` based on the Apache Ant project to build Logi Report Server WAR/EAR file to contain the full Logi Report Server runtime environment. You can specify information you need for building the WAR/EAR file using the **makewar.xml** file in the same directory.

When you create a Logi Report Server WAR/EAR file using the tool, Server automatically puts the **jrenv.jar** package into the WAR/EAR and extracts it to the specified reporthome when initializing Logi Report Server. See the following structure of the jrenv.jar package:

**jrenv.jar**

workspace/ -- This is the root folder.

bin/ -- This folder contains the license file jslc.dat and configuration files, such as LogConfig.properties and redirect.properties.

template/ -- This folder contains template files.

profiling/report/ -- This folder contains profiling report files.

jreports/ -- This folder contains demo reports or pre-published reports.

db/ -- This folder contains demo database for demo reports.

help/ -- This folder contains help documents.

The bin, lib, and template folders are necessary for the Logi Report runtime, while the profiling, jreports, db, and help folders are optional.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)Since v15.5, Logi Report has added Feature Guide in the help folder to introduce main Logi Report features with videos. Feature Guide takes up over 150 MB on disk and increases the jrenv.jar file size. You can exclude the Feature Guide from your WAR/EAR by adding the following code in the makewar.xml and then rebuilding the WAR/EAR:

```
<zipfileset dir="${installroot}/help"	prefix="workspace/help">  
<exclude name="featureguide/**" />  
</zipfileset>
```

The following sections describe how you can use makewar.xml and makewar.bat/makewar.sh.

### makewar.xml

You can use this file to specify the following:

* Targets to build the WAR/EAR file. They start with the tag <target name="xxx"...>. You can modify the target names. By default, the main targets in the makewar.xml are:
  + Making the server runtime environment
  + Making the WAR file for normal or remote integration
  + Making the EAR file
* Temp directories.
  + The temp directory to save the temp files when building the WAR/EAR. By default, it is  `<install_root>\bin\distribute\temp`.
  + The directory to store the generated WAR/EAR file. By default, it is  `<install_root>\bin\distribute`.
* The deployment descriptors, such as web.xml and application.xml. Server stores the configuration information for the WAR/EAR file in these files, for example, the database connection information.

### makewar.bat/makewar.sh

You can use the batch/script file to build a Logi Report Server WAR/EAR according to the target in makewar.xml.

**Usage**

`makewar.bat/makewar.sh [Target Name] [-Dpredeploy=ReportFolder] [-Dreporthome=XXX] [-Djrs.remote.host=XXX] [-Djrs.remote.rmiport=XXX] [-Djrs.rmi.auth_file=XXX]`

**Parameters**

* **Target Name**  
   You can perform the following targets:
  + buildWar - Build the Logi Report Server WAR. It is the default target.
  + buildEar - Build the Logi Report Server EAR.
  + buildRemoteWar - Build the Logi Report Server WAR for remote integration.
* **-Dpredeploy=ReportFolder**  
   Deploy the reports and catalogs under **ReportFolder** to the WAR/EAR file.
* **-Djbossas7=true**  
   When building a remote WAR using `makewar.bat buildRemoteWar` or `makewar.sh buildRemoteWar` to deploy to WildFly 16.0.0.Final or JBoss AS 7/JBoss EAP 6 or above, add the parameter **-Djbossas7=true**.
* **-Dreporthome**  
   Reporthome to set into web.xml in the WAR/EAR. If you do not set this argument, reporthome will be `%user.home%/.jreport/default`. This argument takes effect only when the target name is buildWar, buildEar, or buildWar4WS.
* **-Djrs.remote.host**  
  Server's RMI host when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.
* **-Djrs.remote.rmiport**  
   Server's RMI port when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.
* **-Djrs.rmi.auth\_file**  
  RMI auth file with the absolute file path when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.

**Examples**

* Build the Logi Report Server WAR file which is defined by makewar.xml (the default target) and save the generated WAR file to the default directory `<install_root>\bin\distribute`.

  `makewar.bat`
* Build the Logi Report Server WAR file and save the generated WAR file jreport.war to the default directory `<install_root>\bin\distribute`. When deploying the jreport.war to an application server, the reporthome will use `C:\LogiReport`.

  `makewar.bat buildWar -Dreporthome=C:\LogiReport`
* Build the Logi Report Server EAR file and save the generated EAR file jreport.ear to the default directory `<install_root>\bin\distribute`.

  `makewar.bat buildEar`
* Build the Logi Report Server WAR file, deploy the reports and catalogs in  `C:\myReport` to the WAR file, and save the generated WAR file jreport.war in the default directory  `<install_root>\bin\distribute`.

  `makewar.bat buildWar -Dpredeploy=c:\myReport`
* Build the Logi Report Server WAR file as defined by makewar.xml for remote integration and save the generated WAR file to the default directory `<install_root>\bin\distribute`.

  `makewar.bat buildRemoteWar -Djrs.remote.host=127.0.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=C:\LogiReport\Server\bin\rmi.auth`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741460910103--Server-Integration-Server-v19)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741467928983-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)
