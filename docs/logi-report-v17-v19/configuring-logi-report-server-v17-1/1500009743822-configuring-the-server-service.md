---
title: "Configuring the Server Service"
id: 1500009743822
section: "Configuring Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009743822-Configuring-the-Server-Service
updated_at: 2021-07-24T00:49:26Z
---

# Configuring the Server Service

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771561-Initializing-the-Database-System-as-a-Non-admin-Database-User)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743562-Configuring-Connections)

# Configuring the Server Service

Administrators can customize the service settings of Logi Report Server, such as the ports for accessing Logi Report Server, maximum connections and handlers, and SSL connection. This topic describes how you can configure the server service and SSL for a standalone Logi Report Server.

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Configuration** > **Service** from the drop-down menu. Server displays the Service page.

   ![Service page](https://devnet.logianalytics.com/hc/article_attachments/4404880563735/config_service.gif)
2. In the **Port** text box, type an integer between 1024 and 65535 as the TCP port on which Logi Report Server listens. Usually the system reserves numbers less than 1024. Server uses 8888 as the default port.
3. In the **Maximum Number of Handlers** text box, type the maximum number of connection handlers. A connection is set up between the server-side and a client-side when a request from the client-side reaches the server. The maximum number of requests that can be handled depends on the maximum number of handlers. When there is a limit on the maximum number of connection handlers, if there are no free connection handlers available, a request from the client-side will be blocked. In which case, the request will either be handled after a connection handler has been set free or be refused when timeout occurs. A connection handler is set free after the server sends a response to a client request.
4. In the **Maximum Number of Connections** text box, type the maximum number of HTTP connections between the server-side and client-side. The maximum number of connections depends on the number of requests that can be handled. It should be larger than the maximum number of handlers. For example, if the maximum number of handlers is 10, and the maximum number of connections is 12, when the eleventh and twelfth requests come, they will be blocked until a handler has been set free. When the thirteenth request comes, it will be refused.
5. In the **Connection Timeout in** text box, type the maximum time in milliseconds for a request from a client-side to be blocked before being refused by the server. A request will be blocked if there are no free connection handlers in the server. However, it cannot be blocked forever, and if there are still no free connection handlers after the time specified here (in milliseconds), then the request will be refused back to the client.
6. ![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")Server selects **Enable Secure Socket Layer Connection** by default. It means that you can use HTTPS schema to visit the Logi Report Server UI in the standalone mode. You can configure the other SSL settings. For more information, see [Configuring SSL in Standalone Logi Report Server](#SSL).
7. The
   **Servlet Properties File Name** text box displays the full path of the property file **servlet.properties** of the servlet jet.server.servlet.JRServlet.
8. From the
   **Active Realm** drop-down list select
   the [realm](https://devnet.logianalytics.com/hc/en-us/articles/1500009749822-Managing-Realms) that will take effect when the server starts up. A realm is the context of Logi Report Server where the resources and authentication entities reside. There can be multiple realms on Server, but only one is active at runtime. You can only access the users and resources in the active realm. Realm names cannot contain the "/" or "\" character.
9. Specify whether Logi Report Server listens on all network addresses or just some, by selecting the corresponding radio button:
   * **All Network Addresses**  
      Server listens on all network addresses, which means that all the hosts of the machine are active, and the client-end can connect with any of the hosts of this server.
   * **Network Address At**  
      Select this option if you want Server to listen on the specified hosts. You can specify them by typing the host names or IP addresses. \* means all the host addresses are active. If you want more than one address to be active, separate them using a blank, for example, "leo 204.177.148.110".

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)The machine that Logi Report Server runs on can be multi-homed (for example, two interface cards have installed on the machine), if there is more than one IP address. Server opens the listening port at host name **localhost** or at IP address **127.0.0.1** automatically.

   The **Active Host Address** box lists the current active hosts' addresses.
10. Select **Save** to apply the changes.
11. Restart Server to make the settings take effect.

## Configuring SSL in Standalone Logi Report Server

Logi Report Server supports HTTPS requests in standalone mode. Secure port for HTTPS requests should use different port from non-secure port for HTTP requests. By default, port 6888 is set as the secure port for accessing the Server Console. The URL for visiting Logi Report Server via HTTPS schema is like this:

`https://IP_address or localhost:6888`

![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")Server enables SSL support by default. However, you still need to configure other settings in order to use HTTPS schema to visit Logi Report Server UI. You can achieve this either in the Server Console as an administrator or using the **server.properties** file in the `<install_root>\bin` directory.

Logi Report Server Monitor does not support SSL.

**To configure the SSL feature via the Server Console:**

1. Point to **Administration** on the system toolbar, and then select **Configuration** > **Service** from the drop-down menu. Server displays the Service page.
2. ![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")By default, Server selects the **Enable Secure Socket Layer Connection** option.
3. In the **Secure Port**
   text box, type a
   port for visiting the Server Console via HTTPS schema. It should be different from the Port for HTTP schema.
4. In the **Keystore File Path** text box, type the location of your trusted keystore file.

   Logi Report provides a self-signed keystore file `<install_root>/bin/keystore` for evaluation purpose. You need to replace it with your trusted keystore file since Logi Report is not a trusted certificate authority. There are many trusted authorities that can provide keystore files. Select the following link to see an example of creating a keystore file: <http://docs.oracle.com/cd/E19509-01/820-3503/ggsxx/index.html>.
5. In the **Keystore Password** text box, type the password for protecting the integrity of the keystore.
6. From the
   **Keystore Type**
   drop-down list, select
   the type of keystore to instantiate: **JKS** or **PKCS12**.
7. Select
   the encryption/decryption protocol to use on the socket from the
   **Keystore Protocol**
   drop-down list.
   The valid values are **SSL** and **TLS**.
8. Select
   the X509 algorithm to use from the
   **Keystore Algorithm** drop-down list. This defaults to the Sun implementation (**SunX509**). For IBM JVMs you should use **IBMX509**.
9. Select **Save**.
10. Restart Server in order for the settings to take effect.

**To configure the SSL feature in the server.properties file:**

1. Open the **server.properties** file in the `<install_root>\bin` directory.
2. ![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")By default, **httpserver.ssl.enable** is **true**.
3. Set the other properties starting with httpserver.ssl to meet your requirements.
4. Save the file.
5. Restart Server in order for the settings to take effect.

### Multiple SSL Certificate Support

When accessing Logi Report Server by domain names via HTTPS, you can apply different SSL certificates for different domain names. You can use a configuration file **httpsCertificateMapping.xml** for defining the mapping relationship between domains and certificate aliases. You should create the file manually and put it in the `<install_root>\bin` folder.

The following is a sample of the httpsCertificateMapping.xml file. It defines three groups of mapping relationship: www.a.com maps to certificate alias A, www.b.com maps to certificate alias B, and www.example.com and www.example.org map to certificate alias C.

```
<?xml version="1.0"  encoding="UTF-8" standalone="yes"?>  
    <httpsCertificateMapping>  
        <certificateMapping>  
        <description>www.a.com</description>  
        <certificateAlias>A</certificateAlias>  
        <domainPattern>www\.a\.com</domainPattern>  
        </certificateMapping>  
        <certificateMapping>  
        <description>www.b.com</description>  
        <certificateAlias>B</certificateAlias>  
        <domainPattern>www\.b\.com</domainPattern>  
        </certificateMapping>  
        <certificateMapping>  
            <description>www.example.com/www.example.org</description>  
            <certificateAlias>C</certificateAlias>  
            <domainPattern>www\.example\.(com|org)</domainPattern>  
    </certificateMapping>  
</httpsCertificateMapping>
```

See the details about the elements in the file:

* **httpsCertificateMapping**: The
  root element.
* **certificateMapping**: One mapping relationship between certificate alias and domain name.
* **description**: Optional. The description about the mapping.
* **certificateAlias**: The alias of the certificate defined in the keystore file.
* **domainPattern**: A domain name pattern.

When an HTTPS request comes in, Logi Report Server first checks the domain name input in the browser. If the domain name matches domainPattern of a certificateMapping in httpsCertificateMapping.xml, the corresponding cerificateAlias will be used to get the certificate from the keystore, and then the certificate will be applied. If no matched domainPattern is found or no certificate is got, the first certificate in the keystore will be applied.

To apply different certificates to multiple domain names, take the following steps:

1. Make sure Logi Report Server starts by JDK 8.
2. [Configure SSL](#SSL) on Logi Report Server.
3. Generate a keystore file which contains multiple entities (each entity contains a certificate and has an alias).
4. Set the keystore file name as the value of the **httpserver.ssl.keystore** property in server.properties in `<install_root>\bin`.
5. Create the file **httpsCertificateMapping.xml** in the `<install_root>\bin` folder. In the file, specify mapping relationship between domains and certificate aliases defined in the keystore file.
6. Restart Logi Report Server. Then when accessing Logi Report Server using different domain name, the corresponding certificate will be applied.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009771561-Initializing-the-Database-System-as-a-Non-admin-Database-User)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009743562-Configuring-Connections)
