---
title: "Defining Report Security"
id: 28897728921613
section: "Defining Report Security - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897728921613-Defining-Report-Security
updated_at: 2024-09-30T09:08:46Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Defining Report Security

Security in a report is a type of filter control that limits the data shown on a report according to the user's access permissions. This topic introduces controlling access to reports and different subsets of data by means of defining security on the users, roles, and groups that exist in the security system of Server. No matter to whom you need to provide information at runtime,  Report enables you to control access to it according to your requirements.

Generally, Report classifies  report security  into the following categories:

- Cached Report Bursting

- Record Level and Column Level Security

- Business View Security

Depending on the data resource a report uses, query or business view, the security policies you can apply to the report vary. You can define cached report bursting, record level security, and column level security on a page report that uses query resources. For a library component, you can apply business view security and record level security to it. On a web report or a business view-based page report, you can only use business view security. For a query-based page report, report bursting is also a very convenient way to filter data based on physically splitting the report into groups for each user.

Report security structure

The following diagram illustrates the report security structure in Report.

You can assign permissions to users, roles, and groups. A role/group can have more than one user, and a user can belong to more than one role/group. The permissions that a user may have depends on the permissions of the roles/groups it belongs to and its own permissions. The inheritance relationship is logical "OR".

When calculating a user's permissions, Report first calculates the permission collections of its roles and groups using the logical "OR". If the calculation result conflicts with the user's permissions, the user's permissions have higher priority, meaning if one access right is permitted for the user's groups and roles but denied by the user's permissions, the user is not permitted to have this access right. For example, if user U1 belongs to two roles and two groups, such as R1, R2, G1, and G2. The permissions the user has are the permissions collections of the roles, groups, and itself, which is P1, P2, P3, P4, and P5, as shown in the preceding diagram. The group and role relationships are the same. Here is another example: if group G1 has two roles, R1 and R2, together with its own permissions, the users in group G1 will have P1, P2, and P3, and also the permissions assigned directly to the them.

See also Report Security System in the Report Server Guide for more information about how Server applies report security at runtime.

Previous Topic  Next Topic
