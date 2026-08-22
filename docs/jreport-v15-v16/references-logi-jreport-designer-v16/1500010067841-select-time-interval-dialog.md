---
title: "Select Time Interval Dialog"
id: 1500010067841
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067841-Select-Time-Interval-Dialog
updated_at: 2021-07-24T10:38:24Z
---

# Select Time Interval Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032622-Select-Report-Tab-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032642-Send-Message-Dialog)

# Select Time Interval Dialog

The Select Time Interval dialog helps you to specify how a group element will be created based on the specified DBField whose data type is Timestamp/DateTime. It appears when you drag a DBField of the Timestamp/DateTime data type from the Resource Objects panel to the Business View panel in the [Business View Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010064841-Business-View-Editor-Dialog).

![Select Time Interval dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909135255/slcttmintvl.gif)

The following are details about options in the dialog:

**For Each Year**

Specifies to create a group element that uses the expression *Year(@MappingName)* to retrieve years of the current field as its values. The data type of the group element is Integer.

**For Each Quarter**

Specifies to create a group element that uses the expression *Quarter(@MappingName,Integer)* to retrieve quarters of the current field as its values. The data type of the group element is Integer.

**For Each Month**

Specifies to create a group element that uses the expression *Month(@MappingName)*to retrieve months of the current field as its values. The data type of the group element is Integer.

**For Each Week**

Specifies to create a group element that uses the expression *WeekOfYear(@MappingName)*to retrieve weeks of the current field as its values. The data type of the group element is Integer.

**For Each Day**

Specifies to create a group element that uses the expression *Day(@MappingName)*to retrieve days of the current field as its values. The data type of the group element is Integer.

**Keep Original**

Specifies to create a group element based on the field itself.

**OK**

Creates the group elements and closes the dialog.

**Cancel**

Cancels adding group elements and exists the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032622-Select-Report-Tab-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010032642-Send-Message-Dialog)
