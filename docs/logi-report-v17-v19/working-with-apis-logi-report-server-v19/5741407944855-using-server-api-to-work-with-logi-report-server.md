---
title: "Using Server API to Work with Logi Report Server"
id: 5741407944855
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741407944855-Using-Server-API-to-Work-with-Logi-Report-Server
updated_at: 2022-10-31T17:15:45Z
---

# Using Server API to Work with Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394606103-Using-JavaScript-API-to-Embed-Server-Console-and-Reports-in-Your-Applications-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741408039575-Technical-Architecture)

# Using Server API to Work with Logi Report Server

Logi Report Server API is a set of Java programming interfaces that run reports, explore report resources, and provide access control for report servers. This topic describes the three ways you can use Logi Report Server with an application: JSPs, servlets, and Java APIs.

* **Use the web application composed of** Logi Report **Server JSP pages.** You can browse to the existing web pages for an interactive session to make report requests, rather than write new programs to offer special features based on calls of the Java API. The web application components offer a full set of report functions as well as listing available report resources based on the signed-in user's identity and permissions. You can use Logi Report Server in this way with an application built with any technology including .NET and HTML web pages.
* **Use the compiled servlets to make direct requests by URL.** Although not technically API, they serve the same purpose. Action requests are the method calls, with query parameters similar to method parameters. The servlet actions are limited to running, scheduling, and viewing reports. You can use servlets with an application built with any technology that can request a URL including HTML web pages, .NET applications, and Java web applications.
* **Use the Java API classes and methods.** You can call Java API classes and methods directly from a Java program to extend existing applications by building access to Logi Report functionality. Logi Report servlets and JSP web pages also use the same Java API classes and methods. Each Java API method has a Javadoc entry that describes how to use it.

  The functions of Logi Report are available through classes in the Java API including creating and modifying catalogs and reports, providing security such as Single Sign-on (SSO) authentication and authorization, and running, scheduling, and viewing reports.

Select the following links to view the topics:

* [Technical Architecture](https://devnet.logianalytics.com/hc/en-us/articles/5741408039575-Technical-Architecture)
* [Tour of the Java API](https://devnet.logianalytics.com/hc/en-us/articles/5741408065175-Tour-of-the-Java-API)
* [Java API for a Servlet](https://devnet.logianalytics.com/hc/en-us/articles/5741408671639-Java-API-for-a-Servlet)
* [Java API for an Application](https://devnet.logianalytics.com/hc/en-us/articles/5741394666391-Java-API-for-an-Application)
* [Installing the Server API](https://devnet.logianalytics.com/hc/en-us/articles/5741363396375-Installing-the-Server-API)
* [Using the Server API](https://devnet.logianalytics.com/hc/en-us/articles/5741394799255-Using-the-Server-API)
* [API Demos](https://devnet.logianalytics.com/hc/en-us/articles/5741407991063-API-Demos)
* [RMI Demos](https://devnet.logianalytics.com/hc/en-us/articles/5741363379863-RMI-Demos)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394606103-Using-JavaScript-API-to-Embed-Server-Console-and-Reports-in-Your-Applications-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741408039575-Technical-Architecture)
