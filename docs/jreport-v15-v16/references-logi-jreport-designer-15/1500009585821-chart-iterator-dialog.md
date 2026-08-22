---
title: "Chart Iterator Dialog"
id: 1500009585821
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585821-Chart-Iterator-Dialog
updated_at: 2021-07-24T05:55:35Z
---

# Chart Iterator Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585781-Change-Property-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585841-Chart-Wizard-Dialog-Business-View-Based-)

# Chart Iterator Dialog

The Chart Iterator dialog appears when you right-click the blank space and select Chart Iterator from the shortcut menu in the editing box of the [Data Label Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009565062-Data-Label-Editor-Dialog). It helps you to edit the [properties of an iterator](https://devnet.logianalytics.com/hc/en-us/articles/1500009562982-Formatting-the-Axes#Category) in a chart, and consists of the following tabs:

* [Text Format](#Text)
* [Font](#Font)
* [Iteration](#Iteration)

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## Text Format

Specifies the properties for the text in the iterator. [See the tab](javascript:%20void(null)).

![Chart Interator dialog - Text Format](https://devnet.logianalytics.com/hc/article_attachments/4404893952407/chtitratr_txt.gif)

**Alignment**

Specifies how text fit between the margins.

* **Left**  
   Specifies to make the text left-aligned.
* **Centered**  
   Specifies to make the text centered.
* **Right**  
   Specifies to make the text right-aligned.
* **Justified**  
   Specifies to adjust the horizontal spacing so that text is aligned evenly along both the left and right margins. Justifying text creates a smooth edge on both sides.

**Indentation**

Specifies the distance of the text and the left or right margins.

* **Left**  
   Specifies the distance of the text and the left margin.
* **Right**  
   Specifies the distance of the text and the right margin.
* **Special**  
   Specifies to make the text in the iterator specially indented.
  + **None**  
     If selected, no special indent rule will be applied in this iterator.
  + **First line**  
     If selected, use the First line indent in the iterator with the length you specified in the By text box.
  + **Hanging**  
     If selected, use the Hanging indent in the iterator with the length you specified in the By text box.

**Spacing**

Specifies the spaces between lines in the paragraph.

* **Before**  
   Specifies the distance with N lines before the specified iterator.
* **After**  
   Specifies the distance with N lines after the specified iterator.
* **Line Spacing**  
   Specifies the amount of vertical space between lines of text in a iterator.
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

Specifies the font format of text in the iterator. [See the tab](javascript:%20void(null)).

![Chart Iterator dialog - Font](https://devnet.logianalytics.com/hc/article_attachments/4404889389719/chtitratr_fnt.gif)

**Font list**

Lists all the available font faces for the text.

**Font Size**

Specifies the font size of the text.

**Font Color**

Specifies the font color of the text. Select a color from the drop-down list or select Custom from the list to customize a color in the [Pick a Color](https://devnet.logianalytics.com/hc/en-us/articles/1500009567042-Pick-a-Color-Dialog#Color) dialog.

**Rotation**

Specifies the rotation angle of the text around its center, in degrees. Not supported on text in the iterator.

**Shearing**

Specifies the gradient of text. Not supported on text in the iterator.

**Preview**

Displays a preview sample of your selection.

**Effects**

Specifies special effect for the text in the iterator.

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
   If true, the text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the field value, if any, will not be parsed); or HTML tag elements of the text will be parsed while the report is to be saved as an HTML file. Not supported on text in the iterator.
* **Subscript**  
   Specifies whether to make the specified text as subscript.
* **Superscript**  
   Specifies whether to make the specified text as superscript.

## Iteration

Specifies the iteration information. [See the tab](javascript:%20void(null)).

![Chart Iterator dialog - Iteration](https://devnet.logianalytics.com/hc/article_attachments/4404889389975/chtitratr_itratn.gif)

**Iterated By**

Specifies the fields used as the marks of the iterator.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)  
   Moves the selected field one step up.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)  
   Moves the selected field one step down.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585781-Change-Property-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585841-Chart-Wizard-Dialog-Business-View-Based-)
