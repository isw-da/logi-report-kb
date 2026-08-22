---
title: "Chart Iterator Dialog Box"
id: 5735521975319
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735521975319-Chart-Iterator-Dialog-Box
updated_at: 2022-11-02T08:20:20Z
---

# Chart Iterator Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565102615-Change-Property-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513259415-Chart-Wizard-Dialog-Box)

# Chart Iterator Dialog Box

You can use the Chart Iterator dialog box to [edit properties of an iterator](https://devnet.logianalytics.com/hc/en-us/articles/5735520916503-Editing-Range-Groups-on-Category-Values) in a chart. This topic describes the options in the dialog box.

Designer displays the Chart Iterator dialog box when you right-click the blank area and select Chart Iterator from the shortcut menu in the editing box of the [Data Label Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735528944151-Data-Label-Editor-Dialog-Box).

This dialog box contains the following tabs:

* [Text Format Tab](#Text)
* [Font Tab](#Font)
* [Iteration Tab](#Iteration)

Designer displays these buttons in all the tabs:

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Apply**

Select to apply all changes and leave the dialog box open.

**Help**

Select to view information about the dialog box.

## Text Format Tab

Use this tab to specify properties of the text in the iterator.

![Chart Interator dialog box - Text Format](https://devnet.logianalytics.com/hc/article_attachments/7933732368663/chtitratr_txt.gif)

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

You can specify the indentation of the text in the iterator in this box.

* **Left**  
  Specify the distance between the text and the left margin.
* **Right**  
  Specify the distance between the text and the right margin.
* **Special**  
  Select in which way to specially indent the text in the iterator.
  + **none**  
    Select to apply no special indent rule in the iterator.
  + **first line**  
    Select to use the first line indent in the iterator with the length you specify in the By text box.
  + **hanging**  
    Select to use the hanging indent in the iterator with the length you specify in the By text box.

**Spacing**

You can specify the space between lines in the paragraph of the iterator in this box.

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
  Specify the distance between lines. This option takes effect for the "at least", "exactly", or "multiple" Line Spacing only.

**Preview**

This box displays a preview of your settings.

## Font Tab

Use this tab to specify the font style of the text in the iterator.

![Chart Iterator dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/7933761235991/chtitratr_fnt.gif)

**Font list**

This box lists all the font faces you can select to apply to the text.

**Font Size**

Specify the font size of the text.

**Font Color**

Select the font color of the text. You can also select **Custom** from the drop-down list to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color).

**Rotation**

Designer does not support applying a rotation angle to the text in an iterator.

**Shearing**

Designer does not support applying a gradient effect on the text in an iterator.

**Preview**

This box displays a preview of your settings.

**Effects**

You can specify the special effects of the text in the iterator in this box.

* **Bold**  
  Specify whether to apply bold formatting to the text.
* **Italic**  
  Specify whether to italicize the text.
* **Strikethrough**  
  Specify whether to draw a line through the text.
* **Underline**  
  Specify whether to add a horizontal line under the text.
* **Underline Color**  
  Select the color for the horizontal line under the text. You can also select **Custom** from the drop-down list to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735524246423-Pick-a-Color-Dialog-Box#Color).
* **Underline Style**  
  Specify the style of the horizontal line under the text.
* **Ignore HTML Tag**  
  Designer does not support this option for text in an iterator.
* **Subscript**  
  Select to raise the text above the baseline and change the text to a smaller font size, if a smaller size is available.
* **Superscript**  
  Select to lower the text below the baseline and change the text to a smaller font size, if a smaller size is available.

## Iteration Tab

Use this tab to specify the iteration information.

![Chart Iterator dialog box - Iteration](https://devnet.logianalytics.com/hc/article_attachments/7933732395415/chtitratr_itratn.gif)

**Iterated By**

This box lists the fields that you select to use as marks of the iterator. You can change the display order of the fields.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/7933647186583/btn_mvup.gif)**Move Up button**  
  Select to move the specified field higher in the list.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/7933647199511/btn_mvdwn.gif)**Move Down button**  
  Select to move the specified field lower in the list.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565102615-Change-Property-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735513259415-Chart-Wizard-Dialog-Box)
