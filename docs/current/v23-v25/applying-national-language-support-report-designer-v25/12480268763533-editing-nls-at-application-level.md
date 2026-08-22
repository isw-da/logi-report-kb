---
title: "Editing NLS at Application Level"
id: 12480268763533
section: "Applying National Language Support - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480268763533-Editing-NLS-at-Application-Level
updated_at: 2026-02-25T23:48:21Z
source_host: docs-report.zendesk.com
---
# 
Editing NLS at Application Level

All the Designer UI text and message related files are packaged in the file resource_en_US.jar in <install_root>\lib (for Designer of the Chinese version, the file name is resource_zh_CN.jar). To display Designer in your required language, you just need to translate the needed files in this package. This topic describes how you can translate Designer into another language, French for example.

- Backup the file resource_en_US.jar in <install_root>\lib, then rename it to resource_fr_FR.jar. The name of the file must follow this format: resource_language_country.jar.  Designer uses the two-letter codes of the language and country as defined by ISO-639 and ISO-3166 in the file name.
  

- Open the newly saved file resource_fr_FR.jar, and you can find it contains two folders: META-INF and resource. 

- Open the following files in the resource folder one by one and translate the property values in the files to French, then save and close the files.
- JWColorChooser.properties

- JWFileChooser.properties

- JWMessage.properties

- JWMisc.properties

- JWNLSPropertyValue.properties

- JWObject.properties

- JWObjectToolTip.properties

- JWPropertyGroup.properties

- JWToolTip.properties

- Open the folder images in the resource folder, translate all text that can be translated in the image files, and save them. You should not change the file names.

- Copy the folder uidescriptors in the resource folder to a specified location, the Desktop for example, then open it. The folder contains a lot of .xml files.

- 
Right-click the file CatalogDoctorResource.xml in the uidescriptors folder and select Edit from the shortcut menu. The file contains some name properties. Translate their values to French, then save and close the file.

- 
Translate values of the name property in the following XML files as described in the previous step.
- DataBrowser.xml

- ReferenceEntityDialog.xml

- MainMenu.xml

- ToolBoxResource.xml

- HelpLinkResource.xml

- 
Translate values of the displayname property in the following files as you do in step 6.
- FormulaSpecialFieldsResource.xml

- CrosstabFormulaFunctions.xml

- FormulaFunctions.xml

- FormulaOperators.xml

- CTFormulaSpecialFieldsResource.xml

- DynamicFormulaSpecialFieldsResource.xml

- Translate values of the title, name, tooltip, and text properties in the other .xml files except ComponentContainerRelationship.xml, GraphPanel.xml, and the ones listed in step 7 and step 8 as you do in step 6.

- After finishing the translation, copy the folder uidescriptors from where you have placed it,  the Desktop for example, to the resource folder in resource_fr_FR.jar in <install_root>\lib to replace the original one.

- Open the file config.xml in <install_root>\bin, and set the value of the property to _fr_FR. Make sure you do not start Designer  when you modify this file. The language name must follow this format: abbreviation of the language with lowercase_abbreviation of the country using the language with uppercase.jar. If the name format is not correct, Designer starts with the default language.     

- Right-click the file JReport.bat in <install_root>\bin, select Edit from the shortcut menu, then change the name of the language package resource_en_US.jar to resource_fr_FR.jar. Save the file. 

- Start Designer. The UI text now displays in French.
