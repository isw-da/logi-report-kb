---
title: "Filter - Web Behavior Dialog"
id: 1500009586921
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586921-Filter-Web-Behavior-Dialog
updated_at: 2021-07-24T05:55:18Z
---

# Filter - Web Behavior Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586901-Filter-Web-Action-Builder-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565642-Filter-dialog-Dialog)

# Filter - Web Behavior Dialog

The Filter-Web Behavior dialog appears when you right-click a web control in the configuration panel of a library component and select Web Behaviors > Filter from the shortcut menu. It helps you to build a [Filter web behavior](https://devnet.logianalytics.com/hc/en-us/articles/1500009570822-Using-the-Configuration-Panel#Filter) to the web control so as to filter data of the library component at runtime. [See the dialog](javascript:%20void(null)).

![Filter - Web Behavior dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893817239/wbbhvr_fltr.gif)

The following are details about options in the dialog:

**Apply Action To**

Specifies the data component to which to apply the filter action. Select the desired object from the drop-down list.

**Filter On**

Specifies the field on which the filter is based. Which fields are available here depends on which object you choose from the Apply Action To drop-down list.

**Operator**

Specifies the operator to compose the filter expression.

* **=**  
   Equal to
* **>**  
   Greater than
* **<**  
   Less than
* **>=**  
   Greater than or equal to
* **<=**  
   Less than or equal to
* **!=**  
   Not equal to
* **in**  
   Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For operator ‘in', it is allowed to input multiple values in the Value input box and separate the values with comma (,).

**Value**

Specifies the value of how to filter the field. The value may be input by yourself, or be specified by the value of a web control. If multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

**OK**

Accepts the changes and closes this dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586901-Filter-Web-Action-Builder-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565642-Filter-dialog-Dialog)
