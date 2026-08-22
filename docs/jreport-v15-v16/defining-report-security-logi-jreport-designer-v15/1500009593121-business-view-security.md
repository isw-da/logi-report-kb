---
title: "Business View Security"
id: 1500009593121
section: "Defining Report Security - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593121-Business-View-Security
updated_at: 2021-07-24T05:53:43Z
---

# Business View Security

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593201-RLS-at-Report-Scope)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571182-Permission-Logic-on-Group-Elements)

# Business View Security

Business view security enables report designers to limit user access to the specific members of groups in business views. By defining which members of a group are available to which users, groups, or roles, report results are created for each user, role and group. When a user accesses a report at runtime, Logi JReport checks the user, group and role of the user and merges the data in the report the user is authorized to see and displays it to the user.

Business view security also applies to new reports end users create on Logi JReport Server using the business view. Logi JReport Designer does not check business view security when getting data from business views.

Business view security contains these parts:

* **Data security**  
   It controls whether a user/role/group can access the data of a group/detail/aggregation in a business view at runtime. For a group element, you can allow or deny the access of some specific members of it to a user/role/group.
* **Resource security**  
   It controls whether a user/role/group can see a group/detail/aggregation/category in a business view at runtime.
* **Member-level security**  
   It controls which members or values of a group element in a business view that a user/role/group can access.

The following topics explain business view security:

> * [Permission Logic on Group Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009571182-Permission-Logic-on-Group-Elements)
> * [Configuring Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security)
> * [Example of Using Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009571162-Example-of-Using-Business-View-Security)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593201-RLS-at-Report-Scope)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571182-Permission-Logic-on-Group-Elements)
