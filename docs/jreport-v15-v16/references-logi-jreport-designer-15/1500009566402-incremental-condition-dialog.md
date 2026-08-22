---
title: "Incremental Condition Dialog"
id: 1500009566402
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009566402-Incremental-Condition-Dialog
updated_at: 2021-07-24T05:55:07Z
---

# Incremental Condition Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566382-Import-from-Logi-JReport-Server-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566422-Information-Bus-Dialog)

# Incremental Condition Dialog

The Incremental Condition dialog appears when you select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell of the Incremental Fetch property of a refresh object in a library component in the Report Inspector. It helps you to specify conditions to filter the incremental data.  [See the dialog](javascript:%20void(null)).

![Incremental Condition dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889335959/incrmntlcndtn.gif)

The following are details about options in the dialog:

**Add Condition**

Adds a condition line.

**Delete**

Deletes the selected condition line.

**Group**

Makes the selected conditions in one group.

**Ungroup**

Makes the selected condition ungrouped.

**Up**

Moves the selected condition or group up to a higher level.

**Down**

Moves the selected condition or group down to a lower level.

**Field**

Specifies the business view element on which the filter condition is based. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to the text box to select the business view element.

**Operator**

Specifies the operator to compose the condition expression.

**Value**

Specifies the value of how to filter the business view element. You can type in the value manually, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to the text box to specify the value, or select a value from the drop-down list.

* **MaxExistValue**  
   If selected, the maximum data value in the selected business view element from the last refresh time will be used as the value to filter the business view element.
* **MinExistValue**  
   If selected, the minimum data value in the selected business view element from the last refresh time will be used as the value to filter the business view element.
* **LastRefreshTime**  
   If selected, the previous refresh time will be used as the value to filter the business view element.

**SQL**

Statement Displays the SQL statement of the condition expression.

**OK**

Applies the changes and closes this dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009566382-Import-from-Logi-JReport-Server-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009566422-Information-Bus-Dialog)
