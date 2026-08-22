---
title: "Deploying Server to Resin"
id: 45204012032141
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204012032141-Deploying-Server-to-Resin
updated_at: 2026-04-30T14:10:19Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Deploying Server to Resin 4.0.66

This topic describes how you can deploy Report Server to Resin 4.0.66. 

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format C:\LogiReport\Server instead of /opt/LogiReport/Server. 

Assume that:

- You installed Resin 4.0.66 in the /opt/resin directory.

- The Report Server WAR file jreport.war is in the /opt/LogiReport/Server/bin/distribute directory. To create the WAR file, see Building a WAR/EAR File to Include a Self-contained Report Server.  

To deploy Report Server to Resin 4.0.66:

- Generate the password.
    

- Modify resin.properties in /opt/resin/conf. Set remote_admin_enable to true and add the generated password. 
    

- Enable the commands that allow administrators and programmers to perform debugging and monitoring tasks on the remote Resin server using command line. 
    By default, these commands are disabled. To enable them, register ManagerService in the resin.xml file. Since the default resin.xml already includes a <resin:AdminAuthenticator> with a <resin:import>, you can just reuse the admin configuration from the /resin-admin page.

- Start Resin by running the resin.sh start script in /opt/resin/bin. 

- Sign in to the Resin Administration Console with the specified username and password using the URL http://localhost:8080/resin-admin/index.php. 

- In the deploy tab, select Browse to select the file jreport.war. 

- In the Name text box, type jreport. 

- Select Deploy. 

- Access Report Server using the following URLs:
    http://localhost:8080/jreport/jrserver
    
    http://localhost:8080/jreport/jinfonet/index.jsp

## Troubleshooting

If you run into problems when using Report Server in Resin, you may have to send the log files of Report Server to Customer Service. The following procedure illustrates how to generate the log files: 

- Modify the file resin.sh in /opt/resin/bin by adding -Dlogall=true after the reporthome definition:
    

"$JAVA" $JAVA_OPTS \
 
-classpath "$RESIN_CLASSPATH" -Dreporthome=/opt/LogiReport/Server \ 
-Dlogall=true  \ 
org.resin.Main "$@"

- Run the modified resin.sh to start Resin. 

- After reproducing the problem, send the log files in reporthome/logs to Customer Service.
    The Resin log files may also help identify the problem. The most useful one is /opt/Resin/server/default/log/server.log.
