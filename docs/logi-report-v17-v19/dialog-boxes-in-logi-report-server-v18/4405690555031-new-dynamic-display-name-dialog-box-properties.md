---
title: "New Dynamic Display Name Dialog Box Properties"
id: 4405690555031
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690555031-New-Dynamic-Display-Name-Dialog-Box-Properties
updated_at: 2022-01-27T07:59:03Z
---

# New Dynamic Display Name Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690554135-New-Dynamic-Connection-Dialog-Box-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683751703-New-Dynamic-Security-Dialog-Box-Properties)

# New Dynamic Display Name Dialog Box Properties

This topic describes how you can use the New Dynamic Display Name dialog box to [add dynamic display names for business view elements](https://devnet.logianalytics.com/hc/en-us/articles/4405683929879-Managing-Dynamic-Display-Names-of-Business-View-Elements) in a catalog for a specified Security Identifier (SID).

Server displays the dialog box when an administrator selects **New Dynamic Display Name** in the Administration > Other > Dynamic Display Names page on the Server Console.

![New Dynamic Display Name dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420447186967/nwdyndsplynm.gif)

**Catalog**

Specify the catalog that contains the business views for which you want to define dynamic display names.

Type the catalog with the full resource path in the text box, for example, `/SampleReports/SampleReports.cat`, or select **Browse** to select a catalog in the [Select Catalog dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683769367-Select-Catalog-Dialog-Box-Properties).

**Organization**

The property is available when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/4405684028567-Multitenancy-Supported-via-Organizations) feature is enabled. System admin can select the organization of the SID. For an organization admin, the organization of the admin is selected by default and cannot be changed.

**SID**

Select the SID for which you want to define dynamic display names. An SID can be a group, role, or user in the [Logi Report Server security system](https://devnet.logianalytics.com/hc/en-us/articles/4405684019735-Security-System-Data-Model). When the value is blank, it means all the users (when the Organization feature is enabled, it means all the users in the specified organization).

**Select Business View Elements**

Select to open the [Select Business View Elements dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683768215-Select-Business-View-Elements-Dialog-Box-Properties) to select business view elements in the specified catalog for which you want to define dynamic display names.

**Delete**

Select to delete the selected business view elements.

**Business view elements table**

After you select the business view elements, you can then delete them if you do not want them. Select the checkbox on the column header to select all the business view elements.

You can also select a column header name to sort the elements either by their qualified names or display names.

* **Business View Element**  
  Qualified names of the business view elements with the path in the catalog.
* **Dynamic Display Name**  
  Display names of the business view elements. Double-click a name box, and then edit the name.

**OK**

Select to apply the dynamic display names and exit the dialog box.

**Cancel**

Select to close the dialog box without adding dynamic display names.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690554135-New-Dynamic-Connection-Dialog-Box-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683751703-New-Dynamic-Security-Dialog-Box-Properties)
