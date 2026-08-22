---
title: "Deploying Server to WebLogic 14.1.1"
id: 4405690630551
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690630551-Deploying-Server-to-WebLogic-14-1-1
updated_at: 2022-01-27T07:59:35Z
---

# Deploying Server to WebLogic 14.1.1

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690631447-Deploying-Server-to-IBM-WebSphere-9-0-5-6)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690629655-Deploying-Server-to-Tomcat)

# Deploying Server to WebLogic 14.1.1

This topic describes how you can deploy Logi Report Server to WebLogic.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed WebLogic 14.1.1 in the `/opt/bea` directory. This is BEA\_HOME in the WebLogic documentation.
* The Logi Report Server WAR file **jreport.war** is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi Report Server to BEA WebLogic:**

1. If you have not already created a WebLogic Domain for Logi Report Server, you must create one before starting the integration.
2. Start WebLogic by running **startWeblogic.sh** in `/opt/bea/user_projects/domains/domain_name/bin`.
3. Access the WebLogic Administrative Console using the URL `http://hostname:7001/console/`, where **hostname** is host name or IP address, and 7001 is the port number.
4. After you sign in, in the Domain Structure panel on the left, select **Deployments** node.
5. In the Summary of Deployments panel, select **Install**.
6. In the Install Application Assistant panel, select **upload your file(s)**.
7. In the Deployment Archive section, select **Browse** to select the **jreport.war** file in `C:\LogiReport\Server\bin\distribute`, and then select **Next**.
8. Keep selecting **Next** until the **Finish** button is enabled, and then select **Finish**.
9. Start Logi Report Server and then access it using the following URL:

   `http://localhost:7001/jreport/`

## Troubleshooting

If you run into problems when using Logi Report Server in BEA WebLogic, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Add **`-Dlogall=true`** on the same line as **-Dreporthome** in the `startWebLogic.sh` shell script.
2. Restart the application server
3. Try to reproduce the problem. After reproducing the problem, send [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.) the log files in `reporthome/logs`.

   The WebLogic log file may also help to identify the problem. It is /opt/bea/user\_projects/domains/domain\_name/logs.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690631447-Deploying-Server-to-IBM-WebSphere-9-0-5-6)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690629655-Deploying-Server-to-Tomcat)
