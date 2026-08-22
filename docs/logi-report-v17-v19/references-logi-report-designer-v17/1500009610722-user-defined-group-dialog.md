---
title: "User Defined Group Dialog"
id: 1500009610722
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009610722-User-Defined-Group-Dialog
updated_at: 2021-07-24T16:04:02Z
---

# User Defined Group Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009633941-User-Defined-Function-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog)

# User Defined Group Dialog

The User Defined Group dialog helps you to define how to group data. It appears when you select Special Group from the Sort column in the Group screen of the banded/table wizard or [Map Binding Data Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009609062-Shape-Map-Data-Binding-Wizard-Dialog), or select the Special Group button in the Display screen of the chart wizard, or the Properties sub tab of the Range tab in the [Format Category(X) Axis](https://devnet.logianalytics.com/hc/en-us/articles/1500009608382-Format-Category-X-Axis-Dialog#Properties) dialog.

![User Defined Group dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911674903/udg.gif)

The following are details about options in the dialog:

**Group Name**

Specifies the name for the grouping criterion.

If you use this dialog to group data in the dataset that is bound with a map, the group name here should match with data in the specified group-by field.

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009633941-User-Defined-Function-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009633961-Web-Action-List-Dialog)
