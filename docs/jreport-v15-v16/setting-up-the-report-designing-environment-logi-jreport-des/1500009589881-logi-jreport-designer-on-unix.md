---
title: "Logi JReport Designer on Unix"
id: 1500009589881
section: "Setting Up the Report Designing Environment - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589881-Logi-JReport-Designer-on-Unix
updated_at: 2021-07-24T05:54:33Z
---

# Logi JReport Designer on Unix

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568482-Logi-JReport-Designer-on-Windows)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589821-Silent-Installation)

# Logi JReport Designer on Unix

This topic introduces how to install Logi JReport Designer v15 on Unix.

Below is list of the sections covered in this topic:

> * [Installing Logi JReport Designer on Unix](#Install)
> * [Running Logi JReport Designer on Unix](#Run)
> * [Uninstalling Logi JReport Designer on Unix](#Uninstall)

## Installing Logi JReport Designer on Unix

To install Logi JReport Designer on Unix, follow the steps below:

1. Download the Logi JReport Designer installation file for Unix from the Jinfonet download center: [http://www.jinfonet.com/downloadLogi JReport/](http://www.jinfonet.com/downloadLogi%20JReport/).
2. Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window, and change the directory to the location of the file. The following are examples of the commands that can be used.

   `$ cd thepath`

   To make the installation file executable, type the command:

   `$ chmod +x jrdesigner-xxx-linux.bin` (change jrdesigner-xxx-linux.bin to the real file name of the installation file)

   To run the installation file:

   `$ ./jrdesigner-xxx-linux.bin` (change jrdesigner-xxx-linux.bin to the real file name of the installation file)
3. Once the Installation Wizard has been successfully loaded, you can then follow the default prompt to install Logi JReport Designer.

During the installation, pay attention to the following:

* The Installation Wizard will first find a JVM to get started. If no JVM is found, the Logi JReport installer will fail to launch. To resolve this issue, you can try either way:
  + Set JAVA\_HOME variable and append `$JAVA_HOME/bin` to PATH variable in system environment.
  + Specify a JVM for Installation Wizard with the option `LAX_VM` as follows:

    `$ ./jrdesigner-xxx-linux.bin LAX_VM "/home/jdk1.7.0_17/bin/java"` (change jrdesigner-xxx-linux.bin to the real file name of the installation file)

    The JDK path should use absolute path and be quoted by "".
* You are recommended to use JDK 7 or higher versions.

## Running Logi JReport Designer on Unix

To run Logi JReport Designer on Unix, run the script file Logi JReport.sh in `<install_root>/bin`. You can modify this script file by adding additional classes before launching Logi JReport Designer.

`$ ./Logi JReport.sh`

## Uninstalling Logi JReport Designer on Unix

To uninstall Logi JReport Designer on Unix, execute uninstaller.sh in `<install_root>/_uninst`.

Alternatively, you can open a console window, and change the directory to the location of the uninstaller.sh file. The following are examples of the commands that can be used:

`$ cd thepath`

Run the uninstaller file:

`$ ./uninstaller`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568482-Logi-JReport-Designer-on-Windows)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589821-Silent-Installation)
