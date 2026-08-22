---
title: "Solving Installation Problems"
id: 1500009634321
section: "Setting Up the Report Designing Environment - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634321-Solving-Installation-Problems
updated_at: 2021-07-24T16:03:54Z
---

# Solving Installation Problems

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611262-Installing-Updates-Service-Packs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611302-Upgrading-Reports-from-v7-or-Prior-to-v17)

# Solving Installation Problems

If an error occurs during the installation, you can check the log information to find out what the problem is. This topic describes how you can access the logs to help you solve the problems you may encounter during the installation process.

Depending on when the installation process fails, the logs are generated in different destinations:

* If the installation is canceled before you select the Install button in the Installation Wizard, logs are created on the desktop for Windows and in the userhome directory for Unix/Linux.
* If the installation is canceled after you select the Install button in the Installation Wizard, logs are created in the logs folder in the installation root directory.

You can also specify the log destination that should use absolute path and log file name when launching the Installation Wizard by running the following command:

`designer-xxx-win64.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"`

or

`$ ./designer-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"`

Change designer-xxx-win64.exe or designer-xxx-linux.bin to the real file name of the installation file.

Feel free to send your questions to [support@logianalytics.com](mailto:support@logianalytics.com).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611262-Installing-Updates-Service-Packs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611302-Upgrading-Reports-from-v7-or-Prior-to-v17)
