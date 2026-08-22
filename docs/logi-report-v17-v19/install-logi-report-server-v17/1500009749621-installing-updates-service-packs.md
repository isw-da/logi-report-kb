---
title: "Installing Updates/Service Packs"
id: 1500009749621
section: "Install Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749621-Installing-Updates-Service-Packs
updated_at: 2021-07-25T07:19:05Z
---

# Installing Updates/Service Packs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722682-Installing-by-Deploying-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722622-Logi-Report-Server-Reporthome-Directory-Overview)

# Installing Updates/Service Packs

To apply a Logi Report Server Update/Service Pack, you must have already installed the Server. Logi Report includes all resolved issues and new features of an Update/Service Pack in JAR files. When you run the installation file for an Update/Service Pack, Logi Report will modify files in the lib directory of the existing Server to apply the changes. The JSP files in the public\_html directory may also be updated according to the new features and resolved issues. Therefore, you are recommended to back up your current Server installation before applying any Update or Service Pack. The configuration of your Server will not be changed. This topic describes the methods to install an Update/Service Pack to Logi Report Server and how you can apply an Update/Service Pack to EAR/WAR files.

Select the following links to view the topics:

* [Installing an Update/Service Pack Using the Installation Wizard](#Wizard)
* [Installing an Update/Service Pack Silently](#Silent)
* [Applying an Update/Service Pack to EAR/WAR Files](#EAR)

## Installing an Update/Service Pack Using the Installation Wizard

You can install an Update/Service Pack for your Logi Report Server using the Installation Wizard in the same way as you install a full GA version. For detailed information, refer to [Installing Using the Installation Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009749661-Installing-Using-the-Installation-Wizard).

## Installing an Update/Service Pack Silently

You can install a Logi Report Server Update/Service Pack silently without participation in the installation process on Windows, Unix, and Linux.

1. Fine the file update.properties in `<install_root>\help\samples\SilentInstall` of the current Logi Report Server installation directory. This file is used to create an option file (that is, response file) for the Installation Wizard. It defines all the information that is required for the installation.
2. Edit update.properties to your own requirements.

   You can also create a property file and save it as follows. Modify the lines according to your own environment and configurations.

   `USER_INSTALL_DIR=<server_install_root>  
   USER_KEY=UID  
   USER_PASSWORD=Password`
3. Open a console window and change the directory to the location of the installation file.

   `$ cd thepath`
4. Run commands to install the Update/Service Pack in the designated path:
   * For Windows, run the following command:

     `$ server-xxx-win64.exe -i silent -f update.properties`
   * For Unix/Linux:

     First run the following command to make the installation file executable:

     `$ chmod +x server-xxx-linux.bin`

     Then run the command:

     `$ ./server-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f update.properties`

   Change server-xxx-win64.exe or server-xxx-linux.bin to the real file name of the installation file for the Update/Service Pack.

## Applying an Update/Service Pack to EAR/WAR Files

In order to apply an Update/Service Pack to your web Application, the EAR/WAR files must be updated. When you install the Update/Service Pack to the same location where Logi Report Server is installed, you will be notified which files are being updated and overwritten. After the installation finishes, you can also refer to Update.htm in the `<install_root>\help\update` directory for a list of the files that have been modified.

Because Logi Report can be embedded using various configurations, you can update the EAR/WAR files in different ways.

### Using the Server API in EAR/WAR Files

After you install an Update/Service Pack, new JAR files will replace the old versions in the `<install_root>\lib` directory of the existing Logi Report Server. Therefore you will need to remove all the existing Logi Report JAR files in your current EAR/WAR files and copy those new JAR files into your EAR/WAR files to update them.

For the list of the JAR files that you need to copy from the updated `<install_root>\lib` directory into your EAR/WAR files, refer to [Installing the Server API.](https://devnet.logianalytics.com/hc/en-us/articles/1500009718362-Installing-the-Server-API)

### Integrating Servlets & JSPs into EAR/WAR Files

To apply an Update/Service Pack to the EAR/WAR files, follow the integration steps and re-integrate the updated version of Logi Report Server as described in [Logi Report Server Integration](https://devnet.logianalytics.com/hc/en-us/articles/1500009722742-Logi-Report-Server-Integration).

Since Updates/Service Packs only update JAR files and some JSPs, a faster method to update your EAR/WAR files is to use the updated JAR files in the lib directory of Logi Report Server to replace the JAR files in the EAR/WAR files. If you have not modified the JSP pages in your EAR/WAR files, you can simply copy the new JSP folders into your EAR/WAR files to replace the existing files. Then clear the class files compiled from JSP.

**Note:** If your Logi Report Servers are clustered, you must install the Updates/Service Packs on each clustered server node because each node has an independent installation directory. Then you must modify the EAR/WAR files with the updated JAR files and JSPs on each clustered server node of the web application server, or update a single EAR/WAR file with the new JAR files and JSPs and then deploy it to each web application server cluster node.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722682-Installing-by-Deploying-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722622-Logi-Report-Server-Reporthome-Directory-Overview)
