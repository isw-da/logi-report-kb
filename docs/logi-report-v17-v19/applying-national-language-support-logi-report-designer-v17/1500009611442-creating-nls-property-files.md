---
title: "Creating NLS Property Files"
id: 1500009611442
section: "Applying National Language Support - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009611442-Creating-NLS-Property-Files
updated_at: 2021-07-24T16:03:51Z
---

# Creating NLS Property Files

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634461-Mapping-Data-Values-to-Different-Languages) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611422-Built-in-Functions-for-NLS)

# Creating NLS Property Files

The NLS Editor is used to create and edit NLS property files for reports. With the NLS Editor, you can translate the language, and modify the format, font size and font face of the target language.

You can create NLS property files for a report by using the report and catalog NLS resources, or by using NLS resources that are created on Logi Report Server and can be used globally for all reports in Logi Report. For details about global NLS, refer to Creating Global NLS in the *Logi Report Server Guide*.

When you publish the reports to Logi Report Server the NLS property files will automatically be published to Logi Report Server as well so running the reports on Logi Report Server will honor the user's locale settings and use the appropriate language.

**To create NLS property files for a report:**

1. Open the report, then select **Home**/**View** > **Language** > **NLS Editor**. The [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009632541-NLS-Editor-Dialog) appears.

   ![NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904216727/nlsedtr.gif)
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the Language box to display the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009607122-Add-Language-Dialog) dialog.

   ![Add Language dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904216983/addlng.gif)
3. Select the required languages in which you want the report to display, then select **OK**. The selected languages are now listed in the Language box of the NLS Editor.
4. When you open the NLS Editor for a report for the first time, by default, all the available report and catalog NLS resources are listed in the Display, Format and Font tabs of the NLS Editor. If you also want to use the global NLS resources created on a started Logi Report Server in the report, select **Synchronize Global NLS with Server**, Logi Report Designer will then get the global NLS resources defined for the selected languages from the server and display them in the Display, Format and Font tabs together with the report and catalog NLS resources (if Logi Report Designer cannot automatically connect to the server and log you in, you will be prompted with the [Connect to Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009607442-Connect-to-Logi-Report-Server-Dialog) dialog to specify the properties for connecting with the server first).
5. Select a target language from the Language box to edit NLS information for it.
6. In the Display tab, give the corresponding target language text for the keys in the Translate in <language> column.

   For any key, it may have three items with different scope: Global, Catalog and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the translation specific for the report, edit the report scope item.

   When you have edited some display text keys for a specific language for a report, the next time you open the NLS Editor for the report to edit NLS for this language, only the edited keys are displayed by default.

   If some catalog scope display text keys are edited for a language, when you use the NLS Editor to edit NLS for another report in the same catalog for this language, by default only the edited catalog scope display text keys are listed for this language.

   To add more display text keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the key table, then in the [Add Display](https://devnet.logianalytics.com/hc/en-us/articles/1500009629761-Add-Display-Dialog) dialog, specify the scope of the keys to be shown in the Available Display table, select the required keys and select **OK**.

   ![Add Display dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911658775/adddsply.gif)

   To remove any display text key, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) above the key table. You can select multiple keys and remove them at a time.

   If some of the text cannot be displayed when you preview the report in the target language, change the font face and font size of the text in the [Font](#Font) tab.
7. In the Format tab, provide the corresponding formats for the keys in the Format in <language> column for the target language.

   ![NLS Editor - Format tab](https://devnet.logianalytics.com/hc/article_attachments/4404911659031/nls_rpt_prpty_fmt.gif)

   For any key, it may have three items with different scope: Global, Catalog and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the format specific for the report, edit the report scope item.

   When you have edited some format keys for a specific language for a report, the next time you open the NLS Editor for the report to edit NLS for this language, only the edited keys are displayed by default.

   If some catalog scope format keys are edited for a language, when you use the NLS Editor to edit NLS for another report in the same catalog for this language, by default only the edited catalog scope format keys are listed for this language.

   To add more format keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the key table, then in the [Add Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009629801-Add-Format-Dialog) dialog, specify the scope of the keys to be shown in the Available Format table, select the required keys and select **OK**.

   ![Add Format dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911659543/addfmt.gif)

   To remove any format key, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) above the key table. You can select multiple keys and remove them at a time.

   **Note:** To edit the format of the special fields Page N of M or Global Page N of M, you should first edit its format too, for example, Page <N> of <M> or Global Page <N> of <M> in the Report Inspector, and then in the Format tab of the NLS Editor dialog, a new line Page <N> of <M> or Global Page <N> of <M> will be listed and you can translate Page, of, Global Page into the desired language. N and M must be formatted as <N> and <M> in order to avoid errors.
8. In the Font tab, give the font face and font size for the keys in the Font Face and Font Size columns for the target language.

   ![NLS Editor - Font tab](https://devnet.logianalytics.com/hc/article_attachments/4404911659799/nls_rpt_prpty_font.gif)

   For any key, it may have three items with different scope: Global, Catalog and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the font properties specific for the report, edit the report scope item.

   When you have edited some font keys for a specific language for a report, the next time you open the NLS Editor for the report to edit NLS for this language, only the edited keys are displayed by default.

   If some catalog scope font keys are edited for a language, when you use the NLS Editor to edit NLS for another report in the same catalog for this language, by default only the edited catalog scope font keys are listed for this language.

   To add more font keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the key table, then in the [Add Font](https://devnet.logianalytics.com/hc/en-us/articles/1500009629821-Add-Font-Dialog) dialog, specify the scope of the keys to be shown in the Available Font table, select the required keys and select **OK**.

   ![Add Font dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911660055/addfont.gif)

   To remove any font key, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif) above the key table. You can select multiple keys and remove them all at the same time.
9. Select another language and edit NLS for it as shown above.
10. Select **OK** to save the settings and close the dialog.

**Notes:**

* For the same key, its NLS definition can be specified at three level: global, catalog and report. Among them, the global has the lowest priority, and the report has the highest priority. Global NLS resources cannot be edited in Logi Report Designer, they can only be edited in Logi Report Server.
* When the same key exists both in a catalog NLS resource and a report NLS resource and the translations at both levels are also the same, the one from the report NLS resource will be automatically deleted after selecting OK in the NLS Editor.
* When you have added some languages to the NLS Editor, a set of NLS property files will be generated in the directory where the current catalog exists according to the languages you have selected. One file is for one language with the name ReportName\_language\_locale.properties. The abbreviations of the language and locale are used in the NLS property file name. For example, the German NLS property file name for Report1 will be like this: Report1\_de\_DE.properties. This means the German language (de) as used in the German region (DE). If you want to use it for all German locales you can rename it just Report1\_de.properties.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009634461-Mapping-Data-Values-to-Different-Languages) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009611422-Built-in-Functions-for-NLS)
