---
title: "Installing Silently"
id: 1500009672961
section: "Installing Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009672961-Installing-Silently
updated_at: 2021-07-24T20:54:13Z
---

# Installing Silently

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648362-Installing-Using-the-Installation-Wizard)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009672921-Installing-Using-the-Console-Interface)

# Installing Silently

Logi JReport provides two files for installing Logi JReport Server silently without user participation in the installation process, which are ServerInstall\_typical.properties for the Typical Installation for Standalone Server type and ServerInstall\_custom.properties for the Custom Installation for Standalone Server
type.

Follow the steps below to install Logi JReport Server silently:

1. Copy the appropriate file from `<install_root>\help\samples\SilentInstall` to the directory where the Logi JReport Server installation file is saved and edit it to suit your requirements.
2. Some built-in demo reports (\\*.cls) with Derby as the data source (install\_root\db\SampleDB.script) have been provided. At the end of the installation, the installer will configure the reports and catalog to the correct data path. This calls some AWT classes that require GUI support.

   So, if you have an X server installed, you should set the Display variable so that this step can be performed successfully.

   `$ DISPLAY=hostname(or IP address):0.0  
    $ export DISPLAY`

   **Note:** If you do not have X server or a pure text environment, this step can be ignored. However, you may find that the demo reports will not be able to run after you start the Logi JReport Server due to having the wrong default data source path. In this case, you can use Logi JReport Designer to publish some working reports for testing purposes.
3. Run the following command, and Logi JReport Server will be installed in the designated path:

   `$ ./jrserver-xxx-linux.bin -i silent -f ServerInstall_typical.properties` (change *jrserver-xxx-linux.bin* to the real file name of the installation file)

**Notes:**

* When installing Logi JReport Server silently, make sure you do not use upgrade installation, it is not supported for now.
* When you install the Update or Service Pack silently, edit the file update.properties in `<install_root>\help\samples\SilentInstall` to your own requirements. This file is used to create an option file (that is, response file) for the Installation Wizard. It predefines all the information that is required for the installation.

  You can also create a property file and save it as follows:

  `USER_INSTALL_DIR=/usr/local/Logi JReport/Server  
   USER_KEY=UID  
   USER_PASSWORD=Password`

  Modify the above lines according to your own environment and configurations.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009648362-Installing-Using-the-Installation-Wizard)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009672921-Installing-Using-the-Console-Interface)
