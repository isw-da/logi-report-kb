---
title: "Logi JReport Designer on Unix/Linux"
id: 1500010068741
section: "Setting Up the Report Designing Environment - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068741-Logi-JReport-Designer-on-Unix-Linux
updated_at: 2021-07-24T10:38:11Z
---

# Logi JReport Designer on Unix/Linux

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068661-Logi-JReport-Designer-on-macOS) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033322-Silent-Installation-)

# Logi JReport Designer on Unix/Linux

This topic introduces how to install, run, and uninstall Logi JReport Designer on Unix.

Below is a list of the sections covered in this topic:

* [Installing Logi JReport Designer on Unix/Linux](#Install)
* [Running Logi JReport Designer on Unix/Linux](#Run)
* [Uninstalling Logi JReport Designer on Unix/Linux](#Uninstall)

## Installing Logi JReport Designer on Unix/Linux

1. Download the Logi JReport Designer installation file for Unix/Linux from the [Logi JReport download center](https://www.jinfonet.com/product/download-Logi%20JReport/).
2. Select the installation file to launch the Installation Wizard. Alternatively, you can open a console window, and change the directory to the location of the file. The following are examples of the commands that can be used.

   `$ cd thepath`

   To make the installation file executable, type the command:

   `$ chmod +x jrdesigner-xxx-linux.bin` (change jrdesigner-xxx-linux.bin to the real file name of the installation file)

   To run the installation file:

   `$ ./jrdesigner-xxx-linux.bin` (change jrdesigner-xxx-linux.bin to the real file name of the installation file)
3. Once the Installation wizard has been successfully loaded, you can then follow the [standard prompts](https://devnet.logianalytics.com/hc/en-us/articles/1500010068781-Logi-JReport-Designer-on-Windows#Wizard) to install Logi JReport Designer.

## Running Logi JReport Designer on Unix/Linux

Run the script file Logi JReport.sh in `<install_root>/bin`. You can modify this script file by adding additional classes before launching Logi JReport Designer.

`$ ./Logi JReport.sh`

## Uninstalling Logi JReport Designer on Unix/Linux

Execute uninstaller.sh in `<install_root>/_uninst`.

Alternatively, you can open a console window, and change the directory to the location of the uninstaller.sh file. The following are examples of the commands that can be used:

`$ cd thepath`

Run the uninstaller file:

`$ ./uninstaller`

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068661-Logi-JReport-Designer-on-macOS) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033322-Silent-Installation-)
