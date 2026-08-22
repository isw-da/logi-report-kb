---
title: "Silent Installation"
id: 1500009589821
section: "Setting Up the Report Designing Environment - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589821-Silent-Installation
updated_at: 2021-07-24T05:54:34Z
---

# Silent Installation

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589881-Logi-JReport-Designer-on-Unix)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589841-Solving-Installation-Problems)

# Silent Installation

Logi JReport provides a file for installing Logi JReport Designer silently without user participation in the installation process, both on Windows and Unix platforms.

Follow the steps below to install Logi JReport Designer silently:

1. Copy the file DesignerInstall.properties from `<install_root>\help\samples\SilentInstall` to the directory where the Logi JReport Designer installation file is saved and edit it to suit your requirements.
2. Run the following command, and Logi JReport Designer will be installed in the designated path:

   `$ ./jrdesigner-xxx-linux.bin -i silent -f DesignerInstall.properties`

   Or

   `$ ./jrdesigner-xxx-linux.bin LAX_VM "USER_JAVA_HOME/bin/java" -i silent -f DesignerInstall.properties` (recommended)

   Change jrdesigner-xxx-linux.bin to the real file name of the installation file.

**Notes:**

* When installing Logi JReport Designer silently, make sure you do not use overwrite installation, instead, install it to a new directory.
* When you install the Update or Service Pack silently, edit the file update.properties in `<install_root>\help\samples\SilentInstall` to your own requirements. This file is used to create an option file (that is, response file) for the Installation Wizard. It predefines all the information that is required for the installation.

  You can also create a property file and save it as follows:

  `USER_INSTALL_DIR=/usr/local/Logi JReport/Designer  
   USER_KEY=UID  
   USER_PASSWORD=Password`

  Modify the above lines according to your own environment and configurations.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589881-Logi-JReport-Designer-on-Unix)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589841-Solving-Installation-Problems)
