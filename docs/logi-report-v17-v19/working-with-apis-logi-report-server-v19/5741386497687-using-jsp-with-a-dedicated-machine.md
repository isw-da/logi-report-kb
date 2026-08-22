---
title: "Using JSP with a Dedicated Machine"
id: 5741386497687
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741386497687-Using-JSP-with-a-Dedicated-Machine
updated_at: 2022-10-31T17:15:48Z
---

# Using JSP with a Dedicated Machine

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400342295-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415368343-Using-RMI-in-Logi-Report-Server)

# Using JSP with a Dedicated Machine

You can configure Logi Report Server to run JSP pages on a web server computer while deploying the Logi Report Server Engine to another machine. This topic describes the combination of JSP and Remote Server API, and how you can configure the RMI service, administer Logi Report Server remotely, and implement Single Sign-on in the RMI client.

[In this configuration](https://devnet.logianalytics.com/hc/en-us/articles/5741408039575-Technical-Architecture#Remote), you use the web server computer as the client machine accessing the Logi Report Server system.
The Java API library used on the client side is different from the one used when JSP pages run in the same JVM as Logi Report Server. The method calls
are the same, but the library for the client provides stubs for the methods that do a Remote Method Invocation (RMI) to the remote Logi Report Server to have the processing
performed over there. The needed classes are in `<install_root>\lib\JRSRMI.jar`.

The use of RMI as the way to obtain processing is transparent to the JSP code in the client. Developers write exactly the same code in the JSP file. At deploy time, that JSP code
will be bound to the proper library to use for the specific configuration.

Using JSPs in your web applications, the Remote Server API enables you to perform report running tasks remotely, to view reports directly from the client side, and to administer Logi Report Server, without having to install Logi Report Server on the client machine.

You can use the Remote Server API class **jet.server.api.rmi** explicitly to call methods that are specific to the configuration where RMI is used.
For more information, see the **jet.server.api.rmi** package in the Logi Report Javadoc.

This topic contains the following sections:

* [Configuring the RMI Service](#Configure)
* [Administering Logi Report Server Remotely](#Admin)
* [Using Single Sign-on in RMI Client](#SSO)

## Configuring the RMI Service

Before using the Remote Server API, you should configure the machines properly:

1. Open the RMI service by configuration on the Logi Report Server side.

   Set the two properties **server.rmiserver.enable** and **server.rmiadminservice.enable** to **true** in the **server.properties** file located in `<install_ root>\bin`.

   When Logi Report Server resides behind a firewall, you need to specify a fixed port in order to pass through the firewall and obtain the remote objects from the client side by setting the **server.rmiserver.fixed\_port** property in the server.properties file.
2. Pass the Logi Report Server remote host and port information to the client application.

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
     file's realpath and auth file name. For example: C:\LogiReport\Server\bin\rmi.auth-->  
     <context-param>  
         <param-name>jrs.rmi.auth_file</param-name>  
         <param-value>C:\LogiReport\Server\bin\rmi.auth</param-value>  
     </context-param>  
     <listener>   
         <listener-class>jet.server.servlets.JRServerContextListener</listener-class>   
     </listener>
     ```

## Administering Logi Report Server Remotely

You can administer Logi Report Server from a remote client by Remote Admin Service API. The administration of a Logi Report Server includes cluster administration, resource administration, security administration, configuration, connection pool management, resource alias management, connection information provider service, and catalog information management.

You can find the Remote Admin Service API in the **jet.server.api.rmi.admin** package in the Logi Report Javadoc.

Before you can perform the remote administration operation on a Logi Report Server, you need to set the following properties in the **server.properties** file located in `<install_root>\bin` on the Logi Report Server side:

* **server.rmiserver.enable=true**  
   Used to open the RMI service.
* **server.rmiadminservice.enable=true**  
   Used to open the administration service in the RMI server. By default, this property is set to false and Logi Report Server does not support remote administration.
* **server.rmiserver.fixed\_port=<AnOpenedPort>**  
   Required when Logi Report Server runs behind a firewall.

## Using Single Sign-on in RMI Client

When using a Single Sign-on (SSO) system, the web application machine is changed. This is where you set up
the SSO system and where to deploy the needed class implementations of the Java interface **ExternalAuthorized**.

To implement SSO, follow the steps:

1. Write your HttpExternalAuthorized implementation. For more information, see [Single Sign-on](https://devnet.logianalytics.com/hc/en-us/articles/5741484187415-Security-for-Accessing-Web-Pages#SSO).
2. Compile Java classes. Compiling requires the library **JRESServlets.jar** in `<install_root>\lib` directory.
3. Modify the class path used by your RMI client to include your external authentication classes, so that your application of RMI can access them.

   If it is in an integration environment, you can add the authentication classes in a folder named **classes** in the WEB-INF folder.
4. Modify the start file of your RMI client to define the system property **jrs.httpExternalAuthorized** with your implementation.

   For example, assuming that the implementation of this interface is **com.mycorp.HttpExternalAuthorizedImpl.class**, use the following command line to start the RMI client:

   `java -Djrs.httpExternalAuthorized=com.mycorp.HttpExternalAuthorizedImpl ....`

   Then, restart the RMI client.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741400342295-Creating-and-Getting-Instances-of-Report-Engine-and-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415368343-Using-RMI-in-Logi-Report-Server)
