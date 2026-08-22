---
title: "Filter - Web Action Builder Dialog"
id: 1500009586901
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586901-Filter-Web-Action-Builder-Dialog
updated_at: 2021-07-24T05:55:18Z
---

# Filter - Web Action Builder Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586821-Fill-Effects-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586921-Filter-Web-Behavior-Dialog)

# Filter - Web Action Builder Dialog

The Filter-Web Action Builder dialog appears when you select \*Filter and then select OK in the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog) dialog. It helps you to build a [Filter web action](https://devnet.logianalytics.com/hc/en-us/articles/1500009584021-Applying-Web-Actions-to-a-Label) on an object so as to filter data of the specified data components when the event bound with the action is triggered at runtime. [See the dialog](javascript:%20void(null)).

![Filter - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889361943/wbactnbldr_fltr.gif)

The following are details about options in the dialog:

**Get Input From**

Specifies where to get the object. You can select Form if you add some objects to a form. Otherwise, only the item Other in Report you can choose.

**Apply Action To**

Specifies the data component to which to apply the Filter action.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif)

Adds a new filter condition.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif)

Removes the selected filter condition.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the selected filter condition up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the selected filter condition down a step.

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

Specifies the value of how to filter the field. If multiple values are required, they should be separated with ",", and if "," or "\" is contained in the values, write it as "\," or "\\".

**More**

Lists some additional commands, which includes And, Or, and End.

**OK**

Accepts the changes and closes this dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009586821-Fill-Effects-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586921-Filter-Web-Behavior-Dialog)
