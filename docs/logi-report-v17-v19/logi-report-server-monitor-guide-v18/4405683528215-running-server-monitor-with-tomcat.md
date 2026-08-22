---
title: "Running Server Monitor with Tomcat"
id: 4405683528215
section: "Logi Report Server Monitor Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683528215-Running-Server-Monitor-with-Tomcat
updated_at: 2022-01-27T07:58:26Z
---

# Running Server Monitor with Tomcat

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690461463-Running-Server-Monitor-with-WebLogic-14-1-1)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690462359-Running-Server-Monitor-with-IBM-WebSphere-9-0-5-6-by-WAR-File)

# Running Server Monitor with Tomcat 9.0.56

This topic describes how you can run Server Monitor with Tomcat 9.0.56.

Assume that:

* You installed Server Monitor to `C:\LogiReport\Monitor.`
* You installed Tomcat to `C:\tomcat`.

Step 1: Configuring Tomcat

1. Build the Server Monitor WAR file using the makewar.bat/makewar.sh utility in the `C:\LogiReport\Monitor\bin` folder. Server Monitor generates the WAR file **monitor.war** to the folder `C:\LogiReport\Monitor\bin\distribute`.
2. Set **JAVA\_HOME** in the batch file **catalina.bat** in `C:\tomcat\bin`. For example, use `C:\jdk1.8.0`.

   ```
   rem $Id: catalina.bat,v 1.29 2020/09/08 19:51:31 patrickl Exp $  
   rem ---------------------------------------------------------------------------  
   set JAVA_HOME=C:\jdk1.8.0  
   rem Guess CATALINA_HOME if not defined  
   if not "%CATALINA_HOME%" == "" goto gotHome  
   set CATALINA_HOME=.
   ```
3. Modify **catalina.bat** again to set the Java system variable, for example,

   ```
   if not "%SECURITY_POLICY_FILE%" == "" goto doSecurity  
   %_EXECJAVA% %JAVA_OPTS% %CATALINA_OPTS% %DEBUG_OPTS%  
   -Djava.endorsed.dirs="%JAVA_ENDORSED_DIRS%"  
   -classpath "%CLASSPATH%"   
   -Dcatalina.base="%CATALINA_BASE%"  
   -Dmonitor.home="C:\LogiReport\Monitor"
   ```
4. Copy the WAR file **monitor.war** to `C:\tomcat\webapps`.
5. Copy **rmi.auth** from `<server_install_root>\bin` of the admin Server (the Server you want to monitor) to `C:\LogiReport\Monitor\bin`.
6. Enable RMI service for remote connection by setting the property **server.rmiserver.enable=true** in **server.properties** in `<server_intall_root>\bin`.
7. Start the admin Server.

Step 2 : Launching Tomcat

1. Start Tomcat using `C:\tomcat\bin\startup`.
2. Load the default page of Server Monitor using `http://hostname:8080/monitor` or `http://hostname:8080/monitor/monitor/index.jsp`.
3. If you install the admin Server and Server Monitor in different computers, you need to specify the right host and port of the admin Server in Server Monitor side via the following two properties in **server.properties** in `C:\LogiReport\Monitor\bin` before starting Tomcat:

   * admin.server.host = The RMI host name or IP address of the admin Server.
   * admin.server.port = The RMI port number of the admin Server.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690461463-Running-Server-Monitor-with-WebLogic-14-1-1)   [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690462359-Running-Server-Monitor-with-IBM-WebSphere-9-0-5-6-by-WAR-File)
