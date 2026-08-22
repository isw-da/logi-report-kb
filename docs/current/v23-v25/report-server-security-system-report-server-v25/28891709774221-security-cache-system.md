---
title: "Security Cache System"
id: 28891709774221
section: "Report Server Security System Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891709774221-Security-Cache-System
updated_at: 2026-02-26T02:13:49Z
source_host: docs-report.zendesk.com
---
# 
Security Cache System

The security cache system temporarily stores security objects such as users, roles, groups, and ACLs. Report Server can fetch security information from the security cache for better performance. This topic describes how you can configure and synchronize the security cache system.

ACL, short for Access Control List, is the core object of the security authorization system, and is in charge of storing and checking principal permissions.

The cache system caches not only security objects for the built-in security system, but also those implemented by the Security API from the external security system. It caches security information in the security data. If the security service needs security information, it fetches it from the security data. However, if the security data cannot find the information, it will request it from the Security API, and then cache it in the cache system. When the security information is modified in the security system, the Security API is invoked directly in order to modify the security data.

This topic contains the following sections:

- 
                    Configuring the Security Cache System
                

- 
                    Synchronizing the Security Cache System
                

## 
Configuring the Security Cache System

The security cache system enables you to define the maximum number of users, roles, groups, and ACL objects to cache. You can customize the security cache system using the following ways:

- 
Configuring via UI
- On the system toolbar of the Server Console, navigate to Administration > Configuration > Cache > Security Cache to open the Security Cache page. You must be a member of the administrator role to access the Administration menu.
        

- In the Number of User Objects text box, specify the maximum number of user objects in the security cache, which should be an integer value.

- In the Number of Role Objects text box, specify the maximum number of role objects in the security cache, which should be an integer value.

- In the Number of Group Objects text box, specify the maximum number of group objects in the security cache, which should be an integer value.

- In the Number of ACL Objects text box, specify the maximum number of ACL objects in the security cache, which should be an integer value.

- In the Expire Time text box, specify how long the security cache will be kept for. The time is measured in seconds.

- Select Save to save the cache configuration.

- Restart Report Server to apply the settings.

- 
Configuring by editing the server.properties fileEdit the following four properties:

- 
server.security.user.cache.size
        This should be an integer value. Its value indicates the maximum number of user objects that the security cache can store. The default value is 1000.

- 
server.security.role.cache.size
        This should be an integer value. Its value indicates the maximum number of role objects that the security cache can store. The default value is 50.

- 
server.security.group.cache.size
        This should be an integer value. Its value indicates the maximum number of group objects that the security cache can store. The default value is 50.

- 
server.security.protection.cache.size
        This should be an integer value. Its value indicates the maximum number of ACL objects that the security cache can store. The default value is 100.

For instance,

- If server.security.user.cache.size=1000, the cache can then store at most 1000 user objects.

- If server.security.role.cache.size=100, the cache can then store 100 role objects.

- If server.security.group.cache.size=100, the cache can then store 100 group objects.

- If server.security.protection.cache.size=100, the cache can then store 100 ACL objects.

Developer users can also configure the security cache system by using API method.

## 
Synchronizing the Security Cache System

Report Server provides a synchronization system for synchronizing the server security system with your external security systems. When the security cache system receives a security information modification event, it then fetches the security information from API and updates the cached information.

The following is a diagram of the synchronization system mechanism:

There are two ways to invoke the synchronization system. The first is to modify the security information via server UI (red line), and the second is to modify the external security system (blue line).
