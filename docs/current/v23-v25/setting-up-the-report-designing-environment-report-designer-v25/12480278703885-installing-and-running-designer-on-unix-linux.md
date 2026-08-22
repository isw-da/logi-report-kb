---
title: "Installing and Running Designer on UNIX/Linux"
id: 12480278703885
section: "Setting Up the Report Designing Environment - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480278703885-Installing-and-Running-Designer-on-UNIX-Linux
updated_at: 2026-02-25T23:48:23Z
source_host: docs-report.zendesk.com
---
# Installing and Running Designer on UNIX/Linux

This topic introduces how you can install, run, and uninstall Designer on UNIX/Linux.

This topic contains the following sections:

- Installing Designer on UNIX/Linux

- Running Designer on UNIX/Linux

- Uninstalling Designer on UNIX/Linux

## 
Installing Designer on UNIX/Linux

You can install Designer on a UNIX or Linux system either by using the Installation Wizard or in  silent mode. Silent installation frees you from participation in the installation process.

To install Designer on UNIX/Linux using the Installation Wizard

- Download the  Designer installation file for UNIX/Linux from the Logi Analytics product download center.

- Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window and run the following commands. To change the directory to the location of the installation file:

$ cd thepath

To make the installation file executable:

$ chmod +x designer-xxx-linux.bin (change designer-xxx-linux.bin to the real file name of the installation file)

To run the installation file:

$ ./designer-xxx-linux.bin (change designer-xxx-linux.bin to the real file name of the installation file)

- Once you have loaded the Report Designer Installation Wizard , you can then follow the standard prompts to install Designer.

To install Designer on UNIX/Linux silently

- Download the  Designer installation file for UNIX/Linux from the Logi Analytics product download center.

- Get the file DesignerInstall.properties for silent Designer installation from Logi Analytics Support. 

- Put DesignerInstall.properties to the directory where you save the Designer installation file.

- Edit DesignerInstall.properties to suit your requirements. 

- Open a console window and change the directory to the location of the installation file.$ cd thepath

- Run the following command to make the installation file executable: $ chmod +x designer-xxx-linux.bin	(Change designer-xxx-linux.bin to the real file name of the installation file.)

- Run the following command to install  Designer in the designated path: $ ./designer-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f DesignerInstall.properties (Change designer-xxx-linux.bin to the real file name of the installation file.)

 When installing Designer silently, make sure you do not use overwrite installation, instead, install it to a new directory.

## 
Running Designer on UNIX/Linux

Run the script file JReport.sh in <install_root>/bin. You can modify this script file by adding additional classes before launching Designer.

$ ./JReport.sh

## 
Uninstalling Designer on UNIX/Linux

Execute uninstaller.sh in <install_root>/_uninst.

Alternatively, you can open a console window, change the directory to the location of the uninstaller.sh file and run the file.

To change the directory:

$ cd thepath

Run the uninstaller file:

$ ./uninstaller
