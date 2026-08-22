---
title: "Creating NLS Property Files"
id: 1500009568562
section: "Applying National Language Support - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568562-Creating-NLS-Property-Files
updated_at: 2021-07-24T05:54:31Z
---

# Creating NLS Property Files

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590001-Mapping-Data-Values-to-Different-Languages)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589981-Built-in-Functions-for-NLS)

# Creating NLS Property Files

The [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009566782-NLS-Editor-Dialog) is used to create and edit NLS property files for reports. With the NLS Editor, you can translate the language, and modify the format, font size and font face of the target language.

You can create NLS property files for a report by using the report and catalog NLS resources, or by using NLS resources that are created on Logi JReport Server and can be used globally for all reports in Logi JReport. For details about global NLS, see Creating Global NLS for Reports in the *Logi JReport Server User's Guide*.

When you publish the reports to Logi JReport Server the NLS property files will automatically be published to Logi JReport Server as well so running the reports on Logi JReport Server will honor the user's locale settings and use the appropriate language.

**To create NLS property files for a report:**

1. Open the report, then select **Home**/**View** > **Language** > **NLS Editor**. The [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009566782-NLS-Editor-Dialog) appears.

   ![NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404893830167/nlsedtr.gif)
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the Language box to display the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009564462-Add-Language-Dialog) dialog.

   ![Add Language dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893830423/addlng.gif)
3. Select the required languages in which you want the report to display, then select **OK**. The selected languages are now listed in the Language box of the NLS Editor.
4. When you open the NLS Editor for a report for the first time, by default, all the available report and catalog NLS resources are listed in the Display, Format and Font tabs of the NLS Editor. If you also want to use the global NLS resources created on Logi JReport Server in the report, select **Synchronize Global NLS with Server**. The Connect to Logi JReport Server dialog appears.

   ![Connect to Logi JReport Server dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893818519/connect.gif)
5. Type in the host and port of the remote Logi JReport Server in the Host and Port text fields.
6. When using a standalone server, enter **/jrserver** in the Servlet Path text field or the context root of your web application if deployed as a war or ear fie such as **/Logi JReport/jrserver**.
7. If the server has been integrated with another web server that supports SSL, select the **SSL** (Security Socket Layer) checkbox to create an SSL connection.
8. Check **Remember connection information**  to enable Logi JReport Designer to remember the connection information.
9. Provide the user name and password of the server. When the Organization feature is enabled and when the user is an organization user, User Name should include the organization name. Use \ to separate the organization name and the user name, for example, org1\user1.
10. Select **Connect**. The global NLS resources defined for the selected languages are now displayed in the Display, Format and Font tabs together with the report and catalog NLS resources.
11. Select a target language from the Language box to edit NLS information for it.
12. In the Display tab, give the corresponding target language text for the keys in the Translate in <language> column. Use the quick search toolbar to locate the desired keys if needed.

    For any key, it may have three items with different scope: Global, Catalog and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the translation specific for the report, edit the report scope item.

    When you have edited some display text keys for a specific language for a report, the next time you open the NLS Editor for the report to edit NLS for this language, only the edited keys are displayed by default.

    If some catalog scope display text keys are edited for a language, when you use the NLS Editor to edit NLS for another report in the same catalog for this language, by default only the edited catalog scope display text keys are listed for this language.

    To add more display text keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the key table, then in the [Add Display](https://devnet.logianalytics.com/hc/en-us/articles/1500009564422-Add-Display-Dialog) dialog, specify the scope of the keys to be shown in the Available Display table, select the required keys and select **OK**. Use the quick search toolbar to locate the desired keys if needed.

    ![Add Display dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889303447/adddsply.gif)

    To remove any display text key, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) above the key table. You can select multiple keys and remove them at a time.
13. In the Format tab, provide the corresponding formats for the keys in the Format in <language> column for the target language. Use the quick search toolbar to locate the desired keys if needed.

    ![NLS Editor - Format](https://devnet.logianalytics.com/hc/article_attachments/4404889303703/nls_rpt_prpty_fmt.gif)

    For any key, it may have three items with different scope: Global, Catalog and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the format specific for the report, edit the report scope item.

    When you have edited some format keys for a specific language for a report, the next time you open the NLS Editor for the report to edit NLS for this language, only the edited keys are displayed by default.

    If some catalog scope format keys are edited for a language, when you use the NLS Editor to edit NLS for another report in the same catalog for this language, by default only the edited catalog scope format keys are listed for this language.

    To add more format keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the key table, then in the [Add Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009585541-Add-Format-Dialog) dialog, specify the scope of the keys to be shown in the Available Format table, select the required keys and select **OK**. Use the quick search toolbar to locate the desired keys if needed.

    ![Add Format dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893830679/addfmt.gif)

    To remove any format key, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) above the key table. You can select multiple keys and remove them at a time.

    **Note:** To edit the format of the special fields Page N of M or Global Page N of M, you should first edit its format too, for example, Page <N> of <M> or Global Page <N> of <M> in the Report Inspector, and then in the Format tab of the NLS Editor dialog, a new line Page <N> of <M> or Global Page <N> of <M> will be listed and you can translate Page, of, Global Page into the desired language. N and M must be formatted as <N> and <M> in order to avoid errors.
14. In the Font tab, give the font face and font size for the keys in the Font Face and Font Size columns for the target language. Use the quick search toolbar to locate the desired keys if needed.

    ![NLS Editor - Font](https://devnet.logianalytics.com/hc/article_attachments/4404893830935/nls_rpt_prpty_font.gif)

    For any key, it may have three items with different scope: Global, Catalog and Report. If you want to use the global NLS definition for the key, leave its report and catalog scope items unchanged. If you edit the catalog scope item for the key, the definition can be used by all reports in the current catalog for the same language. To make the font properties specific for the report, edit the report scope item.

    When you have edited some font keys for a specific language for a report, the next time you open the NLS Editor for the report to edit NLS for this language, only the edited keys are displayed by default.

    If some catalog scope font keys are edited for a language, when you use the NLS Editor to edit NLS for another report in the same catalog for this language, by default only the edited catalog scope font keys are listed for this language.

    To add more font keys for a language, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the key table, then in the [Add Font](https://devnet.logianalytics.com/hc/en-us/articles/1500009564442-Add-Font-Dialog) dialog, specify the scope of the keys to be shown in the Available Font table, select the required keys and select **OK**.

    ![Add Font dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889303959/addfont.gif)

    To remove any format key, select it and select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) above the key table. You can select multiple keys and remove them all at the same time.
15. Select another language and edit NLS for it as shown above.
16. When done, select **OK** to close the dialog.

**Notes:**

* For the same key, its NLS definition can be specified at three level: global, catalog and report. Among them, the global has the lowest priority, and the report has the highest priority. Global NLS resources cannot be edited in Logi JReport Designer, they can only be edited in Logi JReport Server.
* When the same key exists both in a catalog NLS resource and a report NLS resource and the translations at both levels are also the same, the one from the report NLS resource will be automatically deleted after selecting OK in the NLS Editor.
* When you have added some languages to the NLS Editor, a set of NLS property files will be generated in the directory where the current catalog exists according to the languages you have selected. One file is for one language with the name ReportName\_language\_locale.properties. The abbreviations of the language and locale are used in the NLS property file name. For example, the German NLS property file name for Report1 will be like this: Report1\_de\_DE.properties. This means the German language (de) as used in the German region (DE). If you want to use it for all German locales you can rename it just Report1\_de.properties.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590001-Mapping-Data-Values-to-Different-Languages)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589981-Built-in-Functions-for-NLS)
