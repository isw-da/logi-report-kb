---
title: "Dynamic Security"
id: 12491407823757
section: "Report Feature Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12491407823757-Dynamic-Security
updated_at: 2025-05-30T03:01:50Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Dynamic Security

The Server administrators can create dynamic security policies for catalogs published to Server using security files, which contain catalog internal security definitions for Business View Security, Record Level Security, and Column Level Security. With dynamic security, administrators can change the security policies applied to a catalog at runtime, without having to edit the security in Designer and publish the catalog again.

In the following example, we suppose new security policies are added in the SampleReports.cat catalog file and we want them to be applied to the same catalog in the Public Reports\SampleReports folder in Server resource tree. So we export the security in Designer to the security file SampleReports.security.xml, then we sign in to the Server Console as an administrator to apply the security file to the catalog to dynamically modify its security definitions.

Previous Topic  Next Topic
