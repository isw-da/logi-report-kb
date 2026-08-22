---
title: "Seamless Integrated Security Solution"
id: 1500009673241
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673241-Seamless-Integrated-Security-Solution
updated_at: 2021-07-24T20:54:10Z
---

# Seamless Integrated Security Solution

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673181-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-WebLogic-11g-Release-1-10-3-2-by-a-WAR-File)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644262-Logi-JReport-Server-Guide-v15-Server-Cluster)

# Seamless Integrated Security Solution

As a reporting server, Logi JReport Server protects information via authentication and authorization processes. Furthermore, Logi JReport allows a web application to embed this reporting solution in it seamlessly not only on UI but also with the Java EE technology. In this way, the seamless integrated security solution becomes one of the key solutions of Logi JReport Server.

There are all kinds of scenarios on using Logi JReport solution. However, they can all be categorized into the following two types according to the location of the Logi JReport Server instance.

## Logi JReport Server Instance Is Located in the Same JVM As the Web Application

![](https://devnet.logianalytics.com/hc/article_attachments/4404926699287/integ_sltn_same.gif)

In this scenario, the application includes Logi JReport Server JAR files into the same JVM, and it also includes Logi JReport built-in servlets and JSPs which handle running web and page reports and other reporting services, for example, scheduling reports.

**Description of the illustration**

In this scenario, the client (HTTP client) most of time will send a request to the portal, JSP or Servlet of the web application, and the web application can either call the public Server API to the server instance directly to run a report and output a report result to file system, or it can re-direct the request to the Logi JReport services provided by the Logi JReport JSPs and Servlets, for example the Page Report Studio JSP and Servlet. Logi JReport JSPs/Servlets will first make sure the request is authenticated and authorized. After which, it will call the internal API method against the Logi JReport Server Instance in the same JVM to fulfill the requirement and return suitable information to the client via JSPs or internally generated output steam.

In the illustration above, you can see that the HTTP client can send a request directly to the application JSP/Servlets or Logi JReport JSPs/Servlets. Before a response is made by the Logi JReport JSP and Servlet, an Auth Check is performed to authenticate the session and then authorize the action. Normally, the built-in authenticator and authorization instance of Logi JReport Server (Instance) is called to perform these checking actions. However, if the application wants to control the process, the web application developer can set up the configuration to ensure that the customized authenticator and authorization instance is used instead.

Pay attention to the box "External Authorized Instance". This Java class implements Logi JReport jet.server.api.http.HttpExternalAuthorized to provide the authenticated user ID from the session. If this Instance returns a user ID, Logi JReport will pass it to its authenticator to check if it is valid. If the user ID is valid for Logi JReport, Logi JReport will qualify the session of the request, and will not ask for a login again. If this external authorized instance does not return a user ID, Logi JReport will respond the request by asking for a login.

The box "Authenticator and Authorizer Instance" can be provided by implementing two other interfaces: jet.server.api.custom.security.AuthenticationProvider and jet.server.api.custom.security.AuthorizationProvider.

The AuthenticationProvider is used to authenticate the user ID, including whether or not the user ID is valid. The AuthorizationProvider is used to check the privileges of the user against the action that the user requests.

During the auth check process, if the external authorized instance returns a user ID of the session, Logi JReport auth check will continue to send the user ID to the AuthenticatorProvider to check if it is valid or not. If the user is valid, the auth check will qualify the session of the request, and then continue to check if the action is valid for the user by asking the AuthorizationProvider instance.

In general, there is an authentication callback via the implemented interface of External Authorized. Two security check providers can be implemented to seamlessly integrate Logi JReport security into the application.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logi JReport Server Instance Is Located in a Different JVM From the Web Application

![](https://devnet.logianalytics.com/hc/article_attachments/4404926699543/integ_sltn_dif.gif)

From the web application itself, the architecture is not changed. However, the way that it uses the Logi JReport solution is different since the Logi JReport Server Instance is outside of the Web application server. Inside of the Web Application, the instance is RMI server being called by the web application server or Logi JReport built-in JSP/Servlets for the RMI solution.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673181-Integrating-Remote-Logi-JReport-Server-Guide-v15-Server-with-WebLogic-11g-Release-1-10-3-2-by-a-WAR-File)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644262-Logi-JReport-Server-Guide-v15-Server-Cluster)
