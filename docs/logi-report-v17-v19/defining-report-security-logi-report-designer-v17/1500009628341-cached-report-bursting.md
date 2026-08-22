---
title: "Cached Report Bursting"
id: 1500009628341
section: "Defining Report Security - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009628341-Cached-Report-Bursting
updated_at: 2021-07-24T16:05:25Z
---

# Cached Report Bursting

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605362-Defining-Report-Security) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605402-Record-Level-and-Column-Level-Security)

# Cached Report Bursting

Cached report bursting is a security mechanism for controlling user access to data at the group level in a page report. It enables different users to view different data groups according to their access privileges. The report designer defines which groups of data in a report are available to which users, groups, or roles existing in the Logi Report Server security system. Then when a specified user accesses the report at runtime, Logi Report Server checks the user, and the group and role of the user and merges the groups of data the user is authorized to see and displays permitted result to the user. Cached report bursting also applies to nested groups. This topics describes how to create cached report bursting on page reports to limit user access to different groups of data.

Cached report bursting is implemented with these security properties on the group panels of tables or banded objects: [Cascade, Grant, Groups, and Roles](https://devnet.logianalytics.com/hc/en-us/articles/1500009635121-Group-Panel-Properties#Security). The following example shows the basic procedure to set up a cached report bursting policy.

1. [Create a group table](https://devnet.logianalytics.com/hc/en-us/articles/1500009629281-Inserting-Tables-in-a-Report-) in a page report for customer information which is grouped by the Country field.
2. [Create a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009634201-Creating-Formulas-in-a-Catalog) to control the Grant property value. This formula returns a String value indicating which user will have the privilege to access the data of which Country group.

   Here, we write the formula Burst\_User to set the security identifier as follows:

   `if (@Country == "China" || @Country == "Canada")  
   return "admin";  
   if (@Country == "USA")  
   return "jennifer";`

   "admin" and "jennifer" are two users in the Logi Report Server security system. The above formula states that, the user "admin" is authorized to view the China and Canada groups, while the user "jennifer" can only view the USA group. If the formula is written as follows:

   `if ( @Country =="USA")  
   return "user1|user2|user3";`

   Then, user1, user2, and user3 can view the USA group.
3. Create another formula Burst\_Group to control the Groups property value. This formula returns a String value indicating which group of users will have the privilege to access the data of which Country group.

   `if(@Country=='Italy')  
   return 'group1';  
   if(@Country=='USA')  
   return 'group2';`
4. Create one more formula Burst\_Role to control the Roles property value. This formula returns a String value indicating which role will have the privilege to access the data of which Country group.

   `if(@Country=='Japan')  
   return 'role1';  
   if(@Country=='USA')  
   return 'role2';`
5. In the Report Inspector, select the **Table Group** object for the group and locate the **Security** section in the Properties sheet (for a banded object, it is the Group Panel object).

   ![Properties Sheet for Table Group Object](https://devnet.logianalytics.com/hc/article_attachments/4404904471319/scrty_crb.gif)
6. Set the Grant property's value to the formula **Burst\_User**, Groups to **Burst\_Group**, and Roles to **Burst\_Role**.

After a report with cached report bursting is published to Logi Report Server, when the specified users try to access the report, they can only view the groups of data that are authorized to them. In the above example, if the user "admin" belongs to group1 and role1, he will be able to view the China, Canada, Italy, and Japan groups; jennifer will be able to view only the USA group if she belongs to group2 and role2.

**Tip:** In addition to creating formulas and selecting the formulas to control the security properties, you can also edit expressions directly as the values the properties to define the cached report bursting security policy.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605362-Defining-Report-Security) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605402-Record-Level-and-Column-Level-Security)
