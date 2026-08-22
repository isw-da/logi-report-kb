---
title: "Shutting Down Report Server"
id: 28891675804685
section: "Starting, Accessing, and Shutting Down Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891675804685-Shutting-Down-Report-Server
updated_at: 2026-02-26T02:13:25Z
source_host: docs-report.zendesk.com
---
# 
Shutting Down Report Server 

This topic describes how you can shut down Report Server under different circumstances.

To shut down Report Server normally:

- In a standalone environment, choose one of the following:
			
- Select the Gear icon  at the upper right of the Server Console and select Shut Down Server from the drop-down menu.

- Take Report 23.1 as an example. Select Report 23.1 > Stop Server on the Start menu of your computer.

- Run the stopServer.bat or      stopServer.sh file in <install_root>\bin.

- In an integrated environment, shut down the application server according to the vendor's instructions.

Also, Report provides a feature for handling an abnormal system exit that enables the program to close itself gracefully when the Java virtual machine (JVM) is terminated in response to a user interrupt, such as typing ^C, or a system-wide event such as a user signs out or the system shuts down.
