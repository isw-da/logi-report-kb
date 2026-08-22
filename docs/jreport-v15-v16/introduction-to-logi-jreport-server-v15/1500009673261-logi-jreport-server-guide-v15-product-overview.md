---
title: " Logi JReport Server Guide v15 Product Overview"
id: 1500009673261
section: "Introduction to Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673261--Logi-JReport-Server-Guide-v15-Product-Overview
updated_at: 2021-07-24T20:54:08Z
---

#  Logi JReport Server Guide v15 Product Overview

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648542-Logi-JReport-v15-Release-Notes)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648202-Installing-Logi-JReport-Server)

# Logi JReport Product Overview

Logi JReport delivers operational business intelligence to enterprise applications through powerful embedded reporting.

Logi JReport is a complete Java reporting solution that provides sophisticated enterprise reporting, ad hoc reporting, and data analysis. A 100% Java EE architecture and a rich set of APIs allow Logi JReport to be seamlessly embedded into any application, providing end users with a transparent interface to easily generate reports, share information, and analyze data. With Logi JReport, any report can be made interactive, extending the "life" of a report by allowing users to easily sort, group, navigate, and filter via the Web. This wide range of functionality, including the ability to drill down on data, enables users to quickly derive value from their business intelligence.

Below is a list of the sections covered in this topic:

* [Logi JReport Product Architecture](#Architecture)
* [Reporting a Problem or Requesting a Feature](#Report)

## Logi JReport Product Architecture

Logi JReport's architecture takes advantage of the portability, scalability, and ease of integration associated with Java EE technology to provide a powerful, flexible reporting solution that fits perfectly within any application architecture.

![JReport Product Architecture](https://devnet.logianalytics.com/hc/article_attachments/4404926698775/jrpt_archtctr.png)

**Logi JReport Designer** is a Swing-based Integrated Development Environment (IDE) that enables sophisticated report design and presentation of critical business data. It provides an intuitive interface, reusable report components, flexible layout, and a toolset for designing and testing reports. With Logi JReport Designer, you can build reports using simple drag and drop techniques or by using the Report Wizard. Data can be accessed from any data source to design and preview reports in order to deliver information to end users in the most relevant and intuitive manner. Rapid creation and modification of reports is accomplished by toggling between design mode and view mode where the report will be displayed with the actual dataset. Once report design is complete, the report is published to Logi JReport Server for generation, delivery, and management.

**Logi JReport Server** is a 100% Java report generation and management tool. It enables efficient management, sharing, scheduling, versioning, and delivery of reports and enables reporting to be integrated into the workflow of any Java application. The high-performance engine can scale to any workload. Report results can be saved to a versioning system, sent to enterprise/workgroup printers, or e-mailed. With Logi JReport, reports can be viewed in any modern enterprise format including Page Report and Web Report using any standard browser, HTML, TEXT and standard business documents, such as PDF, Excel, and RTF. Logi JReport Server also supports on-demand, live report creation and modification, providing Logi JReport’s powerful ad hoc solution.

**JDashboard** delivers interactive data visualization and analysis to users. Users can freely choose the objects they want to display in the dashboard, without having to know how these objects were created, what data sources to use, what styles to set, and so on. A dashboard can hold multiple data components so that when browsing the dashboard users are able to see multiple data aspects. Within a dashboard, data components are able to communicate with each other via the message mechanism. This allows actions such as common filters to be applied to all the components of a dashboard even when coming from different data sources.

**Page Report Studio** and **Web Report Studio** enable reports to be accessed through a web browser via Dynamic HTML or AJAX. With Page Report Studio and Web Report Studio, end users can create their own richly visual and interactive reports for powerful and secure data exploration in a completely self-service manner. Using Page Report Studio and Web Report Studio's advanced capabilities, users can modify reports using dynamic filter and sort, drag and drop columns to and from an existing report, dynamically change chart types, pivot crosstabs, drill report data to specific groups, and convert report components or create an entirely new report.

**Visual Analysis** is a WYSIWYG product to visualize the result of every work step. Simply by dragging and dropping data fields onto a layout module, users are able to visually create crosstabs and charts step by step. The use of colors, sizes, shapes, and pie slices demonstrates the data in rich aspects.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Reporting a Problem or Requesting a Feature

If you are having trouble running Logi JReport Server or encounter any problems during reporting, take the following steps.

1. Check whether the system on which Logi JReport Server is running meets the [system requirements](https://devnet.logianalytics.com/hc/en-us/articles/1500009672941-System-Requirements).
2. Check the [Logi JReport FAQ pages](http://www.jinfonet.com/faq/) for frequently-asked questions and their solutions.

If the problem persists, report it to Jinfonet Support ([support@jinfonet.com](mailto:support@jinfonet.com)) with the following information:

1. Describe the precise steps leading to the problem.
2. Run the batch file jrenv.bat in the `<install_root>\bin` subdirectory. Running this batch file will generate a file called report.env in the current directory. Send this file to Jinfonet Support. Also, describe the operating environment, including machine type, CPU, memory, OS, and Java version.
3. If you are running Logi JReport in an integrated Java application server, select the **Server Information** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926699031/btn_srv_srvinfo.gif) on the Logi JReport Administration page to list the environment.
4. Send Jinfonet Support the log file with the recorded Logi JReport Server problems.
   * **For a standalone server**  
      Start Logi JReport with the batch file DJRServer.bat (.sh on Unix). Running this batch file will record the most detailed logging information and write them to the log files in the `<install_root>\logs` directory. Try to reproduce the problem, and send the log files along with the other information.
   * **For an integrated Logi JReport Server**  
      If your Logi JReport Server runs as a servlet inside a Java application server, send the log files generated by the Logi JReport Engine in the application server. When the Logi JReport Servlet is installed, a property file is generated which is used to define the class and arguments of the JRServlet. For example, if you integrated Logi JReport Server into WebLogic, find the WebLogic properties file located in the installation path of WebLogic. Edit the file to use the option -vDebug -vError. Your file should then contain the following content:

     vError=true  
      vDebug=true

     In addition, you can also directly add the java option -Dlogall=true (or -DvError=true, -DvDebug=true) to the java command line within the launch file of the application server.

     After restarting your application server, reproduce the problem and send the log files to Support.
5. Send Support the log files recording all of the logging information of engine and server (including event, error, debugging, access, management, and performance).
   * Change the configuration to record all logging events by starting the server and accessing the Logi JReport Administration page through `http://localhost:8889`.
     1. Go to the **Configuration** > **Log** panel.
     2. Set the log level of all logs to **TRIVIAL**.
     3. After that, reproduce your problem and send Support the log files in `<install_root>\logs`. In addition, you can also directly modify the logging configuration file LogConfig.properties in `<install_root>\bin`. If you set the server property log.config.update to true (all server properties are managed within the file server.properties in `<install_root>\bin`), any changes to the configuration file will automatically take effect at runtime after the specified update interval (set by the server property log.config.update.interval).
   * If your Logi JReport Server runs as a servlet within a Java application server, in the address bar of a web browser, type in `http://<hostname>/Logi JReport/admin`, where Logi JReport is the servlet context path.
6. To reproduce your problem of running reports with Logi JReport Server, we will often need your report, catalog and data information.
   1. Send Support the catalog file (\*.cat and \*.fml) and the report file \*.cls that you are having problems with.
   2. In order to resolve technical issues that you have reported, we will need to access your report data so that we can recreate and analyze the problem. Your database may be very large. However, we will only require access to the data returned by the query of the troublesome report, and if necessary we will sign a confidentiality agreement with you. To extract the report data, in the Catalog Browser of Logi JReport Designer, right-click the query that your report is using, select the menu item **Create Cached Query Result**. Then, input the data file name and select the **Save** button. The query result will then be saved in this file. Send Support all of the files generated (including the description file).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648542-Logi-JReport-v15-Release-Notes)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648202-Installing-Logi-JReport-Server)
