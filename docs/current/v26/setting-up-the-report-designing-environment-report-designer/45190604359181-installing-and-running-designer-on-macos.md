---
title: "Installing and Running Designer on macOS"
id: 45190604359181
section: "Setting Up the Report Designing Environment - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190604359181-Installing-and-Running-Designer-on-macOS
updated_at: 2026-04-30T15:15:15Z
source_host: logi-report-v26.insightsoftware.com
---
# Installing and Running Designer on macOS

This topic introduces how you can install, run, and uninstall Designer on  macOS.

This topic contains the following sections:

- Installing  Designer on macOS

- Running  Designer on macOS

- Uninstalling  Designer on macOS

## 
Installing Designer on macOS

- Download the  Designer installation zip file for macOS from the Logi Analytics product download center.

- Double-click the zip file to extract the installer file, jrpsetup.app.

- Double-click jrpsetup.app to start installation.

- Once you have loaded the Report Designer Installation Wizard, you can then follow the standard prompts to install Designer. 

 

## 
Running Designer on macOS

Double-click Logi Report Designer.app in <install_root>/bin, or run the script file JReport.sh in the same directory using the following command. You can modify this script file by adding additional classes before launching Designer.

$ ./JReport.sh

 

## 
Uninstalling Designer on macOS

Run the application file uninstaller in <install_root>/_uninst. 

The uninstaller removes all files that the installer generates, while it retains any files that the program creates later. You should remove these files  manually.
