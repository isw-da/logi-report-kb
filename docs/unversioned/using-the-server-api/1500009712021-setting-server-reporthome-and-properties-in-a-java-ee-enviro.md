---
title: "Setting Server Reporthome and Properties in a Java EE Environment"
id: 1500009712021
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712021-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment
updated_at: 2021-11-03T06:58:35Z
---

# Setting Server Reporthome and Properties in a Java EE Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686262-Writing-Customized-Load-Balancing-Algorithm)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686362-Loading-User-Data-Source-Classes-at-Runtime)

# Setting Server Reporthome and Properties in a Java EE Environment

The jet.server.api.http.CustomizedServerEnv interface can be used for specifying the Logi JReport Server reporthome and for setting the server properties in [a Java EE environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009691142-Logi-JReport-Server-Integration). It contains two methods: *String getReportHome()* and *Properties getServerProperties()*. The properties returned from *getServerProperties()* can be the properties listed in the server.properties file stored in `<install_root>\bin`, JVM System properties, or self-defined ones. If you specify the implementation of this interface,
Logi JReport Server will retrieve the reporthome and properties from your implemented class when the WAR/EAR file is deployed.

Below is a list of the sections covered in this topic:

* [Using the Default Implementations of CustomizedServerEnv](#Default)
* [Using a Customized Implementation of CustomizedServerEnv](#Customized)

## Using the Default Implementations of CustomizedServerEnv

The self-contained Logi JReport Server provides two implementations of CustomizedServerEnv. They are jet.server.DefaultServerEnv and jet.server.MultipleInstanceServerEnv.

**jet.server.DefaultServerEnv**

If you use this implementation, you will not need to specify it in the target web.xml in the makewar.xml or in ejb-jar.xml, because it can find the customized reporthome from the <context-param></context-param> tags of the target web.xml or the <env-entry></env-entry> tags of web.xml or ejb-jar.xml.

**jet.server.MultipleInstanceServerEnv**

This is an internally implemented class of the jet.server.api.http.CustomizedServerEnv interface which supports multiple Logi JReport Server instances in one Java EE application server. The reporthome of each instance can be assigned by the class automatically.

This implementation is extended from DefaultServerEnv. It enables finding the reporthome not only from the <context-param></context-param> or <env-entry></env-entry> tags, but also from an external file <user.home>/.jreportrc. However, this implementation has three main limitations as shown below:

* This implementation must be clearly specified with the <env-entry></env-entry> tags in the target web.xml in makewar.xml or in ejb-jar.xml as follows:

  ```
  <env-entry>  

      <env-entry-name>jreport.servenv</env-entry-name>  

      <env-entry-value>jet.server.MultipleInstanceServerEnv</env-entry-value>  

      <env-entry-type>java.lang.String</env-entry-type>
  </env-entry>
  ```
* The Logi JReport Server must be initialized with JRServerContextListener from a Web module.

  In cases of deploying multiple Logi JReport Server instances in one Java EE application server without touching the WAR, such as extracting the WAR, setting reporthome and rebuilding the WAR, Logi JReport Server has to use ServletContext to generate an ID for every instance. Logi JReport Server retrieves javax.servlet.context.tempdir from ServletContext by invoking the method *getAttribute(String)*, and then uses this value to generate the instance ID.

  For detailed information, see Java Servlet Specification Version 2.3/2.4 SRV.3.7.1 Temporary Working Directories.
* The <user.home>/.jreportrc file must be created by Logi JReport Server. You can only edit the file to change the reporthome after the Logi JReport Server initialization.

  Since the instance ID is generated based on a hash code retrieved from javax.servlet.context.tempdir, it cannot be pre-assigned, and is therefore impossible for you to create the <user.home>/.jreportrc file. However, once the file is created, you can edit it to change the reporthome for each instance. The RC file can hold multiple records. The record format should be as follows:

  `jreport.rpthome.<instanceID>=the-instance-report-home`

  The instanceID is created by Logi JReport Server during its first initializing. It is a string of HEX encoded hash value. For example:

  `jreport.rpthome.12345678=/home/user1/.jreport/instance.12345678`

  `jreport.rpthome.12345abc=/home/user1/.jreport/instance.12345abc`

  If Logi JReport Server cannot get the reporthome from CustomizedServerEnv, it will create a default reporthome in <user.home>/.jreport/default.

The following example shows specifying the reporthome when deploying multiple server instances using jet.server.MultipleInstanceServerEnv.

1. In the file makewar.xml, use the <env-entry></env-entry> tags to specify jet.server.MultipleInstanceServerEnv in the target "web.xml". For example:

   ```
   <env-entry>  

       <env-entry-name>jreport.servenv</env-entry-name>  

       <env-entry-value>jet.server.MultipleInstanceServerEnv</env-entry-value>  

       <env-entry-type>java.lang.String</env-entry-type>  

   </env-entry>
   ```
2. Since different Logi JReport instances cannot access the same Logi JReport Server system database at the same time, you will need to create a dbconfig.xml file to store the connection information, and put it in jrenv.jar in `workspace\bin` (you can find the jrenv.jar file after extracting jreport.war) for each Logi JReport Server WAR/EAR.

   For detailed information about modifying dbconfig.xml, see [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009686662-Configuring-the-Server-Database).
3. When the Logi JReport Server WAR/EAR has been deployed, Logi JReport will create a file .jreportrc in <user.home>, and each Logi JReport instance will read its reporthome from this file. This file must be created by Logi JReport Server, however, you can edit it in order to change the reporthome after it is created.

## Using a Customized Implementation of CustomizedServerEnv

You can implement the interface and add your class to the generated WAR/EAR file, then use the <env-entry></env-entry> tags to specify your implemented class in the target web.xml inmakewar.xml file or in ejb-jar.xml.

The following shows an example. Here the customized implementation of CustomizedServerEnv is named my.JReportServerEnv.

```
<!-- Logi JReportServer calls my.JReportServerEnv to obtain reporthome and server properties.-->  

<env-entry>  

    <env-entry-name>jreport.servenv</env-entry-name> <!-- must be jreport.servenv-->  

    <env-entry-value>my.JReportServerEnv</env-entry-value> <!-- your class name -->   

    <env-entry-type>java.lang.String</env-entry-type>  

</env-entry>
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686262-Writing-Customized-Load-Balancing-Algorithm)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686362-Loading-User-Data-Source-Classes-at-Runtime)
