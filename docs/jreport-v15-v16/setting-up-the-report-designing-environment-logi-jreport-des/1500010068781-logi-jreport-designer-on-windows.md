---
title: "Logi JReport Designer on Windows"
id: 1500010068781
section: "Setting Up the Report Designing Environment - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068781-Logi-JReport-Designer-on-Windows
updated_at: 2021-07-24T10:38:10Z
---

# Logi JReport Designer on Windows

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068621-Supported-Report-Databases) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068661-Logi-JReport-Designer-on-macOS)

# Logi JReport Designer on Windows

This topic introduces how to install, run, and uninstall Logi JReport Designer on Windows.

Below is a list of the sections covered in this topic:

* [Installing Logi JReport Designer on Windows](#Install)
* [Running Logi JReport Designer on Windows](#Run)
* [Uninstalling Logi JReport Designer on Windows](#Uninstall)

## Installing Logi JReport Designer on Windows

1. Download the Logi JReport Designer installation file for Windows from the [Logi JReport download center](https://www.jinfonet.com/product/download-Logi%20JReport/).
2. Double-click the installation file to run it, and select **Yes** in the prompt message dialog.
3. The Logi JReport Designer Installation wizard appears. Select **Next** in the Welcome screen.
4. In the License Agreement screen, check the option **I accept the terms of the License Agreement** and select **Next**.
5. In the User ID and License Key screen, input the user ID and the license key separately. If you haven’t received the key please call us directly at +1 240-477-1000 or e-mail us at [sales@jinfonet.com](mailto:sales@jinfonet.com). Then select **Next**.

   ![Logi JReport Designer Installation wizard - User ID and License Key screen](https://devnet.logianalytics.com/hc/article_attachments/4404901159575/install_win_id.gif)
6. In the Choose Installation Set screen, specify the installation directory. You can input the directory in the text box directly or select the **Browse** button to specify the directory. Select **Next**.

   If you install Logi JReport Designer in a folder that already contains an Logi JReport Designer, the installer will replace the packages and create new batch/script files. Meanwhile, a copy of the old batch/script files will be kept for your reference. You should use the batch/script files that come with the installer in order to make sure that all new packages are added to the class path and manually merge any changes you made into the new version.

   ![Logi JReport Designer Installation wizard - Choose Installation Set screen](https://devnet.logianalytics.com/hc/article_attachments/4404909144599/install_win_dir.gif)
7. In the Select JDK screen choose the JDK to use with Logi JReport Designer. You can select one from the Installed JDKs box or select the **Browse** button to locate a JDK. Select **Next**.

   ![Logi JReport Designer Installation wizard - Select JDK screen](https://devnet.logianalytics.com/hc/article_attachments/4404901159831/install_win_jdk.gif)
8. In the Backup Files List screen (available only when you [upgrade](#Upgrade) Logi JReport Designer), review the backup files. Select **Next**.
9. In the Add Class Path screen, select the **Add** button to add additional class paths as required. You can also choose to add them manually into the setenv.bat in  `<install_root>\bin` after installation. Select **Next**.

   ![Logi JReport Designer Installation wizard - Add Class Path screen](https://devnet.logianalytics.com/hc/article_attachments/4404909144855/install_win_clspth.gif)
10. In the Installation Summary screen, review the installation information and select **Install** to install Logi JReport Designer.
11. In the Installing screen, the installing process and status are shown.
12. After installation, the Read Me screen displays. Read the information, specify whether to start Logi JReport Designer once the installation is completed, and select **Done** to close the Installation wizard.

## Running Logi JReport Designer on Windows

There are the following ways to run Logi JReport Designer on Windows:

* Double-click the shortcut for JReport Designer on your desktop.
* Select **JReport Designer** in the JReport folder on the Start menu.
* Run the JReport.bat/JReport.sh file located in `<install_root>\bin`.
* Run the startup batch file from a MS-DOS command prompt. For example, assume that Logi JReport Designer has been installed in `C:\JReport\Designer`, you can type the following commands:

  `C:\>cd JReport\Designer\bin  
  C:\JReport\Designer\bin>JReport.bat`

Information about whether the startup is successful or failed will be output to the file JReport.out.log located in `<install_root>\logs`. After Logi JReport Designer is restarted, JReport.out.log will be recreated and the contents reset.

## Uninstalling Logi JReport Designer on Windows

You can use either of the following ways to uninstall Logi JReport Designer on Windows:

* Open **Control Panel** > **Programs and Features** to remove it.
* Run uninstaller.exe in `<install_root>\_uninst`.

**Note:** The uninstaller removes all files that were generated by the installer, while any files that were created later by the program are retained. These files should be removed manually.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068621-Supported-Report-Databases) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068661-Logi-JReport-Designer-on-macOS)
