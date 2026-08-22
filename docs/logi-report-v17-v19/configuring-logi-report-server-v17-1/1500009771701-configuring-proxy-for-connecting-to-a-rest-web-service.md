---
title: "Configuring Proxy for Connecting to a REST Web Service"
id: 1500009771701
section: "Configuring Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771701-Configuring-Proxy-for-Connecting-to-a-REST-Web-Service
updated_at: 2021-07-24T00:49:26Z
---

# Configuring Proxy for Connecting to a REST Web Service

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771621-Updating-the-Server-License)

# Configuring Proxy for Connecting to a REST Web Service

In a restricted network when you use a proxy to connect to a REST Web Service as the data source, you can set the proxy parameters in a configuration file in Logi Report so as for the proxy to work successfully. You need manually create the configuration file in the XML format and name it **restdsproxy.xml**, in the `<install_root>\bin` directory. This topic describes the content and tags in the configuration file.

See the following example content in restdsproxy.xml:

```
<?xml version="1.0" encoding="UTF-8"?>  
<restdsproxy>  
    <proxymapping>  
        <urlpattern>https://.*\.jinfonet\.com/</urlpattern>  
        <proxyhost>192.0.0.14</proxyhost>
        <proxyport>8888</proxyport>
        <user>user1</user>  
        <password>psw1</password>  
    </proxymapping>  
    <proxymapping>  
        <urlpattern>http://.*\.jinfonet\.com\.cn/</urlpattern>  
        <proxyhost>192.0.0.14</proxyhost>
        <proxyport>80</proxyport>
        <user>user2</user>  
        <password>psw2</password>  
    </proxymapping>  
</restdsproxy>
```

* **restdsproxy**  
  The root tag that contains one or more <proxymapping> sub-tags.
* **proxymapping**  
  Represents the whole set of parameters of a proxy. It contains the following sub-tags each defining a specific proxy parameter.
* **urlpattern**  
  A regular expression string supported by Java that matches the URL of a REST Web Service. If there are multiple URL patterns that match the same URL, the proxy setting in the <proxymapping> tag that contains the first one matched will take effect.
* **proxyhost**  
  The host name or IP address of the proxy.
* **proxyport**  
  The port number of the proxy.
* **user**  
  The user name used for the proxy authentication. It is optional.
* **password**  
  The password used for the proxy authentication. It is optional.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)Logi Report Server encrypts the <user> and <password> information and replaces it with the <encrypt-sign> tag after it starts up as follows:

`<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

If you want to change the user or password, delete the <encrypt-sign> tag and then add the <user> and <password> tags in the **restdsproxy.xml**.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771621-Updating-the-Server-License)
