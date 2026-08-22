---
title: "Configuring Server"
id: 1500009686622
section: "Configuring Server Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686622-Configuring-Server
updated_at: 2021-11-03T06:58:43Z
---

# Configuring Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717661-Shutting-Down-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686662-Configuring-the-Server-Database)

# Configuring Server Logi JReport Server v16

Once Logi JReport Server has been installed and you have prepared the reporting environment, you can then start it. However, you may find that Logi JReport's default port number conflicts with an existing one in your computer, or that you need to generate log files for analyzing a problem. Even more important, you need to change the server DBMS from the default Derby database that cannot be used in production environment. In these cases, you will need to configure your server. Before or while running the server, you can configure it according to your requirements. You can also carry out performance tuning to make Logi JReport Server efficient, reliable, and fast.

The configuration work can be performed in two ways: via the Logi JReport Server UI or via configuration files. Some server UI options and properties in the configuration files are mapped and both function the same way. For these types of settings, you can take either way to do the configuration.

The server.properties file in `<install_root>\bin` provides comprehensive configuration properties. You can also edit the file to suit your requirements. For details about the properties see [Appendix 2: Properties in server.properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009712261-Appendix-2-Properties-in-server-properties).

The following topics provide more information on configuration:

* [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009686662-Configuring-the-Server-Database)
* [Configuring the Server Service](https://devnet.logianalytics.com/hc/en-us/articles/1500009686842-Configuring-the-Server-Service)
* [Configuring Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009712401-Configuring-Connections)
* [Configuring Connection Pool](https://devnet.logianalytics.com/hc/en-us/articles/1500009712521-Configuring-Connection-Pool)
* [Configuring Logs](https://devnet.logianalytics.com/hc/en-us/articles/1500009712501-Configuring-Logs)
* [Configuring Export Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009686762-Configuring-Export-Settings)
* [Configuring the E-mail Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009686782-Configuring-the-E-mail-Server)
* [Configuring Advanced Server Settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009712361-Configuring-Advanced-Server-Settings)
* [Configuring Cache](https://devnet.logianalytics.com/hc/en-us/articles/1500009712381-Configuring-Cache)
* [Configuring Server Profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009686822-Configuring-Server-Profile)
* [Updating the Server License](https://devnet.logianalytics.com/hc/en-us/articles/1500009712481-Updating-the-Server-License)
* [Changing the Server Context Path](https://devnet.logianalytics.com/hc/en-us/articles/1500009686642-Changing-the-Server-Context-Path)
* [Tuning Server Performance](https://devnet.logianalytics.com/hc/en-us/articles/1500009686802-Tuning-Server-Performance)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717661-Shutting-Down-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686662-Configuring-the-Server-Database)
