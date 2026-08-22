---
title: "Working with Text Boxes"
id: 5735527727383
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes
updated_at: 2022-11-02T04:13:23Z
---

# Working with Text Boxes

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports)

# Working with Text Boxes

Similar to a word processing document, a text box is an object that holds text (a single character, a single word, entire sentences, or paragraphs). Editing in a text box is just like working in a word processor. You can cut, copy, and paste selected text easily, and format the text as needed. A text box can also hold other components. This topic describes how you can insert text boxes in a report, format the paragraphs and text in a text box, and use the other text box features.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)You cannot use text boxes in library components.

This topic contains the following sections:

* [Inserting Text Boxes in a Report](#Insert)
* [Formatting Paragraphs](#Paragraph)
* [Formatting Text](#Text)
* [Finding or Replacing a Text String](#Find)
* [Importing and Exporting Text](#Import)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the text box example, open `<install_root>\Demo\Reports\SampleComponents\ForTextBox.cls`.

## Inserting Text Boxes in a Report

You can insert text boxes in the report areas listed in [Component Placement in Different Report Type](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type).

To insert a text box into a report, use either of the following methods:

* Navigate to **Insert** > **Text Box** or **Home** > **Insert** > **Text Box**. If the mouse pointer is in the report body or a tabular cell, Designer inserts a text box there; otherwise, you need to select in the location where you want to insert the text box to place the text box there.
* From the **Components** panel, drag the **Text Box** icon ![Text Box icon](https://devnet.logianalytics.com/hc/article_attachments/9898517876503/icon_txtbx.gif) in the **Basic** category to the target location in the report which allows the insertion of a text box, Designer then inserts a text box there.

After you insert a text box into a report, you can then double-click it to type in text.

## Formatting Paragraphs

Designer creates paragraphs in a text box when you type text in it. You can easily format the paragraphs, for example, the alignment style, indentation, or line spacing.

**To format a paragraph in a text box**

1. Right-click anywhere in the paragraph and select **Paragraph** on the shortcut menu. Designer displays the [Format Text dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735551503511-Format-Text-Dialog-Box#Paragraph).

   ![Format Text dialog box - Paragraph](https://devnet.logianalytics.com/hc/article_attachments/9898462744727/fmttext_prgrph.gif)
2. In the **Paragraph** tab,
   * To specify the alignment style of the paragraph, select the required option from the **Alignment** drop-down list: left, center, right, or justified.
   * To set the indentation of the paragraph, in the **Indentation** box, specify the left and right indent distance in the **Left** and **Right** text boxes. If you want to set the paragraph to be indented, select **first line** or **hanging** from the **Special** drop-down list, then type a number in the **By** text box. This creates a first-line indent or hanging indent in the paragraph using the inputted number as the indent distance.
   * To adjust the spacing before or after the paragraph, specify the required amount of spacing in the **Before** or **After** text box.
   * To change the spacing between the lines in the paragraph, select the required item from the **Line Spacing** drop-down list. If you select **at least**, **exactly**, or **multiple**, specify the required amount of space or the number of lines in the **At** text box.
3. Select **OK** to accept the changes.

You can also set the indentation of a paragraph by simply moving the tap stop icons on the ruler of the Design tab. To do this, position the mouse pointer anywhere on the paragraph, then,

* To create a first-line indent or hanging indent, drag ![](https://devnet.logianalytics.com/hc/article_attachments/9898517880215/btn_lnindnt.gif) to the position where you want the text to start.
* To change the left indent, drag ![](https://devnet.logianalytics.com/hc/article_attachments/9898517899415/btn_lftindnt.gif) to the position where you want the paragraph to start.
* To change the right indent, drag ![](https://devnet.logianalytics.com/hc/article_attachments/9898517908119/btn_rtindnt.gif) to the position where you want the paragraph to end.

## Formatting Text

You can format the text you type into a text box to suit your requirements. For example, you can change the font size, color, alignment, and highlight the text with a distinguishing color.

**To format the text in a text box**

1. Select the text you want to format, right-click and select **Font** on the shortcut menu.
2. In the **Font** tab of the Format Text dialog box, specify the [font settings](https://devnet.logianalytics.com/hc/en-us/articles/5735551503511-Format-Text-Dialog-Box#Font).

   ![Format Text dialog box - Font](https://devnet.logianalytics.com/hc/article_attachments/9898462758423/fmttext_font.gif)
3. Select **OK** to accept the changes.

You can also format the selected text by using the corresponding options in the **Format** ribbon.

## Finding or Replacing a Text String

**To find a character string in a text box**

1. Right-click anywhere in the text box and select **Find a String** from the shortcut menu.
2. In the **Find** tab of the Find and Replace dialog box, specify the string you want to search for and set the other settings as required.

   ![Find and Replace dialog box - Find](https://devnet.logianalytics.com/hc/article_attachments/9898534239255/cmpnt_txtbx_find.gif)
3. Select **Find Next** to start finding the specified string.

Similar to finding text, if you want to replace a string in the text box with another one, take the following steps:

1. Right-click anywhere in the text box and select **Replace** from the shortcut menu. Designer displays the Find and Replace dialog box with the **Replace** tab selected.

   ![Find and Replace dialog box - Replace](https://devnet.logianalytics.com/hc/article_attachments/9898534244119/cmpnt_txtbx_rplc.gif)
2. Specify the settings according to your requirements and select **Replace** or **Replace All** to replace the next or all the specified string with another one.

## Importing and Exporting Text

**To import text into a text box from an external file (.txt or .rtf)**

1. Position the mouse pointer at the location where you want to insert the imported text, then right-click and select **Import External File**.
2. In the Import a File dialog box, select the .txt or .rtf file you want to import and select **OK**. Designer then inserts the text of the file in the text box.

**To export the text from a text box**

1. Position the mouse pointer on the text, right-click and select **Save to RTF File**.
2. In the Save RTF File dialog box, specify the name of the file and select **OK**.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735564368791-Working-with-Multimedia-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports)
