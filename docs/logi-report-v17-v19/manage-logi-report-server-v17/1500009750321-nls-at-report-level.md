---
title: "NLS at Report Level"
id: 1500009750321
section: "Manage Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750321-NLS-at-Report-Level
updated_at: 2021-07-25T07:18:55Z
---

# NLS at Report Level

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750301-NLS-at-Application-Level)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750241-Monitoring-Logi-Report-Server)

# NLS at Report Level

If the NLS feature is enabled for a report or library component when it is designed in Logi Report Designer, it will also be available after the report or library component is published to Logi Report Server. Then when the report or dashboard that contains the library component runs in the client/server scenario, different clients can select different languages to render it.

Logi Report Server also provides administrators with the NLS Editor in the server console with which they can edit NLS for any catalog, report, library component and dashboard. Besides, Logi Report Server administrators can create global NLS resources that can be shared and reused when editing NLS in both Logi Report Server and Logi Report Designer to reduce the translation cost.

Select the following links to view the topics:

* [Creating Global NLS](#Global)
* [Editing Local NLS](#Local)
* [Editing Resource Tree NLS](#Resource)
* [Running NLS Reports/Dashboards](#Run)
* [Localizing Page Navigation Links in HTML Report Outputs](#Link)

## Creating Global NLS

1. In the Logi Report Server console, point to **Administration** on the system toolbar, and then select **Language** > **Global NLS** from the drop-down menu to display the Global NLS page.

   ![Global NLS page](https://devnet.logianalytics.com/hc/article_attachments/4404936793879/nls_rpt_global.gif)
2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) above the Language box. The Select Language Source dialog box is then displayed.
3. Specify where to add the required languages.
   * **Languages Supported by Logi Report**  
      Adds languages from the languages that Logi Report supports.
   * **NLS Resource File**  
      Adds languages from an external NLS resource file which has been defined with some language information.

     NLS resource files should follow the naming rule: NLS\_[language]\_[region A2]\_[UserDefined].properties. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The region argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
4. Select **OK** in the Select Language Source dialog box. Then,
   * If Languages Supported by Logi Report is selected in the dialog box, Report Server will display the Add Language dialog box. Select the required languages and select **OK** to add them.
   * If NLS Resource File is selected in the dialog box, Report Server will display the File Upload dialog box. Browse to the local folder where the NLS resource file is located, select the file and then select **Open**.

   The specified languages are now displayed in the Language box in the Global NLS dialog box.
5. Select a language from the Language box to edit global NLS for it.
6. In the Display tab, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add a new row of display.

   ![Global NLS page - Display tab](https://devnet.logianalytics.com/hc/article_attachments/4404936794135/nls_rpt_global_dsply.gif)

   Select the type of the display from the Type drop-down list, which can be one of the following:

   * **Column**  
      This type is only for page reports running in Page Report Studio. It is the type of display text of columns.
   * **DisplayName**  
      Type of display text of object display name.
   * **Metadata**  
      Type of display text of metadata. Metadata mainly refers to catalog resources, such as table/view columns, business views, formulas, summaries, parameters, and so on.
   * **Label**  
      Type of display text of label, some web controls and UDOs.
   * **Prompt**  
      Type of display text of parameter prompt value.
   * **Title**  
      Type of display text of filter control, library component and objects in it.
   * **TOC**  
      Type of display text in the TOC tree.

   Then specify the key in the Key column and give the corresponding target language text in the Translation column. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add more rows and specify the key and translation according to your requirements. To remove a display row, select it and select **![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif)**.

   If some of the text cannot be displayed when you run the report in the target language, change the font face and font size of the text in the [Font](#Font) tab.
7. In the Format tab, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add a new row of format.

   ![Global NLS page - Format tab](https://devnet.logianalytics.com/hc/article_attachments/4404936794391/nls_rpt_global_fmt.gif)

   In the Key column, specify the format of the key in the original language, then in the Format column, specify the format of the key in the target language. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add more rows and specify the format information according to your requirements. To remove a format row, select it and select **![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif)**.
8. In the Font tab, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add a new row of font.

   ![Global NLS page - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404942499735/nls_rpt_global_font.gif)

   In the Key column, choose from the drop-down lists the font face and font size of the key, in the Font Face column, choose from the drop-down list the font face for the target language, then in the Font Size column, choose from the drop-down list the font size for the target language or select to use relative font size so that the font size can be adjusted according to the font size setting of the web browser. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add more rows and specify the font information according to your requirements. To remove a font row, select it and select **![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif)**.
9. Repeat the above steps to define global NLS for other languages.
10. Select **OK** to accept the settings.

## Editing Local NLS

Using the NLS Editor, administrators can translate a catalog, report, library component or dashboard into different languages from the original one.

1. In the Resources page of the server console, browse to the catalog/report/library component/dashboard for which you want to edit NLS, put the mouse pointer over the resource row and select its **NLS Editor** button ![NLS Editor button](https://devnet.logianalytics.com/hc/article_attachments/4404942499991/btn_srv_nlsedtr.gif) on the floating toolbar. The [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009720602-NLS-Editor) appears.

   ![NLS Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936794647/nlsedtr.gif)
2. Specify a report/component/dashboard if you are editing NLS for a report/library component/dashboard and catalog version as required.
3. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) above the Language box.
   * If you are editing NLS for a catalog, Report Server displays the [Select Language Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009747981-Select-Language-Source) dialog box. Specify where to add the required languages, then select **OK**.
     + If Languages Supported by Logi Report is selected in the dialog box, Report Server displays the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009747281-Add-Language) dialog box. Select the required languages and select **OK** to add them.
     + If NLS Resource File is selected in the dialog box, Report Server displays the File Upload dialog box. Browse to the local folder where the NLS resource file is located, select the file and then select **Open**.
   * If you are editing NLS for a report, library component or dashboard, Report Server displays the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009747281-Add-Language) dialog box. Select the languages in which you want the report/library component/dashboard to display, then select****OK**** to confirm and go back to the NLS Editor.
4. The selected languages are now listed in Language box of the NLS Editor dialog box. Select a target language from the box to edit NLS for it.
5. In the Display tab, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif), then in the [Add Display](https://devnet.logianalytics.com/hc/en-us/articles/1500009747241-Add-Display) dialog box, where all the display text in the catalog/report/library component/dashboard are listed, select the keys you want to translate and type the target language text for the keys in the Translate column, then select **OK**. The selected keys are now listed in the Display tab of the NLS Editor. You can further edit the translation for the keys here. Select **Add to Global NLS** to add the display information you just specify to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Report Server displays the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009747221-Add-to-Global-NLS#Display) dialog box for you to handle the duplication.

   If some of the text cannot be displayed when you run the report/library component/dashboard in the target language, change the font face and font size of the text in the [Font](#Font) tab.
6. Switch to the **Format** tab, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif), then in the [Add Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009720482-Add-Format) dialog box, where all the formats used in objects of the catalog/report/library component/dashboard are listed, select the keys you want to customize and provide the target language format for the keys in the Format column, then select **OK**. The selected keys are now listed in the Format tab of the NLS Editor. You can further edit the format for the keys here. Select **Add to Global NLS** to add the format information you just specify to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Report Server displays the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009747221-Add-to-Global-NLS#Format) dialog box for you to handle the duplication.
7. Select the **Font** tab, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif), then in the [Add Font](https://devnet.logianalytics.com/hc/en-us/articles/1500009747261-Add-Font) dialog box, where all the fonts used in objects of the catalog/report/library component/dashboard are listed, select the keys you want to customize and give the target language font face and font size for the keys in the Font Face and Font Size columns, then select **OK**. The selected keys are now listed in the Font tab of the NLS Editor. You can further edit the font face and font size for the keys here. Select **Add to Global NLS** to add the font information you just specify to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Report Server displays the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009747221-Add-to-Global-NLS#Font) dialog box for you to handle the duplication.
8. Select another language and edit NLS for it as shown above.
9. Select **OK** to accept the settings.

**Tip:** You can also edit NLS for a specific catalog/report/library component/dashboard version. To do this, in the Logi Report Server console, [access the version table of the resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009750201-Browsing-Versions), then select the **NLS Editor** link for the resource version.

**Notes:**

* The keys with default values will not be saved when you select the OK button in the NLS Editor.
* When you switch among different languages by choosing languages from the Language box, you may find that the text in the Translate column become unreadable. To resolve this problem, you can add `-Djreport.url.encoding=UTF-8` to the batch file that starts the server and then restart it. This changes the encoding to Unicode which supports all languages.
* The Add to Global NLS option is not available to [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/1500009751361-Multitenancy-Supported-via-Organizations#Orgadmin).
* You cannot edit NLS for [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009723142-Sharing-Reports). A shared report will apply the NLS settings of its original report.

## Editing Resource Tree NLS

With resource tree NLS, administrators can translate the names of all reports, library components and folders in the resource tree into different languages from the original one.

1. In the Logi Report Server console, point to **Administration** on the system toolbar, and then select **Language** > **Resource Tree NLS** from the drop-down menu to display the Resource Tree NLS page.

   ![Resource Tree NLS page](https://devnet.logianalytics.com/hc/article_attachments/4404936794903/nls_rpt_rsctree.gif)
2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) above the Language box. The Select Language Source dialog box is then displayed.
3. Specify where to add the required languages.
   * **Languages Supported by Logi Report**  
      Adds languages from the languages that Logi Report supports.
   * **NLS Resource File**  
      Adds languages from an external NLS resource file which has been defined with some language information.

     NLS resource files should follow the naming rule: NLS\_[language]\_[region A2]\_[UserDefined].properties. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The region argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
4. Select **OK** in the Select Language Source dialog box. Then,
   * If Languages Supported by Logi Report is selected in the dialog box, Report Server will display the Add Language dialog box. Select the required languages and select **OK** to add them.
   * If NLS Resource File is selected in the dialog box, in the displayed dialog box, browse to the local folder where the NLS resource file is located, select the file and then select **Open**.

   The specified languages are now displayed in the Language box in the Resource Tree NLS dialog box.
5. Select a language from the Language box to edit resource tree NLS for it.
6. The resource names are listed in the right panel. Give the corresponding target language text in the Translation column. You can make use of the search box to search for the Name and Translation items (wildcard search is not supported).
7. Select a folder to open resources in it. Give the corresponding target language text in the Translation column.

   When a new page is entered, the modifications you made on the last opened page will be saved automatically.
8. Repeat the above steps to define resource tree NLS for the other languages as required.
9. When done, select **OK** to accept the settings.
10. You can select **Export** button to export the resource tree NLS map to a resource tree NLS file in the specified location for further use. Only the resource tree of one translated language can be exported at a time and a user can only use the resource tree NLS file exported by himself.

**Notes:**

* The resource tree NLS takes effect only when the translated language is the same as the language specified for the option [Specify Default Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#Language) in the server profile or the browser language, and the former has higher priority.
* Resource tree NLS is not supported for resources from a real path.

## Running NLS Reports/Dashboards

When a report or library component is enabled with NLS in the Logi Report Server console by the administrator, or you have an NLS report or library component published to the server from Logi Report Designer, you can then run the report or dashboard that contains the library component in the specified languages.

Before running a report or dashboard, make sure you have the [Execute and/or Edit permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751241-Managing-Permissions) on it when it's in a public folder in the server resource tree.

**To directly run an NLS report/dashboard in a specified language:**

1. In the Logi Report Server console, point to **My Profile** on the system toolbar, then select  **Customize****Server Preferences** from the drop-down menu.
2. Select the **Advanced** tab, select **Enable NLS**  and choose the language from the Default Language drop-down list, in which you want the NLS report/dashboard to display by default, then select the corresponding encoding from the Default Encoding drop-down list.
3. Select **OK** to save the changes.
4. Select **Resources** on the system toolbar to switch to the Resources page.
5. Browse to the report/dashboard you want to run and select its name. The report result will then be displayed in the language you have specified.

**To run an NLS report in a specified language in Advanced mode:**

1. In the Resources page of the server console, browse to the report you want to run, put the mouse pointer over the report row and select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4404936766487/btn_srv_advrun.gif) on the floating toolbar.
2. In the Format tab, select the **Enable NLS** check box, choose the language from the Using Language drop-down list, then select the corresponding encoding from the Encoding drop-down list.
3. Finish the other related options and select **Finish** to run the report. The report result will then be run in the selected language.

**To schedule an NLS report to make it run in a specified language:**

1. In the Resources page of the server console, browse to the report you want to schedule, put the mouse pointer over the report row and select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404936747415/btn_schdl.gif) on the floating toolbar.
2. In the General tab, select the **Enable NLS** check box, then choose the language from the Using Language drop-down list, select the corresponding encoding from the Encoding drop-down list.
3. Finish the other related options and select **Finish** to perform the task. The report result will then be run in the selected language.

## Localizing Page Navigation Links in HTML Report Outputs

When you schedule to publish a report to HTML format, or run it in Advanced mode in HTML format, you can localize the names of page navigation links in the HTML report outputs, such as First, Previous, Next, and Last, according to your requirements.

The localizing process is divided into three steps:

1. [Create a property file for the desired language](#Create).
2. [Enable the language for the report](#Enable).
3. [Apply the localized link names to HTML report outputs](#Apply).

**Step 1: Creating the property file**

To localize the page navigation link names in HTML report outputs, a property file must be created first for the desired language. To do this:

1. Create the sub directories in `<server_install_root>\resources` as follows: <server\_install\_root>\resources\report\languages\[language-locale]\properties. For example, `C:\LogiReport\Server\resources\report\languages\zh-cn\properties`.

   See [Naming Criterion for Language Package Folders](https://devnet.logianalytics.com/hc/en-us/articles/1500009750301-NLS-at-Application-Level#Name)for more information about the naming criterion for language package folders.
2. Create a report.properties file in the properties directory.
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

   **Note:** For the line "4000107=@CurrentPageNumber; of @TotalPageNumber;", you just need to translate "of" to the desired language. In the HTML outputs, @CurrentPageNumber will be replaced by the current page number, and @TotalPageNumber by the report total page number.
5. Save the property file with UTF-8 encoding.
6. Copy the property file to the `<jdk_install_root>\bin` directory.

   **Note:** You can just add the `<jdk_install_root>\bin` directory to your PATH instead of copying the file.
7. Convert the contents in the property file into Unicode using native2ascii.exe in `<jdk_install_root>\bin` by running the following command:

   `C:\jdk1.8.0\bin>native2ascii -encoding utf-8 report.properties > newreport.properties`

   **Note:** When you convert your property file to the same directory as the original one, you need to give it a new name instead of replacing the original in order to avoid problems.
8. Delete report.properties in `<server_install_root>\resources\report\languages\[language-locale]\properties` and copy newreport.properties in `<jdk_install_root>\bin` to it, then rename the property file back to report.properties.

**Step 2: Enabling the language for the report**

When the property file is ready, the next step is to enable the language defined in the file for the required report.

1. In the Resources page of the Logi Report Server console, browse to the report and select the **NLS Editor** button ![NlS Editor button](https://devnet.logianalytics.com/hc/article_attachments/4404942499991/btn_srv_nlsedtr.gif) on the floating toolbar.
2. In the NLS Editor dialog box, specify a report and catalog version as required.
3. Select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) above the Language box, then in the Add Language dialog box, choose the specified language and select **OK**.
4. Select **OK** in the NLS Editor dialog box to confirm the settings.

Now the language will have been enabled for the report.

**Step 3: Applying the localized link names to HTML report outputs**

1. [Log onto the server console](https://devnet.logianalytics.com/hc/en-us/articles/1500009749881-Accessing-Logi-Report-Server-via-a-Web-Browser), go to the server resource tree in the Resources page and browse to the report.
2. Put the mouse pointer over the report row and select the **Advanced Run** button ![Advanced Run button](https://devnet.logianalytics.com/hc/article_attachments/4404936766487/btn_srv_advrun.gif) or **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404936747415/btn_schdl.gif) on the floating toolbar.
3. In the Format/General tab of the Advanced Run/Schedule dialog box, select **Enable NLS** and select the specified language from the Using Language drop-down list.
4. Specify the other settings and finish the task. Then in the generated HTML outputs, you can see that the page navigation links are displayed in the language you defined for the property file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009750301-NLS-at-Application-Level)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750241-Monitoring-Logi-Report-Server)
