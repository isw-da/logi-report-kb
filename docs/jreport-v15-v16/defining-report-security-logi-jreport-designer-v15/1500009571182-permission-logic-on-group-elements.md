---
title: "Permission Logic on Group Elements"
id: 1500009571182
section: "Defining Report Security - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009571182-Permission-Logic-on-Group-Elements
updated_at: 2021-07-24T05:53:44Z
---

# Permission Logic on Group Elements

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593121-Business-View-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security)

# Permission Logic on Group Elements

The relationship between a principal (user, role or group) and the members of a group are classified into three groups:

* **Allowed Set**  
   The members of a group field that a principal is allowed to access, which are directly specified to the principal, excluding those inherited from the parent roles or groups.
* **Denied Set**  
   The members of a group field that a principal is not allowed to access, which are directly specified to the principal, excluding those inherited from the parent roles or groups.
* **Unspecified members**   
   The members of a group field that are specified neither in a user's allowed/denied set nor in the inherited allowed/denied set from the user's parent roles/groups. Report designer can determine whether a user can access the unspecified members.

A principal can have its own allowed/denied set and inherit the allowed/denied sets from its parent roles or groups. The parent allowed/denied sets will be calculated first and it is a recursive process.

The following are the detailed working logic:

* If for a principal a member exists in both the allowed set and denied set, the denied set has higher priority than the allowed set. In this case the member is not available to the principal.
* The directly defined permission on a principal always overwrites the permission inherited from its parents. That is, for a member of a group, if its permission has not been defined on a given user/role/group, the permission will inherit from the parents of the user/role/group; if it is defined, the permission will be used directly.
* Inheritance rule:
  + If a member is denied by any parent, it will be denied, or else if a member is allowed by any parent, it will be allowed.
  + If a member is neither denied nor allowed by any parent, the permission is regarded as unspecified.
* After inheritance rule is applied to a specific user, if some members are still unspecified, the status of the members will depend on the option setting whether to make them allowed or denied.

Here is the priority order:

Denied Set > Allowed Set > Inherited Denied Set > Inherited Allowed Set > Unspecified (no matter whether it is allowed or denied).

See the diagram below:

![](https://devnet.logianalytics.com/hc/article_attachments/4404893792023/scrty_bv_logic.gif)

The final result of the members of a group that a principal is allowed to access will be:

({Allowed Set} - {Denied Set}) U   
 (({Inherited Allowed Set from parent 1} U {Inherited Allowed Set from parent 2} U ...) - ({Inherited Denied Set from parent 1} U {Inherited Denied Set from parent 2} U ...)) U   
 {Unspecified if allowed}

The final set of the unspecified will be:

{All} - ({Allowed Set} U {Denied Set} U {Inherited Allowed Set from parent 1} U {Inherited Denied Set from parent 1} U {Inherited Allowed Set from parent 2} U ...)

For a user, the security in a business view would be like this:

{Accessible members of group1} And {Accessible members of group2} And...

**Note:** If all members are denied in a group field regardless of whether it is set to a principal directly or to the parents indirectly, no data will be retrieved from the group field to the principal.

We will take some examples to further demonstrate the relationship between a principal and the group members.

**Example 1**

Here we use a simple sample to describe a case when a user belongs to multiple roles.

Assume there is a group Order ID={1,2,3,4,5,6,7,8,9}, and we set business view security on this group for a user (user1) and two roles (role1, role2) separately.

|  | Belong to | Allowed Set | Denied Set |
| --- | --- | --- | --- |
| user1 | role1, role2 | 1 |  |
| role1 |  | 2,3 | 4,5 |
| role2 |  | 3,4,5 | 1,2 |

The unspecified members will be {1,2,3,4,5,6,7,8,9} - ({1}U{2,3}U{4,5}U{3,4,5}U{1,2}) = {6,7,8,9}.

Assume we set the property "Allow Unspecified Members" to true, which means the unspecified members {6,7,8,9} are allowed to the user.

The final result that user1 can see when only this business view security is taking effect will be:

{1} U ( ({2,3}U{3,4,5}) - ({4,5}U{1,2}) ) U {6,7,8,9}={1,3,6,7,8,9}

**Example 2**

This example is more complex. It contains four properties of the business view security setting.

Assume there is a summary table with three groups and a summary.

| Region | Country | City | Summary (the count of Order\_ID) |
| --- | --- | --- | --- |
| APAC |  |  | 41 |
|  | Australia |  | 20 |
|  |  | Sydney | 20 |
|  | China |  | 21 |
|  |  | Beijing | 9 |
|  |  | Hongkong | 4 |
|  |  | Shanghai | 8 |

And in below table, we list the business view security setting in the left cells, and the final result a user will get are listed in the right cells.

| Business view security specified as below | User will get such result |
| --- | --- |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | <empty> | {China} | True | | City | <empty> | <empty> | True | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | | APAC |  |  | 20 | |  | Australia |  | 20 | |  |  | Sydney | 20 | |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | {China} | <empty> | False | | City | <empty> | {Beijing,Shanghai} | True | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | | APAC |  |  | 4 | |  | China |  | 4 | |  |  | Hongkong | 4 | |
| | Group | Allowed Set | Denied Set | Allow Unspecified Members | | --- | --- | --- | --- | | Region | <empty> | <empty> | True | | Country | {China} | <empty> | False | | City | <empty> | {Beijing,Shanghai} | False | | | Region | Country | City | Summary (count Order\_ID) | | --- | --- | --- | --- | |  |  |  | 0 | |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593121-Business-View-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security)
