---
title: "Configuring Proxy for Connecting to REST Web Service"
id: 6417117277591
section: "Setting Up the Report Designing Environment - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/6417117277591-Configuring-Proxy-for-Connecting-to-REST-Web-Service
updated_at: 2022-11-02T08:18:21Z
---

# Configuring Proxy for Connecting to REST Web Service

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735516331543-Configuring-the-Logging-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735570011287-Introducing-the-Designer-Reporting-Environment)

# Configuring Proxy for Connecting to REST Web Service

When setting up a [JSON](https://devnet.logianalytics.com/hc/en-us/articles/5735528141079-Working-with-JSON-Connections-in-a-Catalog) or [XML](https://devnet.logianalytics.com/hc/en-us/articles/5735499628183-Working-with-XML-Connections-in-a-Catalog) data source connection in Designer, if you use a proxy to connect to the REST Web Service in a restricted network, you can set the proxy parameters in a configuration file to enable the proxy to work successfully. This topic presents an example to show the proxy parameters you can define in the configuration file.

To configure the proxy parameters, you need to manually create the configuration file in XML and name it **restdsproxy.xml** in the `<install_root>\bin` folder. For example:

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

The following shows the usage of each tag.

* **restdsproxy**  
  The root tag that contains one or more <proxymapping> subtags.
* **proxymapping**  
  The whole set of the parameters of a proxy. It contains the following subtags, with each defining a specific proxy parameter.
* **urlpattern**  
  A regular expression string supported by Java that matches the URL of a REST Web Service. If there are multiple URL patterns that match the same URL, the proxy setting in the <proxymapping> tag that contains the first one matched takes effect.
* **proxyhost**  
  The host name or IP address of the proxy.
* **proxyport**  
  The port number of the proxy.
* **user**  
  The user name used for the proxy authentication. It is optional.
* **password**  
  The password used for the proxy authentication. It is optional.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The <user> and <password> information is encrypted, and replaced by the <encrypt-sign> tag after Designer starts up.

`<encrypt-sign>enDkq7srM9cHhoUwzYXJ3NvcDIYk</encrypt-sign>`

If you want to change the user or password, delete the <encrypt-sign> tag and then add the <user> and <password> tags in restdsproxy.xml.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735516331543-Configuring-the-Logging-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735570011287-Introducing-the-Designer-Reporting-Environment)
