---
title: "Conditional Formatting Dialog Box"
id: 5735499987863
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735499987863-Conditional-Formatting-Dialog-Box
updated_at: 2022-11-02T08:16:26Z
---

# Conditional Formatting Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735508270871-Comparison-Function-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735499997591-Connect-to-Logi-Report-Server-Dialog-Box)

# Conditional Formatting Dialog Box

You can use the Conditional Formatting dialog box to add conditional formatting [to values of the selected field](https://devnet.logianalytics.com/hc/en-us/articles/5735507243031-Working-with-DBFields#Format) or [to geographic map markers](https://devnet.logianalytics.com/hc/en-us/articles/5735564357015-Modifying-Geographic-Maps#Format). This topic describes the options in the dialog box.

Designer displays the Conditional Formatting dialog box when you select a field or geographic map in a report and then select Conditional Formatting ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/9898421373463/btn_cndtnlfmt.gif) in the Home or Format ribbon, or right-click the field or geographic map and select Conditional Formatting from the shortcut menu. Designer provides you with different options in the dialog box for adding conditional formatting [for the values of a field](#Field) or [for geographic map markers](#GMap).

---

When you use the Conditional Formatting dialog box to add conditional formatting to values of a field, Designer displays the following options in the dialog box:

![Conditional Formatting dialog box for a field](https://devnet.logianalytics.com/hc/article_attachments/9898532989335/cndtnlfmt.gif)

**Condition**

This box lists the conditions that you add to define the conditional formatting.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
  Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513701143-Edit-Conditions-Dialog-Box) to add a new condition.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif)**Edit button**  
  Select to edit the specified condition.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
  Select to delete the specified condition.
* **Priority**
  + **High**  
    Select to move a condition up for a higher priority.
  + **Low**  
    Select to move a condition down for a lower priority.

**Format**

You can specify the formatting to apply to the field values that satisfy the selected condition in this box.

* **Font**  
  Select the font face of the values.
* **Border**  
  Select the border line style of the values.
* **Size**  
  Specify the font size of the values.
* **Bold**  
  Select to apply bold formatting to the values.
* **Italic**  
  Select to italicize the values.
* **Underline**  
  Select to add a horizontal line under the values.
* **Foreground Color**  
  Specify the foreground color for the values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.
* **Background Color**  
  Specify the background color for the values.
* **Sample Text**  
  This box displays a preview sample of your selection.
* **Blinking Text**  
  Select to blink the values.
  + **Duration**  
    Specify
    how long it takes the field values to complete the transition from the foreground color to the transparent color, in seconds.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

When you use the Conditional Formatting dialog box to add conditional formatting for geographic map markers, Designer displays the following options in the dialog box:

![Conditional Formatting dialog box for geographic map](https://devnet.logianalytics.com/hc/article_attachments/9898532995223/cndtnlfmt_gmp.gif)

**Geographic Map**

This box lists all the group levels in the geographic map. Select a group level to edit conditional formatting for its markers.

**Condition**

This box lists the conditions that you add to define the conditional formatting.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**  
  Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513701143-Edit-Conditions-Dialog-Box) to add a new condition.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/9898474047383/btn_edit.gif)**Edit button**  
  Select to edit the specified condition.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**  
  Select to delete the specified condition.
* **Priority**
  + **High**  
    Select to move a condition up for a higher priority.
  + **Low**  
    Select to move a condition down for a lower priority.

**Marker**

You can specify the settings to apply to the markers that satisfy the selected condition in this box.

* **Image**  
  Specify the image of the markers. You can type the URL for a web image or select **Browse** to specify a local image.
  + **Width**  
    Specify the width of the foreground image.
  + **Height**  
    Specify the height of the foreground image.
* **Shadow**  
  Designer displays this option only when the geographic map applies one of the Google Maps types. Type the URL for a web image or select **Browse** to specify a local image as the shadow image of the markers.
  + **Width**  
    Specify the width of the shadow image.
  + **Height**  
    Specify the height of the shadow image.

**Constrain Proportions**

If you select this option, when you set the width or height of the marker image/shadow, Designer adjusts the other accordingly in a certain proportion.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735508270871-Comparison-Function-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735499997591-Connect-to-Logi-Report-Server-Dialog-Box)
