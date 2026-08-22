---
title: "User Defined Group Dialog"
id: 1500009589181
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog
updated_at: 2021-07-24T05:54:45Z
---

# User Defined Group Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567842-Update-Procedures-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog)

# User Defined Group Dialog

The User Defined Group dialog appears when you select Special Group from the Sort column in the Group screen of the banded/table wizard or [Map Binding Data Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009566722-Shape-Map-Data-Binding-Wizard-Dialog), or select the Special Group button in the Display screen of the chart wizard, or the Properties sub tab of the Range tab in the Format Category(X) Axis dialog for [report](https://devnet.logianalytics.com/hc/en-us/articles/1500009565802-Format-Category-X-Axis-Dialog-for-Report-#Properties) or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009587141-Format-Category-X-Axis-Dialog-for-Library-Component-#Properties). It helps you to [define how to group your information](https://devnet.logianalytics.com/hc/en-us/articles/1500009584401-Setting-the-Sort-Manner). [See the dialog](javascript:%20void(null)).

![User Defined Group dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893845783/udg.gif)

The following are details about options in the dialog:

**Group Name**

Specifies the name for the grouping criterion.

If you use this dialog to group data in the dataset that is bound with a map, the group name here should match with data in the specified group by field.

**Operator**

Specifies the operator with which to compose the grouping criterion.

There are many operators with which you can define how your data will be grouped. You can define as: between, not between. > (greater than), < (less than), = (equal to), <= (less than or equal to), >= (greater than or equal to), or != (not equal to).

**Operand**

Either op1 or both op1 and op2 will be seen in the Operand column. Type the criteria here, and if the type of the value you input is not numeric, type it with double quotation marks.

**Keep values outside of the range in special group**

If checked, Logi JReport will put the values that are not included in the specified criteria in a new special group.

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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009567842-Update-Procedures-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009567862-Web-Action-List-Dialog)
