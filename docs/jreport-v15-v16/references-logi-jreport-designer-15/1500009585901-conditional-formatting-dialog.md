---
title: "Conditional Formatting Dialog"
id: 1500009585901
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585901-Conditional-Formatting-Dialog
updated_at: 2021-07-24T05:55:34Z
---

# Conditional Formatting Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585881-Comparison-Function-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585921-Connect-to-JReport-Server-Dialog)

# Conditional Formatting Dialog

The Conditional Formatting dialog appears when you select a field/geographic map and then select Format > Conditional Formatting, or select the Conditional Formatting button**![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404889280535/btn_cndtnlfmt.gif)** on the toolbar, or right-click the field/geographic map and select Conditional Formatting from the shortcut menu. It helps you to add some conditional formats to [values of the selected field](https://devnet.logianalytics.com/hc/en-us/articles/1500009583921-DBFields#Format) or [markers of specific group levels in a geographic map](https://devnet.logianalytics.com/hc/en-us/articles/1500009584081-Adding-Conditional-Formats-to-Geographic-Map-Markers). The options in the dialog vary according to different sources it is opened from.

When you select a field to open the dialog, the options in the dialog are as follows. [See the dialog](javascript:%20void(null)).

![Conditional Formatting dialog for a field](https://devnet.logianalytics.com/hc/article_attachments/4404893948695/cndtnlfmt.gif)

**Condition**

Displays all the conditions you have already added.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new condition in the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog) dialog.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
   Edits the selected condition.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected condition.
* **Priority**  
   Specifies the priority of each condition.
  + **High**  
     Moves a condition up for a higher priority.
  + **Low**  
     Moves a condition down for a lower priority.

**Format**

Specifies the format which will be applied to the field values when the specified condition is fulfilled.

* **Font**  
   Specifies the font type for the field values.
* **Border**  
   Specifies the border line style for the field values.
* **Size**  
   Specifies the font size for the field values.
* **Bold**  
   Specifies whether or not to bold the field values.
* **Italic**  
   Specifies whether or not to make the field values italic.
* **Underline**  
   Specifies whether or not to underline the field values.
* **Foreground Color**  
   Specifies the foreground color for the field values. To edit the color, select the color image and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color directly in the text box.
* **Background Color**  
   Specifies the background color for the field values.
* **Sample Text**  
   Displays a preview sample of your selection.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

When you select a geographic map to open the dialog, the options in the dialog are as follows. [See the dialog](javascript:%20void(null)):

![Conditional Formatting dialog for geographic map](https://devnet.logianalytics.com/hc/article_attachments/4404893948951/cndtnlfmt_gmp.gif)

**Geographic Map**

Lists all the group levels in the geographic map.

**Condition**

Displays all the conditions you have already added.

* ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)  
   Adds a new condition in the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009586381-Edit-Conditions-Dialog) dialog.
* ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif)  
   Edits the selected condition.
* ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)  
   Removes the selected condition.
* **Priority**  
   Specifies the priority of each condition.
  + **High**  
     Moves a condition up for a higher priority.
  + **Low**  
     Moves a condition down for a lower priority.

**Marker**

Specifies the properties of the marker. Available only when there is at least one condition in the Condition box.

* **Image**  
   Specifies the image of the marker. Input the URL for a web image or select Browse button to specify a local image.
  + **Width**  
     Specifies the width of the foreground image.
  + **Height**  
     Specifies the height of the foreground image.
* **Shadow**  
   Specifies the shadow image of the marker. Input the URL for a web image or select Browse button to specify a local image.
  Only available for Google Maps types.
  + **Width**  
     Specifies the width of the shadow image.
  + **Height**  
     Specifies the height of the shadow image.

**Constrain Proportions**

Specifies whether to change the width and height for the marker image/shadow at the same time in a certain proportion. If checked, when the width/height is changed, the height/width will also be changed in a certain proportion.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585881-Comparison-Function-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585921-Connect-to-JReport-Server-Dialog)
