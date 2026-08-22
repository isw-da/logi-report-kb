---
title: "Select Time Interval Dialog Box"
id: 1500010098761
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098761-Select-Time-Interval-Dialog-Box
updated_at: 2021-07-23T19:15:59Z
---

# Select Time Interval Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098741-Select-Report-Tab-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098781-Send-Message-Dialog-Box)

# Select Time Interval Dialog Box

The Select Time Interval dialog box helps you to specify how a group element will be created based on the specified DBField whose data type is Timestamp/DateTime. It appears when you drag a DBField of the Timestamp/DateTime data type from the Resource Objects panel to the Business View panel in the [Business View Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058122-Business-View-Editor-Dialog-Box).

![Select Time Interval dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856849687/slcttmintvl.gif)

The following are details about the options in the dialog box:

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

**Auto Create Hierarchy**

Specifies whether to create a hierarchy which contains the specified group elements. Disabled when none of the above options is selected.

* **Hierarchy Name**  
  Specifies the name of the hierarchy.

**OK**

Creates the group elements and closes the dialog box.

**Cancel**

Cancels adding group elements and exists the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098741-Select-Report-Tab-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098781-Send-Message-Dialog-Box)
