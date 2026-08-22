---
title: "Technical Architecture"
id: 28891485217677
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891485217677-Technical-Architecture
updated_at: 2026-02-26T02:11:02Z
source_host: docs-report.zendesk.com
---
# 
Technical Architecture 

This topic describes specific implementation details about Report Server. It introduces the various elements that make up the full Report Server API. 

The technical view is different from the product architecture covered in another section of the user guide. This shows the programming elements and processes that exist, rather than the services they provide. The focus is on pointing out Java web application elements, Java servlets, and Java programming in the Report Server product.

Report Server is built with Java and uses standard Java and web technologies. The report server functionality is deployed in classes packaged into jar files that are accessed by class loading based on class path settings. Working web applications built on top of Report Server are JSP pages and servlets running in a web server's Servlet Container, using HTTP protocol, generating HTML and Java Script that is passed to the browser. This section gives a picture of how things fit together and what technologies are used. This provides a context for later detailed explanations about writing Java code to extend an application to use Report Server.

Software components

When talking about Report Server, there are three levels of software components to understand.

- Report Server - Software Components

Machine configurations

There are a variety of configurations for setting up a network to use Report Server. This topic will discuss how Report Server may fit into a variety of network layouts, starting with the simplest plain Report Server installed on a local PC or server. The discussion continues with how it fits with an existing web application. Then more complex configurations are explained, that scale up and support large web applications.

- Report Server - Out-of-the-Box - Ready to Run

- Report Server - With Existing Web Application

- Report Server - Remote Dedicated Server

- Report Server - Cluster

## 
Report Server - Software Components

The Report Server product is a combination of several software components.

- At the highest level, there are JSP files that generate interactive web pages that form the Report Server web application.

-  The following level is compiled servlets that supply a group of useful actions controlled by query parameters in the requesting HTTP Request.

- At the bottom level is the Java API. This is a library of Java classes and methods to be used by developers to access Report Server functionality.

The Java API is at the heart of the Report Server functionality, but it is the higher level components that provide immediate value and use.

Report Server has production-ready web pages for accessing reports

Report Server provides a large set of JSP-based web pages that are ready for production. These provide standard operations that most applications need.

When these JSP pages are deployed to the website, a visitor can access a web page that lists the set of reports available to them. From there they can run and schedule reports, including specifying parameters that control the purpose and scope of the report. They can use this web application to view the reports, or direct the reports to a PDF file, an email, or a variety of destinations.

These pages are available immediately. Full report functionality is available through these interactive web interface without writing any Java code or knowing anything about the low-level Java API.

These pages are written by Logi Analytics engineers using the Report Server Java API. Since they are JSP pages with visible source, they can be studied for ways of using the Java API or they can be refactored for a local variation of the web page. Using the CSS files and images it is also very easy to private label the application. 

Providing these Report Server web pages in your application is as easy as adding links that lead to the JSP pages. The JSP code can be customized to fit into the design of the application so that they appear seamlessly as part of the whole.

Any web server technology can be used to build an application that includes these Report Server web pages, including .NET and static HTML.

Report Server has production-ready servlets for accessing reports

Report Server also provides a set of compiled servlets that perform commonly needed actions related to running, scheduling, and viewing reports. These services are requested via HTTP requests, with a set of parameters in the URL that define and control the requested service. They are called with parameters that completely define their service so it is possible to use them as helper operations behind an interactive web page that gathers information from a visitor and posts to the servlet URL, with parameters telling the servlet what to do with any resulting output.

Accessing these components of Report is done by building and sending an HTTP request to the web server with a URL that points to the servlet. This can be done by a desktop program that interacts with a user to build up the needed parameters. A front end for the servlets could be a static HTML web page that provides a form for a user to fill in with the needed parameters before doing a submit to the URL. The web application can dynamically build appropriate links and put them into a menu or other page link. Any type web technology, including .NET can be used to build up an appropriate URL to call up the action of the servlets. Running the servlets does not depend on using Java.

There are examples of how the servlets are called in the sample file TestURL.html which is located in <instal_root>\help\samples\URLSamples.

Report Server has a large set of classes and methods in its Java API

Report Server provides a library of Java classes that can be used by a Java program. This is the Java API, which gives the most complete and versatile way to access Report functionality. In later architectural illustrations, this may be labeled Report Server API.

A developer can extend their application to provide report functionality by writing custom code to call the Report Server Java API to perform any operations needed. This is the key aspect of Report Server that makes it appealing for developers who need reporting functionality resident within the same web server.

Looking at the Javadocs for the Java API is intimidating. There are hundreds of classes and thousands of methods. 

A later section gives a high-level tour of the Java API, organized by functional area. This will introduce the Java API, so it is easier to understand.
 It will explain how the classes are organized to provide specific types of functionality. 

A developer only needs to understand the working set of classes and methods that relate to a particular application need. A developer does not need to know about every class or method documented in the Java API Javadoc.

## 
Report Server - Out-of-the-Box - Ready to Run

Report Server is a ready-to-run product that appears at first as a web application that lets users run and view reports.

Install Report Server and start it using the JRServer command or Windows Start menu. It is a web server ready for requests. It comes with a initial set of registered users and a set of sample reports that are in place to be run and viewed.

Start a browser and type the URL to the entry page. Assuming the install is onto the local PC, this is the URL to use: http://localhost:8888.

Sign in with user/password of admin/admin. The Report Server web application is then available.

What is running and how does it work?

Report Server - web application

The Report Server's web application is based on JSP files in several folders under the server's public_html folder and a few servlets compiled into classes. These JSP files and servlets create the HTML passed back to the browser, which gives users the web pages that access to the Report services. A visitor to the site can see a list of reports available, select one to schedule or run, and view or download the them. This is a standard web application giving access to a set of sample report resources that come with the product.

Viewing reports may involve use of Java Script running within an HTML page. This JavaScript code is supplied by a library of files in the public_html\javascript folder.

The web application also includes a folder of JSP pages (public_html\admin) that are dedicated to performing administrative duties for managing and configuring the server. You can run these only when you are an administrative user.

The servlet code that generates web pages makes calls to classes in Report Engine which does the real work. These classes are the Java API. 

The files that make up Report Server's web application code are JSP files, compiled servlets, and compiled classes deployed in library jar files.

- <install_root>\public_html\jinfonet\*

- <install_root>\public_html\dhtmljsp\*

- <install_root>\public_html\admin\*

- <install_root>\public_html\javascript\*

- <install_root>\lib\JREntServer.jar

- <install_root>\lib\JREngine.jar

- <install_root>\lib\JREESServlets.jar

Sign in and servlet session

All web applications need to protect web page access from unauthorized use. Report Server's web application includes a check at the start of every JSP page and servlet to verify that
 the requesting user is an authenticated Report user before running.

See a detailed explanation of how this works in the Security for Accessing Web Pages section.

User identity for a web session is managed across HTTP requests by data in the servlet session that is passed into the Servlet container with the HTTP Request.

### 
Report Server - With Existing Web Application

Report Server can be integrated into an existing web application. Put the application's JSP files and servlets together with the Report JSP files and servlets, along with the Report Server library files. For more information, see Report Server Integration.

After Report Server is installed along with the existing application, the application can be extended by writing new code that uses the Report Server API library.

It is when Report Server is used as part of a larger web application that its other identity begins to show. Report Server API comes into view. Report Server contains is a large set of classes with methods that can be used by any Java program. This set of classes and methods is the Report Java API.

Integrating JSP pages

An existing application can integrate with Report Server web pages in a simple fashion by adding links from the existing application to the Report Server JSP pages.

This provides the Report Server web pages with the look and feel that is native to Report Server.

Because the Report Server web application is implemented as JSP pages, these can be edited to change the look and feel while not changing the functionality.

An existing application can be extended to access Report Server functionality by adding Java code to access the Report Server classes and methods that are defined in the Java API. An existing application can have complete control over the look and feel of web pages while providing access to running, scheduling, and viewing reports.

Many of the JSP pages in Report Server could be copied to the customer's application, modified, ignored, or removed and have web interactions with users provided by an extended existing application, using Java calls to request report functionality. 

## 
Report Server - Remote Dedicated Server

Report Server can run in standalone mode directly as it is installed out of the box or can run as a Windows service or as a WAR file running in any standard servlet container provided by web servers such as Tomcat, JBoss, WebSphere, and WebLogic. The customers application and users then access Report Server across the net either via RMI to servlets from Java application code or JSP page, or via HTTP requests with a URL that directly call Report's servlets and JSP pages.

In a servlet container

This is a common configuration for accessing Report functionality for small applications. Report Server is installed in a servlet container, ready to handle requests. The client machine can be simply a browser or be a full web application. It requests Report functionality using URLs to Report servlets and Report JSP pages running in the Report Servlet Container. This is the enjoinment when you run Report Server from the JRServer command line or build a jreport.war and deploy it to an application server to run in its own container. 

As a remote dedicated server

When Report is embedded into an existing application it is usually run in a separate JVM or a separate server computer. Report runs as a back-end server handling requests coming from the web application server's front end. Report Servers' JSP pages are moved to the front-end machine into the same servlet container or JVM as the application code. The front end web application's Java code runs with version of the Java API that are stubs providing seamless access to the back end methods using RMI (Remote Method Invocation) to call the real Java methods in Report Server in the other JVM.

## 
Report Server - Cluster

Report can also run as a cluster using either a cluster of remote Report standalone instances or as a cluster of Report WAR files running inside a group of independent application server instances or as an application server cluster such as JBoss's cluster technology. When Report is in a clustered environment, there is a built-in dispatcher that has several available algorithms to distribute the runtime load. A Java interface is defined that enables developers to write their own load distribution algorithm and register that with the Report Server Cluster service.

The following diagram shows one potential configuration where Report and the application are running in web containers. The Report instances can be clustered so no matter where a resource is published it is visible on both systems and even if one system goes down for maintenance, the other system can handle the requests and new instances can be quickly started to handle larger loads. The client machines can go to either server, so the user does not need to be aware of which Report Server is handling the request. 

 For more information, see Report Server Cluster.

Load Balancer 

Report provides several built-in algorithms for load balancing and assigning tasks to servers. In most cases, one of the built-in methods described in load balancing mechanism is adequate; however, Report provides an interface called LoadBalancer that enables you to customize assigning tasks to specific server instances. For example, you may want to assign tasks to specific servers based on the user ID yet still go to other servers if the specified server is overloaded or down.

You can view the jet.server.api.cluster.LoadBalancer and jet.server.api.rmi.RemoteDispatcher interfaces in the Report Javadoc, and see the examples in <install_root>\help\samples\APICluster for reference.
