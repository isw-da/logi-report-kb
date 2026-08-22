---
title: "Conditional Formatting Dialog Box"
id: 1500010058242
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010058242-Conditional-Formatting-Dialog-Box
updated_at: 2021-07-23T19:15:06Z
---

# Conditional Formatting Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058222-Comparison-Function-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box)

# Conditional Formatting Dialog Box

You can use the Conditional Formatting dialog box to add conditional formats [to values of the selected field](https://devnet.logianalytics.com/hc/en-us/articles/1500010057202-Working-with-DBFields#Format) or [to markers of specific group levels in a geographic map](https://devnet.logianalytics.com/hc/en-us/articles/1500010057362-Modifying-Geographic-Maps#Format). This topic describes the options in the dialog box.

Designer displays the Conditional Formatting dialog box when you select a field or geographic map in a report and then select the Conditional Formatting button ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404856793111/btn_cndtnlfmt.gif) on the Home/Format menu tab, or right-click the field or geographic map and select Conditional Formatting from the shortcut menu. Designer provides you with different options in the dialog box for adding conditional formats [for the values of a field](#Field) or [for geographic map markers](#GMap).

---

When you use the Conditional Formatting dialog box to add conditional formats to the values of a field, Designer displays the following options in the dialog box:

![Conditional Formatting dialog box for a field](https://devnet.logianalytics.com/hc/article_attachments/4404857004055/cndtnlfmt.gif)

**Condition**

The box lists the conditions that you add to define the conditional formats.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box) to add a new condition.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
  Select to edit the specified condition.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified condition.
* **Priority**
  + **High**  
    Select to move a condition up for a higher priority.
  + **Low**  
    Select to move a condition down for a lower priority.

**Format**

You can specify the format to apply to the field values when the specified condition is fulfilled in this box.

* **Font**  
  Select the font type for the field values.
* **Border**  
  Select the border line style for the field values.
* **Size**  
  Specify the font size for the field values.
* **Bold**  
  Select to make the field values in bold style.
* **Italic**  
  Select to italicize the field values.
* **Underline**  
  Select to add a horizontal line under the field values.
* **Foreground Color**  
  Specify the foreground color for the field values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010062922-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.
* **Background Color**  
  Specify the background color for the field values.
* **Sample Text**  
  The box displays a preview sample of your selection.
* **Blinking Text**  
  Select to blink the field values.
  + **Duration**  
    Specify
    how long it takes the field values to complete the transition from the foreground color to the transparent color, in seconds.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

When you use the Conditional Formatting dialog box to add conditional formats for geographic map markers, Designer displays the following options in the dialog box:

![Conditional Formatting dialog box for geographic map](https://devnet.logianalytics.com/hc/article_attachments/4404848624663/cndtnlfmt_gmp.gif)

**Geographic Map**

The box lists all the group levels in the geographic map. Select a group level to edit conditional formats for its markers.

**Condition**

The box lists the conditions that you add to define the conditional formats.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**  
  Select to open the [Edit Conditions dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058702-Edit-Conditions-Dialog-Box) to add a new condition.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404856829719/btn_edit.gif)**Edit button**  
  Select to edit the specified condition.
* ![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**  
  Select to delete the specified condition.
* **Priority**
  + **High**  
    Select to move a condition up for a higher priority.
  + **Low**  
    Select to move a condition down for a lower priority.

**Marker**

You can specify the properties of the markers when the specified condition is fulfilled in this box.

* **Image**  
  Specify the image of the markers. Type the URL for a web image or select the Browse button to specify a local image.
  + **Width**  
    Specify the width of the foreground image.
  + **Height**  
    Specify the height of the foreground image.
* **Shadow**  
  Designer displays the option only when the geographic map applies one of the Google Maps types. Type the URL for a web image or select the Browse button to specify a local image as the shadow image of the markers.
  + **Width**  
    Specify the width of the shadow image.
  + **Height**  
    Specify the height of the shadow image.

**Constrain Proportions**

If you select the option, when you set the width or height of the marker image/shadow, Designer adjusts the other accordingly in a certain proportion.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010058222-Comparison-Function-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095741-Connect-to-Logi-Report-Server-Dialog-Box)
