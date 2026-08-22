---
title: "Addressing Security and Authentication for Embedding Reports Within Your Application"
id: 360050173193
section: "Best Practices"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050173193-Addressing-Security-and-Authentication-for-Embedding-Reports-Within-Your-Application
updated_at: 2022-10-31T11:14:01Z
---

# Addressing Security and Authentication for Embedding Reports Within Your Application

To achieve different styles of embedding reports into your application, Logi Report offers different options for security and user authentication: [Logi Report Built-in SSO](https://www.jinfonet.com/knowledge-base/addressing-security-and-authentication-for-embedding-reports-and-dashboards-within-your-application/#Logi%20Report), [3rd-Party SSO – OAuth 2.0/SAML/OpenID](https://www.jinfonet.com/knowledge-base/addressing-security-and-authentication-for-embedding-reports-and-dashboards-within-your-application/#3Party), or [URL Direct](https://www.jinfonet.com/knowledge-base/addressing-security-and-authentication-for-embedding-reports-and-dashboards-within-your-application/#URL). A brief explanation of each follows.

## Option 1: Logi Report Built-in SSO

![Option 1: Logi Report Built-in SSO](https://devnet.logianalytics.com/hc/article_attachments/9900913857815)

| Pros | Cons |
| --- | --- |
| * More secure. * Full control over customization by the development team. | * Need to setup a dedicated database. * Token maintenance (invalidation, expiration process, and so on). * Token generation and verification require development effort. |
| Overview of Setup Steps | |
| 1. Create the Authentication Database. The Authentication Database must include the login user name logged by the user application along with an Authentication key (this can be a randomly generated code with time stamp). 2. Write a java class CustomHttpExternalAuthorized which implements the interface *jet.server.api.http.HttpExternalAuthorized*. The method getExternalAuthorizedUser returns a Logi Report User ID associated with the currently logged in application user, so you will need to modify this method and get the logged in application user from Authentication Database. 3. Add option `-Djrs.httpExternalAuthorized=CustomHttpExternalAuthorized` on your Logi Report java application (don’t forget to set options for integration environment variables on your web services startup script).   **Notes:**   * You will need to maintain the Authentication Database for your application’s user logins and logouts. * The same user information needs to be maintained in Logi Report Server. | |

## Option 2: 3rd-Party SSO w/ OAuth 2.0/SAML/OpenID

![Option 2: 3rd-Party SSO w/ OAuth 2.0](https://devnet.logianalytics.com/hc/article_attachments/9900913835031)

| Pros | Cons |
| --- | --- |
| * More secure. * OAuth 2.0/SAML/OpenID are widely accepted standards for SSO. * No need to maintain a token system. | * Need to setup the required platform. * Learning and coding curve based on the different platform. * 3-rd party libraries are required. |
| **Overview of Setup Steps** | |
| **Example: joauth2 Setup** | |
| 1. Download the needed resource in the attachment section. 2. Deploy joauth2.war into your web service i.e. Tomcat. 3. Install the PostgreSQL database and initialize the joauth2 database using the oauth2.sql file. 4. Change the joauth2 configuration file application.properties. This mainly includes configuring the properties jreport.host and jreport.sso\_url, and the data source information. 5. If the value of jreport.host and oauth\_db\_host changes the local IP, Joauth2.reusserRefreshToken is true, and refresh\_token will be used until the end of the loop; If the value is false, the access\_token will be updated upon each refresh. 6. Place Oauth2HttpExternalAuthorized.class and Oauth2HttpExternalAuthorized$Authentication.class into the classes folder which is local to the Logi Report web application. 7. Put joauth\_sso.jsp into Logi Report folder, and change authen\_url and mix\_erp. 8. Add the option `-Djrs.httpExternalAuthorized=Oauth2HttpExternalAuthorized` to your Logi Report java application. Add integration ENV options to the web service startup script as needed. | |
| **.NET Application Setup** | |
| .NET applications need to integrate DotNetOpenAuth.OAuth2.Client.   DotNetOpenAuth.OAuth2.Client is the default SDK provided by DotNetOpenAuth to the C# client, and Logi Report’s integration uses the license code pattern (Authorization Code), which is now the most common mode of authorization for web apps. The client guides the user to enter credentials to obtain user authorization (AccessToken) in the authorization server, and then offers access to the user resources. | |
| **jOAuth2 Database Description** | |
| * users: Data mode is username, password, enabled. User can be used when enabled is true. * authorities: Saves the spring security permission information. * oauth\_client\_details: Saves the Oauth2 register client information. * oauth\_code: Saves the authorization code of the table; the authorization code is automatically deleted after the exchange. * oauth\_access\_token: Saves access\_token table, automatically maintained by joauth2. * oauth\_refresh\_token: Saves refresh\_token table, automatically maintained by joauth2. | |
| **Required jOAuth 3rd Party Libraries** | |
| * Spring * Spring mvc * Spring security * Spring security config * Spring security-oauth2 | |

## Option 3: URL Direct

![Option 3: URL Direct](https://devnet.logianalytics.com/hc/article_attachments/9900929714199)

| Pros | Cons |
| --- | --- |
| * Simplest method. * No additional system are needed. * Cost friendly and minimal on-going maintenance. | * Less secure. * Dependent on the strength of encryption algorithm selected by your company. * You have to address the coding effort for encryption and decryption. |
| Overview of Setup Steps | |
| Below is an example of directly invoking report via URL, the user name password in the following example is encrypted with Base64 encoding in the jrs.authorization variable:   `http://localhost:8888/jinfonet/tryView.jsp? jrs.cmd=jrs.try_vw&jrs.report=%2fSampleReports%2fEmployeeInformation.cls &jrs.catalog=%2fSampleReports%2fSampleReports.cat&jrs.result_type=8 &jrs.authorization=YWRtaW46YWRtaW4` | |
