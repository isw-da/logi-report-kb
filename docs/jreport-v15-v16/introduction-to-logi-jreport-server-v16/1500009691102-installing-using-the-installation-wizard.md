---
title: "Installing Using the Installation Wizard"
id: 1500009691102
section: "Introduction to Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691102-Installing-Using-the-Installation-Wizard
updated_at: 2021-11-03T06:57:00Z
---

# Installing Using the Installation Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009690982-Supported-Report-Databases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717261-Installing-Silently)

# Installing Using the Installation Wizard

This topic shows you how to install Logi JReport Server to different systems with the installation wizard.

Below is a list of the sections covered in this topic:

* [Installing on Windows](#Win)
* [Installing on Unix/Linux](#Unix)
* [Installing on Linux on IBM Z](#Linux)
* [Solving Installation Problems](#Solve)

## Installing on Windows

1. Download the Logi JReport Server installation file for Windows from the [Logi JReport download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
2. Double-click the installation file to run it, and select **Yes** in the prompt message dialog.
3. The Logi JReport Server Installation wizard appears. Select **Next** in the Welcome screen.
4. In the License Agreement screen, check the option **I accept the terms of the License Agreement** and select **Next**.
5. In the User ID and License Key screen, input the user ID and the license key separately. If you haven’t received the key please call us directly at +1 240-477-1000 or e-mail us at [sales@jinfonet.com](mailto:sales@jinfonet.com). Select **Next**.
6. In the Choose Installation Set screen, input the directory in the text box or select the **Browse** button to specify the directory to install Logi JReport Server and select the installation type from the following two:
   * **Typical Installation for Standalone Server**  
      Installs Logi JReport Server with the default configuration settings.
   * **Custom Installation for Standalone Server**  
      Installs Logi JReport Server in a standalone environment. If you choose this installation type, you can configure the server system environment in the installation wizard. The option is not available when the specified installation directory already contains a Logi JReport Server.

   ![Logi JReport Server Installation wizard - Choose Installation Set screen](https://devnet.logianalytics.com/hc/article_attachments/4412112571287/install_wzd_win_instlst.gif)
7. Select **Next**.

   If you select to install Logi JReport Server in a folder that already contains an Logi JReport Server, you will be prompted to choose whether to overwrite or upgrade the existing server. If you select Upgrade, the installer will replace the packages and create new batch/script files. Meanwhile a copy of the old batch/script files will be kept for your reference. You should use the batch/script files that come with the installer in order to make sure that all new packages are added to the class path and manually merge any changes you made into the new version. However, your configuration files and server runtime data of the existing copy will be kept, and you can choose to recover the previous version during the uninstallation of the newly installed Logi JReport Server.
8. In the System Environment screen (available only when the option Custom Installation for Standalone Server is selected in the Choose Installation Set screen), configure the following server system environment factors according to your requirements. System configuration can also be done in the Logi JReport Server console after the server is installed and started.
   * **[Service](https://devnet.logianalytics.com/hc/en-us/articles/1500009686842-Configuring-the-Server-Service)**
   * [**Cluster**](https://devnet.logianalytics.com/hc/en-us/articles/1500009686542-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster#During)
   * [**E-mail**](https://devnet.logianalytics.com/hc/en-us/articles/1500009686762-Configuring-Export-Settings#Email)
   * **[Cache](https://devnet.logianalytics.com/hc/en-us/articles/1500009712381-Configuring-Cache#Report)**
   * **[Performance](https://devnet.logianalytics.com/hc/en-us/articles/1500009686802-Tuning-Server-Performance#Preload)**
     + **Maximum Number of Concurrent Reports in the Queue**  
        Specifies the [maximum number of concurrent reports in the queue](https://devnet.logianalytics.com/hc/en-us/articles/1500009712261-Appendix-2-Properties-in-server-properties#performance.max.reports), which must be less than or equal to the number that the license permits.
   * **[Advanced](https://devnet.logianalytics.com/hc/en-us/articles/1500009712361-Configuring-Advanced-Server-Settings)**
   * **Demo**Specifies whether to install the Logi JReport demo reports and dashboards which will be available in the Public Reports folder in the server resource tree.
9. Select **Next**.
10. In the System Database screen (not available when you [upgrade](#Upgrade) Logi JReport Server), configure the system database as required.

    ![Logi JReport Server Installation wizard - System Database screen](https://devnet.logianalytics.com/hc/article_attachments/4412131441175/install_wzd_win_systmdtbs.gif)

    * **Trial Database**   
       Installs Logi JReport Server with the default trial database Derby which is provided for testing and evaluation purposes only and which should not be used in a production system. The port is configurable in case it is being used.
    * **Production Database**   
       Installs Logi JReport Server with a production database. In a production environment, you need to configure your own production DBMS. Set the correct database connection information. If the connection fails after selecting Next, a message will pop up and you can choose to reset the connection. Or if you choose to continue after the failure, you will need to configure the database later. For details, see [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009686662-Configuring-the-Server-Database).
11. Select **Next**.
12. In the Select JDK screen (not available when you [upgrade](#Upgrade) Logi JReport Server) choose the JDK to use with Logi JReport Server. You can select one from the Installed JDKs box or select the **Browse** button to locate a JDK.

    ![Logi JReport Server Installation wizard - Select JDK screen](https://devnet.logianalytics.com/hc/article_attachments/4412139536919/install_wzd_win_slctjdk.gif)
13. Select **Next**.
14. In the Add Class Path screen (not available when you [upgrade](#Upgrade) Logi JReport Server), select the **Add** button to add additional class paths as required. You can also choose to add them manually into the setenv.bat in  `<install_root>\bin` after installation.

    ![Logi JReport Server Installation wizard - Add Class Path screen](https://devnet.logianalytics.com/hc/article_attachments/4412131441431/install_wzd_win_adclspth.gif)
15. Select **Next**.
16. In the Lists screen (available only when you [upgrade](#Upgrade) Logi JReport Server), review the removed patches, modified configuration files and backup files if you want and select **Next**.
17. In the Installation Summary screen, review the installation information and select **Install** to install Logi JReport Server.
18. In the Installing screen, the installing process and status are shown.
19. After installation, the Read Me screen is displayed. Read the information and specify what to do next:
    * To start Logi JReport Server right away, keep the option **Start Logi JReport Server once installation is completed** (available only on Windows) selected.
    * To [run Logi JReport Server as a Windows service](https://devnet.logianalytics.com/hc/en-us/articles/1500009691302-Running-as-an-OS-Service#Win), select **Install Logi JReport Server as a Windows Service**.
    * To close the installation wizard, make sure that neither options are selected.Select **Done** to finish the installation.

    ![Logi JReport Server Installation wizard - Read Me screen](https://devnet.logianalytics.com/hc/article_attachments/4412112571543/install_wzd_win_rdm.gif)

## Installing on Unix/Linux

Logi JReport Server supports Solaris, HP-UX, AIX, and Linux. In the following process, an X server is running and Java 8 is available, otherwise ask your administrator for help. Installing and running Logi JReport Server requires that an X server has been configured.

1. Download the Logi JReport Server installation file for Unix/Linux from the [Logi JReport download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).

   If you need to transfer the installation file from your download machine to your Unix/Linux box, you should transfer it using FTP in binary mode.
2. Select the installation file to launch the installation wizard. Alternatively, you can open a console window by right-clicking on the blank area of the Desktop and selecting Open Terminal from the shortcut menu, and change the directory to the location of the file. Following are examples of the commands that can be used:

   `$ cd /opt/JReport/Server` (or your preferred installation path)

   To make the installation file executable, type the command:

   `$ chmod +x jrserver-xxx-linux.bin` (change jrserver-xxx-linux.bin to the actual name of the installation file)

   To run the installation file:

   `$ ./jrserver-xxx-linux.bin` (change jrserver-xxx-linux.bin to the actual name of the installation file)
3. Once the installation wizard has successfully loaded, you can follow the [standard prompts](#Win) to install Logi JReport Server.

## Installing on Linux on IBM Z

Logi JReport Server supports Linux on IBM System z. In the following process, an X server is running and a JDK specially used for IBM is available, otherwise ask your administrator for help. Installing and running Logi JReport Server requires that an X server has been configured.

1. Download the Logi JReport Server installation file for Linux on IBM Z from the [Logi JReport download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).

   If you need to transfer the installation file from your download machine to your Linux on IBM Z box, you should transfer it using FTP in binary mode.
2. Open a console window by right-clicking on the blank area of the Desktop and selecting Open Terminal from the shortcut menu. Then:
   1. Change the directory to the location of the file. You can type the following command in the console window: `cd /opt/JReport/Server` (input the absolute install location). Then press the **Enter** key on the keyboard.
   2. Type the following command to make the installation file executable: `chmod +x jrserver-xxx-linux.bin` (change jrserver-xxx-linux.bin to the actual name of the installation file). Then press the **Enter** key on the keyboard.
   3. Type the following command to run the installation file: `./jrserver-xxx-linux.bin` (change jrserver-xxx-linux.bin to the actual name of the installation file). Then press the **Enter** key on the keyboard.

   See the following example.

   ![Install on Linux](https://devnet.logianalytics.com/hc/article_attachments/4412112571799/install_wzd_linux.gif)
3. The Logi JReport Server Installation wizard appears. Follow the [standard prompts](#Win) to install Logi JReport Server.

## Solving Installation Problems

If errors occur during the installation, you can check the log information recorded to find out what the problem is. Where logs are generated depends on when the installation process get stuck:

* If the installation is cancelled before you select the Install button in the installation wizard, logs are created on the desktop for Windows and in the userhome directory for Unix/Linux.
* If the installation is cancelled after you select the Install button in the installation wizard, logs are created in the logs folder in the installation root directory.

Besides, on a Windows platform you can specify the log destination that should use absolute path and log file name when launching the installation wizard by running the following command:

`jrserver-xxx-windows.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"`

or

`$ ./jrserver-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"`

Change jrserver-xxx-windows.exe or jrserver-xxx-linux.bin to the real file name of the installation file.

Feel free to send your questions to [support@jinfonet.com](mailto:support@jinfonet.com).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009690982-Supported-Report-Databases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717261-Installing-Silently)
