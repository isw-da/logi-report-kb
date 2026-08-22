---
title: "Deploying Server to IBM WebSphere 9.0.5.6"
id: 45204012229133
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204012229133-Deploying-Server-to-IBM-WebSphere-9-0-5-6
updated_at: 2026-04-30T14:10:20Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Deploying Server to IBM WebSphere 9.0.5.6

This topic describes how you can deploy Report Server to IBM WebSphere 9.0.5.6. 

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assume that:

- You installed WebSphere 9.0.5.6 in the /opt/IBM/WebSphere/AppServer directory. 

- The Report Server WAR file jreport.war is in the /opt/LogiReport/Server/bin/distribute directory. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server.
     Before creating the WAR, you need to modify the LogConfig.properties file in /opt/LogiReport/Server/bin: 

- Change JRPatternLayout to PatternLayout all over the file. 

- Change all the Logger levels from ERROR to TRACE.

To deploy Report Server to IBM WebSphere:

- Copy Derby jars in /opt/LogiReport/Server/derby to the /opt/IBM/WebSphere/AppServer/lib directory.

- Run the shell script /opt/IBM/WebSphere/AppServer/bin/startServer.sh <servername> to start the IBM WebSphere server. The default server name is server1.

- Access the WebSphere Administrative Console using the URL http://hostname:9060/ibm/console, where hostname is host name or IP address and 9060 is the port number.

- Provide your username and password.

- After you sign in, expand Applications.

- Select Application Types.

- Select Websphere enterprise applications.

- Select Install.

- Select Browse to select the jreport.war file.

- Keep selecting Next until you see the requirement for specifying context root.

- In the Context Root field, type a context path such as /jreport/.

- Select Next.

- Select Finish in the Summary page. The installing process may take several minutes. Wait until the process completes.

- Select Save.

- Select jreport.war.

- Select Start to start Report Server.

- Access Report Server using the following URL:
      http://<hostname>:9080/jreport/jrserver
      
http://<hostname>:9080/jreport/jinfonet/index.jsp

## Troubleshooting

If you run into problems when using Report Server in IBM WebSphere, you may have to send the log files of Report Server to Customer Service. The following procedure illustrates how to generate the log files:

- Go to Application servers > server1 > Process Definition > Java Virtual Machine.

- Type -Dlogall=true in the Generic JVM arguments field. 

- Restart the application server.

- Try to reproduce the problem. 

- After reproducing the problem, send Customer Service the log files in reporthome/logs.The WebSphere log files may also help to identify the problem. The most useful one is in /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/logs/server1/SystemErr.log.

 For WebSphere Application Server Liberty Profile, you need to:

- Configure JNDI to generate the reporthome. Add the following lines in server.xml in ${WebSphere_home}/usr/servers/defaultServer:
    <featureManager>
<feature>jndi-1.0</feature>
</featureManager>

- Extract jreport.war to ${wlphome}/usr/servers/defaultServer/dropins and then start WebSphere Application Server Liberty Profile. In this way the sample reports will be able to run well.
