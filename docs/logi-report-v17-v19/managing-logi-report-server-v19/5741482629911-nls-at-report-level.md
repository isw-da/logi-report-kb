---
title: "NLS at Report Level"
id: 5741482629911
section: "Managing Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741482629911-NLS-at-Report-Level
updated_at: 2022-10-31T17:18:12Z
---

# NLS at Report Level

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741474708887-NLS-at-Application-Level)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741468825239-Monitoring-Logi-Report-Server)

# NLS at Report Level

Logi Report Server administrators can use the NLS Editor on the Server Console to edit NLS for any catalog, report, library component, and dashboard. Besides, Server administrators can create global NLS resources to share and reuse to reduce the translation cost. This topic describes how you can set NLS for reports.

If you have enabled the NLS feature for a report or library component when you designed it in Logi Report Designer, NLS is also available after you published the report or library component to Logi Report Server. Then when the report or dashboard that contains the library component runs in the client/server scenario, different clients can select different languages to render it.

This topic contains the following sections:

* [Creating Global NLS](#Global)
* [Editing Local NLS](#Local)
* [Editing Resource Tree NLS](#Resource)
* [Running NLS Reports/Dashboards](#Run)
* [Localizing Page Navigation Links in HTML Report Outputs](#Link)

## Creating Global NLS

1. On the system toolbar of the Server Console, navigate to **Administration** > **Language** > **Global NLS**. Server displays the Global NLS page.

   ![Global NLS page](https://devnet.logianalytics.com/hc/article_attachments/9905675094295/nls_rpt_global.gif)
2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) above the **Language** box. Server displays the Select Language Source dialog box.
3. Specify where to get the languages that you want.
   * **Languages Supported by Logi Report**  
      Select if you want to select a language from the languages that Logi Report supports.
   * **NLS Resource File**  
      Select if you want to add a language from an external NLS resource file in which you have defined language information.

     NLS resource files should follow the naming rule: NLS\_[language]\_[region A2]\_[UserDefined].properties. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at: <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The region argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
4. Select **OK**. Then,
   * If you selected **Languages Supported by** Logi Report, Server displays the Add Language dialog box. Select a language and select **OK** to add them.
   * If you selected **NLS Resource File**, Server displays the Open dialog box. Browse to the local folder where the NLS resource file is, select the file, and then select **Open**.

   Server displays the language that you selected in the Language box in the Global NLS dialog box.
5. Select a language from the Language box to edit global NLS for it.
6. In the **Display** tab, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) on the right to add a new row of display.

   ![Global NLS page - Display tab](https://devnet.logianalytics.com/hc/article_attachments/9905675118871/nls_rpt_global_dsply.gif)
7. Select the type of the display from the **Type** drop-down list, which can be one of the following:
   * **Column**  
      This type is only for page reports running in Page Report Studio. It is the type of display text of columns.
   * **Display Name**  
      Type of display text of object display name.
   * **Metadata**  
      Type of display text of metadata. Metadata mainly refers to catalog resources, such as table/view columns, business views, formulas, summaries, and parameters.
   * **Label**  
      Type of display text of label, some web controls, and UDOs.
   * **Prompt**  
      Type of display text of parameter prompt value.
   * **Title**  
      Type of display text of filter control, library component, and objects in it.
   * **TOC**  
      Type of display text in the TOC tree.
8. Specify the key in the **Key** column.
9. Give the corresponding target language text in the **Translation** column.
10. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) to add more rows and specify the key and translation. To remove a display row, select it and select the **Remove** button **![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**.

    If some of the text cannot display when you run the report in the target language, change the font face and font size of the text in the [Font](#Font) tab.
11. In the **Format** tab, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) to add a new row of format.

    ![Global NLS page - Format tab](https://devnet.logianalytics.com/hc/article_attachments/9905675132823/nls_rpt_global_fmt.gif)
12. In the **Key** column, specify the format of the key in the original language.
13. In the **Format** column, specify the format of the key in the target language.
14. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) to add more rows and specify the format information. To remove a format row, select it and select **![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**.
15. In the **Font** tab, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) to add a new row of font.

    ![Global NLS page - Font tab](https://devnet.logianalytics.com/hc/article_attachments/9905713613975/nls_rpt_global_font.gif)
16. In the **Key** column, choose from the drop-down lists the font face and font size of the key.
17. In the **Font Face** column, choose from the drop-down list the font face for the target language.
18. In the **Font Size** column, choose from the drop-down list the font size for the target language. Or select **Use Relative Font Size** if you want the font size to adjust according to the font size setting of the web browser.
19. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) to add more rows and specify the font information. To remove a font row, select it and select **![Delete button](https://devnet.logianalytics.com/hc/article_attachments/9905578411927/btn_delete.gif)**.
20. Repeat the preceding steps to define global NLS for other languages.
21. Select **OK** to accept the settings.

## Editing Local NLS

Using the NLS Editor, administrators can translate a catalog, report, library component, or dashboard into different languages from the original one.

1. In the Resources page of the Server Console, browse to the catalog/report/library component/dashboard for which you want to edit NLS, put the mouse pointer over the resource row and select its **NLS Editor** button ![NLS Editor button](https://devnet.logianalytics.com/hc/article_attachments/9905675174807/btn_srv_nlsedtr.gif) on the floating toolbar. Server displays the [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/5741420821783-NLS-Editor-Dialog-Box-Properties).

   ![NLS Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/9905713659671/nlsedtr.gif)
2. Select a version for the report/component/dashboard if you are editing NLS for it.
3. Select a catalog version.
4. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) above the Language box.
   * If you are editing NLS for a catalog, Server displays the [Select Language Source](https://devnet.logianalytics.com/hc/en-us/articles/5741414956951-Select-Language-Source-Dialog-Box-Properties) dialog box. Specify where to get the required language, then select **OK**.
     + If you selected **Languages Supported by** Logi Report in the dialog box, Server displays the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/5741420483223-Add-Language-Dialog-Box-Properties) dialog box. Select a language and select **OK** to add them.
     + If you selected **NLS Resource File** in the dialog box, Server displays the Open dialog box. Browse to the local folder where the NLS resource file is, select the file, and then select **Open**.
   * If you are editing NLS for a report, library component, or dashboard, Server displays the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/5741420483223-Add-Language-Dialog-Box-Properties) dialog box. Select the language in which you want the report/library component/dashboard to display, then select****OK**** to go back to the NLS Editor.
5. Server lists the selected language in the **Language** box of the NLS Editor dialog box. Select a target language from the box to edit NLS for it.
6. In the **Display** tab, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif). Server displays the [Add Display](https://devnet.logianalytics.com/hc/en-us/articles/5741432706711-Add-Display-Dialog-Box-Properties) dialog box and lists all the display text in the catalog/report/library component/dashboard.
7. Select the keys you want to translate.
8. Type the target language text for the keys in the **Translate** column.
9. Select **OK**.
10. Server lists the selected keys in the **Display** tab of the NLS Editor. You can further edit the translation for the keys here.
11. Select **Add to Global NLS** to add the display information you specified to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Server displays the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741405515287-Add-to-Global-NLS-Dialog-Box-Properties#Display) dialog box for you to handle the duplication.

    If some of the text cannot display when you run the report/library component/dashboard in the target language, change the font face and font size of the text in the [Font](#Font) tab.
12. Select the **Format** tab.
13. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif). Server displays the [Add Format](https://devnet.logianalytics.com/hc/en-us/articles/5741420443927-Add-Format-Dialog-Box-Properties) dialog box and lists all the formats used in objects of the catalog/report/library component/dashboard.
14. Select the keys you want to customize.
15. Provide the target language format for the keys in the **Format** column.
16. Select **OK**.
17. Server displays the selected keys in the **Format** tab of the NLS Editor. You can further edit the format for the keys here.
18. Select **Add to Global NLS** to add the format information you specified to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Server displays the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741405515287-Add-to-Global-NLS-Dialog-Box-Properties#Format) dialog box for you to handle the duplication.
19. Select the **Font** tab.
20. Select the Add button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif). Server displays the [Add Font](https://devnet.logianalytics.com/hc/en-us/articles/5741442248727-Add-Font-Dialog-Box-Properties) dialog box and lists all the fonts used in objects of the catalog/report/library component/dashboard.
21. Select the keys you want to customize.
22. Give the target language font face and font size for the keys in the **Font Face** and **Font Size** columns.
23. Select **OK**.
24. Server lists the selected keys in the **Font** tab of the NLS Editor. You can further edit the font face and font size for the keys here.
25. Select **Add to Global NLS** to add the font information you specified to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Server displays the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/5741405515287-Add-to-Global-NLS-Dialog-Box-Properties#Font) dialog box for you to handle the duplication.
26. Select another language and edit NLS for it as shown earlier.
27. Select **OK** to accept the settings.

**Tip:** You can also edit NLS for a specific catalog/report/library component/dashboard version. To do this, on the Server Console, [access the version table of the resource](https://devnet.logianalytics.com/hc/en-us/articles/5741462114583-Browsing-Versions), then select the **NLS Editor** link for the resource version.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* Server does not save the keys with default values when you selected **OK** in the NLS Editor.
* When you switch among different languages by choosing languages from the **Language** box, you may find that the text in the **Translate** column becomes unreadable. To resolve this problem, you can add `-Djreport.url.encoding=UTF-8` to the batch file that starts the server and then restart it. This changes the encoding to Unicode which supports all languages.
* The **Add to Global NLS** option is not available to [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/5741463905047-Multitenancy-Supported-via-Organizations#Orgadmin).
* You cannot edit NLS for [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/5741461964439-Sharing-Web-Reports). A shared report applies the NLS settings of its original report.

## Editing Resource Tree NLS

With resource tree NLS, administrators can translate the names of all reports, library components, and folders in the resource tree into different languages from the original one.

1. On the system toolbar of the Server Console, navigate to **Administration** > **Language** > **Resource Tree NLS**. Server displays the Resource Tree NLS page.

   ![Resource Tree NLS page](https://devnet.logianalytics.com/hc/article_attachments/9905675234455/nls_rpt_rsctree.gif)
2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) above the **Language** box. Server displays the Select Language Source dialog box.
3. Specify where to get the required language.
   * **Languages Supported by Logi Report**  
      Select if you want to select a language from the languages that Logi Report supports.
   * **NLS Resource File**  
      Select if you want to add a language from an external NLS resource file in which you have defined language information.

     NLS resource files should follow the naming rule: NLS\_[language]\_[region A2]\_[UserDefined].properties. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The region argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
4. Select **OK**. Then,
   * If you selected **Languages Supported by** Logi Report in the dialog box, Server displays the Add Language dialog box. Select a language and select **OK** to add it.
   * If you selected **NLS Resource File** in the dialog box, Server displays the Open dialog box. Browse to the local folder where the NLS resource file is, select the file, and then select **Open**.

   Server displays the specified language in the **Language** box in the Resource Tree NLS dialog box.
5. Select a language from the **Language** box to edit resource tree NLS for it.
6. Server lists the resource names in the right panel. Give the corresponding target language text in the **Translation** column.
7. You can make use of the search box to search for the Name and Translation items (wildcard search is not supported).
8. Select a folder to open resources in it.
9. Give the corresponding target language text in the **Translation** column.

   When you enter a new page, Server saves the modifications you made on the last opened page automatically.
10. Repeat the preceding steps to define resource tree NLS for the other languages.
11. Select **OK** to accept the settings.
12. You can select **Export** to export the resource tree NLS map to a resource tree NLS file in the specified location for further use. You can only export the resource tree of one translated language at a time and use the resource tree NLS file that you exported.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* The resource tree NLS takes effect only when the translated language is the same as the language that you specified for the option [Specify Default Language](https://devnet.logianalytics.com/hc/en-us/articles/5741409420567-Configuring-Server-Profile#Language) in the server profile or the browser language, and the former has higher priority.
* You cannot set resource tree NLS for resources from a real path.

## Running NLS Reports/Dashboards

When you enabled a report or library component with NLS on the Server Console as an administrator, or published an NLS report or library component to Server from Designer, you can then run the report or dashboard that contains the library component in the specified languages.

Before running a report or dashboard, make sure you have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/5741463668119-Managing-Permissions) on it when it is in a public folder in the server resource tree.

**To directly run an NLS report/dashboard in a specified language:**

1. On the system toolbar of the Server Console, navigate to **My Profile** > **Customize** **Server Preferences**.
2. Select the **Advanced** tab.
3. Select **Yes** for **Enable NLS**.
4. Choose the language from the **Default Language** drop-down list, in which you want the NLS report/dashboard to display by default.
5. Select the corresponding encoding from the **Default Encoding** drop-down list.
6. Select **OK** to save the changes.
7. Select **Resources** on the system toolbar to switch to the Resources page.
8. Browse to the report/dashboard you want to run and select its name. Server displays the report in the language that you specified.

**To run an NLS report in a specified language in Advanced mode:**

1. In the Resources page of the Server Console, browse to the report you want to run, put the mouse pointer over the report row and select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/9905637152919/btn_srv_advrun.gif) on the floating toolbar.
2. Select the **Format** tab.
3. Expand the **Advanced** node.
4. Select **Enable NLS**.
5. Choose the language from the **Using Language** drop-down list.
6. Select the corresponding encoding from the **Encoding** drop-down list.
7. Finish the other related settings and select **Finish** to run the report. Server then displays the report in the selected language.

**To schedule an NLS report to run in a specified language:**

1. In the Resources page of the Server Console, browse to the report you want to schedule, put the mouse pointer over the report row and select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/9905654855063/btn_schdl.gif) on the floating toolbar.
2. In the **General** tab, expand the **Advanced** node.
3. Select **Enable NLS**.
4. Choose the language from the **Using Language** drop-down list.
5. Select the corresponding encoding from the **Encoding** drop-down list.
6. Finish the other related options and select **Finish** to perform the task. Server then displays the report in the selected language.

## Localizing Page Navigation Links in HTML Report Outputs

When you schedule to publish a report to the HTML format, or run it in Advanced mode in HTML, you can localize the names of page navigation links in the HTML report outputs, such as First, Previous, Next, and Last.

The localizing process is divided into three steps:

1. [Create a property file for the language](#Create) you want.
2. [Enable the language for the report](#Enable).
3. [Apply the localized link names to HTML report outputs](#Apply).

**Step 1: Create the property file**

To localize the page navigation link names in HTML report outputs, you should create a property file first for the language you want. To do this:

1. Create the sub directories in `<server_install_root>\resources`: <server\_install\_root>\resources\report\languages\[language-locale]\properties. For example, `C:\LogiReport\Server\resources\report\languages\zh-cn\properties`.

   See [Naming Criterion for Language Package Folders](https://devnet.logianalytics.com/hc/en-us/articles/5741474708887-NLS-at-Application-Level#Name) for more information about the naming criterion for language package folders.
2. Create a file **report.properties** in the **properties** directory.
3. Open the property file and copy the following contents to it:

   `# The following is the report properties file format that can localize the link names in HTML.  
   4000101=First  
   4000102=Prev  
   4000103=Next  
   4000104=Last  
   4000105=Back  
   4000106=Refresh  
   4000107=@CurrentPageNumber; of @TotalPageNumber;`
4. Translate the text after = to the language specified by the folder name.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)For the line "4000107=@CurrentPageNumber; of @TotalPageNumber;", you just need to translate "of" to the language you want. In the HTML outputs, @CurrentPageNumber will be replaced by the current page number, and @TotalPageNumber by the report total page number.
5. Save the property file with UTF-8 encoding.
6. Copy the property file to the `<jdk_install_root>\bin` directory.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)You can just add the `<jdk_install_root>\bin` directory to your PATH instead of copying the file.
7. Convert the contents in the property file into Unicode using **native2ascii.exe** in `<jdk_install_root>\bin` by running the following command:

   `C:\jdk1.8.0\bin>native2ascii -encoding utf-8 report.properties > newreport.properties`

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)When you convert your property file to the same directory as the original one, you need to give it a new name instead of replacing the original to avoid problems.
8. Delete **report.properties** from `<server_install_root>\resources\report\languages\[language-locale]\properties`.
9. Copy **newreport.properties** in `<jdk_install_root>\bin` to `<server_install_root>\resources\report\languages\[language-locale]\properties`.
10. Rename the property file **newreport.properties** back to **report.properties**.

**Step 2: Enable the language for the report**

When the property file is ready, the next step is to enable the language defined in the file for the required report.

1. In the Resources page of the Server Console, browse to the report and select the **NLS Editor** button ![NlS Editor button](https://devnet.logianalytics.com/hc/article_attachments/9905675174807/btn_srv_nlsedtr.gif) on the floating toolbar.
2. In the NLS Editor dialog box, select a report and catalog version.
3. Select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905619223831/btn_add1.gif) above the Language box. Server displays the Add Language dialog box.
4. Choose the specified language.
5. Select **OK**.
6. Select **OK** in the NLS Editor dialog box to confirm the settings.

Server enables the language for the report.

**Step 3: Apply the localized link names to HTML report outputs**

1. [Sign in to the Server Console](https://devnet.logianalytics.com/hc/en-us/articles/5741461387031-Accessing-Logi-Report-Server-via-a-Web-Browser).
2. Go to the resource tree in the Resources page and browse to the report.
3. Put the mouse pointer over the report row and select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/9905637152919/btn_srv_advrun.gif) or **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/9905654855063/btn_schdl.gif) on the floating toolbar.
4. In the Format/General tab of the Advanced Run/Schedule dialog box, expand the **Advanced** node.
5. Select **Enable NLS**.
6. Select the specified language from the **Using Language** drop-down list.
7. Specify the other settings and finish the task. Then in the generated HTML outputs, you can see that the page navigation links display in the language you defined for the property file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741474708887-NLS-at-Application-Level)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741468825239-Monitoring-Logi-Report-Server)
