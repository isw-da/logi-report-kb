---
title: "New Dynamic Display Name"
id: 1500009646622
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009646622-New-Dynamic-Display-Name
updated_at: 2021-07-24T20:54:47Z
---

# New Dynamic Display Name

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646602-New-Dynamic-Connection)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646642-New-Dynamic-Security)

# New Dynamic Display Name

The New Dynamic Display Name dialog appears when you select the New Dynamic Display Name link on the Logi JReport Administration > Configuration > Dynamic Display Names page. It helps you to [add dynamic display names for business view elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009648822-Managing-Dynamic-Display-Names-of-Business-View-Elements) in a catalog for a specified SID (security identifier). [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920489495/nwdyndsplynm.gif)

**Catalog**

Specifies the catalog that contains the required business views for which you want to define dynamic display names.

Type the catalog with the full resource path in the text box, for example, `/SampleReports/SampleReports.cat`, or select the **Browse** button to select a catalog in the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009646802-Select-Catalog) dialog.

**Organization**

The option is available when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations) feature is enabled. System admin can select an organization from the drop-down list. For an organization admin, the organization of the admin is selected by default and cannot be changed.

**SID**

Specifies the SID for which you want to define dynamic display names. An SID can be a group, role, or user in the [Logi JReport Server security system](https://devnet.logianalytics.com/hc/en-us/articles/1500009650062-Security-System-Data-Model). Select a value from the drop-down list. The **x** button in the text box is used to clear the current value. Empty means all the users (when the Organization feature is enabled, empty means all the users in the specified organization).

**Select Business View Elements**

Opens the [Select Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009646782-Select-Business-View-Elements) dialog to select business view elements in the specified catalog for which to define dynamic display names.

**Delete**

Deletes the selected business view elements.

**Business view elements table**

**Checkboxes are used to** specify whether or not to select the business view elements. Select the checkbox on the column header to select all the business view elements. After you select the business view elements, you can then delete them if you do not want them. You can also select the underlined column header name to sort the elements either by their qualified names or display names.

* **Business View Element**Displays the qualified names of the business view elements with the path in the catalog.
* **Dynamic Display Name**Shows the display names of the business view elements. The display names are editable. Double-select in a name text box to enter the editing mode and then change the name. The **x** button in the text box is used to clear the text.

**OK**

Applies the dynamic display names and exits the dialog.

**Cancel**

Cancels adding the dynamic display names and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009646602-New-Dynamic-Connection)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009646642-New-Dynamic-Security)
