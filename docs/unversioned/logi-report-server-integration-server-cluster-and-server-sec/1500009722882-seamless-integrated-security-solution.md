---
title: "Seamless Integrated Security Solution"
id: 1500009722882
section: "Logi Report Server Integration, Server Cluster, and Server Security Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722882-Seamless-Integrated-Security-Solution
updated_at: 2021-07-25T07:19:02Z
---

# Seamless Integrated Security Solution

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749801-Integrating-Remote-Logi-Report-Server-with-WebLogic-12c-12-2-1-3-0-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744601-Logi-Report-Server-Cluster)

# Seamless Integrated Security Solution

As a reporting server, Logi Report Server protects information via authentication and authorization processes. Furthermore, Logi Report allows a web application to embed this reporting solution in it seamlessly not only on UI but also with the Java EE technology. In this way, the seamless integrated security solution becomes one of the key solutions of Logi Report Server.

There are all kinds of scenarios on using Logi Report solution. However, they can all be categorized into the following two types according to the location of the Logi Report Server instance.

Select the following links to view the topics:

* [Logi Report Server Instance is Located in the Same JVM as the Web Application](#Same)
* [Logi Report Server Instance is Located in a Different JVM from the Web Application](#Dif)

## Logi Report Server Instance is Located in the Same JVM as the Web Application

![Same JVM](https://devnet.logianalytics.com/hc/article_attachments/4404936808215/integ_sltn_same.gif)

In this scenario, the application includes Logi Report Server JAR files into the same JVM, and it also includes Logi Report built-in servlets and JSPs which handle running web and page reports and other reporting services, for example, scheduling reports.

**Description of the illustration**

In this scenario, the client (HTTP client) most of time will send a request to the portal, JSP or Servlet of the web application, and the web application can either call the public Server API to the server instance directly to run a report and output a report result to file system, or it can re-direct the request to the Logi Report services provided by the Logi Report JSPs and Servlets, for example the Page Report Studio JSP and Servlet. Logi Report JSPs/Servlets will first make sure the request is authenticated and authorized. After which, it will call the internal API method against the Logi Report Server Instance in the same JVM to fulfill the requirement and return suitable information to the client via JSPs or internally generated output steam.

In the illustration above, you can see that the HTTP client can send a request directly to the application JSP/Servlets or Logi Report JSPs/Servlets. Before a response is made by the Logi Report JSP and Servlet, an Auth Check is performed to authenticate the session and then authorize the action. Normally, the built-in authenticator and authorization instance of Logi Report Server (Instance) is called to perform these checking actions. However, if the application wants to control the process, the web application developer can set up the configuration to ensure that the customized authenticator and authorization instance is used instead.

Pay attention to the box "External Authorized Instance". This Java class implements Logi Report jet.server.api.http.HttpExternalAuthorized to provide the authenticated user ID from the session. If this Instance returns a user ID, Logi Report will pass it to its authenticator to check if it is valid. If the user ID is valid for Logi Report, Logi Report will qualify the session of the request, and will not ask for a login again. If this external authorized instance does not return a user ID, Logi Report will respond the request by asking for a login.

The box "Authenticator and Authorizer Instance" can be provided by implementing two other interfaces: jet.server.api.custom.security.AuthenticationProvider and jet.server.api.custom.security.AuthorizationProvider.

The AuthenticationProvider is used to authenticate the user ID, including whether or not the user ID is valid. The AuthorizationProvider is used to check the privileges of the user against the action that the user requests.

During the auth check process, if the external authorized instance returns a user ID of the session, Logi Report auth check will continue to send the user ID to the AuthenticatorProvider to check if it is valid or not. If the user is valid, the auth check will qualify the session of the request, and then continue to check if the action is valid for the user by asking the AuthorizationProvider instance.

In general, there is an authentication callback via the implemented interface of External Authorized. Two security check providers can be implemented to seamlessly integrate Logi Report security into the application.

## Logi Report Server Instance is Located in a Different JVM from the Web Application

![Different JVM](https://devnet.logianalytics.com/hc/article_attachments/4404936808471/integ_sltn_dif.gif)

From the web application itself, the architecture is not changed. However, the way that it uses the Logi Report solution is different since the Logi Report Server Instance is outside of the Web application server. Inside of the Web Application, the instance is RMI server being called by the web application server or Logi Report built-in JSP/Servlets for the RMI solution.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749801-Integrating-Remote-Logi-Report-Server-with-WebLogic-12c-12-2-1-3-0-by-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744601-Logi-Report-Server-Cluster)
