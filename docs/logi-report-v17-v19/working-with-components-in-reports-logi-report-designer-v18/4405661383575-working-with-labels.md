---
title: "Working with Labels"
id: 4405661383575
section: "Working with Components in Reports - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661383575-Working-with-Labels
updated_at: 2022-01-27T20:34:30Z
---

# Working with Labels

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661382551-Working-with-KPIs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields)

# Working with Labels

A label is an object containing a string, which is typically a brief description used to identify a field or other value nearby. This topic describes how you can insert and format labels in a report.

For the labels in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/4405661930647-Changing-the-Display-Type-of-Objects-in-Reports) if you want.

This topic contains the following sections:

* [Inserting Labels in a Report](#Insert)
* [Formatting the Labels in a Report](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the label component example, open `<install_root>\Demo\Reports\SampleComponents\ForLabel.cls`.

## Inserting Labels in a Report

You can insert labels in the report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/4405664365463-Working-with-Components-in-Reports#Relationship).

**To insert a label in a report**

* From the **Components** panel, drag the **Label** icon ![Label icon](https://devnet.logianalytics.com/hc/article_attachments/4420542198807/icon_label.gif) in the **Basic** category to the desired report destination.
* Navigate to **Insert** > **Label** or **Home** > **Insert** > **Label**, then select in the location where you want to display the label.

Designer inserts a label with the default text "Label". You can then edit the text of a label.

* To edit the full text of a label, double-click the label to select the text, then type the replacement text.
* To edit a portion of a label's text, double-click the label, then select in the label and drag to select the portion, after that, type the replacement text.

You can also modify a label's text by using the **Text** property value in the Report Inspector.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) You can neither drag nor use the Insert menu to insert labels into charts. For more information about chart labels, see [Formatting the Labels](https://devnet.logianalytics.com/hc/en-us/articles/4405664380951-Formatting-the-Labels).

## Formatting the Labels in a Report

You can format the label text with the **Format** menu tab of the Designer main window, for example, you can change the font size, color, and alignment of the text.

To format a label, first select the label, and then perform any of the following operations:

* To change the alignment of a label, select the required alignment button: **Justify**![Justify button](https://devnet.logianalytics.com/hc/article_attachments/4420542060823/btn_justify.gif), **Left**![Left button](https://devnet.logianalytics.com/hc/article_attachments/4420542060183/btn_left.gif), **Center**![Center button](https://devnet.logianalytics.com/hc/article_attachments/4420556081687/btn_center.gif) or **Right**![Right button](https://devnet.logianalytics.com/hc/article_attachments/4420542060567/btn_right.gif). Designer then aligns the text in the label according to your selection.
* To change the font face, select **Font Face Box**![Font Face Box button](https://devnet.logianalytics.com/hc/article_attachments/4420550809367/btn_fntface.gif) and then select the required font from the drop-down list. The fonts introduced with "\*" are True Type Fonts. For more information, see [Applying True Type Fonts in Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405661940119-Applying-True-Type-Fonts-in-Reports).
* To change the font size, select **Font Size Box**![Font Size Box button](https://devnet.logianalytics.com/hc/article_attachments/4420556076951/btn_fntsize.gif) and then select the required size from the drop-down list (or type the required value in the text box and then select **Enter** on the keyboard).
* To change the font style, select the corresponding font style buttons on the Format menu tab: **Bold**![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4420556077591/btn_bold.gif), **Italic**![Italic button](https://devnet.logianalytics.com/hc/article_attachments/4420550810391/btn_italic.gif), and **Underline**![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4420556077847/btn_underline.gif).
* To change the background color of the label, select **Background Color**![Background Color button](https://devnet.logianalytics.com/hc/article_attachments/4420556078231/btn_bkgrdcolor.gif) on the Format menu tab; to change the foreground color of the label text, select **Foreground Color**![Foreground Color button](https://devnet.logianalytics.com/hc/article_attachments/4420556078487/btn_fntcolor.gif).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661382551-Working-with-KPIs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664395799-Working-with-DBFields)
