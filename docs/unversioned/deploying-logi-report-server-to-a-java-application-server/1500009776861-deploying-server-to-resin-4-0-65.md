---
title: "Deploying Server to Resin 4.0.65"
id: 1500009776861
section: "Deploying Logi Report Server to a Java Application Server"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776861-Deploying-Server-to-Resin-4-0-65
updated_at: 2021-07-24T00:48:03Z
---

# Deploying Server to Resin 4.0.65

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748422-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776901-Deploying-Server-to-WildFly-20-0-1)

# Deploying Server to Resin 4.0.65

This topic describes how you can deploy Logi Report Server to Resin.

In the example we use directory paths based on Unix. The instructions are applicable to both Unix and Windows installations. However, the format of the paths for Windows should use the Windows format, that is, `C:\LogiReport\Server` instead of `/opt/LogiReport/Server`.

Assume that:

* You installed Resin 4.0.65 in the `/opt/resin` directory.
* The Logi Report Server WAR file jreport.war is in the `/opt/LogiReport/Server/bin/distribute` directory. To create the WAR file, refer to the instructions in [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

**To deploy Logi Report Server to Resin 4.0.65:**

1. Generate the password.

   ![Generate Password](https://devnet.logianalytics.com/hc/article_attachments/4404885424663/integ_dply_rsn_pswd.gif)
2. Modify **resin.properties** in `/opt/resin/conf`. Set **remote\_admin\_enable** to **true** and add the generated password.

   ![Set Remote_admin_enable](https://devnet.logianalytics.com/hc/article_attachments/4404880310167/integ_dply_rsn_prp.gif)
3. Enable the commands that allow administrators and programmers to perform debugging and monitoring tasks on the remote Resin server using command line.

   By default, these commands are disabled. Enabling the command requires ManagerService be registered in resin.xml file. Since the default resin.xml already includes a <resin:AdminAuthenticator> with a <resin:import>, you can just reuse the admin configuration from the /resin-admin page.

   ![Enable Command](https://devnet.logianalytics.com/hc/article_attachments/4404880310423/integ_dply_rsn_cmnd.gif)
4. Start Resin 4.0.65 by running the **resin.sh** start script in `/opt/resin/bin.`
5. Log onto the Resin 4.0.65 Administration Console with the specified user name and password using the URL `http://localhost:8080/resin-admin/index.php`.
6. In the deploy tab, select **Browse** to select the file **jreport.war**. In the **Name** text box, type **jreport**. Then select **Deploy**.
7. Access Logi Report Server using the following URLs:

   `http://localhost:8080/jreport/jrserver
     
    http://localhost:8080/jreport/jinfonet/index.jsp`

## Troubleshooting

If you run into problems when using Logi Report Server in Resin, send the log files of Logi Report Server to [support@logianalytics.com](mailto:support@logianalytics.com). The following procedure illustrates how to generate the log files:

1. Modify the file **resin.sh** in `/opt/resin/bin` by adding **-Dlogall=true** after the reporthome definition:

   ```
   "$JAVA" $JAVA_OPTS \  
    
   -classpath "$RESIN_CLASSPATH" -Dreporthome=/opt/LogiReport/Server \   
   -Dlogall=true  \   
   org.resin.Main "$@"
   ```
2. Run the modified **resin.sh** to start Resin.
3. After reproducing the problem, send [support@logianalytics.com](mailto:support@logianalytics.com) the log files in `reporthome/logs`.

   The Resin log files may also help to identify the problem. The most useful one is /opt/Resin/server/default/log/server.log.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748422-Deploying-Server-to-GlassFish-Server-Open-Source-Edition-5-0)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776901-Deploying-Server-to-WildFly-20-0-1)
