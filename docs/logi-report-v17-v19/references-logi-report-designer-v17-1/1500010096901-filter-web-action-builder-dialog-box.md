---
title: "Filter - Web Action Builder Dialog Box"
id: 1500010096901
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096901-Filter-Web-Action-Builder-Dialog-Box
updated_at: 2021-07-23T19:15:25Z
---

# Filter - Web Action Builder Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096841-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059062-Filter-Web-Behavior-Dialog-Box)

# Filter - Web Action Builder Dialog Box

You can use the Filter-Web Action Builder dialog box to [build a Filter web action](https://devnet.logianalytics.com/hc/en-us/articles/1500010057562-Using-Basic-Web-Controls-in-a-Report#Filter) on an object so as to filter the data components in a report when the event bound with the action is triggered at runtime. This topic describes the options in the dialog box.

Designer displays the Filter-Web Action Builder dialog box when you select \*Filter and select OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box).

![Filter - Web Action Builder dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848576279/fltrwbactnbld.gif)

You see the following options in the dialog box:

**Apply Action To**

The box lists all the data components in the report. Select a data component to specify the filter conditions on it.

**Get Input From**

Select where to get the object. You can select Form if you add some objects to a form; otherwise, you can only choose the item Other in Report.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif)**Add button**

Select to add a new condition.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/4404848403351/btn_trashcan.gif)**Remove button**

Select to delete the specified condition.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

Select to move the specified condition higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

Select to move the specified condition lower in the list.

**Filter On**

The column shows the fields of the selected data component that you select to perform the filter on.

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

The column shows the relationship that you select for the conditions, which can be And, Or, or End.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096841-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010059062-Filter-Web-Behavior-Dialog-Box)
