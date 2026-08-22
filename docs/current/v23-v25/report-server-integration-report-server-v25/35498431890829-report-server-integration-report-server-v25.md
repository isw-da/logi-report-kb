---
title: "Report Server Integration Report Server v25"
id: 35498431890829
section: "Report Server Integration Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/35498431890829-Report-Server-Integration-Report-Server-v25
updated_at: 2026-02-26T02:13:18Z
source_host: docs-report.zendesk.com
---
# 
Report Server IntegrationReport Server v25

You can integrate Report Server seamlessly with any other Java application server to meet the information delivery needs of a single department or an entire enterprise. This topic describes how you can work with Java application servers.

Report Server contains a rich set of APIs that enable seamless integration and is implemented using Java Servlet technology and Java Server Page (JSP). These servlets and JSP pages enable you to work with any Java EE compliant application server that supports a Servlet Container and administer Report Server remotely through a web browser.

In order to deploy to an application server, you first have to create a Web Application Archive (WAR) file or an Enterprise Application Archive (EAR) file to include a Report Server, and then use the application server deployment tools to deploy the WAR/EAR file.

Select the following links to view the topics:

- 
                    Building a WAR/EAR File to Include a Self-contained Report Server
                

- 
                    Specifying Reporthome for Report Server in a Java EE Environment
                

- 
                    Four Ways of Integrating Report Server
                

- 
                    Deploying Report Server to a Java Application Server
                

- 
                    Integrating Remote Report Server
                

- 
                    Seamless Integrated Security Solution
                

 Page Report Studio and Web Report Studio use many dynamic classes, so you may encounter OutOfMemoryError: PermGen space problems when working with them after integration and when the JDK version in use is earlier than JDK 1.8.0. To solve the problem, you need to add -XX:MaxPermSize=256m to JVM or set the number to a larger one according to your situation. 

Related topic:

- 
                    Upgrading Server in an Integration Environment
