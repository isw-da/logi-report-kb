---
title: "Group Control Image Properties"
id: 1500009612042
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009612042-Group-Control-Image-Properties
updated_at: 2021-07-24T16:03:40Z
---

# Group Control Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612022-Group-Header-Panel-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612082-Body-Properties)

# Group Control Image Properties

This topic lists the properties of a Group Control Image object, which is supported in banded objects in page reports only.

| Property Name | Description |
| --- | --- |
| General (only supported on banded objects created using query resources) | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Height | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Type a numeric value to change the position. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009635501-Label-Properties#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Type a valid class name from the CSS file.   Data type: String |
| Others | |
| Export to Report Result | Specifies whether to include the object when previewing the report in Page Report Result and running the report in Page Report Studio. Data type: Boolean |
| Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009613302-Editing-Reports#Position) | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Attribute | |
| Access Key | Specifies the accelerator key for the object. Data type: String |
| Alternate Text | Specifies the text that will be displayed if the object cannot be displayed. Data type: String |
| Checked | Specifies whether the object is checked. Data type: Boolean |
| Class | This property is typically used to associate a particular style rule in a style sheet with the object. Data type: String |
| Direction | Specifies a value that indicates the reading order of the object. Data type: String |
| Disabled | Indicates if the image is disabled. This property is read only. |
| ID | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
| Name | Specifies the name of the image. Data type: String |
| Size | Specifies the size of the object, in pixels. Data type: Integer |
| Source | Displays the URL to be loaded by the object. This property is read only. |
| Tab Index | Specifies the index that defines the tab order for the image. Data type: Integer |
| Title | Specifies the tip information about the image, which will be displayed when you hover the mouse pointer over the image after the report is exported to HTML or Page Report Result. Data type: String |
| Value | Specifies the text displayed in the image field. Data type: String |
| Event | |
| [On Blur](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the object loses input focus. Data type: String |
| [On Change](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the contents of the object or selection have changed. Data type: String |
| [On select](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user selects the left mouse button on the object. Data type: String |
| [On Double click](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user double-clicks the object. Data type: String |
| [On Focus](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the object receives focus. Data type: String |
| [On Key Down](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user presses a key. Data type: String |
| [On Key Press](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user presses an alphanumeric key. Data type: String |
| [On Key Up](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user releases a key. Data type: String |
| [On Mouse Down](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user selects the object with either mouse button. Data type: String |
| [On Mouse Move](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user moves the mouse over the object. Data type: String |
| [On Mouse Out](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user moves the mouse pointer outside the boundaries of the object. Data type: String |
| [On Mouse Over](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user moves the mouse pointer into the object. Data type: String |
| [On Mouse Up](https://devnet.logianalytics.com/hc/en-us/articles/1500009612342-Image-Properties#Event) | Specifies the action when the user releases a mouse button while the mouse is over the object. Data type: String |
| Accessibility (only supported on banded objects created using query resources) | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Type a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009612022-Group-Header-Panel-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009612082-Body-Properties)
