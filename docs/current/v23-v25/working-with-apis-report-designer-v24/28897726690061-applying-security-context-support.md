---
title: "Applying Security Context Support"
id: 28897726690061
section: "Working with APIs - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897726690061-Applying-Security-Context-Support
updated_at: 2024-09-30T09:10:35Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Applying Security Context Support

Security Context Support refers to a new set of functionalities that Report products provide to support Unify NXJ Security Context. Other than using the security system of Report, Security Context Support enables Unify NXJ developers to write code that obtains user profile information from the security database.  This topic describes the Security Context APIs Report provides, how you can configure the Report products to adopt Security Context Support and apply Security Context in different scenarios in Report.

This topic contains the following sections:

- Security Context APIs

- Configuring Report Products for Security Context Support

- Using Security Context in Viewing Report

- Using Security Context in the Formula Editor

- Using Security Context in the Deployment Wizard

## 
Security Context APIs

Report provides a set of APIs to support the Security Context feature.

- 
JRSecurityContextFactory
This interface is in the jet.acl.api package. You can use it  to create an instance of SecurityContext.The interface contains one method: getSecurityContext(javax.swing.JFrame frame, java.util.Vector roles). You can call it to return the SecurityContext object. The following are parameters in the method:

- 
frame
The parent window.

- 
roles
The role list defined by RLS (Record Level Security).

- 
JRSecurityUserDataSource
This interface is in the jet.datasource package. A JRSecurityUserDataSource provides data to Report for generating reports.  You can develop the JRSecurityUserDataSource class according to your requirements to provide data from a flat file, non-relational database, or application data. The data returned by this class is in the ResultSet object, so you need to create a ResultSet instance. Then, Report uses the instance to fetch the data. You can also create their own ResultSet class.The interface contains one method: getResultSet(SecurityContext sc, java.lang.String param). You can call it to get data in ResultSet according to parameters. The following are parameters in the method:

- 
sc
A SecurityContext object you implement.

- 
param
The parameter that is to be used for UDS.

- 
JRSecurityHierarchicalDataSource
This interface is in the jet.datasource package. A JRSecurityHierarchicalDataSource provides data to Report for generating reports. You can develop JRSecurityHierarchicalDataSource according to your requirements to provide data from a flat file, non-relational database, or application data. The data returned by this class is in the JRHierarchicalDataset object, so you need to create a JRHierarchicalDataset instance. Then, Report uses the instance to fetch the data. You can also create their own JRHierarchicalDataset class.The interface contains one method: getHierarchicalDataset(SecurityContext sc, java.lang.String param). You can call it to get data in JRSecurityHierarchicalDataset according to the Security Context and parameters. The following are parameters in the method:

- 
sc
A SecurityContext object you implement.

- 
param
The parameter that is to be used for HDS.

- 
SecurityContextFactory
This interface is in the jet.server.api package. You can use it to implement the Security Context. The interface contains one method: getSecurityContext(java.lang.String realmName, java.lang.String userName, java.lang.String resource, int versionNumber). You can call it to return the SecurityContext of a specified resource. The following are parameters in the method:

- 
realmName
The realm name of the current active realm on Server.

- 
userName
The user name. For a schedule task, it is submitter; for an advanced run task, it is the user signing in to Server.

- 
resource
The resource on Server. Now, it is limited to report resource only. For example: /SampleReports/Employee Information List.cls

- 
versionNumber
The version number of the resource.

- 
SecurityContext
This interface is in the jet.server.api package. You can use it to implement the Security Context. The interface contains the following methods:

- 
getEmail()
This method returns the email address of the user.

- 
getRoles()
This method returns the roles the user belongs to.

- 
getSalutation()
This method returns the salutation of the user (for example, Mr., Mrs., and so on).

- 
getUserName()
This method returns the user name.

## 
Configuring Report Products for Security Context Support 

By default, Report uses its own security system. If you want to enable the Security Context Support feature in the Report products, you need to configure the products by yourself.

To configure  Designer

- Open the file config.xml in <designer_install_root>\bin, and add the elements <SecurityContextFactory value=""/> and <DeployWizardFactory value=""/> as the child of the element <Option>.

- Implement classes to the attribute values. For example, part of the config.xml file might be:
                <Option>

    …

    <SecurityContextFactory value="com.utify.JRSecurityContextFactoryImpl"/>

    <DeployWizardFactory value="com.utify.JRDeployWizardFactoryImpl"/>

</Option>

- Add the root path of the implementing class packages to the ADDCLASSPATH variable of setenv.bat in <install_root>\bin.

Security Context interfaces are different between  Designer and Server, so you need to implement the Server interfaces separately.

To configure Server

- Open the file server.properites in <server_install_root>\bin, and modify the value of the property com.jinfonet.securityContextFactory  (add the property if it doesn't exist) to be that of your SecurityContextFactory implementing class package and name.com.jinfonet.securityContextFactory=mypackage.myclass

Alternatively, you can add the parameter –D com.jinfonet.securityContextFactory = mypackage.myclass to the file JRServer.bat in <server_install_root>\bin with which you start your Server.

- Add the root path of the implementing class packages to the class path of the file JRServer.bat.

## 
Using Security Context in Viewing Report

When you view a report that requires the Security Context to run, Designer applies the implemented JRSecurityContextFactory to instantiate the SecurityContext instance that it uses to execute the report.

## 
Using Security Context in the Formula Editor

The Formula Editor enables you to pass the Security Context to a user-defined function (UDF) .

You can call getSecurityContext() in your formula, which passes the returned object to your UDF function. The getSecurityContext() method returns a DbSecurityContext type object, which provides the get() method to get the Security Context instance transfer from Server or Designer.

DbSecurityContext is a new data type for the SecurityContext object. The data type of all the variables used in UDF functions should be DbValue. The following shows an example.

Import userClass from "UserFunction";

userClass.getData(getSecurityContext(), @country, …);

## 
Using Security Context in the Deployment Wizard

Report provides you some API methods that enable you to bring out your own deployment tool.

- 
DeploymentWizard
This interface is in the com.jinfonet.designer.deployment.api package. You can use it to implement the customized deployment wizard.
                The interface contains one method: deploy (Frame frame, String catFullPathName, String reporthome). The following are parameters in the method:

- 
frame
The frame of the deployment wizard.

- 
catalogFullPath
The full path of the catalog file.

- 
reporthome
The report home path.

- 
DeploymentWizardFactory
This interface is in the com.jinfonet.designer.deployment.api package. You can use it to implement the customized deployment wizard.The interface contains one method: getDeploymentWizard(), which you can call to return the DeploymentWizard.

The following are the working principles:

- Loading DeployWizardFactory class name from configuration information.In Designer, you can find config.xml stored in <designer_install_root>\bin. This file corresponds with the Options dialog box. You can modify the XML file to suit your requirements. Designer loads information from the XML file and configures the Options dialog box when it starts up.

- Getting DeployWizardFactory class name and showing the customized deployment wizard. When you select an option from the Publish drop-down menu in the File ribbon in Designer, Designer first checks if there is deployWizardFactory in ReportOption, and then tries to create new instance by the class name. If Designer can load the class of the customized deployWizard successfully, it displays the corresponding wizard; otherwise, Designer displays the default wizard.

Previous Topic  Next Topic
