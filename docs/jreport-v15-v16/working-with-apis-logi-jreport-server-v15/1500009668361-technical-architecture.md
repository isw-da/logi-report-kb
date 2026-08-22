---
title: "Technical Architecture"
id: 1500009668361
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009668361-Technical-Architecture
updated_at: 2021-07-24T20:55:31Z
---

# Technical Architecture

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668121-Logi-JReport-Server-Guide-v15-Server-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668401-Tour-of-the-Java-API)

# Technical Architecture

This topic reviews specific implementation details about Logi JReport Server. The technical view is different from the product architecture covered in other topics of the user guide. This topic shows the programming elements and processes that exist, rather than the services they provide. The focus is on pointing out Java web application elements and Java servlets and Java programming in the Logi JReport Server product. It introduces the various elements that make up the full Logi JReport Server API.

Logi JReport Server is built with Java and uses standard Java and web technologies. The report server functionality is deployed in classes packaged into jar files that are accessed by class loading based on class path settings. Working web applications built on top of the Logi JReport Server are JSP pages and servlets running in a web server's Servlet Container, using HTTP protocol, generating HTML and Java Script that is passed to the browser. This section gives a picture of how things fit together and what technologies are used. This provides a context for later detailed explanations about writing Java code to extend an application to use Logi JReport Server.

**Software components**

When talking about Logi JReport Server, there are three levels of software components to understand.

* [Logi JReport Server - Software Components](#Software)

**Machine configurations**

There are a variety of configurations for setting up a network to use Logi JReport Server. This topic will discuss how Logi JReport Server may fit into a variety of network layouts, starting with the simplest plain Logi JReport Server installed on a local PC or server. The discussion continues with how it fits with an existing web application. Then more complex configurations are explained, that scale up and support large web applications.

* [Logi JReport Server - Out of the Box](#Box)
* [Logi JReport Server - With Existing Web Application](#APP)
* [Logi JReport Server - Remote Dedicated Server](#Remote)
* [Logi JReport Server - Cluster](#Cluster)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logi JReport Server - Software Components

The Logi JReport Server product is a combination of several software components.

* At the highest level, there are JSP files that generate interactive web pages that form the Logi JReport Server web application.
* Below that are compiled servlets that supply a group of useful actions controlled by query parameters in the requesting HTTP Request.
* At the bottom level is the Java API. This is a library of Java classes and methods to be used by developers to access Logi JReport Server functionality.

The Java API is at the heart of the Logi JReport Server functionality but it is the higher level components that provide immediate value and use.

**Logi JReport Server has production-ready web pages for accessing reports**

Logi JReport Server provides a large set of JSP-based web pages that are ready for production. These provide standard operations that most applications need.

When these JSP pages are deployed to the website, a visitor can access a web page that lists the set of reports available to them. From there they can schedule and run reports, including entering parameters that control the purpose and scope of the report. They can use this web application to view the results, or direct the reports to a PDF file, an e-mail, or a variety of destinations.

These pages are available immediately. Full report functionality is available through these interactive web interface without writing any Java code or knowing anything about the low level Java API.

These pages are written by Jinfonet engineers using the Logi JReport Server Java API. Since they are JSP pages with visible source, they can be studied for ways of using the Java API or they can be refactored for a local variation of the web page. Using the CSS files and images it is also very easy to private label the application.

Providing these Logi JReport Server web pages in your application is as easy as adding links that lead to the JSP pages. The JSP code can be customized as needed to fit into the design of the application so that they appear seamlessly as part of the whole.

Any web server technology can be used to build an application that includes these Logi JReport Server web pages, including .NET and static HTML.

**Logi JReport Server has production-ready servlets for accessing reports**

Logi JReport Server also provides a set of compiled servlets that perform commonly needed actions related to running and scheduling reports, and viewing results. These services are requested via HTTP requests, with a set of parameters in the URL that define and control the requested service. They are called with parameters that completely define their service so it is possible to use them as helper operations behind an interactive web page that gathers information from a visitor and posts to the servlet URL, with parameters telling the servlet what to do with any resulting output.

Accessing these components of Logi JReport is done by building and sending an HTTP request to the web server with a URL that points to the servlet. This can be done by a desktop program that interacts with a user to build up the needed parameters. A front end for the servlets could be a static HTML web page that provides a form for a user to fill in with the needed parameters before doing a submit to the URL. The web application can dynamically build appropriate links and put them into a menu or other page link. Any type web technology, including .NET can be used to build up an appropriate URL to call up the action of the servlets. Running the servlets does not depend on using Java.

There are examples of how the servlets are called in the sample file TestURL.html which is located in `<instal_root>\help\samples\URLSamples`.

**Logi JReport Server has a large set of classes and methods in its Java API**

Logi JReport Server provides a library of Java classes that can be used by a Java program. This is the Java API, which gives the most complete and versatile way to access Logi JReport functionality. In later architectural illustrations, this may be labeled Logi JReport Server API.

An application developer can extend their application to provide report functionality by writing custom code to call the Logi JReport Server Java API to perform any operations needed. This is the key aspect of Logi JReport Server that makes it appealing for application developers who need reporting functionality resident within the same web server.

Looking at the Javadocs for the Java API is intimidating. There are hundreds of classes and thousands of methods.

A later section gives a high-level [tour of the Java API](https://devnet.logianalytics.com/hc/en-us/articles/1500009668401-Tour-of-the-Java-API), organized by functional area. This will introduce the Java API so it is easier to understand.
It will explain how the classes are organized to provide specific types of functionality.

A developer only needs to understand the working set of classes and methods that relate to a particular application need. A developer does not need to know about every class or method documented in the Java API Javadocs.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logi JReport Server - Out of the Box

Logi JReport Server is a ready-to-run product that appears at first as a web application that lets users run reports and view results.

Install Logi JReport Server and start it running by using the JRServer command or Windows Start menu. It is a web server ready for requests. It comes with a initial set of registered users and a set of sample reports that are in place to be run and viewed.

Start a browser and enter the URL to the entry page. Assuming the install is onto the local PC, this is the URL to use: `http://localhost:8888`.

Login with user/password of admin/admin. After login, the Logi JReport Server web application is available.

What's running and how does it work?

**Logi JReport Server - web application**

![](https://devnet.logianalytics.com/hc/article_attachments/4404920411543/wkapi_srv_tarch_jrs.gif)

The Logi JReport Server's web application is based on JSP files in several folders under the server's public\_html folder and a few servlets compiled into classes. These JSP files and servlets create the HTML passed back to the browser, which gives users the web pages that access to the Logi JReport services. A visitor to the site can see a list of reports available, select one to schedule or run, and view or download the results. This is a standard web application giving access to a set of sample report resources that come with the product.

Viewing report result may involve use of Java Script running within an HTML page. This javascript code is supplied by a library of files in the public\_html\javascript folder.

The web application also includes a folder of JSP pages (public\_html\admin) that are dedicated to performing administrative duties for managing and configuring the server. These can only be run by an administrative user.

The servlet code that generates web pages makes calls to classes in the Logi JReport Engine which does the real work. These classes are the Java API.

The files that make up Logi JReport Server's web application code are JSP files, compiled servlets, and compiled classes deployed in library jar files.

* <install\_root>\public\_html\jinfonet\\*
* <install\_root>\public\_html\dhtmljsp\\*
* <install\_root>\public\_html\admin\\*
* <install\_root>\public\_html\javascript\\*
* <install\_root>\lib\JREntServer.jar
* <install\_root>\lib\JREngine.jar
* <install\_root>\lib\JREESServlets.jar

**Login and servlet session**

All web applications need to protect web page access from unauthorized use. Logi JReport Server's web application includes a check at the start of every JSP page and servlet to verify that
the requesting user is an authenticated Logi JReport user before running.

See a detailed explanation of how this works in the [Security for Accessing Web Pages](https://devnet.logianalytics.com/hc/en-us/articles/1500009650182-Security-for-Accessing-Web-Pages) section.

User identity for a web session is managed across HTTP requests by data in the servlet session that is passed into the Servlet container with the HTTP Request.

## Logi JReport Server - With Existing Web Application

![](https://devnet.logianalytics.com/hc/article_attachments/4404926786967/wkapi_srv_tarch_web.gif)

Logi JReport Server can be integrated into an existing web application. Put the application's JSP files and servlets together with the Logi JReport JSP files and servlets, along with the Logi JReport Server library files. Read more about the details on how to do this in [Logi JReport Server Ingegration](https://devnet.logianalytics.com/hc/en-us/articles/1500009648382-Logi-JReport-Server-Guide-v15-Server-Integration).

After Logi JReport Server is installed along with the existing application, the application can be extended by writing new code that uses the Logi JReport Server API library.

It is when Logi JReport Server is used as part of a larger web application that it's other identity begins to show. Logi JReport Server API comes into view. Logi JReport Server contains is a large set of classes with methods that can be used by any Java program. This set of classes and methods is the Logi JReport Java API.

**Integrating JSP pages**

An existing application can integrate with Logi JReport Server web pages in a simple fashion by adding links from the existing application to the Logi JReport Server JSP pages.

This provides the Logi JReport Server web pages with the look and feel that is native to Logi JReport Server.

Because the Logi JReport Server web application is implemented as JSP pages, these can be edited to change the look and feel while not changing the functionality.

An existing application can be extended to access Logi JReport Server functionality by adding Java code to access the Report Server classes and methods that are defined in the Java API. An existing application can have complete control over the look and feel of web pages while providing access to running and scheduling reports and viewing results.

Many of the JSP pages in Logi JReport Server could be copied to the customer's application, modified, ignored or removed and have web interactions with users provided by an extended existing application, using Java calls to request report functionality.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logi JReport Server - Remote Dedicated Server

Logi JReport Server can run in standalone mode directly as it is installed out of the box or can run as a Windows Service or as a WAR file running in any standard servlet container such as provided by Tomcat, JBoss, WebSphere, WebLogic, and so on. The customers application and users then access the Logi JReport Server across the net either via RMI to servlets from Java application code or JSP page, or via HTTP requests with a URL that directly call Logi JReport's servlets and JSP pages.

**In a servlet container**

This is a common configuration for accessing Logi JReport functionality for small applications. Logi JReport Server is installed in a servlet container, ready to handle requests. The client machine can be simply a browser or be a full web application. It requests Logi JReport functionality by using URLs to Logi JReport servlets and Logi JReport JSP pages running in the Logi JReport Servlet Container. This is the enjoinment when you run Logi JReport Server from the JRServer command line or build a Logi JReport.war and and deploy it to an application server to run in it's own container.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926787223/wkapi_srv_tarch_remote1.gif)

**As a remote dedicated server**

When Logi JReport is embedded into an existing application it is usually run in a separate JVM or a separate server machine. Logi JReport runs as a back end server handling requests coming from the web application server's front end. Logi JReport Servers' JSP pages are moved to the front end machine into the same servlet container or JVM as the application code. The front end web application's Java code runs with version of the Java API that are stubs providing seamless access to the back end methods using RMI (Remote Method Invocation) to call the real Java methods in the Logi JReport Server in the other JVM.

![](https://devnet.logianalytics.com/hc/article_attachments/4404926787479/wkapi_srv_tarch_remote2.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logi JReport Server - Cluster

Logi JReport can also run as a cluster using either a cluster of remote Logi JReport standalone instances or as a cluster of Logi JReport WAR files running inside a group of independent application server instances or as an application server cluster such as JBoss's cluster technology. When Logi JReport is in a clustered environment, there is a built-in dispatcher that has several available algorithms to distribute the runtime load. A Java interface is defined that allows application developers to write their own load distribution algorithm and register that with the Logi JReport Cluster service.

The following diagram shows one potential configuration where Logi JReport and the application are running in web containers. The Logi JReport instances can be clustered so no matter where a resource is published it is visible on both systems and even if one system goes down for maintenance, the other system can handle the requests and new instances can be quickly started to handle larger loads. The client machines can go to either server so the user does not need to be aware of which Logi JReport Server is handling the request.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920661655/wkapi_srv_tarch_cluster.gif)

Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009644262-Logi-JReport-Server-Guide-v15-Server-Cluster) for more information about Logi JReport Server Cluster.

**Load Balancer**

Logi JReport provides several built-in algorithms for load balancing and assigning tasks to servers. In most cases, one of the built-in methods described in [load balancing mechanism](https://devnet.logianalytics.com/hc/en-us/articles/1500009668921-Logi-JReport-Server-Guide-v15-Server-Cluster-Main-Features#Algorithms) is adequate; however, Logi JReport provides an interface called LoadBalancer that allows you to customize assigning tasks to specific server instances. For example, you may want to assign tasks to specific servers based on the user id yet still go to other servers if the specified server is overloaded or down.

You can view the Javadoc at jet.server.api.cluster.LoadBalancer and jet.server.api.rmi.RemoteDispatcher. See the examples in `<install_root>\help\samples\APICluster`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668121-Logi-JReport-Server-Guide-v15-Server-API)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668401-Tour-of-the-Java-API)
