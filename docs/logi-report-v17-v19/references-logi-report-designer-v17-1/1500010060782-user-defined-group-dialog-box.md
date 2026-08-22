---
title: "User Defined Group Dialog Box"
id: 1500010060782
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box
updated_at: 2021-07-23T19:16:07Z
---

# User Defined Group Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099101-User-Defined-Function-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box)

# User Defined Group Dialog Box

The User Defined Group dialog box helps you to define how to group data. It appears when you select Special Group from the Sort column in the Group screen of the banded/table wizard or [Map Binding Data Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059822-Shape-Map-Data-Binding-Wizard-Dialog-Box), or select the Special Group button in the Display screen of the chart wizard, or the Properties sub tab of the Range tab in the [Format Category(X) Axis dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097021-Format-Category-X-Axis-Dialog-Box#Properties).

![User Defined Group dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848484375/udg.gif)

The following are details about options in the dialog box:

**Group Name**

Specifies the name for the grouping criterion.

If you use this dialog box to group data in the dataset that is bound with a map, the group name here should match with data in the specified group-by field.

**Operator**

Specifies the operator with which to compose the grouping criterion.

There are many operators with which you can define how your data will be grouped. You can define as: between, not between. > (greater than), < (less than), = (equal to), <= (less than or equal to), >= (greater than or equal to), or != (not equal to).

**Operand**

Either op1 or both op1 and op2 will be seen in the Operand column. Type the criteria here, and if the type of the value is not numeric, type it with double quotation marks.

**Keep values outside of the range in special group**

If the option is selected, Logi Report will put the values that are not included in the specified criteria in a new special group.

* **Special Group Name**  
   Specifies the name for the special group.

**Add**

Adds a new grouping line.

**Remove**

Removes the grouping line you specify.

**OK**

Applies all changes.

**Cancel**

Does not retain any changes.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099101-User-Defined-Function-Editor-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010060822-Web-Action-List-Dialog-Box)
