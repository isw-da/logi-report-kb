---
title: "Add to Global NLS"
id: 1500009747221
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747221-Add-to-Global-NLS
updated_at: 2021-07-25T07:19:44Z
---

# Add to Global NLS

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747281-Add-Language)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747301-Advanced-Run)

# Add to Global NLS

The Add to Global NLS dialog box is used to add the selected display, format, or font items to the target language's global NLS resource library. It appears when an admin user selects the Add to Global NLS button in the [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009720602-NLS-Editor) to add the selected items.

The dialog box varies according to the type of the selected items: [Display](#Display), [Format](#Format) and [Font](#Font).

---

When the Add to Global NLS dialog box is used to add display items, options in the dialog box are as follows.

![Add to Global NLS dialog - Display](https://devnet.logianalytics.com/hc/article_attachments/4404942566935/add2glbnls_dsply.gif)

**Language**

Displays the target language into which the display text is translated.

**Check box**

Specifies the items you want to add to the target language's global NLS resource library. Select the check box on the column header to select all the items.

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

* If the translation is Null for any key, it means the key doesn't exist in the target language's global NLS resource library yet. Select the check box ahead of the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have provided a new translation for it in the Translate column, when you choose to add this display item, the existing global NLS translation for the corresponding key will be replaced by the new one.

**OK**

Adds the selected items to the target language's global NLS resource library and exits the dialog box.

**Cancel**

Cancels the action and exits the dialog box.

**Help**

Displays the help document about this feature.

---

When the Add to Global NLS dialog box is used to add format items, options in the dialog box are as follows.

![Add to Global NLS dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404942567191/add2glbnls_fmt.gif)

**Language**

Displays the target language into which the format properties will be added.

**check box**

Specifies the items you want to add to the target language's global NLS resource library. Select the check box on the column header to select all the items.

**Key**

Lists keys to indicate the formats in the original language.

**Translate**

Specifies the formats for the keys in the target language.

**Global NLS Translation**

Displays the format properties for the keys in the target language's global NLS resource library. There are two circumstances:

* If the translation is Null for any key, it means the key doesn't exist in the target language's global NLS resource library yet. Select the check box ahead of the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have specified a new format for it in the Format column, when you choose to add this format item, the existing global NLS translation for the corresponding key will be replaced by the new one.

**OK**

Adds the selected items to the target language's global NLS resource library and exits the dialog box.

**Cancel**

Cancels the action and exits the dialog box.

**Help**

Displays the help document about this feature.

---

When the Add to Global NLS dialog box is used to add font items, options in the dialog box are as follows.

![Add to Global NLS dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404942567447/add2glbnls_font.gif)

**Language**

Displays the target language to which the font properties will be applied.

**Check box**

Specifies the items you want to add to the target language's global NLS resource library. Select the check box on the column header to select all the items.

**Key**

Lists keys to indicate the fonts in the original language.

**Font Face**

Specifies the font faces for the keys in the target language.

**Font Size**

Specifies the font sizes for the keys in the target language.

**Global NLS Translation**

Displays the font properties for the keys in the target language's global NLS resource library. There are two circumstances:

* If the translation is Null for any key, it means the key doesn't exist in the target language's global NLS resource library yet. Select the check box ahead of the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have specified a new font face and font size for it in the Font Face and Font Size columns, when you choose to add this font item, the existing global NLS translation for the corresponding key will be replaced by the new one.

**OK**

Adds the selected items to the target language's global NLS resource library and exits the dialog box.

**Cancel**

Cancels the action and exits the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009747281-Add-Language)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747301-Advanced-Run)
