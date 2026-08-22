---
title: "Using Server API to Work with Report Server"
id: 28891446152333
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891446152333-Using-Server-API-to-Work-with-Report-Server
updated_at: 2026-02-26T02:11:01Z
source_host: docs-report.zendesk.com
---
# 
Using Server API to Work with Report Server 

Report Server API is a set of Java programming interfaces that run reports, explore report resources, and provide access control for report servers. This topic describes the three ways you can use Report Server with an application: JSPs, servlets, and Java APIs.

- 
Use the web application composed of Report Server JSP pages. You can browse to the existing web pages for an interactive session to make report requests, rather than write new programs to offer special features based on calls of the Java API. The web application components offer a full set of report functions as well as listing available report resources based on the signed-in user's identity and permissions. You can use Report Server in this way with an application built with any technology including .NET and HTML web pages.

- 
Use the compiled servlets to make direct requests by URL. Although not technically API, they serve the same purpose. Action requests are the method calls, with query parameters similar to method parameters. The servlet actions are limited to running, scheduling, and viewing reports. You can use servlets with an application built with any technology that can request a URL including HTML web pages, .NET applications, and Java web applications.

- 
Use the Java API classes and methods. You can call Java API classes and methods directly from a Java program to extend existing applications by building access to Report functionality. Report servlets and JSP web pages also use the same Java API classes and methods. Each Java API method has a Javadoc entry that describes how to use it.
			    The functions of Report are available through classes in the Java API including creating and modifying catalogs and reports, providing security such as Single Sign-on (SSO) authentication and authorization, and running, scheduling, and viewing reports.

Select the following links to view the topics:

- Technical Architecture

- Tour of the Java API

- Java API for a Servlet

- Java API for an Application

- Installing the Server API

- Using the Server API

- API Demos

- RMI Demos
