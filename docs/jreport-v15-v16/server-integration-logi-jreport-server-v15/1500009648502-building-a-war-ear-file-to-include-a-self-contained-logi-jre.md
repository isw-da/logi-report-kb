---
title: "Building a WAR/EAR file to Include a Self-contained Logi JReport Server Guide v15 Server"
id: 1500009648502
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server
updated_at: 2021-07-24T20:54:09Z
---

# Building a WAR/EAR file to Include a Self-contained Logi JReport Server Guide v15 Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648382-Logi-JReport-Server-Guide-v15-Server-Integration)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673221-Specifying-Reporthome-for-Logi-JReport-Server-Guide-v15-Server-in-a-Java-EE-Environment)

# Building a WAR/EAR file to Include a Self-Contained Logi JReport Server

There are two ways of creating a WAR or EAR to include a self-contained Logi JReport Server:

* Create a WAR/EAR file using the provided tool makewar.bat/makewar.sh after you have installed a Logi JReport Server. If you are not familiar with Logi JReport Server, it is better to use this way.
* Create a WAR manually. The method is no longer needed but is still available in this release in case you would like to take it.

The self-contained Logi JReport Server is based on a library. The library contains all class packages required by the Logi JReport Server runtime, such as jrenv.jar, JRESServlets.jar, JREngine.jar, and JRWebDesign.jar. In the library, jrenv.jar contains the entire Logi JReport runtime environment, and is the key to the self-contained integration solution. With the self-contained solution, the WAR/EAR file can be deployed to any Java EE compliant application server without having to specify a Logi JReport Server installation root as the reporthome.

Before generating the WAR/EAR file, you can [customize the reporthome](https://devnet.logianalytics.com/hc/en-us/articles/1500009673221-Specifying-Reporthome-for-Logi-JReport-Server-Guide-v15-Server-in-a-Java-EE-Environment) and data source for Logi JReport Server if necessary, or use the default settings. For details about specifying the data source for Logi JReport Server in a Java EE environment, see [Configuring the Server Database in an Integrated Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009644482-Configuring-in-an-Integrated-Environment).

**Note:** There is a parameter in self-contained WAR/EAR - autoDetectServletPath. It is used to dynamically detect and modify servlet path based on context path of self-contained WAR/EAR when deploying the WAR/EAR to a J2EE application server. This property is enabled by default, and the actual servlet path will be concatenating "context path" with "default servlet path" set in server.properties. If you do not want this way, you can disable the feature using either of the following ways:

* Before making your WAR/EAR, set the parameter autoDetectServletPath to false in makewar.xml which is located in `<install_root>\bin`.
* If the WAR/EAR has already been built, go to web.xml, set this parameter autoDetectServletPath to false.

Below is a list of the sections covered in this topic:

* [Building a Logi JReport Server WAR/EAR by Tool](#Tool)
* [Building a Logi JReport Server WAR Manually (Deprecated)](#Manual)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Building a Logi JReport Server WAR/EAR by Tool

The tool makewar.bat/makewar.sh in `<install_root>\bin` based on the Apache Ant project is provided by Logi JReport Server to build Logi JReport Server WAR/EAR file which contains the full Logi JReport Server runtime environment. The file makewar.xml in the same directory can be used to specify information needed for building the WAR/EAR file.

When you create a Logi JReport Server WAR/EAR file using the tool, the jrenv.jar package will be automatically put into the WAR/EAR, and will be extracted to the specified reporthome when initializing Logi JReport Server. The following is the structure of the jrenv.jar package:

**jrenv.jar**

workspace/ -- This is the root folder.

bin/ -- This folder contains the license file jslc.dat and configuration files, such as LogConfig.properties and redirect.properties.

lib/ -- This folder contains jar files needed by applets, such as view12.jar and chart.jar.

template/ -- This folder contains template files.

profiling/report/ -- This folder contains profiling report files.

Logi JReports/ -- This folder contains demo reports or pre-published reports.

db/ -- This folder contains demo database for demo reports.

help/ -- This folder contains help documents.

The bin/, lib/, and template/ folders are necessary for the Logi JReport runtime, while the profiling/, Logi JReports/, db/ and help/ folders are optional.

The following shows the usages of makewar.xml and makewar.bat/makewar.sh in detail.

### makewar.xml

This file can be used to specify the following:

* Targets specified to build the WAR/EAR file. They start with the tag <target name="xxx"...>. You can modify the target names. By default, the main targets in the makewar.xml are as follows:
  + Making the server runtime environment
  + Making the WAR file for normal or remote integration
  + Making the EAR file
* Temp directories.
  + The temp directory used to save the temp files when building the WAR/EAR. By default, it is  `<install_root>\bin\distribute\temp`.
  + The directory which is used to store the generated WAR/EAR file. By default, it is  `<install_root>\bin\distribute`.
* The deployment descriptors, such as web.xml and application.xml. The configuration information, such as the database connection information for the WAR/EAR file is stored in these files.

### makewar.bat/makewar.sh

The batch/script file used to build a Logi JReport Server WAR/EAR according to the target specified in makewar.xml.

**Usage**

`makewar.bat/makewar.sh [Target Name] [-Dpredeploy=ReportFolder] [-Dreporthome=XXX] [-Djrs.remote.host=XXX] [-Djrs.remote.rmiport=XXX] [-Djrs.rmi.auth_file=XXX]`

**Options**

* **Target Name**  
   The following targets can be performed:
  + buildWar - Specifies to build the Logi JReport Server WAR. It is the default target.
  + buildEar - Specifies to build the Logi JReport Server EAR.
  + buildRemoteWar - Specifies to build the Logi JReport Server WAR for remote integration.
* **-Dpredeploy=ReportFolder**  
   Allows you to deploy the reports and catalogs under ReportFolder to the WAR/EAR file.
* **-Dreporthome**  
   Specifies the reporthome that will be set into web.xml in the WAR/EAR. If this argument is not set, reporthome will be decided when the WAR/EAR is loaded by the application server and the location will be `%user.home%/.Logi JReport/default`. This argument takes effect only when the target name is buildWar, buildEar, or buildWar4WS.
* **-Djrs.remote.host**  
   Specifies the server's RMI host when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.
* **-Djrs.remote.rmiport**  
   Specifies the server's RMI port when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.
* **-Djrs.rmi.auth\_file**  
   Specifies the RMI auth file with the absolute file path when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.

**Examples**

* Builds the Logi JReport Server WAR file which is defined by makewar.xml (the default target). The generated WAR file is saved to the default directory `<install_root>\bin\distribute`.

  `makewar.bat`
* Builds the Logi JReport Server WAR file, and saves the generated WAR file Logi JReport.war to the default directory `<install_root>\bin\distribute`. When deploying the Logi JReport.war to an application server, the report home will use `C:\Logi JReport`.

  `makewar.bat buildWar -Dreporthome=C:\Logi JReport`
* Builds the Logi JReport Server EAR file, and saves the generated EAR file Logi JReport.ear to the default directory  `<install_root>\bin\distribute`.

  `makewar.bat buildEar`
* Builds the Logi JReport Server WAR file, and deploys the reports and catalogs in  `C:\myReport` to the WAR file. The generated WAR file Logi JReport.war will be saved in the default directory  `<install_root>\bin\distribute`.

  `makewar.bat buildWar -Dpredeploy=c:\myReport`
* Builds the Logi JReport Server WAR file as defined by makewar.xml for remote integration. The generated WAR file is saved to the default directory `<install_root>\bin\distribute`.

  `makewar.bat buildRemoteWar -Djrs.remote.host=127.0.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=C:\Logi JReport\Server\bin\rmi.auth`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Building a Logi JReport Server WAR Manually (Deprecated)

This method has been used in earlier versions. If using this method, you will have to specify the Logi JReport Server installation root as the reporthome unless you make the WAR be a self-contained solution.

The following takes creating a WAR file manually on Unix for example. It is assumed that Logi JReport Server has been installed to `/opt/Logi JReport/Server`. The instruction is applicable to both Unix and Windows platforms. However, the paths for Windows should use the Windows format, for example, `C:\Logi JReport\Server`, while paths for Unix should use the Unix format, for example, `/opt/Logi JReport/Server`.

If you want to make the WAR include a self-contained Logi JReport Server, you need create [jrenv.jar](#jrenv) and then put it in the `Logi JReport/WEB-INF/lib` directory before creating the WAR. You can use either way to create jrenv.jar:

* **By the makewar.bat/makewar.sh tool**  
   For example: run the command `makewar jrenv.jar`
* **Creating manually**  
   Make sure all necessary contents are included and then use a proper tool to package them into a jar file.

Then take the following steps to build a Logi JReport Server WAR manually:

1. Create a new directory Logi JReport in the Logi JReport Server installation root: `/opt/Logi JReport/Server/``Logi JReport`.
2. Create a sub directory WEB-INF in Logi JReport: `/opt/Logi JReport/Server/Logi JReport/WEB-INF`.
3. Create a web.xml file in the WEB-INF directory as follows:

   |  |
   | --- |
   | ``` <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE web-app PUBLIC "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN" "http://java.sun.com/dtd/web-app_2_3.dtd">  <web-app>      <!--By default Logi JReport server detect servlet path-->     <!--     <context-param>     <param-name>autoDetectServletPath</param-name>     <param-value>false</param-value>     </context-param>     -->      <filter>         <filter-name>Character Encoding</filter-name>         <filter-class>jet.server.servlets.CharacterEncodingFilter</filter-class>         <init-param>             <param-name>encoding</param-name>             <param-value>UTF-8</param-value>         </init-param>         <init-param>             <param-name>excludedFiles</param-name>             <param-value>.css,.js,.png,.svg,.pdf,.rtf,.xls,.xml,.xlsx,.gif,.ico,.rpt,.cls,.jpg,.jpeg,.zip,.jz</param-value>         </init-param>     </filter>      <filter>         <filter-name>JzFileFilter</filter-name>         <filter-class>com.jinfonet.web.client.RespHeaderFilter</filter-class>         <init-param>             <param-name>Content-Type</param-name>             <param-value>application/x-javascript</param-value>         </init-param>         <init-param>             <param-name>Content-Encoding</param-name>             <param-value>gzip</param-value>         </init-param>     </filter>      <filter-mapping>         <filter-name>JzFileFilter</filter-name>         <url-pattern>*.jz</url-pattern>     </filter-mapping>      <filter-mapping>         <filter-name>Character Encoding</filter-name>         <url-pattern>/*</url-pattern>     </filter-mapping>      <listener>         <listener-class>jet.server.servlets.JRServerContextListener</listener-class>     </listener>      <servlet>         <servlet-name>jrserver</servlet-name>         <servlet-class>jet.server.servlets.JRServlet</servlet-class>     </servlet>      <servlet>         <servlet-name>sendfile</servlet-name>         <servlet-class>jet.server.servlets.SendFileServlet</servlet-class>     </servlet>      <servlet>         <servlet-name>dhtml</servlet-name>         <servlet-class>jet.web.dhtml.DHTMLlet</servlet-class>     </servlet>      <servlet>         <servlet-name>WebOSServlet</servlet-name>         <display-name>WebOSServlet</display-name>         <servlet-class>com.jinfonet.web.client.WebOSServlet</servlet-class>     </servlet>      <servlet-mapping>         <servlet-name>jrserver</servlet-name>         <url-pattern>/jrserver/*</url-pattern>     </servlet-mapping>      <servlet-mapping>         <servlet-name>sendfile</servlet-name>         <url-pattern>/sendfile/*</url-pattern>     </servlet-mapping>      <servlet-mapping>         <servlet-name>dhtml</servlet-name>         <url-pattern>/dhtml/*</url-pattern>     </servlet-mapping>      <servlet-mapping>         <servlet-name>WebOSServlet</servlet-name>         <url-pattern>*.do</url-pattern>     </servlet-mapping>      <servlet-mapping>         <servlet-name>WebOSServlet</servlet-name>         <url-pattern>*.vt</url-pattern>     </servlet-mapping>      <servlet-mapping>         <servlet-name>WebOSServlet</servlet-name>         <url-pattern>/vt/*</url-pattern>     </servlet-mapping>      <welcome-file-list>         <welcome-file>index.htm</welcome-file>         <welcome-file>index.html</welcome-file>         <welcome-file>index.jsp</welcome-file>     </welcome-file-list>      <!-- Define J2EE DataSource resource ref -->     <!--     <resource-ref>         <description>             Define J2EE DataSource resource for Logi JReport server DB 'systemtables'.         </description>         <res-ref-name>jdbc/ds-Logi JReport-systemtables</res-ref-name>         <res-type>javax.sql.DataSource</res-type>         <res-auth>Container</res-auth>     </resource-ref>     -->      <!--     <resource-ref>         <description>             Define J2EE DataSource resource for Logi JReport server DB 'realmtables'.         </description>         <res-ref-name>jdbc/ds-Logi JReport-realmtables</res-ref-name>         <res-type>javax.sql.DataSource</res-type>         <res-auth>Container</res-auth>     </resource-ref>     -->      <!--     <resource-ref>         <description>             Define J2EE DataSource resource for Logi JReport server DB 'profile'.         </description>         <res-ref-name>jdbc/ds-Logi JReport-profiling</res-ref-name>         <res-type>javax.sql.DataSource</res-type>         <res-auth>Container</res-auth>     </resource-ref>     -->      <login-config>         <auth-method>BASIC</auth-method>     </login-config>      <!-- Notify Logi JReport server to use J2EE DataSource -->     <!--     <env-entry>         <description>             Notify Logi JReport server DB 'systemtables' to use J2EE DataSource.         </description>         <env-entry-name>Logi JReport.datasource.systemtables</env-entry-name>         <env-entry-value>jndi://jdbc/ds-Logi JReport-systemtables</env-entry-value>         <env-entry-type>java.lang.String</env-entry-type>     </env-entry>     -->     <!--     <env-entry>         <description>             Notify Logi JReport server DB 'realmtables' to use J2EE DataSource.         </description>         <env-entry-name>Logi JReport.datasource.realmtables</env-entry-name>         <env-entry-value>jndi://jdbc/ds-Logi JReport-realmtables</env-entry-value>         <env-entry-type>java.lang.String</env-entry-type>     </env-entry>     -->     <!--     <env-entry>         <description>             Notify Logi JReport server DB 'profile' to use J2EE DataSource.         </description>         <env-entry-name>Logi JReport.datasource.profiling</env-entry-name>         <env-entry-value>jndi://jdbc/ds-Logi JReport-profiling</env-entry-value>         <env-entry-type>java.lang.String</env-entry-type>     </env-entry>     -->      <!-- Specify report home or customized server environment callback -->     <env-entry>         <description>             Specify report home for Logi JReport server directly.         </description>         <env-entry-name>Logi JReport.rpthome</env-entry-name>         <env-entry-value>/home/Jetty9WarHome</env-entry-value>         <env-entry-type>java.lang.String</env-entry-type>     </env-entry>      <!--     <env-entry>         <description>             Specify customized server environment callback for Logi JReport server.         </description>         <env-entry-name>Logi JReport.servenv</env-entry-name>         <env-entry-value>jet.server.DefaultServerEnv</env-entry-value>         <env-entry-type>java.lang.String</env-entry-type>     </env-entry>     -->  </web-app> ``` |
4. Create a directory lib in the `Logi JReport/WEB-INF` directory:

   `mkdir lib`
5. Create a directory pages in the `Logi JReport/WEB-INF/lib` directory:

   `mkdir lib/pages`
6. Copy all of the files in `/opt/Logi JReport/Server/lib/pages` to the `Logi JReport/WEB-INF/lib/pages` directory:

   `cp /opt/Logi JReport/Server/lib/pages/* lib/pages`
7. Create a jar file to include the resources folder which is located in `/opt/Logi JReport/Server` and name it languages.jar. For example, run the following command:

   `jar -cvf languages.jar resources`

   Then put the languages.jar in `/opt/Logi JReport/Server/lib`.
8. Copy the following jar files from `/opt/Logi JReport/Server/lib` to the `Logi JReport/WEB-INF/lib` directory: commons-codec-1.2.jar, jai\_codec-1.1.3.jar, jai\_core-1.1.3.jar, JREngine.jar, JRESServlets.jar, JRWebDesign.jar, languages.jar, sac-1.3.jar, tar.jar, log4j-core-2.7.jar and log4j-api-2.7.jar.

   If you want to export reports to the following formats, you should copy the corresponding jar to the `Logi JReport/WEB-INF/lib` directory:

   * To e-mail or use the e-mail Notification function, copy activation-1.1.1.jar and mail-1.4.7.jar.
   * To FTP, copy commons-net-3.5.jar.
   * To Excel, copy poi-3.15.jar.
   * To Page Report Result, copy JRWebDesign.jar.
9. Copy the index.htm file and the admin, dhtmljsp, images, javascript, jinfonet, skin, and style folders from `/opt/Logi JReport/Server/public_html` to the `/opt/Logi JReport/Server/Logi JReport` directory:

   `cp -r /opt/Logi JReport/Server/public_html/* /opt/Logi JReport/Server/Logi JReport`

   **Notes**:

   * The jsp files within the admin folder are used by the Logi JReport Administration pages. Those within the dhtmljsp folder are used when viewing reports in Page Report Studio.
   * If you copy index.htm and these folders mentioned above to a sub folder in `/opt/Logi JReport/Server/Logi JReport`, for example, `/opt/Logi JReport/Server/Logi JReport/sub`, to view reports in Page Report Studio, you need:
     + Modify the server.properties file:

       `web.skin.dir=/Logi JReport/sub/skin`
     + In the step 10, edit the index.htm file like this:

       `<FRAME name="ind" src="/Logi JReport/sub/jinfonet/index.jsp" frameborder="0">`

     Then go to step 11.
10. Edit the index.htm file and add the context path `/Logi JReport` to the src tag. Note that the path separator character is the Unix style "/" when referencing JSP. The result should be as follows:

    `<FRAME name="ind" src="/Logi JReport/jinfonet/index.jsp" frameborder="0">`
11. If you are going to create the war for use in Weblogic, you need to check whether there is a weblogic.xml in the `Logi JReport/WEB-INF` directory. If yes, make sure the following line is added in weblogic.xml:

    `<show-archived-real-path-enabled>true</show-archived-real-path-enabled>`

    If no, create a weblogic.xml and add it in the `Logi JReport/WEB-INF` directory. The content in weblogic.xml looks like:

    |  |
    | --- |
    | ``` <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE   weblogic-web-app PUBLIC "-//BEA Systems, Inc.//DTD Web Application 8.1//EN"  "http://www.bea.com/servers/wls810/dtd/weblogic810-web-jar.dtd"> <weblogic-web-app>     <container-descriptor>     <show-archived-real-path-enabled>true</show-archived-real-path-enabled>     </container-descriptor> </weblogic-web-app> ``` |
12. Using the following command to create a WAR file named Logi JReport.war:

    `jar -cvf Logi JReport.war index.htm admin dhtmljsp images javascript jinfonet skin style WEB-INF`

    **Note**: The jar utility is in the Java home bin directory. If it is not on your path you must call jar with the entire path, for example, `/opt/jdk1.7.0_17/bin/jar.exe`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648382-Logi-JReport-Server-Guide-v15-Server-Integration)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673221-Specifying-Reporthome-for-Logi-JReport-Server-Guide-v15-Server-in-a-Java-EE-Environment)
