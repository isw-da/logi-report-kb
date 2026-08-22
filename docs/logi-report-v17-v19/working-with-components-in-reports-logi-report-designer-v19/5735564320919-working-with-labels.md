---
title: "Working with Labels"
id: 5735564320919
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735564320919-Working-with-Labels
updated_at: 2022-11-02T04:13:09Z
---

# Working with Labels

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields)

# Working with Labels

A label is an object containing a string, which is typically a brief description used to identify a field or other value nearby. This topic describes how you can insert and format labels in a report.

For the labels in a report, you can use them as the trigger object of [links](https://devnet.logianalytics.com/hc/en-us/articles/5735569846807-Adding-Links-in-a-Report), and change their [display types](https://devnet.logianalytics.com/hc/en-us/articles/5735555544087-Changing-the-Display-Type-of-Objects-in-a-Report) if you want.

This topic contains the following sections:

* [Inserting Labels in a Report](#Insert)
* [Formatting the Labels in a Report](#Format)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the label component example, open `<install_root>\Demo\Reports\SampleComponents\ForLabel.cls`.

## Inserting Labels in a Report

You can insert labels in the report areas listed in [Component Placement in Different Report Type](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type).

To insert a label in a report, use either of the following methods:

* From the **Components** panel, drag the **Label** icon ![Label icon](https://devnet.logianalytics.com/hc/article_attachments/9898518363799/icon_label.gif) in the **Basic** category to the destination in the report.
* Navigate to **Insert** > **Label** or **Home** > **Insert** > **Label**, then select in the location where you want to display the label.

Designer inserts a label with the default text "Label". You can then edit the text of a label.

* To edit the full text of a label, double-click the label to select the text, then type the replacement text.
* To edit a portion of a label's text, double-click the label, then select in the label and drag to select the portion, after that, type the replacement text.

You can also modify a label's text by using the **Text** property value in the Report Inspector.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can neither drag nor use the Insert menu to insert labels into charts. For more information about chart labels, see [Formatting Chart Labels](https://devnet.logianalytics.com/hc/en-us/articles/5735563973015-Formatting-Chart-Labels).

## Formatting the Labels in a Report

You can format the label text using options in the **Format** ribbon, for example, you can change the font size, color, and alignment of the text.

To format a label, first select the label, then perform any of the following operations:

* To change the alignment of a label, select the required alignment button: **Justify**![Justify button](https://devnet.logianalytics.com/hc/article_attachments/9898421616407/btn_justify.gif), **Left**![Left button](https://devnet.logianalytics.com/hc/article_attachments/9898404853783/btn_left.gif), **Center**![Center button](https://devnet.logianalytics.com/hc/article_attachments/9898421585047/btn_center.gif) or **Right**![Right button](https://devnet.logianalytics.com/hc/article_attachments/9898421600919/btn_right.gif). Designer then aligns the text in the label according to your selection.
* To change the font face, select **Font Face Box**![Font Face Box button](https://devnet.logianalytics.com/hc/article_attachments/9898421183895/btn_fntface.gif) and then select the required font from the drop-down list. The fonts introduced with "\*" are True Type Fonts. For more information, see [Applying True Type Fonts in Reports](https://devnet.logianalytics.com/hc/en-us/articles/5735534328983-Applying-True-Type-Fonts-in-Reports).
* To change the font size, select **Font Size Box**![Font Size Box button](https://devnet.logianalytics.com/hc/article_attachments/9898404573079/btn_fntsize.gif) and then select the required size from the drop-down list (or type the required value in the text box and then select **Enter** on the keyboard).
* To change the font style, select the corresponding font style buttons: **Bold**![Bold button](https://devnet.logianalytics.com/hc/article_attachments/9898404597399/btn_bold.gif), **Italic**![Italic button](https://devnet.logianalytics.com/hc/article_attachments/9898404620951/btn_italic.gif), and **Underline**![Underline button](https://devnet.logianalytics.com/hc/article_attachments/9898404633623/btn_underline.gif).
* To change the background color of the label, select **Background Color**![Background Color button](https://devnet.logianalytics.com/hc/article_attachments/9898404661271/btn_bkgrdcolor.gif) ; to change the foreground color of the label text, select **Foreground Color**![Foreground Color button](https://devnet.logianalytics.com/hc/article_attachments/9898404672663/btn_fntcolor.gif).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735507271831-Working-with-KPIs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields)
