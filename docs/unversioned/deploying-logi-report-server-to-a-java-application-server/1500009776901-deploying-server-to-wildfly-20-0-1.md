---
title: "Deploying Server to WildFly 20.0.1"
id: 1500009776901
section: "Deploying Logi Report Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776901-Deploying-Server-to-WildFly-20-0-1
updated_at: 2021-07-24T00:48:02Z
---

# Deploying Server to WildFly 20.0.1

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776861-Deploying-Server-to-Resin-4-0-65)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776921-Integrating-Remote-Logi-Report-Server)

# Deploying Server to WildFly 20.0.1

This topic describes how you can deploy Logi Report Server to WildFly.

In the example we use directory paths based on Unix. The instructions are applicable to both Unix and Windows installations. However, the format of the paths for Windows should use the Windows format, that is, `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed WildFly 20.0.1 in the `/opt/wildfly` directory.
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

**To deploy Logi Report Server to WildFly 20.0.1:**

1. Start WildFly 20.0.1 by running the **standalone.sh** script in `/opt/wildfly/bin`.
2. By default, WildFly 20.0.1 is distributed with security enabled for the management interfaces. It means that before you connect using the administration console you need to add a new user. You can achieve this using the `add-user.sh` script in the **bin** folder. You will then need to set the user name and password for the new user.
3. Log onto the WildFly 20.0.1 Administration Console with the specified user name and password using the URL `http://localhost:9990/console`.
4. In the Deployments tab, select **Add**.
5. In the Create Deployment dialog box, browse to select the file **jreport.war**.
6. Select **Next**.
7. In the step 2 of the Create Deployment dialog box, select the **Enable** option and then select **Save**.
8. Upon the successful deployment of the Logi Report Server WAR file jreport.war, access Logi Report Server using the following URLs:

   `http://localhost:8080/jreport/jrserver
     
   http://localhost:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in WildFly, send the log files of Logi Report Server to [support@logianalytics.com](mailto:support@logianalytics.com). The following procedure illustrates how to generate the log files:

1. Modify the file **standalone.sh** in `/opt/wildfly/bin`, by adding **-Dlogall=true** after the reporthome definition:

   ```
   "$JAVA" $JAVA_OPTS \ -classpath "$WILDFLY_CLASSPATH" -Dreporthome=/opt/LogiReport/Server \ -Dlogall=true \ org.wildfly.Main "$@"
   ```
2. Start WildFly using the modified file **standalone.sh**.
3. After reproducing the problem, send [support@logianalytics.com](mailto:support@logianalytics.com) the log files in `reporthome/logs`.

   The WildFly log files may also help to identify the problem. The most useful one is /opt/wildfly/server/default/log/server.log.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If you encounter the problem that WildFly 20.0.1 cannot locate **jrenv.jar** when building a WAR/EAR to deploy to WildFly 20.0.1, add **-Djbossas7=true** in makewar.bat/sh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776861-Deploying-Server-to-Resin-4-0-65)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776921-Integrating-Remote-Logi-Report-Server)
