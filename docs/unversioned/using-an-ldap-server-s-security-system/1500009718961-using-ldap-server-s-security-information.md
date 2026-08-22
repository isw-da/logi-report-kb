---
title: "Using LDAP Server's Security Information"
id: 1500009718961
section: "Using an LDAP Server's Security System"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718961-Using-LDAP-Server-s-Security-Information
updated_at: 2021-11-03T06:56:31Z
---

# Using LDAP Server's Security Information

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692722-Configuring-the-LDAP-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718941-SSL-Support-in-the-LDAP-System)

# Using LDAP Server's Security Information

The Logi JReport Server security system can run two modes in which you can use an LDAP server's security system: importing mode and non-importing mode. Below diagram illustrates these two working modes:

![Working Mode](https://devnet.logianalytics.com/hc/article_attachments/4412131402263/scrty_rsc_srv_ldap_use1.gif)

Importing mode: You can import LDAP server's security information into the Logi JReport Server security system (red line) so as to use them in Logi JReport Server.

Non-importing mode: Logi JReport Server can access an LDAP server and obtain LDAP security information directly using the LDAP implementation of the Security API (blue line).

Below is a list of the sections covered in this topic:

* [Importing from the LDAP Server](#Import)
  + [Importing LDAP Users Automatically](#Auto)
  + [Importing LDAP Users and Groups Manually](#Manual)
  + [Synchronizing Local Security Information with That of LDAP Server](#Sync)
  + [Defining Role Maps](#Map)
* [Using the LDAP Implementation of the Security API](#API)

## Importing from the LDAP Server

LDAP server's security information can be imported into the Logi JReport Server security system either automatically or manually. You can also schedule a task to synchronize the security information of Logi JReport Server with that of the LDAP server so as to get the LDAP server's most current security information. By predefining role maps, you can make Logi JReport Server automatically assign the imported LDAP users to specific Logi JReport Server roles.

### Importing LDAP Users Automatically

If the Enable Auto-Import of Users from LDAP Server option in the Configuration > LDAP > Server tab is checked while [configuring the LDAP server](https://devnet.logianalytics.com/hc/en-us/articles/1500009692722-Configuring-the-LDAP-Server), LDAP users will automatically be imported into Logi JReport Server when they log in for the first time. The Enable LDAP and Enable Auto-Import of Users from LDAP Server options in the Configuration > LDAP > Server tab work together. The former determines whether an imported LDAP user can be used in Logi JReport Server, and the latter determines whether LDAP users can be imported automatically, as shown in the following table:

![Checked](https://devnet.logianalytics.com/hc/article_attachments/4412112521879/scrty_rsc_srv_ldap_use2.gif)=Checked; ![Unchecked](https://devnet.logianalytics.com/hc/article_attachments/4412131402519/scrty_rsc_srv_ldap_use3.gif)=Unchecked

|  | Enable LDAP | Enable Auto-Import of Users from LDAP Server | Can Be Used |
| --- | --- | --- | --- |
| **Local User** | Checked | Checked | YES |
| Checked | Unchecked | YES |
| Unchecked | Checked | YES |
| Unchecked | Unchecked | YES |
| **Imported LDAP User** | Checked | Checked | YES |
| Checked | Unchecked | YES |
| Unchecked | Checked | NO |
| Unchecked | Unchecked | NO |
| **Non-Imported LDAP User** | Checked | Checked | YES |
| Checked | Unchecked | NO |
| Unchecked | Checked | NO |
| Unchecked | Unchecked | NO |

### Importing LDAP Users and Groups Manually

You can also import LDAP users and groups into Logi JReport Server's security system manually.

1. In the Logi JReport Server console, point to **Administration** on the system toolbar, and then select **Security** >  **LDAP** from the drop-down menu to open the LDAP page. Select the **Import** tab.

   ![LDAP page](https://devnet.logianalytics.com/hc/article_attachments/4412131402775/scrty_rsc_srv_ldap_use_impt.gif)
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
* When the system built-in admin user logs in Logi JReport Server, Logi JReport always tries the system built-in password first (admin by default). This is to provide a backdoor password for admin user in case the LDAP server is down.

### Synchronizing Local Security Information with That of LDAP Server

In order to have the most current security information, you can schedule a task to synchronize the security information of Logi JReport Server with that of the LDAP server. The synchronization process first compares the security information on both Logi JReport Server and the LDAP server. Then if necessary, it updates the information on Logi JReport Server so that both sides are consistent. However, for security reasons this process does not automatically import the newly-added users or groups from the LDAP server.

**To schedule a synchronization task:**

1. In the Administration > Security > LDAP page, go to the Synchronize tab.

   ![Synchronize tab](https://devnet.logianalytics.com/hc/article_attachments/4412112522135/scrty_rsc_srv_ldap_use_sync.gif)
2. Select the **Edit** link in the LDAP Synchronization Schedule Settings table.
3. From the Select time type to synchronize drop-down list, specify the time for when the task is to be performed.

   ![Specify Time](https://devnet.logianalytics.com/hc/article_attachments/4412139515415/scrty_rsc_srv_ldap_use_schdl.gif)

   * To run the task at a specified time, select **Run this task at**, then define the date and time according to your requirement.
   * If you want to run the task repeatedly, select  **Run this task periodically**, then specify the duration, date and time accordingly.
4. Select **Save** to apply the schedule settings.

Information about the synchronization task is then displayed in LDAP Synchronization Schedule Settings table and the synchronization task is enabled by default. You can perform the following operations on the task:

* To edit the task, select the **Edit** link and then modify the schedule settings.
* To disable the task, select **Disable**; to enable the task again, select **Enable**.
* To view information about the last run of the synchronization task, select the **Detail** link.

You can also manually start the synchronization by selecting the **Synchronize Now** button. Then when the synchronization is completed, the Synchronization Information table will be displayed showing which users and roles/groups have been modified and removed. Select **Back** to return to the Synchronize tab.

### Defining Role Maps

You can predefine role maps for the imported LDAP users, then when an LDAP user account is imported, Logi JReport Server can automatically assign it to specific roles created on the server according to the map. A role map consists of two parts: Search Filter String and Corresponding Role Name. When an imported LDAP user account matches the filter condition, it will automatically be added to a specific role.

**To create a role map:**

1. In the Administration > Security > LDAP page, go to the Role Maptab.

   ![Role Map tab](https://devnet.logianalytics.com/hc/article_attachments/4412131403031/scrty_rsc_srv_ldap_use_role.gif)
2. Select the **Create New Role Map** link.
3. In the Search Filter String text box, input the search filter criteria.

   ![Search Filter String](https://devnet.logianalytics.com/hc/article_attachments/4412112522647/scrty_rsc_srv_ldap_use_map.gif)
4. From the Corresponding Role drop-down list, select a role to which you want to assign the matching users.
5. Select **Test** to test the contents of the filter. The result of the test does not affect the creation of the new role map.
6. Select **Save** to create the role map.

You can create as many role maps as you need and they are listed in the role map table. For any role map you can edit it as follows:

* To edit a role map, select the **Edit** link in the role map row and then modify the settings.
* To test the contents of the filter of a role map, select **Test** in the role map row.
* To remove unwanted role maps, select the checkboxes ahead of them and select **Delete**.

## Using the LDAP Implementation of the Security API

Logi JReport Server can access an LDAP server directly to look for LDAP users via LDAP Security API implementation, which could be your own LDAP implementation or be implemented using Logi JReport's Security API (for details about the Security API, see the jet.server.api.custom.security package in the Logi JReport Javadoc in `<install_root>\help\api`).

To use LDAP Security API implementation, you will need to turn on the LDAP security providers. There are three approaches to achieve this:

* **Via the server UI**   
  In the Administration > Security > LDAP > Server tab, check **Enable Direct Authentication to LDAP Server**.
* **Via the LDAP configuration file**Specify the following property in the LDAPProperties.xml configuration file located in `<install_root>\properties`:

  `<env-enableNoneImportedLDAPSupport>true</env-enableNoneImportedLDAPSupport>`.

  If the value is true, Logi JReport Server security system will then use the LDAP providers. The default value of this property is false.
* **Via API**Invoke the following two methods in the interface ConfigurationLDAPServer:

  ```
  /**   

  * Specifies whether or not the Server security system uses the LDAP providers.  

  * @return Returns true if using none imported LDAP support, otherwise returns false.  

  */  
  public boolean isEnableNoneImportedLDAPSupport();  

  /**  

  * Specifies whether or not the Server security system uses none imported LDAP support.  

  * @param isEnableNoneImportedLDAPSupport Set this parameter to true if the Server   

  security system uses none imported LDAP support, otherwise set it to false.  

  */  
  public void setEnableNoneImportedLDAPSupport (boolean isEnableNoneImportedLDAPSupport);
  ```

In order to use LDAP security providers, a valid admin user is required to access the Logi JReport Server console in order to manage Logi JReport Server. A user that meets one of the following two rules is regarded as an admin user:

* The user is a member of the LDAP admin group. The LDAP admin group is a configuration option in the LDAP configuration XML file.
* The user is a member of the administrators role. The user can be granted the role by a role map.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009692722-Configuring-the-LDAP-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718941-SSL-Support-in-the-LDAP-System)
