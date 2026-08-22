---
title: "Design API Samples"
id: 1500009562402
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562402-Design-API-Samples
updated_at: 2021-12-31T02:47:55Z
---

# Design API Samples

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562462-Working-with-Library-Components)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562522-Logi-JReport-Exit-Functions)

# Design API Samples

Logi JReport provides you with some sample programs which demonstrate how to create and edit reports and library components using the Design API in `<insatll_root>\help\samples\APIDesign`. They are:

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

To compile and run the sample programs, you should add jar files with their paths into the class path. Different jar files are required according to how [the Design API is installed](https://devnet.logianalytics.com/hc/en-us/articles/1500009562362-Installing-the-Design-API).

For example, you can use the following command to compile the sample program TestDesignInvoice.java:

`C:\Logi JReport\Designer\help\samples\APIDesign>javac -classpath "C:\Logi JReport\Designer\lib\JREngine.jar;C:\Logi JReport\Designer\lib\sac-1.3.jar;C:\Logi JReport\Designer\lib\report.jar;C:\Logi JReport\Designer\lib\log4j-core-2.7.jar；C:\Logi JReport\Designer\lib\log4j-api-2.7.jar" TestDesignInvoice.java`

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4411773980183/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

When you run the sample programs, you need to provide two or three parameters. If you want to use two parameters, they should be catalog path and catalog name; if you want to use three parameters, they should be catalog path, catalog name and log file with a full path name.

The following example uses three parameters to run TestDesignInvoice.java. Here, it is assumed that Logi JReport Designer has been installed to `C:\Logi JReport\Designer`, and the current directory when you execute these commands is `C:\Logi JReport\Designer\help\samples\APIDesign` (location of the sample programs). After running the program, you will find a newly created file TestInvoice.cls in `C:\Logi JReport\Designer\Demo\Reports\TutorialReports`.

`C:\Logi JReport\Designer\help\samples\APIDesign>java -Dreporthome="C:\Logi JReport\Designer" -classpath "C:\Logi JReport\Designer\lib\JREngine.jar;C:\Logi JReport\Designer\lib\sac-1.3.jar;C:\Logi JReport\Designer\lib\report.jar;C:\Logi JReport\Designer\lib\log4j-core-2.7.jar;C:\Logi JReport\Designer\lib\log4j-api-2.7.jar;C:\Logi JReport\Designer\lib\resource_en_US.jar;C:\Logi JReport\Designer\lib\hsqldb-2.3.4.jar" TestDesignInvoice -path=C:\Logi JReport\Designer\Demo\Reports\TutorialReports -catalog=JinfonetGourmetJava.cat -report=TestInvoice.cls -log=C:\Logi JReport\Designer\logs\designer.log`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562462-Working-with-Library-Components)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562522-Logi-JReport-Exit-Functions)
