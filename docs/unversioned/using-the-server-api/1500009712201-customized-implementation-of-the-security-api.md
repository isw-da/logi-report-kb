---
title: "Customized Implementation of the Security API"
id: 1500009712201
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009712201-Customized-Implementation-of-the-Security-API
updated_at: 2021-11-03T06:58:31Z
---

# Customized Implementation of the Security API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686422-Customizing-the-Web-Report-Studio-Toolbar)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712101-Advanced-Running-Reports-Using-the-On-Demand-API)

# Customized Implementation of the Security API

Logi JReport Server provides a set of Security API which you can implement in order to build your preferred [security system](https://devnet.logianalytics.com/hc/en-us/articles/1500009692622-Server-Security-System). For detailed usage about the Security API, refer to the jet.server.api.custom.security package in the Logi JReport Javadoc.

Below is a list of the sections covered in this topic:

* [Implementation Rules](#Rule)
* [Partial Implementation of the Security API](#Partial)
* [Implementing the Security API Using an XML File](#XML)
* [Security API Demos](#Demo)

## Implementation Rules

When applying customized Security API, you need to pay attention to the following rules:

* AuthenticationProvider is a core interface and must be implemented. It is first loaded when Logi JReport Server loads a customized Security API.
* There are dependency relationships among some interfaces:

  Interfaces PermissionProvider and PrivilegeProvider depend on the corresponding principal interface provider. For example, the prerequisite for applying a customized UserPermissionProvider is that a customized UserProvider has been applied.

  Interface RelationProvider depends on both the corresponding principal interfaces. For example, the prerequisite for applying a customized GroupUserRelationProvider is that a customized UserProvider and GroupProvider have been applied.
* If you partly implement the Security API, Logi JReport Server will automatically provide implementation of some missed but required interfaces, in order to build an integrated security system. Below are the rules:
  + If customized implementations of Providers have not been applied, Logi JReport Server will apply built-in implementations of these Providers, including: AuthorizationProvider, UserProvider, GroupProvider, RoleProvider, GroupUserRelationProvider, RoleGroupRelationProvider, and RoleUserRelationProvider.
  + If you have applied a PermissionProvider or PrivilegeProvider, but not applied an AuthorizationProvider, Logi JReport Server will apply the built-in implementation of the AuthorizationProvider.
* If you have applied an AuthorizationProvider, but not applied a PermissionProvider or PrivilegeProvider, for example, UserPermissionProvider or UserPrivilegeProvider, Logi JReport Server will not apply the built-in implementation of the PermissionProvider or PrivilegeProvider.

## Partial Implementation of the Security API

The Security API can meet various requirements for seamlessly integrating the Logi JReport security system into an existing external security system.

By implementing all interfaces, you provide full functions to the Logi JReport Server security system. However, if you do not want to provide a complete security system to your Logi JReport Server, but only to use part of the functions available, you can achieve this by implementing the interfaces that meet your requirements.

Here are some examples:

**Example 1**

Requirements: You only want to customize authentication and authorization.

The following interfaces are required to be implemented: AuthenticationProvider and AuthorizationProvider.

**Example 2**

Requirements: You want to customize authentication and users, while Logi JReport Server maintains other functions of the security system.

The following interfaces are required to be implemented: AuthenticationProvider and UserProvider.

**Example 3**

Requirements: For [Record Level Security/Column Level Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009718801-Record-level-Security-and-Column-level-Security) scenario, you must provide user/role information.

The following interfaces are required to be implemented: AuthenticationProvider, UserProvider, RoleProvider and RoleUserRelationProvider.

## Implementing the Security API Using an XML File

You can specify a customized implementation of the Security API in an XML file. Logi JReport Server loads classes according to this file.

The file is customizedAPI.xml in `<install_root>\bin`. Specify the content in the .xml file as follows:

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

**Notes:**

* Logi JReport Server provides the ability to use customized user authentication scheme by the implementation of the two interfaces jet.server.api.custom.security.AuthenticationProvider and jet.server.api.custom.security.AuthorizationProvider.
* From V8, two new methods *addSecurityListener()* and *isEnableEdit()* are added into the jet.server.api.custom.security.AuthenticationProvider interface. If you have upgraded your Logi JReport Server from V7 to a higher version, and have applied customized implementation of AuthenticationProvider in V7, you need implement the new methods in the API.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686422-Customizing-the-Web-Report-Studio-Toolbar)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712101-Advanced-Running-Reports-Using-the-On-Demand-API)
