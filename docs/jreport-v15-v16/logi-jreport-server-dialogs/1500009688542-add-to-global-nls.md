---
title: "Add to Global NLS"
id: 1500009688542
section: "Logi JReport Server Dialogs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009688542-Add-to-Global-NLS
updated_at: 2021-11-03T06:57:46Z
---

# Add to Global NLS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714521-Add-Language)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714541-Advanced-Run)

# Add to Global NLS

The Add to Global NLS dialog helps you to add the selected display, format, or font items to the target language's global NLS resource library. It is displayed when you select the Add to Global NLS button in the [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009714681-NLS-Editor) to add the selected display. The dialog varies according to the type of the selected items.

---

When the Add to Global NLS dialog is used for adding display items, options in the dialog are as follows.

![Add to Global NLS dialog - Display](https://devnet.logianalytics.com/hc/article_attachments/4412131475351/add2glbnls_dsply.gif)

**Language**

Displays the target language into which the display text is translated.

**Checkbox**

Specifies the items you want to add to the target language's global NLS resource library. Check the checkbox on the column header to select all the items.

**Type**

Lists types of display text for different objects.

* **Label**  
   Type of display text of label and some web controls.
* **Column**  
   This type is only for page reports running in Page Report Studio. It is the type of display text of columns.
* **Prompt**  
   Type of display text of parameter prompt value.
* **TOC**  
   Type of display text in the TOC tree.

**Key**

Lists keys to indicate the objects in the original language.

**Translate**

Specifies the translation for the keys in the target language.

**Global NLS Translation**

Displays the text to which the keys are translated in the target language's global NLS resource library. There are two circumstances:

* If the translation is Null for any key, it means the key doesn't exist in the target language's global NLS resource library yet. Check the checkbox ahead of the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have provided a new translation for it in the Translate column, when you choose to add this display item, the existing global NLS translation for the corresponding key will be replaced by the new one.

**OK**

Adds the selected items to the target language's global NLS resource library and exits the dialog.

**Cancel**

Cancels the action and exits the dialog.

**Help**

Displays the help document about this feature.

---

When the Add to Global NLS dialog is used for adding format items, options in the dialog are as follows.

![Add to Global NLS dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4412131475607/add2glbnls_fmt.gif)

**Language**

Displays the target language into which the format properties will be added.

**Checkbox**

Specifies the items you want to add to the target language's global NLS resource library. Check the checkbox on the column header to select all the items.

**Key**

Lists keys to indicate the formats in the original language.

**Translate**

Specifies the formats for the keys in the target language.

**Global NLS Translation**

Displays the format properties for the keys in the target language's global NLS resource library. There are two circumstances:

* If the translation is Null for any key, it means the key doesn't exist in the target language's global NLS resource library yet. Check the checkbox ahead of the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have specified a new format for it in the Format column, when you choose to add this format item, the existing global NLS translation for the corresponding key will be replaced by the new one.

**OK**

Adds the selected items to the target language's global NLS resource library and exits the dialog.

**Cancel**

Cancels the action and exits the dialog.

**Help**

Displays the help document about this feature.

---

When the Add to Global NLS dialog is used for adding font items, options in the dialog are as follows.

![Add to Global NLS dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4412139568919/add2glbnls_font.gif)

**Language**

Displays the target language to which the font properties will be applied.

**Checkbox**

Specifies the items you want to add to the target language's global NLS resource library. Check the checkbox on the column header to select all the items.

**Key**

Lists keys to indicate the fonts in the original language.

**Font Face**

Specifies the font faces for the keys in the target language.

**Font Size**

Specifies the font sizes for the keys in the target language.

**Global NLS Translation**

Displays the font properties for the keys in the target language's global NLS resource library. There are two circumstances:

* If the translation is Null for any key, it means the key doesn't exist in the target language's global NLS resource library yet. Check the checkbox ahead of the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have specified a new font face and font size for it in the Font Face and Font Size columns, when you choose to add this font item, the existing global NLS translation for the corresponding key will be replaced by the new one.

**OK**

Adds the selected items to the target language's global NLS resource library and exits the dialog.

**Cancel**

Cancels the action and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009714521-Add-Language)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009714541-Advanced-Run)
