---
title: "New Dynamic Display Name"
id: 1500009688802
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009688802-New-Dynamic-Display-Name
updated_at: 2021-11-03T06:57:41Z
---

# New Dynamic Display Name

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009688782-New-Dynamic-Connection)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009688822-New-Dynamic-Security)

# New Dynamic Display Name

The New Dynamic Display Name dialog helps you to [add dynamic display names for business view elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009717801-Managing-Dynamic-Display-Names-of-Business-View-Elements) in a catalog for a specified Security Identifier (SID). It appears when you select the New Dynamic Display Name link in the Administration > Other > Dynamic Display Names page in the server console.

![New Dynamic Display Name dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131437719/nwdyndsplynm.gif)

**Catalog**

Specifies the catalog that contains the required business views for which you want to define dynamic display names.

Type the catalog with the full resource path in the text box, for example, `/SampleReports/SampleReports.cat`, or select the **Browse** button to select a catalog in the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009715121-Select-Catalog) dialog.

**Organization**

The option is available when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009692742-Multi-tenancy-Supported-via-Organizations) feature is enabled. System admin can select an organization from the drop-down list. For an organization admin, the organization of the admin is selected by default and cannot be changed.

**SID**

Specifies the SID for which you want to define dynamic display names. An SID can be a group, role, or user in the [Logi JReport Server security system](https://devnet.logianalytics.com/hc/en-us/articles/1500009718821-Security-System-Data-Model). Select a value from the drop-down list. The **x** button in the text box is used to clear the current value. Empty means all the users (when the Organization feature is enabled, empty means all the users in the specified organization).

**Select Business View Elements**

Opens the [Select Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009689062-Select-Business-View-Elements) dialog to select business view elements in the specified catalog for which to define dynamic display names.

**Delete**

Deletes the selected business view elements.

**Business view elements table**

**Checkboxes are used to** specify whether or not to select the business view elements. Select the checkbox on the column header to select all the business view elements. After you select the business view elements, you can then delete them if you do not want them. You can also select the underlined column header name to sort the elements either by their qualified names or display names.

* **Business View Element**Displays the qualified names of the business view elements with the path in the catalog.
* **Dynamic Display Name**Shows the display names of the business view elements. The display names are editable. Double-click in a name text box to enter the editing mode and then change the name. The **x** button in the text box is used to clear the text.

**OK**

Applies the dynamic display names and exits the dialog.

**Cancel**

Cancels adding the dynamic display names and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009688782-New-Dynamic-Connection)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009688822-New-Dynamic-Security)
