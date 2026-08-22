---
title: "Installing Server Silently"
id: 1500009776721
section: "Installing and Uninstalling Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009776721-Installing-Server-Silently
updated_at: 2021-07-24T00:48:06Z
---

# Installing Server Silently

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748322-Installing-Server-Using-the-Installation-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776641-Installing-Server-Using-the-Console-Interface)

# Installing Server Silently

This topic describes how you can install Server silently using .properties files, without participation in the installation process on Windows, Unix, and Linux.

**To install Server silently:**

1. Get the appropriate .properties file for silent Server installation from Logi Analytics Support and put it to the directory where you saved the Server installation file.

   Logi Report provides two files for installing Server silently. **ServerInstall\_typical.properties** is for the Typical Installation for Standalone Server type and **ServerInstall\_custom.properties** for the Custom Installation for Standalone Server type.
2. Edit the .properties file to suit your requirements.
3. Server provides built-in demo reports with Derby as the data source. At the end of the installation, the installer configures the reports and catalog to the correct data path. This calls AWT classes that require GUI support.

   If you have installed an X server, you should set the **Display** variable to perform this step successfully.

   `$ DISPLAY=hostname(or IP address):0.0  
    $ export DISPLAY`
4. Open a console window and change the directory to the location of the installation file.

   `$ cd thepath`
5. Run commands to install the Update/Service Pack in the designated path:
   * For Windows, run the following command:

     `$ server-xxx-win64.exe -i silent -f ServerInstall_xxx.properties`
   * For Unix/Linux:

     First run the following command to make the installation file executable:

     `$ chmod +x server-xxx-linux.bin`

     Then run the command:

     `$ ./server-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f ServerInstall_xxx.properties`

   Change server-xxx-win64.exe/server-xxx-linux.bin and ServerInstall\_xxx.properties to the real file names of the installation and properties files.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* When installing Server silently, make sure you do not use upgrade installation. It is not supported for now.
* If you do not have X server or a pure text environment, you can ignore step 3. However, you may find that you cannot run the demo reports after you start Server due to the data source path is not configured correctly. In this case, you can use Designer to publish some working reports for testing purposes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748322-Installing-Server-Using-the-Installation-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009776641-Installing-Server-Using-the-Console-Interface)
