---
title: "Silent Installation "
id: 1500010033322
section: "Setting Up the Report Designing Environment - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033322-Silent-Installation
updated_at: 2021-07-24T10:38:11Z
---

# Silent Installation 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068741-Logi-JReport-Designer-on-Unix-Linux) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068681-Solving-Installation-Problems)

# Silent Installation

Logi JReport provides .properties files for installing Logi JReport Designer silently without user participation in the installation process on Windows, Unix, and Linux. Follow these steps to silently install Designer.

1. Get the file DesignerInstall.properties used for silent Logi JReport Designer installation from Logi Analytics Support and put it to the directory where the Logi JReport Designer installation file is saved.
2. Edit DesignerInstall.properties to suit your requirements.
3. Run the following command, and Logi JReport Designer will be installed in the designated path:

   `$ ./jrdesigner.exe -i silent -f DesignerInstall.properties`

   Or

   `$ ./jrdesigner.exe LAX_VM "USER_JAVA_HOME\bin\java.exe" -i silent -f DesignerInstall.properties` (recommended)

   Change jrdesigner.exe to the real file name of the installation file`.`

**Note:** When installing Logi JReport Designer silently, make sure you do not use overwrite installation, instead install it to a new directory.

## Installing Logi JReport Designer Update or Service Pack Silently

Edit the file update.properties in `<install_root>\help\samples\SilentInstall` to your own requirements. This file is used to create an option file (that is, response file) for the installation wizard. It predefines all the information that is required for the installation.

You can also create a property file and save it as follows:

`USER_INSTALL_DIR=<Designer_Install_Root>  
USER_KEY=UID  
USER_PASSWORD=Password`

Modify the above lines according to your own environment and configurations.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068741-Logi-JReport-Designer-on-Unix-Linux) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010068681-Solving-Installation-Problems)
