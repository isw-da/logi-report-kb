---
title: "Filter Dialog Box"
id: 4405664481303
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664481303-Filter-Dialog-Box
updated_at: 2022-01-27T20:35:09Z
---

# Filter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664480151-Fill-Effects-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661554839-Filter-Web-Action-Builder-Dialog-Box)

# Filter Dialog Box

You can use the Filter dialog box to define to filter data of the current library component as a response to the message the library component receives at runtime. This topic describes the options in the dialog box.

Designer displays the Filter dialog box in two scenarios and you can use it for different purposes.

* When you open the dialog box by selecting 0001 - Filter from the drop-down list of the Message ID column and selecting the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420410588951/btn_ellipsis1.gif) in the Actions column of the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664556951-Receive-Message-Dialog-Box), you can use it to define to [receive the built-in Filter message](https://devnet.logianalytics.com/hc/en-us/articles/4405661935255-Delivering-Messages-Between-Library-Components#BFilter) at runtime.
* When you open the dialog box by selecting a user-defined message from the drop-down list of the Message ID column, selecting the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420410588951/btn_ellipsis1.gif) in the Actions column of the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664556951-Receive-Message-Dialog-Box), and then selecting \*Filter and selecting OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661744791-Web-Action-List-Dialog-Box), you can use it to define to [receive the user-defined Filter message](https://devnet.logianalytics.com/hc/en-us/articles/4405661935255-Delivering-Messages-Between-Library-Components#UFilter) at runtime.

![Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410589719/fltr2.gif)

You see the following options in the dialog box:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif)**Add button**

Select to add a new filter condition.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4420402325015/btn_trashcan.gif)**Remove button**

Select to delete the specified filter condition.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420410588439/btn_mvup.gif)**Move Up button**

Select to move the specified filter condition higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420410588695/btn_mvdwn.gif)**Move Down button**

Select to move the specified filter condition lower in the list.

**Filter On**

This column shows the fields that you select to perform the filter on.

**Operator**

This column shows the operators that you select to compose the filter expressions.

* **=**  
  Equal to
* **>=**  
  Greater than or equal to
* **>**  
  Greater than
* **<**  
  Less than
* **<=**  
  Less than or equal to
* **!=**/**<>**  
  Not equal to
* **in**  
  The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the "in" operator, you can use multiple values separated by comma (,).

**Value**

This column shows the values using which you specify to filter the fields.

**More**

This column shows the relationship that you select for the conditions, which can be "And", "Or", or "End".

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664480151-Fill-Effects-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661554839-Filter-Web-Action-Builder-Dialog-Box)
