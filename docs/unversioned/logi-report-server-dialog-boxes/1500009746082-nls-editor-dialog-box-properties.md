---
title: "NLS Editor Dialog Box Properties"
id: 1500009746082
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746082-NLS-Editor-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:48Z
---

# NLS Editor Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774301-New-User-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774341-Page-Report-Studio-Profile-Properties)

# NLS Editor Dialog Box Properties

This topic describes how you can use the NLS Editor dialog box to [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009777481-NLS-at-Report-Level#Local) for the specified resource.

Server displays the dialog box when an admin user selects the NLS Editor button ![NLS Editor button](https://devnet.logianalytics.com/hc/article_attachments/4404880282391/btn_srv_nlsedtr.gif) on the floating toolbar of a catalog, report, library component, or dashboard in the Resources page of the Server Console.

![NLS Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880282647/nlsedtr.gif)

**Report/Component/Dashboard**

Displays the name of the report/library component/dashboard. Available only when editing NLS for a report, library component or dashboard.

**Edit Subreport's NLS**

Specifies to edit each subreport's NLS. Available only when the specified report has subreports.

When you select this button, another dialog box will appear showing all the subreports of the specified report. To edit a subreport's NLS, just select the Edit NLS link for it in the dialog box. The method of editing NLS for a subreport is just the same as that for a primary report.

**Catalog**

Displays the name of the catalog or the catalog that the report/library component/dashboard uses.

**Select Another Catalog**

Specifies another catalog for the report/library component/dashboard in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009746402-Select-Another-Catalog-Dialog-Box-Properties) dialog box. Available only when editing NLS for a report, library component or dashboard.

**Report/Component/Dashboard Version**

Specifies the report/library component/dashboard version to apply the NLS settings. Available only when editing NLS for a report, library component or dashboard.

**Catalog Version**

Specifies the catalog version.

**Language**

Lists the languages into which the display text in the catalog/report/library component/dashboard will be translated. If you cannot find the language you need, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif) above the box to add it.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)

* When editing NLS for a report, library component or dashboard, selecting the button opens the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009745862-Add-Language-Dialog-Box-Properties) dialog box to add languages.
* When editing NLS for a catalog, selecting the button opens the [Select Language Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009746442-Select-Language-Source-Dialog-Box-Properties) dialog box to choose where to add a language.

![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)

Removes the selected language from the Language box.

**Display Tab**

Specifies the translation of every display text in the catalog/report/library component/dashboard. You can select the underlined column header to sort the items by that column in an ascending or descending order.

* **Search box**  
   Searches for the items that contain the specified keyword. After typing in the keyword, select ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif) in the box or press Enter on the keyboard to start searching. Logi Report searches in both the Key and Translate columns.
* **Type**  
   Lists types of display text for different objects.
  + **Column**  
     This type is only for page reports running in Page Report Studio. It is the type of display text of columns.
  + **DisplayName**  
     Type of display text of object display name.
  + **Metadata**  
     Type of display text of metadata. Metadata mainly refers to catalog resources, such as table/view columns, business views, formulas, summaries, and parameters.
  + **Label**  
     Type of display text of label, some web controls and UDOs.
  + **Prompt**  
     Type of display text of parameter prompt value.
  + **Title**  
     Type of display text of filter control, library component and objects in it.
  + **TOC**  
     Type of display text in the TOC tree.
* **Key**  
   Lists keys to indicate the objects in the original language.
* **Translate**  
   Specifies the translation of the keys in the target language.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
   Opens the [Add Display](https://devnet.logianalytics.com/hc/en-us/articles/1500009745842-Add-Display-Dialog-Box-Properties) dialog box to add available display text in the objects of the catalog/report/library component/dashboard for the target language.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
   Removes the selected display items for the target language.

**Format tab**

Specifies the format for all fields in the catalog/report/library component/dashboard. You can select the underlined column header to sort the items by that column in an ascending or descending order.

* **Search box**  
   Searches for the items that contain the specified keyword. After typing in the keyword, select ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif) in the box or press Enter on the keyboard to start searching. Logi Report searches in both the Key and Format in <language> columns.
* **Key**  
   Lists keys to indicate the formats in the original language.
* **Format**Specifies the formats for the keys in the target language.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
   Opens the [Add Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009773881-Add-Format-Dialog-Box-Properties) dialog box to add available formats in the objects of the catalog/report/library component/dashboard for the target language.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
   Removes the selected format items for the target language.

**Font tab**

Specifies font properties for all fields in the catalog/report/library component/dashboard. You can select the underlined column header to sort the items by that column in an ascending or descending order.

* **Search box**  
   Searches for the items that contain the specified keyword. After typing the keyword, select the search button in the box or press Enter on the keyboard to start searching. Logi Report searches in both the Font Face and Font Size columns.
* **Key**  
   Lists keys to indicate the fonts in the original language.
* **Font Face**  
   Specifies the font faces for the keys in the target language.
* **Font Size**  
   Specifies the font sizes for the keys in the target language.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif)  
   Opens the [Add Font](https://devnet.logianalytics.com/hc/en-us/articles/1500009773901-Add-Font-Dialog-Box-Properties) dialog box to add available fonts in the objects of the catalog/report/library component/dashboard for the target language.
* ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif)  
   Removes the selected font items for the target language.

**Add to Global NLS**

Specifies to add the selected display/format/font items to the target language's global NLS resource library. If some of the items already exist in the global NLS resource library of the target language, Server displays the [Add to Global NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009773861-Add-to-Global-NLS-Dialog-Box-Properties) dialog box for you to handle the duplication.

This option is not available to [organization admin](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations).

**OK**

Applies the settings and closes the dialog box.

**Cancel**

Cancels the settings and exits the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009774301-New-User-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774341-Page-Report-Studio-Profile-Properties)
