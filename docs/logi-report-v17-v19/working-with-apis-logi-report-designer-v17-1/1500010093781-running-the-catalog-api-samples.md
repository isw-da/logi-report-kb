---
title: "Running the Catalog API Samples"
id: 1500010093781
section: "Working with APIs - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010093781-Running-the-Catalog-API-Samples
updated_at: 2021-12-31T02:36:55Z
---

# Running the Catalog API Samples

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093761-Manipulating-Catalogs-with-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093801-Using-Design-API-to-Design-Reports)

# Running the Catalog API Samples

The sample programs, TestCatalogAPI.java and TestCatalogBV.java in `<install_root>\help\samples\APICatalog`, show how you can use the Catalog API to create a catalog and to create business views in a catalog. This topic describes how you can compile and run the sample programs.

In order to compile and run the Catalog API samples, you should add the required classes to the class path (make sure that the path of the file **JREngine.jar** is before that of the file **report.jar**).

For example, you can use the following command to compile and run the sample program TestCatalogAPI.java. After you run the program, it creates a new catalog file **MyReports.cat** in `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Demo\MyReports`. Be sure to create this empty directory first.

`C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help\samples\APICatalog>javac -classpath "C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\JREngine.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\sac-1.3.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\report.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\log4j-core-2.13.3.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\log4j-api-2.13.3.jar;C:\test\classes" TestCatalogAPI.java`

`C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help\samples\APICatalog>java -classpath "C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\jrengine.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\sac-1.3.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\report.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\log4j-core-2.13.3.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\log4j-api-2.13.3.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help;C:\test\classes" -Dreporthome=C:\(Undefined variable: Logi_Variables.LogiReport)\Designer TestCatalogAPI -path=C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Demo\MyReports -catalog=MyReports.cat -log=C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\logs\designer.log`

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093761-Manipulating-Catalogs-with-the-Catalog-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093801-Using-Design-API-to-Design-Reports)
