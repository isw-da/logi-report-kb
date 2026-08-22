---
title: "Installing and Running Designer on UNIX/Linux"
id: 5735532262679
section: "Setting Up the Report Designing Environment - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735532262679-Installing-and-Running-Designer-on-UNIX-Linux
updated_at: 2022-11-02T08:07:40Z
---

# Installing and Running Designer on UNIX/Linux

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525675543-Installing-and-Running-Designer-on-macOS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516356887-Installing-Service-Packs)

# Installing and Running Designer on UNIX/Linux

This topic introduces how you can install, run, and uninstall Designer on UNIX/Linux.

This topic contains the following sections:

* [Installing Designer on UNIX/Linux](#Install)
* [Running Designer on UNIX/Linux](#Run)
* [Uninstalling Designer on UNIX/Linux](#Uninstall)

## Installing Designer on UNIX/Linux

You can install Designer on a UNIX or Linux system either by [using the Installation Wizard](#Wizard) or [in silent mode](#Silent). Silent installation frees you from participation in the installation process.

**To install Designer on UNIX/Linux using the Installation Wizard**

1. Download the Designer installation file for UNIX/Linux from the Logi Analytics [product download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
2. Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window and run the following commands.

   To change the directory to the location of the installation file:

   `$ cd thepath`

   To make the installation file executable:

   `$ chmod +x designer-xxx-linux.bin` (change designer-xxx-linux.bin to the real file name of the installation file)

   To run the installation file:

   `$ ./designer-xxx-linux.bin` (change designer-xxx-linux.bin to the real file name of the installation file)
3. Once you have loaded the Logi Report Designer Installation Wizard , you can then follow the [standard prompts](https://devnet.logianalytics.com/hc/en-us/articles/5735568230167-Installing-and-Running-Designer-on-Windows#Wizard) to install Designer.

**To install Designer on UNIX/Linux silently**

1. Download the Designer installation file for UNIX/Linux from the Logi Analytics [product download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
2. Get the file **DesignerInstall.properties** for silent Designer installation from Logi Analytics Support.
3. Put DesignerInstall.properties to the directory where you save the Designer installation file.
4. Edit DesignerInstall.properties to suit your requirements.
5. Open a console window and change the directory to the location of the installation file.

   `$ cd thepath`
6. Run the following command to make the installation file executable:

   `$ chmod +x designer-xxx-linux.bin` (Change **designer-xxx-linux.bin** to the real file name of the installation file.)
7. Run the following command to install Designer in the designated path:

   `$ ./designer-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f DesignerInstall.properties` (Change **designer-xxx-linux.bin** to the real file name of the installation file.)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When installing Designer silently, make sure you do not use overwrite installation, instead, install it to a new directory.

## Running Designer on UNIX/Linux

Run the script file **JReport.sh** in `<install_root>/bin`. You can modify this script file by adding additional classes before launching Designer.

`$ ./JReport.sh`

## Uninstalling Designer on UNIX/Linux

Execute **uninstaller.sh** in `<install_root>/_uninst`.

Alternatively, you can open a console window, change the directory to the location of the uninstaller.sh file and run the file.

To change the directory:

`$ cd thepath`

Run the uninstaller file:

`$ ./uninstaller`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525675543-Installing-and-Running-Designer-on-macOS)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735516356887-Installing-Service-Packs)
