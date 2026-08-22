---
title: "Business View Security"
id: 12491478319245
section: "Report Feature Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491478319245-Business-View-Security
updated_at: 2025-05-30T03:01:51Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Business View Security

Business view security enables report designers to limit user access to the data and to the specific members of groups in business views. By defining which members of a group object in a business view are available to which users, groups, or roles existing in the security system of Server, you can create different report results  for each user, role, and group. When a user accesses any report created using the specified business view at runtime,  Server checks the user, and the group and role of the user and merges the data in the report the user is authorized to see and displays the permitted result to the user.

In the following example, we suppose the security system contains the user Manager_NA who is the manager of the North America region, and the user has the necessary permissions to run the sample reports in the Public Reports\SampleReports folder in the resource tree of Server. In Designer we first define a security policy on the WorldWideSalesBV business view in the SampleReports.cat catalog file to limit the manager's data access permission to that of North America  only, and then we publish the catalog to the Public Reports\SampleReports folder in Server to update its business view security. Then when the manager logs onto the Server Console with the username Manager_NA and runs the sample reports that use WorldWideSalesBV, he will only be able to view data about North America in the reports.

Previous Topic  Next Topic
