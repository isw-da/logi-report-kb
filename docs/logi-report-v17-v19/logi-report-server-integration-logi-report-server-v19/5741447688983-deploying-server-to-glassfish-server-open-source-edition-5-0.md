---
title: "Deploying Server to GlassFish Server Open Source Edition 5.0"
id: 5741447688983
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741447688983-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0
updated_at: 2022-10-31T17:17:56Z
---

# Deploying Server to GlassFish Server Open Source Edition 5.0

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741467690263-Deploying-Server-to-Jetty)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741452764823-Deploying-Server-to-Resin)

# Deploying Server to GlassFish Server Open Source Edition 5.0

This topic describes how you can deploy Logi Report Server to GlassFish.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that the Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/5741473837719-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi Report Server to GlassFish Server Open Source Edition 5.0:**

1. Start GlassFish in the default **domain1** and launch the Admin Console.
2. Select the **Applications** node on the left.
3. Select **Deploy** on the displayed page.
4. Select **Choose File** to select the WAR file **jreport.war**.
5. Leave Application Name and Context Root as jreport and jreport. Then select **OK**.
6. Expand the **Deployment** node on the left and you see a new node named **jreport**. Select it and then on the displayed page select **Save**.
7. In the console tree, select **Configuration**.
8. Go to the **JVM Settings** tab and select **JVM Options**.
9. In the JVM Options section, select **Add JVM Option**, and then type **-Djava.awt.headless=true**. Select **Save** to save your changes.

   You need not add this JVM option if you are using Windows.
10. Restart GlassFish and start the application **jreport**.
11. Access Logi Report Server using the following URLs:

    `http://<hostname>:8080/jreport  
     http://<hostname>:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using GlassFish, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Start GlassFish in the default domain1 and then launch the Admin Console.
2. In the console tree, select **Configuration**.
3. Go to the JVM Settings tab, and then select **JVM Options**.
4. In the JVM Options section, select **Add JVM Option**, and then type **-Dlogall=true**. Select **Save** to save your changes.
5. Restart GlassFish and try to reproduce the problem.
6. After reproducing the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs`.

   The GlassFish log file may also help to identify the problem. It is /opt/glassfish/domains/domain1/logs/server.log.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741467690263-Deploying-Server-to-Jetty)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741452764823-Deploying-Server-to-Resin)
