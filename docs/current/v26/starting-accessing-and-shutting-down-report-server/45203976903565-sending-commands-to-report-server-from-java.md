---
title: "Sending Commands to Report Server from Java"
id: 45203976903565
section: "Starting, Accessing, and Shutting Down Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203976903565-Sending-Commands-to-Report-Server-from-Java
updated_at: 2026-04-30T14:10:24Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Sending Commands to Report Server from Java 

You can send commands to Report Server to either shut it down or pop up the user interactive interface for administration, after you start Server as a standalone server. This topic describes the commands and properties.

Report has automatically generated the batch file CmdSender.bat for you so that you do not have to write a complicated command line.

You can send commands through the class jet.server.CommandSender. The full command is:

JAVA -classpath <classpath> -Djava.compiler=NONE [-Dreporthome=<install_root>] jet.server.CommandSender [-s:server -p:port] -w:password [-?]|admin|shutdown|gc|(local:on|off)

- 
-?
  Print brief help message.

- 
-Djava.compiler=NONE
  This is without JIT. This property is optional. However, if you encounter problems running the server and you think that they relate to the Java VM, you can try turning off the JIT compiler and then running again.

- 
-Dreporthome
  This is where you installed Report Server. You need to provide this property only when you do not run the command from the local host on which Report Server is running.

- 
-Dpoperror=true
  Set -Dpoperror=true if you want Server to display a message with the error information when an error occurs. By default, Server does not display the error message.

- 
-Classpath
  The classpath must include the following packages originally in your <install_root>\lib:
 JRESServlets.jar; JREntServer.jar.

- 
-s:server
  Host name on which Report Server is running.

- 
-p:port
  The port on which Report Server is running. The default value is 8888.

- 
-w:password
  Password of the administrator, for example: -w:admin.

- 
admin
  A command that you send to Server to access the user interactive interface for administering Report Server.

- 
shutdown
  A command that you send to Server to shut it down.

- 
local:on
  A command that you send to Server to only accept the administration commands from the local machine.

- 
local:off
  A command that you send to Server to accept administration commands from anywhere. 

- 
gc
  A command that you send to Server asking the JVM to schedule the Java Garbage Collector.

You will use some of the common options in the later topics. In addition, Report has automatically generated the batch file CmdSender.bat for you so that you do not have to write a complicated command line.
