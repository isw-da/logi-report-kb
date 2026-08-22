---
title: "Form Properties"
id: 5735533213079
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735533213079-Form-Properties
updated_at: 2022-11-02T08:15:59Z
---

# Form Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533183511-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735517135127-Formula-Field-Properties)

# Form Properties

This topic describes the properties of a [Form object](https://devnet.logianalytics.com/hc/en-us/articles/5735564508951-Using-Forms-in-a-Page-Report) that you can use in page reports only.

| Property Name | Description |
| --- | --- |
| General **(available when the object is in a query-based page report)** | |
| Class Type | Shows the class type of the object. Read only. |
| Instance Name | Shows the instance name of the object. Read only. |
| CSS | |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/5735586517143-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list when you have specified the [Style Group](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#StyleGroup) property for the page report tab and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | |
| Logic Column | Designer displays this property when the object is in a table. You can use it to specify whether to show the object in the next visible table cell in the same row when the column that holds the object is hidden. Choose an option from the drop-down list. Data type: Enumeration  Note icon   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When you set this property for several objects in the same row to "next visible column", and the columns holding these objects are all hidden, only the object in the rightmost column shows in the next visible cell. |
| Form | |
| Disabled | Specifies whether to disable user interaction with the form. Data type: Boolean |
| Form Action | Specifies the URL to which to send the form content for processing. Data type: String |
| Form ID | Specifies the string for identifying the form. Data type: String |
| Form Method | Specifies how you want to send the form data to Server. Choose an option from the drop-down list.  * **get** Select to append the arguments to the Form Action URL and open it as if it were an anchor. * **post** Select to send the data through an HTTP post transaction.   Data type: Enumeration |
| Form Name | Specifies the name of the form. Data type: String |
| Form Target | Specifies the window or frame to load the form content at runtime. Choose an option from the drop-down list.  * **default** Select to load the content into the window in which the link is selected (the active window). This option is the same as "self". * **blank** Select to load the content into a new blank window. This window is not named. * **parent** Select to load the content into the immediate parent window of the active window. If there is no parent window, the active window is used. * **self** Select to load the content into the window in which the link is selected (the active window). * **top** Select to load the content into the topmost window.   Data type: Enumeration |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/5735567902231-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML)**(available when the object is in a query-based page report)** | |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External Style | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Title | This property is mapped to the HTML attribute *title*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533183511-Filter-Control-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735517135127-Formula-Field-Properties)
