---
title: "Security for Accessing Web Pages"
id: 1500009749962
section: "Logi Report Server Security System Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749962-Security-for-Accessing-Web-Pages
updated_at: 2021-07-24T00:47:33Z
---

# Security for Accessing Web Pages

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749902-SSL-Support-in-the-LDAP-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748622-Managing-Logi-Report-Server)

# Security for Accessing Web Pages

This topic introduces the web page security mechanism of Logi Report Server, how to use Single Sign On, and how to configure HTTP Security Response Headers.

Logi Report Server provides a working web application as part of the product mix. This web application is implemented as a group of JSP pages and servlets that run in a Java web server's servlet container. Logi Report Server controls access to these JSP pages and servlets by requiring that a user be logged in to a web session before the JSP pages or servlets run.

The security framework of Logi Report Server also enables Single Sign On so that a user only needs to log in to an existing application and need not to do another login to access the Logi Report Server web pages.

![Security Framework](https://devnet.logianalytics.com/hc/article_attachments/4404880205847/wkapi_srv_tarch_jrs.gif)

This topic contains the following sections:

* [Web Page Security](#Page)
* [Single Sign On](#SSO)
* [Configuring HTTP Security Response Headers](#HTTPHeader)

## Web Page Security

Logi Report Server provides a working set of JSP pages and servlets that form a web application to schedule and run reports, view results, and so on. This web application is only available to registered users who identify themselves and log in to Logi Report Server. An administrator can [register users](https://devnet.logianalytics.com/hc/en-us/articles/1500009749862-Managing-User-Accounts), set passwords for them, associate them with groups and roles, and [grant them permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions), which is necessary for accessing the resources on Logi Report Server. This database of user information is used to validate the user name and password that is used to log in to the web application.

The sample in `<install_root>\help\samples\APISecurity\LoginLogout` can help you learn about web page security. It contains a set of JSP pages that can run to try out various styles of accessing a JSP page to see how the login dynamics work. The entry point to the set of JSP pages is **loginIndex.jsp**. Read the comments in the JSP pages to understand how to run the demonstration.

The following describes how Logi Report Server processes the web page security check.

**Only logged-in users may access the web pages**

When accessing Logi Report Server users should first log in. Once a user logs in to the web application the user can access the web pages.

Each JSP page and servlet in the web application starts off with code that checks if the current HTTP Request is from a user who is already logged in. If it is, the rest of the code executes because this user is a known user. There may be more permission checks within the code to control the specific request, but the user is allowed to access the web page.

If the current HTTP Request is not from a user who is already logged in, then the code attempts to log in the user using information available in the current HTTP Request, which may come from the following:

* An external service  
   When there is no current user logged in, Logi Report Server will make a call to an external helper class method, asking it to return the User ID to use. If the method call returns a User ID, Logi Report Server will validate if the User ID is registered on the server, and if it is, it will log that user in. This is called [Single Sign On](#SSO).
* A proprietary protocol based on authentication properties in the URL  
   When there is no current user logged in, Logi Report Server looks for specific [authentication properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009750302-Using-the-Authentication-Properties-in-URL) that it has designated as a way to pass in login credentials in the URL. If these authentication properties exist, Logi Report Server will use their value and try to log in the identified user. If the credentials are valid, then the user can log in and access the web page. Later HTTP Requests from that user will show that the user is already logged in.

If it is not possible to log in a user, then the code recognizes that it is an unauthorized request and does not allow the rest of the code to execute. It may send back a response to pop up the login dialog box on the browser or may do something else depending on the SSO implementation.

**Validation of users during login**

When obtaining the user name and password, Logi Report Server will validate if the login credentials match a Logi Report Server user. The built-in system for doing this looks at the information for the set of users that are registered in Logi Report Server. It validates whether the password is correct for the given user name.

Logi Report Server also defines the Java interface **AuthenticationProvider** that developers can implement to do the validation using an application's user database. For more information, see [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009771221-Customized-Implementation-of-the-Security-API).

**Permission control**

Once a web page is deemed accessible following the rules for login and validation, the JSP page or servlet is allowed to run. However, it may be that the logged in user does not have permission to do the requested operation or have rights for the target resource of the operation. This aspect of whether the user is authorized for the request is determined by Logi Report Server evaluating the permission information.

For developer users Logi Report Server also defines the Java interface **AuthorizationProvider** that they can implement to replace the built-in system for evaluating permissions and determining authorization. For more information, see [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009771221-Customized-Implementation-of-the-Security-API).

## Single Sign On

Logi Report Server's web pages are built to work with an existing web application. In particular, it is possible to set up the web server so that users of the website can log into an existing web application and have that login grant them access to the Logi Report Server web pages. This is called the Single Sign On feature.

Single Sign On is done by developers implementing the class defined by the Logi Report Server Java interface [HttpExternalAuthorized](https://devnet.logianalytics.com/hc/en-us/articles/1500009770901-Tour-of-the-Java-API#SSO) and telling Logi Report Server to use that implementation. The implementation can be aware of the application's technique for managing login state in the servlet session. This code can tell Logi Report Server which user is logged in. The implementation can redirect the user to the application's login workflow if the request is not from a logged-in user.

This system gives the user one spot in the application to log in. A successful login there will allow the user to run Logi Report Server web pages without doing another login dialog box.

Logi Report Server is told to use the local implementation of ExternalAuthorized in two ways.

* **Using the command line to define a system property that registers the class**

  You can use the system property **jrs.httpExternalAuthorized** to hold the name of the class that implements **HttpExternalAuthorized**.

  If the name of the class is **DemoExternalAuthorized.java**, then change the script file that starts up Logi Report Server to include the parameter string: `-Djrs.httpExternalAuthorized=DemoExternalAuthorized`.

  **Example 1: A simple example of retrieving user name from the database server**

  1. Create a table by DDL as below in the database:

     `CREATE TABLE jr_auth(auth_key varchar(64), auth_uid varchar(256) NOT NULL, PRIMARY KEY(auth_key))`

     Insert testing data for an example:

     `insert into jr_auth (auth_key, auth_uid) values('987654321', 'admin');`

     **Tip:** jr\_auth includes the inserted/updated data. auth\_uid should be a Logi Report Server user name (the login user).
  2. Configure the database connection in **databaseCfg.ini** located in the sub-directory config\ of the DemoExternalAuthorized class. The default path is `<server_install_root>\help\samples\APISecurity\SSO\config`.

     driver=com.mysql.jdbc.Driver  
     dbUrl=jdbc:mysql://IP\_Address:3306/test  
     dbUser=root  
     dbPassword=1234
  3. Extract **compile\_tool.zip** in `<server_install_root>\help\samples\APISecurity\SSO` to the same directory as **DemoExternalAuthorized.java**. Choose a compile tool according to your operating system, compile\_tool.bat for Windows or compile\_tool.sh for Unix. Configure the arguments in the corresponding file based on your environment, then double-click the file to start compiling the Java code **DemoExternalAuthorized.java**.
  4. Download the JDBC driver required in this example, **mysql-connector-java-5.1.7-bin.jar**, from the MySQL website, and put it to `<server_install_root>\help\samples\APISecurity\SSO\lib`.
  5. Modify the Logi Report Server start shell script **JRServer.bat** in `<server_install_root>\bin` to add the following in the class path:
     + The JDBC driver, for example, `C:\LogiReport\Server\help\samples\APIsecurity\SSO\lib\mysql-connector-java-5.1.7-bin.jar`.
     + The absolute path of the directory that contains all the SSO implementaion files, for example, `C:\LogiReport\Server\help\samples\APISecurity\SSO\`
     + The JVM option `-Djrs.httpExternalAuthorized=DemoExternalAuthorized`

     ![Add JVM Option](https://devnet.logianalytics.com/hc/article_attachments/4404885353495/scrty_web_sso_pth.gif)

     The class **DemoExternalAuthorized** in the example implements the interface **HttpExternalAuthorized**. Once the class has loaded, after Logi Report Server starts up you will get the following message in its console window: DemoExternalAuthorized class is loaded. If you want to edit the authorization method, you just need to edit the method *getExternalAuthorizedUser* in DemoExternalAuthorized.
  6. You can change the web page that Logi Report Server displays after login, by changing the URL under the sentence "Which web page do you want to visit after login?" in **ssodemo.jsp** in `<server_install_root>\help\samples\APISecurity\SSO`.

     ![Change URL](https://devnet.logianalytics.com/hc/article_attachments/4404885353751/scrty_web_sso_scrpt.gif)
  7. Move **ssodemo.jsp** to the **public\_html** folder in the Logi Report Server root directory.
  8. Start Logi Report Server by running **JRServer.bat**.
  9. Access **ssodemo.jsp** and pass the parameters **jrauth\_key** and **jrauth\_id** from other pages.
  10. Test the SSO demo using **login.html** in `<server_install_root>\help\samples\APISecurity\SSO`.

      ![Test SSO Demo](https://devnet.logianalytics.com/hc/article_attachments/4404880206743/scrty_web_sso_dm.gif)

      **Tip:** Do not modify the two parameter names when using **ssodemo.jsp** we provided, or there will be exceptions. If you need to modify the parameter names, change them in all the three files: login.html, ssodemo.jsp, and DemoExternalAuthorized.java.

  **Example 2: An example of retrieving user name from the SSO server**

  The demo SSO implementation **DemoSSO.java** for this example is in `<server_install_root>\help\samples\APISecurity\SingleSignOn\Example2`. In order for it to work, modify the Logi Report Server start shell script **JRServer.bat** in `<server_install_root>\bin` to add the following in the class path:

  + The absolute path of the directory that contains the demo SSO implementation files: `<server_install_root>\help\samples\APISecurity\SingleSignOn\Example2\`
  + The JVM option `-Djrs.httpExternalAuthorized=DemoSSO`

  The SSO code logic is as follows:

  1. Receive token from customer application incoming HTTP request, for example `auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NzksImV4cCI6MTU0NDY0NTUzOS4wLCJjbGFpbXMiOiJDYW5BY2Nlc3NDb3Vyc2VDYXRhbG9nLENhbkFjY2Vzc1VzZXJzLENhbk1vZGlmeUFjY291bnRTZXR0aW5ncyxDYW5Nb2RpZnlBc3NpZ25tZW50cyxDYW5Nb2RpZnlBdXRvbWF0aWNBc3NpZ25tZW50cyxDYW5Nb2RpZnlCaWxsaW5nSW5mb3JtYXRpb24sQ2FuTW9kaWZ5Q3VzdG9tQ291cnNlcyxDYW5Nb2RpZnlDdXN0b21GaWVsZHMsQ2FuTW9kaWZ5U2Vzc2lvbnMsQ2FuTW9kaWZ5R3JvdXBzLENhbk1vZGlmeU11bHRpcGxlVXNlcnMsQ2FuTW9kaWZ5UmVwb3J0cyxDYW5Nb2RpZnlVc2VycyJ9.xqQgiVFhrujJskkjjbgPrvey8gZa2if1QSfgKTMib-g`

     Receive lms-url (host variable) from incoming HTTP request, too. For example, `lms-url=Logi Report.inclassnow.info`
  2. Pass token to customer's end point for validation check.

     **Request URL:** https://{lms-url}/self/claims  
     **Request Method:** GET  
     **content-type:** application/json; charset=utf-8  
     **Headers:**  
     **authorization:** bearer
     eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NzksImV4cCI6MTU0NDY0NTUzOS4wLCJjbGFpbXMiOiJDYW5BY2Nlc3NDb3Vyc2VDYXRhbG9nLENhbkFjY2Vzc1VzZXJzLENhbk1vZGlmeUFjY291bnRTZXR0aW5ncyxDYW5Nb2RpZnlBc3NpZ25tZW50cyxDYW5Nb2RpZnlBdXRvbWF0aWNBc3NpZ25tZW50cyxDYW5Nb2RpZnlCaWxsaW5nSW5mb3JtYXRpb24sQ2FuTW9kaWZ5Q3VzdG9tQ291cnNlcyxDYW5Nb2RpZnlDdXN0b21GaWVsZHMsQ2FuTW9kaWZ5U2Vzc2lvbnMsQ2FuTW9kaWZ5R3JvdXBzLENhbk1vZGlmeU11bHRpcGxlVXNlcnMsQ2FuTW9kaWZ5UmVwb3J0cyxDYW5Nb2RpZnlVc2VycyJ9.xqQgiVFhrujJskkjjbgPrvey8gZa2if1QSfgKTMib-g  
     **Response:**  
     {"accountId":501,"userId":1979,"claims":["CanAccessCourseCatalog","CanAccessUsers","CanManageAllUsers","CanModifyAccountSettings","CanModifySessions","CanModifyGroups","CanModifyMultipleUsers","CanModifyReports","CanModifyUsers"]}
  3. Receive returning JSON string as above and parse the **accountId** and **userId** out.
  4. Check received **userId** in our system to see whether this user name exists in Logi Report Server.
     If it exists, we can move on.
     However, if it does not exist, we need to add this **userId** as our user name in Logi Report, create a group named accountId, add this user to the accountID group, and add the user to at least the "everyone" role.
  5. Check whether there is a subfolder named accountId under the root node in the server resource tree. If the folder is there, move on. If the folder is not there yet, create that folder and set the permission that only the same accountID and userID can access this folder.
  6. Set **accountId** as a parameter in our session variable.
  7. Return **userId** and exit from SSO code.
* **Using a Java API method call to register the class**

  The Java API class **HttpUserSessionManager** has a method for setting the ExternalAuthrized object that Logi Report Server uses.

  If the name of the package is **com.mycorp.myHttpExternalAuthorized**, then in a JSP page, connect to Logi Report Server, then pass an instance of the class object for myHttpExtneralAuthorized
  as the parameter in the method *HttpUserSessonManager.setHttpExternalAuthorized()*.

  ```
  <%@ page import="com.example.MyHttpExternalAuthorized" %>  
  				
          // initialize and connect to Logi Report Server  
      initEnv(System.getProperties());  
      HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);  
          // set the HttpExternalAuthorized object used by Logi Report Server  
      HttpUserSessionManager    hsm  = (HttpUserSessionManager)httpRptServer.getHttpUserSessionManager();  
      hsm.setHttpExternalAuthorized(new DemoExternalAuthorized());
  ```

There are examples of implementations of the Java interface **ExternalAuthorized** in the sample source files that come with Logi Report Server. Look in the folder `<install_root>\help\samples\APISecurity\SingleSignOn`. Read the comments in the source code for more information about Single Sign On and how to use the Java interface.

* help\samples\APISecurity\SingleSignOn\CustomHttpExternalAuthorized.java
* help\samples\APISecurity\SingleSignOn\com\example\MyExternalAuthorized.java

In that same **SingleSignOn** folder are several JSP pages that you can place into the public\_html\jinfonet folder and run as web applications to exercise and demonstrate how Single Sign On works. The file **customIndex.jsp** is the entry point page. It has comments inside it on how to run the demonstration.

## Configuring HTTP Security Response Headers

There are many HTTP security headers you can utilize to provide the necessary protection for your Logi Report Server JSPs and servlets that respond to browser requests in a standalone environment, like HTTP Strict Transport Security (HSTS), X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, and Content-Security-Policy. Since different users may choose different response headers for security, Logi Report provides a configuration file which enables you to configure the security response headers all by yourselves. The configuration file is **responseHeaders.properties** in the `<install_root>\bin` directory. You can set the security header name/value pairs in the file according to your security policy. You can write a name/value pair as either "Name=Value" or "Name: Value". See two examples below:

* `X-Content-Type-Options=nosniff  
  Content-Security-Policy=script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; worker-src blob:; report-uri http://localhost:8888/demo/cspReport.jsp  
  X-XSS-Protection=1; mode=block`
* `X-Content-Type-Options: nosniff  
  Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; worker-src blob:; report-uri http://localhost:8888/demo/cspReport.jsp  
  X-XSS-Protection: 1; mode=block`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* The set of application users does not need to be the same set of users that are registered in Logi Report Server. However, the Single Sign On protocol does require that the application code identify the logged-in user to Logi Report Server using a registered Logi Report Server user name.
* When the set of application users is different from the set of Logi Report Server users, the application code for returning the logged-in user needs a system to map the application user to a Logi Report Server user.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749902-SSL-Support-in-the-LDAP-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748622-Managing-Logi-Report-Server)
