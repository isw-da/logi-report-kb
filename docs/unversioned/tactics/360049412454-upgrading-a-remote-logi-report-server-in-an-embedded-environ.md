---
title: "Upgrading a Remote Logi Report Server in an Embedded Environment"
id: 360049412454
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049412454-Upgrading-a-Remote-Logi-Report-Server-in-an-Embedded-Environment
updated_at: 2022-10-31T11:37:26Z
---

# Upgrading a Remote Logi Report Server in an Embedded Environment

### Part 1: Download and install a new version of Logi Report Server

1. Shut down the old version of Logi Report Server.
2. Download a new version of Logi Report Server and install it. For Linux without GUI, use the following command.  
   *./server-xxxxxxx-linux.bin -i console*  
   (xxxxxxx is the build number)
3. Choose option 3 for "Choose Installation Set", and then type in the installation location of the old version of Logi Report Server.

   ![Choose Installation Set](https://devnet.logianalytics.com/hc/article_attachments/9901229356951)
4. Start the install, and type in username, license key, and so on.
5. Type N for "Start Logi Report Server once installation is completed."

   ![Installation Completed](https://devnet.logianalytics.com/hc/article_attachments/9901244912919)

### Part 2: Delete old JAR files Backup and delete the following old libraries. For example, users can simply rename ant.jar to ant.jar.bak.

* activation-1.1.jar.
* ant.jar
* ant-launcher.jar
* commons-collections-3.2.1.jar
* commons-httpclient-3.0.jar
* commons-logging-1.1.jar
* commons-net-ftp-2.0.0.jar
* dwr-1.1.3.jar
* hsqldb.jar
* itext\_1.5.4.jar
* iTextAsian.jar
* jai\_codec.jar
* jai\_core.jar
* jasper-compiler.jar
* jasper-runtime.jar
* jdom-1.0.jar
* jsch-0.1.30.jar
* jaxen-1.1-beta-9.jar
* mail-1.4.jar
* opensaml-1.1.jar
* sac.jar
* servlet.jar
* woden-api-1.0M8.jar
* woden-impl-dom-1.0M8.jar
* wsdl4j-1.6.1.jar
* wstx-asl-3.2.0.jar
* xercesImpl.jar
* XmlSchema-1.4.5.jar
* xmlsec-1.4.3.jar
* wss4j-1.5.8.jar
* log4j-1.2.8.jar
* jgroups-all.jar

### Part 3: Start the upgraded Logi Report Server

1. Start the upgraded Logi Report Server with the following command.  
   *./Server.sh*  
   It may fail for the first time. If the server is a clustered server, try to start it again. If not, open the server.properties file located in <Server\_install\_root>/bin, and then change the value of the cluster.enable property from true to false.
2. Login to the upgraded Logi Report Server after it starts.

### Part 4: Upgrade the remote war

1. Test the upgraded Logi Report Server. Shut it down after the test is successful.
2. Back up the dbconfig.xml file under the <Server\_install\_root>/bin directory if the system database is NOT Derby.
3. Copy the backup of the dbconfig.xml file to <Server\_install\_root>/bin again (ignore this step if using Derby).
4. Create a remote.war file based on the upgraded Logi Report Server. Details [here](https://documentation.logianalytics.com/logireportserverguidev17/content/search.htm?q=remote%20.war).
5. Stop the application server (e.g., JBoss, Apache Tomcat, etc.).
6. Back up and then delete the old remote.war and the folder created by the remote.war. As an example for Tomcat, delete the contents in $TOMCAT\_HOME/webapps, and clear Tomcat’s cache (e.g., delete the folder $TOMCAT\_HOME/work/localhost/remote).
7. Redeploy the newly created remote.war to your application server.
8. Start Logi Report Server and the application server.
