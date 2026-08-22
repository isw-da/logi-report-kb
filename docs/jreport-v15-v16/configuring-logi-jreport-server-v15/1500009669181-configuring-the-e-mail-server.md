---
title: "Configuring the E-Mail Server"
id: 1500009669181
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669181-Configuring-the-E-Mail-Server
updated_at: 2021-07-24T20:55:20Z
---

# Configuring the E-Mail Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644522-Configuring-Export-Settings)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644402-Configuring-Advanced-Server-Settings)

# Configuring the E-Mail Server

In order to [publish report results to e-mail](https://devnet.logianalytics.com/hc/en-us/articles/1500009674761-Example-3-Publishing-a-Report-to-E-mail) and to notify the task status via e-mails when scheduling tasks to [run reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009649902-Scheduling-Tasks-to-Publish-Reports), [create in-memory cubes](https://devnet.logianalytics.com/hc/en-us/articles/1500009673441-Creating-In-memory-Cubes) or [create CRDs](https://devnet.logianalytics.com/hc/en-us/articles/1500009673421-Scheduling-Cached-Report-Data-Results), administrators need to configure an e-mail server for use in advance.

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar and then select **E-mail Server** from the drop-down menu to open the Configuration - E-mail Server page.

   ![Configure E-mail Server](https://devnet.logianalytics.com/hc/article_attachments/4404920651287/config_mail.gif)
2. In the SMTP Server text box, enter the numeric or named host of the machine where the e-mail server is located.
3. In the SMTP Server Port text box, enter the port where the e-mail server runs.
4. If the SMTP server requires authentication, check the **Server Requires Authentication** checkbox, then specify
   the user name and password for logging in to the SMTP server.
5. If the SMTP server does not need a secure connection, keep the option No Need Secure Connection checked as it is. If it requires a secure connection, check the **Server Requires a Secure Connection (SSL)** or **Server Requires a Secure Connection (TLS)** according to the SMTP server configuration.
6. In the E-mail Address text box, type in the address of the e-mail sender. You must specify an address and make sure that the format of the specified address is valid.
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644522-Configuring-Export-Settings)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644402-Configuring-Advanced-Server-Settings)
