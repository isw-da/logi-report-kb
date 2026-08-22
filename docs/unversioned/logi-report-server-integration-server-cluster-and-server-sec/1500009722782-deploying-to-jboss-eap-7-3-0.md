---
title: "Deploying to JBoss EAP 7.3.0"
id: 1500009722782
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722782-Deploying-to-JBoss-EAP-7-3-0
updated_at: 2021-07-25T07:19:04Z
---

# Deploying to JBoss EAP 7.3.0

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749741-Deploying-to-Tomcat-9-0-34)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722822-Deploying-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)

# Deploying to JBoss EAP 7.3.0

This topic introduces how to deploy Logi Report Server to JBoss EAP. The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\LogiReport\Server` instead of `/optLogiReport/Server`.

The following takes JBoss EAP 7.3.0 as an example.

It is assumed that:

* JBoss EAP 7.3.0 is installed in the `/opt/JBoss EAP 7.3.0` directory.
* The Logi Report Server WAR file jreport.war is located in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  **Note:** Before creating the WAR, you need to change JRPatternLayout to PatternLayout all over the LogConfig.properties file in `/opt/LogiReport/Server/bin`. After jreport.war is generated, create a file named jboss-deployment-structure.xml as follows in the jreport.war/META-INFO folder:

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

1. To avoid the issue that JBoss EAP 7 cannot locate jrenv.jar, when building a WAR/EAR to deploy to JBoss EAP 7, add -Djbossas7=true in makewar.bat/sh like this:

   ![Add -Djbossas7=true](https://devnet.logianalytics.com/hc/article_attachments/4404936808727/integ_dply_jboss_add.gif)
2. Start JBoss by running the standalone.sh script if it is not started.
3. Add a management user to JBoss EAP 7 by running the add-user.sh script. Then you need to access the JBoss Management Console to deploy jreport.war and enable it.

   ![JBoss Management Console](https://devnet.logianalytics.com/hc/article_attachments/4404936808983/integ_dply_jboss_dply.gif)
4. Access Logi Report Server using the following URLs:

   `http://localhost:8080/jreport/jrserver
     
    http://localhost:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in JBoss, send the log files of Logi Report Server to [support@logianalytics.com](mailto:support@logianalytics.com). The following procedure illustrates how to generate the log files:

1. Modify the file standalone.conf in `/opt/JBoss EAP 7.3.0/bin`.

   In the file standalone.conf, add `-Dlogall=true` like this:

   ![Add -Dlogall=true](https://devnet.logianalytics.com/hc/article_attachments/4404942514967/integ_dply_jboss_conf.gif)
2. After editing standalone.conf, start JBoss using the modified file.
3. After reproducing the problem, send [support@logianalytics.com](mailto:support@logianalytics.com) the log files in `reporthome/logs`.

   The JBoss log files may also help to identify the problem. The most useful one is /opt/jboss-eap-7.3.0/standalone/log/server.log.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749741-Deploying-to-Tomcat-9-0-34)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722822-Deploying-to-Sun-Java-System-Application-Server-Platform-Edition-9-1)
