---
title: "Shutting Down Logi Report Server"
id: 5741468149783
section: "Starting, Accessing, and Shutting Down Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741468149783-Shutting-Down-Logi-Report-Server
updated_at: 2022-10-31T17:18:02Z
---

# Shutting Down Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741461387031-Accessing-Logi-Report-Server-via-a-Web-Browser)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741448163607-Using-and-Upgrading-Logi-Report-Server-on-Docker)

# Shutting Down Logi Report Server

This topic describes how you can shut down Logi Report Server under different circumstances.

**To shut down Logi Report Server normally:**

* In a standalone environment, select **Stop Server** in the Logi Report folder on the Start menu; or select the Gear icon ![Shut Down the Server button](https://devnet.logianalytics.com/hc/article_attachments/9905715393943/btn_srv_shtdwn.gif) at the upper right of the Server Console and select **Shut Down Server** from the drop-down menu.
* In an integrated environment, shut down the application server according to the vendor's instructions.

Also, Logi Report provides a feature for handling an abnormal system exit that enables the program to close itself gracefully when the Java virtual machine (JVM) is terminated in response to a user interrupt, such as typing ^C, or a system-wide event such as a user signs out or the system shuts down.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741461387031-Accessing-Logi-Report-Server-via-a-Web-Browser)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741448163607-Using-and-Upgrading-Logi-Report-Server-on-Docker)
