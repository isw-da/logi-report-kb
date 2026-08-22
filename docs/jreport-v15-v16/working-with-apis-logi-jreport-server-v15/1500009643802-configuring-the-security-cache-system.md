---
title: "Configuring the Security Cache System"
id: 1500009643802
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009643802-Configuring-the-Security-Cache-System
updated_at: 2021-07-24T20:55:30Z
---

# Configuring the Security Cache System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668481-Tracing-Server-Resource-Change-Events)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644162-Customizing-the-Web-Report-Studio-Toolbar)

# Configuring the Security Cache System

You can define the maximum number of users, roles, groups and ACL objects that can be cached in the [security cache system](https://devnet.logianalytics.com/hc/en-us/articles/1500009650042-Security-Cache-System) by invoking the following methods in the API class jet.server.api.admin.cfg.ConfigurationCache.

|  |
| --- |
| ``` /**   * Set the security user cache's size  * Setting the size of the cache to zero or negative means closing the security user cache.  * @param size  */  public void setSecurityUserCacheSize(int size); /**  * Get the size of the security user cache   * @return the size of the security user cache   */  public int getSecurityUserCacheSize(); /**  * Set the size of the security role cache  * Setting the size of the cache to zero or negative means closing the security role cache  * @param size  */ public void setSecurityRoleCacheSize(int size); /**  * Get the size of the security role cache  * @return the size of the security role cache   */  public int getSecurityRoleCacheSize(); /**  * Set the size of the security group cache  * Setting the size of the cache to zero or negative means closing the security group cache  * @param size  */ public void setSecurityGroupCacheSize(int size); /**  * Get the size of the security group cache  * @return the size of the security group cache  */  public int getSecurityGroupCacheSize(); /**  * Set the size of the security protection cache  * Setting the size of the cache to zero or negative means closing the security protection cache  * @param size  */ public void setSecurityProtectionCacheSize(int size); /**  * Get the size of the security protection cache  * @return the size of the security protection cache  */  public int getSecurityProectionCacheSize(); ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668481-Tracing-Server-Resource-Change-Events)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644162-Customizing-the-Web-Report-Studio-Toolbar)
