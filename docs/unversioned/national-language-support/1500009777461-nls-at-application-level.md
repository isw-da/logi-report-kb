---
title: "NLS at Application Level"
id: 1500009777461
section: "National Language Support"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009777461-NLS-at-Application-Level
updated_at: 2021-07-24T00:47:54Z
---

# NLS at Application Level

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777441-National-Language-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777481-NLS-at-Report-Level)

# NLS at Application Level

Logi Report Server adds a folder "resources" in the installation root directory for holding language resources. This topic describes how you can create language packages and resource files respectively to display the whole server environment in your favorite language.

The resources are classified into two types, language packages and resources for Logi Report Engine. To display Server in your favorite language completely, you need to create the language files for these two types of resources, respectively.

When you create a WAR/EAR file to include a Logi Report Server, Server generates the **languages.jar** to pack all language resources in the `<server_install_root>\resources` directory and includes it in the WAR/EAR for the multiple language support. The languages.jar ensures that the server UI text displays correctly after you deploy the WAR/EAR to other application servers.

This topic contains the following sections:

* [Creating Language Packages](#Package)

+ [Manually Adding a Language Package](#Add)
+ [Specifying the Default Language Package](#Default)

* [Creating the Logi Report Engine Language Resource Files](#Engine)

## Creating Language Packages

The language packages hold almost all the UI text and messages available in Logi Report Server, including the Server Console, Page Report Studio, Web Report Studio, JDashboard, and Visual Analysis. When you apply a language package, the Server UI displays in the language specified in the language package. When there are more than one language packages, you can select the one you are familiar with for your own convenience as the Server environment language. For example, if you are a German you may be glad to apply the German language package.

Currently Logi Report provides only the English language packages "en" and "en-us" for the English version. However, Logi Report accepts user-customized language packages and can recognize and load them if you define them correctly.

In each language package, there are three property files which together contain all UI text and messages in Server:

* **common.properties**  
   This property file stores some common UI text all over Server (including the Server Console, Page Report Studio, Web Report Studio, JDashboard, and Visual Analysis) in the specific language.
* **dhtml.properties**  
   This property file stores UI text and messages referred by Page Report Studio, Web Report Studio, JDashboard, and Visual Analysis in the specific language.
* **server.properties**  
   This property file stores UI text and messages referred by the Server Console in the specific language.

Server stores the language packages in the `<server_install_root>\resources\server\languages` directory.

The structure of a language package is as follows:

\LanguageName

\properties

common.properties

dhtml.properties

server.properties

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)You can translate one additional property file for users of Logi Report Server Monitor. The file is **monitor.properties** in the `<monitor_install_root>\resources\server\languages\en\properties` directory.

### Manually Adding a Language Package

To add a language package, follow the steps below:

1. Browse to the `<server_install_root>\resources\server\languages` directory.
2. Create a folder for the new language. The folder name should keep to ISO language and country code [naming criterion](#Name).
3. Copy the **properties** folder in the existing `<server_install_root>\resources\server\languages\en` directory to the new folder.
4. Modify the three property files: common.properties, dhtml.properties, and server.properties in the new folder by translating all the text and messages after "=" to the new language.
5. Save these property files with UTF-8 encoding.
6. Convert the contents in the three property files into Unicode using **native2ascii.exe** in the `<jdk_install_root>\bin` directory by running the following line in the Command Console:

   `C:\jdk1.8.0\bin>native2ascii -encoding utf-8 common.properties >newcommon.properties`

   `C:\jdk1.8.0\bin>native2ascii -encoding utf-8 dhtml.properties >newdhtml.properties`

   `C:\jdk1.8.0\bin>native2ascii -encoding utf-8 server.properties >newserver.properties`

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)When you convert your property files to the same directory as the original ones, you need to give them new names instead of replacing the original to avoid problems.
7. Rename the original property files. You may want to modify them later.
8. Change the names of the generated property files back to the same names as the original property files: newcommon.properties to common.properties, newdhtml.properties to dhtml.properties, and newserver.properties to server.properties.
9. Restart Server.

**Naming Criterion for Language Package Folders**

\* FolderName(language)

\* FolderName(language-country)

\* FolderName(language-country-variant)

The folder name should be lower-case code.

The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>.

The country argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.

The variant argument is a vendor or browser-specific code. For example, use **win** for Windows, **mac** for Macintosh, and **posix** for POSIX. Where there are two variants, separate them with an underscore, and put the more important one first.

### Specifying the Default Language Package

When you have finished creating the language packages, you can select one to apply to your server. There are two ways to specify the default language package:

You can use the option [Specify Default Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#Language) in the server profile to switch the language. The available language list depends on the language packages in `<server_install_root>\resources\server\languages`.

**To specify the language in the Server Console:**

Make a choice according to your user account:

* Anyone can configure for themselves: go to the **My Profile** > **Customize Server Preferences** > **Advanced** tab and set a language.
* Administrators can configure for all users: go to the **Administration** > **Server Profile** > **Customize Server Preferences** > **Advanced** tab and set the default language for all users.

You can also control the UI language by the property **jrs.language** when accessing the Server Console or Page Report Studio [via URL](https://devnet.logianalytics.com/hc/en-us/articles/1500009750382-Working-with-Server-via-URL#NLS).

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)The specified language by URL property has higher priority than that you specified by UI option; however, it takes effect only in the current user session.

## Creating the Logi Report Engine Language Resource Files

Server saves the Logi Report Engine language resources in the following files in the `<server_install_root>\resources\common\resource` directory: JRError.properties, JRMessage.properties, JVMessage.properties, and JVMisc.properties. To create the files in a specified language, follow the steps below:

1. Save the files with new names which contain the ISO language and country code suffix in the same directory (for more information, see the above [naming criterion)](#Name). For example, if you want to create the French language files, save them as JRError\_fr\_FR.properties, JRMessage\_fr\_FR.properties, JVMessage\_fr\_FR.properties, and JVMisc\_fr\_FR.properties.
2. Translate all the text after "=" in the newly saved files to French.
3. Save the files with UTF-8 encoding.
4. [Convert the contents](#Convert) in the files into Unicode.
5. Rename the files to the original ones with the language and country suffix.
6. Restart Server.

Which language resource files will apply depends on the language and locale settings of your system.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777441-National-Language-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777481-NLS-at-Report-Level)
