---
title: "Shape Map Editor Dialog"
id: 1500009566742
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566742-Shape-Map-Editor-Dialog
updated_at: 2021-07-24T05:55:02Z
---

# Shape Map Editor Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566722-Shape-Map-Data-Binding-Wizard-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567362-Show-Column-Dialog)

# Shape Map Editor Dialog

This editor appears when you select Insert > Map > Shape Map, or drag the Insert Shape Map button ![Shape Map button](https://devnet.logianalytics.com/hc/article_attachments/4404893865367/btn_instmap.gif) from the Components panel to the report destination, or right-click a shape map and select Format Shape Map from the shortcut menu. It helps you to [insert a shape map](https://devnet.logianalytics.com/hc/en-us/articles/1500009584141-Inserting-a-Shape-Map) into a report, or to edit an existing shape map. [See the editor](javascript:%20void(null)).

![Shape Map Editor window](https://devnet.logianalytics.com/hc/article_attachments/4404893865623/mpedtr.gif)

The following are details about options in the editor:

**Menu**

* **File**
  + **Open**  
    Specifies to import a .shp or .xml file which has been defined with some area information to the map object.
  + **Save**  
    Accepts and saves the changes on the map object.
  + **Save As**  
    Saves the map object to an .xml file with the name you specify.
  + **Canvas Setup**  
    Opens the [Shape Map Canvas Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500009587821-Shape-Map-Canvas-Setup-Dialog) dialog to change the width and height of the map object.
  + **Close**  
    Closes the window.
* **Edit**
  + **Undo**  
    Reverses a previous action.
  + **Redo**  
    The counter-operation of Undo.
  + **Cut**  
    Erases an object and places it in the clipboard.
  + **Copy**  
    Copies an object and places it in the clipboard.
  + **Paste**  
    Takes an object from the clipboard and places it into the report.
  + **Delete**  
    Deletes a selected object.
  + **Insert Mode**  
    If checked, the window is in insert mode, and you can add areas into the map manually; if unchecked, the window is in edit mode, and you can edit areas as required.
  + **Reset All**  
    Opens the [Reset All](https://devnet.logianalytics.com/hc/en-us/articles/1500009567262-Reset-All-Dialog) dialog to reset the properties for map areas including the labels and summary fields inside the areas globally.
  + **Hide Duplicate Labels**  
    If selected, for map areas with the same name, only the label and summary field for the biggest area will be shown.
* **View**
  + **Show Area Inspector**  
    Specifies whether or not to show the Map Area Inspector panel in the Shape Map Editor.
  + **Show Area Labels**  
    Specifies whether or not to show labels and summary fields in map areas in the Shape Map Editor.
* **Insert** 
  + **Background Image**  
    Specifies to select an image as background of the map.
  + **Match Background Image**  
    Resizes the map object to make it match the size of the background image. Activated only when the size of the background image is not the same as that of the map object.
  + **Label**  
    Inserts a label to the map object.
  + **Line**  
    Inserts a line to the map object.
  + **Bind Data**  
    Opens the [Shape Map Data Binding Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009566722-Shape-Map-Data-Binding-Wizard-Dialog) to bind data to the map object.
* **Format** 

  - **Conditional Formatting**  
    Opens the [Shape Map Area Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500009587801-Shape-Map-Area-Condition-Formatting-Dialog) dialog to add some conditional formats to the map areas.+ **Align**
    - **Left**  
      Aligns the content in the selected object to the left boundary of the object.
    - **Center**  
      Aligns the content in the selected object to the center of the object.
    - **Right**  
      Aligns the content in the selected object to the right boundary of the object.
    - **Justify**  
      Adjusts horizontal spacing so that the content is aligned evenly along both the left and right margins in the selected object.
  + **Text Style**
    - **Bold**  
      Specifies whether or not to bold the text in the selected object.
    - **Italic**  
      Specifies whether or not to italicize the text in the selected object.
    - **Underline**  
      Specifies whether or not to underline the text in the selected object
* **Help**  
  Displays the help document about this feature.

**Toolbar**

The following are commands on the toolbar:

* **Open**  
  Specifies to import a .shp or .xml file which has been defined with some area information to the map object.
* **Save**  
  Accepts and saves the changes on the map object.
* **Canvas Setup**  
  Opens the Map Canvas Setup dialog to change the width and height of the map object.
* **Cut**  
  Erases an object and places it on the clipboard.
* **Copy**  
  Copies an object and places it on the clipboard.
* **Paste**  
  Takes an object from the clipboard and places it into the map object.
* **Delete**  
  Deletes a selected object.
* **Undo**  
  Reverses a previous action.
* **Redo**  
  The counter-operation of Undo.
* **Insert Mode**  
  If pressed, the window is in insert mode, and you can insert areas into the map; otherwise, the window is in edit mode, and you can edit the map areas.
* **Line**  
  Inserts a line into the map object.
* **Bind Data**  
  Opens the Map Data Binding Wizard to bind data to the map areas.
* ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404889280535/btn_cndtnlfmt.gif)**Conditional Formatting**  
  Opens the Shape Map Area Conditional Formatting dialog to add some conditional formats to the map areas.
* ![Font Face Box](https://devnet.logianalytics.com/hc/article_attachments/4404893794583/btn_fntface.gif)**Font Face Box**  
  Specifies the font face of the text in the selected object.
* ![Font Size box](https://devnet.logianalytics.com/hc/article_attachments/4404893794839/btn_fntsize.gif)**Font Size Box**  
  Specifies the font size of the text in the selected object.
* ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404889279511/btn_bold.gif)**Bold**  
  Specifies whether or not to bold the text in the selected object.
* ![Italic button](https://devnet.logianalytics.com/hc/article_attachments/4404889279767/btn_italic.gif)**Italic**  
  Specifies whether or not to italicize the text in the selected object.
* ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4404893795095/btn_underline.gif)**Underline**  
  Specifies whether or not to underline the text in the selected object.
* ![Justify button](https://devnet.logianalytics.com/hc/article_attachments/4404893865879/btn_justify.gif)**Justify**  
  Adjusts horizontal spacing so that the content is aligned evenly along both the left and right margins in the selected object.
* ![Left button](https://devnet.logianalytics.com/hc/article_attachments/4404893798551/btn_left.gif)**Left**  
  Aligns the content in the selected object to the left boundary of the object.
* ![Center button](https://devnet.logianalytics.com/hc/article_attachments/4404889281815/btn_center.gif)**Center**  
  Aligns the content in the selected object to the center of the object.
* ![Right button](https://devnet.logianalytics.com/hc/article_attachments/4404889282071/btn_right.gif)**Right**  
  Aligns the content in the selected object to the right boundary of the object.
* ![Background Color button](https://devnet.logianalytics.com/hc/article_attachments/4404893795351/btn_bkgrdcolor.gif)**Background Color**  
  Specifies the background color of the selected object on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette).
* ![Foreground Color button](https://devnet.logianalytics.com/hc/article_attachments/4404893795607/btn_fntcolor.gif)**Foreground Color**  
  Specifies the foreground color of the selected object on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009593081-Menu-Tabs#Palette).

**Map Area Inspector**

On the right part of the Shape Map Editor, there is a Map Area Inspector panel, where you can control properties of any [area](https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map), [label](https://devnet.logianalytics.com/hc/en-us/articles/1500009591561-Properties-of-Label-in-Page-Report-Shape-Map), [summary field](https://devnet.logianalytics.com/hc/en-us/articles/1500009591581-Properties-of-Summary-Field-in-Page-Report-Shape-Map) and [line](https://devnet.logianalytics.com/hc/en-us/articles/1500009569682-Properties-of-Line-in-Page-Report-Shape-Map) in the map object.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404893807511/btn_srch.gif)**Search**

Opens the quick search toolbar for searching map object properties. The search toolbar is closed when you select another object.

![Qiuck Search Toolbar button](https://devnet.logianalytics.com/hc/article_attachments/4404889288855/btn_srchtlbr.gif)

* **Text box**  
  The quick search toolbar treats resource names as strings and searches by consecutive text. Type in the text you want to search for in the text box and the resources containing the matched text will be listed.
* **X**  
  Clear the text in the text box.
* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404889289239/btn_srchtlbr_adv.gif)  
  Lists more search options.
  + **Highlight All**   
    Specifies whether to highlight all matched text.
  + **Match Case**   
    Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
    Specifies whether to search for text that looks the same as the typed text.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566722-Shape-Map-Data-Binding-Wizard-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567362-Show-Column-Dialog)
