---
title: "Installing Service Packs"
id: 4411769083671
section: "Setting Up the Report Designing Environment - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4411769083671-Installing-Service-Packs
updated_at: 2022-01-27T20:34:04Z
---

# Installing Service Packs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661775895-Installing-and-Running-Designer-on-UNIX-Linux)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661774871-Solving-Installation-Problems)

# Installing Service Packs

To apply a Designer Service Pack, you must have already installed Designer. Logi Report includes all resolved issues of a Service Pack in JAR files. When you run the installation file for a Service Pack, Logi Report modifies files in the lib folder of the existing Designer to apply the changes; therefore, you may want to back up your current Designer installation before applying any Service Pack. This topic describes the methods to install a Service Pack to an existing Designer.

This topic contains the following sections:

* [Installing a Service Pack Using the Installation Wizard](#Wizard)
* [Installing a Service Pack Silently](#Silent)

## Installing a Service Pack Using the Installation Wizard

You can install a Service Pack for your Designer using the Installation Wizard in the same way as you install a full GA version. For more information, select the following links:

* [Installing Designer on Windows](https://devnet.logianalytics.com/hc/en-us/articles/4405664605975-Installing-and-Running-Designer-on-Windows#Install)
* [Installing Designer on macOS](https://devnet.logianalytics.com/hc/en-us/articles/4405661773847-Installing-and-Running-Designer-on-macOS#Install)
* [Installing Designer on UNIX/Linux](https://devnet.logianalytics.com/hc/en-us/articles/4405661775895-Installing-and-Running-Designer-on-UNIX-Linux#Install)

## Installing a Service Pack Silently

You can install a Designer Service Pack silently without participation in the installation process on Windows, UNIX, and Linux.

1. Find the file **update.properties** in `<install_root>\help\samples\SilentInstall` of the current Designer installation directory. You can use this file to create an option file (that is, response file) for the Installation Wizard, which defines all the information that is required for the installation.
2. Edit update.properties to your own requirements.

   You can also create a property file and save it as follows. Modify the lines according to your own environment and configurations.

   `USER_INSTALL_DIR=<designer_install_root>  
   USER_KEY=UID  
   USER_PASSWORD=Password`
3. Open a console window and change the directory to the location of the installation file.

   `$ cd thepath`
4. Run commands to install the Service Pack in the designated path.
   * For Windows, run the following command:

     `$ designer-xxx-win64.exe -i silent -f update.properties`
   * For UNIX/Linux:

     First run the following command to make the installation file executable:

     `$ chmod +x designer-xxx-linux.bin`

     Then run the command:

     `$ ./designer-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f update.properties`

Change **designer-xxx-win64.exe** or **designer-xxx-linux.bin** to the real file name of the installation file for the Service Pack.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661775895-Installing-and-Running-Designer-on-UNIX-Linux)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661774871-Solving-Installation-Problems)
