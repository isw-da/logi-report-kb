---
title: "Security Context Support"
id: 1500009711881
section: "Working with APIs Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009711881-Security-Context-Support
updated_at: 2021-11-03T06:58:38Z
---

# Security Context Support

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686142-Exit-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686462-Accessibility)

# Security Context Support

Security Context Support refers to a new set of functionalities that Logi JReport products provide to support Unify NXJ Security Context. Other than using the security system of Logi JReport, Security Context Support allows Unify NXJ developers to write code that obtains user profile information from the security database. Security Context Support may be useful for any developer who uses Java EE Security.

Below is a list of the sections covered in this topic:

* [Configuring Logi JReport Products](#Configure)
* [Security Context APIs](#Security)
* [Using Security Context When Viewing a Report](#View)
* [Using Security Context in the Formula Editor](#Formula)
* [Using Security Context in the Deployment Wizard](#Deploy)

## Configuring Logi JReport Products

**To configure Logi JReport Designer:**

By default, Logi JReport Designer uses its own security system. If you want to enable the Security Context Support, you will first need to configure the config.xml file in `<designer_install_root>\bin`.

1. Add the elements <SecurityContextFactory value=""/> and <DeployWizardFactory value=""/> as the child of the element <Option>.
2. Implement classes to the attribute values. For example, part of the config.xml file might be as follows:

   ```
   <Option>  

       …  
     

       <SecurityContextFactory value="com.utify.JRSecurityContextFactoryImpl"/>  

       <DeployWizardFactory value="com.utify.JRDeployWizardFactoryImpl"/>  

   </Option>
   ```
3. Add the root path of the implementing class packages to the ADDCLASSPATH variable of setenv.bat in `<install_root>\bin`.

Security Context interfaces in Logi JReport Server are different from those of Logi JReport Designer, and you will have to implement the Server interfaces separately.

**To configure Logi JReport Server:**

1. Before you can use the Security Context feature, first configure the server.properties file in `<server_install_root>\bin`.

   Open the server.properites file, and then modify (add if it doesn't exist) the value of the property com.jinfonet.securityContextFactory to be that of your SecurityContextFactory implementing class package and name as follows:

   com.jinfonet.securityContextFactory=mypackage.myclass

   **Tip:** Alternatively, you can add the parameter `–D com.jinfonet.securityContextFactory = mypackage.myclass` to the file JRServer.bat stored in `<server_install_root>\bin`, with which you start Logi JReport Server.
2. Add the root path of the implementing class packages to the class path of the file JRServer.bat.

## Security Context APIs

Logi JReport provides a set of APIs to support the Security Context feature.

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
* **Usage**: A JRSecurityUserDataSource provides data to Logi JReport for generating reports. The JRSecurityUserDataSource class is developed by users of Logi JReport. It can provide data from a flat file, non-relational database, or application data.
* The data returned by this class is in ResultSet object, so users will need to create a ResultSet instance. Then, Logi JReport will use the instance to fetch the data. Users can also create their own ResultSet class.
* **Method**: getResultSet(SecurityContext sc, java.lang.String param) - Gets the data in ResultSet according to parameters.
* **Parameters**:
  + sc - A SecurityContext object, which is implemented by the user.
  + param - The parameter that is to be used for UDS.
* **Return**: The ResultSet object.

**JRSecurityHierarchicalDataSource**

* **Package**: jet.datasource
* **Usage**: A JRSecurityHierarchicalDataSource provides data to Logi JReport for generating reports. The JRSecurityHierarchicalDataSource class is developed by users of Logi JReport. It can provide data from a flat file, non-relational database, or application data.

  The data returned by this class is in JRHierarchicalDataset object, so users will need to create a JRHierarchicalDataset instance. Then, Logi JReport will use the instance to fetch the data. Users can also create their own JRHierarchicalDataset class.
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
  + userName - The user name, for a schedule task it is submitter, for an advance run task, it is login user.
  + resource - The resource of the server. Now, it is only limited to report resource in the server. For example: /SampleReports/Employee Information List.cls
  + versionNumber - The version number of the resource.
* **Return**: The SecurityContext of the specified resource.

**SecurityContext**

* **Package**: jet.server.api
* **Usage**: SecurityContext is an interface that is used to help you implement security context.
* **Methods**:
  + getEmail() - Returns the e-mail address of the user.
  + getRoles() - Returns the roles the user belongs to.
  + getSalutation() - Returns the salutation of the user (for example, Mr., Mrs., and so on).
  + getUserName() - Returns the user name.

## Using Security Context When Viewing a Report

When you view a report that requires the security context to run, Logi JReport Designer will use the implemented JRSecurityContextFactory to instantiate the SecurityContext instance which will be used to execute the report.

## Using Security Context in the Formula Editor

The Formula Editor now allows you to pass the Security Context to a user-defined formula (UDF) function.

You can call *getSecurityContext()* in your formula, which will pass the returning object to your UDF function. The method *getSecurityContext()* returns a DbSecurityContext type object, which provides the method *get()* to get the Security Context instance transfer from Server or Designer.

DbSecurityContext is a new data type for the SecurityContext object, since the data type of all the variables used in UDF functions should be DbValue.

The following is an example.

`Import userClass from "UserFunction";  
userClass.getData(getSecurityContext(), @country, …);`

## Using Security Context in the Deployment Wizard

Logi JReport provides you with two API methods which allow you to bring out your own publishing tool.

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

Below are the working principles:

* Loading DeployWizardFactory class name from configuration information:

  In Logi JReport Designer, there is a config.xml file in `<install_root>\bin`. This file corresponds with the Options dialog. You can make it configurable by modifying the XML file. Designer loads information from the XML file and configures the Options dialog when it starts up.
* Getting DeployWizardFactory class name and showing the customized deployment wizard:

  When you select File > Publish and Download > Publish to Server in Logi JReport Designer, it will first check if there is deployWizardFactory in the ReportOption, and will then try to create new instance by the class name. If the class of the customized deployWizard has been successfully loaded, its wizard will be shown. Otherwise, the default publish wizard will be shown.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686142-Exit-Functions)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009686462-Accessibility)
