---
title: "Specifying Reporthome for Logi Report Server in a Java EE Environment"
id: 1500009776981
section: "Logi Report Server Integration Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776981-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment
updated_at: 2021-07-24T00:48:03Z
---

# Specifying Reporthome for Logi Report Server in a Java EE Environment

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777041-Four-Ways-of-Integrating-Logi-Report-Server)

# Specifying Reporthome for Logi Report Server in a Java EE Environment

This topic describes how you can specify reporthome for Logi Report Server in a Java EE Environment.

Logi Report Server requires a reporthome as its working space to hold the entire Logi Report runtime environment, including the server properties, configuration files, and resources. Logi Report Server extracts the package **jrenv.jar** that contains the entire Logi Report runtime environment to the specified reporthome when initializing Logi Report Server. The reporthome can be any location on the disk where Logi Report Server has the Read and Write privileges.

You can either use the default reporthome or customize the reporthome location before creating the Logi Report Server WAR/EAR file. You should make sure that the reporthome for the integrated Logi Report Server is different from that of the standalone Logi Report Server.

Logi Report also provides you with the **jet.server.api.http.CustomizedServerEnv** interface for specifying the Logi Report Server reporthome and for setting the server properties in a Java EE environment. If you specify the implementation of this interface, Logi Report Server will obtain not only reporthome but also server properties.
For more information, see [Setting Server Reporthome and Properties in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009771061-Setting-Server-Reporthome-and-Properties-in-a-Java-EE-Environment).

This topic contains the following sections:

* [Using the Default Reporthome](#Default)
* [Specifying the Reporthome in web.xml or ejb-jar.xml](#XML)
* [Specifying the Reporthome Using the JVM -D Parameter](#Parameter)
* [Specifying the Reporthome by Invoking API Method](#Method)

## Using the Default Reporthome

If you do not specify a reporthome, the self-contained Logi Report Server will create a default working folder. The default working folder is <user.home>/.jreport/default, where <user.home> is the system property user.home retrieved from Java VM. Logi Report Server has the Read and Write privileges in this directory.
Different OS has different real path for <user.home>. For example,

For Windows: `C:\Documents and Settings\username`

For Unix/Linux: `/home/username`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* user.home is a system property of the Java VM (-Duser.home=xxx). So, you can also specify different folders for this JVM option.
* If Logi Report Server is running on Windows as a service, the username is the user who installed the service or the specified logon user for the service.
* If Logi Report Server is running as a Unix/Linux Daemon, you can specify the JVM system property **-Duser.home** in the script file that starts Logi Report Server.

## Specifying the Reporthome in web.xml or ejb-jar.xml

You should use the <env-entry></env-entry> tags to specify the reporthome directly in the target **web.xml.norpthome** in the makewar.xml file or in ejb-jar.xml. Also, you can specify the reporthome using the <context-param></context-param> tags in the target **web.xml.filter**.

**To specify the reporthome for WAR:**

You can use either of the two methods below to specify the reporthome for WAR:

* In the **makewar.xml** file, use the <env-entry></env-entry> tags to specify the reporthome in the target **web.xml.norpthome**, and then uncomment the setting. For example:

  ```
  <env-entry-name>jreport.rpthome</env-entry-name>  
  <env-entry-value>/home/jreport</env-entry-value>  
   
  <env-entry-type>java.lang.String</env-entry-type>
  ```

  You should use this way to set reporthome since you can also use the <env-entry></env-entry> tags in ejb-jar.xml (if you call the Server API in your EJB).
* In the **makewar.xml** file, use the <context-param></context-param> tags to specify the reporthome in the target **web.xml.filter**, for example:

  ```
  <context-param>  
      <param-name>reporthome</param-name>  
      <param-value>/home/jreport</param-value>  
  </context-param>
  ```

### To specify the reporthome for EAR:

You can use the same methods to specify the reporthome of building the EAR file as of building the WAR file. However, because you can wrap WAR and EJB in the EAR file, you should ensure that you put the reporthome information either in the target **web.xml.norpthome** in the **makewar.xml** file (for the Web module) or in **ejb-jar.xml** (for the EJB module).

In ejb-jar.xml, use the <env-entry></env-entry> tags to specify the reporthome. For example:

```
<env-entry>  
    <env-entry-name>jreport.rpthome</env-entry-name>  
    <env-entry-value>/home/jreport</env-entry-value>  
    <env-entry-type>java.lang.String</env-entry-type>  
</env-entry>
```

## Specifying the Reporthome Using the JVM -D Parameter

Set the JVM option **-Dreporthome** before starting the application server, for example:

`-Dreporthome=/home/LogiReport`

## Specifying the Reporthome by Invoking API Method

You can invoke the method *jet.server.api.http.HttpUtil.initEnv(Properties props)* to specify the reporthome.

For example:

`Properties props = new Properties();  
props.setProperty("reporthome", "/home/test/LogiReport");  
HttpUti.initEnv(props);`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777041-Four-Ways-of-Integrating-Logi-Report-Server)
