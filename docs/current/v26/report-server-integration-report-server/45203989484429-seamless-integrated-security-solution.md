---
title: "Seamless Integrated Security Solution"
id: 45203989484429
section: "Report Server Integration Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203989484429-Seamless-Integrated-Security-Solution
updated_at: 2026-04-30T14:10:22Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Seamless Integrated Security Solution 

This topic describes the seamless integrated security solution for when Report Server instance is in the same or different JVM as the web application.

As a reporting server, Report Server protects information via authentication and authorization processes. Furthermore, Report enables a web application to embed this reporting solution in it seamlessly not only on UI but also with the Java EE technology. In this way, the seamless integrated security solution becomes one of the key solutions of Report Server.

The scenarios of using Report solution can be categorized into the following two types according to the location of the Report Server instance.

This topic contains the following sections:

- Report Server Instance is in the Same JVM as the Web Application
                

- Report Server Instance is in a Different JVM from the Web Application
                

## 
Report Server Instance is in the Same JVM as the Web Application

In this scenario, the application includes Report Server JAR files into the same JVM, and it also includes Report built-in servlets and JSPs which handle running web and page reports and other reporting services, for example, scheduling reports.

In this scenario, the client (HTTP client) most of time will send a request to the portal, JSP, or Servlet of the web application, and the web application can either call the public Server API to the server instance directly to run a report and output a report to file system, or it can re-direct the request to the Report services provided by the Report JSPs and Servlets, for example the Page Report Studio JSP and Servlet. Report JSPs/Servlets will first make sure the request is authenticated and authorized. After that, it will call the internal API method against the Report Server Instance in the same JVM to fulfill the requirement and return suitable information to the client via JSPs or internally generated output steam.

In the preceding illustration, you can see that the HTTP client can send a request directly to the application JSP/Servlets or Report JSPs/Servlets. Before the Report JSP and Servlet make a response, an Auth Check is performed to authenticate the session and then authorize the action. Normally, the built-in authenticator and authorization instance of Report Server (Instance) is called to perform these checking actions. However, if the application wants to control the process, the web developer can set up the configuration to use the customized authenticator and authorization instance instead.

Pay attention to the box "External Authorized Instance". This Java class implements Reportjet.server.api.http.HttpExternalAuthorized to provide the authenticated user ID from the session. If this Instance returns a user ID, Report will pass it to its authenticator to check if it is valid. If the user ID is valid for Report, Report will qualify the session of the request, and will not ask for signing in again. If this external authorized instance does not return a user ID, Report will respond the request by asking for signing in.

You can provide the box "Authenticator and Authorizer Instance" by implementing two other interfaces: jet.server.api.custom.security.AuthenticationProvider and jet.server.api.custom.security.AuthorizationProvider.

You use the AuthenticationProvider to authenticate the user ID, including whether the user ID is valid. And use the AuthorizationProvider to check the privileges of the user against the action that the user requests.

During the auth check process, if the external authorized instance returns a user ID of the session, Report auth check will continue to send the user ID to the AuthenticatorProvider to check if it is valid or not. If the user is valid, the auth check will qualify the session of the request, and then continue to check if the action is valid for the user by asking the AuthorizationProvider instance.

In general, there is an authentication callback via the implemented interface of External Authorized. You can implement two security check providers to seamlessly integrate Report security into the application.

## 
Report Server Instance is in a Different JVM from the Web Application

From the web application itself, the architecture is the same as that when Report Server instance is in the same JVM as the web application. However, the way that it uses the Report solution is different since the Report Server Instance is outside the Web application server. Inside of the Web Application, the instance is RMI server being called by the web application server or Report built-in JSP/Servlets for the RMI solution.
