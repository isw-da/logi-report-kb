---
title: "Deploying Server to Resin"
id: 4405690627735
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690627735-Deploying-Server-to-Resin
updated_at: 2022-01-27T07:59:34Z
---

# Deploying Server to Resin

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690626583-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683912471-Deploying-Server-to-WildFly)

# Deploying Server to Resin 4.0.66

This topic describes how you can deploy Logi Report Server to Resin 4.0.66.

We use paths based on UNIX path name protocol in our example. The instruction applies to both UNIX and Windows installation. However, the path formats differ. For Windows it is in this format `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed Resin 4.0.66 in the `/opt/resin` directory.
* The Logi Report Server WAR file jreport.war is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, see [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi Report Server to Resin 4.0.66:**

1. Generate the password.

   ![Generate Password](https://devnet.logianalytics.com/hc/article_attachments/4420461604503/integ_dply_rsn_pswd.gif)
2. Modify **resin.properties** in `/opt/resin/conf`. Set **remote\_admin\_enable** to **true** and add the generated password.

   ![Set Remote_admin_enable](https://devnet.logianalytics.com/hc/article_attachments/4420453531159/integ_dply_rsn_prp.gif)
3. Enable the commands that allow administrators and programmers to perform debugging and monitoring tasks on the remote Resin server using command line.

   By default, these commands are disabled. To enable them, register ManagerService in the resin.xml file. Since the default resin.xml already includes a <resin:AdminAuthenticator> with a <resin:import>, you can just reuse the admin configuration from the /resin-admin page.

   ![Enable Command](https://devnet.logianalytics.com/hc/article_attachments/4420461605015/integ_dply_rsn_cmnd.gif)
4. Start Resin by running the **resin.sh** start script in `/opt/resin/bin.`
5. Sign in to the Resin Administration Console with the specified username and password using the URL `http://localhost:8080/resin-admin/index.php`.
6. In the deploy tab, select **Browse** to select the file **jreport.war**.
7. In the **Name** text box, type **jreport**.
8. Select **Deploy**.
9. Access Logi Report Server using the following URLs:

   `http://localhost:8080/jreport/jrserver
     
    http://localhost:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in Resin, you may have to send the log files of Logi Report Server to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.). The following procedure illustrates how to generate the log files:

1. Modify the file **resin.sh** in `/opt/resin/bin` by adding **-Dlogall=true** after the reporthome definition:

   ```
   "$JAVA" $JAVA_OPTS \  
    
   -classpath "$RESIN_CLASSPATH" -Dreporthome=/opt/LogiReport/Server \   
   -Dlogall=true  \   
   org.resin.Main "$@"
   ```
2. Run the modified **resin.sh** to start Resin.
3. After reproducing the problem, send the log files in `reporthome/logs` to [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.).

   The Resin log files may also help identify the problem. The most useful one is /opt/Resin/server/default/log/server.log.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690626583-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683912471-Deploying-Server-to-WildFly)
