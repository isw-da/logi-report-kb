---
title: "Installing Silently"
id: 1500009717261
section: "Introduction to Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009717261-Installing-Silently
updated_at: 2021-11-03T06:57:01Z
---

# Installing Silently

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691102-Installing-Using-the-Installation-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009690962-Installing-Using-the-Console-Interface)

# Installing Silently

Logi JReport provides .properties files for installing Logi JReport Server silently without user participation in the installation process on Windows, Unix and Linux.

**To install Logi JReport Server silently:**

1. Get the appropriate .properties file used for silent Logi JReport Server installation from Logi Analytics Support and put it to the directory where the Logi JReport Server installation file is saved.

   Logi JReport provides two files for installing Logi JReport Server silently, which are ServerInstall\_typical.properties for the Typical Installation for Standalone Server type and ServerInstall\_custom.properties for the Custom Installation for Standalone Server type.
2. Edit the .properties file to suit your requirements.
3. Logi JReport Server provides built-in demo reports with Derby as the data source. At the end of the installation, the installer will configure the reports and catalog to the correct data path. This calls some AWT classes that require GUI support.

   So, if you have an X server installed, you should set the Display variable so that this step can be performed successfully.

   `$ DISPLAY=hostname(or IP address):0.0  
    $ export DISPLAY`
4. Run the following command, and Logi JReport Server will be installed in the designated path:

   `$ ./jrserver.exe -i silent -f ServerInstall_typical.properties` (change jrserver.exe to the real file name of the installation file)

**Notes:**

* When installing Logi JReport Server silently, make sure you do not use upgrade installation. It is not supported for now.
* If you do not have X server or a pure text environment, step 3 can be ignored. However, you may find that the demo reports cannot be run after you start Logi JReport Server due to the data source path is not configured correctly. In this case, you can use Logi JReport Designer to publish some working reports for testing purposes.

**To install Logi JReport Server Update or Service Pack silently:**

Edit the file update.properties in `<install_root>\help\samples\SilentInstall` to your own requirements. This file is used to create an option file (that is, response file) for the installation wizard. It predefines all the information that is required for the installation.

You can also create a property file and save it as follows:

`USER_INSTALL_DIR=<Server_Install_Root>  
USER_KEY=UID  
USER_PASSWORD=Password`

Modify the above lines according to your own environment and configurations.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691102-Installing-Using-the-Installation-Wizard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009690962-Installing-Using-the-Console-Interface)
