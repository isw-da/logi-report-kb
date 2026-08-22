---
title: "Deploying Server to WildFly"
id: 5741437708951
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741437708951-Deploying-Server-to-WildFly
updated_at: 2022-10-31T17:17:58Z
---

# Deploying Server to WildFly

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741452764823-Deploying-Server-to-Resin)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741473756311-Integrating-Remote-Logi-Report-Server)

# Deploying Server to WildFly 26.1.2

This topic describes how you can deploy Logi Report Server to WildFly 26.1.2

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed WildFly 26.1.2 in the `/opt/wildfly` directory.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` folder. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/5741473837719-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif) Before creating the WAR, you need to change **JRPatternLayout** to **PatternLayout** all over the **LogConfig.properties** file in `/opt/LogiReport/Server/bin`. After you generate **jreport.war**, create a file named **jboss-deployment-structure.xml** in the jreport.war/META-INF folder with the contents:

  ```
  <?xml version="1.0" encoding="UTF-8"?>  
      <jboss-deployment-structure>   
          <deployment>   
              <exclusions>  
                  <module name="org.apache.logging.log4j.api"/>  
               <module name="org.slf4j" />  
                  <module name="org.slf4j.impl" />  
              </exclusions>  
          </deployment>  
      </jboss-deployment-structure>
  ```

**To deploy Logi Report Server to WildFly 26.1.2:**

1. Start WildFly by running the **standalone.sh** script in `/opt/wildfly/bin`.
2. By default, WildFly is distributed with security enabled for the management interface. It means that before you access the Administration Console you need to add a new user. You can achieve this using the `add-user.sh` script in the **bin** folder. Set the username and password for the new user.
3. Sign in to the WildFly Administration Console with the specified username and password using the URL `http://localhost:9990/console`.
4. In the **Deployments** tab, select **Add**.
5. In the Create Deployment dialog box, browse to select the **jreport.war** file.
6. Select **Next**.
7. In the step 2 of the Create Deployment dialog box, select **Enable**.
8. Select **Save**.
9. Upon the successful deployment of the Logi Report Server WAR file **jreport.war**, access Logi Report Server using the following URL:

   `http://localhost:8080/jreport/jrserver
     
   http://localhost:8080/jreport/jinfonet/index.jsp`

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif) If you are launching a WildFly instance on SE 17 and aren't using a bootable jar or WildFly launch scripts, you need to add all the content in **java.option** in `/opt/LogiReport/Server/bin` into the **standalone.conf** file in `/opt/wildfly/bin` as follows. For each line in java.option, add it into standalone.conf using this format: `JAVA_OPTS="$JAVA_OPTS Each_Line_Content"`, for example, `JAVA_OPTS="$JAVA_OPTS --illegal-access=permit"`.

![WildFly ](https://devnet.logianalytics.com/hc/article_attachments/9905677248663/integ_dply_wldfly.gif)

## Troubleshooting

If you run into problems when using Logi Report Server in WildFly, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Modify the **standalone.sh** file in `/opt/wildfly/bin`, by adding **-Dlogall=true** after the reporthome definition:

   ```
   "$JAVA" $JAVA_OPTS \ -classpath "$WILDFLY_CLASSPATH" -Dreporthome=/opt/LogiReport/Server \ -Dlogall=true \ org.wildfly.Main "$@"
   ```
2. Start WildFly using the modified **standalone.sh**.
3. After reproducing the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs`.

   The WildFly log files may also help identify the problem. The most useful one is /opt/wildfly/server/default/log/server.log.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) If you encounter the problem that WildFly cannot locate **jrenv.jar** when you are deploying a WAR/EAR to WildFly, add **-Djbossas7=true** in makewar.bat/sh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741452764823-Deploying-Server-to-Resin)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741473756311-Integrating-Remote-Logi-Report-Server)
