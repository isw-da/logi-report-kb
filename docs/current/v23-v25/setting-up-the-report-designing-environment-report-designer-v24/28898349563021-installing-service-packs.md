---
title: "Installing Service Packs"
id: 28898349563021
section: "Setting Up the Report Designing Environment - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898349563021-Installing-Service-Packs
updated_at: 2024-09-30T09:10:27Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Installing Service Packs

To apply a Designer Service Pack, you must have already installed Designer. Report includes all resolved issues of a Service Pack in JAR files. When you run the installation file for a Service Pack, Report modifies files in the lib folder of the existing Designer to apply the changes; therefore, you may want to back up your current Designer installation before applying any Service Pack. This topic describes the methods to install a Service Pack to an existing Designer.

This topic contains the following sections:

- Installing a Service Pack Using the Installation Wizard

- Installing a Service Pack Silently

## 
Installing a Service Pack Using the Installation Wizard

You can install a Service Pack for your Designer using the Installation Wizard in the same way as you install a full GA version. For more information, select the following links:

- Installing  Designer on Windows

- Installing  Designer on macOS

- Installing Designer on UNIX/Linux

## 
Installing a Service Pack Silently

You can install a Designer Service Pack silently without participation in the installation process on Windows, UNIX, and Linux.

- Find the file update.properties in <install_root>\help\samples\SilentInstall of the current Designer installation directory. You can use this file  to create an option file (that is, response file) for the Installation Wizard, which defines all the information that is required for the installation. 

- Edit update.properties to your own requirements. You can also create a property file and save it as follows. Modify the lines according to your own environment and configurations.

USER_INSTALL_DIR=<designer_install_root>
USER_KEY=UID
USER_PASSWORD=Password

- Open a console window and change the directory to the location of the installation file.$ cd thepath

- Run commands to install the Service Pack in the designated path.
- For Windows, run the following command:$ designer-xxx-win64.exe -i silent -f update.properties

- For UNIX/Linux:
						First run the following command to make the installation file executable:

$ chmod +x designer-xxx-linux.bin

Then run the command:

$ ./designer-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f update.properties

Change designer-xxx-win64.exe or designer-xxx-linux.bin to the real file name of the installation file for the Service Pack.

Previous Topic  Next Topic
