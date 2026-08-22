---
title: "Installing and Running Designer on macOS"
id: 5735525675543
section: "Setting Up the Report Designing Environment - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735525675543-Installing-and-Running-Designer-on-macOS
updated_at: 2022-11-02T08:07:39Z
---

# Installing and Running Designer on macOS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735568230167-Installing-and-Running-Designer-on-Windows)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735532262679-Installing-and-Running-Designer-on-UNIX-Linux)

# Installing and Running Designer on macOS

This topic introduces how you can install, run, and uninstall Designer on macOS.

This topic contains the following sections:

* [Installing Designer on macOS](#Install)
* [Running Designer on macOS](#Run)
* [Uninstalling Designer on macOS](#Uninstall)

## Installing Designer on macOS

1. Download the Designer installation zip file for macOS from the Logi Analytics [product download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
2. Double-click the zip file to extract the installer file, jrpsetup.app.
3. Double-click **jrpsetup.app** to start installation.
4. Once you have loaded the Logi Report Designer Installation Wizard, you can then follow the [standard prompts](https://devnet.logianalytics.com/hc/en-us/articles/5735568230167-Installing-and-Running-Designer-on-Windows#Wizard) to install Designer.

## Running Designer on macOS

Double-click **Logi Report Designer.app** in `<install_root>/bin`, or run the script file **JReport.sh** in the same directory using the following command. You can modify this script file by adding additional classes before launching Designer.

`$ ./JReport.sh`

## Uninstalling Designer on macOS

Run the application file **uninstaller** in `<install_root>/_uninst`.

The uninstaller removes all files that the installer generates, while it retains any files that the program creates later. You should remove these files manually.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735568230167-Installing-and-Running-Designer-on-Windows)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735532262679-Installing-and-Running-Designer-on-UNIX-Linux)
