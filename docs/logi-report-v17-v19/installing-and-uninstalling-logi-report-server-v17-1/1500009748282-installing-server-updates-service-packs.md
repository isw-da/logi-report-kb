---
title: "Installing Server Updates/Service Packs"
id: 1500009748282
section: "Installing and Uninstalling Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748282-Installing-Server-Updates-Service-Packs
updated_at: 2021-07-24T00:48:05Z
---

# Installing Server Updates/Service Packs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776741-Installing-Server-by-Deploying-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748242--Server-Report-Home-Directory-Overview)

# Installing Server Updates/Service Packs

This topic describes how you can install an Update/Service Pack to Server silently or using the Installation Wizard and apply an Update/Service Pack to EAR/WAR files.

You must have already installed Server before you apply a Server Update/Service Pack. Logi Report includes all resolved issues and new features of an Update/Service Pack in JAR files. When you run the installation file for an Update/Service Pack, Logi Report modifies the files in the lib directory of the existing Server to apply the changes. It may also update the JSP files in the public\_html directory according to the new features and resolved issues. It does not change your Server configuration. Therefore, you should back up your current Server installation before applying any Update or Service Pack.

This topic contains the following sections:

* [Installing an Update/Service Pack Using the Installation Wizard](#Wizard)
* [Installing an Update/Service Pack Silently](#Silent)
* [Applying an Update/Service Pack to EAR/WAR Files](#EAR)

## Installing an Update/Service Pack Using the Installation Wizard

You can install an Update/Service Pack for your Server using the Installation Wizard in the same way as you install a full GA version. For more information, see [Installing Server Using the Installation Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009748322-Installing-Server-Using-the-Installation-Wizard).

## Installing an Update/Service Pack Silently

You can install a Server Update/Service Pack silently without participation in the installation process on Windows, Unix, and Linux.

1. Find the file **update.properties** in `<install_root>\help\samples\SilentInstall` of the current Server installation directory. This file is used to create an option file (that is, response file) for the Installation Wizard. It defines all the information that the installation requires.
2. Edit **update.properties** to your requirements.

   You can also create a property file and save it as follows. Modify the lines according to your environment and configurations.

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

In order to apply an Update/Service Pack to your web application, you need to update the EAR/WAR files. When you install the Update/Service Pack to the same location where you installed Server, you will get a notification about which files are being updated and overwritten. After the installation finishes, you can also refer to Update.htm in the `<install_root>\help\update` directory for a list of the files that have been modified.

Because Logi Report can be embedded using various configurations, you can update the EAR/WAR files in different ways.

### Using the Server API in EAR/WAR Files

After you install an Update/Service Pack, new JAR files will replace the old versions in the `<install_root>\lib` directory of the existing Server. Therefore, you will need to remove all the existing Logi Report JAR files in your current EAR/WAR files and copy those new JAR files into your EAR/WAR files to update them.

For the list of the JAR files that you need to copy from the updated `<install_root>\lib` directory into your EAR/WAR files, see [Installing the Server API.](https://devnet.logianalytics.com/hc/en-us/articles/1500009743082-Installing-the-Server-API)

### Integrating Servlets & JSPs into EAR/WAR Files

To apply an Update/Service Pack to the EAR/WAR files, follow the integration steps and re-integrate the updated version of Server as described in [Logi Report Server Integration](https://devnet.logianalytics.com/hc/en-us/articles/1500009748382-Logi-Report-Server-Integration).

Since Updates/Service Packs only update JAR files and some JSPs, a faster method to update your EAR/WAR files is to use the updated JAR files in the lib directory of Server to replace the JAR files in the EAR/WAR files. If you have not modified the JSP pages in your EAR/WAR files, you can simply copy the new JSP folders into your EAR/WAR files to replace the existing files. Then clear the class files compiled from JSP.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If your Servers are clustered, you should install the Updates/Service Packs on each clustered server node because each node has an independent installation directory. Then you should modify the EAR/WAR files with the updated JAR files and JSPs on each clustered server node of the web application server, or update a single EAR/WAR file with the new JAR files and JSPs and then deploy it to each web application server cluster node.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776741-Installing-Server-by-Deploying-a-WAR-File)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009748242--Server-Report-Home-Directory-Overview)
