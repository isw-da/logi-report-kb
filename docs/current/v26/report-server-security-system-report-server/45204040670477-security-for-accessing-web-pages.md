---
title: "Security for Accessing Web Pages"
id: 45204040670477
section: "Report Server Security System Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204040670477-Security-for-Accessing-Web-Pages
updated_at: 2026-04-30T14:10:54Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Security for Accessing Web Pages

This topic introduces the web page security mechanism of Report Server, how to use Single Sign-on, and how to configure HTTP Security Response Headers. 

Report Server provides a working web application as part of the product mix. This web application is implemented as a group of JSP pages and servlets that run in a Java web server's servlet container. Report Server controls access to these JSP pages and servlets by requiring a user to sign in to a web session before the JSP pages or servlets run.

The security framework of Report Server also enables Single Sign-on so that a user only needs to sign in to an existing application and need not to do another signing in to access the Report Server web pages.

This topic contains the following sections:

- Web Page Security

- Single Sign-on
                

- 
Built-in Single Sign-on

- Configuring HTTP Security Response Headers

- Handling Preflight Requests to JSP Pages                

## 
Web Page Security

Report Server provides a working set of JSP pages and servlets that form a web application to perform actions such as scheduling and running reports and viewing results. This web application is only available to registered users who identify themselves and sign in to Report Server. An administrator can register users, set passwords for them, associate them with groups and roles, and grant them permissions, which is necessary for accessing the resources on Report Server. This database of user information is used to validate the username and password that is used to sign in to the web application.

The sample in <install_root>\help\samples\APISecurity\LoginLogout can help you learn about web page security. It contains a set of JSP pages that can run to try out various styles of accessing a JSP page to see how the signing in mechanics work. The entry point to the set of JSP pages is loginIndex.jsp. Read the comments in the JSP pages to understand how to run the demonstration.

The following describes how Report Server processes the web page security check. 

Only signed-in users may access the web pages

When accessing Report Server users should first sign in. Once a user signs in to the web application the user can access the web pages.

Each JSP page and servlet in the web application starts off with code that checks if the current HTTP Request is from a user who already signed in. If it is, the rest of the code runs because this user is a known user. There may be more permission checks within the code to control the specific request, but the user is allowed to access the web page. 

If the current HTTP Request is not from a user who already signed in, then the code attempts to sign in the user using information available in the current HTTP Request, which may come from the following:

- An external service
    When no current user signed in, Report Server will make a call to an external helper class method, asking it to return the User ID to use. If the method call returns a User ID, Report Server will validate if the User ID is registered on the server, and if it is, it will sign that user in. This is called Single Sign-on.

- A proprietary protocol based on authentication properties in the URL
    When no current user signed in, Report Server looks for specific authentication properties that it has designated as a way to pass in signing in credentials in the URL. If these authentication properties exist, Report Server will use their value and try to sign in the identified user. If the credentials are valid, then the user can sign in and access the web page. Later HTTP Requests from that user will show that the user already signed in.

If it is not possible to sign in a user, then the code recognizes that it is an unauthorized request and does not allow the rest of the code to run. It may send back a response to pop up the signing in dialog box on the browser or may do something else depending on the SSO implementation.

Validation of users during signing in

When obtaining the username and password, Report Server will validate if the signing in credentials match a Report Server user. The built-in system for doing this looks at the information for the set of users that are registered in Report Server. It validates whether the password is correct for the given username.

Report Server also defines the Java interface AuthenticationProvider that developers can implement to do the validation using an application's user database. For more information, see Customized Implementation of the Security API.

Permission control

Once a web page is deemed accessible following the rules for signing in and validation, the JSP page or servlet is allowed to run. However, it may be that the signed-in user does not have permission to do the requested operation or have rights for the target resource of the operation. This aspect of whether the user is authorized for the request is determined by Report Server evaluating the permission information.

For developer users Report Server also defines the Java interface AuthorizationProvider that they can implement to replace the built-in system for evaluating permissions and determining authorization. For more information, see Customized Implementation of the Security API.

## 
Single Sign-on

Report Server's web pages are built to work with an existing web application. In particular, it is possible to set up the web server so that users of the website can sign in to an existing web application and have that signing in grant them access to the Report Server web pages. This is called the Single Sign-on (SSO) feature.

To achieve SSO, developers can implement the class defined by the Report Server Java interface HttpExternalAuthorized and tell Report Server to use that implementation. The implementation can be aware of the application's technique for managing signing in state in the servlet session. This code can tell Report Server which user has signed in. The implementation can redirect the user to the application's signing in workflow if the request is not from a signed-in user.

This system gives the user one spot in the application to sign in. Successfully signing in there will allow the user to run Report Server web pages without doing another signing in dialog box.

Report Server is told to use the local implementation of ExternalAuthorized in two ways.

- 
Using the command line to define a system property that registers the classYou can use the system property jrs.httpExternalAuthorized to hold the name of the class that implements HttpExternalAuthorized.

If the name of the class is DemoExternalAuthorized.java, then change the script file that starts up Report Server to include the parameter string: -Djrs.httpExternalAuthorized=DemoExternalAuthorized. 

Example 1: A simple example of retrieving username from the database server

- Create a table by DDL in the database:
          CREATE TABLE jr_auth(auth_key varchar(64), auth_uid varchar(256) NOT NULL, PRIMARY KEY(auth_key))

Insert testing data for an example:

insert into jr_auth (auth_key, auth_uid) values('987654321', 'admin');

Tip: jr_auth includes the inserted/updated data. auth_uid should be a Report Server username (the user who signed in).

- Configure the database connection in databaseCfg.ini located in the sub-directory config\ of the DemoExternalAuthorized class. The default path is <server_install_root>\help\samples\APISecurity\SSO\config.
        driver=com.mysql.jdbc.Driver
dbUrl=jdbc:mysql://IP_Address:3306/test
dbUser=root
dbPassword=1234

- Extract compile_tool.zip in <server_install_root>\help\samples\APISecurity\SSO to the same directory as DemoExternalAuthorized.java. Choose a compile tool according to your operating system, compile_tool.bat for Windows or compile_tool.sh for UNIX. Configure the arguments in the corresponding file based on your environment, then double-click the file to start compiling the Java code DemoExternalAuthorized.java.

- Download the JDBC driver required in this example, mysql-connector-java-5.1.7-bin.jar, from the MySQL website, and put it to <server_install_root>\help\samples\APISecurity\SSO\lib.

- Modify the Report Server start shell script JRServer.bat in <server_install_root>\bin to add the following in the class path:
        
- The JDBC driver, for example, C:\LogiReport\Server\help\samples\APIsecurity\SSO\lib\mysql-connector-java-5.1.7-bin.jar. 

- The absolute path of the directory that contains all the SSO implementaion files, for example, C:\LogiReport\Server\help\samples\APISecurity\SSO\

- The JVM option -Djrs.httpExternalAuthorized=DemoExternalAuthorized

The class DemoExternalAuthorized in the example implements the interface HttpExternalAuthorized. Once the class has loaded, after Report Server starts up you will get the following message in its console window: DemoExternalAuthorized class is loaded. If you want to edit the authorization method, you just need to edit the method getExternalAuthorizedUser in DemoExternalAuthorized.

- You can change the web page that Report Server displays after signing in, by changing the URL under the sentence "Which web page do you want to visit after login?" in ssodemo.jsp in <server_install_root>\help\samples\APISecurity\SSO.
        

- Move ssodemo.jsp to the public_html folder in the Report Server root directory.

- Start Report Server by running JRServer.bat. 

- Access ssodemo.jsp and pass the parameters jrauth_key and jrauth_id from other pages. 

- Test the SSO demo using login.html in <server_install_root>\help\samples\APISecurity\SSO.
        

Tip: Do not modify the two parameter names when using ssodemo.jsp we provided, or there will be exceptions. If you need to modify the parameter names, change them in all the three files: login.html, ssodemo.jsp, and DemoExternalAuthorized.java. 

Example 2: An example of retrieving username from the SSO server 

The demo SSO implementation DemoSSO.java for this example is in <server_install_root>\help\samples\APISecurity\SingleSignOn\Example2. In order for it to work, modify the Report Server start shell script JRServer.bat in <server_install_root>\bin to add the following in the class path: 

- The absolute path of the directory that contains the demo SSO implementation files: <server_install_root>\help\samples\APISecurity\SingleSignOn\Example2\

- The JVM option -Djrs.httpExternalAuthorized=DemoSSO

The SSO code logic is: 

- Receive token from customer application incoming HTTP request, for example auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NzksImV4cCI6MTU0NDY0NTUzOS4wLCJjbGFpbXMiOiJDYW5BY2Nlc3NDb3Vyc2VDYXRhbG9nLENhbkFjY2Vzc1VzZXJzLENhbk1vZGlmeUFjY291bnRTZXR0aW5ncyxDYW5Nb2RpZnlBc3NpZ25tZW50cyxDYW5Nb2RpZnlBdXRvbWF0aWNBc3NpZ25tZW50cyxDYW5Nb2RpZnlCaWxsaW5nSW5mb3JtYXRpb24sQ2FuTW9kaWZ5Q3VzdG9tQ291cnNlcyxDYW5Nb2RpZnlDdXN0b21GaWVsZHMsQ2FuTW9kaWZ5U2Vzc2lvbnMsQ2FuTW9kaWZ5R3JvdXBzLENhbk1vZGlmeU11bHRpcGxlVXNlcnMsQ2FuTW9kaWZ5UmVwb3J0cyxDYW5Nb2RpZnlVc2VycyJ9.xqQgiVFhrujJskkjjbgPrvey8gZa2if1QSfgKTMib-gReceive lms-url (host variable) from incoming HTTP request, too. For example, lms-url=Report.inclassnow.info

- Pass token to customer's end point for validation check.
      Request URL: https://{lms-url}/self/claims
Request Method: GET
content-type: application/json; charset=utf-8
Headers:
authorization: bearer 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE5NzksImV4cCI6MTU0NDY0NTUzOS4wLCJjbGFpbXMiOiJDYW5BY2Nlc3NDb3Vyc2VDYXRhbG9nLENhbkFjY2Vzc1VzZXJzLENhbk1vZGlmeUFjY291bnRTZXR0aW5ncyxDYW5Nb2RpZnlBc3NpZ25tZW50cyxDYW5Nb2RpZnlBdXRvbWF0aWNBc3NpZ25tZW50cyxDYW5Nb2RpZnlCaWxsaW5nSW5mb3JtYXRpb24sQ2FuTW9kaWZ5Q3VzdG9tQ291cnNlcyxDYW5Nb2RpZnlDdXN0b21GaWVsZHMsQ2FuTW9kaWZ5U2Vzc2lvbnMsQ2FuTW9kaWZ5R3JvdXBzLENhbk1vZGlmeU11bHRpcGxlVXNlcnMsQ2FuTW9kaWZ5UmVwb3J0cyxDYW5Nb2RpZnlVc2VycyJ9.xqQgiVFhrujJskkjjbgPrvey8gZa2if1QSfgKTMib-g
Response:
{"accountId":501,"userId":1979,"claims":["CanAccessCourseCatalog","CanAccessUsers","CanManageAllUsers","CanModifyAccountSettings","CanModifySessions","CanModifyGroups","CanModifyMultipleUsers","CanModifyReports","CanModifyUsers"]}	

- Receive returning JSON string as above and parse the accountId and userId out.

- Check received userId in our system to see whether this username exists in Report Server.
 If it exists, we can move on.
 However, if it does not exist, we need to add this userId as our username in Report, create a group named accountId, add this user to the accountID group, and add the user to at least the "everyone" role.

- Check whether there is a subfolder named accountId under the root node in the server resource tree. If the folder is there, move on. If the folder is not there yet, create that folder and set the permission that only the same accountID and userID can access this folder.

- Set accountId as a parameter in our session variable.

- Return userId and exit from SSO code.

- 
Using a Java API method call to register the classThe Java API class HttpUserSessionManager has a method for setting the ExternalAuthrized object that Report Server uses.

If the name of the package is com.mycorp.myHttpExternalAuthorized, then in a JSP page, connect to Report Server, then pass an instance of the class object for myHttpExtneralAuthorized
 as the parameter in the method HttpUserSessonManager.setHttpExternalAuthorized().

<%@ page import="com.example.MyHttpExternalAuthorized" %>
				
        // initialize and connect to Report Server
    initEnv(System.getProperties());
    HttpRptServer httpRptServer = HttpUtil.getHttpRptServer(request);
        // set the HttpExternalAuthorized object used by Report Server
    HttpUserSessionManager    hsm  = (HttpUserSessionManager)httpRptServer.getHttpUserSessionManager();
    hsm.setHttpExternalAuthorized(new DemoExternalAuthorized());

There are examples of implementations of the Java interface ExternalAuthorized in the sample source files that come with Report Server. Look in the folder <install_root>\help\samples\APISecurity\SingleSignOn. Read the comments in the source code for more information about SSO and how to use the Java interface.

- help\samples\APISecurity\SingleSignOn\CustomHttpExternalAuthorized.java

- help\samples\APISecurity\SingleSignOn\com\example\MyExternalAuthorized.java

In that same SingleSignOn folder are several JSP pages that you can place into the public_html\jinfonet folder and run as web applications to exercise and demonstrate how SSO works. The file customIndex.jsp is the entry point page. It has comments inside it on how to run the demonstration.

## 
Built-in Single Sign-on

From version 24.3.3, standalone servers have built-in single sign-on (SSO) by default, handling common scenarios without needing custom SSO code.

- Create new user

- Create orgnaizaton/role/group which loggin user belongs

- Assign permission to user/role/group on certain resource

- Setup session variable

To configure SSO behavior with the built-in SSO, customers can call the POST /sso/register and POST /sso/token web API endpoints.

Example 1: Create user and pass authorization in url

- Start the server, log in as an admin, and call the POST /sso/register web API endpoint. Provide the following details in ssoRegisterInfo:         
           {	
				"name": "eval",
				"onetime": false,
				"expiration": 5184000
				}

- 
Call the POST /sso/token web API endpoint without a logged-in user. The ssoTokenInfo should include register_id and register_secret obtained from the previous step.

{
				"register_id": "9016f100-6cbc-4228-abcb-6bbf98a34c33",
				"register_secret": "07822207920939b23c1368ddb2ec4ef1074e8634",
				"expiration": 5184000,
	        	        "username": "testuser2",
				"principals": {
				"users": [
			"testuser3"
				]
				"roles": [
				"testrole1"
				],
				"groups": [
			"testgroup1"
				]
				}
				"permissionSetting": [
			{
			     "path": "/",
			     "permissions": {
		    	      "forRoles": [
				{
				  "name": "testrole1",
			          "permissions": "0001100010"			
				}
			       ]
			         }
			      }
		         ]
			}
							

- Send the url that contains returned token to run the report and get the report: http://localhost:8888/jinfonet/runReport.jsp?jrs.cmd=jrs.web_vw&jrs.report=/SampleReports/Employee%20Information%20List.cls&jrs.catalog=/SampleReports/SampleReports.cat&jrs.result_type=2&jrs.authorization=eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoidGVzdHVzZXIyIiwia2V5IjoiMmVmZjcwODQtOTRjOS00MGVkLWEwMzQtNmM0NWY4MjZhMWIzIiwiaXNzIjoibG9naXJlcG9ydCIsImV4cCI6MTczOTg1MTcyM30.Y5Z719C_nX14sqwZpzb5zZWuUaKa-j0g2qLFJIj9slU

Example 2: create organization user and pass authorization info in header

- Login with admin user, create new organizaton orgB, publish demo reports to Organization Reports.

- Call web api endpoint POST /sso/token without any logged in user, ssoTokenInfo is as follows, regisert_id and register_secret are gotten from response of step 1 in example1:
          {
				"register_id": "9016f100-6cbc-4228-abcb-6bbf98a34c33",
				"register_secret": "07822207920939b23c1368ddb2ec4ef1074e8634",
				"expiration": 5184000,
				"username": "testB\testuser1",
				"principals": {
				"users": [
				"testB\testuser2"
			],
			"roles": [
				"testB\testrole1"
				],
				"groups": [
				"testB\testgroup1"
				]
				},
				"permissionSetting": [
				{
				"path": "/<testB>/",
				"permissions": {
				"forGroups": [
				{
				"name": "testB\testgroup1",
				"permissions": "0001100010"
				}
				]
				}
				}
				]
				}

- Open postman, put url into address bar: http://localhost:8888/jinfonet/runReport.jsp?jrs.cmd=jrs.web_vw&jrs.report=/<testB>/SampleReports/Employee%20Information%20List.cls&jrs.catalog=/<testB>/SampleReports/SampleReports.cat&jrs.result_type=2 and set returned token of POST /sso/token call to header “Authorization”, ensure "Automatically follow redirects" is on, click "Send and Download", generated pdf result is downloaded correctly

## 
Configuring HTTP Security Response Headers

There are many HTTP security headers you can utilize to provide the necessary protection for your Report Server JSPs and servlets that respond to browser requests in a standalone environment, like HTTP Strict Transport Security (HSTS), X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, and Content-Security-Policy. Since different users may choose different response headers for security, Report provides a configuration file which enables you to configure the security response headers all by yourselves. The configuration file is responseHeaders.properties in the <install_root>\bin directory. You can set the security header name/value pairs in the file according to your security policy. You can write a name/value pair as either "Name=Value" or "Name: Value". See two examples: 

- X-Content-Type-Options=nosniff
Content-Security-Policy=script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; worker-src blob:; report-uri http://localhost:8888/demo/cspReport.jsp
X-XSS-Protection=1; mode=block

- X-Content-Type-Options: nosniff
Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; worker-src blob:; report-uri http://localhost:8888/demo/cspReport.jsp
X-XSS-Protection: 1; mode=block

- The set of application users does not need to be the same set of users that are registered in Report Server. However, the SSO protocol does require that the application code identify the signed-in user to Report Server using a registered Report Server username.

- When the set of application users is different from the set of Report Server users, the application code for returning the signed-in user needs a system to map the application user to a Report Server user.

## 
Handling Preflight Requests to JSP Pages

Standalone server can correctly process CORS preflight requests (HTTP OPTIONS requests) that are sent to JSP pages.

- When a browser sends a preflight request before invoking a JSP, our product will recognize and handle it according to the CORS specification.

- The response will include the necessary Access-Control-Allow-* headers (such as Access-Control-Allow-Origin, Access-Control-Allow-Methods, and Access-Control-Allow-Headers) so that the subsequent actual request to the JSP can proceed without issues.

- This ensures that JSP endpoints in your application remain accessible to cross-origin requests while still adhering to security standards.

- response header Access-Control-Allow-Headers can be configured in responseHeaders.properties.

- response header Access-Control-Allow-Origin can be configured in responseHeaders.properties, and new jvm system property -Djreport.cors.allowed_origins is introduced to list accepted origins. setting in responseHeaders.properties will be ignored when -Djreport.cors.allowed_origins set.

Preflight requests do not execute JSP business logic or return the JSP content. They only serve to validate whether the actual cross-origin request is allowed.
