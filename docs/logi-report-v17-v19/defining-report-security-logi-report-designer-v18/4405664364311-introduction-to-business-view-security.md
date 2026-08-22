---
title: "Introduction to Business View Security"
id: 4405664364311
section: "Defining Report Security - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664364311-Introduction-to-Business-View-Security
updated_at: 2022-01-27T20:34:20Z
---

# Introduction to Business View Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664362007-Setting-Up-Business-View-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664363415-Configuring-Business-View-Security-in-a-Catalog)

# Introduction to Business View Security

This topic introduces what makes up the business view security and how it works. It also illustrates the permission logic on group objects in business views to help you set user permissions on specific members of the group objects appropriately.

## How Business View Security Works

You can apply business view security to restrict different users' access to the view elements of business views in a catalog.

Business view security contains the following two parts:

* **Data Security**  
  It controls whether a user/role/group in the security system of Server can access the data of the view elements at runtime. For a group object, you can further allow or deny the access of its specific members to a user/role/group. For more information, see [Permission Logic on Group Objects](#Logic).
* **Resource Security**  
  It controls whether a user/role/group can see the view elements at runtime.

After the report designer defines users, groups, and roles' permissions on the view elements, when a user accesses a report at runtime that involves the view elements, Server checks the user and the group and role of the user, and then merges the data in the report the user is authorized to see and displays it to the user, thus Server is able to create different reports for different users. Business view security also applies to reports that users create on Server using the business views.

## Permission Logic on Group Objects

Logi Report classifies the relationship between a principal (user, role, or group) and the members of a group object in a business view into three sets:

* **Allowed Set**  
  The members of a group object that a principal is allowed to access, which are directly specified to the principal, excluding those inherited from the parent roles or groups.
* **Denied Set**  
  The members of a group object that a principal is not allowed to access, which are directly specified to the principal, excluding those inherited from the parent roles or groups.
* **Unspecified Members**  
  The members of a group object that are specified neither in a user's allowed/denied set nor in the inherited allowed/denied set from the user's parent roles/groups. Report designer can determine whether a user can access the unspecified members.

A principal can have its own allowed/denied set and inherit the allowed/denied sets from its parent roles or groups. The parent allowed/denied sets will be calculated first and it is a recursive process.

The following are the detailed working logic:

* If for a principal, a member exists in both the allowed set and denied set, the denied set has higher priority than the allowed set. In this case, the member is not available to the principal.
* The directly defined permission on a principal always overwrites the permission inherited from its parents. That is, for a member of a group object, if its permission has not been defined on a given user/role/group, the permission inherits from the parents of the user/role/group; if it is defined, the permission is used directly.
* Inheritance rule:
  + If a member is denied by any parent, it is denied; or else if a member is allowed by any parent, it is allowed.
  + If a member is neither denied nor allowed by any parent, the permission is regarded as unspecified.
* After inheritance rule is applied to a specific user, if some members are still unspecified, the status of the members depends on the option setting whether to make them allowed or denied.

Here is the priority order:

Denied Set > Allowed Set > Inherited Denied Set > Inherited Allowed Set > Unspecified (no matter whether it is allowed or denied).

See the diagram:

![Priority diagram](https://devnet.logianalytics.com/hc/article_attachments/4420542227223/scrty_bv_intro.gif)

The final result of the members of a group object that a principal is allowed to access is:

({Allowed Set} - {Denied Set}) U   
 (({Inherited Allowed Set from parent 1} U {Inherited Allowed Set from parent 2} U ...) - ({Inherited Denied Set from parent 1} U {Inherited Denied Set from parent 2} U ...)) U   
 {Unspecified if allowed}

The final set of the unspecified is:

{All} - ({Allowed Set} U {Denied Set} U {Inherited Allowed Set from parent 1} U {Inherited Denied Set from parent 1} U {Inherited Allowed Set from parent 2} U ...)

For a user, the security in a business view would be like this:

{Accessible members of group1} And {Accessible members of group2} And...

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) If you define all members in a group object regardless of whether it is set to a principal directly or to the parents indirectly, Logi Report Engine retrieves no data from the group object to the principal.

The following shows some examples to further explain the relationship between a principal and the group object members.

**Example 1**

Here we use a simple sample to describe a case when a user belongs to multiple roles.

Assume there is a group object Order ID={1,2,3,4,5,6,7,8,9}, and we set business view security on this group object for a user (user1) and two roles (role1 and role2) separately.

|  | Belong To | Allowed Set | Denied Set |
| --- | --- | --- | --- |
| user1 | role1, role2 | 1 |  |
| role1 |  | 2,3 | 4,5 |
| role2 |  | 3,4,5 | 1,2 |

The unspecified members are {1,2,3,4,5,6,7,8,9} - ({1}U{2,3}U{4,5}U{3,4,5}U{1,2}) = {6,7,8,9}.

Assume we set Allow Unspecified Members to "true", which means the unspecified members {6,7,8,9} are allowed to the user.

The final result that user1 can see when only this business view security is taking effect is:

{1} U ( ({2,3}U{3,4,5}) - ({4,5}U{1,2}) ) U {6,7,8,9}={1,3,6,7,8,9}

**Example 2**

This example is more complex. It contains four properties of the business view security setting.

Assume there is a summary table with three group objects and a summary.

| Region | Country | City | Summary (the count of Order\_ID) |
| --- | --- | --- | --- |
| APAC |  |  | 41 |
|  | Australia |  | 20 |
|  |  | Sydney | 20 |
|  | China |  | 21 |
|  |  | Beijing | 9 |
|  |  | Hongkong | 4 |
|  |  | Shanghai | 8 |

The following table lists the business view security setting in the left cells, and the final results a user gets in the right cells.

| Business View Security Specified As | The Result User Gets |
| --- | --- |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | <empty> | {China} | True | | City | <empty> | <empty> | True | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | | APAC |  |  | 20 | |  | Australia |  | 20 | |  |  | Sydney | 20 | |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | {China} | <empty> | False | | City | <empty> | {Beijing,Shanghai} | True | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | | APAC |  |  | 4 | |  | China |  | 4 | |  |  | Hongkong | 4 | |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | {China} | <empty> | False | | City | <empty> | {Beijing,Shanghai} | False | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | |  |  |  | 0 | |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664362007-Setting-Up-Business-View-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664363415-Configuring-Business-View-Security-in-a-Catalog)
