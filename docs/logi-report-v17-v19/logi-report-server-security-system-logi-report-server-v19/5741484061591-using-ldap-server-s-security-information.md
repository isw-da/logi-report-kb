---
title: "Using LDAP Server's Security Information"
id: 5741484061591
section: "Logi Report Server Security System Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741484061591-Using-LDAP-Server-s-Security-Information
updated_at: 2022-10-31T17:18:28Z
---

# Using LDAP Server's Security Information

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png) Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483999127-Configuring-the-LDAP-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741470350487-SSL-Support-in-the-LDAP-System)

# Using LDAP Server's Security Information

The Logi Report Server security system can run in two modes in which you can use an LDAP server's security system: importing mode and non-importing mode. This topic describes how you can import LDAP server's security information and enable Logi Report Server to access an LDAP server and obtain LDAP security information directly using LDAP Security API implementation.

The diagram illustrates the two working modes:

![Working Mode](https://devnet.logianalytics.com/hc/article_attachments/9905656806039/scrty_rsc_srv_ldap_use1.gif)

Importing mode: You can import LDAP server's security information into the Logi Report Server security system to use them in Logi Report Server.

Non-importing mode: Logi Report Server can access an LDAP server and obtain LDAP security information directly using the LDAP implementation of the Security API.

This topic contains the following sections:

* [Importing Security Information from the LDAP Server](#Import)
  + [Importing LDAP Users Automatically](#Auto)
  + [Importing LDAP Users and Groups Manually](#Manual)
  + [Synchronizing Local Security Information with That of LDAP Server](#Sync)
  + [Defining Role Maps](#Map)
* [Using the LDAP Implementation of the Security API](#API)

## Importing Security Information from the LDAP Server

LDAP server's security information can be imported into the Logi Report Server security system either automatically or manually. You can also schedule a task to synchronize the security information of Logi Report Server with that of the LDAP server to get the LDAP server's most current security information. By predefining role maps, you can make Logi Report Server automatically assign the imported LDAP users to specific Logi Report Server roles.

### Importing LDAP Users Automatically

If you have selected the **Enable Auto-Import of Users from LDAP Server** option in the Configuration > LDAP > Server tab when [configuring the LDAP server](https://devnet.logianalytics.com/hc/en-us/articles/5741483999127-Configuring-the-LDAP-Server), Logi Report Server will automatically import LDAP users when they sign in for the first time. The **Enable LDAP** and **Enable Auto-Import of Users from LDAP Server** options in the Configuration > LDAP > Server tab work together. The former determines whether an imported LDAP user can be used in Logi Report Server, and the latter determines whether LDAP users can be imported automatically, as shown in the following table:

![Checked](https://devnet.logianalytics.com/hc/article_attachments/9905635484951/scrty_rsc_srv_ldap_use2.gif)=Selected; ![Unchecked](https://devnet.logianalytics.com/hc/article_attachments/9905656865047/scrty_rsc_srv_ldap_use3.gif)=Unselected

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

You can also import LDAP users and groups into Logi Report Server's security system manually.

1. On the system toolbar of the Server Console, navigate to **Administration** > **Security** >  **LDAP**. Server displays the LDAP page.
2. Select the **Import** tab.

   ![LDAP page](https://devnet.logianalytics.com/hc/article_attachments/9905635529751/scrty_rsc_srv_ldap_use_impt.gif)
3. Specify whether LDAP users will overwrite local users or be replaced by local users after you import LDAP users into Logi Report Server.

   If you have imported users/groups from the LDAP server to Logi Report Server before and you want to import them again, to prevent the information of the users/groups on Logi Report Server from being overwritten by the newly imported users/groups, you should select **Local users overwrite LDAP users** and then import the users/groups.
4. To view the LDAP users and groups that have the same names as the users and groups in Logi Report Server, select **List Users** and **List Groups**.
5. Import the LDAP users and groups to Logi Report Server.
   * To import LDAP users, select **Import Users**. Server lists the users on the LDAP server. To import some of them, select them and then select **Import**; to import all of them, select **Import All**.
   * To import LDAP groups, select **Import Groups**. Server lists the groups on the LDAP server. To import some of them, select them and then select **Import**; to import all of them, select **Import All**.
   * To import all LDAP users and groups, select **Import All**.

   The selected or all LDAP users/groups will then be imported based on the specified overwriting rule. Any LDAP group that has the same name as a group on Logi Report Server will be merged into the local group.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* There is an admin group named Administrators on the LDAP Server. If you perform an import operation, Logi Report Server imports all groups except for the Administrators group.
* In the case of a non-admin group on the LDAP Server having the same name as a non-admin group on Logi Report Server, if you perform an import operation, all users from the non-admin group on the LDAP Server will be merged into the non-admin group of Logi Report Server.
* When the system built-in administrator signs in to Logi Report Server, Logi Report always tries the system built-in password first (**admin** by default). This is to provide a backdoor password for administrators in case the LDAP server is down.

### Synchronizing Local Security Information with That of LDAP Server

In order to have the most current security information, you can schedule a task to synchronize the security information of Logi Report Server with that of the LDAP server. The synchronization process first compares the security information on both Logi Report Server and the LDAP server. Then it updates the information on Logi Report Server so that both sides are consistent. However, for security reasons, this process does not automatically import the newly added users or groups from the LDAP server.

**To schedule a synchronization task:**

1. In the Administration > Security > LDAP page, go to the **Synchronize** tab.

   ![Synchronize tab](https://devnet.logianalytics.com/hc/article_attachments/9905635554199/scrty_rsc_srv_ldap_use_sync.gif)
2. Select **Edit** in the LDAP Synchronization Schedule Settings table.
3. From the **Select time type to synchronize** drop-down list, specify the time when you want to perform the task.

   ![Specify Time](https://devnet.logianalytics.com/hc/article_attachments/9905635582743/scrty_rsc_srv_ldap_use_schdl.gif)

   * To run the task at a specified time, select **Run this task at**, then define the date and time.
   * If you want to run the task repeatedly, select **Run this task periodically**, then specify the duration, date, and time accordingly.
4. Select **Save** to apply the schedule settings.

Logi Report Server displays information about the synchronization task in the LDAP Synchronization Schedule Settings table and enables the synchronization task by default. You can perform the following operations on the task:

* To edit the task, select **Edit** and then modify the schedule settings.
* To disable the task, select **Disable**; to enable the task again, select **Enable**.
* To view information about the last run of the synchronization task, select **Detail**.

You can also manually start the synchronization by selecting **Synchronize Now**. Then when the synchronization is completed, Logi Report Server displays the Synchronization Information table showing which users and roles/groups have been modified and removed. Select **Back** to return to the Synchronize tab.

### Defining Role Maps

You can predefine role maps for the imported LDAP users, then when an LDAP user account is imported, Logi Report Server can automatically assign it to specific roles created on the server according to the map. A role map consists of two parts: **Search Filter String** and **Corresponding Role Name**. When an imported LDAP user account matches the filter condition, Logi Report Server will automatically add it to a specific role.

**To create a role map:**

1. In the Administration > Security > LDAP page, go to the **Role Map** tab.

   ![Role Map tab](https://devnet.logianalytics.com/hc/article_attachments/9905635596823/scrty_rsc_srv_ldap_use_role.gif)
2. Select **Create New Role Map**.
3. In the **Search Filter String** text box, type the search filter criteria.

   ![Search Filter String](https://devnet.logianalytics.com/hc/article_attachments/9905635625879/scrty_rsc_srv_ldap_use_map.gif)
4. From the **Corresponding Role** drop-down list, select a role to which you want to assign the matching users.
5. Select **Test** to test the contents of the filter. The result of the test does not affect the creation of the new role map.
6. Select **Save** to create the role map.

You can create as many role maps as you need. Logi Report Server lists them in the role map table. You can edit any role map as follows:

* To edit a role map, select **Edit** in the role map row and then modify the settings.
* To test the contents of the filter of a role map, select **Test** in the role map row.
* To remove unwanted role maps, select them and select **Delete**.

## Using the LDAP Implementation of the Security API

Logi Report Server can access an LDAP server directly to look for LDAP users via LDAP Security API implementation, which could be your own LDAP implementation or be implemented using Logi Report's Security API (for more information, see the **jet.server.api.custom.security** package in the Logi Report Javadoc).

To use LDAP Security API implementation, you will need to turn on the LDAP security providers. There are three approaches to achieve this:

* **Via the server UI**   
  In the Administration > Security > LDAP > Server tab, select **Enable Direct Authentication to LDAP Server**.
* **Via the LDAP configuration file**  
  Specify the following property in the configuration file **LDAPProperties.xml** in `<install_root>\properties`:

  `<env-enableNoneImportedLDAPSupport>true</env-enableNoneImportedLDAPSupport>`

  If the value is true, Logi Report Server security system will then use the LDAP providers. The default value of this property is false.
* **Via API**  
  Invoke the following two methods in the interface **ConfigurationLDAPServer**:

  ```
  /**   
  * Specify whether the Server security system uses the LDAP providers.  
  * @return Return true if using none imported LDAP support, otherwise returns false.  
  */  
  public boolean isEnableNoneImportedLDAPSupport();  
  /**  
  * Specify whether the Server security system uses none imported LDAP support.  
  * @param isEnableNoneImportedLDAPSupport Set this parameter to true if the Server   
  security system uses none imported LDAP support, otherwise set it to false.  
  */  
  public void setEnableNoneImportedLDAPSupport (boolean isEnableNoneImportedLDAPSupport);
  ```

In order to use LDAP security providers, a valid administrator is required to access the Server Console to manage Logi Report Server. A user that meets either of the two rules is an administrator:

* The user is a member of the LDAP admin group. The LDAP admin group is a configuration option in the LDAP configuration XML file.
* The user is a member of the administrators role. The user can be granted the role by a role map.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483999127-Configuring-the-LDAP-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741470350487-SSL-Support-in-the-LDAP-System)
