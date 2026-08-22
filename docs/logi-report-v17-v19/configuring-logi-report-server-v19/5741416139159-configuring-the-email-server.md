---
title: "Configuring the Email Server"
id: 5741416139159
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741416139159-Configuring-the-Email-Server
updated_at: 2022-10-31T17:16:02Z
---

# Configuring the Email Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741416077591-Configuring-Export-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741401055383-Configuring-Advanced-Server-Settings)

# Configuring the Email Server

In order for users to [publish reports to email](https://devnet.logianalytics.com/hc/en-us/articles/5741483494551-Examples-of-Scheduling-Reports#Mail) and to notify the task status via email when scheduling tasks to [run reports](https://devnet.logianalytics.com/hc/en-us/articles/5741483471255-Scheduling-Tasks-to-Run-Reports), [create in-memory cubes](https://devnet.logianalytics.com/hc/en-us/articles/5741437977495-Managing-In-Memory-Cubes#Create), or [create CRDs](https://devnet.logianalytics.com/hc/en-us/articles/5741453292183-Managing-Cached-Report-Data#Schedule), administrators need to configure an email server in advance. This topic describes how you can configure an email server on the Server Console.

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **E-mail Server**. Server displays the E-mail Server page.

   ![E-mail Server page](https://devnet.logianalytics.com/hc/article_attachments/9905779805463/config_mail.gif)
2. In the **SMTP Server** text box, type the numeric or named host of the machine where the email server is.
3. In the **SMTP Server Port** text box, type the port where the email server runs.
4. If the SMTP server requires authentication, select **Server Requires Authentication**, then specify
   the username and password for signing in to the SMTP server.
5. If the SMTP server requires a secure connection, select **Server Requires a Secure Connection (SSL)** or **Server Requires a Secure Connection (STARTTLS)** according to the SMTP server configuration.
6. In the **E-mail Address** text box, type the address of the email sender. Make sure that the format of the specified address is valid.
7. From the **Encoding** list, select the encoding for the titles and comments of the email.
8. Select **Save** to apply the settings.

Server saves the email server settings in the **mailconfig.properties** file in the `<install_root>\bin` directory. You can also use the property file for default email server configuration. The following table lists the available properties in the property file and the UI options they map to.

| Property in mailconfig.properties | Mapped UI Option |
| --- | --- |
| smtp.server | SMTP Server |
| smtp.server.port | SMTP Server Port |
| smtp.authentication | Server Requires Authentication |
| smtp.SSL | Server Requires a Secure Connection (SSL) |
| smtp.TLS | Server Requires a Secure Connection (STARTTLS) |
| mailbox | E-mail Address |
| mail.encoding | Encoding |
| smtp.user | SMTP Login Account > User Name |
| smtp.npassword | SMTP Login Account > Password |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741416077591-Configuring-Export-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741401055383-Configuring-Advanced-Server-Settings)
