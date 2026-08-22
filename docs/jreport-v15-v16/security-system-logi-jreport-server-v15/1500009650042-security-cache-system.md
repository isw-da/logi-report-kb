---
title: "Security Cache System"
id: 1500009650042
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650042-Security-Cache-System
updated_at: 2021-07-24T20:53:41Z
---

# Security Cache System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650162-Role-Based-Security)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650122-Using-an-LDAP-Server-s-Security-System)

# Security Cache System

The security cache system temporarily stores security objects such as users, roles, groups and ACLs. ACL, short for Access Control List, is the core object of the security authorization system, and is in charge of storing and checking principal permissions. When Logi JReport Server requires information from the security system, it can fetch it from the cache for better performance.

The cache system caches not only security objects for the built-in security system, but also those implemented by the [Security API](https://devnet.logianalytics.com/hc/en-us/articles/1500009668781-Customized-Implementation-of-the-Security-API) from the external security system. It caches security information in the security data. If the security service needs security information, it will fetch it from the security data. However, if the security data cannot find the information, it will request it from the Security API, and then cache it in the cache system. When the security information is modified in the security system, the Security API is invoked directly in order to modify the security data.

The following focuses on the configuration and synchronization of the security cache system.

Below is a list of the sections covered in this topic:

* [Configuring the Security Cache System](#Config)
* [Synchronizing the Security Cache System](#Sync)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Configuring the Security Cache System

The security cache system enables you to define the maximum number of users, roles, groups and ACL objects that can be cached. There are the following ways in which you can customize the security cache system:

* **Configuring from the Logi JReport Administration page**

  You must be a member of the administrator role in order to access the Logi JReport Administration page.

  1. Log onto the Logi JReport Administration page, select **Cache** on the system toolbar and then select **Security Cache** from the drop-down menu to open the Cache - Security Cache page.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404920420247/scrty_rsc_srv_cache1.gif)
  2. In the Number of User Objects text box, specify the maximum number of user objects in the security cache, which should be an integer value.
  3. In the Number of Role Objects text box, specify the maximum number of role objects in the security cache, which should be an integer value.
  4. In the Number of Group Objects text box, specify the maximum number of group objects in the security cache, which should be an integer value.
  5. In the Number of ACL Objects text box, specify the maximum number of ACL objects in the security cache, which should be an integer value.
  6. In the Expire Time text box, specify how long the security cache will be kept for. The time is measured in seconds.
  7. Select **Save** to save the cache configuration.
  8. Restart Logi JReport Server to apply the settings.
* **Configuring by editing the server.properties file**

  Edit the following four properties:

  + **server.security.user.cache.size**  
     This should be an integer value. Its value indicates the maximum number of user objects that the security cache can store. The default value is 1000.
  + **server.security.role.cache.size**  
     This should be an integer value. Its value indicates the maximum number of role objects that the security cache can store. The default value is 50.
  + **server.security.group.cache.size**  
     This should be an integer value. Its value indicates the maximum number of group objects that the security cache can store. The default value is 50.
  + **server.security.protection.cache.size**  
     This should be an integer value. Its value indicates the maximum number of ACL objects that the security cache can store. The default value is 100.

  For instance,

  + If server.security.user.cache.size=1000, the cache can then store at most 1000 user objects.
  + If server.security.role.cache.size=100, the cache can then store 100 role objects.
  + If server.security.group.cache.size=100, the cache can then store 100 group objects.
  + If server.security.protection.cache.size=100, the cache can then store 100 ACL objects.

Developer users can also configure the security cache system by [using API method](https://devnet.logianalytics.com/hc/en-us/articles/1500009643802-Configuring-the-Security-Cache-System)**.**

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Synchronizing the Security Cache System

A synchronization system has been provided for synchronizing Logi JReport Server's security system with your external security systems. When the security cache system receives a security information modification event, it then fetches the security information from API and updates the cached information.

The following is a diagram of the synchronization system mechanism:

![](https://devnet.logianalytics.com/hc/article_attachments/4404926661655/scrty_rsc_srv_cache2.gif)

There are two ways to invoke the synchronization system. The first is to modify the security information on the server UI (red line), and the second is to modify the external security system (blue line).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650162-Role-Based-Security)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650122-Using-an-LDAP-Server-s-Security-System)
