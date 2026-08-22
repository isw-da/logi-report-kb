---
title: "Sending Commands to Logi Report Server from Java"
id: 1500009748542
section: "Starting, Accessing, and Shutting Down Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748542-Sending-Commands-to-Logi-Report-Server-from-Java
updated_at: 2021-07-24T00:48:00Z
---

# Sending Commands to Logi Report Server from Java

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748522-Running-Logi-Report-Server-Within-an-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777061-Accessing-Logi-Report-Server-via-a-Web-Browser)

# Sending Commands to Logi Report Server from Java

You can send commands to Logi Report Server to either shut it down or pop up the user interactive interface for administration, after you started the server [as a standalone server](https://devnet.logianalytics.com/hc/en-us/articles/1500009748582-Running-Logi-Report-Server-as-a-Standalone-Server). This topic describes the commands and properties.

Logi Report has automatically generated the batch file **CmdSender.bat** for you so that you do not have to write a complicated command line.

You can send commands through the class **jet.server.CommandSender**. The full command is as follows:

`JAVA -classpath <classpath> -Djava.compiler=NONE [-Dreporthome=<install_root>] jet.server.CommandSender [-s:server -p:port] -w:password [-?]|admin|shutdown|gc|(local:on|off)`

* **-?**  
   Print brief help message.
* **-Djava.compiler=NONE**  
   This is without JIT. This property is optional. However, if you encounter problems running the server and you think that they relate to the Java VM, you can try turning off the JIT compiler and then running again.
* **-Dreporthome**  
   This is where you installed Logi Report Server. You need to provide this property only when you do not execute the command from the local host on which Logi Report Server is running.
* **-Dpoperror=true**  
   Set **-Dpoperror=true** if you want Server to display a message with the error information when an error occurs. By default, Server does not display the error message.
* **-Classpath**  
   The classpath must include the following packages originally in your `<install_root>\lib`:
  JRESServlets.jar; JREntServer.jar.
* **-s:server**  
   Host name on which Logi Report Server is running.
* **-p:port**  
   The port on which Logi Report Server is running. The default value is 8888.
* **-w:password**  
   Password of the admin user, for example: -w:admin.
* **admin**  
   A command that you send to Server to access the user interactive interface for administering Logi Report Server.
* **shutdown**  
   A command that you send to Server to shut it down.
* **local:on**  
   A command that you send to Server to only accept the administration commands from the local machine.
* **local:off**  
   A command that you send to Server to accept administration commands from anywhere.
* **gc**  
   A command that you send to Server asking the JVM to schedule the Java Garbage Collector.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)You will use some of the common options in the later topics. In addition, Logi Report has automatically generated the batch file **CmdSender.bat** for you so that you do not have to write a complicated command line.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748522-Running-Logi-Report-Server-Within-an-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777061-Accessing-Logi-Report-Server-via-a-Web-Browser)
