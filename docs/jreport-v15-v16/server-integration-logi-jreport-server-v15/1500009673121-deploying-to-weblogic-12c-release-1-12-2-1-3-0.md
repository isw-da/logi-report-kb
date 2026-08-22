---
title: "Deploying to WebLogic 12c Release 1 (12.2.1.3.0)"
id: 1500009673121
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673121-Deploying-to-WebLogic-12c-Release-1-12-2-1-3-0
updated_at: 2021-07-24T20:54:10Z
---

# Deploying to WebLogic 12c Release 1 (12.2.1.3.0)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673141-Deploying-to-IBM-WebSphere-9-0-0-4)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673101-Deploying-to-Tomcat-8-5-23)

# Deploying to WebLogic 12c Release 1 (12.2.1.3.0)

This topic introduces how to deploy Logi JReport Server Guide v15 Server to WebLogic 12c Release 1 (12.2.1.3.0). The example directory paths listed below are based on Unix. The instructions are applicable to both Unix and Windows installations; however, the format of the paths for Windows would use the Windows format, that is, `C:\Logi JReport\Server` instead of `/opt/Logi JReport/Server`.

It is assumed that:

* WebLogic 12c Release 1 (12.2.1.3.0) is installed in the `/opt/bea` directory. This is referred to as BEA\_HOME in the WebLogic documentation.
* The Logi JReport Server WAR file Logi JReport.war is located in the `/opt/Logi JReport/Server/bin/distribute` directory. To create the WAR file refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server).

**To deploy Logi JReport Server to BEA WebLogic:**

1. If you have not already created a WebLogic Domain for Logi JReport Server you must create one before starting the integration.
2. Start WebLogic by running startWeblogic.sh in `/opt/bea/user_projects/domains/domain_name/bin`.
3. Access the WebLogic Administrative Console by using URL `http://hostname:7001/console/`, where the hostname is host name or IP address, and 7001 is the port number.
4. After your successful login, in the Domain Structure panel on the left, select **Deployments** node.
5. In the Summary of Deployments panel, select **Install**.
6. In the Install Application Assistant panel, select the **upload your file(s)** link.
7. In the Deployment Archive section, select **Browse** to select the **Logi JReport.war** file in `C:\Logi JReport\Server\bin\distribute`, and then select **Next**.
8. Keep selecting **Next** until the Finish button is enabled, and then select **Finish**.
9. Start Logi JReport Server and then access it using the following URL:

   `http://localhost:7001/Logi JReport/`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Troubleshooting

If you run into problems when using Logi JReport Server in BEA WebLogic, send the log files of Logi JReport Server to [support@jinfonet.com](mailto:support@jinfonet.com). The following procedure illustrates how to generate the log files:

1. Add **`-Dlogall=true`** on the same line as -Dreporthome in the `startWebLogic.sh` shell script.
2. Restart the application server, and then try to reproduce the problem. After reproducing the problem, send [support@jinfonet.com](mailto:support@jinfonet.com) the log files in `reporthome/logs`.

   The WebLogic log file may also help to identify the problem. It is `/opt/bea/user_projects/domains/domain_name/logs`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673141-Deploying-to-IBM-WebSphere-9-0-0-4)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673101-Deploying-to-Tomcat-8-5-23)
