---
title: "Installing and Running Designer on Unix/Linux"
id: 1500010061122
section: "Setting Up the Report Designing Environment - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061122-Installing-and-Running-Designer-on-Unix-Linux
updated_at: 2021-07-23T19:16:15Z
---

# Installing and Running Designer on Unix/Linux

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099521-Installing-and-Running-Designer-on-macOS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099561-Installing-Updates-Service-Packs)

# Installing and Running Designer on Unix/Linux

This topic introduces how you can install, run, and uninstall Designer on Unix/Linux.

This topic contains the following sections:

* [Installing Designer on Unix/Linux](#Install)
* [Running Designer on Unix/Linux](#Run)
* [Uninstalling Designer on Unix/Linux](#Uninstall)

## Installing Designer on Unix/Linux

You can install Designer on a Unix or Linux system either by [using the Installation Wizard](#Wizard) or [in the silent way](#Silent). Silent installation frees you from participation in the installation process.

To install Designer on Unix/Linux using the Installation Wizard:

1. Download the Designer installation file for Unix/Linux from the [Logi Report download center](https://www.jinfonet.com/product/download-jreport/).
2. Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window and run the following commands:

   To change the directory to the location of the installation file:

   `$ cd thepath`

   To make the installation file executable:

   `$ chmod +x designer-xxx-linux.bin` (change designer-xxx-linux.bin to the real file name of the installation file)

   To run the installation file:

   `$ ./designer-xxx-linux.bin` (change designer-xxx-linux.bin to the real file name of the installation file)
3. Once you have loaded the Logi Report Designer Installation Wizard , you can then follow the [standard prompts](https://devnet.logianalytics.com/hc/en-us/articles/1500010061142-Installing-and-Running-Designer-on-Windows#Wizard) to install Designer.

To install Designer on Unix/Linux silently:

1. Download the Designer installation file for Unix/Linux from the [Logi Report download center](https://www.jinfonet.com/product/download-jreport/).
2. Get the file **DesignerInstall.properties** used for silent Designer installation from Logi Analytics Support at [support@logianalytics.com.](mailto:support@logianalytics.com)
3. Put DesignerInstall.properties to the directory where you save the Designer installation file.
4. Edit DesignerInstall.properties to suit your requirements.
5. Open a console window and change the directory to the location of the installation file.

   `$ cd thepath`
6. Run the following command to make the installation file executable:

   `$ chmod +x designer-xxx-linux.bin` (Change designer-xxx-linux.bin to the real file name of the installation file.)
7. Run the following command to install Designer in the designated path:

   `$ ./designer-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f DesignerInstall.properties` (Change designer-xxx-linux.bin to the real file name of the installation file.)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When installing Designer silently, make sure you do not use overwrite installation, instead, install it to a new directory.

## Running Designer on Unix/Linux

Run the script file **JReport.sh** in `<install_root>/bin`. You can modify this script file by adding additional classes before launching Designer.

`$ ./JReport.sh`

## Uninstalling Designer on Unix/Linux

Execute **uninstaller.sh** in `<install_root>/_uninst`.

Alternatively, you can open a console window, change the directory to the location of the uninstaller.sh file and run the file.

To change the directory:

`$ cd thepath`

Run the uninstaller file:

`$ ./uninstaller`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099521-Installing-and-Running-Designer-on-macOS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099561-Installing-Updates-Service-Packs)
