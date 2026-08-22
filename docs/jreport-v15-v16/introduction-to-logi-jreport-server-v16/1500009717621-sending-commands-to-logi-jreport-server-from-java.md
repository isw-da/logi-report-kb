---
title: "Sending Commands to Logi JReport Server from Java"
id: 1500009717621
section: "Introduction to Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717621-Sending-Commands-to-Logi-JReport-Server-from-Java
updated_at: 2021-11-03T06:56:57Z
---

# Sending Commands to Logi JReport Server from Java

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691262-Running-Within-an-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717601-Accessing-Logi-Report-Server-via-a-Web-Browser)

# Sending Commands to Logi JReport Server from Java

After Logi JReport Server has been [started as a standalone server](https://devnet.logianalytics.com/hc/en-us/articles/1500009691282-Running-as-a-Standalone-Server), you can send commands to the server to either shut it down or pop up the user interactive interface for administration. All of these can be done through the class jet.server.CommandSender. The full command is as follows:

`JAVA -classpath <classpath> -Djava.compiler=NONE [-Dreporthome=<install_root>] jet.server.CommandSender [-s:server -p:port] -w:password [-?]|admin|shutdown|gc|(local:on|off)`

* **-?**  
   Prints brief help message.
* **-Djava.compiler=NONE**  
   This is without JIT. This is not a required option. However, if you encounter problems running the server and you think that they relate to the Java VM, you can try turning off the JIT compiler and running again.
* **-Dreporthome**  
   This is where Logi JReport Server is installed. It is the destination location you specified when you installed it. It is required only if you do not execute the command from the local host on which Logi JReport Server is running.
* **-Dpoperror=true**  
   This property is used to control whether to pop up a message to show error information. The default value is false which indicates that the error message will not be displayed.
* **-Classpath**  
   The classpath must include the following packages originally in your `<install_root>\lib`:
  JRESServlets.jar;
  JREntServer.jar.
* **-s:server**  
   Host name on which Logi JReport Server is running.
* **-p:port**  
   The port on which Logi JReport Server is running. The default value is 8888.
* **-w:password**  
   Password of the admin user. Example: -w:admin.
* **admin**  
   A command sent to the server asking to pop up the user interactive interface for administering Logi JReport Server.
* **shutdown**  
   A command sent to the server asking it to shut down.
* **local:on**  
   A command sent to the server asking to only allow the administration commands sent by the local machine.
* **local:off**  
   A command sent to the server asking to accept administration commands from anywhere.
* **gc**  
   A command sent to the server asking the JVM to schedule the Java Garbage Collector.

**Note:** Some of the common options will be used in the later topics. In addition, Logi JReport has automatically generated the batch file CmdSender.bat for you so that you do not have to write a complicated command line.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691262-Running-Within-an-Application-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717601-Accessing-Logi-Report-Server-via-a-Web-Browser)
