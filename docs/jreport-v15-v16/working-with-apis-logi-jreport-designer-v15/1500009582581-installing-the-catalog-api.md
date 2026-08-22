---
title: "Installing the Catalog API"
id: 1500009582581
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582581-Installing-the-Catalog-API
updated_at: 2022-10-14T07:44:25Z
---

# Installing the Catalog API

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582561-Logi-JReport-Catalog-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562182-Using-the-Catalog-API)

# Installing the Catalog API

When you install Logi JReport Designer, the Catalog API is also installed at the same time. After installation, you will have the following components in `<install_root>\lib`:

* report.jar
* JREngine.jar
* log4j-core-2.7.jar and log4j-api-2.7.jar (for Logi JReport logging system)
* sac-1.3.jar (for installing Catalog API with Design API product)
* ...

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4411773980183/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

The Catalog API class is stored in the archive file report.jar. You will need to do the two steps below before you can compile and run the program:

1. Set the class path environment variable. Append the following string to your class path that starts the Catalog API (make sure that the path of JREngine.jar is before that of report.jar):

   `<install_root>\lib\JREngine.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\report.jar;<install_root>\lib\log4j-core-2.7.jar;<install_root>\lib\log4j-api-2.7.jar`
2. In your Java program you must set the licensed user and Design API license key.

   `DesignerUserInfo userInfo=new DesignerUserInfo("UID","Design API Key");`
3. Set the reporthome parameter equal to the root path of Logi JReport Designer. You can set this in your environment or with the -Dreporthome argument to your JVM.

Logi JReport Server also includes the Catalog API. If you prefer to use the libraries from Logi JReport Server, include the jar file *<server\_install\_root>\lib\JRESServlets.jar* in your class path instead of report.jar. You would then need to use the Server Design API license key rather than the Design API license key.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009582561-Logi-JReport-Catalog-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562182-Using-the-Catalog-API)
