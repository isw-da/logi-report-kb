---
title: "Configuring the E-mail Server"
id: 1500009744921
section: "Configure Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744921-Configuring-the-E-mail-Server
updated_at: 2021-07-25T07:20:15Z
---

# Configuring the E-mail Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744881-Configuring-Export-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744721-Configuring-Advanced-Server-Settings)

# Configuring the E-mail Server

In order to [publish report results to e-mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009724282-Examples-of-Scheduling-Reports#Mail) and to notify the task status via e-mails when scheduling tasks to [run reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009724262-Scheduling-Tasks-to-Run-Reports), [create in-memory cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009750021-Managing-In-memory-Cubes#Create) or [create CRDs](https://devnet.logianalytics.com/hc/en-us/articles/1500009750001-Managing-Cached-Report-Data#Schedule), administrators need to configure an e-mail server for use in advance.

1. In the Logi Report Server console, point to **Administration** on the system toolbar, and then select **Configuration** > **E-mail Server** from the drop-down menu to open the E-mail Server page.

   ![E-mail Server](https://devnet.logianalytics.com/hc/article_attachments/4404936957335/config_mail.gif)
2. In the SMTP Server text box, type the numeric or named host of the machine where the e-mail server is located.
3. In the SMTP Server Port text box, type the port where the e-mail server runs.
4. If the SMTP server requires authentication, select the **Server Requires Authentication** check box, then specify
   the user name and password for logging in to the SMTP server.
5. If the SMTP server does not need a secure connection, keep the option No Need Secure Connection selected as it is. If it requires a secure connection, select **Server Requires a Secure Connection (SSL)** or **Server Requires a Secure Connection (TLS)** according to the SMTP server configuration.
6. In the E-mail Address text box, type the address of the e-mail sender. You must specify an address and make sure that the format of the specified address is valid.
7. From the Encoding drop-down list, select the encoding for the titles and comments of the e-mails.
8. Select **Save** to apply the settings.

The e-mail server settings are saved in the file mailconfig.properties in the `<install_root>\bin` directory. You can also use the file for default e-mail server configuration. The following table lists the available properties and the UI options they are mapped to.

| Property in mailconfig.properties | Mapped UI Option |
| --- | --- |
| smtp.server | SMTP Server |
| smtp.server.port | SMTP Server Port |
| smtp.authentication | Server Requires Authentication |
| smtp.SSL | Server Requires a Secure Connection (SSL) |
| smtp.TLS | Server Requires a Secure Connection (TLS) |
| mailbox | E-mail Address |
| mail.encoding | Encoding |
| smtp.user | SMTP Login Account > User Name |
| smtp.password | SMTP Login Account > Password |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744881-Configuring-Export-Settings)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744721-Configuring-Advanced-Server-Settings)
