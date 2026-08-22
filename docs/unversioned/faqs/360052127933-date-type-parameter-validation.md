---
title: "Date type parameter validation"
id: 360052127933
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360052127933-Date-type-parameter-validation
updated_at: 2020-08-18T16:12:36Z
---

# Date type parameter validation

**Question:**

I have created two parameters in my report - "Start Date" and "End Date".   
The values for these parameters is provided by the user at the time of report execution.   
How do I set a validation that ensures the difference between "Start Date" and "End Date" is not greater than 3 months?

**Answer:**

Logi Report offers a parameter validation feature via a special property:

|  |  |
| --- | --- |
| **On Parameter Value Change** | Specifies to define an action that will be called when the parameter value changes. Choose a formula from the drop-down list to develop an action, which will be called before the other actions defined in the report or library component. It can work as a parameter value validation rule. |

This property is available on the Parameter itself or on the Report template.  
   
 For this case, you can create a formula named **f\_validation,** with the following expression:

```
if(DateDiff("M", @pStartDate, @pEndDate) > 3)  
     return "Start date and end date can't exceed 3 months!"  
 else  
     return "";
```

Then assign the formula **f\_validation** to property "On Parameter Value Change" either on parameter @pStartDate or @pEndDate, or on the Report template.

![mceclip1.png](https://devnet.logianalytics.com/hc/article_attachments/360081826293/mceclip1.png)  
   
 Run the report and you will get the notification message if the start date and end date exceed 3 months.  
 ​​

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360080762294/mceclip0.png)
