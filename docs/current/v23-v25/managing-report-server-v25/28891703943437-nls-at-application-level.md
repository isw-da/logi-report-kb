---
title: "NLS at Application Level"
id: 28891703943437
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891703943437-NLS-at-Application-Level
updated_at: 2026-02-26T02:13:34Z
source_host: docs-report.zendesk.com
---
# 
NLS at Application Level 

Report Server adds a folder "resources" in the installation root directory for holding language resources. This topic describes how you can create language packages and resource files respectively to display the whole server environment in your favorite language.

The resources are classified into two types, language packages and resources for Report Engine. To display Server in your favorite language completely, you need to create the language files for these two types of resources, respectively.

When you create a WAR/EAR file to include a Report Server, Server generates the languages.jar to pack all language resources in the <server_install_root>\resources directory and includes it in the WAR/EAR for the multiple language support. The languages.jar ensures that the server UI text displays correctly after you deploy the WAR/EAR to other application servers.

This topic contains the following sections:

- 
                    Creating Language Packages
                

- 
                        Manually Adding a Language Package
                    

- 
                        Specifying the Default Language Package 
                    

- 
                    Creating the Report Engine Language Resource Files
                

## 
Creating Language Packages

The language packages hold almost all the UI text and messages available in Report Server, including the Server Console, Page Report Studio, Web Report Studio, JDashboard, and Visual Analysis. When you apply a language package, the Server UI displays in the language specified in the language package. When there are more than one language packages, you can select the one you are familiar with for your own convenience as the Server environment language. For example, if you are a German you may be glad to apply the German language package.

Currently Report provides only the English language packages "en" and "en-us" for the English version. However, Report accepts user-customized language packages and can recognize and load them if you define them correctly. 

In each language package, there are three property files which together contain all UI text and messages in Server: 

- 
common.properties
    This property file stores some common UI text all over Server (including the Server Console, Page Report Studio, Web Report Studio, JDashboard, and Visual Analysis) in the specific language.

- 
dhtml.properties
    This property file stores UI text and messages referred by Page Report Studio, Web Report Studio, JDashboard, and Visual Analysis in the specific language.

- 
server.properties
    This property file stores UI text and messages referred by the Server Console in the specific language.

Server stores the language packages in the <server_install_root>\resources\server\languages directory.

The structure of a language package is: 

\LanguageName

  \properties
  common.properties
dhtml.properties
server.properties

You can translate one additional property file for users of Report Server Monitor. The file is monitor.properties in the <monitor_install_root>\resources\server\languages\en\properties directory.

### 
Manually Adding a Language Package

To add a language package, follow the steps: 

- Browse to the <server_install_root>\resources\server\languages directory.

- Create a folder for the new language. The folder name should keep to ISO language and country code naming criterion. 

- Copy the properties folder in the existing <server_install_root>\resources\server\languages\en directory to the new folder. 

- Modify the three property files: common.properties, dhtml.properties, and server.properties in the new folder by translating all the text and messages after "=" to the new language.

-  Save these property files with UTF-8 encoding. 

- 
Convert the contents in the three property files into Unicode using native2ascii.exe in the <jdk_install_root>\bin directory by running the following line in the Command Console:
    C:\jdk1.8.0\bin>native2ascii -encoding utf-8 common.properties >newcommon.properties

C:\jdk1.8.0\bin>native2ascii -encoding utf-8 dhtml.properties >newdhtml.properties

C:\jdk1.8.0\bin>native2ascii -encoding utf-8 server.properties >newserver.properties

When you convert your property files to the same directory as the original ones, you need to give them new names instead of replacing the original to avoid problems.

- Rename the original property files. You may want to modify them later.

- Change the names of the generated property files back to the same names as the original property files: newcommon.properties to common.properties, newdhtml.properties to dhtml.properties, and newserver.properties to server.properties.

- Restart Server.

Naming Criterion for Language Package Folders

* FolderName(language)

* FolderName(language-country)

* FolderName(language-country-variant)

The folder name should be lower-case code.

 The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: http://www.loc.gov/standards/iso639-2/php/code_list.php.

The country argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html.

The variant argument is a vendor or browser-specific code. For example, use win for Windows, mac for Macintosh, and posix for POSIX. Where there are two variants, separate them with an underscore, and put the more important one first.

### 
Specifying the Default Language Package 

When you have finished creating the language packages, you can select one to apply to your server. There are two ways to specify the default language package:

You can use the option Specify Default Language in the server profile to switch the language. The available language list depends on the language packages in <server_install_root>\resources\server\languages.

To specify the language on the Server Console:

Choose according to your user account: 

-  Anyone can configure for themselves: go to the My Profile > Customize Server Preferences > Advanced tab and set a language.

- Administrators can configure for all users: go to the Administration > Server Profile > Customize Server Preferences > Advanced tab and set the default language for all users.

You can also control the UI language by the property jrs.language when accessing the Server Console or Page Report Studio via URL.

The specified language by URL property has higher priority than that you specified by UI option; however, it takes effect only in the current user session.

## 
Creating the Report Engine Language Resource Files

Server saves the Report Engine language resources in the following files in the <server_install_root>\resources\common\resource directory: JRError.properties, JRMessage.properties, JVMessage.properties, and JVMisc.properties. To create the files in a specified language, follow the steps:

- Save the files with new names which contain the ISO language and country code suffix in the same directory (for more information, see naming criterion). For example, if you want to create the French language files, save them as JRError_fr_FR.properties, JRMessage_fr_FR.properties, JVMessage_fr_FR.properties, and JVMisc_fr_FR.properties.

-  Translate all the text after "=" in the newly saved files to French.

- Save the files with UTF-8 encoding.

- 
Convert the contents in the files into Unicode.

- Rename the files to the original ones with the language and country suffix.

- Restart Server.

Which language resource files will apply depends on the language and locale settings of your system.
