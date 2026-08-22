---
title: "Installing Silently"
id: 1500009722662
section: "Install Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009722662-Installing-Silently
updated_at: 2021-07-25T07:19:06Z
---

# Installing Silently

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749661-Installing-Using-the-Installation-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722582-Installing-Using-the-Console-Interface)

# Installing Silently

Logi Report provides .properties files for installing Logi Report Server silently without user participation in the installation process on Windows, Unix, and Linux.

**To install Logi Report Server silently:**

1. Get the appropriate .properties file used for silent Logi Report Server installation from Logi Analytics Support and put it to the directory where the Logi Report Server installation file is saved.

   Logi Report provides two files for installing Logi Report Server silently, which are ServerInstall\_typical.properties for the Typical Installation for Standalone Server type and ServerInstall\_custom.properties for the Custom Installation for Standalone Server type.
2. Edit the .properties file to suit your requirements.
3. Logi Report Server provides built-in demo reports with Derby as the data source. At the end of the installation, the installer will configure the reports and catalog to the correct data path. This calls some AWT classes that require GUI support.

   So, if you have an X server installed, you should set the Display variable so that this step can be performed successfully.

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

**Notes:**

* When installing Logi Report Server silently, make sure you do not use upgrade installation. It is not supported for now.
* If you do not have X server or a pure text environment, step 3 can be ignored. However, you may find that you cannot run the demo reports after you start Logi Report Server due to the data source path is not configured correctly. In this case, you can use Logi Report Designer to publish some working reports for testing purposes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749661-Installing-Using-the-Installation-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009722582-Installing-Using-the-Console-Interface)
