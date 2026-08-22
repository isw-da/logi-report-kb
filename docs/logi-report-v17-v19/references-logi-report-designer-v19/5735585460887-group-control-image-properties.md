---
title: "Group Control Image Properties"
id: 5735585460887
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735585460887-Group-Control-Image-Properties
updated_at: 2022-11-02T08:16:03Z
---

# Group Control Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569010583-GMarker-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735533272087-Image-Properties)

# Group Control Image Properties

This topic describes the properties of a Group Control Image object, that is, the [Expand/Collapse Group web control](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Expand) that you can use in banded objects in page reports only.

| Property Name | Description |
| --- | --- |
| General **(available when the object is in a query-based page report)** | |
| Class Type | Shows the class type of the object. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Color | |
| Background | Specifies the background color or fill effect of the object. Choose a color from the drop-down list, or select **Custom** to customize a color in the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/5735555208983-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/5735534157079-Editing-Reports#Position) | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Attribute | |
| Access Key | Specifies the accelerator key for the object. Data type: String |
| Alternate Text | Specifies the text you want to show instead when the object cannot display. Data type: String |
| Checked | Specifies whether the object is selected. Data type: Boolean |
| Class | This property is typically used to associate a particular style rule in a style sheet with the object. Data type: String |
| Direction | Specifies a value that indicates the reading order of the object. Data type: String |
| Disabled | Shows if the image is disabled. Read only. |
| ID | Specifies the identifier of the object, which must be unique in the report. You can type a style sheet selector as the value. Data type: String |
| Name | Specifies the name of the object. Data type: String |
| Size | Specifies the size of the object, in pixels. Data type: Integer |
| Source | Shows the URL you specify to load from the object. Read only. |
| Tab Index | Specifies the index that defines the tab order for the object. Data type: Integer |
| Title | Specifies the tool tip that displays when you point to the object in HTML output or at runtime. Data type: String |
| Value | Specifies the initial value of the object. Data type: String |
| [Event](https://devnet.logianalytics.com/hc/en-us/articles/5735533272087-Image-Properties#Event) | |
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
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML)**(available when the object is in a query-based page report)** | |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735569010583-GMarker-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735533272087-Image-Properties)
