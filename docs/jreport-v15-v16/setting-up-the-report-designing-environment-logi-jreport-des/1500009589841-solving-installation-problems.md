---
title: "Solving Installation Problems"
id: 1500009589841
section: "Setting Up the Report Designing Environment - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589841-Solving-Installation-Problems
updated_at: 2021-07-24T05:54:33Z
---

# Solving Installation Problems

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589821-Silent-Installation)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568462-Upgrading-from-a-Previous-Version)

# Solving Installation Problems

If an error occurs during the installation, you can check the log information recorded to find out what the problem is. Where logs are generated depends on when the installation process failed:

* If the installation is cancelled before you select the Install button on the installation wizard, logs are created on the desktop for Windows and in the userhome directory for Unix/Linux.
* If the installation is cancelled after you select the Install button on the installation wizard, logs are created in the logs folder in the installation root directory.

In addition, on a Windows platform, you can choose to specify the log destination that should use absolute path and log file name when launching the installation wizard by running the following command:

`jrdesigner-xxx-windows.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"`

or

`$ ./jrdesigner-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"`

Change jrdesigner-xxx-windows.exe or jrdesigner-xxx-linux.bin to the real file name of the installation file.

Feel free to send your questions to [support@jinfonet.com](mailto:support@jinfonet.com).

## An Issue on Windows Vista

**Problem**

When running Logi JReport Designer's installer on Windows Vista, the installer cannot find the browser and the installed JDKs, or when running installers of other Logi JReport products, the installer cannot find the installed JDKs. These browsers are supported in Logi JReport Designer's installer: Internet Explorer, Firefox, and Google Chrome.

**Reason**

By default Vista's security settings are stricter than Windows 2000, XP, and 2003. The children processes do not inherit the execution right from their parent process.

**Solution**

Make the compatibility property of the installer file (.exe) available:

1. Right-click the installer file, and select **Properties** from the shortcut menu.
2. In the Compatibility mode panel of the Compatibility tab, check the **Run this program in compatibility mode for** option, and then select **Windows 2000** from the drop-down list.
3. Select **OK**.
4. Run the installer.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589821-Silent-Installation)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568462-Upgrading-from-a-Previous-Version)
