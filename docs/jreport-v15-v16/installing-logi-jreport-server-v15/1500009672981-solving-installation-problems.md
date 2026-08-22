---
title: "Solving Installation Problems"
id: 1500009672981
section: "Installing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009672981-Solving-Installation-Problems
updated_at: 2022-02-17T11:53:43Z
---

# Solving Installation Problems

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648322-Upgrading-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648242-Logi-JReport-Server-Guide-v15-Server-Reporthome-Directory-Overview)

# Solving Installation Problems

If errors occur during the installation, you can check the log information recorded to find out what the problem is. Where logs are generated depends on when the installation process get stuck:

* If the installation is cancelled before you select the Install button on the installation wizard, logs are created on the desktop for Windows and in the userhome directory for Unix/Linux.
* If the installation is cancelled after you select the Install button on the installation wizard, logs are created in the logs folder in the installation root directory.

Besides, on a Windows platform, you can choose to specify the log destination that should use absolute path and log file name when launching the installation wizard by running the following command:

`jrserver-xxx-windows.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"`

or

`$ ./jrserver-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"`

Change *jrserver-xxx-windows.exe* or *jrserver-xxx-linux.bin* to the real file name of the installation file.

Feel free to send your questions to [support@jinfonet.com](mailto:support@jinfonet.com).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## An Issue on Windows Vista

**Problem**

When running Logi JReport Server's installer on Windows Vista, the installer cannot find the installed JDKs.

**Reason**

By default Vista's security settings are stricter than Windows 2000, XP, and 2003. The children processes do not inherit the execution right from their parent process.

**Solution**

Make the compatibility property of the installer file (.exe) available:

1. Right-select the installer file, and select **Properties** from the shortcut menu.
2. In the Compatibility mode panel of the Compatibility tab, check the **Run this program in compatibility mode for** option, and then select **Windows 2000** from the drop-down list.
3. Select **OK**.
4. Run the installer.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648322-Upgrading-Logi-JReport-Server-Guide-v15-Server)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648242-Logi-JReport-Server-Guide-v15-Server-Reporthome-Directory-Overview)
