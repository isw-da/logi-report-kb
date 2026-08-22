---
title: "Filter - Web Action Builder Dialog Box"
id: 5735500770711
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735500770711-Filter-Web-Action-Builder-Dialog-Box
updated_at: 2022-11-02T04:37:27Z
---

# Filter - Web Action Builder Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735509055895-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735500773527-Filter-Web-Behavior-Dialog-Box)

# Filter - Web Action Builder Dialog Box

You can use the Filter - Web Action Builder dialog box to [build a Filter web action](https://devnet.logianalytics.com/hc/en-us/articles/9898540480023-Defining-Web-Behaviors-of-Objects-in-a-Report#Filter) on an object so as to filter the data components in a report when the event bound with the action is triggered at runtime. This topic describes the options in the dialog box.

Designer displays the Filter - Web Action Builder dialog box when you select \*Filter and select OK in the [Web Action List dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735531755159-Web-Action-List-Dialog-Box), and displays it differently for a [page report](#Page) or [web report/library component](#Web).

---

Designer displays the Filter - Web Action Builder dialog box as follows for a page report:

![Filter - Web Action Builder dialog box for page report](https://devnet.logianalytics.com/hc/article_attachments/9898464341783/fltrwbactnbld-pg.gif)

Designer displays these options:

**Get Input From**

Select where to get the input.

**Apply Action To**

This drop-down list contains all the data components in the page report. Select the data component to which to apply the filter action.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**

Select to add a new filter condition.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified filter condition.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified filter condition higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified filter condition lower in the list.

**Filter On**

This column shows the fields of the selected data component that you select to perform the filter on.

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

This column shows the relationship that you select for the conditions, which can be And, Or, or End.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

---

Designer displays the Filter - Web Action Builder dialog box as follows for a web report/library component:

![Filter - Web Action Builder dialog box for library component](https://devnet.logianalytics.com/hc/article_attachments/9898464348311/fltrwbactnbld.gif)

Designer displays these options:

**Apply Action To**

This box lists all the data components in the web report or library component. Select each data component that you want to filter and define the filter conditions for it in the right box.

**Get Input From**

Select where to get the input.

![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898403108631/btn_add.gif)**Add button**

Select to add a new filter condition.

![Trash Can button](https://devnet.logianalytics.com/hc/article_attachments/9898403114647/btn_trashcan.gif)**Remove button**

Select to delete the specified filter condition.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/9898406165911/btn_mvup.gif)**Move Up button**

Select to move the specified filter condition higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/9898423100695/btn_mvdwn.gif)**Move Down button**

Select to move the specified filter condition lower in the list.

**Filter On**

This column shows the fields of the selected data component that you select to perform the filter on.

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

This column shows the relationship that you select for the conditions, which can be And, Or, or End.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735509055895-Filter-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735500773527-Filter-Web-Behavior-Dialog-Box)
