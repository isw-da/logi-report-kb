---
title: "SSL Support in the LDAP System"
id: 1500009718941
section: "Using an LDAP Server's Security System"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718941-SSL-Support-in-the-LDAP-System
updated_at: 2021-11-03T06:56:31Z
---

# SSL Support in the LDAP System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718961-Using-LDAP-Server-s-Security-Information)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692762-Security-for-Accessing-Web-Pages)

# SSL Support in the LDAP System

Logi JReport Server's LDAP system supports SSL when connecting to an LDAP server for obtaining security information. The following introduces the problems that may happen when using SSL in the LDAP system.

**Solving the wrong connection port type problem**

Logi JReport implements a method in the security system to solve the wrong connection port type problem.

If you use an SSL socket to connect to a server on a port that is not using SSL, or if you use a plain socket to connect to a server's SSL socket, your program will hang. This is a characteristic of the SSL protocol. To avoid this, you can use a main thread to create a child thread for connecting to the LDAP server. The main thread can wait the child thread for a period of time which is specified by the socket timeout time by users. If the child thread creates an LDAP connection successfully, it will notify the main thread, and the program will continue to run. However, if the child thread hangs due to using the wrong port type, the main thread will only need to wait until the socket timeout time has been reached and can continue to run.

Since the connection time varies with the user's network environment, it is better to set the socket timeout time in LDAPProperties.xml: modify the element env-socketTime's value before the server is started. Its default value is 10, which means that the socket timeout time is 10 seconds. You can modify this value according to your network environment.

**About SSL certificate store in Logi JReport Server**

Since JNDI uses the default SSL provider, the certificates will be checked by JSSE's default TrustManager: X509TrustManager. If the TrustManager does not accept them, Logi JReport Server will store the SSL certificates into another key store file. This file is placed in  `<install_root>\properties``\LDAPKeyStore.keystore`. The password to access the file is *jinfonet*. You can also use `-`D parameters to specify another file and password. For instance, if you want to add the certificates into: `C:\certs\certs.keystore`, and use the password *test*, you should add the following parameters to Logi JReport Server's startup file:

`"-Djavax.net.ssl.trustStore= C:\certs\certs.keystore"  
"-Djavax.net.ssl.trustStorePassword=test"`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718961-Using-LDAP-Server-s-Security-Information)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009692762-Security-for-Accessing-Web-Pages)
