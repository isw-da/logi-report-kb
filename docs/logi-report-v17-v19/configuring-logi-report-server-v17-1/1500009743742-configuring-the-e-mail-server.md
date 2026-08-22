---
title: "Configuring the E-mail Server"
id: 1500009743742
section: "Configuring Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009743742-Configuring-the-E-mail-Server
updated_at: 2021-07-24T00:49:27Z
---

# Configuring the E-mail Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743702-Configuring-Export-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771481-Configuring-Advanced-Server-Settings)

# Configuring the E-mail Server

In order for users to [publish report results to e-mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009778441-Examples-of-Scheduling-Reports#Mail) and to notify the task status via e-mails when scheduling tasks to [run reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009778421-Scheduling-Tasks-to-Run-Reports), [create in-memory cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009777121-Managing-In-Memory-Cubes#Create), or [create CRDs](https://devnet.logianalytics.com/hc/en-us/articles/1500009777101-Managing-Cached-Report-Data#Schedule), administrators need to configure an e-mail server in advance. This topic describes how you can configure an e-mail server in the Server Console.

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Configuration** > **E-mail Server** from the drop-down menu. Server displays the E-mail Server page.

   ![E-mail Server page](https://devnet.logianalytics.com/hc/article_attachments/4404880564503/config_mail.gif)
2. In the **SMTP Server** text box, type the numeric or named host of the machine where the e-mail server is located.
3. In the **SMTP Server Port** text box, type the port where the e-mail server runs.
4. If the SMTP server requires authentication, select the **Server Requires Authentication** check box, then specify
   the user name and password for logging into the SMTP server.
5. If the SMTP server does not need a secure connection, keep the option **No Need Secure Connection** selected. If it requires a secure connection, select **Server Requires a Secure Connection (SSL)** or ![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")**Server Requires a Secure Connection (STARTTLS)** according to the SMTP server configuration.
6. In the **E-mail Address** text box, type the address of the e-mail sender. Make sure that the format of the specified address is valid.
7. From the **Encoding** drop-down list, select the encoding for the titles and comments of the e-mails.
8. Select **Save** to apply the settings.

Logi Report Server saves the e-mail server settings in the file **mailconfig.properties** in the `<install_root>\bin` directory. You can also use the file for default e-mail server configuration. The following table lists the available properties and the UI options they are mapped to.

| Property in mailconfig.properties | Mapped UI Option |
| --- | --- |
| smtp.server | SMTP Server |
| smtp.server.port | SMTP Server Port |
| smtp.authentication | Server Requires Authentication |
| smtp.SSL | Server Requires a Secure Connection (SSL) |
| smtp.TLS | Marks content and feature updates for Logi Report v17.1. New feature new content.Server Requires a Secure Connection (STARTTLS) |
| mailbox | E-mail Address |
| mail.encoding | Encoding |
| smtp.user | SMTP Login Account > User Name |
| smtp.password | SMTP Login Account > Password |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743702-Configuring-Export-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771481-Configuring-Advanced-Server-Settings)
