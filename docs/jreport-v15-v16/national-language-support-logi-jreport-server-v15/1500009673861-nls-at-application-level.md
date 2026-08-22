---
title: "NLS at Application Level"
id: 1500009673861
section: "National Language Support Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009673861-NLS-at-Application-Level
updated_at: 2021-07-24T20:53:58Z
---

# NLS at Application Level

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673841-National-Language-Support)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649142-NLS-at-Report-Level)

# NLS at Application Level

In Logi JReport Server, a folder "resources" is added in the installation root directory for holding language resources. The resources are classified into two types, language packages and resources for Logi JReport Engine. To make Logi JReport Server display in your desired language completely, you need to create the language files for these two types of resources respectively.

When creating a WAR/EAR file to include a Logi JReport Server, the languages.jar which packs all language resources in the `<server_install_root>\resources` directory will be generated and included for the multiple language support. The languages.jar makes sure the server UI text is displayed correctly after deploying the WAR/EAR to other application servers.

Below is a list of the sections covered in this topic:

* [Creating Language Packages](#Package)
* [Manually Adding a Language Package](#Add)
* [Specifying the Default Language Package](#Default)
* [Creating the Logi JReport Engine Language Resource Files](#Engine)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating Language Packages

The language packages hold almost all the UI text and messages available in Logi JReport Server (including Page Report Studio, Web Report Studio, JDashboard and Visual Analysis). When a language package is applied, the UI will be displayed in the language specified in the language package. When there are more than one language packages, you can select the one you are familiar with for your own convenience as the Logi JReport Server environment language. For example, if you are a German you may be glad to apply the German language package.

Currently Logi JReport provides only the English language packages "en" and "en-us" for the English version and the Chinese language package "zh-cn" for the Chinese version. However, Logi JReport accepts user-customized language packages and can recognize and load them if they are correctly specified.

In each language package, there are three property files which together contain all UI text and messages in Logi JReport Server:

* **common.properties**  
   This property file stores some common UI text all over Logi JReport Server (including Page Report Studio, Web Report Studio, JDashboard and Visual Analysis) in the specific language.
* **dhtml.properties**  
   This property file stores UI text and messages referred by Page Report Studio, Web Report Studio, JDashboard and Visual Analysis in the specific language.
* **server.properties**  
   This property file stores UI text and messages referred by Logi JReport Server in the specific language.

The structure of a language package which is stored in the `<server_install_root>\resources\server\languages` directory follows:

\LanguageName

\properties

common.properties

dhtml.properties

server.properties

## Manually Adding a Language Package

To add a language package, follow the steps below:

1. Browse to the `<server_install_root>\resources\server\languages` directory.
2. Create a folder named fr. The folder name should keep to the [naming criterion](#Name).
3. Copy the properties folder in the existing `<server_install_root>\resources\server\languages\en` directory to the \fr folder.
4. Modify the three property files: common.properties, dhtml.properties, and server.properties in the \fr folder by translating all the text and messages after "=" to French.
5. Save these property files with UTF-8 encoding.
6. Convert the contents in the three property files into Unicode using native2ascii.exe in the `<jdk_install_root>\bin` directory by running the following line in the Command Console:

   `C:\jdk1.7.0_17\bin>native2ascii -encoding utf-8 common.properties >newcommon.properties`

   `C:\jdk1.7.0_17\bin>native2ascii -encoding utf-8 dhtml.properties >newdhtml.properties`

   `C:\jdk1.7.0_17\bin>native2ascii -encoding utf-8 server.properties >newserver.properties`

   **Note:** When you convert your property files to the same directory as the original ones you need give them new names instead of replacing the original in order to avoid problems.
7. Rename the original property files, you may want to modify them more at a later time.
8. Change the names of the generated property files back to the same names as the original property files: newcommon.properties to common.properties, newdhtml.properties to dhtml.properties, and newserver.properties to server.properties.
9. Restart Logi JReport Server.

**Naming criterion for language package folders**

\* FolderName(language)

\* FolderName(language-country)

\* FolderName(language-country-variant)

The folder name should be lower-case codes.

The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>.

The country argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.

The variant argument is a vendor or browser-specific code. For example, use win for Windows, mac for Macintosh, and posix for POSIX. Where there are two variants, separate them with an underscore, and put the more important one first.

## Specifying the Default Language Package

When the language packages are created, you can specify which of them will be applied to your server. There are two ways to specify the default language package:

There is an option [Specify Default Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Language) in the server profile for you to switch the language. The available language list depends on the language packages in `<server_install_root>\resources\server\languages`.

**To specify the language:**

* For administrators, on the Logi JReport Administration page, select **Profile** on the system toolbar, select **Customize Server Preferences** from the drop-down menu, then select the **Advanced** tab and set the default language for all users.
* For end users, on the Logi JReport Console page, select **Profile** on the system toolbar, then select **Customize Server Preferences** on the task bar of the Profile page, select the **Advanced** tab and set a language for themselves.

You can also control the language by the property jrs.language when accessing the Logi JReport Console page or Page Report Studio UI [via URLs](https://devnet.logianalytics.com/hc/en-us/articles/1500009650542-Working-with-Logi-JReport-Server-Guide-v15-Server#NLS).

**Note:** The specified language by URL property has higher priority than that specified by UI option; however, it takes effect only in the current user session.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating the Logi JReport Engine Language Resource Files

The Logi JReport Engine language resources are saved in the following files in the `<server_install_root>\resources\common\resource` directory: JRError.properties, JRMessage.properties, JVMessage.properties and JVMisc.properties. To create the files in a specified language, follow the steps below:

1. Save the files with new names which contain the ISO language and country code suffix in the same directory (for more information, see the above [naming criterion)](#Name). For example, if you want to create the French language files, save them as JRError\_fr\_FR.properties, JRMessage\_fr\_FR.properties, JVMessage\_fr\_FR.properties and JVMisc\_fr\_FR.properties.
2. Translate all the text after "=" in the newly saved files to French.
3. Save the files with UTF-8 encoding.
4. [Convert the contents](#Convert) in the files into Unicode and rename them to the original ones with the language and country suffix.
5. Restart Logi JReport Server.

Which language resource files will be applied depends on the language and locale settings of your system.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673841-National-Language-Support)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649142-NLS-at-Report-Level)
