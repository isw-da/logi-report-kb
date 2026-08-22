---
title: "Filter dialog Dialog"
id: 1500009565642
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565642-Filter-dialog-Dialog
updated_at: 2021-07-24T05:55:19Z
---

# Filter dialog Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586921-Filter-Web-Behavior-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565662-Filter-Options-Dialog)

# Filter Dialog

The Filter dialog helps you to define to filter data of the current library component as a response to the [message](https://devnet.logianalytics.com/hc/en-us/articles/1500009570842-Delivering-Messages-Between-Library-Components) the library component receives at runtime. It is displayed when you select 0001 - Filter from the drop-down list of the Message ID column and then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the Actions column of the [Receive Message](https://devnet.logianalytics.com/hc/en-us/articles/1500009567242-Receive-Message-Dialog) dialog, or when you select \*Filter and then select OK in the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog. [See the dialog](javascript:%20void(null)).

![Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893811863/fltr2.gif)

The following are details about options in the dialog:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a new filter condition.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected filter condition.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected filter condition up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected filter condition down a step.

**Filter On**

Specifies the field on which the filter is based.

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

Specifies the value of how to filter the field. If multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

**More**

Lists some additional commands, which includes And, Or, and End.

**OK**

Accepts the changes and closes this dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586921-Filter-Web-Behavior-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565662-Filter-Options-Dialog)
