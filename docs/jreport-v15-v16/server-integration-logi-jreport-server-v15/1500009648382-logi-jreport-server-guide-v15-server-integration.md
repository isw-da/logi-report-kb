---
title: "Logi JReport Server Guide v15 Server Integration"
id: 1500009648382
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648382-Logi-JReport-Server-Guide-v15-Server-Integration
updated_at: 2021-07-24T20:54:12Z
---

# Logi JReport Server Guide v15 Server Integration

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009667801-Saving-Analysis-Templates)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server)

# Server Integration Logi JReport Server Guide v15

Logi JReport Server can be seamlessly integrated with any other Java application server to meet the information delivery needs of a single department or an entire enterprise. It contains a rich set of APIs that allow for seamless integration and is implemented using Java Servlet technology and Java Server Page (JSP). These servlets and JSP pages enable the user to work with any Java EE compliant application server that supports a Servlet Container and administer the Logi JReport Server remotely through a web browser.

In order to deploy to an application server, you first have to create a Web Application Archive (WAR) file or an Enterprise Application Archive (EAR) file to include a Logi JReport Server, and then use the application server deployment tools to deploy the WAR/EAR file.

The following topics provide more information about ingegration:

* [Building a WAR/EAR File to Include a Self-Contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server)
* [Specifying Reporthome for Logi JReport Server in a Java EE Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009673221-Specifying-Reporthome-for-Logi-JReport-Server-Guide-v15-Server-in-a-Java-EE-Environment)
* [Four Ways of Integrating Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648522-Four-Ways-of-Integrating-Logi-JReport-Server-Guide-v15-Server)
* [Deploying Logi JReport Server to a Java Application Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009673041-Deploying-Logi-JReport-Server-Guide-v15-Server-to-a-Java-Application-Server)
* [Integrating Remote Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648482-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server)
* [Seamless Integrated Security Solution](https://devnet.logianalytics.com/hc/en-us/articles/1500009673241-Seamless-Integrated-Security-Solution)

**Note:** Page Report Studio and Web Report Studio use many dynamic classes, so you may encounter "OutOfMemoryError: PermGen space" problems when working with them after integration and when the JDK version in use is earlier than JDK 1.8. To solve the problem, you need to add `-XX:MaxPermSize=256m` to JVM or set the number to a larger one according to your situation.

**Related topic:**[Upgrading Logi JReport Server in an Integration Environment](https://devnet.logianalytics.com/hc/en-us/articles/1500009648322-Upgrading-Logi-JReport-Server-Guide-v15-Server#Integ)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009667801-Saving-Analysis-Templates)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server)
