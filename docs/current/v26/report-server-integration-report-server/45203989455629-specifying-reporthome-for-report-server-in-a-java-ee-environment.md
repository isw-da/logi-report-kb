---
title: "Specifying Reporthome for Report Server in a Java EE Environment"
id: 45203989455629
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203989455629-Specifying-Reporthome-for-Report-Server-in-a-Java-EE-Environment
updated_at: 2026-04-30T14:10:22Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Specifying Reporthome for Report Server in a Java EE Environment 

This topic describes how you can specify reporthome for Report Server in a Java EE Environment. 

Report Server requires a reporthome as its working space to hold the entire Report runtime environment, including the server properties, configuration files, and resources. Report Server extracts the package jrenv.jar that contains the entire Report runtime environment to the specified reporthome when initializing Report Server. The reporthome can be any location on the disk where Report Server has the Read and Write privileges.

You can either use the default reporthome or customize the reporthome location before creating the Report Server WAR/EAR file. You should make sure that the reporthome for the integrated Report Server is different from that of the standalone Report Server.

Report also provides you with the jet.server.api.http.CustomizedServerEnv interface for specifying the Report Server reporthome and for setting the server properties in a Java EE environment. If you specify the implementation of this interface, Report Server will obtain not only reporthome but also server properties.
For more information, see Setting Server Reporthome and Properties in a Java EE Environment.

This topic contains the following sections:

- Using the Default Reporthome 
                

- Specifying the Reporthome in web.xml or ejb-jar.xml
                

- Specifying the Reporthome Using the JVM -D Parameter
                

- Specifying the Reporthome by Invoking API Method 
                

## 
Using the Default Reporthome 

If you do not specify a reporthome, the self-contained Report Server will create a default working folder. The default working folder is <user.home>/.jreport/default, where <user.home> is the system property user.home retrieved from Java VM. Report Server has the Read and Write privileges in this directory. 
 Different OS has different real path for <user.home>. For example,

For Windows: C:\Documents and Settings\username

For UNIX/Linux: /home/username

- user.home is a system property of the Java VM (-Duser.home=xxx). So, you can also specify different folders for this JVM option.
    

- If Report Server is running on Windows as a service, the username is the user who installed the service or the specified user who can sign in to the service.
    

- If Report Server is running as a UNIX/Linux Daemon, you can specify the JVM system property -Duser.home in the script file that starts Report Server.

## 
Specifying the Reporthome in web.xml or ejb-jar.xml

You should use the <env-entry></env-entry> tags to specify the reporthome directly in the target web.xml.norpthome in the makewar.xml file or in ejb-jar.xml. Also, you can specify the reporthome using the <context-param></context-param> tags  in the target web.xml.filter.

To specify the reporthome for WAR:

You can use either of the two methods to specify the reporthome for WAR: 

- In the makewar.xml file, use the <env-entry></env-entry> tags to specify the reporthome in the target web.xml.norpthome, and then uncomment the setting. For example:
                

<env-entry-name>jreport.rpthome</env-entry-name>
<env-entry-value>/home/jreport</env-entry-value>
 
<env-entry-type>java.lang.String</env-entry-type>
You should use this way to set reporthome since you can also use the <env-entry></env-entry> tags in ejb-jar.xml (if you call the Server API in your EJB).

- In the makewar.xml file, use the <context-param></context-param> tags to specify the reporthome in the target web.xml.filter, for example:
    

<context-param>
    <param-name>reporthome</param-name>
    <param-value>/home/jreport</param-value>
</context-param>

### To specify the reporthome for EAR:

You can use the same methods to specify the reporthome of building the EAR file as of building the WAR file. However, because you can wrap WAR and EJB in the EAR file, you should ensure that you put the reporthome information either in the target web.xml.norpthome in the makewar.xml file (for the Web module) or in ejb-jar.xml (for the EJB module).

In ejb-jar.xml, use the <env-entry></env-entry> tags to specify the reporthome. For example:

<env-entry>
    <env-entry-name>jreport.rpthome</env-entry-name>
    <env-entry-value>/home/jreport</env-entry-value>
    <env-entry-type>java.lang.String</env-entry-type>
</env-entry>

## 
Specifying the Reporthome Using the JVM -D Parameter

Set the JVM option -Dreporthome before starting the application server, for example:

-Dreporthome=/home/LogiReport

## 
Specifying the Reporthome by Invoking API Method 

You can invoke the method jet.server.api.http.HttpUtil.initEnv(Properties props) to specify the reporthome. 

For example:

Properties props = new Properties();
props.setProperty("reporthome", "/home/test/LogiReport");
HttpUti.initEnv(props);
