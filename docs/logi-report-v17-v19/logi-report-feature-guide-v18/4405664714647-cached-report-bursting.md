---
title: "Cached Report Bursting"
id: 4405664714647
section: "Logi Report Feature Guide v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664714647-Cached-Report-Bursting
updated_at: 2022-01-27T20:35:02Z
---

# Cached Report Bursting

![](https://devnet.logianalytics.com/hc/article_attachments/4420556073751/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664715543-Business-View-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420542052759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661966103-Record-Level-Security-and-Column-Level-Security)

# Cached Report Bursting

Cached report bursting is a security mechanism for controlling user access to data at the group level in a page report. It enables different users to view different data groups according to their access privileges. The report designer defines which groups of data in a report are available to which users, groups, or roles existing in the security system of Server. Then when a specified user accesses the report at runtime, Server checks the user, and the group and role of the user and merges the groups of data the user is authorized to see and displays permitted result to the user.

Logi Report implements cached report bursting with these security properties on the group panels of tables or banded objects: Cascade, Grant, Groups, and Roles.

In the following example, we edit an expression as the value of the Grant property for the SHIPPER NAME group in the Master Detail Shipment Log.cls page report which is saved in the SampleReports.cat catalog file to limit the user Tom's access to the Corban Truck Lines group and Cindy to Associated Transit. The users should be available in the security system of Server and they have the necessary permissions to run the report.

We will write the expression as follows:

`if (@"Shipper Name" == "Corban Truck Lines")  
 return "Tom";  
 if (@"Shipper Name" == "Associated Transit")  
 return "Cindy";`

![Cached Report Bursting](https://devnet.logianalytics.com/hc/article_attachments/4420550806423/rptscrty_burst.gif)

![](https://devnet.logianalytics.com/hc/article_attachments/4420556073751/back.png)[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664715543-Business-View-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4420542052759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661966103-Record-Level-Security-and-Column-Level-Security)
