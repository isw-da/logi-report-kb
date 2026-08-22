---
title: "Security Cache System"
id: 4405684018711
section: "Logi Report Server Security System Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405684018711-Security-Cache-System
updated_at: 2022-01-27T07:59:48Z
---

# Security Cache System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684029591-Role-Based-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690681623-Using-an-LDAP-Server-s-Security-System)

# Security Cache System

The security cache system temporarily stores security objects such as users, roles, groups, and ACLs. Logi Report Server can fetch security information from the security cache for better performance. This topic describes how you can configure and synchronize the security cache system.

ACL, short for Access Control List, is the core object of the security authorization system, and is in charge of storing and checking principal permissions.

The cache system caches not only security objects for the built-in security system, but also those implemented by the [Security API](https://devnet.logianalytics.com/hc/en-us/articles/4405690478871-Customized-Implementation-of-the-Security-API) from the external security system. It caches security information in the security data. If the security service needs security information, it fetches it from the security data. However, if the security data cannot find the information, it will request it from the Security API, and then cache it in the cache system. When the security information is modified in the security system, the Security API is invoked directly in order to modify the security data.

This topic contains the following sections:

* [Configuring the Security Cache System](#Config)
* [Synchronizing the Security Cache System](#Sync)

## Configuring the Security Cache System

The security cache system enables you to define the maximum number of users, roles, groups, and ACL objects to cache. You can customize the security cache system using the following ways:

* **Configuring via UI**
  1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** > **Cache** > **Security Cache** to open the Security Cache page. You must be a member of the administrator role to access the Administration menu.

     ![Cache - Security Cache page](https://devnet.logianalytics.com/hc/article_attachments/4420453464215/scrty_rsc_srv_cache1.gif)
  2. In the Number of User Objects text box, specify the maximum number of user objects in the security cache, which should be an integer value.
  3. In the Number of Role Objects text box, specify the maximum number of role objects in the security cache, which should be an integer value.
  4. In the Number of Group Objects text box, specify the maximum number of group objects in the security cache, which should be an integer value.
  5. In the Number of ACL Objects text box, specify the maximum number of ACL objects in the security cache, which should be an integer value.
  6. In the Expire Time text box, specify how long the security cache will be kept for. The time is measured in seconds.
  7. Select **Save** to save the cache configuration.
  8. Restart Logi Report Server to apply the settings.
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

Developer users can also configure the security cache system by [using API method](https://devnet.logianalytics.com/hc/en-us/articles/4405683549335-Configuring-the-Security-Cache-System)**.**

## Synchronizing the Security Cache System

Logi Report Server provides a synchronization system for synchronizing the server security system with your external security systems. When the security cache system receives a security information modification event, it then fetches the security information from API and updates the cached information.

The following is a diagram of the synchronization system mechanism:

![Synchronization System Mechanism](https://devnet.logianalytics.com/hc/article_attachments/4420461532439/scrty_rsc_srv_cache2.gif)

There are two ways to invoke the synchronization system. The first is to modify the security information via server UI (red line), and the second is to modify the external security system (blue line).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405684029591-Role-Based-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690681623-Using-an-LDAP-Server-s-Security-System)
