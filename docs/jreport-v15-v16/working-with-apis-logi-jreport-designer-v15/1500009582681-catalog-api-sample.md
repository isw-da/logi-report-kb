---
title: "Catalog API Sample"
id: 1500009582681
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582681-Catalog-API-Sample
updated_at: 2021-12-31T02:44:40Z
---

# Catalog API Sample

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562282-Saving-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562342-Logi-JReport-Design-API)

# Catalog API Sample

This topic provides a sample program that demonstrates how to use the Catalog API to create or modify a catalog - TestCatalogAPI.java that is located in `<install_root>\help\samples\APICatalog`.

To compile and run the demo program, you should add the required classes to the class path (make sure that the path of the file JREngine.jar is before that of the file report.jar).

After running the program, a new catalog file MyReports.cat will be created in `C:\Logi JReport\Designer\Demo\MyReports`. Be sure to create this empty directory first.

`C:\Logi JReport\Designer\help\samples\APICatalog>javac -classpath "C:\Logi JReport\Designer\lib\JREngine.jar;C:\Logi JReport\Designer\lib\sac-1.3.jar;C:\Logi JReport\Designer\lib\report.jar;C:\Logi JReport\Designer\lib\log4j-core-2.7.jar;C:\Logi JReport\Designer\lib\log4j-api-2.7.jar;C:\test\classes" TestCatalogAPI.java`

`C:\Logi JReport\Designer\help\samples\APICatalog>java -classpath "C:\Logi JReport\Designer\lib\jrengine.jar;C:\Logi JReport\Designer\lib\sac-1.3.jar;C:\Logi JReport\Designer\lib\report.jar;C:\Logi JReport\Designer\lib\log4j-core-2.7.jar;C:\Logi JReport\Designer\lib\log4j-api-2.7.jar;C:\Logi JReport\Designer\help;C:\test\classes" -Dreporthome=C:\Logi JReport\Designer TestCatalogAPI -path=C:\Logi JReport\Designer\Demo\MyReports -catalog=MyReports.cat -log=C:\Logi JReport\Designer\logs\designer.log`

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4411773980183/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562282-Saving-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562342-Logi-JReport-Design-API)
