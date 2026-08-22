---
title: "Cached Report Bursting"
id: 1500010028602
section: "Defining Report Security - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028602-Cached-Report-Bursting
updated_at: 2021-07-24T10:39:31Z
---

# Cached Report Bursting

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063221-Defining-Report-Security) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security)

# Cached Report Bursting

Cached report bursting is a security mechanism for controlling user access to data at the group level in a page report. It enables different users to view different data groups according to their access privileges. By defining which groups of data are available to which users, groups, or roles exist in the Logi JReport Server security system, report result is created for each user, role and group. When a user accesses a report at runtime, Logi JReport checks the user and the group and role of the user and merges the groups of data the user is authorized to see and displays it to the user. Cached report bursting also applies to nested groups.

Cached report bursting is implemented with these security properties on the group panel of a table or banded object: [Cascade, Grant, Groups, and Roles](https://devnet.logianalytics.com/hc/en-us/articles/1500010033882-Group-Panel-Properties#Security). The following example shows the basic procedure to set up a cached report bursting policy.

1. [Create a group table](https://devnet.logianalytics.com/hc/en-us/articles/1500010063941-Inserting-Tables-in-a-Report-)  in a page report for customer information which is grouped by the Country field.
2. [Create a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010068541-Creating-Formulas-in-a-Catalog) to control the Grant property value. This formula returns a String value indicating which user will have the privilege to access which country group of data.

   Here, we write the formula Burst\_User to set the security identifier as follows:

   `if (@Country == "China" || @Country == "Canada")  
   return "admin";  
   if (@Country == "USA")  
   return "jennifer";`

   "admin" and "jennifer" are two users assigned by the Logi JReport Server administrator. The above formula states that, the user "admin" is authorized to view only the China and Canada groups, while the user "jennifer" can only view the USA group. If the formula is written as follows:

   `if ( @Country =="USA")  
   return "user1|user2|user3";`

   Then, user1, user2, and user3 can view the USA group.
3. Create another formula Burst\_Group to control the Groups property value. This formula returns a String value indicating which group of users will have the privilege to access which country group of data.

   `if(@Country=='Italy')  
   return 'group1';  
   if(@Country=='USA')  
   return 'group2';`
4. Create one more formula Burst\_Role to control the Roles property value. This formula returns a String value indicating which role will have the privilege to access which country group of data.

   `if(@Country=='Japan')  
   return 'role1';  
   if(@Country=='USA')  
   return 'role2';`
5. In the Report Inspector, select the node that represents the group. Then, in the Security section of the Properties sheet, set Cascade to **true**, the Grant property's value to the formula **Burst\_User**, Groups to **Burst\_Group**, and Roles to **Burst\_Role**.

Since the control of report access is not possible without user ID, the significance of this function is only apparent when other users try to access a report after it has been published to Logi JReport Server. When an end user views a report with cached report bursting on Logi JReport Server, the corresponding group will be displayed according to the security identifier.

In the above example, if "admin" belongs to group1 and role1, he will be able to view the China, Canada, Italy, and Japan groups. jennifer will be able to view only the USA group if she belongs to group2 and role2.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063221-Defining-Report-Security) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security)
