---
title: "Installing Server Using the Console Interface"
id: 45204001020813
section: "Introduction to Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204001020813-Installing-Server-Using-the-Console-Interface
updated_at: 2026-04-30T14:10:12Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Installing Server Using the Console Interface 

This topic describes how to perform an interactive installation from a command prompt. With this, you are able to see the installation status and follow the installation process.

Take the following steps to perform console installation:

- Download the appropriate installation file according to your system requirements from the Report download center.

- Run the following command:
    For UNIX/Linux and Linux on IBM Z:

$ chmod +x server-xxx-linux.bin

$ ./server-xxx-linux.bin -i console (change server-xxx-linux.bin to the real file name of the installation file)

For Windows:

server-xxx-win64.exe -i console (change server-xxx-win64.exe to the real file name of the installation file)

- Make decisions following the installation process.
