---
title: "Deploying Server to WildFly"
id: 4405683912471
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683912471-Deploying-Server-to-WildFly
updated_at: 2022-01-27T07:59:35Z
---

# Deploying Server to WildFly

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690627735-Deploying-Server-to-Resin-4-0-65)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683913495-Integrating-Remote-Logi-Report-Server)

# Deploying Server to WildFly 26.0.0

This topic describes how you can deploy Logi Report Server to WildFly 26.0.0.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed WildFly 26.0.0 in the `/opt/wildfly` directory.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

  ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif) Before creating the WAR, you need to change **JRPatternLayout** to **PatternLayout** all over the **LogConfig.properties** file in `/opt/LogiReport/Server/bin`. After you generate **jreport.war**, create a file named **jboss-deployment-structure.xml** in the jreport.war/META-INFO folder with the contents:

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

**To deploy Logi Report Server to WildFly 26.0.0:**

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

## Troubleshooting

If you run into problems when using Logi Report Server in WildFly, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Modify the **standalone.sh** file in `/opt/wildfly/bin`, by adding **-Dlogall=true** after the reporthome definition:

   ```
   "$JAVA" $JAVA_OPTS \ -classpath "$WILDFLY_CLASSPATH" -Dreporthome=/opt/LogiReport/Server \ -Dlogall=true \ org.wildfly.Main "$@"
   ```
2. Start WildFly using the modified **standalone.sh**.
3. After reproducing the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs`.

   The WildFly log files may also help identify the problem. The most useful one is /opt/wildfly/server/default/log/server.log.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) If you encounter the problem that WildFly cannot locate **jrenv.jar** when you are deploying a WAR/EAR to WildFly, add **-Djbossas7=true** in makewar.bat/sh.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690627735-Deploying-Server-to-Resin-4-0-65)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683913495-Integrating-Remote-Logi-Report-Server)
