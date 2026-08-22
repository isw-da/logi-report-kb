---
title: "Logi Report Server Integration"
id: 1500009748382
section: "Logi Report Server Integration Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748382-Logi-Report-Server-Integration
updated_at: 2021-07-24T00:48:03Z
---

# Logi Report Server Integration

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742942-Saving-Analysis-Templates)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)

# Logi Report Server Integration Logi Report Server v17.1

You can integrate Logi Report Server seamlessly with any other Java application server to meet the information delivery needs of a single department or an entire enterprise. This topic describes how you can work with Java application servers.

Logi Report Server contains a rich set of APIs that enable seamless integration and is implemented using Java Servlet technology and Java Server Page (JSP). These servlets and JSP pages enable you to work with any Java EE compliant application server that supports a Servlet Container and administer Logi Report Server remotely through a web browser.

In order to deploy to an application server, you first have to create a Web Application Archive (WAR) file or an Enterprise Application Archive (EAR) file to include a Logi Report Server, and then use the application server deployment tools to deploy the WAR/EAR file.

Select the following links to view the topics:

* [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)
* [Specifying Reporthome for Logi Report Server in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009776981-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)
* [Four Ways of Integrating Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009777041-Four-Ways-of-Integrating-Logi-Report-Server)
* [Deploying Logi Report Server to a Java Application Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009748402-Deploying-Logi-Report-Server-to-a-Java-Application-Server)
* [Integrating Remote Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009776921-Integrating-Remote-Logi-Report-Server)
* [Seamless Integrated Security Solution](https://devnet.logianalytics.com/hc/en-us/articles/1500009777001-Seamless-Integrated-Security-Solution)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)Page Report Studio and Web Report Studio use many dynamic classes, so you may encounter **OutOfMemoryError: PermGen space** problems when working with them after integration and when the JDK version in use is earlier than JDK 1.8.0. To solve the problem, you need to add `-XX:MaxPermSize=256m` to JVM or set the number to a larger one according to your situation.

**Related topic:**

* [Upgrading Server in an Integration Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009748302-Upgrading-Logi-Report-Server#Integ)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742942-Saving-Analysis-Templates)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777021-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)
