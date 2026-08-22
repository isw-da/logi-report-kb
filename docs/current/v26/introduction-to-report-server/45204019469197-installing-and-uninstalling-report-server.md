---
title: "Installing and Uninstalling Report Server"
id: 45204019469197
section: "Introduction to Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204019469197-Installing-and-Uninstalling-Report-Server
updated_at: 2026-04-30T14:10:12Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Installing and Uninstalling Report Server

Report Server can run on Windows, UNIX, and Linux platforms. This topic describes how to install Server on different platforms using different methods.

You need to choose a Java Development Kit (JDK) to install Server. Report supports the Oracle JDK and OpenJDK versions as stated in the System Requirements. If you need more information, contact Customer Service.
    

Report supports the current mainstream databases as well as most databases which support JDBC drivers. In addition to traditional databases, Report also supports databases in the cloud, such as Vertica, Amazon RDS, and RedShift. For information about the databases and JDBC drivers that have been tested with Report, see Supported Report Databases in the Report Designer Guide.

Select the following links to view the topics:

- Checklist for an Install or Upgrade of Report

- Report Licenses

- Installing Server Using the Installation Wizard

- Installing Server Silently

- Installing Server Using the Console Interface

- Installing Server on UNIX/Linux Manually

- Installing Server by Deploying a WAR File

- Installing Server Service Packs

- Environment Variable Configuration for Docker

- Report Server Report Home Directory Overview

- Upgrading Report Server

- Migrating Server and Server Data

- Uninstalling Report Server

### 
Solve the Problem When Installer Could Not Find or Load Main Class com.zerog.lax.LAX

When you launch the installer for Report earlier than v23.3.1 with JDK 11.0.20 or higher, you may get the "Could not find or load main class com.zerog.lax.LAX" error message in the console:

~$ ./server-23.3-linux.bin
Preparing to install
Extracting the installation resources from the installer archive...
Configuring the installer for this system's environment...

Launching installer...

Error: Could not find or load main class com.zerog.lax.LAX
Caused by: java.lang.ClassNotFoundException: com.zerog.lax.LAX
~$ java -version
openjdk version "11.0.20" 2023-07-18
OpenJDK Runtime Environment (build 11.0.20+8-post-Ubuntu-1ubuntu122.04)
OpenJDK 64-Bit Server VM (build 11.0.20+8-post-Ubuntu-1ubuntu122.04, mixed mode, sharing)
This error is due to the latest change in JDK 11.0.20 (Release Note):

core-libs/java.util.jar
➜ Improved ZIP64 Extra Field Validation (JDK-8302483 (not public))

java.util.zip.ZipFile has been updated to provide additional validation of ZIP64 extra fields when opening a ZIP file. This validation may be disabled by setting the system property jdk.util.zip.disableZip64ExtraFieldValidation to true.

To solve the problem, use the following command to launch the installer:

# Reference: https://www.rgagnon.com/javadetails/java-set-java-properties-system-wide.html
~$ export _JAVA_OPTIONS=-Djdk.util.zip.disableZip64ExtraFieldValidation=true
# Or
~$ export JAVA_TOOL_OPTIONS=-Djdk.util.zip.disableZip64ExtraFieldValidation=true
# Then launch the installer
~$ ./server-23.3-linux.bin LAX_VM "/path/to/jdk-11.0.20/bin/java"
