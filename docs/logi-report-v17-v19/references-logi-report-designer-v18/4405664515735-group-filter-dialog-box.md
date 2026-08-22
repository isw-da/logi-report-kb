---
title: "Group Filter Dialog Box"
id: 4405664515735
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664515735-Group-Filter-Dialog-Box
updated_at: 2022-01-27T20:36:04Z
---

# Group Filter Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661614615-Go-Up-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661615767-Group-Options-Dialog-Box)

# Group Filter Dialog Box

You can use the Group Filter dialog box to create and modify [advanced filter conditions](https://devnet.logianalytics.com/hc/en-us/articles/4405664404503-Grouping-the-Data-in-Tables#Filter) based on the selected group. This topic describes the options in the dialog box.

Designer displays the Group Filter dialog box when you select Group Filter in the Group screen of the component wizard.

![Group Filter dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420410704663/grpfltr.gif)

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

Expression includes not only the DBField, but also formulas and parameters. You can manually type the strings supported by the database or select the the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420402297111/btn_ellipsis2.gif) to select column names or fields values in the Expressions dialog box.

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

You can also use a parameter for runtime input. You can manually type the value or parameter name, or, for parameters, select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420402297111/btn_ellipsis2.gif) to select the parameter names in the Expressions dialog box.

![Down button](https://devnet.logianalytics.com/hc/article_attachments/4420402429719/btn_down1.gif)

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

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661614615-Go-Up-Web-Action-Builder-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661615767-Group-Options-Dialog-Box)
