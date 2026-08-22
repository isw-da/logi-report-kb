---
title: "Deploying to Jboss-as-7.1.1.Final or JBoss EAP 7.0"
id: 1500009648422
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648422-Deploying-to-Jboss-as-7-1-1-Final-or-JBoss-EAP-7-0
updated_at: 2021-07-24T20:54:12Z
---

# Deploying to Jboss-as-7.1.1.Final or JBoss EAP 7.0

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673101-Deploying-to-Tomcat-8-5-23)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648442-Deploying-to-OC4J-10g-R3-10-1-3-5-0-)

# Deploying to Jboss-as-7.1.1.Final or JBoss EAP 7.0

This topic introduces how to deploy Logi JReport Server Guide v15 Server to Jboss-as-7.1.1.Final or JBoss EAP 7.0. The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\Logi JReport\Server` instead of `/opt/Logi JReport/Server`.

The following takes JBoss EAP 7.0 as an example.

It is assumed that:

* JBoss EAP 7.0 is installed in the `/opt/JBoss EAP 7.0` directory.
* The Logi JReport Server WAR file Logi JReport.war is located in the `/opt/Logi JReport/Server/bin/distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server).

  **Note:** Before creating the WAR, you need to change JRPatternLayout to PatternLayout all over the LogConfig.properties file in `/opt/Logi JReport/Server/bin`.

**To deploy Logi JReport Server to JBoss EAP 7.0:**

1. To avoid the issue that JBoss EAP 7 cannot locate jrenv.jar, when building a WAR/EAR to deploy to JBoss EAP 7, add *-Djbossas7=true* in makewar.bat/sh like this:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920500119/integ_dply_jboss_add.gif)
2. After file Logi JReport.war is generated, extract it with your zip tool.
3. Create a file named *jboss-deployment-structure.xml* in the Logi JReport.war/META-INF directory. The file should contain the following contents:

   ```
   <?xml version="1.0" encoding="UTF-8"?>   
     
   <jboss-deployment-structure>   
      <deployment>   
         <exclusions>   
            <module name="org.apache.log4j" />   
         </exclusions>  
         <dependencies>
            <system>  
               <paths>  
                  <path name="com/sun/org/apache/xml/internal/security/utils"/>  
               </paths>  
            </system>  
         </dependencies>   
      </deployment>   
   </jboss-deployment-structure>
   ```
4. Compress the extracted Logi JReport.war back to a single file.
5. Start JBoss by running the standalone.sh script if it is not started.
6. Add a management user to JBoss EAP 7 by running the add-user.sh script. Then you need to access the JBoss Management Console to deploy Logi JReport.war and enable it.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920500887/integ_dply_jboss_dply.gif)
7. Access Logi JReport Server using the following URLs:

   `http://localhost:8080/Logi JReport/jrserver  
    http://localhost:8080/Logi JReport/admin/index.jsp  
    http://localhost:8080/Logi JReport/jinfonet/index.jsp`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Troubleshooting

If you run into problems when using Logi JReport Server in JBoss, send the log files of Logi JReport Server to [support@jinfonet.com](mailto:support@jinfonet.com). The following procedure illustrates how to generate the log files:

1. Modify the file standalone.conf in `/opt/JBoss EAP 7.0/bin`.

   In the file standalone.conf, add `-Dlogall=true` like this:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920501271/integ_dply_jboss_conf.gif)
2. After editing standalone.conf, start JBoss using the modified file.
3. After reproducing the problem, send [support@jinfonet.com](mailto:support@jinfonet.com) the log files in `reporthome/logs`.

   The JBoss log files may also help to identify the problem. The most useful one is `/opt/jboss-eap-7.0/standalone/log/server.log.`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673101-Deploying-to-Tomcat-8-5-23)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648442-Deploying-to-OC4J-10g-R3-10-1-3-5-0-)
