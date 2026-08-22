---
title: "Using Server API to Work with Logi Report Server"
id: 4405690470551
section: "Working with APIs Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690470551-Using-Server-API-to-Work-with-Logi-Report-Server
updated_at: 2022-01-27T08:00:03Z
---

# Using Server API to Work with Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690468631-Using-JavaScript-API-to-Embed-Server-Console-and-Reports-in-Your-Applications-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690473239-Technical-Architecture)

# Using Server API to Work with Logi Report Server

Logi Report Server API is a set of Java programming interfaces that run reports, explore report resources, and provide access control for report servers. This topic describes the three ways you can use Logi Report Server with an application: JSPs, servlets, and Java APIs.

* **Use the web application composed of** Logi Report **Server JSP pages.** You can browse to the existing web pages for an interactive session to make report requests, rather than write new programs to offer special features based on calls of the Java API. The web application components offer a full set of report functions as well as listing available report resources based on the signed-in user's identity and permissions. You can use Logi Report Server in this way with an application built with any technology including .NET and HTML web pages.
* **Use the compiled servlets to make direct requests by URL.** Although not technically API, they serve the same purpose. Action requests are the method calls, with query parameters similar to method parameters. The servlet actions are limited to running, scheduling, and viewing reports. You can use servlets with an application built with any technology that can request a URL including HTML web pages, .NET applications, and Java web applications.
* **Use the Java API classes and methods.** You can call Java API classes and methods directly from a Java program to extend existing applications by building access to Logi Report functionality. Logi Report servlets and JSP web pages also use the same Java API classes and methods. Each Java API method has a Javadoc entry that describes how to use it.

  The functions of Logi Report are available through classes in the Java API including creating and modifying catalogs and reports, providing security such as Single Sign-on (SSO) authentication and authorization, and running, scheduling, and viewing reports.

Select the following links to view the topics:

* [Technical Architecture](https://devnet.logianalytics.com/hc/en-us/articles/4405690473239-Technical-Architecture)
* [Tour of the Java API](https://devnet.logianalytics.com/hc/en-us/articles/4405683546263-Tour-of-the-Java-API)
* [Java API for a Servlet](https://devnet.logianalytics.com/hc/en-us/articles/4405683569943-Java-API-for-a-Servlet)
* [Java API for an Application](https://devnet.logianalytics.com/hc/en-us/articles/4405690471447-Java-API-for-an-Application)
* [Installing the Server API](https://devnet.logianalytics.com/hc/en-us/articles/4405683545111-Installing-the-Server-API)
* [Using the Server API](https://devnet.logianalytics.com/hc/en-us/articles/4405683547287-Using-the-Server-API)
* [API Demos](https://devnet.logianalytics.com/hc/en-us/articles/4405690472343-API-Demos)
* [RMI Demos](https://devnet.logianalytics.com/hc/en-us/articles/4405683544087-RMI-Demos)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690468631-Using-JavaScript-API-to-Embed-Server-Console-and-Reports-in-Your-Applications-)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690473239-Technical-Architecture)
