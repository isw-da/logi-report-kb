---
title: "Format Text Dialog Box"
id: 1500010059402
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010059402-Format-Text-Dialog-Box
updated_at: 2021-07-23T19:15:33Z
---

# Format Text Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059382-Format-Target-Label-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097301-Format-Value-Y-Axis-Dialog-Box)

# Format Text Dialog Box

You can use the Format Text dialog box to specify the properties of a paragraph and font of the text in the paragraph. This topic describes the options in the dialog box.

Designer displays the Format Text dialog box when you right-click some selected text and select Font or Paragraph (if the text is in a table cell, Format Text) from the shortcut menu.

The dialog box contains the following tabs:

* [Paragraph Tab](#Paragraph)
* [Font Tab](#Font)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## Paragraph Tab

Use this tab to specify the properties for the paragraph.

![Format Text - Paragraph](https://devnet.logianalytics.com/hc/article_attachments/4404848535703/fmttext_prgrph.gif)

**Alignment**

You can specify how paragraphs fit between the margins in this box.

* **left**  
  Select to make the paragraph left-aligned.
* **centered**  
  Select to make the paragraph centered.
* **right**  
  Select to make the paragraph right-aligned.
* **justified**  
  Select to adjust the horizontal spacing so that the text is aligned evenly along both the left and right margins. Justifying text creates a smooth edge on both sides.

**Indentation**

You can specify the distance of the paragraph from either the left or right margins in the box.

* **Left**  
  Specify the distance of the paragraph from the left margin.
* **Right**  
  Specify the distance of the paragraph from the right margin.
* **Special**  
  Select how to specially indent the paragraph.
  + **none**  
    Select to apply no special indent rule in this paragraph.
  + **first line**  
    Select to use the first line indent in the paragraph with the length you specify in the By text box.
  + **hanging**  
    Select to use the hanging indent in the paragraph with the length you specify in the By text box.

**Spacing**

You can specify the space between lines in the paragraph in this box.

* **Before**  
  Specify the distance with N lines before the specified paragraph.
* **After**  
  Specify the distance with N lines after the specified paragraph.
* **Line Spacing**  
  Select the amount of vertical space between lines of text in a paragraph.
  + **Single**  
    Select to accommodate the largest font in that line, plus a small amount of extra space. The amount of extra space varies depending on the font used.
  + **1.5 lines**  
    Select to apply the spacing that is one-and-one-half times of the single line spacing.
  + **double**  
    Select to apply the spacing that is twice of the single line spacing.
  + **at least**  
    Select to apply minimum line spacing that is needed to fit the largest font or graphic on the line.
  + **exactly**  
    Select to apply fixed line spacing that Designer does not adjust.
  + **multiple**  
    Select to apply the spacing that is increased or decreased by the specified percentage. For example, setting line spacing to 1.2 increases the space by 20 percent.
* **At**  
  Specify the distances between lines. Designer applies the option when you select Line Spacing of "at least", "exactly" or "multiple".

**Preview**

The box displays a preview sample of your selection.

## Font Tab

Use this tab to specify the font format of the text in the paragraph.

![Format Text - Font](https://devnet.logianalytics.com/hc/article_attachments/4404848535959/fmttext_font.gif)

**Font list**

The list box contains all the font faces that you can select to apply to the text.

**Font Size**

Specify the font size of the text.

**Font Color**

Select the font color of the text. You can select Custom from the drop-down list to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060102-Pick-a-Color-Dialog-Box#Color).

**Rotation**

Designer does not support the option for text in a paragraph.

**Shearing**

Designer does not support the option for text in a paragraph.

**Preview**

The box displays a preview sample of your selection.

**Effects**

You can specify the special effects for the text in this box.

* **Bold**  
  Select to make the text in bold style.
* **Italic**  
  Select to italicize the text.
* **Strikethrough**  
  Select to draw a line through the text.
* **Underline**  
  Select to add a horizontal line under the text.
* **Underline Color**  
  Select the color for the horizontal line under the text. You can select Custom from the drop-down list to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060102-Pick-a-Color-Dialog-Box#Color).
* **Underline Style**  
  Select the style of the horizontal line under the text.
* **Ignore HTML Tag**  
  Designer does not support the option for text in a paragraph.
* **Subscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Superscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.

![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404848413975/btn_fmla.gif)

Designer displays the button for some options if the report containing the paragraph uses query resources. It indicates that you can [use a formula to control the value of an option](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059382-Format-Target-Label-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097301-Format-Value-Y-Axis-Dialog-Box)
