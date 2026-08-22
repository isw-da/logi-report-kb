---
title: "Installing Using the Installation Wizard"
id: 1500009749661
section: "Install Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749661-Installing-Using-the-Installation-Wizard
updated_at: 2021-07-25T07:19:05Z
---

# Installing Using the Installation Wizard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722602-Supported-Report-Databases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722662-Installing-Silently)

# Installing Using the Installation Wizard

This topic shows you how to install Logi Report Server to different systems with the Installation Wizard.

Select the following links to view the topics:

* [Installing on Windows](#Win)
* [Installing on Unix/Linux](#Unix)
* [Installing on Linux on IBM Z](#Linux)
* [Solving Installation Problems](#Solve)

## Installing on Windows

1. Download the Logi Report Server installation file for Windows from the [Logi Report download center](https://www.jinfonet.com/product/download-jreport/).
2. Double-click the installation file to run it, and select **Yes** in the prompt message dialog box.
3. The Logi Report Server Installation Wizard appears. Select **Next** in the Welcome screen.
4. In the License Agreement screen, select the option **I accept the terms of the License Agreement** and select **Next**.
5. In the User ID and License Key screen, type the user ID and the license key separately. If you haven’t received the key, contact Logi Analytics at +1 240-477-1000 or [salesteam@logianalytics.com](mailto:salesteam@logianalytics.com). Then select **Next**.

   If the license is machine specific, you need to make sure the name of the computer on which this Logi Report Server is being installed matches that defined in the license file.
6. In the Choose Installation Set screen, type the directory in the text box or select the **Browse** button to specify the directory to install Logi Report Server and select the installation type from the following two:
   * **Typical Installation for Standalone Server**  
      Installs Logi Report Server with the default configuration settings.
   * **Custom Installation for Standalone Server**  
      Installs Logi Report Server in a standalone environment. If you choose this installation type, you can configure the server system environment in the Installation Wizard. The option is not available when the specified installation directory already contains a Logi Report Server.

   ![Logi Report Server Installation wizard - Choose Installation Set screen](https://devnet.logianalytics.com/hc/article_attachments/4404936814743/install_wzd_win_instlst.gif)
7. Select **Next**.

   If you select to install Logi Report Server in a folder that already contains an Logi Report Server, you will be prompted to choose whether to overwrite or upgrade the existing server. If you select Upgrade, the installer will replace the packages and create new batch/script files. Meanwhile a copy of the old batch/script files will be kept for your reference. You should use the batch/script files that come with the installer in order to make sure that all new packages are added to the class path and manually merge any changes you made into the new version. However, your configuration files and server runtime data of the existing copy will be kept, and you can choose to recover the previous version during the uninstallation of the newly installed Logi Report Server.
8. In the System Environment screen (available only when the option Custom Installation for Standalone Server is selected in the Choose Installation Set screen), configure the following server system environment factors according to your requirements. System configuration can also be done in the Logi Report Server console after the server is installed and started.
   * **[Service](https://devnet.logianalytics.com/hc/en-us/articles/1500009718902-Configuring-the-Server-Service)**
   * [**Cluster**](https://devnet.logianalytics.com/hc/en-us/articles/1500009718702-Setting-Up-and-Configuring-a-Logi-Report-Server-Cluster#During)
   * [**E-mail**](https://devnet.logianalytics.com/hc/en-us/articles/1500009744881-Configuring-Export-Settings#Email)
   * **[Cache](https://devnet.logianalytics.com/hc/en-us/articles/1500009718762-Configuring-Cache#Report)**
   * **[Performance](https://devnet.logianalytics.com/hc/en-us/articles/1500009718862-Tuning-Server-Performance#Preload)**
     + **Maximum Number of Concurrent Reports in the Queue**  
        Specifies the [maximum number of concurrent reports in the queue](https://devnet.logianalytics.com/hc/en-us/articles/1500009744561-Appendix-2-Configuring-Logi-Report-Server-Using-Properties-in-server-properties#performance.max.reports), which must be less than or equal to the number that the license permits.
   * **[Advanced](https://devnet.logianalytics.com/hc/en-us/articles/1500009744721-Configuring-Advanced-Server-Settings)**
   * **Demo**Specifies whether to install the Logi Report demo reports and dashboards which will be available in the Public Reports folder in the server resource tree.
9. Select **Next**.
10. In the System Database screen (not available when you [upgrade](#Upgrade) Logi Report Server), configure the system database as required.

    ![Logi Report Server Installation wizard - System Database screen](https://devnet.logianalytics.com/hc/article_attachments/4404936815639/install_wzd_win_sysdb.gif)

    * **Trial Database**   
       Installs Logi Report Server with the default trial database Derby which is provided for testing and evaluation purposes only and which should not be used in a production system. The port is configurable in case it is being used.
    * **Production Database**   
       Installs Logi Report Server with a production database. In a production environment, you need to configure your own production DBMS. Set the correct database connection information. If the connection fails after selecting Next, a message will pop up and you can choose to reset the connection. Or if you choose to continue after the failure, you will need to configure the database later. For details, see [Configuring the Server Database](https://devnet.logianalytics.com/hc/en-us/articles/1500009744781-Configuring-the-Server-Database).

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")See an example below of using the Sybase SQL Anywhere JDBC driver sajdbc4.jar as the **Logi Report** Server system database.

      1. Make sure that the folder that contains the JDBC driver support files has been added to the system environment variable. Refer to [JDBC client deployment](http://dcx.sap.com/index.html#sa160/en/dbprogramming/jdbc-client-deploy.html) for the required support files for different platforms.
      2. Select the **Production Database** radio button.
      3. Select **Sybase** from the Database drop-down list.
      4. Specify the JDBC URL as

         `jdbc:sqlanywhere:DBN=dbname;ServerName=servernane;Host=IP_Address;port=2638`

         or

         `jdbc:sqlanywhere:eng=servernane;database=dbname;host=IP_Address;port=2638.`
      5. In the JDBC Driver Class Name text box, type **sybase.jdbc4.sqlanywhere.IDriver**.
      6. Select **Add** to choose **sajdbc4.jar** as the driver.
      7. Provide the user name and password respectively.

      ![Configure Server Database to Use Sybase](https://devnet.logianalytics.com/hc/article_attachments/4404936816023/install_wzd_win_sysdb_eg.gif)
11. Select **Next**.
12. In the Select JDK screen (not available when you [upgrade](#Upgrade) Logi Report Server) choose the JDK to use with Logi Report Server. You can select one from the Installed JDKs box or select the **Browse** button to locate a JDK.

    ![Logi Report Server Installation wizard - Select JDK screen](https://devnet.logianalytics.com/hc/article_attachments/4404936816279/install_wzd_win_slctjdk.gif)
13. Select **Next**.
14. In the Add Class Path screen (not available when you [upgrade](#Upgrade) Logi Report Server), you can add the additional class paths. You can also choose to add them manually into the file setenv.bat in  `<install_root>\bin` after the installation.
    Select **Next**.
15. In the Lists screen (available only when you [upgrade](#Upgrade) Logi Report Server), review the removed patches, modified configuration files, and backup files if you want. Select **Next**.
16. In the Installation Summary screen, review the installation information and select **Install** to install Logi Report Server.
17. In the Installing screen, the installing process and status are shown.
18. After installation, Report Server displays the Read Me screen. Read the information and specify what to do next:
    * To start Logi Report Server right away, keep the option **Start Logi Report Server once installation is completed** (available only on Windows) selected.
    * To [run Logi Report Server as a Windows service](https://devnet.logianalytics.com/hc/en-us/articles/1500009722962-Running-as-an-OS-Service#Win), select **Install Logi Report Server as a Windows Service**.
    * To close the Installation Wizard, make sure that neither options are selected.Select **Done** to finish the installation.

    ![Logi Report Server Installation wizard - Read Me screen](https://devnet.logianalytics.com/hc/article_attachments/4404942518679/install_wzd_win_rdm.gif)

## Installing on Unix/Linux

Logi Report Server supports Solaris, HP-UX, AIX, and Linux. In the following process, an X server is running and Java 8 is available, otherwise ask your administrator for help. Installing and running Logi Report Server requires that an X server has been configured.

1. Download the Logi Report Server installation file for Unix/Linux from the [Logi Report download center](https://www.jinfonet.com/product/download-jreport/).

   If you need to transfer the installation file from your download machine to your Unix/Linux box, you should transfer it using FTP in binary mode.
2. Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window by right-clicking on the blank area of the Desktop and selecting Open Terminal from the shortcut menu, and change the directory to the location of the file. Following are examples of the commands that can be used:

   `$ cd /opt/LogiReport/Server` (or your preferred installation path)

   To make the installation file executable, type the command:

   `$ chmod +x server-xxx-linux.bin` (change server-xxx-linux.bin to the actual name of the installation file)

   To run the installation file:

   `$ ./server-xxx-linux.bin` (change server-xxx-linux.bin to the actual name of the installation file)
3. Once the Installation Wizard has successfully loaded, you can follow the [standard prompts](#Win) to install Logi Report Server.

## Installing on Linux on IBM Z

Logi Report Server supports Linux on IBM System z. In the following process, an X server is running and a JDK specially used for IBM is available, otherwise ask your administrator for help. Installing and running Logi Report Server requires that an X server has been configured.

1. Download the Logi Report Server installation file for Linux on IBM Z from the [Logi Report download center](https://www.jinfonet.com/product/download-jreport/).

   If you need to transfer the installation file from your download machine to your Linux on IBM Z box, you should transfer it using FTP in binary mode.
2. Open a console window by right-clicking on the blank area of the Desktop and selecting Open Terminal from the shortcut menu. Then:
   1. Change the directory to the location of the file. You can type the following command in the console window: `cd /opt/LogiReport/Server` (input the absolute install location). Then press the **Enter** key on the keyboard.
   2. Type the following command to make the installation file executable: `chmod +x server-xxx-linux.bin` (change server-xxx-linux.bin to the actual name of the installation file). Then press the **Enter** key on the keyboard.
   3. Type the following command to run the installation file: `./server-xxx-linux.bin` (change server-xxx-linux.bin to the actual name of the installation file). Then press the **Enter** key on the keyboard.

   See the following example.

   ![Install on Linux](https://devnet.logianalytics.com/hc/article_attachments/4404942518935/install_wzd_linux.gif)
3. The Logi Report Server Installation Wizard appears. Follow the [standard prompts](#Win) to install Logi Report Server.

## Solving Installation Problems

If errors occur during the installation, you can check the log information recorded to find out what the problem is. Where logs are generated depends on when the installation process get stuck:

* If the installation is canceled before you select the Install button in the Installation Wizard, logs are created on the desktop for Windows and in the userhome directory for Unix/Linux.
* If the installation is canceled after you select the Install button in the Installation Wizard, logs are created in the logs folder in the installation root directory.

You can also specify the log destination that should use absolute path and log file name when launching the Installation Wizard by running the following command:

`server-xxx-win64.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"`

or

`$ ./server-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"`

Change server-xxx-win64.exe or server-xxx-linux.bin to the real file name of the installation file.

Feel free to send your questions to [support@logianalytics.com](mailto:support@logianalytics.com).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722602-Supported-Report-Databases)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722662-Installing-Silently)
