---
title: "Add to Global NLS Dialog Box Properties"
id: 1500009773861
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773861-Add-to-Global-NLS-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:50Z
---

# Add to Global NLS Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745862-Add-Language-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties)

# Add to Global NLS Dialog Box Properties

Use the Add to Global NLS dialog box to add the selected display, format, or font items to the target language's global NLS resource library. This topic describes how to translate display, format, and font items.

Server displays the dialog box when an admin user selects **Add to Global** button in the [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009746082-NLS-Editor-Dialog-Box-Properties) to add the selected items.

The dialog box varies according to the type of the selected items: [Display](#Display), [Format](#Format), and [Font](#Font).

---

When you are adding display items, the Add to Global NLS dialog box looks as follows:

![Add to Global NLS dialog - Display](https://devnet.logianalytics.com/hc/article_attachments/4404880429079/add2glbnls_dsply.gif)

**Language**

The target language into which you translate the display text.

**Check box**

Select the items you want to add to the target language's global NLS resource library. You can select the check box on the column header to select all the items.

**Type**

Types of display text for different objects.

* **Label**  
   Type of display text of label and some web controls.
* **Column**  
   This type is only for page reports running in Page Report Studio. It is the type of display text of columns.
* **Prompt**  
   Type of display text of parameter prompt value.
* **TOC**  
   Type of display text in the TOC tree.

**Key**

Keys to indicate the objects in the original language.

**Translate**

Translate the keys in the target language.

**Global NLS Translation**

Text to which the keys are translated in the target language's global NLS resource library. There are two circumstances:

* If the translation is Null for any key, it means the key does not exist in the target language's global NLS resource library yet. Select the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have provided a new translation for it in the **Translate** column, when you choose to add this display item, Server replaces the existing global NLS translation for the corresponding key with the new one.

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

**Help**

Select **Help** to view information about the Add to Global NLS dialog box.

---

When you are adding format items, the Add to Global NLS dialog box looks as follows:

![Add to Global NLS dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4404885516183/add2glbnls_fmt.gif)

**Language**

Target language into which you will add the format properties.

**Check box**

Select the items you want to add to the target language's global NLS resource library. You can select the check box on the column header to select all the items.

**Key**

Keys to indicate the formats in the original language.

**Translate**

Type the formats for the keys in the target language.

**Global NLS Translation**

Format properties for the keys in the target language's global NLS resource library. There are two circumstances:

* If the translation is Null for any key, it means the key does not exist in the target language's global NLS resource library yet. Select the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have specified a new format for it in the Format column, when you choose to add this format item, Server replaces the existing global NLS translation for the corresponding key with the new one.

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

**Help**

Select **Help** to view information about the Add to Global NLS dialog box.

---

When the Add to Global NLS dialog box is used to add font items, options in the dialog box are as follows.

![Add to Global NLS dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404880429463/add2glbnls_font.gif)

**Language**

Target language to which you will add the font properties.

**Check box**

Select the items you want to add to the target language's global NLS resource library. You can select the check box on the column header to select all the items.

**Key**

Keys to indicate the fonts in the original language.

**Font Face**

Select the font faces for the keys in the target language.

**Font Size**

Select or type the font sizes for the keys in the target language.

**Global NLS Translation**

Font properties for the keys in the target language's global NLS resource library. There are two circumstances:

* If the translation is Null for any key, it means the key does not exist in the target language's global NLS resource library yet. Select the key if you want to add it.
* If any key already exists in the target language's global NLS resource library, and you have specified a new font face and font size for it in the Font Face and Font Size columns, when you choose to add this font item, Server replaces the existing global NLS translation for the corresponding key with the new one.

**OK**

Select **OK** to apply any changes you made here.

**Cancel**

Select **Cancel** to close the dialog box without saving any changes.

**Help**

Select **Help** to view information about the Add to Global NLS dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745862-Add-Language-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties)
