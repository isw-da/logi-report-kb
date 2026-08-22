---
title: "Security for Accessing Web Pages"
id: 1500009650182
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650182-Security-for-Accessing-Web-Pages
updated_at: 2021-07-24T20:53:38Z
---

# Security for Accessing Web Pages

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675041-SSL-Support-in-LDAP-System-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673361-Managing-Logi-JReport-Server-Guide-v15-Server)

# Security for Accessing Web Pages

Logi JReport Server provides a working web application as part of the product mix. This web application is implemented as a group of JSP pages and servlets that run in a Java web server's servlet container. Logi JReport Server controls access to these JSP pages and servlets by requiring that a user be logged in to a web session before the JSP pages or servlets run.

The security framework of Logi JReport Server also allows for Single Sign-On so that a user only needs to login to an existing application and not need to do another login to access the Logi JReport Server web pages.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920411543/wkapi_srv_tarch_jrs.gif)

This topic introduces the web page security mechanism of Logi JReport Server and how to use Single Sign-On respectively.

Below is a list of the sections covered in this topic:

* [Web Page Security](#Page)
* [Single Sign-On](#SSO)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Web Page Security

Logi JReport Server provides a working set of JSP pages and servlets that form a web application to schedule and run reports, view results and so on. This web application is only available to registered users who identify themselves and log in to Logi JReport Server. An administrator can [register users](https://devnet.logianalytics.com/hc/en-us/articles/1500009650102-Managing-User-Accounts), set passwords for them, associate them with groups and roles and [grant them permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions) which is necessary for accessing the resources on Logi JReport Server. This database of user information is used to validate the user name and password that is used to log in to the web application.

The sample in `<install_root>\help\samples\APISecurity\LoginLogout` can help you learn about web page security. It contains a set of JSP pages that can be run to try out various styles of accessing a JSP page to see how the login dynamics works. The entry point to the set of JSP pages is loginIndex.jsp. Read the comments in the JSP pages to understand how to run the demonstration.

The following details how the web page security check is processed on Logi JReport Server.

**Only logged-in users may access the web pages**

When accessing Logi JReport Server users should log in first. Once a user logs in to the web application he can access the web pages.

Each JSP page and servlet in the web application starts off with code that checks if the current HTTP Request is from a user who is already logged in. If it is, the rest of the code executes because this user is a known user. There may be more permissions checks within the code to control the specific request, but the user is allowed to access the web page.

If the current HTTP Request is not from a user who is already logged in, then the code attempts to log in the user using information available in the current HTTP Request, which may come from the following:

* An external service.  
   When there is no current user logged in, Logi JReport Server will make a call to an external helper class method, asking it to return the User ID to use. If the method call returns a User ID, Logi JReport Server will validate if the User ID is registered on the server and if it is, it will log that user in. This is called [Single Sign-On](#SSO).
* A proprietary protocol based on authentication properties in the URL.  
   When there is no current user logged in, Logi JReport Server looks for specific [authentication properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009650382-Using-the-Authentication-Properties-) that it has designated as a way to pass in login credentials in the URL. If these authentication properties exist, Logi JReport Server will use their value and try to login the identified user. If the credentials are valid, then the user is logged in and the web page can be accessed. Later HTTP Requests from that user will show that the user is already logged in.

If it is not possible to log in a user, then the code recognizes that it is an unauthorized request and does not allow the rest of the code to execute. It may send back response to pop up the login dialog on the browser or may do something else depending on SSO implementation.

**Validation of users during login**

When the user name and password are obtained, Logi JReport Server will validate if the login credentials match to a Logi JReport Server user. The built-in system for doing this looks at the information for the set of users that are registered in Logi JReport Server. It validates whether the password is correct for the given user name.

Logi JReport Server also defines the AuthenticationProvider Java interface that developers can implement to do the validation using an application's user database. For more information, see [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009668781-Customized-Implementation-of-the-Security-API).

**Permission control**

Once a web page is deemed accessible following the rules for login and validation, the JSP page or servlet is allowed to run. However it may be that the logged in user does not have permission to do the requested operation or have rights for the target resource of the operation. This aspect of whether the user is authorized for the request is determined by Logi JReport Server evaluating the permission information.

For developer users Logi JReport Server also defines the AuthorizationProvider Java interface that can be implemented to replace the built-in system for evaluating permissions and determining authorization. For more information, see [Customized Implementation of the Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009668781-Customized-Implementation-of-the-Security-API).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Single Sign-On

Logi JReport Server's web pages are built to work with an existing web application. In particular, it is possible to set up the web server so that users of the website can login to an existing web application and have that login grant them access to the Logi JReport Server web pages. This is called the Single Sign-On feature.

Single Sign-On is done by developers implementing the class defined by the Logi JReport Server Java interface [HttpExternalAuthorized](https://devnet.logianalytics.com/hc/en-us/articles/1500009668401-Tour-of-the-Java-API#SSO) and telling Logi JReport Server to use that implementation. The implementation can be aware of the application's technique for managing login state in the servlet session. This code can tell Logi JReport Server which user is logged in. The implementation can redirect the user to the application's login workflow if the request is not from a logged-in user.

This system gives the user one spot in the application to login. A successful login there will allow the user to run Logi JReport Server web pages without doing another login dialog.

Logi JReport Server is told to use the local implementation of ExternalAuthorized in two ways.

* **Using the command line to define a system property that registers the class**

  The system property *jrs.httpExternalAuthorized* is used to hold the name of the class that implements HttpExternalAuthorized.

  If the name of the class is DemoExternalAuthorized.java, then change the script file that starts up Logi JReport Server to include the parameter string: `-Djrs.httpExternalAuthorized=DemoExternalAuthorized`.

  The following shows an example:

  1. Create a table by DDL as below in the database:

     `CREATE TABLE jr_auth(auth_key varchar(64), auth_uid varchar(256) NOT NULL, PRIMARY KEY(auth_key))`

     Insert testing data for an example:

     `insert into jr_auth (auth_key, auth_uid) values('987654321', 'admin');`

     **Tip:** jr\_auth includes the inserted/updated data. auth\_uid should be a Logi JReport Server user name (the login user).
  2. Configure the database connection in databaseCfg.ini located in the sub-directory config\ of the DemoExternalAuthorized class. The default path is `<server_install_root>\help\samples\APISecurity\SSO\config`.

     `driver=com.mysql.jdbc.Driver  
      dbUrl=jdbc:mysql://IP_Address:3306/test  
      dbUser=root  
      dbPassword=1234`
  3. Extract compile\_tool.zip in `<server_install_root>\help\samples\APISecurity\SSO`to the same directory as DemoExternalAuthorized.java. Choose a compile tool according to your operating system, compile\_tool.bat for Windows or compile\_tool.sh for Linux. Configure the arguments in the corresponding file based on your environment, then double-click the file to start compiling the Java code DemoExternalAuthorized.java.
  4. Download the JDBC driver required in this example, mysql-connector-java-5.1.7-bin.jar, from the MySQL website and put it to `<server_install_root>\help\samples\APISecurity\SSO\lib`.
  5. Modify the Logi JReport Server start shell script JRServer.bat in `<server_install_root>\bin` to add the following in the class path:
     + The JDBC driver. For example, C:\Logi JReport\Server\help\samples\APIsecurity\SSO\lib\mysql-connector-java-5.1.7-bin.jar.
     + The directory containing all the SSO implementaion files. In this example it is `<server_install_root>\help\samples\APISecurity\SSO\`. You need to add its absolute path `C:\Logi JReport\Server\help\samples\APISecurity\SSO\`.
     + The compiled class of DemoExternalAuthorized.java, by adding the JVM option `-Djrs.httpExternalAuthorized=DemoExternalAuthorized`.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920411799/scrty_web_sso_pth.gif)

     The class DemoExternalAuthorized in the example is used to implement the interface HttpExternalAuthorized. Once the class is successfully loaded, after Logi JReport Server starts up you would be able to get the following message on the server console: DemoExternalAuthorized class is loaded. If you want to edit the authorization method, you just need to edit the method getExternalAuthorizedUser in DemoExternalAuthorized.
  6. You can change the web page that will be displayed after login, by changing the URL under the sentence "Which web page do you want to visit after login?" in ssodemo.jsp in `<server_install_root>\help\samples\APISecurity\SSO`.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920412311/scrty_web_sso_scrpt.gif)
  7. Move ssodemo.jsp to the public\_html folder under the Logi JReport Server root directory.
  8. Start Logi JReport Server by running JRServer.bat. Access ssodemo.jsp and pass the parameters *jrauth\_key* and *jrauth\_id* from other pages. Then test the SSO demo by login.html in `<server_install_root>\help\samples\APISecurity\SSO`.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920412567/scrty_web_sso_dm.gif)

     **Tip:** Do not modify the two parameter names when using ssodemo.jsp we provided, or there will be exceptions. If you need to modify the parameter names, change them in all the three files: login.html, ssodemo.jsp, and DemoExternalAuthorized.java.
* **Using a Java API method call to register the class**

  The Java API class HttpUserSessionManager has a method for setting the ExternalAuthrized object that Logi JReport Server uses.

  If the name of the package is com.mycorp.myHttpExternalAuthorized, then in a JSP page, connect to Logi JReport Server, then pass an instance of the class object for myHttpExtneralAuthorized
  as the parameter in the method HttpUserSessonManager.setHttpExternalAuthorized().

  |  |
  | --- |
  | ``` <%@ page import="com.example.MyHttpExternalAuthorized" %>         // initialize and connect to Logi JReport Server     initEnv(System.getProperties());     HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);         // set the HttpExternalAuthorized object used by Logi JReport Server     HttpUserSessionManager    hsm  = (HttpUserSessionManager)httpRptServer.getHttpUserSessionManager();     hsm.setHttpExternalAuthorized(new DemoExternalAuthorized()); ``` |

There are examples of implementations of the ExternalAuthorized Java interface in the sample source files that come with Logi JReport Server. Look in the folder `<install_root>\help\samples\APISecurity\SingleSignOn`. Read the comments in the source code for more information about Single Sign-On and how the Java interface is used.

* help\samples\APISecurity\SingleSignOn\CustomHttpExternalAuthorized.java
* help\samples\APISecurity\SingleSignOn\com\example\MyExternalAuthorized.java

In that same SingleSignOn folder are several JSP pages that can be placed into the public\_html\jinfonet folder and run as web applications to exercise and demonstrate how Single Sign-On works. The file customIndex.jsp is the entry point page. It has comments inside it on how to run the demonstration.

**Notes:**

* The set of application users does not need to be the same set of users that are registered in Logi JReport Server. However, the Single Sign-On protocol does require that the application code identify the logged-in user to Logi JReport Server using a registered Logi JReport Server user name.
* When the set of application users is different from the set of Logi JReport Server users, then the application code for returning the logged-in user will need a system to map the application user to a Logi JReport Server user.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675041-SSL-Support-in-LDAP-System-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673361-Managing-Logi-JReport-Server-Guide-v15-Server)
