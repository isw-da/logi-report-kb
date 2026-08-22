---
title: " Server Integration  Server v18"
id: 4405683907223
section: "Logi Report Server Integration Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683907223--Server-Integration-Server-v18
updated_at: 2022-01-27T07:59:34Z
---

#  Server Integration  Server v18

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690465943-Saving-Analysis-Templates)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)

# Logi Report Server Integration Logi Report Server v18

You can integrate Logi Report Server seamlessly with any other Java application server to meet the information delivery needs of a single department or an entire enterprise. This topic describes how you can work with Java application servers.

Logi Report Server contains a rich set of APIs that enable seamless integration and is implemented using Java Servlet technology and Java Server Page (JSP). These servlets and JSP pages enable you to work with any Java EE compliant application server that supports a Servlet Container and administer Logi Report Server remotely through a web browser.

In order to deploy to an application server, you first have to create a Web Application Archive (WAR) file or an Enterprise Application Archive (EAR) file to include a Logi Report Server, and then use the application server deployment tools to deploy the WAR/EAR file.

Select the following links to view the topics:

* [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)
* [Specifying Reporthome for Logi Report Server in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/4405690633367-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)
* [Four Ways of Integrating Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405683916439-Four-Ways-of-Integrating-Logi-Report-Server)
* [Deploying Logi Report Server to a Java Application Server](https://devnet.logianalytics.com/hc/en-us/articles/4405683908375-Deploying-Logi-Report-Server-to-a-Java-Application-Server)
* [Integrating Remote Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/4405683913495-Integrating-Remote-Logi-Report-Server)
* [Seamless Integrated Security Solution](https://devnet.logianalytics.com/hc/en-us/articles/4405690634263-Seamless-Integrated-Security-Solution)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg) Page Report Studio and Web Report Studio use many dynamic classes, so you may encounter **OutOfMemoryError: PermGen space** problems when working with them after integration and when the JDK version in use is earlier than JDK 1.8.0. To solve the problem, you need to add `-XX:MaxPermSize=256m` to JVM or set the number to a larger one according to your situation.

**Related topic:**

* [Upgrading Server in an Integration Environment](https://devnet.logianalytics.com/hc/en-us/articles/4405690621207-Upgrading-Logi-Report-Server#Integ)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690465943-Saving-Analysis-Templates)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690635159-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)
