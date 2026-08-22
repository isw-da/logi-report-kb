---
title: "Running the Catalog API Samples"
id: 28897716551565
section: "Working with APIs - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897716551565-Running-the-Catalog-API-Samples
updated_at: 2024-09-30T09:07:54Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Running the Catalog API Samples

The sample programs, TestCatalogAPI.java and TestCatalogBV.java in <install_root>\help\samples\APICatalog, show how you can use the Catalog API to create a catalog and to create business views in a catalog. This topic describes how you can compile and run the sample programs.

In order to compile and run the Catalog API samples, you should add the required classes to the class path (make sure that the path of JREngine.jar is before that of report.jar). 

For example, you can use the following command to compile and run the sample program TestCatalogAPI.java. After you run the program, it creates a new catalog file MyReports.cat in C:\LogiReport\Designer\Demo\MyReports. Be sure to create this empty directory first.

C:\LogiReport\Designer\help\samples\APICatalog>javac -classpath "C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\log4j-api-2.17.2.jar;C:\LogiReport\Designer\lib\log4j-core-2.17.2.jar;C:\LogiReport\Designer\lib\log4j-slf4j-impl-2.17.2.jar;C:\LogiReport\Designer\lib\slf4j-api-1.7.36.jar;C:\test\classes" TestCatalogAPI.java

C:\LogiReport\Designer\help\samples\APICatalog>java -classpath "C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\log4j-api-2.17.2.jar;C:\LogiReport\Designer\lib\log4j-core-2.17.2.jar;C:\LogiReport\Designer\lib\log4j-slf4j-impl-2.17.2.jar;C:\LogiReport\Designer\lib\slf4j-api-1.7.36.jar;C:\LogiReport\Designer\help;C:\test\classes" -Dreporthome=C:\LogiReport\Designer TestCatalogAPI -path=C:\LogiReport\Designer\Demo\MyReports -catalog=MyReports.cat -log=C:\LogiReport\Designer\logs\designer.log

 In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: Statement on Log4j and Log4Net Vulnerabilities.
    

Previous Topic  Next Topic
