---
title: "Configuring the Server Service"
id: 1500009669221
section: "Configuring Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009669221-Configuring-the-Server-Service
updated_at: 2021-07-24T20:55:19Z
---

# Configuring the Server Service

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644462-Configuring-JdbcDriversConfig-properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644422-Configuring-Connections)

# Configuring the Server Service

Administrators can customize the service settings of Logi JReport Server, such as the ports for accessing Logi JReport Server, maximum connections and handlers, SSL connection and so on.

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar and select **Service** from the drop-down menu. The Configuration - Service page is displayed.

   ![Configuration - Service page](https://devnet.logianalytics.com/hc/article_attachments/4404926781719/config_service.gif)
2. In the Port text box, input a port as the TCP port on which Logi JReport Server listens. The port can be an integer between 1 and 65535. However, numbers less than 1024 are usually reserved by system, and so numbers larger than 1024 are preferred. Logi JReport Server uses 8888 as the default port.
3. In the Dashboard Port text box, input a port for accessing JDashboard. The default JDashboard port is 8887.
4. In the Administration Port text box, input a port used for remote administration. If Logi JReport Server is running as a standalone web server, the administrator can specify the port for client users to configure and administer the server remotely. This port is where the servlet for remote administration (jet.server.servlets.RcServlet) listens. The default administration port is 8889.
5. In the Maximum Number of Handlers text box, input the maximum number of connection handlers. A connection is set up between the server-side and a client-side when a request from the client-side reaches the server. The maximum number of requests that can be handled depends on the maximum number of handlers. When there is a limit on the maximum number of connection handlers, if there are no free connection handlers available, a request from the client-side will be blocked. In which case, the request will either be handled after a connection handler has been set free, or be refused when timeout occurs. A connection handler is set free after the server sends a response to a client request.
6. In the Maximum Number of Connections text box, input the maximum number of HTTP connections between the server-side and client-side. The maximum number of connections depends on the number of requests that can be handled. It should be larger than the maximum number of handlers. For example, if the maximum number of handlers is 10, and the maximum number of connections is 12, when the eleventh and twelfth requests come, they will be blocked until a handler has been set free. When the thirteenth request comes, it will be refused.
7. In the Connection Timeout in text box, input the maximum time in milliseconds for a request from a client-side to be blocked before being refused by the server. A request will be blocked if there are no free connection handlers in the server. However it cannot be blocked forever, and if there are still no free connection handlers after the time specified here (in milliseconds), then the request will be refused back to the client.
8. Check **Enable Secure Socket Layer Connection** if you want to use HTTPS schema to visit the Logi JReport Server UI in the standalone mode, then specify the other settings as required. For more information select [here](#SSL).
9. The
   Servlet Properties File Name text box displays the full path of the property file of the servlet jet.server.servlet.JRServlet. Assuming that Logi JReport Server has been installed to `C:\Logi JReport\Server`, the servlet property file is `C:\Logi JReport\Server\bin\servlet.properties`.
10. From the
    Active Realm drop-down list select
    the [realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009675001-Managing-Realms) that will take effect when the server starts up. A realm is the context of Logi JReport Server where the resources and authentication entities reside. There can be multiple realms in the server, but only one is active at runtime. Only the users and resources in the active realm are accessible. Realm names cannot contain the "/" or "\" character.
11. Specify whether Logi JReport Server listens on all network addresses or just some by selecting the corresponding radio button:
    * **All Network Addresses**  
       If selected,
      Logi JReport Server listens on all network addresses, which means that all the hosts of the machine are active, and the client-end can connect with any of the hosts of this server.
    * **Network Address At**  
       If
      selected, Logi JReport Server listens on the specified hosts, and you can specify them by inputting the host names or IP addresses. If you want to specify all the host addresses to be active, input \* into this field; if you want to specify more than one address to be active, you should separate them using a blank, for example, "leo 204.177.148.110".

    **Note:** The machine that Logi JReport Server runs on can be multi-homed (for example, two interface cards have been installed on the machine), if there is more than one IP address. Logi JReport Server opens the listening port at host name 'localhost' or at IP address '127.0.0.1' automatically.

    The Active Host Address box lists the current active hosts' addresses.
12. Select **Save** to apply the changes.
13. Restart Logi JReport Server to make the settings take effect.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Enabling SSL in Standalone Logi JReport Server

Logi JReport Server supports HTTPS requests in standalone mode. Secure ports for HTTPS requests should use different ports from non-secure ports for HTTP requests. By default, port 6888 and 6889 are set as the secure ports separately for accessing the Logi JReport Console UI and Logi JReport Administration UI. The URL for visiting Logi JReport Server via HTTPS schema is like this:

`https://IP_address or localhost:6888`

SSL support is disabled by default. You need to enable it and configure corresponding settings in order to use HTTPS schema to visit Logi JReport Server UI. This can be done either on the Logi JReport Administration page or in the server.properties file located in the `<install_root>\bin` directory.

**To enable the SSL feature via the administration UI:**

1. On the Configuration - Service page, check the **Enable Secure Socket Layer Connection** option.
2. In the Secure Port
   text box, input a
   port used for visiting Logi JReport Console page via HTTPS schema. It should be different from the Port for HTTP schema.
3. In the
   Dashboard Secure Port text box, input a
   port
   used for visiting JDashboard page via HTTPS schema. It should be different from the Dashboard Port for HTTP schema.
4. In the
   Secure Administration Port text box, input a
   port
   used for visiting Logi JReport Administration page via HTTPS schema. It should be different from the Administration Port for HTTP schema.
5. In the
   Keystore File Path text box, input
   the location of your trusted keystore file.
6. In the Keystore Password text box, input the password used to protect the integrity of the keystore.
7. Select
   the type of keystore to be instantiated from the
   Keystore Type
   drop-down list. The valid values are JKS and PKCS12.
8. Select
   the encryption/decryption protocol to be used on the socket from the
   Keystore Protocol
   drop-down list.
   The valid values are SSL and TLS.
9. Select
   the X509 algorithm to use from the
   Keystore Algorithm drop-down list. This defaults to the Sun implementation (SunX509). For IBM JVMs you should use IbmX509.
10. Select **Save** on the page, then restart Logi JReport Server in order for the settings to take effect.

**To enable the SSL feature in the server.properties file:**

1. Open the server.properties file located in the `<install_root>\bin` directory.
2. Set httpserver.ssl.enable to **true**.
3. Set the other [properties starting with httpserver.ssl](https://devnet.logianalytics.com/hc/en-us/articles/1500009668861-Appendix-2-Properties-in-server-properties#ssl) to meet your requirements.
4. Save the file, then restart Logi JReport Server in order for the settings to take effect.

**Notes:**

* Logi JReport does not provide a keystore file since Jinfonet is not a trusted certificate authority and just provides a Keystore File Path option for you to configure the location of your trusted keystore file. There are many trusted authorities that can provide keystore files. Here is an example of creating a keystore file: <http://docs.oracle.com/cd/E19509-01/820-3503/ggsxx/index.html>.
* Logi JReport Server Monitor does not support SSL.

### Multiple SSL Certificate Support

When accessing Logi JReport Server by domain names via HTTPS, you can apply different SSL certificate for different domain name. A configuration file httpsCertificateMapping.xml is used for defining the mapping relationship between domains and certificate aliases. You should create the file manually and put it in the `<install_root>\bin` folder.

The following is a sample of the httpsCertificateMapping.xml file. It defines three groups of mapping relationship: www.a.com maps to certificate alias A, www.b.com maps to certificate alias B, and www.example.com and www.example.org map to certificate alias C.

|  |
| --- |
| ``` <?xml version="1.0"  encoding="UTF-8" standalone="yes"?> <httpsCertificateMapping>  <certificateMapping>     <description>www.a.com</description>     <certificateAlias>A</certificateAlias>     <domainPattern>www\.a\.com</domainPattern>   </certificateMapping>   <certificateMapping>     <description>www.b.com</description>     <certificateAlias>B</certificateAlias>     <domainPattern>www\.b\.com</domainPattern>   </certificateMapping>   <certificateMapping>     <description>www.example.com/www.example.org</description>     <certificateAlias>C</certificateAlias>     <domainPattern>www\.example\.(com|org)</domainPattern>   </certificateMapping>  </httpsCertificateMapping> ``` |

Below are details about the elements in the file:

* **httpsCertificateMapping**: The
  root element.
* **certificateMapping**: Represents one mapping relationship between certificate alias and domain name.
* **description**: Optional. The description about the mapping.
* **certificateAlias**: The alias of the certificate defined in the keystore file.
* **domainPattern**: Represents a domain name pattern.

When an HTTPS request comes in, Logi JReport Server first checks the domain name input in the browser. If the domain name matches domainPattern of a certificateMapping in httpsCertificateMapping.xml, the corresponding cerificateAlias will be used to get the certificate from the keystore, and then the certificate will be applied. If no matched domainPattern is found or no certificate is got, the first certificate in the keystore will be applied.

To apply different certificates to multiple domain names, take the following steps:

1. Make sure Logi JReport Server is started by JDK 8 or a higher JDK version.
2. [Enable SSL](#SSL) on Logi JReport Server.
3. Generate a keystore file which contains multiple entities (each entity contains a certificate and has an alias). Then set the keystore file name as the value of the httpserver.ssl.keystore property in server.properties in `<install_root>\bin`.
4. Create the file httpsCertificateMapping.xml in the `<install_root>\bin` folder. In the file specify mapping relationship between domains and certificate aliases defined in the keystore file.
5. Restart Logi JReport Server. Then when accessing JRepor Server using different domain name, the corresponding certificate will be applied.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009644462-Configuring-JdbcDriversConfig-properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644422-Configuring-Connections)
