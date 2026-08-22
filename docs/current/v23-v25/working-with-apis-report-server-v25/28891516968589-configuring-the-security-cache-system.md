---
title: "Configuring the Security Cache System"
id: 28891516968589
section: "Working with APIs Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891516968589-Configuring-the-Security-Cache-System
updated_at: 2026-02-26T02:11:02Z
source_host: docs-report.zendesk.com
---
# 
Configuring the Security Cache System 

You can define the maximum number of users, roles, groups, and ACL objects to cache in the security cache system by invoking the following methods in the API class jet.server.api.admin.cfg.ConfigurationCache.

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
