---
title: "Running Report Server as an OS Service"
id: 28891675879437
section: "Starting, Accessing, and Shutting Down Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891675879437-Running-Report-Server-as-an-OS-Service
updated_at: 2026-02-26T02:13:25Z
source_host: docs-report.zendesk.com
---
# 
Running Report Server as an OS Service 

You can configure Report Server as an OS service. This topic describes how you can run Report Server as a service of Windows, UNIX, and Linux.

This topic contains the following sections:

- Running Server as a Windows Service

- Configuring the Service

- Starting the Service

- Stopping the Service

- Running Server as a Service on UNIX

- Running Server as a Service on Linux

## 
Running Server as a Windows Service

The tool JRservice.exe in <install_root>\bin can assist you in installing Report Server as a Windows service.

You can get the following information if you run JRservice.exe without any properties:

Usage:

JRService -install [-interactive] to install the service
JRService -remove        to remove the service

    -interactive to enable Report Server service
        to interact with the desktop

StartServiceCtrlDispatcher being called.
This may take several seconds. Please wait.

- 
JRService -install
Running JRservice.exe with the -install property will install Report Server as a Windows service. If you open the Services item in the Control Panel, you will find a service named Report Server in the list.

- 
JRService -install -interactive
If you use the -interactive property together with -install, the service installed will run in interactive mode. That is, when you start the service, Server displays a Command Prompt window. However, if you do not provide this property when you install the service, Server does not display the Command Prompt window when you start the service. After you have installed Report Server as a service, you need to restart your computer for the service installation to take effect.

- 
JRService -remove
Running JRservice.exe with the -remove property removes the Windows service of Report Server from Windows. However, before you run this, you should stop the service.

### 
Configuring the Service

Server reads the parameters for the Windows service of Report Server from the file NTService.ini in <install_root>\bin. In this file, you can find three parameters, as shown in the following image:

- 
JavaVM
The path of the Java VM.

- 
StartArg
The Java command line for launching Report Server as an independent web application server. Server calls this parameter when the service starts. In most cases you need to modify -Xms and -Xmx to specify the Java heap size. After you modify this file you need to stop and start the service again. 

- 
ShutdownArg
The Java command line for shutting down Report Server. Server calls this parameter when the service stops.

### 
Starting the Service

You can start the Report Server service using either of the following ways:

- After you have installed Server as a service, the service will automatically start each time Windows starts.

- You can directly start the service through the Services item in the Control Panel. Open the Services list, find Report Server, select it, and then select Start.

You can change the parameters in the file NTService.ini in <install_root>\bin before you start the service (for more information, see Starting Report Server Using Java). For example, if you would like to set all log level to INFO, you need to append -logall to the value of StartArg:

... StartArg= ...
-Dreporthome="C:\LogiReport\Server" -Dadmin.port.enabled="false" jet.server.JREntServer -logall

### 
Stopping the Service

You can stop the Report Server service using one of the following ways: 
		

- Open the Control Panel, go to Administrative Tools, double-click Services, select Report Server, and then select the Stop button if it is not disabled.

- Run the batch file CmdSender.bat in <install_root>\bin with the localshutdown property, for example: <install_root>\bin\CmdSender.bat localshutdown.

- Select the Gear icon  at the upper right of the Server Console and select Shut Down Server from the drop-down menu.

- When using NT service to start Report Server, you cannot access the mapped disk path due to JVM limitation. You should use UNC path (for example, \\127.0.0.1\public_write) instead of the mapped disk (for example, Z).

- When using the Local System account to run Report Server as a Windows service, under some circumstances you cannot write to a UNC path (for example, \\127.0.0.1\public_write). To solve this problem, you need to start the service as a normal Windows user. 

## 
Running Server as a Service on UNIX

Assume that you installed Report Server to /user/report/jns.		

- Write a script /etc/init.d/jrserver, and make it executable.

#!/bin/sh
mode=$1
if [ ! -d /user/report/jns ]
then # Report not installed
exit 1
fi
case "$mode" in
'start')
if [ -d /user/report/jns ]
then
echo "Starting Report Server"
/user/report/jns/bin/NJRServer.sh &
fi
;;
'stop')
if [ -d /user/report/jns ]
then
echo "Stopping Report Server"
/user/report/jns/bin/CmdSender.sh localshutdown &
fi
;;
*)
echo " Usage: "
echo " $0 start (start Report Server)"
echo " $0 stop (stop Report Server)"
exit 1
;;
esac
exit 0

- Create a soft link to /etc/rc2.d/S99jrserver.
    ln -s /etc/init.d/jrserver /etc/rc2.d/S99jrserver

- Create a soft link to /etc/rc0.d/K99jrserver.
    ln -s /etc/init.d/jrserver /etc/rc0.d/K99jrserver

## 
Running Server as a Service on Linux

Assume that: 

- You are using CentOS.

- You installed Report Server to /opt/LogiReport/Server on the computer with the IP address 127.0.0.1. 

- 
Go to the /etc/systemd/system directory.

cd /etc/systemd/system

- 
Create a service LRServer.service

vi ./LRServer.service
with the contents (an example):

[Unit]
Description=Report Server
Documentation=
After=network.target

[Service]
Type=simple
User=LogiReport
Group=LogiReport
ExecStart=/opt/LogiReport/Server/bin/JRServer.sh
ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/opt/LogiReport/Server/bin/stopServer.sh
KillMode=process
Restart=on-failure
RestartSec=15s

[Install]
WantedBy=multi-user.target
If you are the root user, you can remove the two lines:

User=LogiReport
Group=LogiReport

- 
Make LRServer.service executable.

chmod +x ./LRServer.service

- 
Start the service.

systemctl start LRServer.service

- Access Report Server via http://127.0.0.1:8888.
