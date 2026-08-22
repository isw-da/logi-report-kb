---
title: "Format Text Dialog"
id: 1500010066661
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010066661-Format-Text-Dialog
updated_at: 2021-07-24T10:38:43Z
---

# Format Text Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066641-Format-Target-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031162-Format-Value-Y-Axis-Dialog)

# Format Text Dialog

The Format Text dialog helps you to set the properties of a paragraph and font of the text in the paragraph. It appears when you right-click some selected strings and then select Font or Paragraph (if the string is in a table cell, Format Text) from the shortcut menu.

The dialog contains the following tabs: [Paragraph](#Paragraph) and [Font.](#Font)

**OK**

Accepts all changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes in this dialog.

**Help**

Displays the help document about this feature.

## Paragraph

Specifies properties for the paragraph.

![Format Text - Paragraph](https://devnet.logianalytics.com/hc/article_attachments/4404909195159/fmttext_prgrph.gif)

**Alignment**

Specifies how paragraphs fit between the margins.

* **Left**  
  Specifies to make the paragraph left-aligned.
* **Centered**  
   Specifies to make the paragraph centered.
* **Right**  
   Specifies to make the paragraph right-aligned.
* **Justified**  
   Specifies to adjust the horizontal spacing so that text is aligned evenly along both the left and right margins. Justifying text creates a smooth edge on both sides.

**Indentation**

Specifies the distance of the paragraph from either the left or right margins.

* **Left**  
   Specifies the distance of the paragraph from the left margin.
* **Right**  
   Specifies the distance of the paragraph from the right margin.
* **Special**  
   Specifies to make the paragraph specially indented.
  + **None**  
     If selected, no special indent rule will be applied in this paragraph.
  + **First line**  
     If selected, use the First line indent in the paragraph with the length you specified in the By text box.
  + **Hanging**  
     If selected, use the Hanging indent in the paragraph with the length you specified in the By text box.

**Spacing**

Specifies the spaces between lines in the paragraph.

* **Before**  
   Specifies the distance with N lines before the specified paragraph.
* **After**  
   Specifies the distance with N lines after the specified paragraph.
* **Line Spacing**  
   Specifies the amount of vertical space between lines of text in a paragraph.
  + **Single**  
     Accommodates the largest font in that line, plus a small amount of extra space. The amount of extra space varies depending on the font used.
  + **1.5 lines**  
     One-and-one-half times that of single line spacing.
  + **Double**  
     Twice that of single line spacing.
  + **At least**  
     Minimum line spacing that is needed to fit the largest font or graphic on the line.
  + **Exactly**  
     Fixed line spacing that Logi JReport Designer does not adjust.
  + **Multiple**  
     Line spacing that is increased or decreased by a percentage that you specify. For example, setting line spacing to 1.2 will increase the space by 20 percent.
* **At**  
   Effective only when you have selected At least, Exactly or Multiple**.** it specifies the distances between lines.

**Preview**

Displays a preview sample of your selection.

## Font

Specifies the font format of text in the paragraph.

![Format Text - Font](https://devnet.logianalytics.com/hc/article_attachments/4404901221271/fmttext_font.gif)

**Font list**

Lists all the available font faces for the text.

**Font Size**

Specifies the font size of the text.

**Font Color**

Specifies the font color of the text. Select a color from the drop-down list or select Custom from the list to customize a color in the [Pick a Color](https://devnet.logianalytics.com/hc/en-us/articles/1500010067401-Pick-a-Color-Dialog#Color) dialog.

**Rotation**

Specifies the rotation angle of the text around its center, in degrees. Not supported on text in the paragraph.

**Shearing**

Specifies the gradient of text. Not supported on text in the paragraph.

**Preview**

Displays a preview sample of your selection.

**Effects**

Specifies special effect for the text.

* **Bold**  
   Specifies whether the text to be bold or not.
* **Italic**  
   Specifies whether the text to be italic or not.
* **Strikethrough**  
   Specifies whether or not to draw a line through the text.
* **Underline**  
   Specifies whether to use the horizontal line under the text or not.
* **Underline Color**  
   Specifies the color for the horizontal line under the text.
* **Underline Style**  
   Specifies the style of the horizontal line under the text.
* **Ignore HTML Tag**  
   If true, the text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the field value, if any, will not be parsed); or HTML tag elements of the text will be parsed while the report is to be saved as an HTML file. Not supported on text in the paragraph.
* **Subscript**  
   Specifies whether to make the specified text as subscript.
* **Superscript**  
   Specifies whether to make the specified text as superscript.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif)

Indicates the value of an option can be [controlled by a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066641-Format-Target-Label-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010031162-Format-Value-Y-Axis-Dialog)
