---
title: "Running as an OS Service"
id: 1500009722962
section: "Start Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722962-Running-as-an-OS-Service
updated_at: 2021-07-25T07:19:00Z
---

# Running as an OS Service

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749961-Running-as-a-Standalone-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749901-Running-Within-an-Application-Server)

# Running as an OS Service

Logi Report Server can be configured as an OS service. This topic shows you how to run Logi Report Server as a service of Windows, Unix and Linux.

Select the following links to view the topics:

* [Running as a Windows Service](#Win)

+ [Configuring the Service](#Config)
+ [Starting the Service](#Start)
+ [Stopping the Service](#Stop)

* [Running as a Service on Unix](#Unix)
* [Running as a Service on Linux](#Linux)

+ [Setting Up XVFB](#Set)
+ [Using rc to Run Logi Report Server as a Service](#Run)

## Running as a Windows Service

The tool JRservice.exe saved in  `<install_root>\bin` is provided to assist you in installing Logi Report Server as a Windows service.

You can get the following information if you run JRservice.exe without any options:

```
Usage:  
  
JRService -install [-interactive] to install the service  
JRService -remove        to remove the service  
  
    -interactive to enable Logi Report Server service  
        to interact with the desktop  
  
StartServiceCtrlDispatcher being called.  
This may take several seconds. Please wait.
```

* **JRService -install**  
  Running JRservice.exe with the -install option will install Logi Report Server as a Windows service. If you open the Services item in the Control Panel, you will find a service named Logi Report Server in the list.
* **JRService -install -interactive**  
  If you use the -interactive option together with -install, the service installed will be run in interactive mode. That is, when you start the service, a Command Prompt window will pop up. However, if you don't specify this option when you install the service, the Command Prompt window will not be displayed when you start the service. After you have installed Logi Report Server as a service, you will then be prompted to restart your computer for the service installation to take effect.
* **JRService -remove**  
  Running JRservice.exe with the -remove option removes the Windows service of Logi Report Server from Windows. However, before you run this, you should stop the service.

### Configuring the Service

The parameters for the Windows service of Logi Report Server are read from the file NTService.ini in `<install_root>\bin`. In this file, you can find three parameters specified, as shown in the following image:

![Parameters for the Windows Service](https://devnet.logianalytics.com/hc/article_attachments/4404936804631/launch_svc.gif)

* **JavaVM**  
  The path of the Java VM.
* **StartArg**  
  The Java command line for launching Logi Report Server as an independent web application server. This will be called when the service is started. In most cases you need to modify -Xms and -Xmx to specify the Java heap size. After you modify this file you need to stop and start the service again.
* **ShutdownArg**  
  The Java command line for shutting down Logi Report Server. This is called when the service is stopped.

### Starting the Service

There are two ways to start the Logi Report Server service.

* After the server has been installed as a service, it is by default configured to start automatically each time. In other words, without otherwise modifying the Control Panel, the service will start automatically each time Windows is started.
* You can directly start the service through the Services item in the Control Panel. Open the Services list, find Logi ReportServer on the list, select it and select the **Start** button.

You can change the options in the file NTService.ini in `<install_root>\bin` before you start the service (for more information on the options available, see [Starting Logi Report Server Using Java](https://devnet.logianalytics.com/hc/en-us/articles/1500009749961-Running-as-a-Standalone-Server#Java)). For example, if you would like to set all log level to INFO, you will need to append -logall to the value of StartArg as follows:

```
... StartArg= .....  
-Dreporthome="C:\LogiReport\Server" -Dadmin.port.enabled="false" jet.server.JREntServer -logall
```

### Stopping the Service

There are these ways for you to stop the Logi Report Server service:

* Open the Control Panel, go to **Administrative Tools**, double-click the **Services** item, select **Logi Report Server**, and then select the **Stop** button if it is not disabled.
* Run the batch file CmdSender.bat in  `<install_root>\bin` with the localshutdown argument, for example: `<install_root>\bin\CmdSender.bat localshutdown`.
* Point to the button ![Shut Down the Server button](https://devnet.logianalytics.com/hc/article_attachments/4404936805143/btn_srv_shtdwn.gif) at the top right of the server console and select **Shut Down Server** from the drop-down menu.

**Notes:**

* When using NT service to start Logi Report Server, the mapped disk in path cannot be accessed due to JVM limitation. You should use UNC path (for example, `\\127.0.0.1\public_write`) instead of the mapped disk it is mapped to (for example, `Z`).
* When using the Local System account to run Logi Report Server as a Windows service, under some circumstances writing to a UNC path (for example, `\\127.0.0.1\public_write`) is not allowed. To solve this problem, you need to start the service using a normal Windows user.

## Running as a Service on Unix

Assume that Logi Report Server has been installed to `/user/report/jns`,

1. Write a script /etc/init.d/jrserver as follows, and make it executable.

   ```
   #!/bin/sh  
   mode=$1  
   if [ ! -d /user/report/jns ]  
   then # Logi Report not installed  
   exit 1  
   fi  
   case "$mode" in  
   'start')  
   if [ -d /user/report/jns ]  
   then  
   echo "Starting Logi Report Server"  
   /user/report/jns/bin/NJRServer.sh &  
   fi  
   ;;  
   'stop')  
   if [ -d /user/report/jns ]  
   then  
   echo "Stopping Logi Report Server"  
   /user/report/jns/bin/CmdSender.sh localshutdown &  
   fi  
   ;;  
   *)  
   echo " Usage: "  
   echo " $0 start (start Logi Report Server)"  
   echo " $0 stop (stop Logi Report Server)"  
   exit 1  
   ;;  
   esac  
   exit 0
   ```
2. Create a soft link to /etc/rc2.d/S99jrserver.

   ln `-s /etc/init.d/jrserver /etc/rc2.d/S99jrserver`
3. Create a soft link to /etc/rc0.d/K99jrserver.

   ln `-s /etc/init.d/jrserver /etc/rc0.d/K99jrserver`

## Running as a Service on Linux

Running Logi Report Server as an OS service on Linux is more or less the same as with running on Unix. Here it is assumed that your default start up rc is rc5.

### Setting Up XVFB

1. Install XVFB.
2. Write a script /etc/init.d/xvfb as follows, and make it executable.

   ```
   #!/bin/sh  
   mode=$1  
   case "$mode" in  
   'start')  
   echo "start xvfb "  
   if [ -f /usr/X11R6/bin/Xvfb ]  
   then  
   /usr/X11R6/bin/Xvfb :1 -screen 0 1152x900x8 &  
   fi  
   ;;  
   *)  
   echo " Usage: "  
   echo " $0 start (start XVFB)"  
   echo " $0 stop (stop XVFB not support)"  
   exit 1  
   esac  
   exit 0
   ```
3. Create a soft link to /etc/rc5.d/S97xvfb.

   `ln -s /etc/init.d/xvfb /etc/rc5.d/S97xvfb`

### Using rc to Run Logi Report Server as a Service

Assume that Logi Report Server has been installed to `/LogiReport/Server`.

1. Write a script /LogiReport/Server/bin/JRServer as shown below, and make it executable. Here it is assumed that Logi Report Server is running on a machine with the IP address 127.0.0.1.

   ```
   #!/bin/sh
   DISPLAY=127.0.0.1:1.0
   export DISPLAY
   /LogiReport/Server/bin/JRServer -silent "$@"
   ```
2. Write a script `/etc/init.d/jrserver` as follows, and make it executable.

   ```
   #!/bin/sh  
   mode=$1  
   if [ ! -d /LogiReport/Server ]  
   then # Logi Report not installed  
   exit 1  
   fi  
   case "$mode" in  
   'start')  
   if [ -d /LogiReport/Server ]  
   then  
   echo "Starting Logi ReportServer"  
   cd /LogiReport/Server/bin/;  
   JRServer -silent &   
   fi  
   ;;  
   'stop')  
   if [ -d /LogiReport/Server ]  
   then  
   echo "Stopping Logi ReportServer"   
   /LogiReport/Server/bin/CmdSender localshutdown &  
   fi  
   ;;  
   *)  
   echo " Usage: "  
   echo " $0 start (start Logi ReportServer)"  
   echo " $0 stop (stop Logi ReportServer)"  
   exit 1  
   ;;  
   esac  
   exit 0
   ```
3. Create a soft link to /etc/rc5.d/S98jrserver.

   `ln -s /etc/init.d/jrserver /etc/rc5.d/S98jrserver`
4. Create a soft link to /etc/rc5.d/K98jrserver.

   `ln -s /etc/init.d/jrserver /etc/rc5.d/K98jrserver`

If all has been carried out successfully, the installation of the service will now have finished. Logi Report Server is now ready to run as a daemon process.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749961-Running-as-a-Standalone-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749901-Running-Within-an-Application-Server)
