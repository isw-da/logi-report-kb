---
title: "Using JSP with a Dedicated Machine"
id: 1500009686342
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686342-Using-JSP-with-a-Dedicated-Machine
updated_at: 2021-11-03T06:58:33Z
---

# Using JSP with a Dedicated Machine

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712061-Creating-and-Getting-Instances)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712141-Using-RMI-in-Logi-Report-Server)

# Using JSP with a Dedicated Machine

Logi JReport Server can be configured so that JSP pages run on a web server machine while the Logi JReport Server Engine is deployed to another machine.
[In this configuration](https://devnet.logianalytics.com/hc/en-us/articles/1500009686202-Technical-Architecture#Remote), the web server machine is viewed as the client machine accessing the Logi JReport Server system.

When this configuration is used, the Java API library used on the client side is different than the one used when JSP pages run in the same JVM as Logi JReport Server. The method calls
are the same, but the library for the client provides stubs for the methods that do a Remote Method Invocation (RMI) to the remote Logi JReport Server to have the processing
performed over there. All of the classes that are needed are in `<install_root>\lib\JRSRMI.jar`.

The use of RMI as the way to obtain processing is transparent to the JSP code in the client. Developers write exactly the same code in the JSP file. At deploy time, that JSP code
will be bound to the proper library to use for the specific configuration.

Using JSPs in your web applications, the Remote Server API enables you to perform report running tasks remotely, to view the report result directly from the client side, and to administer Logi JReport Server, without having to install Logi JReport Server on the client machine.

The Report Server API is provided by the class jet.server.api.rmi. This class can be used explicitly to call methods that are specific to the configuration where RMI is used.

You can find more information about the jet.server.api.rmi package in the Logi JReport Javadoc.

Before using the Remote Server API, you must make sure that the machines have been configured properly:

1. Open the RMI service by configuration on the Logi JReport Server side.

   Set the two properties server.rmiserver.enable and server.rmiadminservice.enable to **true** in the server.properties file located in `<install_ root>\bin`.

   When Logi JReport Server resides behind a firewall, you need to specify a fixed port in order to pass through the firewall and obtain the remote objects from the client side by setting the server.rmiserver.fixed\_port property in the server.properties file.
2. Logi JReport Server remote host and port information is passed to the client application.

   Set the following parameters as the JVM environment variables in the client side:

   * Djrs.remote.host=<*HOST\_NAME/IP\_*address>
   * Djrs.remote.rmiport=<*HOST\_PORT*>
   * Djrs.rmi.auth\_file=<authFileName> (optional)

   You have two alternatives for setting these parameters:

   * You can add -Djrs.remote.host, -Djrs.remote.rmiport and -Djrs.rmi.auth\_file (optional) to the batch file that is used to start your application.
   * If you are in an integration environment, you can also add the following to the web.xml file:

     ```
     <context-param>  

         <param-name>jrs.remote.host</param-name>  

         <param-value>127.0.0.1</param-value>  

     </context-param>  

     <context-param>  

         <param-name>jrs.remote.rmiport</param-name>  

         <param-value>1129</param-value>  

     </context-param>  

     <!-- The third param(jrs.rmi.auth_file) is optional. "authFileName" includes the auth  

     file's realpath and auth file name. For example: C:\JReport\Server\bin\rmi.auth-->  

     <context-param>  

         <param-name>jrs.rmi.auth_file</param-name>  

         <param-value>C:\JReport\Server\bin\rmi.auth</param-value>  

     </context-param>  

     <listener>   

         <listener-class>jet.server.servlets.JRServerContextListener</listener-class>   

     </listener>
     ```

## Administering Logi JReport Server Remotely

Logi JReport Server can be administered from a remote client by Remote Admin Service API. The administration of a Logi JReport Server includes cluster administration, resource administration, security administration, configuration, connection pool management, resource alias management, connection information provider service, and catalog information management.

You can find the Remote Admin Service API in the jet.server.api.rmi.admin package in the Logi JReport Javadoc.

Before a Logi JReport Server can be performed the remote administration operation on, you need to set the following properties in the server.properties file located in `<install_root>\bin` on the Logi JReport Server side:

* **server.rmiserver.enable=true**  
   Used to open the RMI service.
* **server.rmiadminservice.enable=true**  
   Used to open the administration service in the RMI server. By default this property is set to false and Logi JReport Server does not support remote administration.
* **server.rmiserver.fixed\_port=<AnOpenedPort>**  
   Required when Logi JReport Server runs behind a firewall.

## Using Single Sign On in RMI Client

When using a Single Sign On (SSO) system, the web application machine is changed. This is where the work is done to set up
the Single Sign On system and where to deploy the needed class implementations of the Java interface ExternalAuthorized.

For implementation of SSO in a standalone server, follow the steps below:

1. Write your HttpExternalAuthorized implementation. For details, see [Single Sign On](https://devnet.logianalytics.com/hc/en-us/articles/1500009692762-Security-for-Accessing-Web-Pages#SSO).
2. Compile Java classes. Compiling requires the library JRESServlets.jar, which can be found in `<install_root>\lib` directory.
3. Modify the class path used by your RMI client to include your external authentication classes, so that your application of RMI can access them.

   If it is in an integration environment, you can add the authentication classes in a folder named classes in the WEB-INF folder.
4. Modify the start file of your RMI client to define the system property jrs.httpExternalAuthorized with your implementation.

   For example, assuming that the implementation of this interface is com.mycorp.HttpExternalAuthorizedImpl.class, use the command line to start the RMI client:

   `java -Djrs.httpExternalAuthorized=com.mycorp.HttpExternalAuthorizedImpl ....`

   Then, restart the RMI client.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009712061-Creating-and-Getting-Instances)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712141-Using-RMI-in-Logi-Report-Server)
