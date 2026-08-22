---
title: "Seamless Integrated Security Solution"
id: 5741461315351
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741461315351-Seamless-Integrated-Security-Solution
updated_at: 2022-10-31T17:17:59Z
---

# Seamless Integrated Security Solution

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741467888791-Integrating-Remote-Logi-Report-Server-with-WebLogic-14-1-1-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415572759-Logi-Report-Server-Cluster-Logi-Report-Server-v19)

# Seamless Integrated Security Solution

This topic describes the seamless integrated security solution for when Logi Report Server instance is in the same or different JVM as the web application.

As a reporting server, Logi Report Server protects information via authentication and authorization processes. Furthermore, Logi Report enables a web application to embed this reporting solution in it seamlessly not only on UI but also with the Java EE technology. In this way, the seamless integrated security solution becomes one of the key solutions of Logi Report Server.

The scenarios of using Logi Report solution can be categorized into the following two types according to the location of the Logi Report Server instance.

This topic contains the following sections:

* [Logi Report Server Instance is in the Same JVM as the Web Application](#Same)
* [Logi Report Server Instance is in a Different JVM from the Web Application](#Dif)

## Logi Report Server Instance is in the Same JVM as the Web Application

![Same JVM](https://devnet.logianalytics.com/hc/article_attachments/9905715637399/integ_sltn_same.gif)

In this scenario, the application includes Logi Report Server JAR files into the same JVM, and it also includes Logi Report built-in servlets and JSPs which handle running web and page reports and other reporting services, for example, scheduling reports.

In this scenario, the client (HTTP client) most of time will send a request to the portal, JSP, or Servlet of the web application, and the web application can either call the public Server API to the server instance directly to run a report and output a report to file system, or it can re-direct the request to the Logi Report services provided by the Logi Report JSPs and Servlets, for example the Page Report Studio JSP and Servlet. Logi Report JSPs/Servlets will first make sure the request is authenticated and authorized. After that, it will call the internal API method against the Logi Report Server Instance in the same JVM to fulfill the requirement and return suitable information to the client via JSPs or internally generated output steam.

In the preceding illustration, you can see that the HTTP client can send a request directly to the application JSP/Servlets or Logi Report JSPs/Servlets. Before the Logi Report JSP and Servlet make a response, an Auth Check is performed to authenticate the session and then authorize the action. Normally, the built-in authenticator and authorization instance of Logi Report Server (Instance) is called to perform these checking actions. However, if the application wants to control the process, the web developer can set up the configuration to use the customized authenticator and authorization instance instead.

Pay attention to the box "External Authorized Instance". This Java class implements Logi Report**jet.server.api.http.HttpExternalAuthorized** to provide the authenticated user ID from the session. If this Instance returns a user ID, Logi Report will pass it to its authenticator to check if it is valid. If the user ID is valid for Logi Report, Logi Report will qualify the session of the request, and will not ask for signing in again. If this external authorized instance does not return a user ID, Logi Report will respond the request by asking for signing in.

You can provide the box "Authenticator and Authorizer Instance" by implementing two other interfaces: jet.server.api.custom.security.AuthenticationProvider and jet.server.api.custom.security.AuthorizationProvider.

You use the AuthenticationProvider to authenticate the user ID, including whether the user ID is valid. And use the AuthorizationProvider to check the privileges of the user against the action that the user requests.

During the auth check process, if the external authorized instance returns a user ID of the session, Logi Report auth check will continue to send the user ID to the AuthenticatorProvider to check if it is valid or not. If the user is valid, the auth check will qualify the session of the request, and then continue to check if the action is valid for the user by asking the AuthorizationProvider instance.

In general, there is an authentication callback via the implemented interface of External Authorized. You can implement two security check providers to seamlessly integrate Logi Report security into the application.

## Logi Report Server Instance is in a Different JVM from the Web Application

![Different JVM](https://devnet.logianalytics.com/hc/article_attachments/9905677223703/integ_sltn_dif.gif)

From the web application itself, the architecture is the same as that when Logi Report Server instance is in the same JVM as the web application. However, the way that it uses the Logi Report solution is different since the Logi Report Server Instance is outside the Web application server. Inside of the Web Application, the instance is RMI server being called by the web application server or Logi Report built-in JSP/Servlets for the RMI solution.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741467888791-Integrating-Remote-Logi-Report-Server-with-WebLogic-14-1-1-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415572759-Logi-Report-Server-Cluster-Logi-Report-Server-v19)
