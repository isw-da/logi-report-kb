---
title: "Group Filter Dialog Box"
id: 1500010097461
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010097461-Group-Filter-Dialog-Box
updated_at: 2021-07-23T19:15:36Z
---

# Group Filter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097441-Go-Up-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097481-Group-Options-Dialog-Box)

# Group Filter Dialog Box

You can use the Group Filter dialog box to create and modify [advanced filtering conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables#Filter) based on the selected group. This topic describes the options in the dialog box.

Designer displays the Group Filter dialog box when you select the Group Filter button in the Group screen of the report wizard.

![Group Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848527895/grpfltr.gif)

You see the following options in the dialog box:

**Logic**

Select to evaluate the records that are not in the record aggregate.

**Functions**

Select the function to aggregate on a certain field.

* **Min**  
  Select to evaluate the records that have the lowest values for the selected field.
* **Max**  
  Select to evaluate the records that have the largest values for the selected field.
* **Exist**  
  Select to check if there exists at least one qualified record.

**Field Name** (before Occur With)

Specify the field you want to aggregate on.

**Field Name** (after Occur With)

Specify the criteria of the filter.

Expression includes not only the DBField, but also formulas and parameters. You can manually type the strings supported by the database or select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select column names or fields values in the Expressions dialog box.

**Operators**

Select the operator to compose the filter expression.

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
* **<>**  
  Not equal to

**Value**

Specify the value to use in the filter condition.

You can also use a parameter for runtime input. You can manually type the value or parameter name, or, for parameters, select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to select the parameter names in the Expressions dialog box.

![Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856922775/btn_down.gif)**Down button**

Select to display some additional commands.

* **END**  
  Select to finish entering the condition.
* **And**  
  Select to insert the logic operator "AND" which applies to this line and the next line.
* **OR**  
  Select to insert the logic operator "OR" which applies to this line and the next line.
* **Insert Row**  
  Select to insert a single Expression line.
* **Delete Row**  
  Select to delete a single Expression line.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010097441-Go-Up-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010097481-Group-Options-Dialog-Box)
