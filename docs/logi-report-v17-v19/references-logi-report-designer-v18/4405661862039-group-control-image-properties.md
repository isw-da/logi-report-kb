---
title: "Group Control Image Properties"
id: 4405661862039
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661862039-Group-Control-Image-Properties
updated_at: 2022-01-27T20:38:05Z
---

# Group Control Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661860503-GMarker-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661863319-Image-Properties)

# Group Control Image Properties

This topic describes the properties of a Group Control Image object, that is, the [Expand/Collapse Group web control](https://devnet.logianalytics.com/hc/en-us/articles/4405661411351-Using-Advanced-Web-Controls#Expand) that you can use in banded objects in page reports only.

| Property Name | Description |
| --- | --- |
| General **(available when the object is in a query-based page report)** | |
| Class Type | Shows the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | |
| Background | Specifies the background color or fill effect of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Position) | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Attribute | |
| Access Key | Specifies the accelerator key for the object. Data type: String |
| Alternate Text | Specifies the text you want to show instead when the object cannot display. Data type: String |
| Checked | Specifies whether the object is selected. Data type: Boolean |
| Class | This property is typically used to associate a particular style rule in a style sheet with the object. Data type: String |
| Direction | Specifies a value that indicates the reading order of the object. Data type: String |
| Disabled | Shows if the image is disabled. This property is read only. |
| ID | Specifies the identifier of the object, which must be unique in the report. You can type a style sheet selector as the value. Data type: String |
| Name | Specifies the name of the object. Data type: String |
| Size | Specifies the size of the object, in pixels. Data type: Integer |
| Source | Shows the URL you specify to load from the object. This property is read only. |
| Tab Index | Specifies the index that defines the tab order for the object. Data type: Integer |
| Title | Specifies the tool tip information of the object, which displays when you hover over the object in HTML output or at runtime. Data type: String |
| Value | Specifies the initial value of the object. Data type: String |
| [Event](https://devnet.logianalytics.com/hc/en-us/articles/4405661863319-Image-Properties#Event) | |
| On Blur | Specifies the action you want to trigger from the object at runtime when the object loses input focus. Data type: String |
| On Change | Specifies the action you want to trigger from the object at runtime when the content of the object or selection is changed. Data type: String |
| On Click | Specifies the action you want to trigger from the object at runtime when the user selects the left mouse button on the object. Data type: String |
| On Double click | Specifies the action you want to trigger from the object at runtime when the user double-clicks the object. Data type: String |
| On Focus | Specifies the action you want to trigger from the object at runtime when the object receives focus. Data type: String |
| On Key Down | Specifies the action you want to trigger from the object at runtime when the user presses a key. Data type: String |
| On Key Press | Specifies the action you want to trigger from the object at runtime when the user presses an alphanumeric key. Data type: String |
| On Key Up | Specifies the action you want to trigger from the object at runtime when the user releases a key. Data type: String |
| On Mouse Down | Specifies the action you want to trigger from the object at runtime when the user selects the object with either mouse button. Data type: String |
| On Mouse Move | Specifies the action you want to trigger from the object at runtime when the user moves the mouse over the object. Data type: String |
| On Mouse Out | Specifies the action you want to trigger from the object at runtime when the user moves the mouse pointer outside the boundaries of the object. Data type: String |
| On Mouse Over | Specifies the action you want to trigger from the object at runtime when the user moves the mouse pointer into the object. Data type: String |
| On Mouse Up | Specifies the action you want to trigger from the object at runtime when the user releases a mouse button while the mouse is over the object. Data type: String |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML)**(available when the object is in a query-based page report)** | |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661860503-GMarker-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661863319-Image-Properties)
