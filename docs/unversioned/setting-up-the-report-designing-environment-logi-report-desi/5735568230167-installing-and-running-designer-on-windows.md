---
title: "Installing and Running Designer on Windows"
id: 5735568230167
section: "Setting Up the Report Designing Environment - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735568230167-Installing-and-Running-Designer-on-Windows
updated_at: 2022-11-02T08:07:42Z
---

# Installing and Running Designer on Windows

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525627159-Logi-Report-Licenses)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525675543-Installing-and-Running-Designer-on-macOS)

# Installing and Running Designer on Windows

This topic introduces how you can install, run, and uninstall Designer on Windows.

This topic contains the following sections:

* [Installing Designer on Windows](#Install)
* [Running Designer on Windows](#Run)
* [Uninstalling Designer on Windows](#Uninstall)

## Installing Designer on Windows

You can install Designer on Windows either by [using the Installation Wizard](#Wizard) or [in silent mode](#Silent). Silent installation frees you from participation in the installation process. It can be useful if you do installation in an automated fashion across a network, or work in an environment where the Windows desktop is unavailable for security reasons.

**To install Designer on Windows using the Installation Wizard**

1. Download the Designer installation file for Windows from the Logi Analytics [product download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
2. Double-click the installation file to run it, and select **Yes** in the prompt message dialog box.
3. The Logi Report Designer Installation Wizard appears. Select **Next** in the Welcome screen.
4. In the **License Agreement** screen, select the option **I accept the terms of the License Agreement** and select **Next**.
5. In the **User ID and License Key** screen, specify the user ID and the license key separately, then select **Next**. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When the license is machine specific, you need to make sure the name of the computer on which you are installing this Designer matches that defined in the license file.
6. In the **Choose Installation Set** screen, specify the installation directory. You can type the directory in the text box or select **Browse** to specify the directory. Select **Next**.

   ![Logi Report Designer Installation wizard - Choose Installation Set screen](https://devnet.logianalytics.com/hc/article_attachments/9898476612119/install_win_dir.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) If you install Designer in a folder that already contains a Designer, the installer replaces the packages and creates new batch/script files. Meanwhile, the installer keeps a copy of the old batch/script files for your reference. You should use the batch/script files that come with the installer in order to make sure that all new packages are added to the class path and manually merge any changes you made into the new version.
7. In the **Select JDK** screen, choose the JDK to use with Designer. You can select one from the **Installed JDKs** box or select **Browse** to locate a JDK. Select **Next**.

   ![Logi Report Designer Installation wizard - Select JDK screen](https://devnet.logianalytics.com/hc/article_attachments/9898476617367/install_win_jdk.gif)
8. In the **Backup Files List** screen (available only when you [upgrade](#Upgrade) Designer), review the backup files. Select **Next**.
9. In the **Add Class Path** screen, you can add additional class paths. You can also choose to add the class paths manually into **setenv.bat** in  `<install_root>\bin` after installation. Select **Next**.
10. In the **Installation Summary** screen, review the installation information and select **Install** to install Designer.
11. The **Installing** screen shows the installing process and status.
12. After installation, the **Read Me screen** displays. Read the information, specify whether to start Designer once the installation is completed, and select **Done** to close the Installation Wizard.

**To install Designer on Windows silently**

1. Download the Designer installation file for Windows from the Logi Analytics [product download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
2. Get the file **DesignerInstall.properties** for silent Designer installation from Logi Analytics Support.
3. Put DesignerInstall.properties to the directory where you save the Designer installation file.
4. Edit DesignerInstall.properties to suit your requirements.
5. Open a console window and change the directory to the location of the installation file.

   `$ cd thepath`
6. Run the following command to install Designer in the designated path:

   `$ designer-xxx-win64.exe -i silent -f DesignerInstall.properties`

   Change **designer-xxx-win64.exe** to the real file name of the installation file.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) When installing Designer silently, make sure you do not use overwrite installation, instead, install it to a new directory.

## Running Designer on Windows

To run Designer on Windows, you can use the following methods:

* Double-click the shortcut for Designer on your desktop.
* Select **Logi Report Designer** in the Logi Report folder on the Start menu.
* Run **JReport.bat**/**JReport.sh** located in `<install_root>\bin`.
* Run the startup batch file from a Command Prompt window. For example, assume that you have installed Designer in `C:\LogiReport\Designer`, you can type the following commands:

  `C:\>cd LogiReport\Designer\bin  
  C:\LogiReport\Designer\bin>JReport.bat`

Designer outputs the information about whether the startup is successful or failed to the file **LogiReport.out.log** located in `<install_root>\logs`. After you start Designer, Designer recreates and resets the content in the file.

## Uninstalling Designer on Windows

You can use either of the following methods to uninstall Designer on Windows:

* Open **Control Panel**, and then **Programs and Features** to remove it.
* Run **uninstaller.exe** in `<install_root>\_uninst`.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) The uninstaller removes all files that the installer generates, while it retains any files that the program creates later. You should remove these files manually.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735525627159-Logi-Report-Licenses)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735525675543-Installing-and-Running-Designer-on-macOS)
