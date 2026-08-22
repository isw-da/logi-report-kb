---
title: "Solving Installation Problems"
id: 1500010099541
section: "Setting Up the Report Designing Environment - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099541-Solving-Installation-Problems
updated_at: 2021-07-23T19:16:15Z
---

# Solving Installation Problems

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099561-Installing-Updates-Service-Packs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099501-Using-the-Designer-Launch-Files)

# Solving Installation Problems

If an error occurs during the installation, you can check the log information to find out what the problem is. This topic describes how you can access the logs to help you solve the problems you may encounter during the installation process.

Depending on when the installation process fails, Designer generates the logs in different destinations:

* If you cancel the installation before you select the Install button in the Installation Wizard, the installer creates the logs on the desktop for Windows and in the userhome directory for Unix/Linux.
* If you cancel the installation after you select the Install button in the Installation Wizard, the installer creates logs in the logs folder in the installation root directory.

You can also specify the log destination that should use absolute path and log file name when launching the Installation Wizard by running the following command:

`designer-xxx-win64.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"`

or

`$ ./designer-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"`

Change designer-xxx-win64.exe or designer-xxx-linux.bin to the real file name of the installation file.

Feel free to send your questions to [support@logianalytics.com](mailto:support@logianalytics.com).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099561-Installing-Updates-Service-Packs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099501-Using-the-Designer-Launch-Files)
