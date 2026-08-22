---
title: "Installing on Unix Manually"
id: 1500009749581
section: "Install Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749581-Installing-on-Unix-Manually
updated_at: 2021-07-25T07:19:06Z
---

# Installing on Unix Manually

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722582-Installing-Using-the-Console-Interface)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722682-Installing-by-Deploying-a-WAR-File)

# Installing on Unix Manually

In rare cases, Logi Report Server may fail to install on Unix directly. In this case, follow the steps below to install it manually. You can also take the procedure to install Logi Report Server manually on Linux and Linux on IBM Z systems.

1. [Install Logi Report Server on Windows](https://devnet.logianalytics.com/hc/en-us/articles/1500009749661-Installing-Using-the-Installation-Wizard#Win), but don't start it.
2. Make the following changes to the server:
   * Modify javahome and reporthome in report.ini, servlet.properties and setenv.sh in `<install_root>/bin` to the Unix directories using absolute path, where the Java JDK is located and you are going to copy the server on the Unix system, for example `/usr/local/lib/jdk1.8.0` and `/opt/LogiReport/Server`. Be sure to modify them carefully. Any mistake will cause problems starting Logi Report.
   * Modify javahome in the file env.sh in `<install_root>/derby/bin` to the Unix directory where the Java JDK is located on the Unix system, using absolute path.
   * Delete the file server.properties from `<install_root>/bin` if it exists and remember to reset the required configuration settings in the Logi Report Server console after launching the server on Unix.
3. Make a zip or jar archive for the Windows Logi Report Server.
4. Copy the archive file to your Unix system (use binary format if using FTP).
5. Extract the archive to the Unix destination directory in accordance with the reporthome path you have specified to copy the server, for example `/opt/LogiReport/Server`.
6. Use the dos2unix command to convert all the .sh files under `/opt/LogiReport/Server/bin` to the format that can be recognized by Unix. You can execute the command like this:

   `$ dos2unix *.sh`
7. Use the chmod command to set the converted files under `/opt/LogiReport/Server/bin` to have read, write and execute permission. You can execute the command like this:

   `$ chmod 777 *.sh`
8. Start a shell (Console) and login as root or become the root user by running the su command. Make JRServer.sh executable and then start Logi Report Server by running `./JRServer.sh`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009722582-Installing-Using-the-Console-Interface)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722682-Installing-by-Deploying-a-WAR-File)
