---
title: "Defining Report Security"
id: 1500010063221
section: "Defining Report Security - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063221-Defining-Report-Security
updated_at: 2021-07-24T10:39:32Z
---

# Defining Report Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034922-Applying-Styles) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028602-Cached-Report-Bursting)

# Defining Report Security

Security in a report is a type of filter control that limits the data shown on a report according to the user's access permissions. This topic demonstrates controlling access to reports and different subsets of data by means of defining security on the users, roles and groups that are created in the Logi JReport Server security system (for more information, see Security System Data Model in the *Logi JReport Server User's Guide*). No matter to whom you need to provide information at runtime, Logi JReport allows you to control access to it according to your requirements.

Generally, report security can be classified into these groups in Logi JReport:

* [Cached Report Bursting](https://devnet.logianalytics.com/hc/en-us/articles/1500010028602-Cached-Report-Bursting)
* [Record Level and Column Level Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security)
* [Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/1500010028582-Business-View-Security)

Depending on the data source a report uses, query or business view, the security policies that can be applied to the report vary. A page report that is created using query resources can be defined with cached report bursting, record level security and column level security. For a library component, business view security and record level security can be applied. On a web report or a business view based page report, only business view security is supported. For a page report created using query resources, [report bursting](https://devnet.logianalytics.com/hc/en-us/articles/1500010070801-Creating-Bursting-Reports) is also a very convenient way to filter data based on physically splitting the report into groups for each user.

**Report security structure**

The following diagram illustrates the report security structure in Logi JReport.

![Diagram of report security structure in Logi JReport](https://devnet.logianalytics.com/hc/article_attachments/4404909291927/scrty1.gif)

Permissions can be assigned to users, roles, and groups. A role/group can have more than one user, and a user can belong to more than one role/group. The permissions that a user may have depends on the permissions of the roles/groups it belongs to and its own permissions. The inheritance relationship is logic OR.

![Permission and inheritance relationship diagram](https://devnet.logianalytics.com/hc/article_attachments/4404901345687/scrty2.gif)

When calculating a user's permissions, the permission collections of its roles and groups are first calculated using logical OR. If the calculation result conflicts with the user permissions, the user's permissions will have priority. That is, if one access right is permitted for the user's groups and roles but denied by the user's permissions, the user will not be permitted to have this access right. For example, if user U1 belongs to two roles and two groups, such as R1, R2, G1, and G2. The permissions he/she will have are the permissions collections of the roles, groups and itself, which is P1, P2, P3, P4, and P5, as shown in the above diagram. The group and role relationships are the same. Here is another example, if group G1 has two roles, R1 and R2, together with its own permissions, the users in group G1 will have P1, P2, and P3, and also the permissions assigned directly to the users.

See also Report Security System in the *Logi JReport Server User's Guide* for details about how report security is applied at runtime.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034922-Applying-Styles) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028602-Cached-Report-Bursting)
