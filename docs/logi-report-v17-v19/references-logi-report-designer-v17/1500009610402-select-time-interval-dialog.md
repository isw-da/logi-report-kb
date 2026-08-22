---
title: "Select Time Interval Dialog"
id: 1500009610402
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009610402-Select-Time-Interval-Dialog
updated_at: 2021-07-24T16:04:08Z
---

# Select Time Interval Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610382-Select-Report-Tab-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633601-Send-Message-Dialog)

# Select Time Interval Dialog

The Select Time Interval dialog helps you to specify how a group element will be created based on the specified DBField whose data type is Timestamp/DateTime. It appears when you drag a DBField of the Timestamp/DateTime data type from the Resource Objects panel to the Business View panel in the [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607342-Business-View-Editor-Dialog).

![Select Time Interval dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911639703/slcttmintvl.gif)

The following are details about the options in the dialog:

**For Each Year**

Specifies to create a group element that uses the expression *Year(@MappingName)* to retrieve years of the current field as its values. The data type of the group element is Integer.

**For Each Quarter**

Specifies to create a group element that uses the expression *Quarter(@MappingName,Integer)* to retrieve quarters of the current field as its values. The data type of the group element is Integer.

**For Each Month**

Specifies to create a group element that uses the expression *Month(@MappingName)* to retrieve months of the current field as its values. The data type of the group element is Integer.

**For Each Week**

Specifies to create a group element that uses the expression *WeekOfYear(@MappingName)* to retrieve weeks of the current field as its values. The data type of the group element is Integer.

**For Each Day**

Specifies to create a group element that uses the expression *Day(@MappingName)* to retrieve days of the current field as its values. The data type of the group element is Integer.

**Keep Original**

Specifies to create a group element based on the field itself.

**![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")Auto Create Hierarchy**

Specifies whether to create a hierarchy which contains the specified group elements. Disabled when none of the above options is selected.

* **Hierarchy Name**  
  Specifies the name of the hierarchy.

**OK**

Creates the group elements and closes the dialog.

**Cancel**

Cancels adding group elements and exists the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009610382-Select-Report-Tab-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633601-Send-Message-Dialog)
