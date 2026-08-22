---
title: "Running the Design API Samples"
id: 5735498221463
section: "Working with APIs - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735498221463-Running-the-Design-API-Samples
updated_at: 2022-11-02T08:17:10Z
---

# Running the Design API Samples

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511592855-Designing-Reports-with-the-Design-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563519639-Using-the-Exit-Functions)

# Running the Design API Samples

This topic introduces the Design API sample programs Logi Report provides and how you can run them to create and edit reports.

After you install the Design API by Designer or Server, you can get the following Design API sample programs in `<insatll_root>\help\samples\APIDesign`:

* **CreateLCSample.java**  
  An example of creating a library component with a table, a crosstab, and a chart.
* **CreateWebReportSample.java**  
  An example of creating a web report with a table, a crosstab, and a chart arranged in a tabular.
* **TestDesignEditInvoice.java**  
  An example of how to modify an existing page report template.
* **TestDesignGraph.java**  
  An example of designing a report with a chart.
* **TestDesignInvoice.java**  
  An example of designing a report containing a banded object.
* **TestDesignSubreport.java**  
  An example of designing a report with a subreport.
* **TestInsertCrossTabIntoBanded.java**  
  An example of inserting a crosstab into a banded object.
* **TestInsertCrossTabIntoReport.java**  
  An example of designing a report with a crosstab.

To compile and run the sample programs, you should add JAR files with their paths into the class path. You need to add different JAR files according to how you install the Design API.

For example, you can use the following command to compile the sample program TestDesignInvoice.java:

`C:\LogiReport\Designer\help\samples\APIDesign>javac -classpath "C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\log4j-api-``2.17.2.jar``;C:\LogiReport\Designer\lib\log4j-core-``2.17.2.jar``;C:\LogiReport\Designer\lib\log4j-slf4j-impl-2.17.2.jar;C:\LogiReport\Designer\lib\slf4j-api-1.7.36.jar``" TestDesignInvoice.java`

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9898419824023/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: [Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751).

When you run the sample programs, you need to provide two or three parameters. If you want to use two parameters, they should be the catalog path and catalog name; if you want to use three parameters, they should be the catalog path, catalog name, and log file with a full path name.

The following example uses three parameters to run TestDesignInvoice.java. Here, it is assumed that you have installed Designer in `C:\LogiReport\Designer`, and the current directory when you execute these commands is `C:\LogiReport\Designer\help\samples\APIDesign` (location of the sample programs). After running the program, you can find a newly created file **TestInvoice.cls** in `C:\LogiReport\Designer\Demo\Reports\TutorialReports`.

`C:\LogiReport\Designer\help\samples\APIDesign>java -Dreporthome="C:\LogiReport\Designer" -classpath "C:\LogiReport\Designer\lib\JREngine.jar;C:\LogiReport\Designer\lib\sac-1.3.jar;C:\LogiReport\Designer\lib\report.jar;C:\LogiReport\Designer\lib\log4j-api-``2.17.2.jar``;C:\LogiReport\Designer\lib\log4j-core-``2.17.2.jar``;C:\LogiReport\Designer\lib\log4j-slf4j-impl-2.17.2.jar;C:\LogiReport\Designer\lib\slf4j-api-1.7.36.jar``;C:\LogiReport\Designer\lib\resource_en_US.jar;C:\LogiReport\Designer\lib\hsqldb-hsqldb-2.6.1.jar" TestDesignInvoice -path=C:\LogiReport\Designer\Demo\Reports\TutorialReports -catalog=JinfonetGourmetJava.cat -report=TestInvoice.cls -log=C:\LogiReport\Designer\logs\designer.log`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511592855-Designing-Reports-with-the-Design-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735563519639-Using-the-Exit-Functions)
