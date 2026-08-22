---
title: "Managing Dynamic Display Names of Business View Elements"
id: 45204013113101
section: "Managing Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204013113101-Managing-Dynamic-Display-Names-of-Business-View-Elements
updated_at: 2026-04-30T14:10:29Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Managing Dynamic Display Names of Business View Elements 

This topic describes how you can customize, import, and export dynamic display names of business view elements. 

Administrators can define dynamic business view element display names for different SIDs (security identifiers that refer to the users, roles, and groups in the Report Server security system). Then, when any user of a specified SID signs in to Server, Server displays the dynamic display names defined for the SID in the business view resource tree. For business view elements that do not have dynamic display names, Server displays their original display names.

Dynamic display name resources have higher priority than NLS resources.

This topic contains the following sections:

- Adding Dynamic Display Names for Business View Elements

- Editing Dynamic Display Names

- Importing/Exporting Dynamic Display Names from/to a Resource Bundle File

## 
Adding Dynamic Display Names for Business View Elements

To create dynamic display names for business view elements in a catalog for a specified SID (security identifier), take the following steps:

- On the system toolbar of the Server Console, navigate to Administration > Other > Dynamic Display Names. Server displays the Dynamic Display Names page.
    

- Select New Dynamic Display Name. Server displays the New Dynamic Display Name dialog box.
    

- In the Catalog text box, type the catalog resource path, or select Browse to select one from the server resource tree. 

- If the Organization option is available and editable, select an organization from the drop-down list. The item System is a category to include users that do not belong to any organizations.

- From the SID drop-down list, select a user, role, or group for whom the dynamic display names will take effect. If left blank, it means all the users (when Server enables the Organization feature, blank means all the users in the specified organization).

- Select Select Business View Elements. Server displays the Select Business View Elements dialog box.
    

- Select the business view elements in the catalog that you would like to define dynamic display names for the specified SID. To select all the elements, select All. Then select OK to go back to the New Dynamic Display Name dialog box.

- Server lists the selected business view elements in the business view elements table. You can change their display names in the Dynamic Display Name column: double-click in a name text box to enter the editing mode, change the name, then select outside of the text box to accept the change.
    To remove a view element from the table, select it, then select Delete. You can select multiple elements and remove them at a time. 

- Select OK to finish editing the names.

Server adds a new dynamic display name resource row in the resource table which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Catalog | The catalogs of the dynamic display name resources with the full resource path, for example, /SampleReports/SampleReports.cat. |
| Organization | The organizations that the SIDs belong to. The column is available to system admin when Server enables the Organization feature. |
| SID | The security identifiers (SID). SID can be a group, a role, or a user in the Server security system. |
| Dynamic Display Names | You can perform the following tasks: Edit Edit the specified dynamic display name resource. Import Import dynamic display names from a local resource bundle file. Export Export the dynamic display names to a resource bundle file. |

In the resource table, the system admin can sort the resources by the first three columns or delete the resources that are not required.

- To sort the resources by a column, select on the column name.

- To delete any resources, select the resources (to select all resources, select the checkbox on the column header), then select Delete.

## 
Editing Dynamic Display Names

To edit the dynamic display names defined for a specific SID, in the Dynamic Display Names page, select its corresponding Edit in the Dynamic Display Names column. In the Edit Dynamic Display Name dialog box, edit the dynamic display names. You can make the dynamic display names apply to another SID if you want.

## 
Importing/Exporting Dynamic Display Names from/to a Resource Bundle File

A resource bundle file is a properties file with .properties as the suffix. It defines dynamic display names by key/value pairs. The key is a qualified object name. The format is [Data Source Name].[Business View Name].[Category Name].[Element Name], for example, Data Source 1.WorldWideSalesBV.Customers.Customer Name. The value is a dynamic display name.

See the following example of the contents of a resource bundle file:

Data Source 1.SalesStatForRegionBV.Account Managers.Assigned Region=Region
Data Source 1.WorldWideSalesBV.Customers.Customer Name=Customer
Data Source 1.SalesStatForRegionBV.Account Managers=Managers

To import dynamic display names from a resource bundle file:

- Locate the dynamic display name resource defined for a specific SID in the Dynamic Display Names page and select Import in the Dynamic Display Names column. 

- Server displays the Select Dynamic Display Name File dialog box. Select Browse to select a local resource bundle file that defines the dynamic display names of the business view elements in a catalog. 

- Select OK. 

The dynamic display names defined in the resource bundle file will overwrite those in the current dynamic display name resource.

To export dynamic display names to a resource bundle file:

Locate the dynamic display name resource defined for a specific SID on in the Dynamic Display Names page and select Export in the Dynamic Display Names column. Server exports the dynamic display names defined in the resource to a resource bundle file.
