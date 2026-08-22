---
title: "Security Context Support"
id: 1500009628181
section: "Working with APIs - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009628181-Security-Context-Support
updated_at: 2021-07-24T16:05:28Z
---

# Security Context Support

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605142-Exit-Functions) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605102-Auditing-on-Exporting-Printing-and-Saving-of-Reports)

# Security Context Support

Security Context Support refers to a new set of functionalities that Logi Report products provide to support Unify NXJ Security Context. Other than using the security system of Logi Report, Security Context Support allows Unify NXJ developers to write code that obtains user profile information from the security database. This topic describes the Security Context APIs Logi Report provides, how to configure the Logi Report products to adopt Security Context Support, and how to apply Security Context in different scenarios in Logi Report.

This topic includes the following sections:

* [Security Context APIs](#Security)
* [Configuring Logi Report Products for Security Context Support](#Configure)
* [Using Security Context in Viewing Report](#View)
* [Using Security Context in the Formula Editor](#Formula)
* [Using Security Context in the Deployment Wizard](#Deploy)

## Security Context APIs

Logi Report provides a set of APIs to support the Security Context feature.

**JRSecurityContextFactory**

* **Package**: jet.acl.api
* **Usage**: This interface is used to create an instance of SecurityContext.
* **Method**: getSecurityContext(javax.swing.JFrame frame, java.util.Vector roles)
* **Parameters**:
  + frame - The parent window.
  + roles - The role list defined by RLS (Record Level Security).
* **Return**: The SecurityContext object.

**JRSecurityUserDataSource**

* **Package**: jet.datasource
* **Usage**: A JRSecurityUserDataSource provides data to Logi Report for generating reports. The JRSecurityUserDataSource class is developed by users. It can provide data from a flat file, non-relational database, or application data. The data returned by this class is in the ResultSet object, so users will need to create a ResultSet instance. Then, Logi Report will use the instance to fetch the data. Users can also create their own ResultSet class.
* **Method**: getResultSet(SecurityContext sc, java.lang.String param) - Gets the data in ResultSet according to parameters.
* **Parameters**:
  + sc - A SecurityContext object, which is implemented by the user.
  + param - The parameter that is to be used for UDS.
* **Return**: The ResultSet object.

**JRSecurityHierarchicalDataSource**

* **Package**: jet.datasource
* **Usage**: A JRSecurityHierarchicalDataSource provides data to Logi Report for generating reports. The JRSecurityHierarchicalDataSource class is developed by users. It can provide data from a flat file, non-relational database, or application data. The data returned by this class is in the JRHierarchicalDataset object, so users will need to create a JRHierarchicalDataset instance. Then, Logi Report will use the instance to fetch the data. Users can also create their own JRHierarchicalDataset class.
* **Method**: getHierarchicalDataset(SecurityContext sc, java.lang.String param) - Gets the data in JRSecurityHierarchicalDataset according to the Security Context and parameters.
* **Parameters**:
  + sc - A SecurityContext object, which is implemented by the user.
  + param - The parameter that is to be used for HDS.
* **Return**: The JRHierarchicalDataset object.

**SecurityContextFactory**

* **Package**: jet.server.api
* **Usage**: SecurityContextFactory is an interface for implementing the Security Context.
* **Method**: getSecurityContext(java.lang.String realmName, java.lang.String userName, java.lang.String resource, int versionNumber) - Returns the SecurityContext of a specified resource.
* **Parameters**:
  + realmName - The realm name of the current active realm on Logi Report Server.
  + userName - The user name. For a schedule task it is submitter; for an advanced run task, it is the login user.
  + resource - The resource on Logi Report Server. Now, it is only limited to report resource on the server. For example: /SampleReports/Employee Information List.cls
  + versionNumber - The version number of the resource.
* **Return**: The SecurityContext of the specified resource.

**SecurityContext**

* **Package**: jet.server.api
* **Usage**: SecurityContext is an interface for implementing the Security Context.
* **Methods**:
  + getEmail() - Returns the e-mail address of the user.
  + getRoles() - Returns the roles the user belongs to.
  + getSalutation() - Returns the salutation of the user (for example, Mr., Mrs., and so on).
  + getUserName() - Returns the user name.

## Configuring Logi Report Products for Security Context Support

By default, Logi Report uses its own security system. If you want to enable the Security Context Support feature in the Logi Report products, you need to configure the products by yourself.

**To configure Logi Report Designer:**

1. Open the file **config.xml** in `<designer_install_root>\bin,` and add the elements **<SecurityContextFactory value=""/>** and **<DeployWizardFactory value=""/>** as the child of the element <Option>.
2. Implement classes to the attribute values. For example, part of the config.xml file might be as follows:

   ```
   <Option>  
       …  
       <SecurityContextFactory value="com.utify.JRSecurityContextFactoryImpl"/>  
       <DeployWizardFactory value="com.utify.JRDeployWizardFactoryImpl"/>  
   </Option>
   ```
3. Add the root path of the implementing class packages to the ADDCLASSPATH variable of **setenv.bat** in `<install_root>\bin`.

Security Context interfaces in Logi Report Server are different from those in Logi Report Designer, so you need to implement the Server interfaces separately.

**To configure Logi Report Server:**

1. Open the file **server.properites** in `<server_install_root>\bin`, and modify the value of the property **com.jinfonet.securityContextFactory** (add the property if it doesn't exist) to be that of your SecurityContextFactory implementing class package and name as follows:

   com.jinfonet.securityContextFactory=mypackage.myclass

   **Tip:** Alternatively, you can add the parameter `–D com.jinfonet.securityContextFactory = mypackage.myclass` to the file **JRServer.bat** in `<server_install_root>\bin` with which you start your Logi Report Server.
2. Add the root path of the implementing class packages to the class path of the file **JRServer.bat**.

## Using Security Context in Viewing Report

When you view a report that requires the Security Context to run, Logi Report Designer will use the implemented JRSecurityContextFactory to instantiate the SecurityContext instance which will be used to execute the report.

## Using Security Context in the Formula Editor

The Formula Editor allows you to pass the Security Context to a user defined formula (UDF) function.

You can call *getSecurityContext()* in your formula, which will pass the returning object to your UDF function. The method *getSecurityContext()* returns a DbSecurityContext type object, which provides the method *get()* to get the Security Context instance transfer from Server or Designer.

DbSecurityContext is a new data type for the SecurityContext object. The data type of all the variables used in UDF functions should be DbValue. The following shows an example.

`Import userClass from "UserFunction";  
userClass.getData(getSecurityContext(), @country, …);`

## Using Security Context in the Deployment Wizard

Logi Report provides you with two API methods which allow you to bring out your own deployment tool.

**DeploymentWizard**

* **Package**: com.jinfonet.designer.deployment.api
* **Usage**: DeploymentWizard is an interface used for implementing the customized deployment wizard.
* **Method**: deploy (Frame frame, String catFullPathName, String reporthome).
* **Parameters**:
  + frame - The frame of the deployment wizard.
  + catalogFullPath - The full path name of the catalog file.
  + reporthome - The report home path.

**DeploymentWizardFactory**

* **Package**: com.jinfonet.designer.deployment.api
* **Usage**: DeploymentWizardFactory is an interface used for implementing the customized deployment wizard.
* **Method**: getDeploymentWizard() - Returns the DeploymentWizard.

See the working principles:

* Loading DeployWizardFactory class name from configuration information:

  In Logi Report Designer, you can find the file config.xml stored in `<designer_install_root>\bin`. This file corresponds with the Options dialog. You can modify the XML file to suit your requirements. Designer loads information from the XML file and configures the Options dialog when it starts up.
* Getting DeployWizardFactory class name and showing the customized deployment wizard:

  When you select an item in the File > Publish menu in Logi Report Designer, Designer will first check if there is deployWizardFactory in ReportOption, and will then try to create new instance by the class name. If the class of the customized deployWizard has been successfully loaded, the corresponding wizard will be shown. Otherwise, Designer will show the default wizard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009605142-Exit-Functions) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009605102-Auditing-on-Exporting-Printing-and-Saving-of-Reports)
