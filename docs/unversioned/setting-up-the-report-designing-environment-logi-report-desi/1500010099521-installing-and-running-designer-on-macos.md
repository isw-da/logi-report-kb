---
title: "Installing and Running Designer on macOS"
id: 1500010099521
section: "Setting Up the Report Designing Environment - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099521-Installing-and-Running-Designer-on-macOS
updated_at: 2021-08-17T20:39:49Z
---

# Installing and Running Designer on macOS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061142-Installing-and-Running-Designer-on-Windows)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061122-Installing-and-Running-Designer-on-Unix-Linux)

# Installing and Running Designer on macOS

This topic introduces how you can install, run, and uninstall Designer on macOS.

This topic contains the following sections:

* [Installing Designer on macOS](#Install)
* [Running Designer on macOS](#Run)
* [Uninstalling Designer on macOS](#Uninstall)

## Installing Designer on macOS

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4405660704151/noteicon.jpg) You should be using JDK 8 or 9 for the installation.

1. Download the Designer installation zip file for macOS from the [Logi Report download center](https://www.jinfonet.com/product/download-jreport/).
2. Double-click the zip file to extract the installer file, jrpsetup.app.
3. Open **Terminal** and navigate to the folder where you have extracted jrpsetup.app.
4. Next, either:  
   Execute this command to start the installation: `open -a jrpsetup.app`  
   Or, execute this command: `xattr -cr jrpsetup.app` and then double-click **jrpsetup.app** to start installation.
5. Once you have loaded the Logi Report Designer Installation Wizard, you can then follow the [standard prompts](https://devnet.logianalytics.com/hc/en-us/articles/1500010061142-Installing-and-Running-Designer-on-Windows#Wizard) to install Designer.

## Running Designer on macOS

Double-click **Logi Report Designer.app** in `<install_root>/bin`, or run the script file **JReport.sh** in the same directory using the following command. You can modify this script file by adding additional classes before launching Designer.

`$ ./JReport.sh`

## Uninstalling Designer on macOS

Run the application file **uninstaller** in `<install_root>/_uninst`.

The uninstaller removes all files that the installer generates, while it retains any files that the program creates later. You should remove these files manually.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061142-Installing-and-Running-Designer-on-Windows)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061122-Installing-and-Running-Designer-on-Unix-Linux)
