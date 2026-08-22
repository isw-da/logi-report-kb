---
title: "Configuring Logi JReport Server Guide v15 Server"
id: 1500009644382
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644382-Configuring-Logi-JReport-Server-Guide-v15-Server
updated_at: 2021-07-24T20:55:23Z
---

# Configuring Logi JReport Server Guide v15 Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673321-Shutting-Down-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database)

# Configuring Logi JReport Server Guide v15

Once Logi JReport Server has been installed and you have prepared the reporting environment, you can then start it. However, you may find that Logi JReport's default port number conflicts with an existing one in your computer, or that you need to generate log files for analyzing a problem. Even more important, you need to change the server DBMS from the default Derby database that cannot be used in production environments. In these cases, you will need to configure your server. Before or while running the server, you can configure it according to your requirements. You can also carry out performance tuning to make Logi JReport Server efficient, reliable, and fast.

The configuration work can be performed in two ways: via the Logi JReport Server UI or via configuration files. Some server UI options and properties in the configuration files are mapped and both function the same way. For these types of settings, you can take either way to do the configuration.

The server.properties file in `<install_root>\bin` provides comprehensive configuration properties. You can also edit the file to suit your requirements. For details about the properties see [Appendix 2: Properties in server.properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009668861-Appendix-2-Properties-in-server-properties).

To perform administrative configuration work as an administrator via the Logi JReport Server UI, [log onto the Logi JReport Server administration console](https://devnet.logianalytics.com/hc/en-us/articles/1500009648602-Accessing-Logi-JReport-Server-Guide-v15-Server-via-a-Web-Browser#Admin).

The following topics discuss configuring the Logi JReport Server Guide v15 Server in further detail:

* [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database)
* [Configuring the Server Service](https://devnet.logianalytics.com/hc/en-us/articles/1500009669221-Configuring-the-Server-Service)
* [Configuring Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009644422-Configuring-Connections)
* [Configuring Connection Pool](https://devnet.logianalytics.com/hc/en-us/articles/1500009644562-Configuring-Connection-Pool)
* [Configuring Logs](https://devnet.logianalytics.com/hc/en-us/articles/1500009644542-Configuring-Logs)
* [Configuring Export Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009644522-Configuring-Export-Settings)
* [Configuring the E-Mail Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009669181-Configuring-the-E-Mail-Server)
* [Configuring Advanced Server Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009644402-Configuring-Advanced-Server-Settings)
* [Configuring Cache](https://devnet.logianalytics.com/hc/en-us/articles/1500009669021-Configuring-Cache)
* [Configuring Server Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile)
* [Updating the Server License](https://devnet.logianalytics.com/hc/en-us/articles/1500009669161-Updating-the-Server-License)
* [Changing the Server Context Path](https://devnet.logianalytics.com/hc/en-us/articles/1500009644442-Changing-the-Server-Context-Path)
* [Tuning Server Performance](https://devnet.logianalytics.com/hc/en-us/articles/1500009669201-Tuning-Server-Performance)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673321-Shutting-Down-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009669081-Configuring-the-Server-Database)
