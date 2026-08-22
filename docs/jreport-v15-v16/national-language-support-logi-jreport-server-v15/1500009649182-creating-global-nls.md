---
title: "Creating Global NLS"
id: 1500009649182
section: "National Language Support Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649182-Creating-Global-NLS
updated_at: 2021-07-24T20:53:58Z
---

# Creating Global NLS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649142-NLS-at-Report-Level)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS)

# Creating Global NLS

The global NLS is similar to the [local NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS) feature. Local NLS is the NLS resource used for a particular report or library component, while global NLS is the NLS resource that can be used for all reports and library components in any catalog in both Logi JReport Server and Logi JReport Designer. With global NLS, you can share the NLS information between all reports and library components and reduce your translation cost. This feature is provided to administrators only.

**To create global NLS on Logi JReport Server:**

1. Start Logi JReport Server and log onto the Logi JReport Administration page.
2. Select **Resources** on the system toolbar and select **Global NLS** from the drop-down menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920484631/glbnls.gif)
3. Select the **Add** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) above the Language box. The Select Language Source dialog is then displayed.
4. Specify where to add the required languages.
   * **Languages Supported by Logi JReport**  
      Adds languages from the languages that Logi JReport supports.
   * **NLS Resource File**  
      Adds languages from an external NLS resource file which has been defined with some language information.

     NLS resource files should follow the naming rule: NLS\_[language]\_[region A2]\_[User-Defined].properties. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The region argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
5. Select **OK** in the Select Language Source dialog. Then,
   * If Languages Supported by Logi JReport is checked in the dialog, the Add Language dialog will be displayed. Select the required languages and select **OK** to add them.
   * If NLS Resource File is checked in the dialog, the File Upload dialog will be displayed. Browse to the local folder where the NLS resource file is located, select the file and then select **Open**.

   The specified languages are now displayed in the Language box in the Global NLS dialog.
6. Select a language from the Language box to edit global NLS for it.
7. In the Display tab, select the **Add** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif)
   to add a new row of display.
   Select the type of the display from the Type drop-down list, specify the key in the Key column, then give the corresponding target language text in the Translation column. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to add more rows and specify the key and translation according to your requirements.
8. In the Format tab, select the **Add** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to add a new row of format. In the Key column, specify the format of the key in the original language, then in the Format column, specify the format of the key in the target language. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to add more rows and specify the format information according to your requirements.
9. In the Font tab, select the **Add** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to add a new row of font. In the Key column, choose from the drop-down lists the font face and font size of the key, in the Font Face column, choose from the drop-down list the font face for the target language, then in the Font Size column, choose from the drop-down list the font size for the target language or check to use relative font size. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to add more rows and specify the font information according to your requirements.
10. Repeat the above steps to define global NLS for the other languages as required.
11. When done, select **OK** to accept the settings.

See also the [Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009670801-Global-NLS) dialog for detailed explanation about options in the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649142-NLS-at-Report-Level)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS)
