---
title: "Creating NLS Property Files"
id: 1500010061242
section: "Applying National Language Support - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010061242-Creating-NLS-Property-Files
updated_at: 2021-07-23T19:16:18Z
---

# Creating NLS Property Files

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061222-Mapping-Data-Values-to-Different-Languages)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061182-Using-the-Built-in-Functions-for-NLS)

# Creating NLS Property Files

You can use the NLS Editor to create and edit NLS property files for your reports in order to display the reports in other languages. Using the NLS Editor, you can translate any language, and modify the format, font size, and font face of the target language. This topic describes how you can create NLS property files for a report.

When creating NLS property files for a report, you can use the report and catalog NLS resources, as well as the NLS resources that are created on Server and can be used globally for all reports in Logi Report (for more information about global NLS, see Creating Global NLS in the *Logi Report Server Guide*). Then, when you publish the report to Server, Designer publishes the NLS property files to Server automatically at the same time; therefore, running the report on Server honors the user's locale settings and uses the appropriate language.

**To create NLS property files for a report:**

1. Open the report, then select **Home**/**View** > **Language** > **NLS Editor**. Designer displays the [NLS Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059882-NLS-Editor-Dialog-Box).

   ![NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404856862615/nlsedtr.gif)
2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) above the **Language** box.
3. In the [Add Language dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010057962-Add-Language-Dialog-Box), select the languages in which you want to display the report and select **OK**.

   ![Add Language dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848461591/addlng.gif)

   Designer then adds the selected languages to the Language box of the NLS Editor dialog box.
4. When you open the NLS Editor dialog box or a report for the first time, by default, Designer lists all the available report and catalog NLS resources in the Display, Format, and Font tabs of the NLS Editor dialog box. If you also want to use the global NLS resources created on a started Server in the report, select **Synchronize Global NLS with Server**, Designer then gets the global NLS resources defined for the selected languages from Server and displays them in the three tabs together with the report and catalog NLS resources (if Designer cannot automatically connect to Server and log you in, it displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the information for connecting with Server first).
5. Select a target language from the Language box to edit NLS information for it.
6. In the **Display** tab, give the corresponding target language text for the keys in the **Translate in *<language>*** column.

   For any key, it may have three items with different scope: Global, Catalog, and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the translation specific for the report, edit the report scope item.

   When you have edited some display text keys for a specific language for a report, the next time you open the NLS Editor dialog box for the report to edit NLS for this language, Designer only displays the edited keys by default.

   If you have edited some catalog scope display text keys for a language, when you use the NLS Editor dialog box to edit NLS for another report in the same catalog for this language, by default, Designer only lists the edited catalog scope display text keys for this language.

   To add more display text keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) above the key table, then in the [Add Display dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095441-Add-Display-Dialog-Box), specify the scope of the keys, select the required keys and select **OK**.

   ![Add Display dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856862999/adddsply.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If some of the text cannot display when you preview the report in the target language, change the font face and font size of the text in the [Font](#Font) tab.
7. In the **Format** tab, provide the corresponding formats for the keys in the **Format in *<language>*** column for the target language.

   ![NLS Editor - Format tab](https://devnet.logianalytics.com/hc/article_attachments/4404848461975/nls_rpt_prpty_fmt.gif)

   For any key, it may have three items with different scope: Global, Catalog, and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the format specific for the report, edit the report scope item.

   When you have edited some format keys for a specific language for a report, the next time you open the NLS Editor dialog box for the report to edit NLS for this language, Designer only displays the edited keys by default.

   If you have edited some catalog scope format keys for a language, when you use the NLS Editor dialog box to edit NLS for another report in the same catalog for this language, by default, Designer only lists the edited catalog scope format keys for this language.

   To add more format keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) above the key table, then in the [Add Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010057922-Add-Format-Dialog-Box), specify the scope of the keys, select the required keys and select **OK**.

   ![Add Format dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848462231/addfmt.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) To edit the format of the special fields "Page N of M" or "Global Page N of M", you should first edit its format too, for example, "Page <N> of <M>" or "Global Page <N> of <M>" in the Report Inspector. Then, in the Format tab of the NLS Editor dialog box, Designer adds a new line "Page <N> of <M>" or "Global Page <N> of <M>" and you can translate "Page", "of", "Global Page" into the desired language. You should format "N" and "M" as "<N>" and "<M>" in order to avoid errors.
8. In the **Font** tab, give the font face and font size for the keys in the **Font Face** and **Font Size** columns for the target language.

   ![NLS Editor - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404848462487/nls_rpt_prpty_font.gif)

   For any key, it may have three items with different scope: Global, Catalog, and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the font properties specific for the report, edit the report scope item.

   When you have edited some font keys for a specific language for a report, the next time you open the NLS Editor dialog box for the report to edit NLS for this language, Designer only displays the edited keys by default.

   If you have edited some catalog scope font keys for a language, when you use the NLS Editor dialog box to edit NLS for another report in the same catalog for this language, by default, Designer only lists the edited catalog scope font keys for this language.

   To add more font keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) above the key table, then in the [Add Font dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095481-Add-Font-Dialog-Box), specify the scope of the keys, select the required keys and select **OK**.

   ![Add Font dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856863511/addfont.gif)
9. Select another language and edit NLS for it as shown above.
10. Select **OK** to save the settings and close the dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* For the same key, you can specify its NLS definition at three levels: global, catalog, and report. Among them, the global key has the lowest priority, and the report key has the highest priority. You cannot edit global NLS resources in Designer. Only the Server administrators can edit global NLS resources in the Server Console.
* When the same key exists both in a catalog NLS resource and a report NLS resource and the translations at both levels are also the same, Designer automatically deletes the one from the report NLS resource after you select OK in the NLS Editor dialog box.
* When you have added some languages to the NLS Editor dialog box, Designer generates a set of NLS property files in the directory where the current catalog exists according to the languages you have selected. One file is for one language with the name "ReportName\_language\_locale.properties". Designer uses the abbreviations of the language and locale in the NLS property file name. For example, the German NLS property file name for Report1 is "Report1\_de\_DE.properties", which indicates the German language (de) is used in the German region (DE). If you want to use it for all German locales, you can rename it to "Report1\_de.properties".

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061222-Mapping-Data-Values-to-Different-Languages)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061182-Using-the-Built-in-Functions-for-NLS)
