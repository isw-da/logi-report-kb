---
title: "Deploying to WildFly 17.0.1.Final"
id: 1500009717461
section: "Deploying Logi JReport Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717461-Deploying-to-WildFly-17-0-1-Final
updated_at: 2021-11-03T06:56:59Z
---

# Deploying to WildFly 17.0.1.Final

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691182-Deploying-to-Resin-4-0-62)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717481-Integrating-Remote-Logi-Report-Server)

# Deploying to WildFly 17.0.1.Final

This topic introduces how to deploy Logi JReport Server to WildFly. The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\JReport\Server` instead of `/opt/JReport/Server`.

It is assumed that:

* WildFly 17.0.1.Final is installed in the `/opt/wildfly` directory.
* The Logi JReport Server WAR file jreport.war is located in the `/opt/JReport/Server/bin/distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009717561-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  **Note:** Before creating the WAR, you need to change JRPatternLayout to PatternLayout all over the LogConfig.properties file in `/opt/JReport/Server/bin`. After jreport.war is generated, create a file named jboss-deployment-structure.xml as follows in the jreport.war/META-INFO folder:

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

**To deploy Logi JReport Server to WildFly 17.0.1.Final:**

1. Start WildFly 17.0.1.Final by running the standalone.sh script in `/opt/wildfly/bin`.
2. By default WildFly 17.0.1.Final is now distributed with security enabled for the management interfaces, this means that before you connect using the administration console you need to add a new user, this can be achieved using the `add-user.sh` script in the bin folder. You will then be prompted to set the user name and password for the new user.
3. Log onto the WildFly 17.0.1.Final Administration Console with the specified user name and password using the URL `http://localhost:9990/console`.
4. In the Deployments tab, select **Add**. In the Create Deployment dialog, browse to select the file jreport.war. Then select **Next**.
5. In the step 2 of the Create Deployment dialog, check the **Enable** option and then select **Save**.
6. Upon the successful deployment of the Logi JReport Server WAR file jreport.war, access Logi JReport Server using the following URLs:

   `http://localhost:8080/jreport/jrserver
     
   http://localhost:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi JReport Server in WildFly, send the log files of Logi JReport Server to [support@jinfonet.com](mailto:support@jinfonet.com). The following procedure illustrates how to generate the log files:

1. Modify the file standalone.sh in `/opt/wildfly/bin`.

   In the file standalone.sh, add -Dlogall=true after the reporthome definition:

   ```
   "$JAVA" $JAVA_OPTS \ -classpath "$WILDFLY_CLASSPATH" -Dreporthome=/opt/JReport/Server \ -Dlogall=true \ org.wildfly.Main "$@"
   ```
2. After editing standalone.sh, start WildFly using the modified file.
3. After reproducing the problem, send [support@jinfonet.com](mailto:support@jinfonet.com) the log files in `reporthome/logs`.

   The WildFly log files may also help to identify the problem. The most useful one is /opt/wildfly/server/default/log/server.log.

**Note:** If you encounter the issue that WildFly 17.0.1.Final cannot locate jrenv.jar when building a WAR/EAR to deploy to WildFly 17.0.1.Final, add -Djbossas7=true in makewar.bat/sh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691182-Deploying-to-Resin-4-0-62)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717481-Integrating-Remote-Logi-Report-Server)
