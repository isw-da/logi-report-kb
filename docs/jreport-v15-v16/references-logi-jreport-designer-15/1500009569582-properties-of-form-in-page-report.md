---
title: "Properties of Form in Page Report"
id: 1500009569582
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569582-Properties-of-Form-in-Page-Report
updated_at: 2021-07-24T05:54:12Z
---

# Properties of Form in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569562-Properties-of-Filter-Control-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591481-Properties-of-Formula-Field-in-Page-Report)

# Properties of Form in Page Report

The properties of a form object in a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Form | |
| Disabled | Specifies whether the user can interact with the form. Data type: Boolean |
| Form Action | Specifies the URL to which the form content is sent for processing. Data type: String |
| Form ID | Specifies the string identifying the form. Data type: String |
| Form Method | Specifies how to send the form data to the server. Choose an option from the drop-down list.  * **get** - Appends the arguments to the Form Action URL and opens it as if it were an anchor. * **post** - Sends the data through an HTTP post transaction.   Data type: Enumeration |
| Form Name | Specifies the name of the form. Data type: String |
| Form Target | Specifies the window or frame at which to target contents. Choose an option from the drop-down list.  * **default** - Loads the linked document into the window in which the link is selected (the active window). Same as "self". * **blank** - Loads the linked document into a new blank window. This window is not named. * **media** - Loads the linked document into the HTML content area of the Media Bar. Available in Microsoft Internet Explorer 6 or later. * **parent** - Loads the linked document into the immediate parent window of the active window. If there is no parent window, the active window is used. * **search** - Loads the linked document into the browser search page. Available in Internet Explorer 5 or later. * **self** - Loads the linked document into the window in which the link is selected (the active window). * **top** - Loads the linked document into the topmost window.   Data type: Enumeration |
| Accessibility | |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569562-Properties-of-Filter-Control-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591481-Properties-of-Formula-Field-in-Page-Report)
