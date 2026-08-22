---
title: "Edit Dynamic Display Name Dialog Box Properties"
id: 1500009745942
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745942-Edit-Dynamic-Display-Name-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:47Z
---

# Edit Dynamic Display Name Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745922-Edit-Dynamic-Connection-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745962-Edit-Group-Dialog-Box-Properties)

# Edit Dynamic Display Name Dialog Box Properties

This topic describes how you can use the Edit Dynamic Display Name dialog box to edit the [dynamic display names for business view elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009777181-Managing-Dynamic-Display-Names-of-Business-View-Elements) in a catalog.

Server displays the dialog box when an admin user selects the Edit link in the Dynamic Display Names column of the Administration > Other > Dynamic Display Names page in the Server Console.

![Edit Dynamic Display Name dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880427159/edtdyndsplynm.gif)

**Catalog**

Displays the catalog with the resource path that contains the required business views for which the dynamic display names are defined.

**Organization**

Displays the organization. The option is available when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) feature is enabled.

**SID**

Specifies the SID for which you want to define dynamic display names. An SID can be a group, role, or user in the Logi Report Server security system. Select a value from the drop-down list. The **x** button in the text box is used to clear the current value. Empty means all the users (when the Organization feature is enabled, empty means all the users in the specified organization).

**Select Business View Elements**

Opens the [Select Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009746382-Select-Business-View-Elements-Dialog-Box-Properties) dialog box to select business view elements in the current catalog for which to define dynamic display names.

**Delete**

Deletes the selected business view elements.

**Business view elements table**

**check boxes are used to** specify whether to select the business view elements. Select the check box on the column header to select all the business view elements. After you select the business view elements, you can then delete them if you do not want them. You can also select the underlined column header name to sort the elements either by their qualified names or display names.

* **Business View Element**Displays the qualified names of the business view elements with the path in the catalog.
* **Dynamic Display Name**Shows the display names of the business view elements. The display names are editable. Select or double-click in a name text box to enter the editing mode and then change the name. The **x** in the text box is used to clear the text.

**OK**

Applies the dynamic display names and exits the dialog box.

**Cancel**

Cancels editing the dynamic display names and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745922-Edit-Dynamic-Connection-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745962-Edit-Group-Dialog-Box-Properties)
