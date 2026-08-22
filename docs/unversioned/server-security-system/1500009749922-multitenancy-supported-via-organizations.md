---
title: "Multitenancy Supported via Organizations"
id: 1500009749922
section: "Server Security System"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations
updated_at: 2021-07-24T00:47:34Z
---

# Multitenancy Supported via Organizations

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749942-Role-Based-Security)

# Multitenancy Supported via Organizations

Logi Report Server supports the multitenancy architecture by organizing users into different organizations. This topic describes the definition of Organization, and how you can create organizations and allocate server resources to organizations. System admin can create and manage organizations.

An organization is a group of users that has its own administrator. This enables the tenant administrators for fine-grained management of their own resources, security, and user policies.

The Organization feature is a separately licensed feature of Logi Report Server. It is installed together with Logi Report Server so only the license key needs updating to enable it to work. To find out how to license Organization, contact Logi Analytics sales at [sales@jinfonet.com](mailto:sales@jinfonet.com) or contact your Enterprise Account Manager.

When Logi Report Server enables Organization, you need to specify the organization name before logging onto Logi Report Server. The default organization name *System* means that the login user does not belong to any organizations. if you are an organization user, you need to provide the correct organization name, otherwise you cannot log in.

This topic contains the following sections:

* [Organization Definitions](#Definition)
* [Creating Organizations](#Create)
* [Allocating Server Resources to Organizations](#Allocate)

## Organization Definitions

To use the Organization feature, you should first have a general idea of the following:

* **System admin**  
   The overall server system administrator who has the administrators role. System admin must be a user that does not belong to any organizations.
* **Organization admin**  
   The administrator who has the administrators role in an organization. You cannot log onto Logi Report Server Monitor as an organization admin. Only the system admin can log onto Logi Report Server Monitor and view both organization and non-organization information. The organization admin of an organization can manage resources and users in the organization and configure Logi Report Server to adapt for the organization the same as system admin does. However, some administration features are unavailable to an organization admin.

* **Non-organization users**  
   Belong to no organizations. When you server upgraded from a version earlier than version 13, the users, groups, and roles in the earlier version are all regarded as non-organization principals.
* **Organization users**  
   Users, groups, and roles that you created in an organization are called organization principals.

  An organization principal can belong to any other non-organization group/role, but a non-organization principal cannot belong to any organization group/role. An organization principal cannot belong to any group/role of other organizations.

  Organization admin cannot add principals to non-organization groups/roles.

  The naming rule of an organization user is composed of the organization name and the user name separated by "\". The format is [Organization Name]\[User Name]. For example, a\b, here "a" is the organization name and "b" is the user name.

  If organization is disabled, the organization principals will not be supported. However, the information will be saved in the server and can be retrieved next time when organization is enabled again.

* **System public resources**  
   Public resources in the Public Reports and Public Components folders, that all organization users and non-organization users can access.
* **Organization public resources**  
   Each organization has its own public resources that only the users within the organization can access. Organization admin has built-in permissions on the organization public resources the same as system admin on the system public resources. Organization public resources are in the Organization Reports and Organization Components folders.

## Creating Organizations

1. In the Server Console, point to **Administration** on the system toolbar, and then select **Security** > **Organization** from the drop-down menu. Server displays the Organization page.

   ![Organization page](https://devnet.logianalytics.com/hc/article_attachments/4404880207127/scrty_rsc_srv_ognz.gif)
2. Select the **New Organization**  link. Server displays the [New Organization](https://devnet.logianalytics.com/hc/en-us/articles/1500009746202-New-Organization-Dialog-Box-Properties) dialog box.

   ![New Organization dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885354391/nwognz.gif)
3. Specify the name of the organization, the maximum number of users allowed in the organization, and the description about the organization.
4. Select **OK** to create the organization.

Server adds the new organization in the organization table which consists of the following columns.

| Column Name | Description |
| --- | --- |
| Organization Name | The organization names. |
| Max Number of Users | The maximum number of users allowed in the organizations. The values are editable. Double-click in the text box and then select a value from the drop-down list or type an integer number in the combo box directly, then select outside of the combo box to accept the change. You can select the **x** in the combo box to clear the input text. |
| Description | The information about the organizations. It is editable. |
| Control | * **Resource Allocation**  Select if you want to allocate server resources to the specific organization. |

In the organization table, the system admin can sort the organizations by the first three columns, search for required organizations, change the maximum number of users in an organization, and delete the organizations that are not required.

* To sort the organizations by a column, select on the column name.
* To search for organizations, in the Search box, type the text in the organization names you want to search for. Server lists the organizations that contain the matched text. After typing text in the Search box, you can select ![Search Options](https://devnet.logianalytics.com/hc/article_attachments/4404885328919/btn_mvdown1.gif) in the box to specify the following search options: Highlight All, Match Case, and Match Whole Word. To cancel the search operation, clear the text or select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885308823/btn_dltobj.gif).

* To change the maximum number of users in an organization, in the **Max Number of Users** text box for the organization, select a value from the drop-down list or type an integer number in the combo box directly.
* To delete any organizations, select the organizations (to select all organizations, select the check box on the column header), then select **Delete** above the table.

## Allocating Server Resources to Organizations

You can allocate server resources to different organizations, then when one organization encounters report running performance problems, it will not affect the other organizations. The server resources include maximum concurrent users/reports, maximum disk/memory size, whether to cache catalogs, reports, or images used in the organization and the maximum memory size for them as well as for cached report data and cube, and whether to compress swap files to reduce I/O time by increasing CPU usage.

You can achieve resource allocation either via UI or by modifying the property file.

* **Allocating via UI**
  1. Select the **Resource Allocation** link of the organization in the Control column of the organization table. Server displays the [Resource Allocation](https://devnet.logianalytics.com/hc/en-us/articles/1500009774541-Resource-Allocation-Dialog-Box-Properties) dialog box.

     ![Resource Allocation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880207767/rscalct.gif)
  2. Configure the settings
  3. Select **OK** to finish allocating resources to the organization.
* **Allocating by modifying property file**

  You can also modify the **organization\_config.properties** file in the `<install_root>\properties` folder directly. The property file provides default values to all newly created organizations.

  The following table lists the mapping relationship between properties in the file and options in the Resource Allocation dialog box.

  | Property in organization\_config.properties | Option in the Resource Allocation dialog box |
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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749942-Role-Based-Security)
