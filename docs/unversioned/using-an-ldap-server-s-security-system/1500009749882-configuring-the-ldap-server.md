---
title: "Configuring the LDAP Server"
id: 1500009749882
section: "Using an LDAP Server's Security System"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749882-Configuring-the-LDAP-Server
updated_at: 2021-07-24T00:47:34Z
---

# Configuring the LDAP Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778661-Using-an-LDAP-Server-s-Security-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778681-Using-LDAP-Server-s-Security-Information)

# Configuring the LDAP Server

To use an LDAP server's security system, you should first enable Logi Report Server to adapt to a directory server. This topic describes how you can configure an LDAP Server either via the Server Console or using the file LDAPProperties.xml, and troubleshoot problems.

This topic contains the following sections:

* [Configuring via Server UI](#UI)
* [Configuring in LDAPProperties.xml](#XML)
* [Troubleshooting LDAP Server Configuration](#TS)

## Configuring via Server UI

To configure the LDAP server via UI, in the Server Console go to the Administration > Security > LDAP > Server tab, then configure the following options.

| Option | Description |
| --- | --- |
| Select LDAP Server | Select a directory server. |
| Load Settings | Select to load the settings of the specified LDAP server. |
| Enable LDAP Version2/Version3 | Select if you want to enable Logi Report Server to retrieve users from the directory server and then select the LDAP version to adopt. The LDAP Version3 extends LDAP Version2 in the areas of internationalization, authentication, referral, and deployment. It also enables new features to be added to the protocol without also requiring changes to the protocol. This is done using extensions and controls.  LDAP Version3 protocol has extensible authentication which uses Simple Authentication and Security Layer (SASL) mechanisms to support pluggable authentication.  Note iconCurrently when you selected **Version3**, Logi Report Server only uses LDAP Version3 protocol to connect to LDAP server. |
| Enable Direct Authentication to LDAP Server | Select if you want to enable Logi Report Server to directly access an LDAP server and obtain LDAP security information without having to import it. When you select this option, Logi Report Server automatically assigns the users from the LDAP server the *everyone* role in the Logi Report Server security system. By default, this option is not activated and to use an LDAP server's security system you have to import the security information from the LDAP server. |
| [Enable Auto-Import of Users from LDAP Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009778681-Using-LDAP-Server-s-Security-Information#Import) | Select if you want to enable Logi Report Server to import LDAP users automatically. If you select this option, Logi Report Server's security system will import security information from the LDAP server automatically when an LDAP user logs into Logi Report Server for the first time. |
| LDAP URL | The URL of the LDAP server. |
| LDAP Server Port | The port of the LDAP server. |
| Root Entry | The root of the directory server. From this root, Logi Report Server searches for objects in the directory server. |
| Directory Manager DN | The entry path of the Directory Manager who can manage users on the directory server. |
| Password | The Directory Manager's password. |
| Remember Password | Select if you want Server to remember the Directory Manager's password. |
| Encryption Type | Select the encryption type. There are two types available. **None** means using a plain port to connect to the LDAP server, and **SSL** refers to connecting to the LDAP server by SSL. |
| Import LDAP Groups to | Select Role or Group if you want to import the users in the LDAP groups into the Logi Report security system as local roles or local groups. |
| Test Connection | Select if you want to test whether the connection to the specified server is successful. |
| User Schema | Specify the settings of user schema.  * **User Attribute Name**  The user's attribute name. * **User Common Name**  The user's common name. * **User Password**  The user's password. * **Distinguished Name** The name of the organization unit inside the LDAP server where you want to perform a search for users. * **Query User**  Select to view properties of users in the organization unit. * **Filter**  The filter criteria with which to search for users. * **Specify the attribute for user description**  Select if want to use an attribute as Logi Report user information.   + **Attribute Name**  The attribute name. |
| Group Schema | Specify the group schema settings.  * **Group Common Name**  A common name for the group. * **Group Member Type**  The member type of the group. * **Distinguished Name**  The name of the organization unit inside the LDAP server where you want to perform a search for groups. * **Filter**  The filter criteria with which to search for groups. * **Admin Group** Logi Report Server adds the group you specified here as a member to the Admin group. * **Query Group**  Select to view properties of groups in the organization unit. * **Specify the attribute for group description**  Select if you want to use an attribute as Logi Report group information.   + **Attribute Name**  The attribute name. |

The following examples show how to adapt Logi Report Server to specific directory servers:

* [Example 1: Configuration for adapting to a Novell Directory Server](#Example1)
* [Example 2: Configuration for adapting to a Microsoft Site Server](#Example2)
* [Example 3: Configuration for adapting to an iPlanet Directory Server](#Example3)
* [Example 4: Configuration for adapting to an Active Directory](#Example4)
* [Example 5: Configuration for adapting to a Lotus Domino on NT](#Example5)
* [Example 6: Configuration for adapting to an OpenLDAP Directory Server](#Example6)

**Example 1: Configuration for adapting to a Novell Directory Server**

1. Select **Novell Directory Server** from the **Select LDAP Server** drop-down list.
2. Select **Load Settings**. Server loads the settings for Novell Directory Server.
3. Select the **Enable LDAP** check box.
4. Input the following information:
   * **LDAP URL:**`ldap://IP_address_or_hostname_of_the_server` (for example: `ldap://127.0.0.1`)
   * **LDAP Server Port:** 389
   * **Root Entry:** o=the name of the root (for example: o=myorg)
   * **Directory Manager DN:** cn=user name of the directory manager,o=context (for example: cn=admin,o=context)
   * **Password:** the password of the Directory Manager (for example: 1234)
   * **Encryption Type:**  None
   * **Import LDAP Groups to:** Group
   * **User Schema**
     + Distinguished Name: ou=the name of the organization unit where you want to perform a search for users (for example: ou=orgunit)
     + Filter: (&(cn=the filter criteria that you want to set )(objectclass=person)) (for example: (&(cn=\*)(objectclass=person)))
   * **Group Schema**
     + Distinguished Name: ou=the name of the organization unit that you want to perform a search for groups (for example: ou=orgunit)
     + Filter: (&(cn=the filter criteria that you want to set )(objectclass=groupofuniquenames)) (for example: (&(cn=\*)(objectclass=groupofuniquenames)))
     + Admin Group: The name of the group you want to add to the Admin group (for example: develop)

   ![Novell Directory Server](https://devnet.logianalytics.com/hc/article_attachments/4404880211479/scrty_rsc_srv_ldap_config_ui1.gif)
5. To test the connection settings, select **Test Connection**.
6. To get the query result of the users that you specified in the **Filter** field, select **Query User**.
7. To get the query result of groups that you specified in the **Filter** field, select **Query Group**.
8. Select **Save** to save all settings. You can then get all users and groups from the orgunit organizational unit.

**Example 2: Configuration for adapting to a Microsoft Site Server**

1. Select **Microsoft Site Server** from the **Select LDAP Server** drop-down list.
2. Select  **Load Settings**. Server loads the settings for the LDAP server.
3. Select the **Enable LDAP** check box.
4. Input the following information:
   * **LDAP URL:**`ldap://IP_address_or_hostname_of_the_server` (for example: `ldap://127.0.0.1`)
   * **LDAP Server Port:** 1003
   * **Root Entry:** o=test
   * **Directory Manager DN:** cn=administrator,ou=members,o=test
   * **Password:** test
   * **Encryption Type:** None
   * **Import LDAP Groups to**: Group

   ![Microsoft Site Server](https://devnet.logianalytics.com/hc/article_attachments/4404880212247/scrty_rsc_srv_ldap_config_ui3.gif)
5. Select **Save** to save all settings in this page.

You can then get all users from the members organizational unit and all groups from the groups organizational unit.

**Example 3: Configuration for adapting to an iPlanet Directory Server**

1. Select **iPlanet Directory Server** from the **Select LDAP Server** drop-down list.
2. Select  **Load Settings**. Server loads the settings for the LDAP server.
3. Select the **Enable LDAP** check box.
4. Input the following information:
   * **LDAP URL:**`ldap://IP_address_of_the_server` (for example: `ldap://127.0.0.1`)
   * **LDAP Server Port:** 389
   * **Root Entry:** dc=mailbj,dc=jinfonet,dc=com
   * **Directory Manager DN:** cn=directory manager
   * **Password:** jinfonet
   * **Encryption Type:**  None
   * **Import LDAP Groups to**: Group

   ![iPlanet Directory Server](https://devnet.logianalytics.com/hc/article_attachments/4404880212631/scrty_rsc_srv_ldap_config_ui4.gif)
5. Select **Save** to save all the settings in this page. You can then get all users in the people organizational unit and all groups in the groups organizational unit.

**Example 4: Configuration for adapting to an Active Directory**

1. Select **Active Directory** from the **Select LDAP Server** drop-down list.
2. Select **Load Settings**. Server loads the settings for the LDAP server.
3. Select the **Enable LDAP** check box.
4. Input the following information:
   * **LDAP URL:**`ldap://IP_address_of_the_server` (for example: `ldap://127.0.0.1`)
   * **LDAP Server Port:** 389
   * **Root Entry:** DC=testad,DC=local
   * **Directory Manager DN:** CN=administrator,CN=Users,DC=testad,DC=local
   * **Password:** 1234
   * **Encryption Type:**  None
   * **Import LDAP Groups to**: Group
   * **User Schema**
     + User Attribute Name: cn
     + User Common Name: userPrincipalName
     + User Password: userPassword
     + Distinguished Name: ou=myorg
     + Filter: (&(cn=\*)(objectclass=person))
   * **Group Schema**
     + Group Common Name: cn
     + Group Member Type: member
     + Distinguished Name: ou=myorg
     + Filter: (&(cn=\*)(objectclass=group))

   ![Active Directory Advanced Server](https://devnet.logianalytics.com/hc/article_attachments/4404880212887/scrty_rsc_srv_ldap_config_ui5.gif)
5. Select **Save** to save all settings in this page. You can then get all users and groups from the myorg organizational unit.

**Example 5: Configuration for adapting to a Lotus Domino on NT**

1. Select **Lotus Domino on NT** from the **Select LDAP Server** drop-down list.
2. Select **Load Settings**. Server loads the settings for the LDAP server.
3. Select the **Enable LDAP** check box.
4. Input the following information:
   * **LDAP URL:**`ldap://IP_address_of_the_server` (for example: `ldap://127.0.0.1`)
   * **LDAP Server Port:** 389
   * **Root Entry:**
   * **Directory Manager DN:** cn=admin,o=jtotal
   * **Password:** 123456
   * **Encryption Type:**  None
   * **Import LDAP Groups to**: Group
   * **User Schema**
     + User Attribute Name: uid
     + User Common Name: cn
     + User Password: userPassword
     + Distinguished Name: ou=developer, o=jtotal
     + Filter: (&(cn=\*)(objectclass=person))
   * **Group Schema**
     + Group Common Name: cn
     + Group Member Type: member
     + Distinguished Name:
     + Filter: (&(cn=\*)(objectclass=groupofnames))

   ![Lotus Domino Server on NT](https://devnet.logianalytics.com/hc/article_attachments/4404880213399/scrty_rsc_srv_ldap_config_ui6.gif)
5. Select **Save** to save all settings in this page. You can then get all users and groups from the developer organization unit.

**Example 6: Configuration for adapting to an OpenLDAP Directory Server**

1. Select **OpenLDAP Directory Server** from the **Select LDAP Server** drop-down list
2. Select **Load Settings**. Server loads the settings for the LDAP server.
3. Select the **Enable LDAP** check box.
4. Input the following information:
   * **LDAP URL**: `ldap://IP_address_of_the_server` (for example: `ldap://127.0.0.1`)
   * **LDAP Server Port**: 389
   * **Root Entry:**  dc=openldap, dc=ldaptest
   * **Directory Manager DN**: cn=Manager,dc=openldap,dc=ldaptest
   * **Password**: 123456789
   * **Encryption Type**: None
   * **Import LDAP Groups to**: Group
   * **User Schema**
     + User Attribute Name: uid
     + User Common Name: cn
     + User Password: userPassword
     + Distinguished Name: ou=members
     + Filter: (&(uid=\*)(objectclass=person))
   * **Group Schema** 
     + Group Common Name: cn
     + Group Member Type: uniqueMember
     + Distinguished Name: ou=groups
     + Filter: (&(cn=\*)(objectclass=groupofuniquenames))

   ![OpenLDAP Directory Server](https://devnet.logianalytics.com/hc/article_attachments/4404880213783/scrty_rsc_srv_ldap_config_ui7.gif)
5. Select **Save** to save all settings in this page. You can then get all users and groups from the developer organization unit.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* Make sure that the Directory Manager DN is a user with prior LDAP Server permission, and who can retrieve other LDAP users.
* Make sure that the users and groups you want to query and import into Logi Report Server belong to the organization you typed into the **Distinguished Name** field.

## Configuring in LDAPProperties.xml

You can use the file **LDAPProperties.xml** in `<install_root>\properties` for LDAP server configuration. Server maps the properties in the file to the options in the Configuration > LDAP > Server tab. For more information, see that of the mapped [options](#Option).

| UI Option | Properties in LDAPProperties.xml |
| --- | --- |
| Enable LDAP | enableLDAPSupport |
| Version2/Version3 | ldapVersion |
| Enable Direct Authentication to LDAP Server | enableNoneImportedLDAPSupport |
| Enable Auto-Import of Users from LDAP Server | enableAutoImportLDAPUser |
| LDAP URL | url |
| LDAP Server Port | serverPort |
| Root Entry | rootEntry |
| Directory Manager DN | directoryManagerDN |
| Password | password |
| Encryption Type | isUsingSSL |
| Import LDAP Groups to | importGroupType |
| User Attribute Name | userAN |
| User Common Name | userCN |
| User Password | userPassword |
| Distinguished Name | userDN |
| Filter (for user schema) | userFilter |
| Specify the attribute for user description | userEnableSAN |
| Attribute Name (for user schema) | userSAN |
| Group Common Name | groupCN |
| Group Member Type | groupMemeberType |
| Distinguished Name | groupDN |
| Filter (for group schema) | groupFilter |
| Admin Group | groupAdminGroup |
| Specify the attribute for group description | groupEnableSAN |
| Attribute Name (for group schema) | groupSAN |

The following example configures Active Directory in LDAPProperties.xml:

```
<?xml version="1.0" encoding="UTF-8"?>  
<LDAP>  
    <LDAP-configuration>  
        <LDAP-name>defaultLDAP</LDAP-name>  
        <LDAP-Server-name>Active Directory</LDAP-Server-name>  
        <LDAP-baseInfo>  
            <env-enableLDAPSupport>true</env-enableLDAPSupport>  
            <env-ldapVersion>3</env-ldapVersion>  
            <env-enableNoneImportedLDAPSupport>false</env-enableNoneImportedLDAPSupport>  
            <env-enableAutoImportLDAPUser>false</env-enableAutoImportLDAPUser>  
            <env-url>ldap://127.0.0.1</env-url>  
            <env-serverPort>389</env-serverPort>  
            <env-rootEntry>DC=qau08,DC=jinfonet,DC=com,DC=cn</env-rootEntry>  
            <env-isUsingSSL>false</env-isUsingSSL>   
            <env-directoryManagerDN>CN=Administrator,CN=users,DC=qau08,DC=jinfonet,DC=com,DC=cn</env-directoryManagerDN>  
            <env-password>AEBoKZOjFzMzABwq</env-password>  
            <env-socketTime>10</env-socketTime>  
            <env-importGroupType>Role</env-importGroupType>  
        </LDAP-baseInfo>  
        <LDAP-userSchemaInfo>  
            <env-userAN>CN</env-userAN>  
            <env-userCN>CN</env-userCN>  
            <env-userEnableSAN>false</env-userEnableSAN>  
            <env-userSAN></env-userSAN>  
            <env-userPassword>userPassword</env-userPassword>  
            <env-userDN>OU=People</env-userDN>  
            <env-userFilter>(&(cn=*)(objectclass=person))</env-userFilter>  
        </LDAP-userSchemaInfo>  
        <LDAP-groupSchemaInfo>  
            <env-groupCN>CN</env-groupCN>  
            <env-groupEnableSAN>false</env-groupEnableSAN>  
            <env-groupSAN></env-groupSAN>  
            <env-groupMemberType>member</env-groupMemberType>  
            <env-groupFilter>(&(cn=*)(objectclass=group))</env-groupFilter> 
             <env-groupDN>OU=company</env-groupDN>  
            <env-groupAdminGroup>QAs</env-groupAdminGroup>  
        </LDAP-groupSchemaInfo>  
    </LDAP-configuration>  
    <LDAP-scheduleTaskID>2019-03-04 15:43:48.383</LDAP-scheduleTaskID>  
    <LDAP-encode />  
    <LDAP-roleMaps></LDAP-roleMaps>  
</LDAP>
```

## Troubleshooting LDAP Server Configuration

When you encountered problems during the LDAP configuration, refer to the following for help.

**LDAP configuration failure resulting in re-login failure as an admin user**

An admin user may fail to carry out LDAP configuration properly, and thus cannot log onto the Server Console to manage the server. If this happens, you should follow the below steps:

1. Modify the property in the LDAP configuration XML file **LDAPProperties.xml** in `<install_root>\properties` as follows to turn off the E**nable Direct Authentication to LDAP Server** option:

   `<env-enableNoneImportedLDAPSupport>false</env-enableNoneImportedLDAPSupport>`
2. Restart Logi Report Server and log in as a built-in security admin user to correct the LDAP configuration.

**Warning messages in the advent of incorrect LDAP configuration**

Apart from the notes in the Administration > Security > LDAP page, the server system also prompts warning messages to cope with incorrect LDAP configuration, in the following cases:

* If you do not fill in the **Admin Group** field or specify an admin group.
* If the admin group does not hold a user.
* If the admin group does not exist in the LDAP server.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778661-Using-an-LDAP-Server-s-Security-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778681-Using-LDAP-Server-s-Security-Information)
