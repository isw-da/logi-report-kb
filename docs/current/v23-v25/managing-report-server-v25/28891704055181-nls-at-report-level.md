---
title: "NLS at Report Level"
id: 28891704055181
section: "Managing Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891704055181-NLS-at-Report-Level
updated_at: 2026-02-26T02:13:35Z
source_host: docs-report.zendesk.com
---
# 
NLS at Report Level 

Report Server administrators can use the NLS Editor on the Server Console to edit NLS for any catalog, report, library component, and dashboard. Besides, Server administrators can create global NLS resources to share and reuse to reduce the translation cost. This topic describes how you can set NLS for reports.

If you have enabled the NLS feature for a report or library component when you designed it in Report Designer, NLS is also available after you published the report or library component to Report Server. Then when the report or dashboard that contains the library component runs in the client/server scenario, different clients can select different languages to render it.

This topic contains the following sections:

- Creating Global NLS
                

- Editing Local NLS
                

- Editing Resource Tree NLS
                

- Running NLS Reports/Dashboards
                

- Localizing Page Navigation Links in HTML Report Outputs
                

## 
Creating Global NLS

- On the system toolbar of the Server Console, navigate to Administration > Language > Global NLS. Server displays the Global NLS page. 
    

- Select the Export button to package and download all current Global NLS files into a zip file.

- Select the Import button to display the upload interface for importing NLS settings.

- Select the Add button  above the Language box. Server displays the Select Language Source dialog box.

- Specify where to get the languages that you want.
    
- 
Languages Supported by Report
          Select if you want to select a language from the languages that Report supports.

- 
NLS Resource File
        Select if you want to add a language from an external NLS resource file in which you have defined language information.
        NLS resource files should follow the naming rule: NLS_[language]_[region A2]_[UserDefined].properties. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at: http://www.loc.gov/standards/iso639-2/php/code_list.php. The region argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at: http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html.

- Select OK. Then,
    
- If you selected Languages Supported by Report, Server displays the Add Language dialog box. Select a language and select OK to add them.

- If you selected NLS Resource File, Server displays the Open dialog box. Browse to the local folder where the NLS resource file is, select the file, and then select Open.

Server displays the language that you selected in the Language box in the Global NLS dialog box.

- Select a language from the Language box to edit global NLS for it.

- In the Display tab, select the Add button  on the right to add a new row of display.
    

- Select the type of the display from the Type drop-down list, which can be one of the following:
- 
Column
      This type is only for page reports running in Page Report Studio. It is the type of display text of columns. 

- 
Display Name
      Type of display text of object display name.

- 
Metadata
      Type of display text of metadata. Metadata mainly refers to catalog resources, such as table/view columns, business views, formulas, summaries, and parameters.

- 
Label
      Type of display text of label, some web controls, and UDOs.

- 
Prompt
      Type of display text of parameter prompt value.

- 
Title
      Type of display text of filter control, library component, and objects in it.

- 
TOC
      Type of display text in the TOC tree.

- Specify the key in the Key column.

- Give the corresponding target language text in the Translation column. 

- Select the Add button  to add more rows and specify the key and translation. To remove a display row, select it and select the Remove button .If some of the text cannot display when you run the report in the target language, change the font face and font size of the text in the Font tab.

- In the Format tab, select the Add button  to add a new row of format.
    

- In the Key column, specify the format of the key in the original language. 

- In the Format column, specify the format of the key in the target language. 

- Select the Add button  to add more rows and specify the format information. To remove a format row, select it and select .

- 
In the Font tab, select the Add button  to add a new row of font.
    

- In the Key column, choose from the drop-down lists the font face and font size of the key.

- In the Font Face column, choose from the drop-down list the font face for the target language.

- In the Font Size column, choose from the drop-down list the font size for the target language. Or select Use Relative Font Size if you want the font size to adjust according to the font size setting of the web browser. 

- Select  to add more rows and specify the font information. To remove a font row, select it and select .

- Repeat the preceding steps to define global NLS for other languages.

- Select OK to accept the settings.

## 
Editing Local NLS

Using the NLS Editor, administrators can translate a catalog, report, library component, or dashboard into different languages from the original one.

- In the Resources page of the Server Console, browse to the catalog/report/library component/dashboard for which you want to edit NLS, put the mouse pointer over the resource row and select its NLS Editor button  on the floating toolbar. Server displays the NLS Editor.
    

- Select a version for the report/component/dashboard if you are editing NLS for it.

- Select a catalog version. 

- Select the Add button  above the Language box.
    
- If you are editing NLS for a catalog, Server displays the Select Language Source dialog box. Specify where to get the required language, then select OK.
          
- If you selected Languages Supported by Report in the dialog box, Server displays the Add Language dialog box. Select a language and select OK to add them.

- If you selected NLS Resource File in the dialog box, Server displays the Open dialog box. Browse to the local folder where the NLS resource file is, select the file, and then select Open.

- If you are editing NLS for a report, library component, or dashboard, Server displays the Add Language dialog box. Select the language in which you want the report/library component/dashboard to display, then selectOK to go back to the NLS Editor.

- Server lists the selected language in the Language box of the NLS Editor dialog box. Select a target language from the box to edit NLS for it.

- In the Display tab, select . Server displays the Add Display dialog box and lists all the display text in the catalog/report/library component/dashboard.

- Select the keys you want to translate. 

- Type the target language text for the keys in the Translate column. 

- Select OK. 

- Server lists the selected keys in the Display tab of the NLS Editor. You can further edit the translation for the keys here. 

- Select Add to Global NLS to add the display information you specified to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Server displays the Add to Global NLS dialog box for you to handle the duplication.
    If some of the text cannot display when you run the report/library component/dashboard in the target language, change the font face and font size of the text in the Font tab.

- Select the Format tab.

- Select . Server displays the Add Format dialog box and lists all the formats used in objects of the catalog/report/library component/dashboard.

- Select the keys you want to customize.

- Provide the target language format for the keys in the Format column.

- Select OK. 

- Server displays the selected keys in the Format tab of the NLS Editor. You can further edit the format for the keys here. 

- Select Add to Global NLS to add the format information you specified to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Server displays the Add to Global NLS dialog box for you to handle the duplication.

- 
Select the Font tab.

- Select the Add button . Server displays the Add Font dialog box and lists all the fonts used in objects of the catalog/report/library component/dashboard.

- Select the keys you want to customize.

- Give the target language font face and font size for the keys in the Font Face and Font Size columns.

- Select OK. 

- Server lists the selected keys in the Font tab of the NLS Editor. You can further edit the font face and font size for the keys here. 

- Select Add to Global NLS to add the font information you  specified to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, Server displays the Add to Global NLS dialog box for you to handle the duplication.

- Select another language and edit NLS for it as shown earlier.

- Select OK to accept the settings.

Tip: You can also edit NLS for a specific catalog/report/library component/dashboard version. To do this, on the Server Console, access the version table of the resource, then select the NLS Editor link for the resource version. 

- Server does not save the keys with default values when you selected OK in the NLS Editor.

- When you switch among different languages by choosing languages from the Language box, you may find that the text in the Translate column becomes unreadable. To resolve this problem, you can add -Djreport.url.encoding=UTF-8 to the batch file that starts the server and then restart it. This changes the encoding to Unicode which supports all languages. 

- The Add to Global NLS option is not available to organization admin.

- You cannot edit NLS for shared reports. A shared report applies the NLS settings of its original report.

## 
Editing Resource Tree NLS

With resource tree NLS, administrators can translate the names of all reports, library components, and folders in the resource tree into different languages from the original one.

- On the system toolbar of the Server Console, navigate to Administration > Language > Resource Tree NLS. Server displays the Resource Tree NLS page.
    

- Select the Add button  above the Language box. Server displays the Select Language Source dialog box.

- Specify where to get the required language.
    
- 
Languages Supported by Report
 Select if you want to select a language from the languages that Report supports.

- 
NLS Resource File
 Select if you want to add a language from an external NLS resource file in which you have defined language information.
        NLS resource files should follow the naming rule: NLS_[language]_[region A2]_[UserDefined].properties. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at http://www.loc.gov/standards/iso639-2/php/code_list.php. The region argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html.

- Select OK. Then,
    
- If you selected Languages Supported by Report in the dialog box, Server displays the Add Language dialog box. Select a language and select OK to add it.

- If you selected NLS Resource File in the dialog box, Server displays the Open dialog box. Browse to the local folder where the NLS resource file is, select the file, and then select Open.

Server displays the specified language in the Language box in the Resource Tree NLS dialog box.

- Select a language from the Language box to edit resource tree NLS for it.

- Server lists the resource names in the right panel. Give the corresponding target language text in the Translation column. 

- You can make use of the search box to search for the Name and Translation items (wildcard search is not supported).

- Select a folder to open resources in it. 

- Give the corresponding target language text in the Translation column.
    When you enter a new page, Server saves the modifications you made on the last opened page automatically. 

- Repeat the preceding steps to define resource tree NLS for the other languages.

- Select OK to accept the settings.

- You can select Export to export the resource tree NLS map to a resource tree NLS file in the specified location for further use. You can only export the resource tree of one translated language at a time and use the resource tree NLS file that you exported.

- The resource tree NLS takes effect only when the translated language is the same as the language that you specified for the option Specify Default Language in the server profile or the browser language, and the former has higher priority.

- You cannot set resource tree NLS for resources from a real path.

## 
Running NLS Reports/Dashboards

When you enabled a report or library component with NLS on the Server Console as an administrator, or published an NLS report or library component to Server from Designer, you can then run the report or dashboard that contains the library component in the specified languages.

Before running a report or dashboard, make sure you have the Execute and/or Edit permissions on it when it is in a public folder in the server resource tree. 

To directly run an NLS report/dashboard in a specified language:

- On the system toolbar of the Server Console, navigate to My Profile > Customize Server Preferences.

- Select the Advanced tab.

- Select Yes for Enable NLS.

- Choose the language from the Default Language drop-down list, in which you want the NLS report/dashboard to display by default.

- Select the corresponding encoding from the Default Encoding drop-down list.

- Select OK to save the changes. 

- Select Resources on the system toolbar to switch to the Resources page.

- Browse to the report/dashboard you want to run and select its name. Server displays the report in the language that you specified.

To run an NLS report in a specified language in Advanced mode:

- In the Resources page of the Server Console, browse to the report you want to run, put the mouse pointer over the report row and select the Advanced Run button  on the floating toolbar.

- Select the Format tab.

- Expand the Advanced node.

- Select Enable NLS.

- Choose the language from the Using Language drop-down list.

- Select the corresponding encoding from the Encoding drop-down list.

- Finish the other related settings and select Finish to run the report. Server then displays the report in the selected language.

To schedule an NLS report to run in a specified language:

- In the Resources page of the Server Console, browse to the report you want to schedule, put the mouse pointer over the report row and select the Schedule button  on the floating toolbar.

- In the General tab, expand the Advanced node.

- Select Enable NLS.

- Choose the language from the Using Language drop-down list.

- Select the corresponding encoding from the Encoding drop-down list. 

- Finish the other related options and select Finish to perform the task. Server then displays the report in the selected language.

## 
Localizing Page Navigation Links in HTML Report Outputs

When you schedule to publish a report to the HTML format, or run it in Advanced mode in HTML, you can localize the names of page navigation links in the HTML report outputs, such as First, Previous, Next, and Last.

The localizing process is divided into three steps:

- 
Create a property file for the language you want.

- 
Enable the language for the report.

- 
Apply the localized link names to HTML report outputs.

Step 1: Create the property file

To localize the page navigation link names in HTML report outputs, you should create a property file first for the language you want. To do this: 

- Create the sub directories in <server_install_root>\resources: <server_install_root>\resources\report\languages\[language-locale]\properties. For example, C:\LogiReport\Server\resources\report\languages\zh-cn\properties.
    See Naming Criterion for Language Package Folders for more information about the naming criterion for language package folders.

- Create a file report.properties in the properties directory.

- Open the property file and copy the following contents to it:
# The following is the report properties file format that can localize the link names in HTML.
4000101=First
4000102=Prev
4000103=Next
4000104=Last
4000105=Back
4000106=Refresh
4000107=@CurrentPageNumber; of @TotalPageNumber;

- Translate the text after = to the language specified by the folder name.
    For the line "4000107=@CurrentPageNumber; of @TotalPageNumber;", you just need to translate "of" to the language you want. In the HTML outputs, @CurrentPageNumber will be replaced by the current page number, and @TotalPageNumber by the report total page number.

- Save the property file with UTF-8 encoding.

- Copy the property file to the <jdk_install_root>\bin directory.
    You can just add the <jdk_install_root>\bin directory to your PATH instead of copying the file. 

- Convert the contents in the property file into Unicode using native2ascii.exe in <jdk_install_root>\bin by running the following command:
    C:\jdk1.8.0\bin>native2ascii -encoding utf-8 report.properties > newreport.properties

When you convert your property file to the same directory as the original one, you need to give it a new name instead of replacing the original to avoid problems.

- Delete report.properties from <server_install_root>\resources\report\languages\[language-locale]\properties.

- Copy newreport.properties in <jdk_install_root>\bin to <server_install_root>\resources\report\languages\[language-locale]\properties. 

- Rename the property file newreport.properties back to report.properties.

Step 2: Enable the language for the report

When the property file is ready, the next step is to enable the language defined in the file for the required report. 

- In the Resources page of the Server Console, browse to the report and select the NLS Editor button  on the floating toolbar. 

- In the NLS Editor dialog box, select a report and catalog version.

- Select the button  above the Language box. Server displays the Add Language dialog box.

- Choose the specified language.

- Select OK.

- Select OK in the NLS Editor dialog box to confirm the settings.

Server enables the language for the report.

Step 3: Apply the localized link names to HTML report outputs

- 
Sign in to the Server Console. 

- Go to the resource tree in the Resources page and browse to the report. 

- Put the mouse pointer over the report row and select the Advanced Run button  or Schedule button  on the floating toolbar.

- In the Format/General tab of the Advanced Run/Schedule dialog box, expand the Advanced node.

- Select Enable NLS.

- Select the specified language from the Using Language drop-down list.

- Specify the other settings and finish the task. Then in the generated HTML outputs, you can see that the page navigation links display in the language you defined for the property file.
