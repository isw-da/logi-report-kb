---
title: "Security Context Support"
id: 1500010063041
section: "Working with APIs - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063041-Security-Context-Support
updated_at: 2021-07-24T10:39:35Z
---

# Security Context Support

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063021-Exit-Functions) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063081-Accessibility)

# Security Context Support

Security Context Support refers to a new set of functionalities that Logi JReport products provide to support Unify NXJ Security Context. Other than using the security system of Logi JReport, Security Context Support allows Unify NXJ developers to write code that obtains user profile information from the security database. Security Context Support may be useful for any developer who uses Java EE Security.

Below is a list of the sections covered in this topic:

* [Security Context APIs](#Security)
* [Configuring Logi JReport Products for Security Context Support](#Configure)
* [Using Security Context in Viewing Report](#View)
* [Using Security Context in the Formula Editor](#Formula)
* [Using Security Context in the Deployment Wizard](#Deploy)

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
* The data returned by this class is in JRHierarchicalDataset object, so users will need to create a JRHierarchicalDataset instance. Then, Logi JReport will use the instance to fetch the data. Users can also create their own JRHierarchicalDataset class.
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
  + resource - The resource of the server. Now, it is only limited to report resource in the server. For example: /SampleReports/Corporate Overview.cls
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

## Configuring Logi JReport Products for Security Context Support

By default, Logi JReport uses its own security system. If you want to enable the Security Context Support feature in the Logi JReport products, you need to configure the products by yourself.

**To configure Logi JReport Designer:**

1. Open the file config.xml in `<designer_install_root>\bin,` and add the elements <SecurityContextFactory value=""/> and ><DeployWizardFactory value=""/> as the child of the element <Option>.
2. Implement classes to the attribute values. For example, part of the config.xml file might be as follows:

   ```
   <Option>  

       …  

       <SecurityContextFactory value="com.utify.JRSecurityContextFactoryImpl"/>  

       <DeployWizardFactory value="com.utify.JRDeployWizardFactoryImpl"/>  

   </Option>
   ```
3. Add the root path of the implementing class packages to the ADDCLASSPATH variable of setenv.bat in `<install_root>\bin`.

Security Context interfaces in Logi JReport Server are different from those of Logi JReport Designer, so you need to implement the Server interfaces separately.

**To configure Logi JReport Server:**

1. Open the server.properites file in `<server_install_root>\bin`, and modify (add if it doesn't exist) the value of the property com.jinfonet.securityContextFactory to be that of your SecurityContextFactory implementing class package and name as follows:

   com.jinfonet.securityContextFactory=mypackage.myclass

   **Tip:** Alternatively, you can add the parameter `–D com.jinfonet.securityContextFactory = mypackage.myclass` to the file JRServer.bat with which you start your Logi JReport Server.
2. Add the root path of the implementing class packages to the class path of the file JRServer.bat.

## Using Security Context in Viewing Report

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
  + reporthome - The report home path.

**DeploymentWizardFactory**

* **Package**: com.jinfonet.designer.deployment.api
* **Usage**: DeploymentWizardFactory is an interface used for implementing the customized deployment wizard.
* **Method**: getDeploymentWizard() - Returns the DeploymentWizard.

Below are the working principles:

* Loading DeployWizardFactory class name from configuration information:

  In Logi JReport Designer, there is a config.xml file in `<``install_root>\bin`. This file corresponds with the Options dialog. You can make it configurable by modifying the XML file. Designer loads information from the XML file and configures the Options dialog when it starts up.
* Getting DeployWizardFactory class name and showing the customized deployment wizard:

  When you select File > Publish and Download > Publish to Server in Logi JReport Designer, it will first check if there is deployWizardFactory in the ReportOption, and will then try to create new instance by the class name. If the class of the customized deployWizard has been successfully loaded, its wizard will be shown. Otherwise, the default publish wizard will be shown.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063021-Exit-Functions) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010063081-Accessibility)
