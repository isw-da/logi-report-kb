---
title: "Specifying Reporthome for Logi JReport Server in a Java EE Environment"
id: 1500009717521
section: "Server Integration Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717521-Specifying-Reporthome-for-Logi-JReport-Server-in-a-Java-EE-Environment
updated_at: 2021-11-03T06:56:57Z
---

# Specifying Reporthome for Logi JReport Server in a Java EE Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717561-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691242-Four-Ways-of-Integrating-Logi-Report-Server)

# Specifying Reporthome for Logi JReport Server in a Java EE Environment

This topic introduces how to specify reporthome for Logi JReport Server in a Java EE Environment. Logi JReport Server requires a reporthome as its working space to hold the entire Logi JReport runtime environment, including the server properties, configuration files and resources. The package jrenv.jar that contains the entire Logi JReport runtime environment will be extracted to the specified reporthome when initializing Logi JReport Server. The reporthome can be any location on the disk where Logi JReport Server has the Read and Write privileges.

You can either use the default reporthome or customize the reporthome location before creating the Logi JReport Server WAR/EAR file. You should make sure that the reporthome for the integrated Logi JReport Server is different from that of the standalone Logi JReport Server.

Logi JReport also provides you with the jet.server.api.http.CustomizedServerEnv interface for specifying the Logi JReport Server reporthome and for setting the server properties in a Java EE environment. If you specify the implementation of this interface, Logi JReport Server will obtain not only reporthome but also server properties.
For details, see [Setting Server Reporthome and Properties in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009712021-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment).

Below is a list of the sections covered in this topic:

* [Using the Default Reporthome](#Default)
* [Specifying the Reporthome in web.xml or ejb-jar.xml](#XML)
* [Specifying the Reporthome Using the JVM -D Parameter](#Parameter)
* [Specifying the Reporthome by Invoking API Method](#Method)

## Using the Default Reporthome

If you do not specify a reporthome, the self-contained Logi JReport Server will create a default working folder. The default working folder is <user.home>/.jreport/default, where <user.home> is the system property user.home retrieved from Java VM. Logi JReport Server has the Read and Write privileges in this directory.
Different OS has different real path for <user.home>. For example,

For Windows: `C:\Documents and Settings\username`

For Unix/Linux: `/home/username`

**Notes:**

* user.home is a system property of the Java VM (-Duser.home=xxx). So you can also specify different folders for this JVM option.
* If Logi JReport Server is running on Windows as a service, the username is the user who installed the service or the specified logon user for the service.
* If Logi JReport Server is running as a Unix/Linux Daemon, you can specify the JVM system property -Duser.home in the script file that starts Logi JReport Server.

## Specifying the Reporthome in web.xml or ejb-jar.xml

It is recommended that you use the <env-entry></env-entry> tags to specify the reporthome directly in the target "web.xml.norpthome" in the makewar.xml file or in ejb-jar.xml. Also, in the target "web.xml.filter", you can specify the reporthome using the <context-param></context-param> tags.

**To specify the reporthome for WAR:**

You can use one of the two methods listed below to specify the reporthome for WAR:

* In the makewar.xml file, use the <env-entry></env-entry> tags to specify the reporthome in the target "web.xml.norpthome", and then uncomment the setting. For example:

  ```
  <env-entry-name>jreport.rpthome</env-entry-name>  
  <env-entry-value>/home/jreport</env-entry-value>  
   
  <env-entry-type>java.lang.String</env-entry-type>
  ```

  This is the recommended way to set reporthome since the <env-entry></env-entry> tags are also supported in ejb-jar.xml (if you call the Server API in your EJB).
* In the makewar.xml file, use the <context-param></context-param> tags to specify the reporthome in the target "web.xml.filter", for example:

  ```
  <context-param>  
      <param-name>reporthome</param-name>  
   
      <param-value>/home/jreport</param-value>  
  </context-param>
  ```

### To specify the reporthome for EAR:

The same methods can be used to specify the reporthome of building the EAR file as of building the WAR file. However, because you can wrap WAR and EJB in the EAR file, you should ensure that you put the reporthome information either in the target "web.xml.norpthome" in the makewar.xml file (for the Web module) or in ejb-jar.xml (for the EJB module).

In ejb-jar.xml, use the <env-entry></env-entry> tags to specify the reporthome. For example:

```
<env-entry>  
            
    <env-entry-name>jreport.rpthome</env-entry-name>  
            
    <env-entry-value>/home/jreport</env-entry-value>  
            
    <env-entry-type>java.lang.String</env-entry-type>  
            
<env-entry>
```

## Specifying the Reporthome Using the JVM -D Parameter

Set the JVM option -Dreporthome before starting the application server, for example:

`-Dreporthome=/home/jreport`

## Specifying the Reporthome by Invoking API Method

You can invoke the method *jet.server.api.http.HttpUtil.initEnv(Properties props)* to specify the reporthome.

For example:

`Properties props = new Properties();  
props.setProperty("reporthome", "/home/test/JReport");  
HttpUti.initEnv(props);`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717561-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009691242-Four-Ways-of-Integrating-Logi-Report-Server)
