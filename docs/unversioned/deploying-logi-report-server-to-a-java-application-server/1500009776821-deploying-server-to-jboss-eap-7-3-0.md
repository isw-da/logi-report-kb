---
title: "Deploying Server to JBoss EAP 7.3.0"
id: 1500009776821
section: "Deploying Logi Report Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776821-Deploying-Server-to-JBoss-EAP-7-3-0
updated_at: 2021-07-24T00:48:04Z
---

# Deploying Server to JBoss EAP 7.3.0

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776881-Deploying-Server-to-Tomcat-9-0-38)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748442-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)

# Deploying Server to JBoss EAP 7.3.0

This topic describes how you can deploy Logi Report Server to JBoss EAP.

In the example we use directory paths based on Unix. The instructions are applicable to both Unix and Windows installations. However, the format of the paths for Windows should use the Windows format, that is, `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

The example takes JBoss EAP 7.3.0 as an example.

Assumed that:

* You installed JBoss EAP 7.3.0 in the `/opt/JBoss EAP 7.3.0` directory.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404885352855/criticalicon.gif)Before creating the WAR, you need to change **JRPatternLayout** to **PatternLayout** all over the **LogConfig.properties** file in `/opt/LogiReport/Server/bin`. After you generate **jreport.war**, create a file named **jboss-deployment-structure.xml** as follows in the jreport.war/META-INFO folder:

  ```
  <?xml version="1.0" encoding="UTF-8"?>  
      <jboss-deployment-structure>   
          <deployment>   
              <dependencies>  
                  <system>  
                      <paths>  
                          <path name="org/w3c/dom/css"/>  
                      </paths>  
                  </system>  
              </dependencies>  
          </deployment>  
      </jboss-deployment-structure>
  ```

**To deploy Logi Report Server to JBoss EAP 7.3.0:**

1. To avoid the problem that JBoss EAP 7 cannot locate jrenv.jar, when you build a WAR/EAR to deploy to JBoss EAP 7, add **-Djbossas7=true** in makewar.bat/sh like this:

   ![Add -Djbossas7=true](https://devnet.logianalytics.com/hc/article_attachments/4404885425303/integ_dply_jboss_add.gif)
2. Start JBoss by running the **standalone.sh** script.
3. Add a management user to JBoss EAP 7 by running the add-user.sh script.
4. Access the JBoss Management Console to deploy **jreport.war** and enable it.

   ![JBoss Management Console](https://devnet.logianalytics.com/hc/article_attachments/4404885425559/integ_dply_jboss_dply.gif)
5. Access Logi Report Server using the following URLs:

   `http://localhost:8080/jreport/jrserver
     
    http://localhost:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in JBoss, send the log files of Logi Report Server to [support@logianalytics.com](mailto:support@logianalytics.com). The following procedure illustrates how to generate the log files:

1. Modify the file **standalone.conf** in `/opt/JBoss EAP 7.3.0/bin` to add **-Dlogall=true** as follows.

   ![Add -Dlogall=true](https://devnet.logianalytics.com/hc/article_attachments/4404880310935/integ_dply_jboss_conf.gif)
2. Start JBoss using the modified file standalone.conf.
3. After you reproduce the problem, send [support@logianalytics.com](mailto:support@logianalytics.com) the log files in `reporthome/logs`.

   The JBoss log files may also help to identify the problem. The most useful one is /opt/jboss-eap-7.3.0/standalone/log/server.log.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776881-Deploying-Server-to-Tomcat-9-0-38)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748442-Deploying-Server-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
