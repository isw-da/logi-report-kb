---
title: "Editing Local NLS"
id: 1500009649162
section: "National Language Support Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS
updated_at: 2021-07-24T20:53:58Z
---

# Editing Local NLS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649182-Creating-Global-NLS)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649222-Editing-Resource-Tree-NLS)

# Editing Local NLS

Logi JReport allows you to edit NLS for each catalog, report or library component as the report designer would with the NLS Editor in Logi JReport Designer. With the NLS Editor, you can translate a catalog, report or library component into different languages from the original one. This feature is provided to administrators only.

**To edit NLS for a catalog, report or library component on Logi JReport Server:**

1. Start Logi JReport Server and log onto the Logi JReport Administration page.
2. In the resource tree, browse to the catalog/report/library component for which you want to edit NLS.
3. Select the row that the catalog/report/library component is in, then select the **NLS Editor** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926691351/btn_srv_nlsedtr.gif) in the Control column. The [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009646522-NLS-Editor) appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920484887/nlsedtr.gif)
4. Specify a report/component if you are editing NLS for a report/library component and catalog version as required.
5. Select the **Add** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) above the Language box.
   * If you are editing NLS for a catalog, the [Select Language Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009646862-Select-Language-Source) dialog is displayed.
     Specify where to add the required languages, then select **OK**.
     + If Languages Supported by Logi JReport is checked in the dialog, the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009646362-Add-Language) dialog appears. Select the required languages and select **OK** to add them.
     + If NLS Resource File is checked in the dialog, the File Upload dialog appears. Browse to the local folder where the NLS resource file is located, select the file and then select **Open**.
   * If you are editing NLS for a report or library component, the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009646362-Add-Language) dialog is displayed. Select the languages in which you want the report/library component to display, then select****OK**** to confirm and go back to the NLS Editor.
6. The selected languages are now listed in Language box of the NLS Editor dialog. Select a target language from the box to edit NLS for it.
7. In the Display tab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif), then in the [Add Display](https://devnet.logianalytics.com/hc/en-us/articles/1500009670621-Add-Display) dialog, where all the display text in the catalog/report/library component are listed, select the keys you want to translate and enter the target language text for the keys in the Translate column, then select **OK**. The selected keys are now listed in the Display tab of the NLS Editor. You can further edit the translation for the keys here if required. Select **Add to Global NLS** to add the display information you just specify to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009670601-Add-to-Global-NLS#Display) dialog appears for you to handle the duplication.
8. Switch to the **Format** tab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif), then in the [Add Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009670641-Add-Format) dialog, where all the formats used in objects of the catalog/report/library component are listed, select the keys you want to customize and provide the target language format for the keys in the Format column, then select **OK**. The selected keys are now listed in the Format tab of the NLS Editor. You can further edit the format for the keys here if required. Select **Add to Global NLS** to add the format information you just specify to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009670601-Add-to-Global-NLS#Format) dialog appears for you to handle the duplication.
9. Select the **Font** tab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif), then in the [Add Font](https://devnet.logianalytics.com/hc/en-us/articles/1500009670661-Add-Font) dialog, where all the fonts used in objects of the catalog/report/library component are listed, select the keys you want to customize and give the target language font face and font size for the keys in the Font Face and Font Size columns, then select **OK**. The selected keys are now listed in the Font tab of the NLS Editor. You can further edit the font face and font size for the keys here if required. Select **Add to Global NLS** to add the font information you just specify to the global NLS library of the target language if you want to reuse them later. If some of the keys already exist in the global NLS library, the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009670601-Add-to-Global-NLS#Font) dialog appears for you to handle the duplication.
10. Select another language and edit NLS for it as shown above.
11. Select **OK** to accept the settings.

**Notes:**

* The keys with default values will not be saved when you select the OK button in the NLS Editor.
* You can also edit NLS for a specific catalog/report/library component version. To do this, on the Logi JReport Administration page, [access the version table of the report/library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009673741-Browsing-Versions), then select the **NLS Editor** link for the catalog/report/library component version.
* When you switch among different languages by choosing languages from the Language box, you may find that the text in the Translate column become unreadable. To resolve this problem, you can add `-DLogi JReport.url.encoding=UTF-8` to the batch file that starts the server and then restart it. This changes the encoding to Unicode which supports all languages.
* The Add to Global NLS option is not available to [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/1500009675081-Multi-tenancy-Supported-via-Organizations#Orgadmin).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649182-Creating-Global-NLS)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009649222-Editing-Resource-Tree-NLS)
