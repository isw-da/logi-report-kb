---
title: "Solving Installation Problems"
id: 1500010068681
section: "Setting Up the Report Designing Environment - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068681-Solving-Installation-Problems
updated_at: 2021-07-24T10:38:12Z
---

# Solving Installation Problems

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033322-Silent-Installation-) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068761-Upgrading-from-a-Previous-Version)

# Solving Installation Problems

If an error occurs during the installation, you can check the log information recorded to find out what the problem is. Where logs are generated depends on when the installation process failed:

* If the installation is canceled before you select the Install button in the installation wizard, logs are created on the desktop for Windows and in the userhome directory for Unix/Linux.
* If the installation is canceled after you select the Install button in the installation wizard, logs are created in the *logs* folder in the installation root directory.

In addition, on a Windows platform, you can specify the log destination that should use absolute path and log file name when launching the installation wizard by running the following command:

`jrdesigner-xxx-windows.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"`

or

`$ ./jrdesigner-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"`

Change jrdesigner-xxx-windows.exe or jrdesigner-xxx-linux.bin to the real file name of the installation file.

Feel free to send your questions to [support@jinfonet.com](mailto:support@jinfonet.com).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033322-Silent-Installation-) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068761-Upgrading-from-a-Previous-Version)
