---
title: "Building a WAR/EAR File to Include a Self-contained Logi Report Server"
id: 1500009749861
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server
updated_at: 2021-07-25T07:19:01Z
---

# Building a WAR/EAR File to Include a Self-contained Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722742-Logi-Report-Server-Integration)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749841-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)

# Building a WAR/EAR File to Include a Self-contained Logi Report Server

There are two ways of creating a WAR or EAR to include a self-contained Logi Report Server:

* Create a WAR/EAR file using the provided tool makewar.bat/makewar.sh after you have installed a Logi Report Server. If you are not familiar with Logi Report Server, it is better to use this way.
* Create a WAR manually. The method is no longer needed but is still available in this release in case you would like to take it.

The self-contained Logi Report Server is based on a library. The library contains all class packages required by the Logi Report Server runtime, such as jrenv.jar, JRESServlets.jar, JREngine.jar, and JRWebDesign.jar. In the library, jrenv.jar contains the entire Logi Report runtime environment, and is the key to the self-contained integration solution. With the self-contained solution, the WAR/EAR file can be deployed to any Java EE compliant application server without having to specify a Logi Report Server installation root as the reporthome.

Before generating the WAR/EAR file, you can [customize the reporthome](https://devnet.logianalytics.com/hc/en-us/articles/1500009749841-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment) and data source for Logi Report Server, or use the default settings. For details about specifying the data source for Logi Report Server in a Java EE environment, see [Configuring the Server Database in an Integrated Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009744801-Configuring-in-an-Integrated-Environment).

Select the following links to view the topics:

* [Building a Logi Report Server WAR/EAR by Tool](#Tool)

+ [makewar.xml](#xml)
+ [makewar.bat/makewar.sh](#bat)

* [Building a Logi Report Server WAR Manually (Deprecated)](#Manual)

**Note:** There is a parameter in the self-contained WAR/EAR - autoDetectServletPath. It is used to dynamically detect and modify servlet path based on context path of self-contained WAR/EAR when deploying the WAR/EAR to a J2EE application server. This property is enabled by default, and the actual servlet path will be concatenating "context path" with "default servlet path" set in server.properties. If you do not want this way, you can disable the feature using either of the following ways:

* Before making your WAR/EAR, set the parameter autoDetectServletPath to false in makewar.xml which is located in `<install_root>\bin`.
* If the WAR/EAR has already been built, go to web.xml, set this parameter autoDetectServletPath to false.

## Building a Logi Report Server WAR/EAR by Tool

The tool makewar.bat/makewar.sh in `<install_root>\bin` based on the Apache Ant project is provided by Logi Report Server to build Logi Report Server WAR/EAR file which contains the full Logi Report Server runtime environment. The file makewar.xml in the same directory can be used to specify information needed for building the WAR/EAR file.

When you create a Logi Report Server WAR/EAR file using the tool, the jrenv.jar package will be automatically put into the WAR/EAR, and will be extracted to the specified reporthome when initializing Logi Report Server. The following is the structure of the jrenv.jar package:

**jrenv.jar**

workspace/ -- This is the root folder.

bin/ -- This folder contains the license file jslc.dat and configuration files, such as LogConfig.properties and redirect.properties.

template/ -- This folder contains template files.

profiling/report/ -- This folder contains profiling report files.

jreports/ -- This folder contains demo reports or pre-published reports.

db/ -- This folder contains demo database for demo reports.

help/ -- This folder contains help documents.

The bin/, lib/, and template/ folders are necessary for the Logi Report runtime, while the profiling/, jreports/, db/ and help/ folders are optional.

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

The batch/script file used to build a Logi Report Server WAR/EAR according to the target specified in makewar.xml.

**Usage**

`makewar.bat/makewar.sh [Target Name] [-Dpredeploy=ReportFolder] [-Dreporthome=XXX] [-Djrs.remote.host=XXX] [-Djrs.remote.rmiport=XXX] [-Djrs.rmi.auth_file=XXX]`

**Options**

* **Target Name**  
   The following targets can be performed:
  + buildWar - Specifies to build the Logi Report Server WAR. It is the default target.
  + buildEar - Specifies to build the Logi Report Server EAR.
  + buildRemoteWar - Specifies to build the Logi Report Server WAR for remote integration.
* **-Dpredeploy=ReportFolder**  
   Allows you to deploy the reports and catalogs under ReportFolder to the WAR/EAR file.
* **-Djbossas7=true**  
   When building a remote WAR using `makewar.bat buildRemoteWar` or `makewar.sh buildRemoteWar`to deploy to WildFly 16.0.0.Final or JBoss AS 7/JBoss EAP 6 above, add the parameter -Djbossas7=true.
* **-Dreporthome**  
   Specifies the reporthome that will be set into web.xml in the WAR/EAR. If this argument is not set, reporthome will be decided when the WAR/EAR is loaded by the application server and the location will be `%user.home%/.jreport/default`. This argument takes effect only when the target name is buildWar, buildEar, or buildWar4WS.
* **-Djrs.remote.host**  
   Specifies the server's RMI host when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.
* **-Djrs.remote.rmiport**  
   Specifies the server's RMI port when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.
* **-Djrs.rmi.auth\_file**  
   Specifies the RMI auth file with the absolute file path when building a WAR for remote integration. This argument takes effect only when the target name is buildRemoteWar.

**Examples**

* Builds the Logi Report Server WAR file which is defined by makewar.xml (the default target). The generated WAR file is saved to the default directory `<install_root>\bin\distribute`.

  `makewar.bat`
* Builds the Logi Report Server WAR file, and saves the generated WAR file jreport.war to the default directory `<install_root>\bin\distribute`. When deploying the jreport.war to an application server, the reporthome will use `C:\LogiReport`.

  `makewar.bat buildWar -Dreporthome=C:\LogiReport`
* Builds the Logi Report Server EAR file, and saves the generated EAR file jreport.ear to the default directory  `<install_root>\bin\distribute`.

  `makewar.bat buildEar`
* Builds the Logi Report Server WAR file, and deploys the reports and catalogs in  `C:\myReport` to the WAR file. The generated WAR file jreport.war will be saved in the default directory  `<install_root>\bin\distribute`.

  `makewar.bat buildWar -Dpredeploy=c:\myReport`
* Builds the Logi Report Server WAR file as defined by makewar.xml for remote integration. The generated WAR file is saved to the default directory `<install_root>\bin\distribute`.

  `makewar.bat buildRemoteWar -Djrs.remote.host=127.0.0.1 -Djrs.remote.rmiport=1129 -Djrs.rmi.auth_file=C:\LogiReport\Server\bin\rmi.auth`

## Building a Logi Report Server WAR Manually (Deprecated)

This method has been used in earlier versions. If using this method, you will have to specify the Logi Report Server installation root as the reporthome unless you make the WAR be a self-contained solution.

The following takes creating a WAR file manually on Unix for example. It is assumed that Logi Report Server has been installed to `/opt/LogiReport/Server`. The instruction is also applicable to Windows but the paths for Windows should use the Windows format, for example, `C:\LogiReport\Server`.

If you want to make the WAR include a self-contained Logi Report Server, you need create [jrenv.jar](#jrenv) and then put it in the `jreport/WEB-INF/lib` directory before creating the WAR. You can use either way to create jrenv.jar:

* **By the makewar.bat/makewar.sh tool**  
   For example: run the command `makewar jrenv.jar`
* **Creating manually**  
   Make sure all necessary contents are included and then use a proper tool to package them into a jar file.

Then take the following steps to build a Logi Report Server WAR manually:

1. Create a new directory jreport in the Logi Report Server installation root: `/opt/LogiReport/Server/jreport`.
2. Create a sub directory WEB-INF in jreport: `/opt/LogiReport/Server/jreport/WEB-INF`.
3. Create a web.xml file in the WEB-INF directory as follows:

   ```
   <?xml version="1.0" encoding="UTF-8"?>  
   <!DOCTYPE web-app PUBLIC "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN" "http://java.sun.com/dtd/web-app_2_3.dtd">  
     
   <web-app>  
     
       <!--By default Logi Report Server detect servlet path-->  
       <!--  
       <context-param>  
       <param-name>autoDetectServletPath</param-name>  
       <param-value>false</param-value>  
       </context-param>  
       -->  
     
       <filter>  
           <filter-name>Character Encoding</filter-name>  
           <filter-class>jet.server.servlets.CharacterEncodingFilter</filter-class>  
           <init-param>  
               <param-name>encoding</param-name>  
               <param-value>UTF-8</param-value>  
           </init-param>  
           <init-param>  
               <param-name>excludedFiles</param-name>  
               
               <param-value>.css,.js,.png,.svg,.pdf,.rtf,.xls,.xml,.xlsx,.gif,.ico,.rpt,.cls,.jpg,.jpeg,.zip,.jz</param-value>  
           
           </init-param>  
       </filter>  
     
    
       <filter>  
      
           <filter-name>JzFileFilter</filter-name>  
     
           <filter-class>com.jinfonet.web.client.RespHeaderFilter</filter-class>  
     
           <init-param>  
    
               <param-name>Content-Type</param-name>  
    
               <param-value>application/x-javascript</param-value>  
     
           </init-param>  
    
           <init-param>  
               <param-name>Content-Encoding</param-name>  
     
               <param-value>gzip</param-value>  
       
           </init-param>  
     
       </filter>  
     
      
       <filter-mapping>  
           <filter-name>JzFileFilter</filter-name>  
      
           <url-pattern>*.jz</url-pattern>  
     
       </filter-mapping>  
     
     
       <filter-mapping>  
      
           <filter-name>Character Encoding</filter-name>  
       
           <url-pattern>/*</url-pattern>  
    
       </filter-mapping>  
     
      
       <listener>  
         
           <listener-class>jet.server.servlets.JRServerContextListener</listener-class>  
      
       </listener>  
     
      
       <servlet>  
        
           <servlet-name>jrserver</servlet-name>  
        
           <servlet-class>jet.server.servlets.JRServlet</servlet-class>  
      
       </servlet>  
     
       
       <servlet>  
          
           <servlet-name>sendfile</servlet-name>  
         
            <servlet-class>jet.server.servlets.SendFileServlet</servlet-class>  
    
       </servlet>  
     
      
       <servlet>  
           
           <servlet-name>dhtml</servlet-name>  
     
           <servlet-class>jet.web.dhtml.DHTMLlet</servlet-class>  
       </servlet>  
     
      
       <servlet>  
          
           <servlet-name>WebOSServlet</servlet-name>  
           <display-name>WebOSServlet</display-name>  
        
           <servlet-class>com.jinfonet.web.client.WebOSServlet</servlet-class>  
     
       </servlet>  
     
      
       <servlet-mapping>  
        
           <servlet-name>jrserver</servlet-name>  
      
           <url-pattern>/jrserver/*</url-pattern>  
     
       </servlet-mapping>  
     
      
       <servlet-mapping>  
          
           <servlet-name>sendfile</servlet-name>  
       
           <url-pattern>/sendfile/*</url-pattern>  
      
       </servlet-mapping>  
     
       
       <servlet-mapping>  
     
           <servlet-name>dhtml</servlet-name>  
          
           <url-pattern>/dhtml/*</url-pattern>  
      
       </servlet-mapping>  
     
    
       <servlet-mapping>  
        
           <servlet-name>WebOSServlet</servlet-name>  
        
           <url-pattern>*.do</url-pattern>  
       </servlet-mapping>  
     
    
       <servlet-mapping>  
       
           <servlet-name>WebOSServlet</servlet-name>  
           <url-pattern>*.vt</url-pattern>  
    
       </servlet-mapping>  
     
      
       <servlet-mapping>  
      
           <servlet-name>WebOSServlet</servlet-name>  
       
           <url-pattern>/vt/*</url-pattern>  
     
       </servlet-mapping>  
     
     
       <welcome-file-list>  
       
           <welcome-file>index.htm</welcome-file>  
      
           <welcome-file>index.html</welcome-file>  
         
           <welcome-file>index.jsp</welcome-file>  
     
       </welcome-file-list>  
     
       
       <!-- Define J2EE DataSource resource ref -->  
      
       <!--  
    
        <resource-ref>  
       
           <description>  
              
               Define J2EE DataSource resource for Logi Report Server DB 'systemtables'.  
     
           </description>  
      
           <res-ref-name>jdbc/ds-jreport-systemtables</res-ref-name>  
     
           <res-type>javax.sql.DataSource</res-type>  
     
            <res-auth>Container</res-auth>  
       
       </resource-ref>  
     
       -->  
     
       
       <!--  
       
       <resource-ref>  
         
           <description>  
        
               Define J2EE DataSource resource for Logi Report Server DB 'realmtables'.  
      
           </description>  
       
           <res-ref-name>jdbc/ds-jreport-realmtables</res-ref-name>  
    
           <res-type>javax.sql.DataSource</res-type>  
       
           <res-auth>Container</res-auth>  
       </resource-ref>  
       -->  
     
      
       <!--  
      
       <resource-ref>  
    
           <description>  
     
               Define J2EE DataSource resource for Logi Report Server DB 'profile'.  
         
           </description>  
    
           <res-ref-name>jdbc/ds-jreport-profiling</res-ref-name>  
        
           <res-type>javax.sql.DataSource</res-type>  
       
           <res-auth>Container</res-auth>  
      
       </resource-ref>  
       
       -->  
     
       <login-config>  
    
           <auth-method>BASIC</auth-method>  
       </login-config>  
     
    
       <!-- Notify Logi Report Server to use J2EE DataSource -->  
    
       <!--  
      
       <env-entry>  
       
           <description>  
          
               Notify Logi Report Server DB 'systemtables' to use J2EE DataSource.  
    
           </description>  
        
           <env-entry-name>jreport.datasource.systemtables</env-entry-name>  
       
           <env-entry-value>jndi://jdbc/ds-jreport-systemtables</env-entry-value>  
       
           <env-entry-type>java.lang.String</env-entry-type>  
     
        </env-entry>  
       
       -->  
     
       <!--  
      
       <env-entry>  
    
           <description>  
      
               Notify Logi Report Server DB 'realmtables' to use J2EE DataSource.  
      
           </description>  
           <env-entry-name>jreport.datasource.realmtables</env-entry-name>  
     
           <env-entry-value>jndi://jdbc/ds-jreport-realmtables</env-entry-value>  
      
           <env-entry-type>java.lang.String</env-entry-type>  
     
        </env-entry>  
     
       -->  
    
       <!--  
      
       <env-entry>  
          
           <description>  
       
               Notify Logi Report Server DB 'profile' to use J2EE DataSource.  
       
           </description>  
      
           <env-entry-name>jreport.datasource.profiling</env-entry-name>  
      
           <env-entry-value>jndi://jdbc/ds-jreport-profiling</env-entry-value>  
           <env-entry-type>java.lang.String</env-entry-type>  
     
       </env-entry>  
     
       -->  
     
    
       <!-- Specify reporthome or customized server environment callback -->  
       <env-entry>  
      
           <description>  
      
               Specify reporthome for Logi Report Server directly.  
       
           </description>  
    
           <env-entry-name>jreport.rpthome</env-entry-name>  
     
           <env-entry-value>/home/Jetty9WarHome</env-entry-value>  
      
           <env-entry-type>java.lang.String</env-entry-type>  
    
       </env-entry>  
     
     
       <!--  
      
       <env-entry>  
         
           <description>  
      
               Specify customized server environment callback for Logi Report Server.  
       
           </description>  
     
           <env-entry-name>jreport.servenv</env-entry-name>  
    
           <env-entry-value>jet.server.DefaultServerEnv</env-entry-value>  
     
           <env-entry-type>java.lang.String</env-entry-type>  
      
       </env-entry>  
      
       -->  
     
   </web-app>
   ```
4. Create a directory lib in the `jreport/WEB-INF` directory:

   `mkdir lib`
5. Create a directory pages in the `jreport/WEB-INF/lib` directory:

   `mkdir lib/pages`
6. Copy all of the files in `/opt/LogiReport/Server/lib/pages` to the `jreport/WEB-INF/lib/pages` directory:

   `cp /opt/LogiReport/Server/lib/pages/* lib/pages`
7. Create a jar file to include the resources folder which is located in `/opt/LogiReport/Server` and name it languages.jar. For example, run the following command:

   `jar -cvf languages.jar resources`

   Then put the languages.jar in `/opt/LogiReport/Server/lib`.
8. Copy the following jar files from `/opt/LogiReport/Server/lib` to the `jreport/WEB-INF/lib` directory: jai\_codec-1.1.3.jar, jai\_core-1.1.3.jar, JREngine.jar, JRESServlets.jar, JRWebDesign.jar, languages.jar, sac-1.3.jar, tar.jar, log4j-core-2.12.1.jar and log4j-api-2.12.1.jar.

   If you want to export reports to the following formats, you should copy the corresponding jar to the `jreport/WEB-INF/lib` directory:

   * To e-mail or use the e-mail Notification function, copy jakarta.mail.jar.
   * To FTP, copy commons-net-3.6.jar.
   * To Excel, copy poi-3.15.jar.
   * To Page Report Result, copy JRWebDesign.jar.
9. Copy the index.htm file and the admin, dhtmljsp, images, javascript, jinfonet, skin, and style folders from `/opt/LogiReport/Server/public_html` to the `/opt/LogiReport/Server/jreport` directory:

   `cp -r /opt/LogiReport/Server/public_html/* /opt/LogiReport/Server/jreport`

   **Notes**:

   * The jsp files within the admin folder are used by pages from the Logi Report Server console > Administration drop-down menu. Those within the dhtmljsp folder are used when viewing reports in Page Report Studio.
   * If you copy index.htm and these folders mentioned above to a subfolder in `/opt/LogiReport/Server/jreport`, for example, `/opt/LogiReport/Server/jreport/sub`, to view reports in Page Report Studio, you need:
     + Modify the server.properties file:

       `web.skin.dir=/jreport/sub/skin`
     + In the step 10, edit the index.htm file like this:

       `<FRAME name="ind" src="/jreport/sub/jinfonet/index.jsp" frameborder="0">`

     Then go to step 11.
10. Edit the index.htm file and add the context path /jreport to the src tag. Note that the path separator character is the Unix style "/" when referencing JSP. The result should be as follows:

    `<FRAME name="ind" src="/jreport/jinfonet/index.jsp" frameborder="0">`
11. If you are going to create the war for use in Weblogic, you need to check whether there is a weblogic.xml in the `jreport/WEB-INF` directory. If yes, make sure the following line is added in weblogic.xml:

    `<show-archived-real-path-enabled>true</show-archived-real-path-enabled>`

    If no, create a weblogic.xml and add it in the `jreport/WEB-INF` directory. The content in weblogic.xml looks like:

    ```
    <?xml version="1.0" encoding="UTF-8"?>  
    <!DOCTYPE   weblogic-web-app PUBLIC "-//BEA Systems, Inc.//DTD Web Application 8.1//EN"   
    "http://www.bea.com/servers/wls810/dtd/weblogic810-web-jar.dtd">  
    <weblogic-web-app>  
        <container-descriptor>  
        <show-archived-real-path-enabled>true</show-archived-real-path-enabled>  
        </container-descriptor>  
    </weblogic-web-app>
    ```
12. Using the following command to create a WAR file named jreport.war:

    `jar -cvf jreport.war index.htm admin dhtmljsp images javascript jinfonet skin style WEB-INF`

    **Note**: The jar utility is in the Java home bin directory. If it is not on your path you must call jar with the entire path, for example, `/opt/jdk1.8.0/bin/jar.exe`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722742-Logi-Report-Server-Integration)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749841-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)
