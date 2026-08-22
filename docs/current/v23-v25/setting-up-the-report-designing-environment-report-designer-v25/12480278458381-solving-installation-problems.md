---
title: "Solving Installation Problems"
id: 12480278458381
section: "Setting Up the Report Designing Environment - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480278458381-Solving-Installation-Problems
updated_at: 2026-02-25T23:48:24Z
source_host: docs-report.zendesk.com
---
# Solving Installation Problems

If an error occurs during the installation, you can check the log information to find out what the problem is. This topic describes how you can access the logs to help you solve the problems you may encounter during the installation process.

Depending on when the installation process fails, Designer generates the logs in different destinations.

- If you cancel the installation  before you select the Install button in the Installation Wizard, the installer creates the logs on the desktop for Windows and in the userhome directory for UNIX/Linux.

- If you cancel the installation after you select the Install button in the Installation Wizard, the installer creates logs  in the logs folder in the installation root directory.

You can also specify the log destination that should use absolute path and log file name when launching the Installation Wizard by running the following command:

designer-xxx-win64.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"

or

$ ./designer-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"

Change designer-xxx-win64.exe or designer-xxx-linux.bin to the real file name of the installation file.

If you need more information, contact Customer Service.
