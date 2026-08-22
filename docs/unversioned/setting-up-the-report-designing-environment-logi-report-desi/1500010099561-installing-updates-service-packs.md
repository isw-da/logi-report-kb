---
title: "Installing Updates/Service Packs"
id: 1500010099561
section: "Setting Up the Report Designing Environment - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099561-Installing-Updates-Service-Packs
updated_at: 2021-07-23T19:16:16Z
---

# Installing Updates/Service Packs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061122-Installing-and-Running-Designer-on-Unix-Linux)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099541-Solving-Installation-Problems)

# Installing Updates/Service Packs

To apply a Designer Update/Service Pack, you must have already installed Designer. Logi Report includes all resolved issues and new features of an Update/Service Pack in JAR files. When you run the installation file for an Update/Service Pack, Logi Report modifies files in the "lib" directory of the existing Designer to apply the changes. Therefore, you are recommended to back up your current Designer installation before applying any Update or Service Pack. This topic describes the methods to install an Update/Service Pack to an existing Designer.

This topic contains the following sections:

* [Installing an Update/Service Pack Using the Installation Wizard](#Wizard)
* [Installing an Update/Service Pack Silently](#Silent)

## Installing an Update/Service Pack Using the Installation Wizard

You can install an Update/Service Pack for your Designer using the Installation Wizard in the same way as you install a full GA version. For detailed information, select the following links:

* [Installing Designer on Windows](https://devnet.logianalytics.com/hc/en-us/articles/1500010061142-Installing-and-Running-Designer-on-Windows#Install)
* [Installing Designer on macOS](https://devnet.logianalytics.com/hc/en-us/articles/1500010099521-Installing-and-Running-Designer-on-macOS#Install)
* [Installing Designer on Unix/Linux](https://devnet.logianalytics.com/hc/en-us/articles/1500010061122-Installing-and-Running-Designer-on-Unix-Linux#Install)

## Installing an Update/Service Pack Silently

You can install a Designer Update/Service Pack silently without participation in the installation process on Windows, Unix, and Linux.

1. Find the file **update.properties** in `<install_root>\help\samples\SilentInstall` of the current Designer installation directory. You can use this file to create an option file (that is, response file) for the Installation Wizard, which defines all the information that is required for the installation.
2. Edit update.properties to your own requirements.

   You can also create a property file and save it as follows. Modify the lines according to your own environment and configurations.

   `USER_INSTALL_DIR=<designer_install_root>  
   USER_KEY=UID  
   USER_PASSWORD=Password`
3. Open a console window and change the directory to the location of the installation file.

   `$ cd thepath`
4. Run commands to install the Update/Service Pack in the designated path:
   * For Windows, run the following command:

     `$ designer-xxx-win64.exe -i silent -f update.properties`
   * For Unix/Linux:

     First run the following command to make the installation file executable:

     `$ chmod +x designer-xxx-linux.bin`

     Then run the command:

     `$ ./designer-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f update.properties`

Change designer-xxx-win64.exe or designer-xxx-linux.bin to the real file name of the installation file for the Update/Service Pack.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061122-Installing-and-Running-Designer-on-Unix-Linux)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099541-Solving-Installation-Problems)
