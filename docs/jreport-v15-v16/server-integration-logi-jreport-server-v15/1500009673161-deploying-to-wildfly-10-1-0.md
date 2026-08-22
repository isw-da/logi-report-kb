---
title: "Deploying to WildFly 10.1.0"
id: 1500009673161
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673161-Deploying-to-WildFly-10-1-0
updated_at: 2021-07-24T20:54:10Z
---

# Deploying to WildFly 10.1.0

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648462-Deploying-to-Resin-4-0-53)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648482-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server)

# Deploying to WildFly 10.1.0

This topic introduces how to deploy Logi JReport Server Guide v15 Server to WildFly 10.1.0. The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\Logi JReport\Server` instead of `/opt/Logi JReport/Server`.

It is assumed that:

* WildFly 10.1.0 is installed in the `/opt/wildfly` directory.
* The Logi JReport Server WAR file Logi JReport.war is located in the `/opt/Logi JReport/Server/bin/distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server).

  **Note:** Before creating the WAR, you need to change JRPatternLayout to PatternLayout all over the LogConfig.properties file in `/opt/Logi JReport/Server/bin`.

**To deploy Logi JReport Server to WildFly 10.1.0:**

1. Start WildFly 10.1.0 by running the standalone.sh script in `/opt/wildfly/bin`.
2. By default WildFly 10.1.0 is now distributed with security enabled for the management interfaces, this means that before you connect using the administration console you need to add a new user, this can be achieved by using the `add-user.sh` script in the bin folder. You will then be prompted to set the user name and password for the new user.
3. Log onto the WildFly 10.1.0 Administration Console with the specified user name and password using the URL `http://localhost:9990/console`.
4. In the Deployments tab, select **Add**. In the Create Deployment dialog, browse to select the file Logi JReport.war. Then select **Next**.
5. In the step 2 of the Create Deployment dialog, check the **Enable** option and then select **Save**.
6. Upon the successful deployment of the Logi JReport Server WAR file Logi JReport.war, access Logi JReport Server using the following URLs:

   `http://localhost:8080/Logi JReport/jrserver  
    http://localhost:8080/Logi JReport/admin/index.jsp  
    http://localhost:8080/Logi JReport/jinfonet/index.jsp`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Troubleshooting

If you run into problems when using Logi JReport Server in WildFly, send the log files of Logi JReport Server to [support@jinfonet.com](mailto:support@jinfonet.com). The following procedure illustrates how to generate the log files:

1. Modify the file standalone.sh in `/opt/wildfly/bin`.

   In the file standalone.sh, add `-Dlogall=true` after the reporthome definition:

   |  |
   | --- |
   | ``` "$JAVA" $JAVA_OPTS \  -classpath "$WILDFLY_CLASSPATH" -Dreporthome=/opt/Logi JReport/Server \  -Dlogall=true  \  org.wildfly.Main "$@" ``` |
2. After editing standalone.sh, start WildFly using the modified file.
3. After reproducing the problem, send [support@jinfonet.com](mailto:support@jinfonet.com) the log files in `reporthome/logs`.

   The WildFly log files may also help to identify the problem. The most useful one is `/opt/wildfly/server/default/log/server.log.`

**Notes:**

* To resolve the issue that WildFly 10.1.0 cannot locate jrenv.jar, when building a WAR/EAR to deploy to WildFly 10.1.0, add *-Djbossas7=true* in makewar.bat/sh.
* After Logi JReport.war is generated, you need to create a file named *jboss-deployment-structure.xml* in the Logi JReport.war/META-INF directory. The file should contain the following contents:  

  `<?xml version="1.0" encoding="UTF-8"?>   
   <jboss-deployment-structure>   
   <deployment>   
   <exclusions>   
   <module name="org.apache.log4j" />   
   </exclusions>   
   </deployment>   
   </jboss-deployment-structure>`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648462-Deploying-to-Resin-4-0-53)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648482-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server)
