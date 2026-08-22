---
title: "Installing Server on UNIX/Linux Manually"
id: 4405690617623
section: "Introduction to Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690617623-Installing-Server-on-UNIX-Linux-Manually
updated_at: 2022-01-27T07:59:32Z
---

# Installing Server on UNIX/Linux Manually

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690616471-Installing-Server-Using-the-Console-Interface)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690622103-Installing-Server-by-Deploying-a-WAR-File)

# Installing Server on UNIX/Linux Manually

This topic describes how you can install Server manually on UNIX, Linux, and Linux on IBM Z systems.

The following procedure takes UNIX as an example:

1. [Install Server on Windows](https://devnet.logianalytics.com/hc/en-us/articles/4405683902487-Installing-Server-Using-the-Installation-Wizard#Win), but do not start it.
2. Make the following changes to the server:
   * Modify javahome and reporthome in report.ini, servlet.properties, and setenv.sh in `<install_root>/bin` to the UNIX directories using absolute path, where the Java JDK is located and you are going to copy the server on the UNIX system, for example `/usr/local/lib/jdk1.8.0` and `/opt/LogiReport/Server`. Be sure to modify them carefully. Any mistake will cause problems of starting Logi Report.
   * Modify javahome in the file env.sh in `<install_root>/derby/bin` to the UNIX directory where the Java JDK is located on the UNIX system, using absolute path.
   * Delete the file server.properties from `<install_root>/bin` if it exists and remember to reset the required configuration settings on the Server Console after launching Server on UNIX.
3. Make a zip or jar archive for the Logi Report Server on Windows.
4. Copy the archive file to your UNIX system (use binary format if using FTP).
5. Extract the archive to the UNIX destination directory in accordance with the report home path you have specified to copy the server, for example `/opt/LogiReport/Server`.
6. Use the dos2unix command to convert all the .sh files under `/opt/LogiReport/Server/bin` to the format that UNIX can recognize. You can execute the command like this:

   `$ dos2unix *.sh`
7. Use the chmod command to set the converted files under `/opt/LogiReport/Server/bin` to have read, write, and execute permission.

   `$ chmod 777 *.sh`
8. Start a shell (Console) and sign in as root or become the root user by running the su command. Make JRServer.sh executable and then start Logi Report Server by running `./JRServer.sh`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690616471-Installing-Server-Using-the-Console-Interface)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690622103-Installing-Server-by-Deploying-a-WAR-File)
