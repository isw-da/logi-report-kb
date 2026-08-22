---
title: "Using LDAP Server's Security Information"
id: 1500009675061
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675061-Using-LDAP-Server-s-Security-Information
updated_at: 2021-07-24T20:53:38Z
---

# Using LDAP Server's Security Information

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650142-Configuring-the-LDAP-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675041-SSL-Support-in-LDAP-System-)

# Using LDAP Server's Security Information

LDAP (Lightweight Directory Access Protocol) is a lightweight client-server protocol for accessing directory services. With LDAP support, Logi JReport Server enables you to import users/groups from directory servers. Logi JReport Server can also access an LDAP server directly using the LDAP Security API implementation.

Below is a list of the sections covered in this topic:

* [*Importing LDAP Server Security Information*](#Import)
* [*Using the LDAP Implementation of the Security API*](#API)

## Importing LDAP Server Security Information

### Importing LDAP Users Automatically

If the Enable Auto-Import of Users from LDAP Server option in the Configuration > LDAP > Server tab has been checked while configuring the LDAP server, LDAP users will automatically be imported into Logi JReport Server when they log in for the first time. The Enable LDAP Support and Enable Auto-Import of Users from LDAP Server options in the Configuration > LDAP > Server tab work together. The former determines whether an imported LDAP user can be used in Logi JReport Server, and the latter determines whether LDAP users can be imported automatically, as shown in the following table:

![](https://devnet.logianalytics.com/hc/article_attachments/4404926656407/scrty_rsc_srv_ldap_impt1.gif)=Checked; ![](https://devnet.logianalytics.com/hc/article_attachments/4404926656663/scrty_rsc_srv_ldap_impt2.gif)=Unchecked

|  | Enable LDAP Support | Enable Auto-Import of Users from LDAP Server | Can be used |
| --- | --- | --- | --- |
| Local User |  |  | YES |
|  |  | YES |
|  |  | YES |
|  |  | YES |
| Imported LDAP User |  |  | YES |
|  |  | YES |
|  |  | NO |
|  |  | NO |
| None-Imported LDAP User |  |  | YES |
|  |  | NO |
|  |  | NO |
|  |  | NO |

**Importing LDAP users and groups manually**

You can also import LDAP users and groups into the Logi JReport Server's security system manually.

1. On the Logi JReport Administration page, select **Configuration** on the system toolbar and then select **LDAP** from the drop-down menu to open the Configuration - LDAP page. Select the **Import** tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926656919/scrty_rsc_srv_ldap_use_impt.gif)
2. Specify whether LDAP users will overwrite local users or be replaced by local users after LDAP users are imported into Logi JReport Server.

   If you have imported users/groups from the LDAP server to Logi JReport Server before and you want to import them again, in order to prevent the information of the users/groups on Logi JReport Server from being overwritten by the newly imported users/groups, you should check Local users overwrite LDAP users and then import the users/groups.
3. To view the LDAP users and groups that have the same names as the users and groups in Logi JReport Server, select the **List Users** and **List Groups** buttons.
4. Import the LDAP users and groups to Logi JReport Server.
   * To import LDAP users select **Import Users**, the users on the LDAP server are then listed. To import some of them, select them and then select **Import**; to import all of them, select **Import All**.
   * To import LDAP groups select **Import Groups**, the groups on the LDAP server are then listed. To import some of them, select them and then select **Import**; to import all of them, select **Import All**.
   * To import all LDAP users and groups, select the **Import All** button.

   The selected or all LDAP users/groups will then be imported based on the specified overwriting rule. Any LDAP group that has the same name as a group on Logi JReport Server will be merged into the local group.

**Notes:**

* There is an admin group named Administrators on the LDAP Server. If you perform an import operation, all groups will then be imported except for the Administrators group.
* In the case of a non-admin group on the LDAP Server having the same name as a non-admin group on Logi JReport Server, if you perform an import operation, all users from the non-admin group on the LDAP Server will be merged into the non-admin group of Logi JReport Server.
* When the system built-in admin user logs in Logi JReport Server, Logi JReport always tries the system built-in password first (admin by default). This is to provide a backdoor password for admin in case the LDAP server is down.

### Synchronizing Local Security Information With That of LDAP Server

In order to have the most current security information, you can schedule a task to synchronize the security information of Logi JReport Server with that of the LDAP server. The synchronization process first compares the security information on both Logi JReport Server and the LDAP server. Then if necessary, it updates the information on Logi JReport Server so that both sides are consistent. However, for security reasons this process does not automatically import the newly-added users or groups from the LDAP server.

To schedule a synchronization task, take the following steps:

1. On the Logi JReport Administration > Configuration > LDAP page, go to the Synchronize tab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920413719/scrty_rsc_srv_ldap_use_sync.gif)
2. Select the **Edit** link in the LDAP Synchronization Schedule Settings table.
3. From the Select time type to synchronize drop-down list, specify the time for when the task is to be performed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926657431/scrty_rsc_srv_ldap_use_schdl.gif)

   * To run the task at a specified time, select **Run this task at**, then define the date and time according to your requirement.
   * If you want to run the task repeatedly, select  **Run this task periodically**, then specify the duration, date and time accordingly.
4. Select **Save** to apply the schedule settings.

Information about the synchronization task is then displayed in LDAP Synchronization Schedule Settings table and the synchronization task is enabled by default. You can perform the following operations on the task:

* To edit the task, select the **Edit** link and then modify the schedule settings.
* To disable the task, select **Disable**; to enable the task again, select **Enable**.
* To view information about the last run of the synchronization task, select the **Detail** link.

You can also manually start the synchronization by selecting the **Synchronize Now** button. Then when the synchronization is completed, the Synchronization Information table will be displayed showing which users and roles/groups have been modified and removed. Select **Back** to return to the Synchronize tab.

### Defining Role Maps

You can predefine role maps for the imported LDAP users, then when an LDAP user account is automatically imported, Logi JReport Server can automatically assign it to specific roles according to the predefined role map. A role map consists of two parts: Search Filter String and Corresponding Role Name. When an imported LDAP user account matches the filter condition (specified by Search Filter String), it will automatically be added to a specific role (specified by Corresponding Role Name).

To create a role map, follow the steps below:

1. On the Logi JReport Administration > Configuration > LDAP page, go to the Role Maptab.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920414231/scrty_rsc_srv_ldap_use_role.gif)
2. Select the **Create New Role Map** link.
3. In the Search Filter String text box, input the search filter criteria.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926658327/scrty_rsc_srv_ldap_use_map.gif)
4. From the Corresponding Role drop-down list, select a role to which you want to assign the matching users.
5. Select **Test** to test the contents of the filter. The result of the test does not affect the creation of the new role map.
6. Select **Save** to create the role map.

You can create more role maps following the above steps. The role maps are listed in the role map table. You can perform the following tasks on the role maps if required:

* To edit a role map, select the **Edit** link in the role map row and then modify the settings.
* To test the contents of the filter of a role map, select **Test** in the role map row.
* To remove unwanted role maps, select the checkboxes ahead of them and select **Delete**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Using the LDAP Implementation of the Security API

To access an LDAP server directly using the LDAP Security API implementation, you will need to turn on the LDAP security providers. There are three approaches to achieve this:

* **Configuring on the Logi JReport Administration page**  
   In the Server tab of the Logi JReport Administration > Configuration > LDAP page, check **Enable Direct Authentication to LDAP Server**.
* **Editing the LDAP .xml configuration file**Specify the following property in the LDAP .xml configuration file:

  `<env-enableNoneImportedLDAPSupport>true</env-enableNoneImportedLDAPSupport>`.

  If the value is true, Logi JReport Server security system will then use the LDAP providers. The default value of this property is false.
* **Configuring by API method**Invoke the following two methods in the interface ConfigurationLDAPServer:

  |  |
  | --- |
  | ``` /**  * Specifies whether or not the Server security system uses the LDAP providers. * @return Returns true if using none imported LDAP support, otherwise returns false. */ public boolean isEnableNoneImportedLDAPSupport(); /** * Specifies whether or not the Server security system uses none imported LDAP support. * @param isEnableNoneImportedLDAPSupport Set this parameter to true if the Server  security system uses none imported LDAP support, otherwise set it to false. */ public void setEnableNoneImportedLDAPSupport (boolean isEnableNoneImportedLDAPSupport); ``` |

To use LDAP security providers, a valid admin user is required to manage the Logi JReport Server. The following are rules for checking whether or not a user is an admin user:

* Whether or not the user is a member of the LDAP admin group. The LDAP admin group is a configuration option in the LDAP configuration XML file.
* Whether or not the user is a member of the administrators role. The user can be granted the role by a role map.

A user that meets one of these two rules is regarded as an admin user, and is thus allowed to access the Logi JReport Administration page.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650142-Configuring-the-LDAP-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675041-SSL-Support-in-LDAP-System-)
