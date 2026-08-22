---
title: "Installing Server Using the Installation Wizard"
id: 4405683902487
section: "Introduction to Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683902487-Installing-Server-Using-the-Installation-Wizard
updated_at: 2022-07-28T19:51:33Z
---

# Installing Server Using the Installation Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683897495-Supported-Report-Databases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690619415-Installing-Server-Silently)

# Installing Server Using the Installation Wizard

This topic describes how you can install Server on Windows, UNIX, Linux, and macOS using the Installation Wizard and solve problems during installation.

This topic contains the following sections:

* [Installing Server on Windows](#Win)
* [Installing Server on UNIX/Linux](#UNIX)
* [Installing Server on Linux on IBM Z](#Linux)
* [Installing Server on macOS](#Mac)
* [Solving Installation Problems](#Solve)

## Installing Server on Windows

1. Download the Server installation file for Windows from the [Logi Report download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
2. Double-click the installation file to run it.
3. Server displays a message dialog box. Select **Yes**.
4. Server displays the Installation Wizard. Select **Next** in the Welcome screen.
5. In the License Agreement screen, select **I accept the terms of the License Agreement**.
6. Select **Next**.
7. In the User ID and License Key screen, type the user ID and the license key separately. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

   If the license is machine specific, make sure the name of the computer on which you are installing Server matches that defined in the license file.
8. Select **Next**.
9. In the Choose Installation Set screen, type the directory in the text box or select **Browse** to specify the directory where you want to install Server.
10. Select an installation type:
    * **Typical Installation for Standalone Server**  
       Select to install Server with the default configuration settings.
    * **Custom Installation for Standalone Server**  
       Select if you want to configure the server system environment in the Installation Wizard. The option is not available when the specified installation directory already contains a Server.

    ![Logi Report Server Installation wizard - Choose Installation Set screen](https://devnet.logianalytics.com/hc/article_attachments/4420447200919/install_wzd_win_instlst.gif)
11. Select **Next**.

    If you select to install Server in a folder that already contains a Server, Server asks you to choose whether to overwrite or upgrade the existing server. If you select **Upgrade**, the installer replaces the packages and creates new batch/script files. Meanwhile it keeps a copy of the old batch/script files for your reference. You should use the batch/script files that come with the installer to make sure to add all new packages to the class path and to manually merge any changes you made into the new version. Server keeps your configuration files and server runtime data of the existing copy, and you can choose to recover the previous version during uninstalling the newly installed Server.
12. In the System Environment screen (available only when you have selected **Custom Installation for Standalone Server** in the Choose Installation Set screen), configure the following server system environment factors. You can also do this on the Server Console after you install and start Server.
    * **[Service](https://devnet.logianalytics.com/hc/en-us/articles/4405683591319-Configuring-the-Server-Service)**
    * [**Cluster**](https://devnet.logianalytics.com/hc/en-us/articles/4405683576343-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster#During)
    * [**E-mail**](https://devnet.logianalytics.com/hc/en-us/articles/4405690487319-Configuring-Export-Settings#Email)
    * **[Cache](https://devnet.logianalytics.com/hc/en-us/articles/4405690483735-Configuring-Cache#Report)**
    * **[Performance](https://devnet.logianalytics.com/hc/en-us/articles/4405683589015-Tuning-Server-Performance#Preload)**
      + **Maximum Number of Concurrent Reports in the Queue**  
        [Maximum number of concurrent reports in the queue](https://devnet.logianalytics.com/hc/en-us/articles/4405690492695-Configuring-Server-Using-Properties-in-server-properties#performance.max.reports), which must be less than or equal to the number that the license permits.
    * **[Advanced](https://devnet.logianalytics.com/hc/en-us/articles/4405683579799-Configuring-Advanced-Server-Settings)**
    * **Demo**Select to install the Logi Report demo reports and dashboards so that you will see them in the Public Reports folder in the server resource tree.
13. Select **Next**.
14. In the System Database screen (not available when you [upgrade Server](#Upgrade)), configure the system database.

    ![Logi Report Server Installation wizard - System Database screen](https://devnet.logianalytics.com/hc/article_attachments/4420447201431/install_wzd_win_sysdb.gif)

    * **Trial Database**   
       Select to install Server with the default trial database Derby for testing and evaluation purposes only. You should not use it in a production system. The port is configurable in case it is being used.
    * **Production Database**   
       Select to install Server with a production database. In a production environment, you need to configure your own production DBMS. Set the correct database connection information. If the connection fails after you select **Next**, Server displays a message, and you can choose to reset the connection. If you choose to continue after the failure, you will need to configure the database later. For more information, see [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/4405690486423-Configuring-the-Server-Database).

      See an example of using the Sybase SQL Anywhere JDBC driver sajdbc4.jar as the Server system database.

      1. Make sure to add the folder that contains the JDBC driver support files to the system environment variable. Refer to [JDBC client deployment](http://dcx.sap.com/index.html#sa160/en/dbprogramming/jdbc-client-deploy.html) for the required support files for different platforms.
      2. Select **Production Database**.
      3. Select **Sybase** from the Database list.
      4. Specify the JDBC URL as

         `jdbc:sqlanywhere:DBN=dbname;ServerName=servernane;Host=IP_Address;port=2638`

         or

         `jdbc:sqlanywhere:eng=servernane;database=dbname;host=IP_Address;port=2638.`
      5. In the JDBC Driver Class Name text box, type **sybase.jdbc4.sqlanywhere.IDriver**.
      6. Select **Add** to choose **sajdbc4.jar** as the driver.
      7. Provide the username and password respectively.

      ![Configure Server Database to Use Sybase](https://devnet.logianalytics.com/hc/article_attachments/4420453535767/install_wzd_win_sysdb_eg.gif)
15. Select **Next**.
16. In the Select JDK screen (not available when you [upgrade Server](#Upgrade)), choose the JDK you want Server to use. You can select one from the **Installed JDKs** box or select **Browse** to locate a JDK.

    ![Logi Report Server Installation wizard - Select JDK screen](https://devnet.logianalytics.com/hc/article_attachments/4420461615127/install_wzd_win_slctjdk.gif)
17. Select **Next**.
18. In the Add Class Path screen (not available when you [upgrade Server](#Upgrade)), you can add the additional class paths. You can also choose to add them manually into the **setenv.bat** file in `<install_root>\bin` after the installation.
19. Select **Next**.
20. In the Lists screen (available only when you [upgrade](#Upgrade)Logi Report Server), review the removed patches, modified configuration files, and backup files if you want.
21. Select **Next**.
22. In the Installation Summary screen, review the installation information and select **Install** to install Server.
23. In the Installing screen, you see the installing process and status.
24. After installation, Server displays the Read Me screen. Read the information and specify what to do next:
    * To start Server right away, keep **Start Logi Report Server once installation is completed** (available only on Windows) selected.
    * To [run Logi Report Server as a Windows service](https://devnet.logianalytics.com/hc/en-us/articles/4405683919383-Running-Logi-Report-Server-as-an-OS-Service#Win), select **Install Logi Report Server as a Windows Service**.
    * To close the Installation Wizard, make sure to select neither option.Select **Done** to finish the installation.

    ![Logi Report Server Installation wizard - Read Me screen](https://devnet.logianalytics.com/hc/article_attachments/4420453536023/install_wzd_win_rdm.gif)

## Installing Server on UNIX/Linux

Server supports Solaris, HP-UX, AIX, and Linux. In the following process, an X server is running and Java 8 is available, otherwise ask your administrator for help. You should have configured an X server before installing and running Server.

1. Download the Server installation file for UNIX/Linux from the [Logi Report download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).

   If you need to transfer the installation file from your download computer to your UNIX/Linux box, transfer it using FTP in binary mode.
2. Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window by right-clicking the blank area of the Desktop and selecting **Open Terminal** from the shortcut menu, and change the directory to the location of the file. The following examples introduce the commands that you can use:

   `$ cd /opt/LogiReport/Server` (or your preferred installation path)

   To make the installation file executable, type the command:

   `$ chmod +x server-xxx-linux.bin` (replace server-xxx-linux.bin with the actual name of the installation file)

   To run the installation file:

   `$ ./server-xxx-linux.bin` (replace server-xxx-linux.bin with the actual name of the installation file)
3. Once the Installation Wizard has loaded, you can follow the [standard prompts](#Win) to install Server.

## Installing Server on Linux on IBM Z

Server supports running on Linux on IBM System z. In the following process, an X server is running and a JDK specially used for IBM is available, otherwise ask your administrator for help. You should have configured an X server before installing and running Server.

1. Download the Server installation file for Linux on IBM Z from the [Logi Report download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).

   If you need to transfer the installation file from your download computer to your Linux on IBM Z box, transfer it using FTP in binary mode.
2. Open a console window by right-clicking the blank area of the Desktop and selecting **Open Terminal** from the shortcut menu. Then:
   1. Change the directory to the location of the file. You can type the following command in the console window: `cd /opt/LogiReport/Server` (input the absolute install location). Then press **Enter**.
   2. Type the following command to make the installation file executable: `chmod +x server-xxx-linux.bin` (replace server-xxx-linux.bin with the actual name of the installation file). Then press **Enter**.
   3. Type the following command to run the installation file: `./server-xxx-linux.bin` (replace server-xxx-linux.bin replace the actual name of the installation file). Then press **Enter**.

   See the following example.

   ![Install on Linux](https://devnet.logianalytics.com/hc/article_attachments/4420461615639/install_wzd_linux.gif)
3. Server displays the Installation Wizard. Follow the [standard prompts](#Win) to install Server.

## Installing Server on macOS

1. Download the Server installation zip file for macOS from the [Logi Report download center](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads).
2. Double-click the zip file to extract the installer file, SvrSetup.app.
3. Open **Terminal** and navigate to the folder where you have extracted SvrSetup.app.
4. Next, either:

   Execute this command to start the installation: `open -a SvrSetup.app`

   Or, execute this command: `xattar -cr SvrSetup.app` and then double-click **SvrSetup.app** to start installation.
5. Server displays the Installation Wizard. Follow the [standard prompts](#Win) to install Server.

## Solving Installation Problems

If errors occur during the installation, you can check the log information to find out the problem. Where logs are generated depends on when the installation process get stuck:

* If you cancel the installation before you select **Install** in the Installation Wizard, logs generate on the desktop for Windows and in the userhome directory for UNIX/Linux/macOS.
* If you cancel the installation after you select **Install** in the Installation Wizard, logs generate in the **logs** folder in the installation root directory.

You can also specify the log file path when launching the Installation Wizard by running the following command:

`server-xxx-win64.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"`

or

`$ ./server-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"`

Replace server-xxx-win64.exe or server-xxx-linux.bin with the real file name of the installation file.

If you need more information, contact [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683897495-Supported-Report-Databases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690619415-Installing-Server-Silently)
