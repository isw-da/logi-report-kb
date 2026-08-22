---
title: "Configuring the LDAP Server"
id: 1500009650142
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650142-Configuring-the-LDAP-Server
updated_at: 2021-07-24T20:53:39Z
---

# Configuring the LDAP Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650122-Using-an-LDAP-Server-s-Security-System)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675061-Using-LDAP-Server-s-Security-Information)

# Configuring the LDAP Server

To use an LDAP server's security system, you should first enable Logi JReport Server to adapt to a directory server. You can configure either via UI or with the LDAPProperties.xml file.

Currently the following directory servers are supported: Novell Directory Server, Microsoft Site Server, iPlanet Directory Server, Active Directory Advanced Server, Lotus Domino Server and OpenLDAP Directory Server. If you need access to a different directory server, contact your Logi JReport Sales Representative. New servers are frequently being added.

Below is a list of the sections covered in this topic:

* [Configuring via UI](#UI)
* [Configuring With LDAPProperties.xml](#XML)
* [Troubleshooting LDAP Server Configuration](#TS)

## Configuring via UI

To configure the LDAP server via UI, on the Logi JReport Administration Page, go to the Configuration > LDAP > Server tab, then specify the following options as required.

|  |  |
| --- | --- |
| **Option** | **Description** |
| Select LDAP Server | Specifies the directory server. Supported servers are: Novell Directory Server, iPlanet Directory Server, Microsoft Site Server, OpenLDAP Directory Server, Win2000 Active Directory, and Lotus Domino on NT. |
| Load Settings | Loads the settings of the specified LDAP server. |
| Enable LDAP Version2/Version3 | Specifies whether or not to enable Logi JReport Server to retrieve users from the directory server and which LDAP Version to adopt. The LDAP Version3 extends LDAP Version2 in the areas of internationalization, authentication, referral, and deployment. It also allows new features to be added to the protocol without also requiring changes to the protocol. This is done by using extensions and controls.  LDAP Version3 protocol has extensible authentication which uses Simple Authentication and Security Layer ( SASL) mechanisms so as to support pluggable authentication.  Note that currently when you select Version3, Logi JReport Server will only use LDAP Version3 protocol to connect to LDAP server. |
| Enable Direct Authentication to LDAP Server | Specifies whether or not to enable LDAP without importing LDAP security information. This option controls the LDAP feature's work mode. Currently, the Logi JReport Server security system can run two modes in which you can use an LDAP server's security system. The first is importing mode. In this mode, if you want to use the LDAP feature, you will have to import the security information from an LDAP server. The second is non-importing mode. With this mode, Logi JReport Server can directly access an LDAP server and obtain LDAP security information without having to import it. |
| Enable Auto-Import of Users from LDAP Server | Specifies to enable Logi JReport Server to import LDAP users automatically. If activated, the server security system will import security information from the LDAP server when an LDAP user logs into Logi JReport Server for the first time. |
| LDAP URL | Specifies the URL of the LDAP server. |
| LDAP Server Port | Specifies the port of the LDAP server. |
| Root Entry | Specifies the root of the directory server. From this root, Logi JReport Server searches for objects in directory server. |
| Directory Manager DN | Specifies the entry path of the Directory Manager who has the priority to manage users on the directory server. |
| Password | Specifies the Directory Manager's password. |
| Remember Password | Specifies to remember the Directory Manager's password. |
| Encryption Type | Specifies the encryption type. There are two types available. None means using a plain port to connect to the LDAP server, and SSL refers to connecting to the LDAP server by SSL. |
| Import LDAP Groups to | Specifies whether the users in the LDAP groups will be imported into the Logi JReport security system as local roles or as local groups. |
| Test Connection | Tests whether the connection to the specified server is successful or not. |
| User Schema | Specifies the settings of user schema.  * **User Attribute Name**  Specifies the user's attribute name. * **User Common Name**  Specifies the user's common name. * **User Password**  Specifies the user's password. * **Distinguished Name** Specifies the name of the organization unit inside the LDAP server where you want to perform a search for users. * **Query User**  Views properties of users in the organization unit. * **Filter**  Specifies the filter criteria with which to search for users. * **Specify the attribute for user description**  Specifes the specific attribute which will be used as Logi JReport user information.   + **Attribute Name**  Specifes the attribute name. |
| Group Schema | Specifies the group schema settings.  * **Group Common Name**  Specifies a common name for the group. * **Group Member Type**  Specifies the member type of the group. * **Distinguished Name**  Specifies the name of the organization unit inside the LDAP server where you want to perform a search for groups. * **Filter**  Specifies the filter criteria with which to search for groups. * **Admin Group** Logi JReport Server will add the group specified here as a member to the Admin group. * **Query Group**  Views properties of groups in the organization unit. * **Specify the attribute for group description**  Specifes the specific attribute which will be used as Logi JReport group information.   + **Attribute Name**  Specifes the attribute name. |

The following presents examples for adapting Logi JReport Server to specific directory servers:

* [Example 1: Configuration for adapting to a Novell Directory Server](#1)
* [Example 2: Configuration for adapting to a Microsoft Site Server](#2)
* [Example 3: Configuration for adapting to an iPlanet Directory Server](#3)
* [Example 4: Configuration for adapting to the Active Directory Advanced Server](#4)
* [Example 5: Configuration for adapting to a Lotus Domino Server on NT](#5)
* [Example 6: Configuration for adapting to an OpenLDAP Directory Server](#6)

**Example 1: Configuration for adapting to a Novell Directory Server**

1. Select **Novell Directory Server** from the Select LDAP Server drop-down list, and then select **Load Settings**. The settings of the Novell Directory Server will then be loaded.
2. Check the **Enable LDAP** checkbox, and input the following information:
   * **LDAP URL:** ldap://IP address or host name of your Novell Directory Server (for example: `ldap://127.0.0.1`)
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

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920414487/scrty_rsc_srv_ldap_config_ui1.gif)
3. You can test the connection settings by selecting the **Test Connection** button, get the query result of the users specified in the option Filter by selecting the **Query User** button, and get the query result of groups specified in the option Filter by selecting the **Query Group** button.
4. Select **Save** to save all settings. You can then get all users and groups from the orgunit organizational unit.

**Example 2: Configuration for adapting to a Microsoft Site Server**

1. Select **Microsoft Site Server** from the Select LDAP Server drop-down list, and then select  **Load Settings**. The settings of the Microsoft Site Server will be loaded.
2. Make sure that the Enable LDAP checkbox is selected, and input the following information:
   * **LDAP URL:** ldap://IP address or host name of your Microsoft site Server (for example: `ldap://127.0.0.1`)
   * **LDAP Server Port:** 1003
   * **Root Entry:** o=test
   * **Directory Manager DN:** cn=administrator,ou=members,o=test
   * **Password:** test
   * **Encryption Type:** None
   * **Import LDAP Groups to**: Group

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920414999/scrty_rsc_srv_ldap_config_ui3.gif)
3. Select **Save** to save all settings in this page.

You can then get all users from the members organizational unit and all groups from the groups organizational unit.

**Example 3: Configuration for adapting to an iPlanet Directory Server**

1. Select **iPlanet Directory Server** from the Select LDAP Server drop-down list, and then select  **Load Settings**. The settings of iPlanet Directory Server will then be loaded.
2. Make sure that the Enable LDAP checkbox is selected, and input the following information:
   * **LDAP URL:** ldap://IP address of your iPlanet Directory Server
   * **LDAP Server Port:** 389
   * **Root Entry:** dc=mailbj,dc=jinfonet,dc=com
   * **Directory Manager DN:** cn=directory manager
   * **Password:** jinfonet
   * **Encryption Type:**  None
   * **Import LDAP Groups to**: Group

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926659223/scrty_rsc_srv_ldap_config_ui4.gif)
3. Select **Save** to save all the settings in this page. You can then get all users in the people organizational unit and all groups in the groups organizational unit.

**Example 4: Configuration for adapting to the Active Directory Advanced Server**

1. Select **Win2000 Active Directory** from the Select LDAP Server drop-down list, and then select  **Load Settings**. The settings are then cleared and you can input your information.
2. Make sure that the Enable LDAP checkbox is selected, and input the following information:
   * **LDAP URL:** ldap://IP address of your Windows 2000 Advanced Server
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

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920415383/scrty_rsc_srv_ldap_config_ui5.gif)  
   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920415767/scrty_rsc_srv_ldap_config_ui6.gif)
3. Select **Save** to save all settings in this page. You can then get all users and groups from the myorg organizational unit.

**Example 5: Configuration for adapting to a Lotus Domino Server on NT**

1. Select **Lotus Domino on NT** from the Select LDAP Server drop-down list, and then select  **Load Settings**. The settings are then cleared and you can input your information.
2. Make sure that the Enable LDAP checkbox is selected, and input the following information:
   * **LDAP URL:** ldap://IP address of your Lotus Domino Server
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

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920416023/scrty_rsc_srv_ldap_config_ui7.gif)  
   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920416279/scrty_rsc_srv_ldap_config_ui8.gif)
3. Select **Save** to save all settings in this page. You can then get all users and groups from the developer organization unit.

**Example 6: Configuration for adapting to an OpenLDAP Directory Server**

1. Select **OpenLDAP Directory Server** from the Select LDAP Server drop-down list, and then select **Load Settings**. The settings are then cleared and you can input your information.
2. Make sure that the Enable LDAP checkbox is selected, and input the following information:
   * **LDAP URL**: ldap://IP address of your OpenLDAP Directory Server (for example: `ldap://127.0.0.1`)
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
     + Admin Group:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920416535/scrty_rsc_srv_ldap_config_ui9.gif)  
   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920416791/scrty_rsc_srv_ldap_config_ui10.gif)
3. Select **Save** to save all settings in this page. You can then get all users and groups from the developer organization unit.

**Notes:**

* Make sure that the Directory Manager DN is a user with prior LDAP Server permission, and who can retrieve other LDAP users.
* Make sure that the users and groups you want to query and import into Logi JReport Server belong to the organization you typed into the Distinguished Name field.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Configuring With LDAPProperties.xml

The file LDAPProperties.xml located in `<install_root>\properties` can be used for LDAP server configuration. The properties in the file can be mapped to the options in the Server tab on the Logi JReport Administration > Configuration > LDAP page. For details about the usages of the properties, refer to that of the mapped [options](#Option).

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Troubleshooting LDAP Server Configuration

When you encountered any problems during the LDAP configuration, refer to the following for help.

**LDAP configuration failure resulting in re-login failure as an admin user**

An admin user may fail to carry out LDAP configuration properly, and thus then cannot log onto the Logi JReport Administration page to manage the server. If this happens, you should follow the below steps:

1. Modify the property in the LDAP configuration XML file LDAPProperties.xml in `<install_root>\properties` as follows to turn off the Enable Direct Authentication to LDAP Server option:

   `<env-enableNoneImportedLDAPSupport>false</env-enableNoneImportedLDAPSupport>`
2. Restart Logi JReport Server and log in as a built-in security admin user to correct the LDAP configuration.

**Warning messages in the advent of incorrect LDAP configuration**

Apart from the notes offered on the Logi JReport Administration > Configuration > LDAP page, prompt warning information is also provided in order to cope with incorrect LDAP configuration. The server system will prompt warning messages in the following cases:

* If you do not fill in the Admin Group field or specify an admin group.
* If the admin group specified does not hold a user.
* If the admin group specified does not exist in the LDAP server.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650122-Using-an-LDAP-Server-s-Security-System)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675061-Using-LDAP-Server-s-Security-Information)
