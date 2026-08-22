---
title: "Customized Implementation of the Security API"
id: 5741363965079
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741363965079-Customized-Implementation-of-the-Security-API
updated_at: 2022-10-31T17:15:53Z
---

# Customized Implementation of the Security API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741395390999-Customizing-the-Web-Report-Studio-Toolbar)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400530711-Advanced-Running-Reports-Using-the-On-Demand-API)

# Customized Implementation of the Security API

Logi Report Server provides a set of Security API which you can implement to build your preferred [security system](https://devnet.logianalytics.com/hc/en-us/articles/5741483732759-Server-Security-System). This topic describes the rules that you should pay attention to during implementation, and how you can partially implement the Security API and implement the Security API using an XML file.

For more information, see the **jet.server.api.custom.security** package in the Logi Report Javadoc.

This topic contains the following sections:

* [Implementation Rules](#Rule)
* [Partial Implementation of the Security API](#Partial)
* [Implementing the Security API Using an XML File](#XML)
* [Security API Demos](#Demo)

## Implementation Rules

When applying customized Security API, you need to pay attention to the following rules:

* AuthenticationProvider is a core interface and must be implemented. It is first loaded when Logi Report Server loads a customized Security API.
* There are dependency relationships among some interfaces:

  Interfaces PermissionProvider and PrivilegeProvider depend on the corresponding principal interface provider. For example, the prerequisite for applying a customized UserPermissionProvider is that a customized UserProvider has been applied.

  Interface RelationProvider depends on both the corresponding principal interfaces. For example, the prerequisite for applying a customized GroupUserRelationProvider is that a customized UserProvider and GroupProvider have been applied.
* If you partly implement the Security API, Logi Report Server will automatically provide implementation of some missed but required interfaces, to build an integrated security system. See the rules:
  + If customized implementations of Providers have not been applied, Logi Report Server will apply built-in implementations of these Providers, including: AuthorizationProvider, UserProvider, GroupProvider, RoleProvider, GroupUserRelationProvider, RoleGroupRelationProvider, and RoleUserRelationProvider.
  + If you have applied a PermissionProvider or PrivilegeProvider, but not applied an AuthorizationProvider, Logi Report Server will apply the built-in implementation of the AuthorizationProvider.
* If you have applied an AuthorizationProvider, but not applied a PermissionProvider or PrivilegeProvider, for example, UserPermissionProvider or UserPrivilegeProvider, Logi Report Server will not apply the built-in implementation of the PermissionProvider or PrivilegeProvider.

## Partial Implementation of the Security API

The Security API can meet various requirements for seamlessly integrating the Logi Report security system into an existing external security system.

By implementing all interfaces, you provide full functions to the Logi Report Server security system. However, if you do not want to provide a complete security system to your Logi Report Server, but only to use part of the functions available, you can achieve this by implementing the interfaces that meet your requirements.

Here are some examples:

**Example 1**

Requirements: You only want to customize authentication and authorization.

You need to implement the following interfaces: AuthenticationProvider and AuthorizationProvider.

**Example 2**

Requirements: You want to customize authentication and users, while Logi Report Server maintains other functions of the security system.

You need to implement the following interfaces: AuthenticationProvider and UserProvider.

**Example 3**

Requirements: For [Record Level Security/Column Level Security](https://devnet.logianalytics.com/hc/en-us/articles/5741463498263-Record-Level-and-Column-Level-Security) scenario, you must provide user/role information.

You need to implement the following interfaces: AuthenticationProvider, UserProvider, RoleProvider, and RoleUserRelationProvider.

## Implementing the Security API Using an XML File

You can specify a customized implementation of the Security API in an XML file. Logi Report Server loads classes according to this file.

The file is customizedAPI.xml in `<install_root>\bin`. Specify the contents in the .xml file as follows:

```
<?xml version="1.0" encoding="UTF-8"?>  
  
<jreport-customized-api>  
    <security>  
        <authentication-provider>  
            com.customer.security.AuthenticationProviderImpl  
        </authentication-provider>  
        <authorization-provider>  
            com.customer.security.AuthorizationProviderImpl  
        </authorization-provider>  
        <user>  
            provider>  
                com.customer.security.user.UserProviderImpl  
            </provider>  
            <permission-provider>  
                com.customer.security.user.UserPermissionProviderImpl  
            </permission-provider>  
            <privilege-provider>  
                com.customer.security.user.UserPrivilegeProviderImpl  
            </privilege-provider>  
        </user>  
        <group>  
            <provider>  
                com.customer.security.group.GroupProviderImpl  
             </provider>  
            <permission-provider>  
                com.customer.security.group.GroupPermissionProviderImpl  
            </permission-provider>  
            <privilege-provider>  
                com.customer.security.group.GroupPrivilegeProviderImpl  
            </privilege-provider>  
        </group>  
        <role>  
            <provider>  
                com.customer.security.role.RoleProviderImpl  
            </provider>  
            <permission-provider>  
                com.customer.security.role.RolePermissionProviderImpl  
            </permission-provider>  
            <privilege-provider>  
                com.customer.security.role.RolePrivilegeProviderImpl  
                </privilege-provider>  
        </role>  
        <relation>  
            <role-group>  
                com.customer.security.relation.RoleGroupRelationProviderImpl  
            </role-group>  
            <role-user>  
                com.customer.security.relation.RoleUserRelationProviderImpl  
            </role-user>  
            <group-user>  
                com.customer.security.relation.GroupUserRelationProviderImpl  
            </group-user>  
        </relation>  
    </security>  
</jreport-customized-api>
```

## Security API Demos

Demo references available in `<install_root>\help\samples\APISecurity`:

* **DemoAuthenticationProvider.java**  
   Demo for implementation of the jet.server.api.custom.security.AuthenticationProvider interface.
* **DemoAuthorizationProvider.java**  
   Demo for implementation of the jet.server.api.custom.security.AuthorizationProvider interface.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* Logi Report Server provides the ability to use customized user authentication scheme by the implementation of the two interfaces jet.server.api.custom.security.AuthenticationProvider and jet.server.api.custom.security.AuthorizationProvider.
* From v8, Server adds two new methods *addSecurityListener()* and *isEnableEdit()* into the jet.server.api.custom.security.AuthenticationProvider interface. If you have upgraded your Logi Report Server from v7 to a higher version, and have applied customized implementation of AuthenticationProvider in v7, you need to implement the new methods in the API.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741395390999-Customizing-the-Web-Report-Studio-Toolbar)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741400530711-Advanced-Running-Reports-Using-the-On-Demand-API)
