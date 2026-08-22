---
title: "Running the Catalog API Samples"
id: 4405661310231
section: "Working with APIs - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661310231-Running-the-Catalog-API-Samples
updated_at: 2022-01-27T20:38:23Z
---

# Running the Catalog API Samples

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661307927-Manipulating-Catalogs-with-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661311255-Using-Design-API-to-Design-Reports)

# Running the Catalog API Samples

The sample programs, TestCatalogAPI.java and TestCatalogBV.java in `<install_root>\help\samples\APICatalog`, show how you can use the Catalog API to create a catalog and to create business views in a catalog. This topic describes how you can compile and run the sample programs.

In order to compile and run the Catalog API samples, you should add the required classes to the class path (make sure that the path of the file **JREngine.jar** is before that of the file **report.jar**).

For example, you can use the following command to compile and run the sample program TestCatalogAPI.java. After you run the program, it creates a new catalog file **MyReports.cat** in `C:\LogiReport\Designer\Demo\MyReports`. Be sure to create this empty directory first.

`C:\LogiReport\Designer\help\samples\APICatalog>javac -classpath "C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\log4j-core-``2.17.1.jar``;C:\LogiReport\Designer\lib\log4j-api-``2.17.1.jar``;C:\test\classes" TestCatalogAPI.java`

`C:\LogiReport\Designer\help\samples\APICatalog>java -classpath "C:\LogiReport\Designer\lib\jrengine.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\log4j-core-``2.17.1.jar``;C:\LogiReport\Designer\lib\log4j-api-``2.17.1.jar``;C:\LogiReport\Designer\help;C:\test\classes" -Dreporthome=C:\LogiReport\Designer TestCatalogAPI -path=C:\LogiReport\Designer\Demo\MyReports -catalog=MyReports.cat -log=C:\LogiReport\Designer\logs\designer.log`

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420542088087/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661307927-Manipulating-Catalogs-with-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661311255-Using-Design-API-to-Design-Reports)
