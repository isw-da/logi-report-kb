---
title: "Installing Server on Unix/Linux Manually"
id: 1500009776681
section: "Installing and Uninstalling Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776681-Installing-Server-on-Unix-Linux-Manually
updated_at: 2021-07-24T00:48:07Z
---

# Installing Server on Unix/Linux Manually

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776641-Installing-Server-Using-the-Console-Interface)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776741-Installing-Server-by-Deploying-a-WAR-File)

# Installing Server on Unix/Linux Manually

This topic describes how you can install Server manually on Unix, Linux, and Linux on IBM Z systems.

The following procedure takes Unix as an example:

1. [Install Server on Windows](https://devnet.logianalytics.com/hc/en-us/articles/1500009748322-Installing-Server-Using-the-Installation-Wizard#Win), but do not start it.
2. Make the following changes to the server:
   * Modify javahome and reporthome in report.ini, servlet.properties, and setenv.sh in `<install_root>/bin` to the Unix directories using absolute path, where the Java JDK is located and you are going to copy the server on the Unix system, for example `/usr/local/lib/jdk1.8.0` and `/opt/LogiReport/Server`. Be sure to modify them carefully. Any mistake will cause problems of starting Logi Report.
   * Modify javahome in the file env.sh in `<install_root>/derby/bin` to the Unix directory where the Java JDK is located on the Unix system, using absolute path.
   * Delete the file server.properties from `<install_root>/bin` if it exists and remember to reset the required configuration settings in the Server Console after launching Server on Unix.
3. Make a zip or jar archive for the Logi Report Server on Windows.
4. Copy the archive file to your Unix system (use binary format if using FTP).
5. Extract the archive to the Unix destination directory in accordance with the report home path you have specified to copy the server, for example `/opt/LogiReport/Server`.
6. Use the dos2unix command to convert all the .sh files under `/opt/LogiReport/Server/bin` to the format that Unix can recognize. You can execute the command like this:

   `$ dos2unix *.sh`
7. Use the chmod command to set the converted files under `/opt/LogiReport/Server/bin` to have read, write and execute permission. You can execute the command as follows:

   `$ chmod 777 *.sh`
8. Start a shell (Console) and log in as root or become the root user by running the su command. Make JRServer.sh executable and then start Logi Report Server by running `./JRServer.sh`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009776641-Installing-Server-Using-the-Console-Interface)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776741-Installing-Server-by-Deploying-a-WAR-File)
