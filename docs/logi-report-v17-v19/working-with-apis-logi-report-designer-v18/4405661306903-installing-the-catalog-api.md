---
title: "Installing the Catalog API"
id: 4405661306903
section: "Working with APIs - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661306903-Installing-the-Catalog-API
updated_at: 2022-10-14T07:20:37Z
---

# Installing the Catalog API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661305623-Using-Catalog-API-to-Manipulate-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661309079-Making-Preparations-Before-Using-the-Catalog-API)

# Installing the Catalog API

This topic describes how you can install the Catalog API.

When you install Designer, you install the Catalog API at the same time. After installation, you have the following components in `<install_root>\lib`:

* report.jar
* JREngine.jar
* log4j-core-2.17.1.jar and log4j-api-2.17.1.jar (for the Logi Report logging system)
* sac-1.3.jar (for installing the Catalog API with the Design API)
* ...

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

You can get the Catalog API class in the archive file report.jar. You need to take the following steps before you can compile and run the program.

1. Set the class path environment variable. Append the following string to your class path that starts the Catalog API (make sure that the path of **JREngine.jar** is before that of **report.jar**):

   `<install_root>\lib\JREngine.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\report.jar;<install_root>\lib\log4j-core-``2.17.1.jar``;<install_root>\lib\log4j-api-``2.17.1.jar`
2. In your Java program, you must set the licensed user and Design API license key.

   `DesignerUserInfo userInfo=new DesignerUserInfo("UID","Design API Key");`
3. Set the reporthome parameter equal to the root path of Designer. You can set this in your environment or with the *-Dreporthome* argument to your JVM.

Logi Report Server also includes the Catalog API. If you prefer to use the libraries from Server, include the jar file *<server\_install\_root>\lib\JRESServlets.jar* in your class path instead of report.jar. You then need to use the Server Design API license key rather than the Design API license key.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661305623-Using-Catalog-API-to-Manipulate-Catalogs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661309079-Making-Preparations-Before-Using-the-Catalog-API)
