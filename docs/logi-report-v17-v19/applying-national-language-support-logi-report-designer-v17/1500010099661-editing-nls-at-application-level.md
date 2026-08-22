---
title: "Editing NLS at Application Level"
id: 1500010099661
section: "Applying National Language Support - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099661-Editing-NLS-at-Application-Level
updated_at: 2021-07-23T19:16:17Z
---

# Editing NLS at Application Level

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099681-Editing-NLS-at-Report-Level)

# Editing NLS at Application Level

All the Designer UI text and message related files are packaged in the file resource\_en\_US.jar in `<install_root>\lib` (for Designer of the Chinese version, the file name is resource\_zh\_CN.jar). To make Designer display in your required language, you just need to translate the needed files in this package. This topic describes how you can translate Designer into another language, French for example.

1. Backup the file **resource\_en\_US.jar** in `<install_root>\lib`, then rename it to **resource\_fr\_FR.jar**.

   The name of the file must follow below format: *resource\_abbreviation* of the language with *lowercase\_abbreviation* of the country using the language with uppercase.jar. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The locale argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
2. Open the newly saved file resource\_fr\_FR.jar, and you can find it contains two folders: META-INF and resource.
3. In the **resource** folder, open the following files one by one and translate the property values in the files to French, then save and close the files:
   * JWColorChooser.properties
   * JWFileChooser.properties
   * JWMessage.properties
   * JWMisc.properties
   * JWNLSPropertyValue.properties
   * JWObject.properties
   * JWObjectToolTip.properties
   * JWPropertyGroup.properties
   * JWToolTip.properties
4. Open the folder **images** in the "resource" folder, translate all text that can be translated in the image files, and save them. You should not change the file names.
5. Copy the folder **uidescriptors** in the "resource" folder to a specified place, the Desktop for example, then open it. The folder contains a lot of .xml files.
6. Right-click the file **CatalogDoctorResource.xml** in the "uidescriptors" folder and select **Edit** from the shortcut menu to open the file. The file contains some name properties. Translate their values to French, then save and close the file.
7. Translate values of the **name** property in the following files as you do in the above step:
   * DataBrowser.xml
   * ReferenceEntityDialog.xml
   * MainMenu.xml
   * ToolBoxResource.xml
   * HelpLinkResource.xml
8. Translate values of the **displayname** property in the following files as you do in [step 6](#Step7):
   * FormulaSpecialFieldsResource.xml
   * CrosstabFormulaFunctions.xml
   * FormulaFunctions.xml
   * FormulaOperators.xml
   * CTFormulaSpecialFieldsResource.xml
   * DynamicFormulaSpecialFieldsResource.xml
9. Translate values of the **title**, **name**, **tooltip**, and **text** properties in the other .xml files except **ComponentContainerRelationship.xml**, **GraphPanel.xml**, and the ones listed in [step 7](#Step7) and [step 8](#Step8) as you do in [step 6](#Step6).
10. After finishing the translation, copy the folder **uidescriptors** from where you have placed, the Desktop for example, to the "resource" folder in resource\_fr\_FR.jar placed in `<install_root>\lib` to replace the original one.
11. Open the file **config.xml** in `<install_root>\bin`, and set the value of the property to **\_fr\_FR**. Make sure that you do not start Designer when you modify this file.

    The language name must follow below format : abbreviation of the language with *lowercase\_abbreviation* of the country using the language with uppercase.jar. If the name format is not correct, Designer starts with the default language.
12. Right-click the file **JReport.bat** in `<install_root>\bin` and select **Edit** from the shortcut menu to open the file, change the name of the language package **resource\_en\_US.jar** to **resource\_fr\_FR.jar**, then save the file.
13. Start Designer. The UI text now displays in French.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099641-Applying-National-Language-Support)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099681-Editing-NLS-at-Report-Level)
