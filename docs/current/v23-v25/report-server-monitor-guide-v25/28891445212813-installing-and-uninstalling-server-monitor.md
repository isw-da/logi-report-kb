---
title: "Installing and Uninstalling Server Monitor"
id: 28891445212813
section: "Report Server Monitor Guide v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891445212813-Installing-and-Uninstalling-Server-Monitor
updated_at: 2026-02-26T02:10:53Z
source_host: docs-report.zendesk.com
---
# 
Installing and Uninstalling Server Monitor

This topic describes how you can install and uninstall Server Monitor on Windows.

Server Monitor is an application for the administrator which does not need to go on the same Server as the report system. So, you should install Server Monitor on a separate system or on systems for system administrators.

To install Server Monitor on Windows:

- Download the Server Monitor installation file from the download center.

- Run the installation file.

- The Installation Wizard displays the Welcome screen. Select Next.

- In the License Agreement screen, read the license agreement carefully. Select I accept the terms of the License Agreement. 

- Select Next. 

- In the Choose Install Folder screen, select Browse to navigate to the absolute path where you want to install Server Monitor. You can also type or paste a path in the text box.

- Select Next. 

- If the install folder that you want to use does not exist, the Installation Wizard displays a dialog box asking whether you want to create it. Select Yes.

- In the Configuration screen, specify the administration port and the active host address. 

- Select Next.

- In the Select JDK screen, select the JDK version you want to use with Server Monitor. The Installation Wizard collects and lists all the available JDK versions that you have installed on your machine, you can then select one of the JDK versions from the list. The Installation Wizard does not list JRE versions on your machine. The lowest JDK version that Server Monitor supports is JDK 1.8.0.

- Select Next.

- In the Add Class Path screen, you must have a class path when using a JDBC driver or user-defined object. A class path is composed of a file path plus a zip file, jar file, or directory path. For example, C:\jdk1.8.0_51\lib\tools.jar.
    Select Add to add the selected class path to the class path list. Select Delete to delete the selected class path from the class path list. Then select Next. 

Or, you can skip this screen by directly selecting Next. You will have to manually edit the batch file or the command line that you use to start your Server Monitor to add class paths.

- The Installation Summary screen displays the product name, location, and disk space information. Select Install. The Installation Wizard starts to install Server Monitor.

- The Installing screen displays the installing process and status.

- After installation, the Read Me screen displays. Read the information and select Done to close the Installation Wizard.

 To remove Server Monitor on Windows:

- Run uninstaller.exe (uninstaller on UNIX) in <install_root>\_uninst.

- Open Settings > Apps to remove it.

The uninstaller removes all the files that the installer generated, while Server Monitor retains the files that the program created later. You need to remove the latter manually.
