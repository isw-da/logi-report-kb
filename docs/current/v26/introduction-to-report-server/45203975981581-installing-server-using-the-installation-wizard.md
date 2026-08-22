---
title: "Installing Server Using the Installation Wizard"
id: 45203975981581
section: "Introduction to Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203975981581-Installing-Server-Using-the-Installation-Wizard
updated_at: 2026-04-30T14:10:15Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Installing Server Using the Installation Wizard

This topic describes how you can install Server on Windows, UNIX, Linux, and macOS using the Installation Wizard and solve problems during installation.

This topic contains the following sections:

- Installing Server on Windows
                

- Installing Server on UNIX/Linux
                

- Installing Server on Linux on IBM Z
                

- Installing Server on macOS
				

- Solving Installation Problems
                

## 
Installing Server on Windows

- Download the Server installation file for Windows from the Report download center. Note that you must have been assigned to be the License Point of Contact to access product downloads. If you need more information, contact Customer Service.
    

- Double-click the Report Server installation file to run it.

- The Installation Wizard displays a Welcome message. Select Next.

- In the License Agreement screen, select I accept the terms of the License Agreement.

- Select Next.

- The next installation wizard screen will prompt for the User ID and License Key.You can find the license information in your DEVNET account if you are assigned to be the License Key Point of Contact.

- In the DEVNET web page navigate to  Support > License Manager (1).

- Select the down arrow icon (2). This will display the License (Product) Key.

- Copy the UID (3) in the DEVNET screen (above), to the User ID field (5) in the Installation Wizard.

- Copy the Product Key (4) in the DEVNET screen (above), to the License Key field (6) in the Installation Wizard.

As an optional step, if a Server license should be assigned to a specific computer device, update the license assignment in the DEVNET License Manager with the name of the computer the license should be assigned to. 

- 
You can find your computer name by typing "About" in Windows search on the computer.  Note that the computer name value is case sensitive. See an example of the Windows computer device name:

- To perform DEVNET License Manager assignment, select Assign.

- A popup window will prompt to enter the Computer Name.

- Select Save.

For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

- Select Next.

- In the Choose Installation Set screen, type the directory in the text box or select Browse to specify the directory where you want to install Server. By default, the Report Server binaries will be installed in C:\LogiReport\Server.

- Select an installation type:
    
- 
Typical Installation for Standalone Server
 Select to install Server with the default configuration settings.

- 
Custom Installation for Standalone Server
        Select if you want to configure the server system environment in the Installation Wizard. The option is not available when the specified installation directory already contains a Server.

- Select Next.If you select to install the Report Server in a folder that already contains a previous installation, you will be asked to choose whether to overwrite or upgrade the existing server. If you select Upgrade, the installer replaces the packages and creates new batch/script files. Meanwhile it keeps a copy of the old batch/script files for your reference. You should use the batch/script files that come with the installer to make sure to add all new packages to the class path and to manually merge any changes you made into the new version. Server keeps your configuration files and server runtime data of the existing copy, and you can choose to recover the previous version during uninstalling the newly installed Server.

- The System Environment screen will be displayed only when you have selected Custom Installation for Standalone Server in the Choose Installation Set screen). Configure the following server system environment factors. You can also do this on the Server Console after you install and start Server.
    
- Service

- 
Cluster

- E-mail

- Cache

- 
Performance- 
Maximum Number of Concurrent Reports in the Queue
Maximum number of concurrent reports in the queue, which must be less than or equal to the number that the license permits.

- Advanced

- 
Demo
Select to install the Report demo reports and dashboards so that you will see them in the Public Reports folder in the server resource tree.

- Select Next. 

- In the System Database screen (not available when you upgrade Server), configure the system database.
    

- 
Trial Database
        Select to install Report Server with the default trial database (Derby) for testing and evaluation purposes only. You should not use it in a production system. The port is configurable in case it is being used.

- 
Production Database
 Select to install Report Server with a production database. In a production environment, you need to configure your own production DBMS. Set the correct database connection information. See an example of using the Sybase SQL Anywhere JDBC driver sajdbc4.jar as the Server system database.

- Make sure to add the folder that contains the JDBC driver support files to the system environment variable. Refer to JDBC client deployment for the required support files for different platforms.

- Select Production Database.

- Select Sybase from the Database list.

- Specify the JDBC URL as jdbc:sqlanywhere:DBN=dbname;ServerName=servernane;Host=IP_Address;port=2638

or

jdbc:sqlanywhere:eng=servernane;database=dbname;host=IP_Address;port=2638.

- In the JDBC Driver Class Name text box, type sybase.jdbc4.sqlanywhere.IDriver.

- Select Add to choose sajdbc4.jar as the driver.

- Provide the username and password respectively.

- Select Next. If the production database connection fails, you can choose to reset the connection. If you choose to continue after the failure, you will need to configure the database later. For more information, see Configuring Server Databases for Server Metadata.

- In the Select JDK screen, choose the JDK you want Server to use. Refer to the minimum server system requirements for which JDK to select here. You can select one from the Installed JDKs section or select Browse to locate a JDK that you download.
Note that this step will not be displayed when you upgrade Server.

-  Select Next. 

- In the Add Class Path screen (not available when you upgrade Server), you can add additional class paths. This is an optional step. If custom functionality is developed using Report’s API, a class path can be added in this screen to reference it. You can also choose to add the class paths manually into setenv.bat in <install_root>\bin after installation.

- Select Next. 

- In the Lists screen (available only when you upgradeReport Server), review the removed patches, modified configuration files, and backup files if you want. 

- Select Next.

- In the Installation Summary screen, review the installation information and select Install to install Report Server.

- During installation you see the process and status.

- After the installation completes, the Read Me screen is displayed. Read the information and specify what to do next: 
    
- To start Report Server immediately, select Start Report Server once installation is completed (available only on Windows).

- To run Report Server as a Windows service, select Install Report Server as a Windows Service.

- To close the Installation Wizard without starting Report Server, make sure to select neither option. 

- Select Done to complete the Report Server installation. 
  

## 
Installing Server on UNIX/Linux

Server supports Solaris, HP-UX, AIX, and Linux. In the following process, an X server is running and Java 8 is available, otherwise ask your administrator for help. You should have configured an X server before installing and running Server.

- Download the Server installation file for UNIX/Linux from the Report download center.
    If you need to transfer the installation file from your download computer to your UNIX/Linux box, transfer it using FTP in binary mode.

- Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window by right-clicking the blank area of the Desktop and selecting Open Terminal from the shortcut menu, and change the directory to the location of the file. The following examples introduce the commands that you can use:
    $ cd /opt/LogiReport/Server (or your preferred installation path)

To make the installation file executable, type the command:

$ chmod +x server-xxx-linux.bin (replace server-xxx-linux.bin with the actual name of the installation file)

To run the installation file:

$ ./server-xxx-linux.bin (replace server-xxx-linux.bin with the actual name of the installation file)

- Once the Installation Wizard has loaded, you can follow the standard prompts to install Server.

## 
Installing Server on Linux on IBM Z

Server supports running on Linux on IBM System z. In the following process, an X server is running and a JDK specially used for IBM is available, otherwise ask your administrator for help. You should have configured an X server before installing and running Server.

- Download the Server installation file for Linux on IBM Z from the Report download center.
    If you need to transfer the installation file from your download computer to your Linux on IBM Z box, transfer it using FTP in binary mode.

- Open a console window by right-clicking the blank area of the Desktop and selecting Open Terminal from the shortcut menu. Then:
    
- Change the directory to the location of the file. You can type the following command in the console window: cd /opt/LogiReport/Server (input the absolute install location). Then press Enter.

- Type the following command to make the installation file executable: chmod +x server-xxx-linux.bin (replace server-xxx-linux.bin with the actual name of the installation file). Then press Enter.

- Type the following command to run the installation file: ./server-xxx-linux.bin (replace server-xxx-linux.bin replace the actual name of the installation file). Then press Enter.

See the following example.

- Server displays the Installation Wizard. Follow the standard prompts to install Server.

## 
Installing Server on macOS

- Download the Server installation zip file for macOS from the Report download center.

- Double-click the zip file to extract the installer file, SvrSetup.app.

- Double-click SvrSetup.app to start installation. Server displays the Installation Wizard.

- Follow the standard prompts to install Server.

## 
Solving Installation Problems

If errors occur during the installation, you can check the log information to find out the problem. Where logs are generated depends on when the installation process get stuck: 

- If you cancel the installation before you select Install in the Installation Wizard, logs generate on the desktop for Windows and in the userhome directory for UNIX/Linux/macOS.

- If you cancel the installation after you select Install in the Installation Wizard, logs generate in the logs folder in the installation root directory.

You can also specify the log file path when launching the Installation Wizard by running the following command: 

server-xxx-win64.exe -D$INSTALL_LOG_NAME$="Install.log" -D$INSTALL_LOG_DESTINATION$="D:\temp"

or

$ ./server-xxx-linux.bin -D\$INSTALL_LOG_NAME\$="Install.log" -D\$INSTALL_LOG_DESTINATION\$="/opt/temp"

Replace server-xxx-win64.exe or server-xxx-linux.bin with the real file name of the installation file.

If you need more information, contact Customer Service.
