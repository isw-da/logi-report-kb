---
title: "Multitenancy Supported via Organizations"
id: 45204016966797
section: "Report Server Security System Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204016966797-Multitenancy-Supported-via-Organizations
updated_at: 2026-04-30T14:10:53Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Multitenancy Supported via Organizations

Report Server supports the multitenancy architecture by organizing users into different organizations. This topic describes the definition of Organization, and how you can create organizations and allocate server resources to organizations. System admin can create and manage organizations.

An organization is a group of users that has its own administrator. This enables the tenant administrators for fine-grained management of their own resources, security, and user policies. 

The Organization feature is a separately licensed feature of Report Server. It is installed together with Report Server so only the license key needs updating to enable it to work. For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

When Report Server enables Organization, you need to specify the organization name before signing into Report Server. The default organization name System means that you do not belong to any organizations. if you are an organization user, you need to provide the correct organization name, otherwise you cannot sign in.

This topic contains the following sections:

- Organization Definitions

- Creating Organizations

- Allocating Server Resources to Organizations

## 
Organization Definitions

To use the Organization feature, you should first have a general idea of the following:

- 
System admin
    The overall server system administrator who has the administrators role. System admin must be a user that does not belong to any organizations.

- 
Organization admin
    The administrator who has the administrators role in an organization. You cannot sign in to Report Server Monitor as an organization admin. Only the system admin can sign in to Report Server Monitor and view both organization and non-organization information. The organization admin of an organization can manage resources and users in the organization and configure Report Server to adapt for the organization the same as system admin does. However, some administration features are unavailable to an organization admin.

- 
Non-organization users
    Belong to no organizations. When you server upgraded from a version earlier than version 13, the users, groups, and roles in the earlier version are all regarded as non-organization principals.

- 
Organization users
    Users, groups, and roles that you created in an organization are called organization principals.
       An organization principal can belong to any other non-organization group/role, but a non-organization principal cannot belong to any organization group/role. An organization principal cannot belong to any group/role of other organizations.

Organization admin cannot add principals to non-organization groups/roles.

The naming rule of an organization user is composed of the organization name and the username separated by "\". The format is [Organization Name]\[Username]. For example, a\b, here "a" is the organization name and "b" is the username.

If organization is disabled, the organization principals will not be supported. However, the information will be saved in the server and can be retrieved next time when organization is enabled again.

- 
System public resources
    Public resources in the Public Reports and Public Components folders, that all organization users and non-organization users can access.

- 
Organization public resources
    Each organization has its own public resources that only the users within the organization can access. Organization admin has built-in permissions on the organization public resources the same as system admin on the system public resources. Organization public resources are in the Organization Reports and Organization Components folders.

## 
Creating Organizations

- On the system toolbar of the Server Console, navigate to Administration > Security > Organization. Server displays the Organization page.
    

- Select New Organization. Server displays the New Organization dialog box.
    

- Specify the name of the organization, the maximum number of users allowed in the organization, and the description about the organization.

- Select OK to create the organization. 

Server adds the new organization in the organization table which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Organization Name | The organization names. |
| Max Number of Users | The maximum number of users allowed in the organizations. The values are editable. Double-click in the text box and then select a value from the drop-down list or type an integer number in the combo box directly, then select outside of the combo box to accept the change. You can select the x in the combo box to clear the input text. |
| Description | The information about the organizations. It is editable. |
| Control | Resource Allocation Select if you want to allocate server resources to the specific organization. |

In the organization table, the system admin can sort the organizations by the first three columns, search for required organizations, change the maximum number of users in an organization, and delete the organizations that are not required.

- To sort the organizations by a column, select on the column name.

- To search for organizations, in the Search box, type the text in the organization names you want to search for. Server lists the organizations that contain the matched text. After typing text in the Search box, you can select  in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select .

- To change the maximum number of users in an organization, in the Max Number of Users text box for the organization, select a value from the drop-down list or type an integer number in the combo box directly. 

- To delete any organizations, select the organizations (to select all organizations, select the checkbox on the column header), then select Delete above the table.

## 
Allocating Server Resources to Organizations

You can allocate server resources to different organizations, then when one organization encounters report running performance problems, it will not affect the other organizations. The server resources include maximum concurrent users/reports, maximum disk/memory size, whether to cache catalogs, reports, or images used in the organization and the maximum memory size for them as well as for cached report data and cube, and whether to compress swap files to reduce I/O time by increasing CPU usage.

You can achieve resource allocation either via UI or by modifying the property file.

- 
Allocating via UI
- Select Resource Allocation of the organization in the Control column of the organization table. Server displays the Resource Allocation dialog box.
        

- Configure the settings

- Select OK to finish allocating resources to the organization. 

- 
Allocating by modifying property fileYou can also modify the organization_config.properties file in the <install_root>\properties folder directly. The property file provides default values to all newly created organizations.

The following table lists the mapping relationship between properties in the file and options in the Resource Allocation dialog box.

| Property in organization_config.properties | Option in the Resource Allocation dialog box |
| --- | --- |
| Concurrent_Users | Maximum Concurrent Users |
| Concurrent_Reports | Maximum Concurrent Reports |
| Maximum_Disk_Size | Disk > Maximum Size |
| Maximum_Memory_Size | Memory > Maximum Size |
| Enable_cache_catalogs | Cache Catalogs |
| Maximum_cache_catalog_size | Cache Catalogs > Maximum Size |
| Enable_cache_reports | Cache Reports |
| Maximum_cache_report_size | Cache Reports > Maximum Size |
| Enable_cache_images | Cache Images |
| Maximum_cache_image_size | Cache Images > Maximum Size |
| Maximum_report_data_size | Maximum Report Data Size |
| Maximum_cube_size | Maximum Cube Size |
| Compress_Swap_Files | Compress Swap Files |
