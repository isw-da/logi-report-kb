---
title: "Configuring the Server Service"
id: 45203898468109
section: "Configuring Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203898468109-Configuring-the-Server-Service
updated_at: 2026-04-30T14:08:04Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Configuring the Server Service

Administrators can customize the service settings of Report Server, such as the ports for accessing Server, maximum connections and handlers, and SSL connection. This topic describes how you can configure the server service and SSL for a standalone Report Server.

- On the system toolbar of the Server Console, navigate to Administration > Configuration > Service. Server displays the Service page.
    

- In the Port text box, type an integer between 1024 and 65535 as the TCP port on which Report Server listens. Usually, the system reserves numbers less than 1024. Server uses 8888 as the default port.

- In the Maximum Number of Handlers text box, type the maximum number of connection handlers. Report sets up a connection between Server and the client when a request from the client reaches Server. The maximum number of requests that Server can handle depends on the maximum number of handlers. When there is a limit on the maximum number of connection handlers, if there are no free connection handlers available, Server will block a request from the client. In which case, Server will either handle the request after a connection handler becomes free or refuse it when timeout occurs. Server sets a connection handler free after sending a response to a client request.

- In the Maximum Number of Connections text box, type the maximum number of HTTP connections between Server and the client. The maximum number of connections depends on the number of requests that Server can handle. It should be larger than the maximum number of handlers. For example, if the maximum number of handlers is 10, and the maximum number of connections is 12, when the 11th and 12th requests come, Server blocks them until a handler becomes free. When the thirteenth request comes, Server refuses it.

- In the Connection Timeout in text box, type the maximum time in milliseconds for Server blocking a request from the client before refusing it. Server will block a request if there are no free connection handlers. However, the block cannot last forever, and if there are still no free connection handlers after the time you specified here (in milliseconds), then Server refuses the request back to the client.

- Server selects Enable Secure Socket Layer Connection by default. It means that you can use HTTPS schema to visit the Server UI in the standalone mode. You can configure the other SSL settings. For more information, see Configuring SSL in Standalone Report Server. 

- The 
 Servlet Properties File Name text box displays the full path of the property file servlet.properties of the servlet jet.server.servlet.JRServlet.

- From the 
 Active Realm list select
 the realm that will take effect when Server starts up. A realm is the context of Server where the resources and authentication entities reside. There can be multiple realms on Server, but only one is active at runtime. You can only access the users and resources in the active realm. Realm names cannot contain the "/" or "\" character.

- Specify whether Server listens on all network addresses or just some, by selecting the corresponding choice:
    
- 
All Network Addresses
 Server listens on all network addresses, which means that all the hosts of the machine are active, and the client can connect with any of the hosts of this server.

- 
Network Address At
        Select this option if you want Server to listen on the specified hosts. You can specify them by typing the host names or IP addresses. * means all the host addresses are active. If you want more than one address to be active, separate them using a blank, for example, "leo 204.177.148.110".

 The computer that Server runs on can be multi-homed (for example, two interface cards have installed on the computer), if there is more than one IP address. Server opens the listening port at host name localhost or at IP address 127.0.0.1 automatically.

The Active Host Address box lists the current active hosts' addresses.

- Select Save to apply the changes. 

- Restart Server to make the settings take effect.

## 
Configuring SSL in Standalone Report Server

Report Server supports HTTPS requests in standalone mode. Secure port for HTTPS requests should use different port from non-secure port for HTTP requests. By default, port 6888 is the secure port for accessing the Server Console. The URL for visiting Server via HTTPS schema is like this:

https://IP_address or localhost:6888

Server enables SSL support by default. However, you still need to configure other settings in order to use HTTPS schema to visit Server UI. You can achieve this either on the Server Console as an administrator or using the server.properties file in the <install_root>\bin directory. 

Server Monitor does not support SSL.

To configure the SSL feature via the Server Console:

- On the system toolbar, navigate to Administration > Configuration > Service. Server displays the Service page.

- By default, Server selects Enable Secure Socket Layer Connection.

- In the Secure Port
 text box, type a 
 port for visiting the Server Console via HTTPS schema. It should be different from the port for HTTP schema. 

- In the Keystore File Path text box, type the location of your trusted keystore file. 
			Report provides a self-signed keystore file <install_root>/bin/keystore for evaluation purpose. You need to replace it with your trusted keystore file since Report is not a trusted certificate authority. There are many trusted authorities that can provide keystore files. Select the following link to see an example of creating a keystore file: http://docs.oracle.com/cd/E19509-01/820-3503/ggsxx/index.html.

- In the Keystore Password text box, type the password for protecting the integrity of the keystore.

- From the Keystore Type list, select
 the type of keystore to instantiate: JKS or PKCS12. 

- Select
 the encryption/decryption protocol to use on the socket from the 
 Keystore Protocol list.
 The valid values are SSL and TLS. 

- Select
 the X509 algorithm to use from the 
 Keystore Algorithm list. This defaults to the Sun implementation (SunX509). For IBM JVMs you should use IBMX509.

- Select Save. 

- Restart Server for the settings to take effect. 

To configure the SSL feature in the server.properties file:

- Open the server.properties file in the <install_root>\bin directory.

- By default, httpserver.ssl.enable is true.

- Set the other properties starting with httpserver.ssl to meet your requirements.

- Save the file.

- Restart Server for the settings to take effect.

### Multiple SSL Certificate Support

When accessing Report Server by domain names via HTTPS, you can apply different SSL certificates for different domain names. You can use a configuration file httpsCertificateMapping.xml for defining the mapping relationship between domains and certificate aliases. You should create the file manually and put it in the <install_root>\bin folder.

The following is a sample of the httpsCertificateMapping.xml file. It defines three groups of mapping relationship: www.a.com maps to certificate alias A, www.b.com maps to certificate alias B, and www.example.com and www.example.org map to certificate alias C.

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
See the details about the elements in the file:

- 
httpsCertificateMapping: The
 root element.

- 
certificateMapping: One mapping relationship between certificate alias and domain name.

- 
description: Optional. The description about the mapping. 

- 
certificateAlias: The alias of the certificate defined in the keystore file. 

- 
domainPattern: A domain name pattern.

When an HTTPS request comes in, Report Server first checks the domain name input in the browser. If the domain name matches domainPattern of a certificateMapping in httpsCertificateMapping.xml, the corresponding cerificateAlias will be used to get the certificate from the keystore, and then the certificate applies. If no matched domainPattern is found or no certificate is got, the first certificate in the keystore will apply. 

To apply different certificates to multiple domain names, take the following steps:

- Make sure Report Server starts by JDK 8.

- 
Configure SSL on Report Server. 

- Generate a keystore file which contains multiple entities (each entity contains a certificate and has an alias). 

- Set the keystore file name as the value of the httpserver.ssl.keystore property in server.properties in <install_root>\bin. 

- Create the file httpsCertificateMapping.xml in the <install_root>\bin folder. In the file, specify mapping relationship between domains and certificate aliases defined in the keystore file.

- Restart Report Server. Then when accessing Server using different domain name, the corresponding certificate will apply.
