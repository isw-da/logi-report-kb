---
title: "NLS Editor Dialog Box"
id: 1500010059882
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059882-NLS-Editor-Dialog-Box
updated_at: 2021-07-23T19:15:45Z
---

# NLS Editor Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098121-New-XML-Hierarchical-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059862-Node-Pattern-List-Dialog-Box)

# NLS Editor Dialog Box

You can use the NLS Editor dialog box to [edit NLS](https://devnet.logianalytics.com/hc/en-us/articles/1500010061242-Creating-NLS-Property-Files) for the current report and catalog in order to display the report in other languages. This topic describes the options in the dialog box.

Designer displays the NLS Editor dialog box when you select Home/View > Language > NLS Editor.

![NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404856862615/nlsedtr.gif)

You see the following options in the dialog box:

**Language**

The box displays the languages that you add to edit NLS.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to open the [Add Language dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010057962-Add-Language-Dialog-Box) to add languages for editing NLS.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified language from the Language box.

**Display tab**

You can translate the display text for the selected target language in this tab. Select the column header to sort the items by the corresponding column in an ascending or descending order.

* **Search box**  
  Type the keyword in the box and Designer searches for the items that contain the specified text in the Key and Translate in *<language>* columns.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to open the [Add Display dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095441-Add-Display-Dialog-Box) to add available display text keys for the target language to edit NLS.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified display text keys for the target language.
* **Scope**  
  The column lists the scope of the keys.
  + **Global**  
    The option indicates that the key is from the global NLS resource.
  + **Catalog**  
    The option indicates that the key is from the catalog NLS resource.
  + **Report**  
    The option indicates that the key is from the report NLS resource.
* **Type**  
  The column lists the types of the display text keys. Designer categories the display text in different objects into different types.
  + **Column**  
    It indicates that the type of the display text key is Column, which only applies to reports running in Page Report Studio.
  + **DisplayName**  
    It indicates that the type of the display text key is Display Name.
  + **Label**  
    This type is for the display text in labels, some web controls, and UDOs.
  + **Metadata**  
    This type is mainly for the display text in catalog resources, such as table/view columns, business views, formulas, summaries, and parameters.
  + **Prompt**  
    This type is for the display text in the prompt values of parameters.
  + **Title**  
    This type is for the display text in filter controls and library components.
  + **TOC**  
    This type is for the display text in the TOC tree.

* **Key**  
  The column lists the display text keys in the original language that you add to translate. A display text key contains the display text of an object in the current report and catalog.
* **Translate in <language>**  
  The column shows the text to which you translate the display text keys in the target language.

**Format tab**

You can modify the field formats for the selected target language in this tab. Select the column header to sort the items by the corresponding column in an ascending or descending order.

* **Search box**  
  Type the keyword in the box and Designer searches for the items that contain the specified text in the Key and Format in *<language>* columns.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to open the [Add Format dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010057922-Add-Format-Dialog-Box) to add available format keys for the target language to edit NLS.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified format keys for the target language.
* **Scope**  
  The column lists the scope of the keys.
  + **Global**  
    The option indicates that the key is from the global NLS resource.
  + **Catalog**  
    The option indicates that the key is from the catalog NLS resource.
  + **Report**  
    The option indicates that the key is from the report NLS resource.
* **Key**  
  The column lists the format keys in the original language that you add to edit. A format key contains the format of a field in the current report and catalog.
* **Format in <language>**  
  The column shows the format that you specify for the format keys in the target language.

**Font tab**

You can modify the font properties for the selected target language in this tab. Select the column header to sort the items by the corresponding column in an ascending or descending order.

* **Search box**  
  Type the keyword in the box and Designer searches for the items that contain the specified text in the Font Face and Font Size columns.
* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to open the [Add Font dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095481-Add-Font-Dialog-Box) to add available font keys for the target language to edit NLS.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified font keys for the target language.
* **Scope**  
  The column lists the scope of the keys.
  + **Global**  
    The option indicates that the key is from the global NLS resource.
  + **Catalog**  
    The option indicates that the key is from the catalog NLS resource.
  + **Report**  
    The option indicates that the key is from the report NLS resource.
* **Key**  
  The column lists the font keys in the original language that you add to edit. A font key contains the font face and font size of a field in the current report and catalog.
* **Font Face**  
  The column shows the font face that you specify for the font keys in the target language.
* **Font Size**  
  The column shows the font size that you specify for the font keys in the target language.

**Synchronize Global NLS with Server**

Select to synchronize the global NLS resources with that on Server if you are connecting to a started Server; otherwise, Designer displays the [Connect to Logi Report Server dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box) for you to specify the information for connecting with the Server first.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098121-New-XML-Hierarchical-Data-Source-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059862-Node-Pattern-List-Dialog-Box)
