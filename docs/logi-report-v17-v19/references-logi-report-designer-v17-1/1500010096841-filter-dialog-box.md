---
title: "Filter Dialog Box"
id: 1500010096841
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096841-Filter-Dialog-Box
updated_at: 2021-07-23T19:15:24Z
---

# Filter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059042-Fill-Effects-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096901-Filter-Web-Action-Builder-Dialog-Box)

# Filter Dialog Box

You can use the Filter dialog box to define to filter data of the current library component as a response to the message the library component receives at runtime. This topic describes the options in the dialog box.

Designer displays the Filter dialog box in two scenarios and you can use it for different purposes.

* When you open the dialog box by selecting 0001 - Filter from the drop-down list of the Message ID column and selecting the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the Actions column of the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box), you can use it to define to [receive the built-in Filter message](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components#BFilter) at runtime.
* When you open the dialog box by selecting a user-defined message from the drop-down list of the Message ID column, selecting ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the Actions column of the [Receive Message dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box), and then selecting \*Filter and selecting OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box), you can use it to define to [receive the user-defined Filter message](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components#UFilter) at runtime.

![Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848405015/fltr2.gif)

You see the following options in the dialog box:

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new filter condition.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified filter condition.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified filter condition higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified filter condition lower in the list.

**Filter On**

The column shows the fields that you select to perform the filter on.

**Operator**

The column shows the operators that you select to compose the filter expressions.

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
* **IN**  
  The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the "IN" operator, you can use multiple values separated by comma (,).

**Value**

The column shows the values using which you specify to filter the fields.

**More**

The column shows the relationship that you select for the conditions, which can be "And", "Or", or "End".

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010059042-Fill-Effects-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096901-Filter-Web-Action-Builder-Dialog-Box)
