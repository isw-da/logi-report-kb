---
title: "Shape Map Editor Dialog"
id: 1500010067141
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067141-Shape-Map-Editor-Dialog
updated_at: 2021-07-24T10:38:35Z
---

# Shape Map Editor Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031722-Shape-Map-Data-Binding-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067721-Show-Column-Dialog)

# Shape Map Editor Dialog

The Shape Map Editor helps you to [create and edit shape maps](https://devnet.logianalytics.com/hc/en-us/articles/1500010063881-Shape-Maps) in a report. It appears when you select Insert > Map > Shape Map, or drag the Insert Shape Map button ![Shape Map button](https://devnet.logianalytics.com/hc/article_attachments/4404901195031/btn_instmap.gif) from the Components panel to the report destination, or right-click a shape map and select Format Shape Map from the shortcut menu.

![Shape Map Editor](https://devnet.logianalytics.com/hc/article_attachments/4404909168791/mpedtr.gif)

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
     Opens the [Shape Map Canvas Setup](https://devnet.logianalytics.com/hc/en-us/articles/1500010031702-Shape-Map-Canvas-Setup-Dialog) dialog to change the width and height of the map object.
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
     Opens the [Reset All](https://devnet.logianalytics.com/hc/en-us/articles/1500010032282-Reset-All-Dialog) dialog to reset the properties for map areas including the labels and summary fields inside the areas globally.
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
     Opens the [Shape Map Data Binding Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500010031722-Shape-Map-Data-Binding-Wizard-Dialog) to bind data to the map object.
* **Format** 
  + **Conditional Formatting**  
     Opens the [Shape Map Area Conditional Formatting](https://devnet.logianalytics.com/hc/en-us/articles/1500010031682-Shape-Map-Area-Condition-Formatting-Dialog) dialog to add conditional formats to the map areas.
  + **Align**
  - **Left**  
     Aligns the content in the selected object to the left boundary of the object.
  - **Center**  
     Aligns the content in the selected object to the center of the object.
  - **Right**  
     Aligns the content in the selected object to the right boundary of the object.
  - **Justify**  
     Adjusts horizontal spacing so that the content is aligned evenly along both the left and right margins in the selected object.+ **Text Style**
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
* ![Conditional Formatting button](https://devnet.logianalytics.com/hc/article_attachments/4404901111191/btn_cndtnlfmt.gif)**Conditional Formatting**  
   Opens the Shape Map Area Conditional Formatting dialog to add conditional formats to the map areas.
* ![Font Face Box](https://devnet.logianalytics.com/hc/article_attachments/4404901109143/btn_fntface.gif)**Font Face Box**  
   Specifies the font face of the text in the selected object.
* ![Font Size box](https://devnet.logianalytics.com/hc/article_attachments/4404901109399/btn_fntsize.gif)**Font Size Box**  
   Specifies the font size of the text in the selected object.
* ![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404909111063/btn_bold.gif)**Bold**  
   Specifies whether or not to bold the text in the selected object.
* ![Italic button](https://devnet.logianalytics.com/hc/article_attachments/4404901109911/btn_italic.gif)**Italic**  
   Specifies whether or not to italicize the text in the selected object.
* ![Underline button](https://devnet.logianalytics.com/hc/article_attachments/4404909111319/btn_underline.gif)**Underline**  
   Specifies whether or not to underline the text in the selected object.
* ![Justify button](https://devnet.logianalytics.com/hc/article_attachments/4404909112727/btn_justify.gif)**Justify**  
   Adjusts horizontal spacing so that the content is aligned evenly along both the left and right margins in the selected object.
* ![Left button](https://devnet.logianalytics.com/hc/article_attachments/4404901114263/btn_left.gif)**Left**  
   Aligns the content in the selected object to the left boundary of the object.
* ![Center button](https://devnet.logianalytics.com/hc/article_attachments/4404901114519/btn_center.gif)**Center**  
   Aligns the content in the selected object to the center of the object.
* ![Right button](https://devnet.logianalytics.com/hc/article_attachments/4404909112471/btn_right.gif)**Right**  
   Aligns the content in the selected object to the right boundary of the object.
* ![Background Color button](https://devnet.logianalytics.com/hc/article_attachments/4404901110551/btn_bkgrdcolor.gif)**Background Color**  
   Specifies the background color of the selected object on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette).
* ![Foreground Color button](https://devnet.logianalytics.com/hc/article_attachments/4404901110935/btn_fntcolor.gif)**Foreground Color**  
   Specifies the foreground color of the selected object on the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500010035022-Menu-Tabs#Palette).

**Map Area Inspector**

Lists the objects in the shape map in a tree structure and the properties of the objects.

![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404909114647/btn_srch.gif)**Search**

Opens the search bar for searching properties of the selected object. The search bar is closed when you select another object.

![Qiuck Search Toolbar button](https://devnet.logianalytics.com/hc/article_attachments/4404901130263/btn_srchtlbr.gif)

* **Text box**  
   Type in the text you want to search for and the properties containing the matched text will be listed.
* ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404901130519/btn_close1.gif)  
   Clear the text in the text box.
* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404909124247/btn_srchtlbr_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.

The following shows the properties of the Area, Label, Summary and Line objects of a shape map in the Map Area Inspector panel.

## Area

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Use Global Setting | Specifies whether to apply the settings that you have set globally for all the map areas to this object.  * **true** - If selected, the object will take the global settings, and all the properties for the object will become read only. * **false**- If selected, the properties for the object can be edited if required.   Data type: Boolean |
| Area | |
| Alternate Text | Specifies the tip of the area, which is displayed when you hover the mouse pointer over the area in HTML result or in Page Report Studio. This property takes effect only when [Alternate Content Type](https://devnet.logianalytics.com/hc/en-us/articles/1500010070341-Shape-Map-Properties#Type) on the map object is set to customized and the area has data. Data type: String |
| Detail Report | Specifies the detail report that the object is linked to. Select  in the value cell to set the detail report. For details, refer to [Linking to a Detail Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports#Detail). Data type: String |
| Fill Color | Specifies the color with which to fill the area which has records. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Link | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports). Data type: String |
| Name | Specifies the name of the area. Data type: String |
| Shape | |
| Coordinates | Indicates the coordinates of the area for laying out the map. The coordinates are displayed as: X1,Y1,X2,Y2,X3,Y3... (X/Y: The X/Y coordinate of one of the polygon's corner.) This property is read only. |
| Type | Indicates the shape of the area. This property is read only. |
| Boundary | |
| Boundary Color | Specifies the color of the area border. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Boundary Style | Specifies the line style of the area border. Choose an option from the drop-down list. Data type: Enumeration |
| Boundary Width | Specifies the width of the area border. Enter a numeric value to change the width. Data type: Float |
| Accessibility | |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External TabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Enter an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |

## Label

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Use Global Setting | Specifies whether to apply the settings that you have set globally for all labels in the map to this object.  * **true** - If selected, the object will take the global settings, and all the properties for the object will become read only. * **false**- If selected, the properties for the object can be edited if required.   Data type: Boolean |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Maximum Width | Specifies the maximum width of the text displayed. Enter a numeric value to change the width. This property often works with the Auto Fit property. If Auto Fit = true and Maximum Width is not equal to 0, the text will extend until the width is this value.  Data type: Float |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Text | Specifies the text in the label. Enter a string to display as the label text. Data type: String |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the object. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the object. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the object. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the object. Enter a numeric value to change the padding. Data type: Float |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Pattern Style | Specifies the style of the pattern. Choose an option from the drop-down list.  * **none** - No pattern will be applied to the object. * **50%** - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid**- The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal**- The pattern will be made of diagonal lines of the Pattern Color.   Data type: Enumeration |
| Others | |
| Auto Connector | Specifies whether a line between the label and the area it describes will be automatically drawn when the label is dragged and dropped out of the area. Data type: Boolean |
| Invisible | Specifies whether to show the label in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Accessibility | |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External Dir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * **LTR** - Left-to-right text or table. * **RTL** - Right-to-left text or table.   Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External TabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Enter an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |

## Summary

| Property Name | Description |
| --- | --- |
| General | |
| Aggregate Function | Shows the function of the summary. This property is read only. |
| Field Type | Shows what kind of field it is. This property is read only. |
| Group By | Shows the group field that the summary is based on. If null, the summary is grouped based on the whole dataset. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Summary Name | Shows the name of the summary. This property is read only. |
| Summary On | Shows the name of the field on which to perform the summary function. This property is read only. |
| Use Global Setting | Specifies whether to apply the settings that you have set globally for all summary fields in the map to this object.  * **true** - If selected, the object will take the global settings, and all the properties for the object will become read only. * **false**- If selected, the properties for the object can be edited if required.   Data type: Boolean |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. Enter a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Foreground | Specifies the foreground color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Padding | |
| Bottom Padding | Specifies the space between the text and the bottom border of the object. Enter a numeric value to change the padding. Data type: Float |
| Left Padding | Specifies the space between the text and the left border of the object. Enter a numeric value to change the padding. Data type: Float |
| Right Padding | Specifies the space between the text and the right border of the object. Enter a numeric value to change the padding. Data type: Float |
| Top Padding | Specifies the space between the text and the top border of the object. Enter a numeric value to change the padding. Data type: Float |
| Border | |
| Border Color | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Thickness | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Right Line | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
| Shadow Color | Specifies the color of the shadow. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Top Line | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Pattern | |
| Pattern Color | Specifies the color in which to draw a pattern to fill the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| [Pattern Style](#PatternStyle) | Specifies the style of the pattern. Choose an option from the drop-down list. Data type: Enumeration |
| Text Format | |
| Auto Fit | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
| Bold | Specifies whether to make the text bold. Data type: Boolean |
| Font Face | Specifies the font of the text. Choose an option from the drop-down list. Data type: Enumeration |
| Font Size | Specifies the font size of the text. Enter an integer value to change the size. Data type: Integer |
| Format | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Note:** For the BigDecimal type, to avoid precision loss, you should enter a prefix JRD when setting the format property value. |
| Horizontal Alignment | Specifies the horizontal justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Italic | Specifies whether to make the text italic. Data type: Boolean |
| Maximum Width | Specifies the maximum width of the text displayed. Enter a numeric value to change the width. This property often works with the Auto Fit property. If Auto Fit = true and Maximum Width is not equal to 0, the text will extend until the width is this value.  Data type: Float |
| Strikethrough | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
| Underline | Specifies whether to underline the text. Data type: Boolean |
| Vertical Alignment | Specifies the vertical justification of the text in the object. Choose an option from the drop-down list. Data type: Enumeration |
| Word Wrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Others | |
| Auto Connector | Specifies whether a line between the summary and the area it describes will be automatically drawn when the summary is dragged and dropped out of the area. Data type: Boolean |
| Cache Value | Specifies whether to cache the value of the summary instead of obtaining it repeatedly. Data type: Boolean |
| Column Name | Substitutes the current summary with another summary by selecting from the drop-down list. To make the property editable, uncheck Forbid changing column in the Options dialog (**File** > **Options** > **Panel** > **Forbid changing column**).  Data type: String |
| Data Mapping File | Specifies the data mapping file to the summary [for NLS use](https://devnet.logianalytics.com/hc/en-us/articles/1500010033362-Applying-National-Language-Support). For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
| Display Null | Specifies the string to be displayed if the summary value is null. Data type: String |
| Invisible | Specifies whether to show the summary in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Accessibility | |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External Dir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * **LTR** - Left-to-right text or table. * **RTL** - Right-to-left text or table.   Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External TabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Enter an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |

## Line

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Others | |
| Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
| Line Property | |
| Line Color | Specifies the color of the line. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Line Style | Specifies the style of the line. Choose an option from the drop-down list. Data type: Enumeration |
| Line Thickness | Specifies the thickness of the line. Enter a numeric value to change the thickness. Data type: Float |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010031722-Shape-Map-Data-Binding-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067721-Show-Column-Dialog)
