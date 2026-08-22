---
title: "NLS Editor Dialog"
id: 1500009632541
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009632541-NLS-Editor-Dialog
updated_at: 2021-07-24T16:04:21Z
---

# NLS Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609442-New-XML-Hierarchical-Data-Source-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632521-Node-Pattern-List-Dialog)

# NLS Editor Dialog

The NLS Editor helps you to [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500009611442-Creating-NLS-Property-Files) for the current report and catalog. It appears when you select Edit > NLS Editor.

![NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904216727/nlsedtr.gif)

The following are details about options in the editor:

**Language**

Displays the languages into which the display text in the current report and catalog will be translated.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)

Opens the [Add Language](https://devnet.logianalytics.com/hc/en-us/articles/1500009607122-Add-Language-Dialog) dialog to add languages for editing here.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)

Removes the selected language from the Language box.

**Display tab**

Specifies the translation of all the display text. You can select the column header in the display table to sort the items by the corresponding column in an ascending or descending order.

* **Search box**   
   Searches for the items that contain the specified text in the Key and Translate in <language> columns.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
   Opens the [Add Display](https://devnet.logianalytics.com/hc/en-us/articles/1500009629761-Add-Display-Dialog) dialog to add available display text keys for the target language to edit NLS.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
   Removes the selected rows of display text for the target language.
* **Scope**  
   Lists the scope of the keys.
  + **Global**  
     Indicates the key is from global NLS resources.
  + **Catalog**  
     Indicates the key is from catalog NLS resouces.
  + **Report**  
     Indicates the key is from report NLS resouces.
* **Type**  
   Lists types of display text for different objects.
  + **Column**  
     This type is only for reports running in Page Report Studio. It is the type of display text of columns.
  + **DisplayName**  
     Type of display text of object display name.
  + **Label**  
     Type of display text of label, some web controls and UDOs.
  + **Metadata**  
     Type of display text of metadata. Metadata mainly refers to catalog resources, such as table/view columns, business views, formulas, summaries, parameters, and so on.
  + **Prompt**  
     Type of display text of parameter prompt value.
  + **Title**  
     Type of display text of filter control and library component.
  + **TOC**  
     Type of display text on the TOC tree.

* **Key**  
   Lists keys to indicate the objects in the original language.
* **Translate** **in <language>**  
   Specifies to which the display text will be translated in the target language.

**Format tab**

Specifies the formats for all fields. You can select the column header in the format table to sort the items by the corresponding column in an ascending or descending order.

* **Search box**   
   Searches for the items that contain the specified text in the Key and Format in <language> columns.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
   Opens the [Add Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009629801-Add-Format-Dialog) dialog to add available format keys for the target language to edit NLS.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
   Removes the selected rows of format for the target language.
* **Scope**  
   Lists the scope of the keys.
  + **Global**  
     Indicates the key is from global NLS resources.
  + **Catalog**  
     Indicates the key is from catalog NLS resouces.
  + **Report**  
     Indicates the key is from report NLS resouces.
* **Key**  
   Displays formats of all fields in the current report and catalog in the original language.
* **Format in <language>**  
   Specifies the format for every field in the current report and catalog in the target language.

**Font tab**

Specifies font properties for all fields. You can select the column header in the font table to sort the items by the corresponding column in an ascending or descending order.

* **Search box**   
   Searches for the items that contain the specified text in the Font Face and Font Size columns.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)  
   Opens the [Add Font](https://devnet.logianalytics.com/hc/en-us/articles/1500009629821-Add-Font-Dialog) dialog to add available font keys for the target language to edit NLS.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif)  
   Removes the selected rows of font for the target language.
* **Scope**  
   Lists the scope of the keys.
  + **Global**  
     Indicates the key is from global NLS resources.
  + **Catalog**  
     Indicates the key is from catalog NLS resouces.
  + **Report**  
     Indicates the key is from report NLS resouces.
* **Key**  
   Lists font face and font size of all fields in the current report and catalog in the original language.
* **Font Face**  
   Specifies font face for every field in the current report and catalog in the target language.
* **Font Size**  
   Specifies font size for every field in the current report and catalog in the target language.

**Synchronize Global NLS with Server**

Synchronizes the global NLS resources for the target language with that on Logi Report Server.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009609442-New-XML-Hierarchical-Data-Source-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009632521-Node-Pattern-List-Dialog)
