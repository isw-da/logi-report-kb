---
title: "Enabling SSL (HTTPS) in a Standalone  Logi Report Server"
id: 360049412614
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049412614-Enabling-SSL-HTTPS-in-a-Standalone-Logi-Report-Server
updated_at: 2020-07-27T22:04:48Z
---

# Enabling SSL (HTTPS) in a Standalone  Logi Report Server

Logi Report Server supports HTTPS requests in standalone mode. Secure port for HTTPS requests should use different port from non-secure port for HTTP requests. By default, port 6888 is set as the secure port for accessing the server console. The URL for visiting Logi Report Server via HTTPS schema is like this:

`https://IP_address or localhost:6888`

SSL support is disabled by default. You need to enable it and configure corresponding settings in order to use HTTPS schema to visit Logi Report Server UI. This can be done either in the Logi Report Server console as an administrator or in the server.properties file located in the `<install_root>\bin` directory.

**To enable the SSL feature via the server console:**

1. Point to **Administration** on the system toolbar, and then select **Configuration** > **Service** from the drop-down menu, select the **Enable Secure Socket Layer Connection** option.
2. In the Secure Port text box, type a port used for visiting the Logi Report Server console via HTTPS schema. It should be different from the Port for HTTP schema.
3. In the Keystore File Path text box, type the location of your trusted keystore file.
4. In the Keystore Password text box, type the password used to protect the integrity of the keystore.
5. Select the type of keystore to be instantiated from the Keystore Type drop-down list. The valid values are JKS and PKCS12.
6. Select the encryption/decryption protocol to be used on the socket from the Keystore Protocol drop-down list. The valid values are SSL and TLS.
7. Select the X509 algorithm to use from the Keystore Algorithm drop-down list. This defaults to the Sun implementation (SunX509). For IBM JVMs you should use IbmX509.
8. Select **Save** in the page, then restart Logi Report Server in order for the settings to take effect.

**To enable the SSL feature in the server.properties file:**

1. Open the server.properties file located in the `<install_root>\bin` directory.
2. Set httpserver.ssl.enable to **true**.
3. Set the other properties starting with httpserver.ssl to meet your requirements.
4. Save the file, then restart Logi Report Server in order for the settings to take effect.

**Notes:**

* Logi Report does not provide a keystore file since Jinfonet is not a trusted certificate authority and just provides a Keystore File Path option for you to configure the location of your trusted keystore file. There are many trusted authorities that can provide keystore files. Here is an example of creating a keystore file: <http://docs.oracle.com/cd/E19509-01/820-3503/ggsxx/index.html>.
* Logi Report Server Monitor does not support SSL.
