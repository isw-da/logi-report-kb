---
title: "Configuring Proxy for Connecting to a REST Web Service"
id: 1500009744961
section: "Configure Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744961-Configuring-Proxy-for-Connecting-to-a-REST-Web-Service
updated_at: 2021-07-25T07:20:14Z
---

# Configuring Proxy for Connecting to a REST Web Service

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718842-Updating-the-Server-License)

# This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.Configuring Proxy for Connecting to a REST Web Service

In a restricted network when a proxy is used for connecting to a REST Web Service as the data source, you can set the proxy parameters in a configuration file in Logi Report so as for the proxy to work successfully. You need manually create the configuration file in the XML format, named **restdsproxy.xml**, in the directory `<install_root>\bin`.

The following is an example of the configuration file and the detailed description of each tag in the file:

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

**Note:** The <user> and <password> information is encrypted, and replaced by the <encrypt-sign> tag after Logi Report starts up as follows:

`<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

If you want to change the user or password, delete the <encrypt-sign> tag and then add the <user> and <password> tags in the restdsproxy.xml.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718842-Updating-the-Server-License)
