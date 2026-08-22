---
title: "Installing Server on UNIX/Linux Manually"
id: 5741467324823
section: "Introduction to Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741467324823-Installing-Server-on-UNIX-Linux-Manually
updated_at: 2022-10-31T17:17:52Z
---

# Installing Server on UNIX/Linux Manually

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741452300695-Installing-Server-Using-the-Console-Interface)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741447438743-Installing-Server-by-Deploying-a-WAR-File)

# Installing Server on UNIX/Linux Manually

This topic describes how you can install Server manually on UNIX, Linux, and Linux on IBM Z systems.

The following procedure takes UNIX as an example:

1. [Install Server on Windows](https://devnet.logianalytics.com/hc/en-us/articles/5741447465111-Installing-Server-Using-the-Installation-Wizard#Win), but do not start it.
2. Make the following changes to the server:
   * Modify javahome and reporthome in report.ini, servlet.properties, and setenv.sh in `<install_root>/bin` to the UNIX directories using absolute path, where the Java JDK is located and you are going to copy the server on the UNIX system, for example `/usr/local/lib/jdk1.8.0` and `/opt/LogiReport/Server`. Be sure to modify them carefully. Any mistake will cause problems of starting Logi Report.
   * Modify javahome in the file env.sh in `<install_root>/derby/bin` to the UNIX directory where the Java JDK is located on the UNIX system, using absolute path.
   * Delete the file server.properties from `<install_root>/bin` if it exists and remember to reset the required configuration settings on the Server Console after launching Server on UNIX.
3. Make a zip or jar archive for the Logi Report Server on Windows.
4. Copy the archive file to your UNIX system (use binary format if using FTP).
5. Extract the archive to the UNIX destination directory in accordance with the report home path you have specified to copy the server, for example `/opt/LogiReport/Server`.
6. Use the dos2unix command to convert all the .sh files under `/opt/LogiReport/Server/bin` to the format that UNIX can recognize. You can run the command like this:

   `$ dos2unix *.sh`
7. Use the chmod command to set the converted files under `/opt/LogiReport/Server/bin` to have read, write, and execute permission.

   `$ chmod 777 *.sh`
8. Start a shell (Console) and sign in as root or become the root user by running the su command. Make JRServer.sh executable and then start Logi Report Server by running `./JRServer.sh`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741452300695-Installing-Server-Using-the-Console-Interface)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741447438743-Installing-Server-by-Deploying-a-WAR-File)
