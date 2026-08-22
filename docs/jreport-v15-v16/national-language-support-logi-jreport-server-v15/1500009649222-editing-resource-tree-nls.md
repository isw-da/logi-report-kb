---
title: "Editing Resource Tree NLS"
id: 1500009649222
section: "National Language Support Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649222-Editing-Resource-Tree-NLS
updated_at: 2021-07-24T20:53:57Z
---

# Editing Resource Tree NLS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673881-Running-NLS-Reports-Dashboards)

# Editing Resource Tree NLS

Logi JReport allows you to edit NLS for resources in the resource tree. With resource tree NLS, you can translate the names of all reports, library components and folders in the resource tree into different languages from the original one. This feature is provided to administrators only.

**To edit NLS for resources in the resource tree on Logi JReport Server:**

1. Start Logi JReport Server and log onto the Logi JReport Administration page.
2. Select **Resources** on the system toolbar and select **Resource Tree NLS** from the drop-down menu. The [Resource Tree NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009671161-Resource-Tree-NLS) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920484247/rscnls.gif)
3. Select the **Add** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) above the Language box. The Select Language Source dialog is then displayed.
4. Specify where to add the required languages.
   * **Languages Supported by Logi JReport**  
      Adds languages from the languages that Logi JReport supports.
   * **NLS Resource File**  
      Adds languages from an external NLS resource file which has been defined with some language information.

     NLS resource files should follow the naming rule: NLS\_[language]\_[region A2]\_[User-Defined].properties. The language argument is a valid ISO Language Code as defined by ISO-639. You can find a full list of these codes at a number of sites, for example: <http://www.loc.gov/standards/iso639-2/php/code_list.php>. The region argument is a valid ISO Country Code as defined by ISO-3166. You can find a full list of these codes at a number of sites, for example: <http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.
5. Select **OK** in the Select Language Source dialog. Then,
   * If Languages Supported by Logi JReport is checked in the dialog, the Add Language dialog will be displayed. Select the required languages and select **OK** to add them.
   * If NLS Resource File is checked in the dialog, in the displayed dialog, browse to the local folder where the NLS resource file is located, select the file and then select **Open**.

   The specified languages are now displayed in the Language box in the Resource Tree NLS dialog.
6. Select a language from the Language box to edit resource tree NLS for it.
7. The resource names are listed in the right panel. Give the corresponding target language text in the Translation column.
8. If needed, type the resource name you want to find in the Search box and then select the **Search** button, which helps you to find the resource quickly.
9. Select a folder to open resources in it. Give the corresponding target language text in the Translation column.

   When a new page is entered, the modifications you made on the last opened page will be saved automatically.
10. Repeat the above steps to define resource tree NLS for the other languages as required.
11. When done, select **OK** to accept the settings.
12. Select **Export** button to export the resource tree NLS map to a resource tree NLS file in the specified location for further use if needed.

    Note that only the resource tree of one translated language can be exported at a time and a user can only use the resource tree NLS file exported by himself.

**Notes:**

* The resource tree NLS takes effect only when the translated language is the same as the language specified for the option [Specify Default Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Language) in the Profile > Customize Server Preferences > Advanced tab or the browser language, and the former has higher priority.
* Resource tree NLS is not supported for resources from a real path.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649162-Editing-Local-NLS)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673881-Running-NLS-Reports-Dashboards)
