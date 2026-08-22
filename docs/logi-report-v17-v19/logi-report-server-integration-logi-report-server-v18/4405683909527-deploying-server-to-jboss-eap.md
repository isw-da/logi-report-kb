---
title: "Deploying Server to JBoss EAP"
id: 4405683909527
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683909527-Deploying-Server-to-JBoss-EAP
updated_at: 2022-01-27T07:59:33Z
---

# Deploying Server to JBoss EAP

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690629655-Deploying-Server-to-Tomcat)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690628631-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)

# Deploying Server to JBoss EAP 7.4.0

This topic describes how you can deploy Logi Report Server to JBoss EAP 7.4.0.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assumed that:

* You installed JBoss EAP 7.4.0 in the `/opt/JBossEAP` directory.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif) Before creating the WAR, you need to change **JRPatternLayout** to **PatternLayout** all over the **LogConfig.properties** file in `/opt/LogiReport/Server/bin`. After you generate **jreport.war**, create a file named **jboss-deployment-structure.xml** in the jreport.war/META-INFO folder:

  ```
  <?xml version="1.0" encoding="UTF-8"?>  
      <jboss-deployment-structure xmlns="urn:jboss:deployment-structure:1.1">   
          <deployment>   
              <dependencies>  
                  <system export="true">  
                      <paths>  
                          <path name="org/w3c/dom/css"/>  
                      </paths>  
                  </system>  
              </dependencies>  
          <exclusions>  
              <module name="org.apache.logging.log4j.api"/>  
          </exclusions>  
          </deployment>  
      </jboss-deployment-structure>
  ```

**To deploy Logi Report Server to JBoss EAP 7.4.0:**

1. To avoid the problem that JBoss EAP 7 cannot locate jrenv.jar, when you build a WAR/EAR to deploy to JBoss EAP 7, add **-Djbossas7=true** in makewar.bat/sh like this:

   ![Add -Djbossas7=true](https://devnet.logianalytics.com/hc/article_attachments/4420453531543/integ_dply_jboss_add.gif)
2. Start JBoss by running the **standalone.sh** script.
3. Add a management user to JBoss EAP 7 by running the add-user.sh script.
4. Access the JBoss Management Console to deploy **jreport.war** and enable it.

   ![JBoss Management Console](https://devnet.logianalytics.com/hc/article_attachments/4420461605399/integ_dply_jboss_dply.gif)
5. Access Logi Report Server using the following URLs:

   `http://localhost:8080/jreport/jrserver
     
    http://localhost:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in JBoss, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Modify the **standalone.conf** file in `/opt/JBossEAP/bin` to add **-Dlogall=true**.

   ![Add -Dlogall=true](https://devnet.logianalytics.com/hc/article_attachments/4420453532311/integ_dply_jboss_conf.gif)
2. Start JBoss using the modified file standalone.conf.
3. After you reproduce the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs`.

   The JBoss log files may also help to identify the problem. The most useful one is /opt/jbosseap/standalone/log/server.log.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690629655-Deploying-Server-to-Tomcat)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690628631-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
