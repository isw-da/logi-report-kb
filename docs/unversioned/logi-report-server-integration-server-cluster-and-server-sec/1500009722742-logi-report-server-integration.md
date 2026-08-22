---
title: "Logi Report Server Integration"
id: 1500009722742
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722742-Logi-Report-Server-Integration
updated_at: 2021-07-25T07:19:04Z
---

# Logi Report Server Integration

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744061-Saving-Analysis-Templates)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)

# Logi Report Server Integration

Logi Report Server can be seamlessly integrated with any other Java application server to meet the information delivery needs of a single department or an entire enterprise. It contains a rich set of APIs that allow for seamless integration and is implemented using Java Servlet technology and Java Server Page (JSP). These servlets and JSP pages enable the user to work with any Java EE compliant application server that supports a Servlet Container and administer Logi Report Server remotely through a web browser.

In order to deploy to an application server, you first have to create a Web Application Archive (WAR) file or an Enterprise Application Archive (EAR) file to include a Logi Report Server, and then use the application server deployment tools to deploy the WAR/EAR file.

The follow topics provide more information about integrating Logi Report Server:

* [Building a WAR/EAR File to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)
* [Specifying Reporthome for Logi Report Server in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009749841-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)
* [Four Ways of Integrating Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009722902-Four-Ways-of-Integrating-Logi-Report-Server)
* [Deploying Logi Report Server to a Java Application Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009722762-Deploying-Logi-Report-Server-to-a-Java-Application-Server)
* [Integrating Remote Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009722862-Integrating-Remote-Logi-Report-Server)
* [Seamless Integrated Security Solution](https://devnet.logianalytics.com/hc/en-us/articles/1500009722882-Seamless-Integrated-Security-Solution)

**Note:** Page Report Studio and Web Report Studio use many dynamic classes, so you may encounter "OutOfMemoryError: PermGen space" problems when working with them after integration and when the JDK version in use is earlier than JDK 1.8.0. To solve the problem, you need to add `-XX:MaxPermSize=256m` to JVM or set the number to a larger one according to your situation.

**Related topic:**

* [Upgrading in an Integration Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009749641-Upgrading-Logi-Report-Server#Integ)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744061-Saving-Analysis-Templates)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749861-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server)
