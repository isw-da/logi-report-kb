---
title: "Setting Server Reporthome and Properties in a Java EE Environment"
id: 4405683555095
section: "Working with APIs Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683555095-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment
updated_at: 2022-01-27T08:00:03Z
---

# Setting Server Reporthome and Properties in a Java EE Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690474135-Writing-Customized-Load-Balancing-Algorithm)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690477079-Loading-User-Data-Source-Classes-at-Runtime)

# Setting Server Reporthome and Properties in a Java EE Environment

You can use the interface **jet.server.api.http.CustomizedServerEnv** to specify the Logi Report Server reporthome and to set the server properties in [a Java EE environment](https://devnet.logianalytics.com/hc/en-us/articles/4405683907223--Server-Integration-Server-v18). This topic describes the interface **CustomizedServerEnv** and how you can apply the default and customized implementations of the interface.

The interface **CustomizedServerEnv** contains two methods: *String getReportHome()* and *Properties getServerProperties()*. The properties returned from *getServerProperties()* can be the properties in the server.properties file in `<install_root>\bin`, JVM System properties, or self-defined ones. If you specify the implementation of this interface,
Logi Report Server will retrieve the reporthome and properties from your implemented class when the WAR/EAR file is deployed.

This topic contains the following sections:

* [Using the Default Implementations of CustomizedServerEnv](#Default)
* [Using a Customized Implementation of CustomizedServerEnv](#Customized)

## Using the Default Implementations of CustomizedServerEnv

The self-contained Logi Report Server provides two implementations of CustomizedServerEnv. They are jet.server.DefaultServerEnv and jet.server.MultipleInstanceServerEnv.

**jet.server.DefaultServerEnv**

If you use this implementation, you will not need to specify it in the target web.xml in the makewar.xml or in ejb-jar.xml, because it can find the customized reporthome from the <context-param></context-param> tags of the target web.xml or the <env-entry></env-entry> tags of web.xml or ejb-jar.xml.

**jet.server.MultipleInstanceServerEnv**

This is an internally implemented class of the jet.server.api.http.CustomizedServerEnv interface which supports multiple Logi Report Server instances in one Java EE application server. The class can automatically assign the reporthome of each instance.

This implementation extends DefaultServerEnv. It enables finding the reporthome not only from the <context-param></context-param> or <env-entry></env-entry> tags, but also from an external file <user.home>/.jreportrc. However, this implementation has three main limitations:

* You must specify this implementation with the <env-entry></env-entry> tags in the target **web.xml** in makewar.xml or in ejb-jar.xml.

  ```
  <env-entry>  
      <env-entry-name>jreport.servenv</env-entry-name>  
      <env-entry-value>jet.server.MultipleInstanceServerEnv</env-entry-value>  
      <env-entry-type>java.lang.String</env-entry-type>
  </env-entry>
  ```
* The Logi Report Server must be initialized with JRServerContextListener from a Web module.

  In cases of deploying multiple Logi Report Server instances in one Java EE application server without touching the WAR, such as extracting the WAR, setting reporthome, and rebuilding the WAR, Logi Report Server has to use ServletContext to generate an ID for every instance. Logi Report Server retrieves javax.servlet.context.tempdir from ServletContext by invoking the method *getAttribute(String)*, and then uses this value to generate the instance ID.

  For more information, see Java Servlet Specification Version 2.3/2.4 SRV.3.7.1 Temporary Working Directories.
* Logi Report Server must create the <user.home>/.jreportrc file. You can only edit the file to change the reporthome after the Logi Report Server initialization.

  Since the instance ID is generated based on a hash code retrieved from javax.servlet.context.tempdir, it cannot be pre-assigned, and is therefore impossible for you to create the <user.home>/.jreportrc file. However, once the file is created, you can edit it to change the reporthome for each instance. The RC file can hold multiple records. The record format should be `jreport.rpthome.<instanceID>=the-instance-report-home`.

  Logi Report Server creates the instanceID during its first initializing. It is a string of HEX encoded hash value. For example:

  `jreport.rpthome.12345678=/home/user1/.jreport/instance.12345678`

  `jreport.rpthome.12345abc=/home/user1/.jreport/instance.12345abc`

  If Logi Report Server cannot get the reporthome from CustomizedServerEnv, it will create a default reporthome in <user.home>/.jreport/default.

The following example shows how to specify the reporthome when deploying multiple server instances using jet.server.MultipleInstanceServerEnv.

1. In the file **makewar.xml**, use the <env-entry></env-entry> tags to specify jet.server.MultipleInstanceServerEnv in the target "web.xml". For example:

   ```
   <env-entry>  
       <env-entry-name>jreport.servenv</env-entry-name>  
       <env-entry-value>jet.server.MultipleInstanceServerEnv</env-entry-value>  
       <env-entry-type>java.lang.String</env-entry-type>  
   </env-entry>
   ```
2. Since different Logi Report instances cannot access the same Logi Report Server system database at the same time, you will need to create a dbconfig.xml file to store the connection information, and put it in jrenv.jar in `workspace\bin` (you can find the jrenv.jar file after extracting jreport.war) for each Logi Report Server WAR/EAR.

   For more information about modifying dbconfig.xml, see [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/4405690486423-Configuring-the-Server-Database).
3. When the Logi Report Server WAR/EAR has been deployed, Logi Report will create a file **.jreportrc** in <user.home>, and each Logi Report instance will read its reporthome from this file. This file must be created by Logi Report Server; however, you can edit it in order to change the reporthome after it is created.

## Using a Customized Implementation of CustomizedServerEnv

You can implement the interface and add your class to the generated WAR/EAR file, then use the <env-entry></env-entry> tags to specify your implemented class in the target web.xml inmakewar.xml file or in ejb-jar.xml.

In the following example, the customized implementation of CustomizedServerEnv is named **my.ReportServerEnv**.

```
<!-- Logi ReportServer calls my.ReportServerEnv to obtain reporthome and server properties.-->  
<env-entry>  
    <env-entry-name>jreport.servenv</env-entry-name> <!-- must be jreport.servenv-->  
    <env-entry-value>my.ReportServerEnv</env-entry-value> <!-- your class name -->   
    <env-entry-type>java.lang.String</env-entry-type>  
</env-entry>
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690474135-Writing-Customized-Load-Balancing-Algorithm)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690477079-Loading-User-Data-Source-Classes-at-Runtime)
