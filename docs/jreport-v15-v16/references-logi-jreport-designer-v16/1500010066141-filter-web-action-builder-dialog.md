---
title: "Filter - Web Action Builder Dialog"
id: 1500010066141
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010066141-Filter-Web-Action-Builder-Dialog
updated_at: 2021-07-24T10:38:51Z
---

# Filter - Web Action Builder Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066101-Filter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066161-Filter-Web-Behavior-Dialog)

# Filter - Web Action Builder Dialog

The Filter-Web Action Builder dialog helps you to [build a Filter web action](https://devnet.logianalytics.com/hc/en-us/articles/1500010029382-Using-Basic-Web-Controls-in-a-Report#Filter) on an object so as to filter the data components in a report when the event bound with the action is triggered at runtime. It appears when you select \*Filter and select OK in the [Web Action List](https://devnet.logianalytics.com/hc/en-us/articles/1500010068321-Web-Action-List-Dialog) dialog.

![Filter - Web Action Builder dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909221015/fltrwbactnbld.gif)

The following are details about options in the dialog:

**Apply Action To**

Lists all the data components in the report. Select a data component to specify the filter conditions on it.

**Get Input From**

Specifies where to get the object. You can select Form if you add some objects to a form. Otherwise, only the item Other in Report you can choose.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)

Adds a new condition.

![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif)

Removes the selected condition.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif)

Moves the selected condition up a step.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif)

Moves the selected condition down a step.

**Filter On**

Specifies on which field of the selected data component to perform the filter.

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
   Causes an enumerated list of values to appear in the WHERE clause predicate, used for evaluating for a true condition. For the operator "in", multiple values separated by comma (,) are allowed.

**Value**

Specifies the value of how to filter the field.

**More**

Specifies the relationship between the current condition and the following, which could be And, Or and End.

**OK**

Accepts the changes and closes this dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010066101-Filter-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066161-Filter-Web-Behavior-Dialog)
