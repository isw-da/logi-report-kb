---
title: "Multi-tenancy Supported via Organizations"
id: 1500009675081
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations
updated_at: 2021-07-24T20:53:38Z
---

# Multi-tenancy Supported via Organizations

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650162-Role-Based-Security)

# Multi-tenancy Supported via Organizations

Logi JReport Server supports the multi-tenancy architecture by organizing users into different organizations. An organization is a group of users that has its own administrator. This enables the tenant administrators for fine-grained management of their own resources, security, and user policies.

Organization is a separately licensed feature of Logi JReport Server. It is installed together with Logi JReport Server so only the license key needs to be updated to enable it to work. To find out how to license Organization, please contact Jinfonet sales at [sales@jinfonet.com](mailto:sales@jinfonet.com) or contact your Enterprise Account Manager.

When Logi JReport Server is Organization enabled, users need to specify the organization name before logging in Logi JReport Server. The organization name *System* means that the login user is a non-organization user. For organization users, the correct organization name must be provided, otherwise they cannot log in.

Below is a list of the sections covered in this topic:

* [Organization Definitions](#Definition)
* [Creating Organizations](#Create)
* [Allocating Server Resources to Organizations](#Allocate)
* [Logi JReport Administration Page for Organization Admin](#Admin)
* [Logi JReport Console Page for Organization Users](#Console)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Organization Definitions

There are two types of admin in the server security system:

* **System admin**  
   The administrator who has the administrators role. System admin must be a non-organization user.
* **Organization admin**  
   The administrator who has the administrators role in an organization. You cannot log onto Logi JReport Server Monitor as an organization admin. Only the system admin can log onto Logi JReport Server Monitor and see both organization and non-organization information.

There are two types of users in the server security system:

* **Non-organization users**  
   Belong to no organizations. When upgrading from a version earlier than version 13, the users, groups, and roles in the earlier version are all regarded as non-organization principals.
* **Organization users**  
   Users, groups, and roles created in an organization are called organization users/groups/roles.

  An organization user/group/role can belong to any other non-organization group/role, but a non-organization user/group/role cannot belong to any organization group/role. An organization user/group/role cannot belong to any group/role of other organizations.

  Organization admin cannot add users/groups/roles to non-organization groups/roles.

  The naming rule of an organization user is composed of the organization name and the user name separated by "\". The format is [Organization Name]\[User Name]. For example, a\b, here "a" is the organization name and "b" is the user name.

  If organization is disabled, the organization users/groups/roles will not be supported. However the information will be saved in the server and can be retrieved next time when organization is enabled again.

There are two types of public resources in the server resource system:

* **System public resources**  
   Public resources that can be accessed by all organization users and non-organization users. They are located in the Public Reports and Public Components folders.
* **Organization public resources**  
   Each organization has its own public resources which can only be accessed by the users within the organization. Organization admin has built-in permissions on the organization public resources the same as system admin on the system public resources. Organization public resources are located in the Organization Reports and Organization Components folders.

Within each organization, there is a built-in admin and two built-in roles:

* **Built-in admin**
  + The full name of the default admin is organization administrator, also as organization admin.
  + The organization admin's user name is *admin* and password is *admin*. The password could be changed by the organization admin himself. If the password is forgotten, the system admin can retrieve it since the system admin can reset password for all users.
  + The organization admin owns the administrators role and everyone role by default, and it must always have the administrators role.
* **Two built-in roles** 
  + **administrators**  
     It has no parent role by default. It enables Publish and Advanced Properties privileges by default.
  + **everyone**  
     It has no parent role by default. It disables Publish and Advanced Properties privileges by default.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating Organizations

The system admin can create organizations.

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar and select **Organizations** from the drop-down menu. The Configuration - Organizations page is displayed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920412823/scrty_rsc_srv_ognz.gif)
2. Select the **New Organization**  link. The [New Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009670881-New-Organization) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926655639/nwognz.gif)
3. Specify the name of the organization, the maximum number of users allowed in the organization, and the description about the organization.
4. Select **OK** to create the organization.

The new organization is then added in the organization table which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Organization Name | Displays the organization names. |
| Max Number of Users | Displays the maximum number of users allowed in the organizations. The values are editable. Double-select in the text box and then select a value from the drop-down list or input an integer number in the combo box directly, then select outside of the combo box to accept the change. The **x** in the combo box is used to clear the input text. |
| Description | Displays the information about the organizations. |
| Control | * **Resource Allocation**  Allocates server resources to the specific organization. |

In the organization table, the system admin can sort the organizations by the first three columns, search for required organizations and delete the organizations that are not required.

* To sort the table by certain column, select on the column name.
* To search for organizations, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920383255/btn_mvdown1.gif) on the quick search toolbar above the organization table to specify the search options, type in the text of the organization names in the text box and the organizations containing the matched text will be listed. The quick search toolbar treats the organization names as strings and searches by consecutive text.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.
* To delete any organizations, select the checkboxes ahead of the organizations (to select all organizations check the checkbox on the column header), then select **Delete**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Allocating Server Resources to Organizations

System admin can allocate server resources to different organizations, then when one organization encounters report running performance problems, the other organizations will not be affected. The server resources include maximum concurrent users/reports, maximum disk/memory size, whether to cache catalogs, reports, or images used in the organization and the maximum memory size for them as well as for cached report data and cube, and whether to compress swap files so as to reduce I/O time by increasing CPU usage.

Resource allocation can be achieved either via UI or by modifying the property file.

### Allocating Server Resources via UI

1. Select the **Resource Allocation** link in the Control column of the organization in the organization table. The [Resource Allocation](https://devnet.logianalytics.com/hc/en-us/articles/1500009671141-Resource-Allocation) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926655895/rscalct.gif)
2. Configure the settings as required.
3. Select **OK** to finish allocating resources to the organization.

### Allocating Server Resources by Modifying the Property File

System admin can also modify the organization\_config.properties file in the `<install_root>\properties` folder directly. The property file provides default values to all newly created organizations.

The following table lists the mapping relationship between properties in the file and options in the Resource Allocation dialog.

| Property in organization\_config.properties | Option in the Resource Allocation dialog |
| --- | --- |
| Concurrent\_Users | Maximum Concurrent Users |
| Concurrent\_Reports | Maximum Concurrent Reports |
| Maximum\_Disk\_Size | Disk > Maximum Size |
| Maximum\_Memory\_Size | Memory > Maximum Size |
| Enable\_cache\_catalogs | Cache Catalogs |
| Maximum\_cache\_catalog\_size | Cache Catalogs > Maximum Size |
| Enable\_cache\_reports | Cache Reports |
| Maximum\_cache\_report\_size | Cache Reports > Maximum Size |
| Enable\_cache\_images | Cache Images |
| Maximum\_cache\_image\_size | Cache Images > Maximum Size |
| Maximum\_report\_data\_size | Maximum Report Data Size |
| Maximum\_cube\_size | Maximum Cube Size |
| Compress\_Swap\_Files | Compress Swap Files |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logi JReport Administration Page for Organization Admin

After the system admin create an organization, the organization admin of the organization will be able to log onto the Logi JReport Administration page by the default user name *admin* and the default password *admin* to manage resources and users in this organization and configure Logi JReport Server to adapt for the organization.

The Logi JReport Administration page contains the following subjects on the system toolbar for organization admin:

* **Resources**  
   The Resources page contains two additional folders under the root directory: Organization Reports and Organization Components. They are used to put reports and library components used by the users in the organization.

  Organization admin can publish resources to the My Reports/Components or Organization Reports/Components folder. For the Public Reports/Components folder, organization admin cannot publish resources, update properties, delete resources, or edit NLS. Meanwhile, the feature of using resources from real path is disabled.
* **Configuration**  
   The Configuration page contains the following items:
  Performance, Dynamic Connections, Dynamic Display Names.
* **Security**  
  The Security page contains these items: User, Group, Role, Privilege, and Data Source. Organization admin can only see the users/groups/roles in the organization and cannot change the realm.
* **Cube**  
   In the Cube page there is no Configuration link since the value is retrieved from resource allocation. Organization admin can define cube based on the catalogs used within the organization only.
* **Cache**  
   The Cache page contains the following items:
  + **Data Cache**  
     There is no Cache Configuration link. Organization admin can cache data based on the catalogs used within the organization only.
  + **Report Cache**  
     Organization admin can define which catalogs and reports and how many of them to be cached.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Logi JReport Console Page for Organization Users

The Logi JReport Console > Resources page contains two additional folders under the root directory: Organization Reports and Organization Components. They are used to put reports and library components used by users in the organization.

Organization users cannot see any information about physical disk or import resources from real path. For the Public Reports/Components folder, organization users cannot publish resources, update properties, or delete resources. Organization users can run and edit reports, dashboards, analysis templates in the Public Reports folder, but cannot save the changes directly into the existing resources or into the Public Reports folder. However, they can make use of the Save As function.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674981-Managing-Permissions)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650162-Role-Based-Security)
