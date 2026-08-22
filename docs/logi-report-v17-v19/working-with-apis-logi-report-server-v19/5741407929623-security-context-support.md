---
title: "Security Context Support"
id: 5741407929623
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741407929623-Security-Context-Support
updated_at: 2022-10-31T17:15:43Z
---

# Security Context Support

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9305227644055/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394590743-Exit-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9305200977175/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741401942167-Dialog-Boxes-in-Logi-Report-Server-v19)

# Security Context Support

Security Context Support refers to a new set of functionalities that Logi Report products provide to support Unify NXJ Security Context. This topic describes the Security Context APIs, how to configure the Logi Report products to adopt Security Context Support, and how to apply Security Context in different scenarios in Logi Report.

Other than using the security system of Logi Report, Security Context Support enables Unify NXJ developers to write code to obtain user profile information from the security database.

This topic contains the following sections:

* [Security Context APIs](#Security)
* [Configuring Logi Report Products for Security Context Support](#Configure)
* [Using Security Context When Viewing a Report](#View)
* [Using Security Context in the Formula Editor](#Formula)
* [Using Security Context in the Deployment Wizard](#Deploy)

## Security Context APIs

Logi Report provides a set of APIs to support the Security Context feature.

**JRSecurityContextFactory**

* **Package**: jet.acl.api
* **Usage**: This interface is used to help the user to create an instance of SecurityContext.
* **Method**: getSecurityContext(javax.swing.JFrame frame, java.util.Vector roles)
* **Parameters**:
  + frame - The parent window.
  + roles - The role list defined by RLS (Record Level Security).
* **Return**: The SecurityContext object.

**JRSecurityUserDataSource**

* **Package**: jet.datasource
* **Usage**: A JRSecurityUserDataSource provides data to Logi Report for generating reports. The JRSecurityUserDataSource class is developed by users of Logi Report. It can provide data from a flat file, non-relational database, or application data.
* The data returned by this class is in ResultSet object, so users will need to create a ResultSet instance. Then, Logi Report will use the instance to fetch the data. Users can also create their own ResultSet class.
* **Method**: getResultSet(SecurityContext sc, java.lang.String param) - Gets the data in ResultSet according to parameters.
* **Parameters**:
  + sc - A SecurityContext object, which is implemented by the user.
  + param - The parameter that is to be used for UDS.
* **Return**: The ResultSet object.

**JRSecurityHierarchicalDataSource**

* **Package**: jet.datasource
* **Usage**: A JRSecurityHierarchicalDataSource provides data to Logi Report for generating reports. The JRSecurityHierarchicalDataSource class is developed by users of Logi Report. It can provide data from a flat file, non-relational database, or application data.

  The data returned by this class is in JRHierarchicalDataset object, so users will need to create a JRHierarchicalDataset instance. Then, Logi Report will use the instance to fetch the data. Users can also create their own JRHierarchicalDataset class.
* **Method**: getHierarchicalDataset(SecurityContext sc, java.lang.String param) - Gets the data in JRSecurityHierarchicalDataset according to the security context and parameters.
* **Parameters**:
  + sc - A SecurityContext object, which is implemented by the user.
  + param - The parameter that is to be used for HDS.
* **Return**: The JRHierarchicalDataset object.

**SecurityContextFactory**

* **Package**: jet.server.api
* **Usage**: SecurityContextFactory is an interface that is used to help you implement security context.
* **Method**: getSecurityContext(java.lang.String realmName, java.lang.String userName, java.lang.String resource, int versionNumber) - Returns the SecurityContext of a specified resource.
* **Parameters**:
  + realmName - The realm name of the current active realm of the server.
  + userName - The username, for a schedule task it is submitter, for an advance run task, it is the user who signed in.
  + resource - The resource of the server. Now, it is only limited to report resource in the server. For example: /SampleReports/Employee Information List.cls
  + versionNumber - The version number of the resource.
* **Return**: The SecurityContext of the specified resource.

**SecurityContext**

* **Package**: jet.server.api
* **Usage**: SecurityContext is an interface that is used to help you implement security context.
* **Methods**:
  + getEmail() - Returns the email address of the user.
  + getRoles() - Returns the roles the user belongs to.
  + getSalutation() - Returns the salutation of the user (for example, Mr., Mrs., and so on).
  + getUserName() - Returns the username.

## Configuring Logi Report Products for Security Context Support

By default, Logi Report uses its own security system. If you want to enable the Security Context Support feature in the Logi Report products, you need to configure the products by yourself.

**To configure Logi Report Designer:**

1. Open the file **config.xml** in `<designer_install_root>\bin`.
2. Add the elements **<SecurityContextFactory value=""/>** and **<DeployWizardFactory value=""/>** as the child of the element **<Option>**.
3. Implement classes to the attribute values. See a part of the **config.xml** file which could be:

   ```
   <Option>  
       …  
     
       <SecurityContextFactory value="com.utify.JRSecurityContextFactoryImpl"/>  
       <DeployWizardFactory value="com.utify.JRDeployWizardFactoryImpl"/>  
   </Option>
   ```
4. Add the root path of the implementing class packages to the ADDCLASSPATH variable of **setenv.bat** in `<install_root>\bin`.

Security Context interfaces in Logi Report Server are different from those in Logi Report Designer, so you need to implement the Server interfaces separately.

**To configure Logi Report Server:**

1. Open the file **server.properties** in `<server_install_root>\bin`, and then modify the value of the property **com.jinfonet.securityContextFactory** (add the property if it does not exist) to be that of your SecurityContextFactory implementing class package and name as follows:

   com.jinfonet.securityContextFactory=mypackage.myclass

   **Tip:** Alternatively, you can add the parameter `–D com.jinfonet.securityContextFactory = mypackage.myclass` to the file **JRServer.bat** in `<server_install_root>\bin` with which you start your Logi Report Server.
2. Add the root path of the implementing class packages to the class path of the file **JRServer.bat**.

## Using Security Context When Viewing a Report

When you view a report that requires the Security Context to run, Designer will use the implemented JRSecurityContextFactory to instantiate the SecurityContext instance to run the report.

## Using Security Context in the Formula Editor

The Formula Editor enables you to pass the Security Context to a user defined formula (UDF) function.

You can call *getSecurityContext()* in your formula, which will pass the returning object to your UDF function. The method *getSecurityContext()* returns a DbSecurityContext type object, which provides the method *get()* to get the Security Context instance transfer from Server or Designer.

DbSecurityContext is a new data type for the SecurityContext object. The data type of all the variables used in UDF functions should be DbValue. The following shows an example.

`Import userClass from "UserFunction";  
userClass.getData(getSecurityContext(), @country, …);`

## Using Security Context in the Deployment Wizard

Logi Report provides you with two API methods which enable you to bring out your own deployment tool.

**DeploymentWizard**

* **Package**: com.jinfonet.designer.deployment.api
* **Usage**: DeploymentWizard is an interface used for implementing the customized publishing wizard.
* **Method**: deploy (Frame frame, String catFullPathName, String reporthome).
* **Parameters**:
  + frame - The frame of the deployment box.
  + catalogFullPath - The full path name of the catalog file.
  + reporthome - The reporthome path.

**DeploymentWizardFactory**

* **Package**: com.jinfonet.designer.deployment.api
* **Usage**: DeploymentWizardFactory is an interface used for implementing the customized deployment wizard.
* **Method**: getDeploymentWizard() - Returns the DeploymentWizard.

See the working principles:

* Loading DeployWizardFactory class name from configuration information:

  In Logi Report Designer, you can find the file **config.xml** in `<install_root>\bin`. This file corresponds with the Options dialog box. You can modify the XML file to suit your requirements. Designer loads information from the XML file and configures the Options dialog box when it starts up.
* Getting DeployWizardFactory class name and showing the customized deployment wizard:

  When you select an item in the File > Publish menu in Logi Report Designer, Designer first checks if there is deployWizardFactory in ReportOption, and then tries to create new instance by the class name. If the class of the customized deployWizard has successfully loaded, the corresponding wizard displays. Otherwise, Designer displays the default wizard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9305227644055/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394590743-Exit-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9305200977175/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741401942167-Dialog-Boxes-in-Logi-Report-Server-v19)
