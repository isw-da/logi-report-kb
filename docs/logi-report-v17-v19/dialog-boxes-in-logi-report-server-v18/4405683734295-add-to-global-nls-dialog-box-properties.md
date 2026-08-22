---
title: "Add to Global NLS Dialog Box Properties"
id: 4405683734295
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683734295-Add-to-Global-NLS-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:59Z
---

# Add to Global NLS Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683736599-Add-Language-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties)

# Add to Global NLS Dialog Box Properties

Use the Add to Global NLS dialog box to add the selected display, format, or font items to the target language's global NLS resource library. This topic describes how to add and translate display, format, and font items.

Server displays the dialog box when an administrator selects **Add to Global** in the [NLS Editor](https://devnet.logianalytics.com/hc/en-us/articles/4405690550551-NLS-Editor-Dialog-Box-Properties) to add the selected items.

The dialog box varies according to the type of the selected items: [Display](#Display), [Format](#Format), or [Font](#Font).

---

When you are adding display items, the Add to Global NLS dialog box looks as follows:

![Add to Global NLS dialog box - Display](https://devnet.logianalytics.com/hc/article_attachments/4420461674135/add2glbnls_dsply.gif)

**Language**

The target language into which you translate the display text.

**Checkbox**

Select the items you want to add to the target language's global NLS resource library. You can select the checkbox on the column header to select all the items.

**Type**

[Type](https://devnet.logianalytics.com/hc/en-us/articles/4405690550551-NLS-Editor-Dialog-Box-Properties#DisplayTextType) of display text for different objects.

**Key**

Keys to indicate the objects in the original language.

**Translate**

Translate the keys in the target language.

**Global NLS Translation**

Translation of the keys in the target language's global NLS resource library.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* If the translation is Null for a key, it means the key does not exist in the target language's global NLS resource library. Select the key if you want to add it.
* If a key already exists in the target language's global NLS resource library, and you provide a new translation for it in the **Translate** column, after you add this display item, Server replaces the existing global NLS translation for the key with the new one.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

When you are adding format items, the Add to Global NLS dialog box looks as follows:

![Add to Global NLS dialog - Format](https://devnet.logianalytics.com/hc/article_attachments/4420461674391/add2glbnls_fmt.gif)

**Language**

The target language into which you translate the format.

**Checkbox**

Select the items you want to add to the target language's global NLS resource library. You can select the checkbox on the column header to select all the items.

**Key**

Keys to indicate the formats in the original language.

**Translate**

Type the formats for the keys in the target language.

**Global NLS Translation**

Translation of the keys in the target language's global NLS resource library.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* If the translation is Null for a key, it means the key does not exist in the target language's global NLS resource library. Select the key if you want to add it.
* If a key already exists in the target language's global NLS resource library, and you provide a new translation for it in the **Translate** column, after you add this format item, Server replaces the existing global NLS translation for the key with the new one.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

When you are adding font items, the Add to Global NLS dialog box looks as follows:

![Add to Global NLS dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4420447267479/add2glbnls_font.gif)

**Language**

The target language into which you translate the font.

**Checkbox**

Select the items you want to add to the target language's global NLS resource library. You can select the checkbox on the column header to select all the items.

**Key**

Key indicates fonts in the original language.

**Font Face**

Select the font faces for the keys in the target language.

**Font Size**

Select or type the font sizes for the keys in the target language.

**Global NLS Translation**

Translation of the keys in the target language's global NLS resource library.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)

* If the translation is Null for a key, it means the key does not exist in the target language's global NLS resource library. Select the key if you want to add it.
* If a key already exists in the target language's global NLS resource library, and you provide a new font face and font size for it in the **Font Face** and **Font Size** columns, when you choose to add this font item, Server replaces the existing global NLS translation for the key with the new one.

**OK**

Select to apply any changes you made here and exit the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683736599-Add-Language-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties)
