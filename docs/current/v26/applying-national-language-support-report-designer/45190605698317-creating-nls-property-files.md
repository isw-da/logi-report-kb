---
title: "Creating NLS Property Files"
id: 45190605698317
section: "Applying National Language Support - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190605698317-Creating-NLS-Property-Files
updated_at: 2026-04-30T15:15:21Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Creating NLS Property Files

You can use the NLS Editor to create and edit NLS property files for your reports to display the reports in other languages. Using the NLS Editor, you can translate a report to any language, and modify the format, font size, and font face of the language. This topic describes how you can create NLS property files for a report.

When creating NLS property files for a report, you can use the report and catalog NLS resources, as well as the global NLS resources on Server. Then, when you publish the report to Server, Designer publishes the NLS property files to Server at the same time, thus Server can honor the user's locale settings and applies the appropriate language when users run the report. 

To create NLS property files for a report

- Open the report.

- Navigate to Home/View > Language > NLS Editor. Designer displays the NLS Editor dialog box.
    

- Select Add above the Language box.

- In the Add Language dialog box, select the languages in which you want to display the report and select OK. Designer then adds the languages to the Language box of the NLS Editor dialog box. 

- When you open the NLS Editor dialog box or a report for the first time, by default, Designer lists all the available report and catalog NLS resources in the Display, Format, and Font tabs of the NLS Editor dialog box. If you also want to use the global NLS resources on a started Server in the report, select Synchronize Global NLS with Server, Designer then gets the global NLS resources of the specified languages from the Server it connects to and displays them in the three tabs together with the report and catalog NLS resources (if Designer cannot automatically set up the connection to a started Server and sign you in, it displays the Connect to Report Server dialog box for you to specify the connection and user information first).

- Select a target language from the Language box to edit NLS information for it.

- In the Display tab, give the corresponding target language text for the keys in the Translate in <language> column.
    
- For any key, it may have three items with different scope: Global, Catalog, and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the translation specific for the report, edit the report scope item.

- When you have edited some display text keys for a specific language for a report, the next time you open the NLS Editor dialog box for the report to edit NLS for this language, Designer only displays the edited keys by default.

-  If you have edited some catalog scope display text keys for a language, when you use the NLS Editor dialog box to edit NLS for another report in the same catalog for this language, by default, Designer only lists the edited catalog scope display text keys for this language.

- To add more display text keys for a language, select Add above the key table, then in the  Add Display dialog box, specify the scope of the keys, select the required keys and select OK. 

- To delete a display text key, select it in the key table and select Remove.

 If some of the text cannot  display when you preview the report in the target language, change the font face and font size of the text in the Font tab.

- In the Format tab, provide the corresponding formats for the keys in the Format in <language> column for the target language.
    

- For any key, it may have three items with different scope: Global, Catalog, and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the format specific for the report, edit the report scope item.

- When you have edited some format keys for a specific language for a report, the next time you open the NLS Editor dialog box for the report to edit NLS for this language, Designer only displays the edited keys by default.

- If you have edited some catalog scope format keys  for a language, when you use the NLS Editor dialog box to edit NLS for another report in the same catalog for this language, by default, Designer only lists the edited catalog scope format keys  for this language.

- To add more format keys for a language, select Add above the key table, then in the Add Format dialog box, specify the scope of the keys, select the keys you need and select OK. 

- To delete a format key, select it in the key table and select Remove.

 To edit the format of the special fields "Page N of M" or "Global Page N of M", you should first edit its format too, for example, "Page <N> of <M>" or "Global Page <N> of <M>" in the Report Inspector. Then, in the Format tab of the NLS Editor dialog box, Designer adds a new line "Page <N> of <M>" or "Global Page <N> of <M>" and you can translate "Page", "of", "Global Page" into the language you want. You should format "N" and "M"  as "<N>" and "<M>" to avoid errors.

- 
In the Font tab, give the font face and font size for the keys in the Font Face and Font Size columns for the target language.
    

- For any key, it may have three items with different scope: Global, Catalog, and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the font properties specific for the report, edit the report scope item.

- When you have edited some font keys for a specific language for a report, the next time you open the NLS Editor dialog box for the report to edit NLS for this language, Designer only displays the edited keys by default.

- If you have edited some catalog scope font keys  for a language, when you use the NLS Editor dialog box to edit NLS for another report in the same catalog for this language, by default, Designer only lists the edited catalog scope font keys  for this language.

- To add more font keys for a language, select Add above the key table, then in the Add Font dialog box, specify the scope of the keys, select the keys you need and select OK. 

-  To delete a font key, select it in the key table and select Remove.

- Repeat the preceding steps to edit NLS for other languages.

- Select OK to save the settings and close the dialog box.

- For the same key, you can specify its NLS definition at three levels: global, catalog, and report. Among them, the global key has the lowest priority, and the report key has the highest priority. You cannot edit global NLS resources  in Designer. Only the Server administrators can edit global NLS resources on the Server Console.

- When the same key exists both in a catalog NLS resource and a report NLS resource and the translations at both levels are also the same, Designer automatically deletes the one from the report NLS resource after you select OK in the NLS Editor dialog box.

- When you have added some languages to the NLS Editor dialog box, Designer generates a set of NLS property files  in the directory where the current catalog exists according to the languages you have selected. One file is for one language with the name ReportName_language_country.properties. Designer uses the two-letter codes of the language and country as defined by ISO-639 and ISO-3166 in the NLS property file name. For example, the German NLS property file name for Report1 is Report1_de_DE.properties. The lowercase "de" indicates the language is German, and the uppercase "DE" indicates the country is Germany. If you want to use it for all countries speaking German, you can rename it to Report1_de.properties.
