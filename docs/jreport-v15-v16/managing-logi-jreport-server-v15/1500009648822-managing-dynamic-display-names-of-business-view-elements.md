---
title: "Managing Dynamic Display Names of Business View Elements"
id: 1500009648822
section: "Managing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648822-Managing-Dynamic-Display-Names-of-Business-View-Elements
updated_at: 2021-07-24T20:54:03Z
---

# Managing Dynamic Display Names of Business View Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648862-Linking-Resources-and-Catalogs)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673601-Deleting-Resources)

# Managing Dynamic Display Names of Business View Elements

Administrators can define dynamic business view element display names for different SIDs (security identifiers that refer to the users, roles and groups in the [Logi JReport Server security system](https://devnet.logianalytics.com/hc/en-us/articles/1500009650062-Security-System-Data-Model)). Then, when any user of a specified SID logs onto Logi JReport Server, the dynamic display names defined for the SID will be shown in the business view resource tree.

Dynamic display name resources have higher priority than NLS resources.

For business view elements that are not given dynamic display names, their original display names will be used.

Below is a list of the sections covered in this topic:

* [Adding Dynamic Display Names for Business View Elements](#Add)
* [Editing Dynamic Display Names](#Edit)
* [Importing/Exporting Dynamic Display Names From/to a Resource Bundle File](#Import)

## Adding Dynamic Display Names for Business View Elements

To create dynamic display names for business view elements in a catalog for a specified SID (security identifier), take the following steps:

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar and select **Dynamic Display Names** from the drop-down menu. The Configuration - Dynamic Display Names page is displayed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920489239/mng_rsc_dyndsplynm.gif)
2. Select the **New Dynamic Display Name** link. The [New Dynamic Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009646622-New-Dynamic-Display-Name) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920489495/nwdyndsplynm.gif)
3. In the Catalog text box, type in the catalog resource path, or select **Browse** to select one from the server resource tree.
4. If the Organization option is available and editable, select an organization from the drop-down list. System is a category to include non-organization users.
5. From the SID drop-down list, select a user, role or group for whom the dynamic display names will take effect. If left blank, it means all the users (when the [Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations) feature is enabled, blank means all the users in the specified organization).
6. Select the **Select Business View Elements** link, and the [Select Business View Elements](https://devnet.logianalytics.com/hc/en-us/articles/1500009646782-Select-Business-View-Elements) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920489751/slctbvelmnt.gif)
7. Select the business view elements in the catalog that you would like to define dynamic display names for the specified SID. To select all of the elements, select the **All** checkbox. Then select **OK** to go back to the New Dynamic Display Name dialog.
8. The selected business view elements will be listed in the business view elements table. Change their display names in the Dynamic Display Name column: double-click in a name text box to enter the editing mode, change the name, then select outside of the text box to accept the change.

   To remove a view element from the table, check the checkbox ahead of it, then select the **Delete** link above the table. You can select multiple elements and remove them at a time.
9. Select **OK** to finish editing the names.

   A new dynamic display name resource row is now added in the resource table which consists of the following columns.

   | Column Name | Description |
   | --- | --- |
   | Catalog | Displays the catalogs of the dynamic display name resources with the full resource path, for example, `/SampleReports/SampleReports.cat`. |
   | Organization | Shows the organizations that the SIDs belong to. The column is available to system admin when the Organization feature is enabled. |
   | SID | Displays the security identifiers (SID). An SID can be a group, a role, or a user in the Logi JReport Server security system. |
   | Dynamic Display Names | You can perform the following tasks: * **Edit**  Edits the specified dynamic display name resource. * **Import**  Imports dynamic display names from a local resource bundle file. * **Export**  Exports the dynamic display names to a resource bundle file. |

In the resource table, the system admin can sort the resources by the first three columns or delete the resources that are not required.

* To sort the table by certain column, select on the column name.
* To delete a resource row, select the checkbox ahead of the resource row and then select **Delete**. To delete all the resource rows at a time, select the checkbox on the column header and then select **Delete**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Editing Dynamic Display Names

To edit the dynamic display names defined for a specific SID, on the Configuration - Dynamic Display Names page, select its corresponding **Edit** link in the Dynamic Display Names column. In the [Edit Dynamic Display Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009670781-Edit-Dynamic-Display-Name) dialog, edit the dynamic display names as required. You can make the dynamic display names applied to another SID if you want.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Importing/Exporting Dynamic Display Names From/to a Resource Bundle File

A resource bundle file is a properties file with .properties as the suffix. It defines dynamic display names by key/value pairs. The key is a qualified object name. The format is *[Data Source Name]**.**[Business View Name]**.**[Category Name]**.**[Element Name]*, for example, Data Source 1.WorldWideSalesBV.Customers.Customer Name. The value is a dynamic display name.

Here is an example of the contents of a resource bundle file:

`Data Source 1.SalesStatForRegionBV.Account Managers.Assigned Region=Region  
Data Source 1.WorldWideSalesBV.Customers.Customer Name=Customer  
Data Source 1.SalesStatForRegionBV.Account Managers=Managers`

**To import dynamic display names from a resource bundle file:**

Locate the dynamic display name resource defined for a specific SID on the Configuration - Dynamic Display Names page and select **Import** in the Dynamic Display Names column. In the [Select Dynamic Display Name File](https://devnet.logianalytics.com/hc/en-us/articles/1500009646842-Select-Dynamic-Display-Name-File) dialog, select **Browse** to select a local resource bundle file that defines the dynamic display names of the business view elements in a catalog and select **OK**. The dynamic display names defined in the resource bundle file will overwrite those in the current dynamic display name resource.

**To export dynamic display names to a resource bundle file:**

Locate the dynamic display name resource defined for a specific SID on the Configuration - Dynamic Display Names page and select **Export** in the Dynamic Display Names column. The dynamic display names defined in the resource will be exported to a resource bundle file.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648862-Linking-Resources-and-Catalogs)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673601-Deleting-Resources)
