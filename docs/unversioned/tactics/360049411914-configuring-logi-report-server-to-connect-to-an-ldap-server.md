---
title: "Configuring Logi Report Server to Connect to an LDAP Server"
id: 360049411914
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049411914-Configuring-Logi-Report-Server-to-Connect-to-an-LDAP-Server
updated_at: 2022-10-31T14:39:35Z
---

# Configuring Logi Report Server to Connect to an LDAP Server

Logi Report Server’s security system can run two modes in which you can use an LDAP server’s security system: importing mode and non-importing mode. Below diagram illustrates these two working modes:

![Two Working Modes](https://devnet.logianalytics.com/hc/article_attachments/9905343086999)

Importing mode: If you want to use the LDAP feature, you will have to import the security information from an LDAP server into the built-in security system (red line).

Non-importing mode: Logi Report Server can access an LDAP server and obtain LDAP security information directly using the LDAP implementation of the Security API (blue line).

To use an LDAP server’s security system, you should first enable Logi Report Server to adapt to a directory server. You can configure either via UI or with the LDAPProperties.xml file.

Currently the following directory servers are supported: Novell Directory Server, Microsoft Site Server, iPlanet Directory Server, Active Directory Advanced Server, Lotus Domino Server on NT, and OpenLDAP Directory Server. If you need access to a different directory server, contact your Logi Report Sales Representative. New servers are frequently being added.

## Configuring via UI

To configure the LDAP server via UI, on the Logi Report Administration Page go to the Configuration > LDAP > Server tab, then specify the following options as required.

|  |  |
| --- | --- |
| **OPTION** | **DESCRIPTION** |
| Select LDAP Server | Specifies the directory server. |
| Load Settings | Loads the settings of the specified LDAP server. |
| Enable LDAP Version2/Version3 | Specifies whether or not to enable Logi Report Server to retrieve users from the directory server and which LDAP version to adopt.   The LDAP Version3 extends LDAP Version2 in the areas of internationalization, authentication, referral, and deployment. It also allows new features to be added to the protocol without also requiring changes to the protocol. This is done by using extensions and controls.  LDAP Version3 protocol has extensible authentication which uses Simple Authentication and Security Layer (SASL) mechanisms so as to support pluggable authentication.  Note that currently when you select Version3, Logi Report Server will only use LDAP Version3 protocol to connect to LDAP server. |
| Enable Direct Authentication to LDAP Server | Specifies whether or not to enable LDAP without importing LDAP security information. This option controls the LDAP feature’s work mode. Currently, the Logi Report Server security system can run two modes in which you can use an LDAP server’s security system. The first is importing mode. In this mode, if you want to use the LDAP feature, you will have to import the security information from an LDAP server. The second is non-importing mode. With this mode, Logi Report Server can directly access an LDAP server and obtain LDAP security information without having to import it. |
| Enable Auto-Import of Users from LDAP Server | Specifies to enable Logi Report Server to import LDAP users automatically. If activated, the server security system will import security information from the LDAP server when an LDAP user logs into Logi Report Server for the first time. |
| LDAP URL | Specifies the URL of the LDAP server. |
| LDAP Server Port | Specifies the port of the LDAP server. |
| Root Entry | Specifies the root of the directory server. From this root, Logi Report Server searches for objects in directory server. |
| Directory Manager DN | Specifies the entry path of the Directory Manager who has the priority to manage users on the directory server. |
| Password | Specifies the Directory Manager’s password. |
| Remember Password | Specifies to remember the Directory Manager’s password. |
| Encryption Type | Specifies the encryption type. There are two types available. None means using a plain port to connect to the LDAP server, and SSL refers to connecting to the LDAP server by SSL. |
| Import LDAP Groups to | Specifies whether the users in the LDAP groups will be imported into the Logi Report security system as local roles or as local groups. |
| Test Connection | Tests whether the connection to the specified server is successful or not. |
| User Schema | Specifies the settings of user schema.    * **User Attribute Name** * Specifies the user’s attribute name. * **User Common Name** * Specifies the user’s common name. * **User Password** * Specifies the user’s password. * **Distinguished Name** * Specifies the name of the organization unit inside the LDAP server where you want to perform a search for users. * **Query User** * Views properties of users in the organization unit. * **Filter** * Specifies the filter criteria with which to search for users. * **Specify the attribute for user description** * Specifies the specific attribute which will be used as Logi Report user information.   + **Attribute Name**   + Specifies the attribute name. |
| Group Schema | Specifies the group schema settings.    * **Group Common Name** * Specifies a common name for the group. * **Group Member Type** * Specifies the member type of the group. * **Distinguished Name** * Specifies the name of the organization unit inside the LDAP server where you want to perform a search for groups. * **Filter** * Specifies the filter criteria with which to search for groups. * **Admin Group** * Logi Report Server will add the group specified here as a member to the Admin group. * **Query Group** * Views properties of groups in the organization unit. * **Specify the attribute for group description** * Specifies the specific attribute which will be used as Logi Report group information.   + **Attribute Name**   + Specifies the attribute name. |

## Configuring with LDAPProperties.xml

The LDAPProperties.xml file located in <install\_root>\properties can be used for LDAP server configuration. The properties in the file can be mapped to the options in the Server tab on the Logi Report Administration > Configuration > LDAP page. For details about the usages of the properties, refer to that of the mapped [options](https://www.stage.jinfonet.com/kbase/server15up1/userguide/HTML/security/scrty_rsc_srv_ldap_config.htm?rhsyns=%20#Option).

|  |  |
| --- | --- |
| **UI OPTION** | **PROPERTIES IN LDAPPROPERTIES.XML** |
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

The following presents examples for adapting Logi Report Server to specific directory servers:

* [Example 1: Configuration for adapting to a Novell Directory Server](https://www.stage.jinfonet.com/kbase/server15up1/userguide/HTML/security/scrty_rsc_srv_ldap_config.htm?rhsyns=%20#1)
* [Example 2: Configuration for adapting to a Microsoft Site Server](https://www.stage.jinfonet.com/kbase/server15up1/userguide/HTML/security/scrty_rsc_srv_ldap_config.htm?rhsyns=%20#2)
* [Example 3: Configuration for adapting to an iPlanet Directory Server](https://www.stage.jinfonet.com/kbase/server15up1/userguide/HTML/security/scrty_rsc_srv_ldap_config.htm?rhsyns=%20#3)
* [Example 4: Configuration for adapting to the Active Directory Advanced Server](https://www.stage.jinfonet.com/kbase/server15up1/userguide/HTML/security/scrty_rsc_srv_ldap_config.htm?rhsyns=%20#4)
* [Example 5: Configuration for adapting to a Lotus Domino Server on NT](https://www.stage.jinfonet.com/kbase/server15up1/userguide/HTML/security/scrty_rsc_srv_ldap_config.htm?rhsyns=%20#5)
* [Example 6: Configuration for adapting to an OpenLDAP Directory Server](https://www.stage.jinfonet.com/kbase/server15up1/userguide/HTML/security/scrty_rsc_srv_ldap_config.htm?rhsyns=%20#6)
