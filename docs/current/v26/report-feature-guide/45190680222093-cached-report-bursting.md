---
title: "Cached Report Bursting"
id: 45190680222093
section: "Report Feature Guide"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190680222093-Cached-Report-Bursting
updated_at: 2026-04-30T15:09:54Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Cached Report Bursting

Cached report bursting is a security mechanism for controlling user access to data at the group level in a page report. It enables different users to view different data groups according to their access privileges. The report designer defines which groups of data in a report are available to which users, groups, or roles existing in the security system of Server. When a specified user accesses the report at runtime, Server checks the user, and the group and role of the user, and then merges the groups of data the user is authorized to see and displays permitted result to the user.

Report implements cached report bursting with these security properties on the group panels of tables or banded objects: Cascade, Grant, Groups, and Roles.

In the following example, we edit an expression as the value of the Grant property for the SHIPPER NAME group in the Master Detail Shipment Log.cls page report that is saved in the SampleReports.cat catalog file, to limit the user Tom's access to the Corban Truck Lines group and Cindy to Associated Transit. The users should be available in the security system of Server, and they have the necessary permissions to run the report. To simplify the example, we removed the Table of Contents at the beginning of the sample page report.

 We write the expression as follows:

if (@"Shipper Name" == "Corban Truck Lines")
        return "Tom";
        if (@"Shipper Name" == "Associated Transit")
        return "Cindy";
