---
title: "NLS at Application Level"
id: 1500009634421
section: "Applying National Language Support - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009634421-NLS-at-Application-Level
updated_at: 2021-07-24T16:03:52Z
---

# NLS at Application Level

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611362-Applying-National-Language-Support) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611382-NLS-at-Report-Level)

# NLS at Application Level

All the Logi Report Designer UI text and message related files are packaged in the file resource\_en\_US.jar (if Logi Report Designer is Chinese version, the file name is resource\_zh\_CN.jar) in `<install_root>\lib`. To make Logi Report Designer display in your required language, you just need to translate the needed files in this package.

The following takes French as an example to explain how to make Logi Report Designer display in another language.

1. Backup the file resource\_en\_US.jar in `<install_root>\lib`, then rename it to **resource\_fr\_FR.jar**.

   The name of the file must follow the format below: resource\_abbreviation of the language with lowercase\_abbreviation of the country using the language with uppercase.jar. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The locale argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
2. Open the newly saved file resource\_fr\_FR.jar, and you can find it contains two folders, META-INF and resource.
3. In the resource folder, open the following files one by one and translate the property values in the files to French, then save and close the files:
   * JWColorChooser.properties
   * JWFileChooser.properties
   * JWMessage.properties
   * JWMisc.properties
   * JWNLSPropertyValue.properties
   * JWObject.properties
   * JWObjectToolTip.properties
   * JWPropertyGroup.properties
   * JWToolTip.properties
4. Open the folder images in the resource folder, translate all text that can be translated in the image files, and save them. The file names cannot be changed.
5. Copy the folder uidescriptors in the resource folder to a specified place (for example, the Desktop), then open it. The folder contains a lot of .xml files.
6. right-click the file CatalogDoctorResource.xml in the uidescriptors folder and select **Edit** from the shortcut menu to open the file. The file contains some name properties. Translate their values to French, then save and close the file.
7. Translate the name property values in the following files as you do in the above step:
   * DataBrowser.xml
   * ReferenceEntityDialog.xml
   * MainMenu.xml
   * ToolBoxResource.xml
   * HelpLinkResource.xml
8. Translate the displayname property values in the following files as you do in [step 6](#Step7):
   * FormulaSpecialFieldsResource.xml
   * CrosstabFormulaFunctions.xml
   * FormulaFunctions.xml
   * FormulaOperators.xml
   * CTFormulaSpecialFieldsResource.xml
   * DynamicFormulaSpecialFieldsResource.xml
9. Translate the title, name, tooltip and text property values in the other .xml files except ComponentContainerRelationship.xml, GraphPanel.xml and the ones listed in [step 7](#Step7) and [step 8](#Step8) as you do in [step 6](#Step6).
10. After finishing the translation, copy the folder uidescriptors from the Desktop to the resource folder in resource\_fr\_FR.jar placed in `<install_root>\lib` to replace the original one.
11. Open the file **config.xml**`in <install_root>\bin`, and set the value of the property to **\_fr\_FR**. Make sure that Logi Report Designer is closed when you modify this file.

    The language name must follow the format below: abbreviation of the language with lowercase\_abbreviation of the country using the language with uppercase.jar. If the name format is not correct, Logi Report Designer will start with the default language.
12. Right-click the file Logi Report.bat in `<install_root>\bin` and select **Edit** from the shortcut menu to open the file, then change the name of the language package resource\_en\_US.jar to **resource\_fr\_FR.jar**.
13. Save the file. Then when you run Logi Report Designer, the UI text will be displayed in the specified language.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009611362-Applying-National-Language-Support) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611382-NLS-at-Report-Level)
