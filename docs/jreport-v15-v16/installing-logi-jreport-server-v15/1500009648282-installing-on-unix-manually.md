---
title: "Installing on Unix Manually"
id: 1500009648282
section: "Installing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648282-Installing-on-Unix-Manually
updated_at: 2021-07-24T20:54:14Z
---

# Installing on Unix Manually

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672921-Installing-Using-the-Console-Interface)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648342-Installing-by-Building-a-WAR-File-on-Windows-to-Deploy-to-Linux-Unix)

# Installing on Unix Manually

In some rare cases, Logi JReport Server may fail to install on Unix directly. In this case, follow the steps below to install it manually:

1. Install Logi JReport Server on Windows following the steps in [Installing on Windows](https://devnet.logianalytics.com/hc/en-us/articles/1500009648362-Installing-Using-the-Installation-Wizard#Win), but don't start it.
2. Prepare a directory on Unix where you will copy the installation, for example `/opt/Logi JReport/Server`.
3. Modify javahome and reporthome in the following files in `<install_root>\bin` to the Unix directories where the Java JDK is located and the directory you are going to copy the release to, using absolute path. Be sure to modify them carefully. Any mistake will cause problems starting Logi JReport.

   report.ini  
    servlet.properties  
    setenv.sh
4. Modify javahome in the file env.sh in `<install_root>\derby\bin` to the Unix directory where the Java JDK is located, using absolute path.
5. Delete the file server.properties from `<install_root>\bin` if it exists and remember to reset the required configuration settings on the Logi JReport Administration page after launching Logi JReport Server on Unix. The server.properties file is created if you use the custom format to install.
6. Make a zip or jar archive of the above folders, and then copy it to your Unix system (use binary format if using FTP).
7. Extract the folder in the destination directory in accordance with the path defined in the property files.
8. Use the `dos2unix` command to convert all the .sh files under `<install_root>/bin` to the format that can be recognized by Unix. You can execute the command like this:

   `$ dos2unix *.sh`
9. Use the `chmod` command to set the converted files under `<install_root>/bin` to have read, write and execute permission. You can execute the command like this:

   `$ chmod 777 *.sh`
10. Start a shell (Console) and login as root or become the root user by running the `su` command. Make JRServer.sh executable and then start Logi JReport Server by running `./JRServer.sh`.

**Note:** If you fail to install Logi JReport Server on your z/Linux system directly, you can also follow the above steps to install the server manually.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009672921-Installing-Using-the-Console-Interface)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009648342-Installing-by-Building-a-WAR-File-on-Windows-to-Deploy-to-Linux-Unix)
