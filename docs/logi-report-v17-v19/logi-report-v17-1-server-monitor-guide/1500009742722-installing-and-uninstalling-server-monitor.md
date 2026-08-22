---
title: "Installing and Uninstalling Server Monitor"
id: 1500009742722
section: "Logi Report v17.1 Server Monitor Guide"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009742722-Installing-and-Uninstalling-Server-Monitor
updated_at: 2021-07-24T00:49:44Z
---

# Installing and Uninstalling Server Monitor

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009769741--Server-Monitor-Guide-v17-1-Overview)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742782-Launching-and-Accessing-Server-Monitor)

# Installing and Uninstalling Server Monitor

This topic describes how you can install and uninstall Server Monitor on Windows.

Server Monitor is an application for the administrator which does not need to go on the same Server as the report system. So, you should install Server Monitor on a separate system or on systems for system administrators.

**To install Server Monitor on Windows:**

1. Download the Server Monitor installation file from the [download center](https://www.jinfonet.com/product/download-jreport/).
2. Execute the installation file.
3. The Installation Wizard displays the Welcome screen. Select **Next**.
4. In the **License Agreement** screen, read the license agreement carefully. Select **I accept the terms of the License Agreement**.
5. Select **Next**.
6. In the **Choose Install Folder** screen, select **Browse** to navigate to the absolute path where you want to install Server Monitor. You can also type or paste a path in the text box.
7. Select **Next**.
8. If the install folder that you want to use does not exist, the Installation Wizard displays a dialog box asking whether you want to create it. Select **Yes**.
9. In the **Configuration** screen, specify the administration port and the active host address.
10. Select **Next**.
11. In the **Select JDK** screen, select the JDK version you want to use with Server Monitor. The Installation Wizard collects and lists all the available JDK versions that you have installed on your machine, you can then select one of the JDK versions from the list.

    **![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)**The Installation Wizard does not list JRE versions on your machine. The lowest JDK version that Server Monitor supports is JDK 1.8.0.
12. Select **Next**.
13. In the **Add Class Path** screen, you must have a class path when using a JDBC driver or user-defined object. A class path is composed of a file path plus a zip file, jar file, or directory path. For example, `C:\jdk1.8.0_51\lib\tools.jar`.

    Select **Add** to add the selected class path to the class path list. Select **Delete** to delete the selected class path from the class path list. Then select **Next**.

    Or, you can skip this screen by directly selecting **Next**. You will have to manually edit the batch file or the command line that you use to start your Server Monitor to add class paths.
14. The **Installation Summary** screen displays the product name, location, and disk space information. Select **Install**. The Installation Wizard starts to install Server Monitor.
15. The **Installing** screen displays the installing process and status.
16. After installation, the **Read Me** screen displays. Read the information and select **Done** to close the Installation Wizard.

**To remove Server Monitor on Windows:**

* Run **uninstaller.exe** (uninstaller on Unix) in `<install_root>\_uninst`.
* Open **Settings** > **Apps** to remove it.

**![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)**The uninstaller removes all the files that the installer generated, while Server Monitor retains the files that the program created later. You need to remove the latter manually.

[Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009769741--Server-Monitor-Guide-v17-1-Overview)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009742782-Launching-and-Accessing-Server-Monitor)
