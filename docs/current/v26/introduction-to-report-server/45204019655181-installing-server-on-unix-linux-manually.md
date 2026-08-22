---
title: "Installing Server on UNIX/Linux Manually"
id: 45204019655181
section: "Introduction to Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204019655181-Installing-Server-on-UNIX-Linux-Manually
updated_at: 2026-04-30T14:10:13Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Installing Server on UNIX/Linux Manually 

This topic describes how you can install  Server manually on UNIX, Linux, and Linux on IBM Z systems.

The following procedure takes UNIX as an example:

- 
Install Server on Windows, but do not start it.

- Make the following changes to the server:
    
- Modify javahome and reporthome in report.ini, servlet.properties, and setenv.sh in <install_root>/bin to the UNIX directories using absolute path, where the Java JDK is located and you are going to copy the server on the UNIX system, for example /usr/local/lib/jdk1.8.0 and /opt/LogiReport/Server. Be sure to modify them carefully. Any mistake will cause problems of starting Report.

- Modify javahome in the file env.sh in <install_root>/derby/bin to the UNIX directory where the Java JDK is located on the UNIX system, using absolute path.

- Delete the file server.properties from <install_root>/bin if it exists and remember to reset the required configuration settings on the Server Console after launching Server on UNIX.

- Make a zip or jar archive for the Report Server on Windows.

- Copy the archive file to your UNIX system (use binary format if using FTP).

- Extract the archive to the UNIX destination directory in accordance with the report home path you have specified to copy the server, for example /opt/LogiReport/Server.

-  Use the dos2unix command to convert all the .sh files under /opt/LogiReport/Server/bin to the format that UNIX can recognize. You can run the command like this:
    $ dos2unix *.sh

- Use the chmod command to set the converted files under /opt/LogiReport/Server/bin to have read, write, and execute permission.    $ chmod 777 *.sh 

- Start a shell (Console) and sign in as root or become the root user by running the su command. Make JRServer.sh executable and then start Report Server by running ./JRServer.sh.
