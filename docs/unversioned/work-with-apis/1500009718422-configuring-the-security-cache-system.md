---
title: "Configuring the Security Cache System"
id: 1500009718422
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718422-Configuring-the-Security-Cache-System
updated_at: 2021-07-25T07:20:24Z
---

# Configuring the Security Cache System

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718402-Auditing-on-Exporting-Printing-and-Saving-of-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718602-Customizing-the-Web-Report-Studio-Toolbar)

# Configuring the Security Cache System

You can define the maximum number of users, roles, groups, and ACL objects to cache in the [security cache system](https://devnet.logianalytics.com/hc/en-us/articles/1500009751221-Security-Cache-System) by invoking the following methods in the API class **jet.server.api.admin.cfg.ConfigurationCache**.

```
/**  
 * Set the security user cache's size.  
 * Setting the size of the cache to zero or negative means closing the security user cache.  
 * @param size  
 */   
public void setSecurityUserCacheSize(int size);  
/**  
 * Get the size of the security user cache.  
 
 * @return the size of the security user cache   
 */   
public int getSecurityUserCacheSize();  
/**  
 * Set the size of the security role cache.  
 * Setting the size of the cache to zero or negative means closing the security role cache.  
 * @param size  
 */  
public void setSecurityRoleCacheSize(int size);  
/**  
 * Get the size of the security role cache.  
 * @return the size of the security role cache   
 */   
public int getSecurityRoleCacheSize();  
/**  
 * Set the size of the security group cache.  
 * Setting the size of the cache to zero or negative means closing the security group cache.  
 * @param size  
 */  
public void setSecurityGroupCacheSize(int size);  
/**  
 * Get the size of the security group cache.  
 * @return the size of the security group cache  
 */   
public int getSecurityGroupCacheSize();  
/**  
 * Set the size of the security protection cache.  
 * Setting the size of the cache to zero or negative means closing the security protection cache.  
 * @param size  
 */  
public void setSecurityProtectionCacheSize(int size);  
/**  
 * Get the size of the security protection cache.  
 * @return the size of the security protection cache  
 */ 
public int getSecurityProectionCacheSize();
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718402-Auditing-on-Exporting-Printing-and-Saving-of-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718602-Customizing-the-Web-Report-Studio-Toolbar)
