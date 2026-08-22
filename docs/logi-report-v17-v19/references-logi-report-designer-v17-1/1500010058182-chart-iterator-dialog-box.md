---
title: "Chart Iterator Dialog Box"
id: 1500010058182
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058182-Chart-Iterator-Dialog-Box
updated_at: 2021-07-23T19:15:06Z
---

# Chart Iterator Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058142-Change-Property-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058202-Chart-Wizard-Dialog-Box)

# Chart Iterator Dialog Box

You can use the Chart Iterator dialog box to edit the [properties of an iterator](https://devnet.logianalytics.com/hc/en-us/articles/1500010057102-Editing-Range-Groups-on-Category-Values) in a chart. This topic describes the options in the dialog box.

Designer displays the Chart Iterator dialog box when you right-click the blank area and select Chart Iterator from the shortcut menu in the editing box of the [Data Label Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058562-Data-Label-Editor-Dialog-Box).

You see the following tabs in the dialog box:

* [Text Format Tab](#Text)
* [Font Tab](#Font)
* [Iteration Tab](#Iteration)

You see these buttons in all the tabs:

**OK**

Select to apply all changes and close the dialog box.

**Apply**

Select to apply all changes and leave the dialog box open.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

## Text Format Tab

Use this tab to specify the properties for the text in the iterator.

![Chart Interator dialog box - Text Format](https://devnet.logianalytics.com/hc/article_attachments/4404848629015/chtitratr_txt.gif)

**Alignment**

Select how text fit between the margins.

* **left**  
  Select to make the text left-aligned.
* **centered**  
  Select to make the text centered.
* **right**  
  Select to make the text right-aligned.
* **justified**  
  Select to adjust the horizontal spacing so as to align the text evenly along both the left and right margins. Justifying text creates a smooth edge on both sides.

**Indentation**

You can specify the distance of the text and the left or right margins in this box.

* **left**  
  Specify the distance of the text and the left margin.
* **right**  
  Specify the distance of the text and the right margin.
* **special**  
  Select in which way to make the text in the iterator specially indented.
  + **none**  
    Select to apply no special indent rule in the iterator.
  + **first line**  
    Select to use the first line indent in the iterator with the length you specify in the By text box.
  + **hanging**  
    Select to use the hanging indent in the iterator with the length you specify in the By text box.

**Spacing**

You can specify the spaces between lines in the paragraph of the iterator in this box.

* **Before**  
  Specify the distance with N lines before the iterator.
* **After**  
  Specify the distance with N lines after the iterator.
* **Line Spacing**  
  Select the amount of vertical space between lines of text in the iterator.
  + **single**  
    Select to accommodate the largest font in that line, plus a small amount of extra space. The amount of extra space varies depending on the font used.
  + **1.5 lines**  
    Select to use one-and-one-half times that of single line spacing.
  + **double**  
    Select to use twice of single line spacing.
  + **at least**  
    Select to use minimum line spacing that is needed to fit the largest font or graphic on the line.
  + **exactly**  
    Select to use fixed line spacing that Designer does not adjust.
  + **multiple**  
    Select to use line spacing that Designer increases or decreases by a percentage you specify. For example, setting line spacing to 1.2 increases the space by 20 percent.
* **At**  
  Specify the distances between lines. The option takes effect for the "at least", "exactly", or "multiple" Line Spacing only.

**Preview**

The box displays a preview sample of your selection.

## Font Tab

Use this tab to specify the font format of the text in the iterator.

![Chart Iterator dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/4404857007895/chtitratr_fnt.gif)

**Font list**

The box lists all the available font faces for the text. Select the font face you want to apply.

**Font Size**

Specify the font size of the text.

**Font Color**

Select the font color of the text. You can select Custom from the drop-down list to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060102-Pick-a-Color-Dialog-Box#Color).

**Rotation**

Designer does not support applying a rotation angle to the text in an iterator.

**Shearing**

Designer does not support applying a gradient effect on the text in an iterator.

**Preview**

The box displays a preview sample of your selection.

**Effects**

You can specify the special effect for the text in the iterator in this box.

* **Bold**  
  Specify whether to make the text in bold style.
* **Italic**  
  Specify whether to italicize the text.
* **Strikethrough**  
  Specify whether to draw a line through the text.
* **Underline**  
  Specify whether to add a horizontal line under the text.
* **Underline Color**  
  Select the color for the horizontal line under the text. You can select Custom from the drop-down list to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060102-Pick-a-Color-Dialog-Box#Color).
* **Underline Style**  
  Specify the style of the horizontal line under the text.
* **Ignore HTML Tag**  
  Designer does not support this option on the text in an iterator.
* **Subscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Superscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.

## Iteration Tab

Use this tab to specify the iteration information.

![Chart Iterator dialog box - Iteration](https://devnet.logianalytics.com/hc/article_attachments/4404848629399/chtitratr_itratn.gif)

**Iterated By**

The box lists the fields that you select to use as the marks of the iterator. You can change the display order of the fields.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**  
  Select to move the specified field higher in the list.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified field lower in the list.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058142-Change-Property-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010058202-Chart-Wizard-Dialog-Box)
