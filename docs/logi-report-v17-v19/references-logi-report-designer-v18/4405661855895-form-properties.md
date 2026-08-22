---
title: "Form Properties"
id: 4405661855895
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661855895-Form-Properties
updated_at: 2022-01-27T20:38:16Z
---

# Form Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661853847-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661854871-Formula-Field-Properties)

# Form Properties

This topic describes the properties of a [Form object](https://devnet.logianalytics.com/hc/en-us/articles/4405661413527-Using-Forms-in-a-Page-Report) that you can use in page reports only.

| Property Name | Description |
| --- | --- |
| General **(available when the object is in a query-based page report)** | |
| Class Type | Shows the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| CSS | |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the [Style Group](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) property for the page report tab, and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | |
| Logic Column | Designer displays this property when the object is in a table. You can use it to specify whether to show the object in the next visible table cell in the same row when the column that holds the object is hidden. Choose an option from the drop-down list. Data type: Enumeration  Note icon   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When you set this property for several objects in the same row to "next visible column", and the columns holding these objects are all hidden, only the object in the rightmost column shows in the next visible cell. |
| Form | |
| Disabled | Specifies whether to disable user interaction with the form. Data type: Boolean |
| Form Action | Specifies the URL to which to send the form content for processing. Data type: String |
| Form ID | Specifies the string for identifying the form. Data type: String |
| Form Method | Specifies how to send the form data to Server. Choose an option from the drop-down list.  * **get** - Select to append the arguments to the Form Action URL and open it as if it were an anchor. * **post** - Select to send the data through an HTTP post transaction.   Data type: Enumeration |
| Form Name | Specifies the name of the form. Data type: String |
| Form Target | Specifies the window or frame to load the form content at runtime. Choose an option from the drop-down list.  * **default** - Select to load the content into the window in which the link is selected (the active window). This option is the same as "self". * **blank** - Select to load the content into a new blank window. This window is not named. * **media** - Select to load the content into the HTML content area of the Media Bar. Available in Microsoft Internet Explorer 6 or later. * **parent** - Select to load the content into the immediate parent window of the active window. If there is no parent window, the active window is used. * **search** - Select to load the content into the browser search page. Available in Internet Explorer 5 or later. * **self** - Select to load the content into the window in which the link is selected (the active window). * **top** - Select to load the content into the topmost window.   Data type: Enumeration |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML)**(available when the object is in a query-based page report)** | |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External Style | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Title | This property is mapped to the HTML attribute *title*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661853847-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661854871-Formula-Field-Properties)
