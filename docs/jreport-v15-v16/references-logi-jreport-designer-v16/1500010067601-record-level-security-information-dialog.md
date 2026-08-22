---
title: "Record Level Security Information Dialog"
id: 1500010067601
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067601-Record-Level-Security-Information-Dialog
updated_at: 2021-07-24T10:38:28Z
---

# Record Level Security Information Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032262-Receive-Message-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067561-Reference-Table-Configuration-Dialog)

# Record Level Security Information Dialog

The Record Level Security Information dialog helps you to change the [record level security](https://devnet.logianalytics.com/hc/en-us/articles/1500010063241-Record-Level-and-Column-Level-Security#Report) settings. It appears when you select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the Report Inspector to specify the property Record Security of a dataset.

![Record Level Security Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901184279/rlsinfo.gif)

The following are details about options in the dialog:

**Use "|" to separate more values in one cell**

If you want to use more values in one cell, use "|" to separate them. Applies to User, E-mail, and Title column. This is useful when you want to apply the same conditions to multiple users. For example, if you want user1, user2, and user3 to share the same security setting, list user1, user2, and user3 in the same cell, separated by "|", and then define the security conditions.

**Columns**

* **User**  
   The user ID to whom the security settings will be applied.
* **Role**  
   The role of the user. More than one user can share one role; for one role, you only need to define once, and other users can share this role without type the same conditions again.
* **Column**  
   The condition expression is comprised of three parts - Column, Operator, and Value.

  The column name, can be the name of a DBField in the current query, the name of a formula (summary) based on any DBField in the current query, and the name of a parameter. You do not need to quote the name when the name contains spaces. However, you must make sure the names you type actually exist.
* **Operator**  
   The operator can be one of the following operators: =, <>, <, >, <=, >=, IN or NOT IN.
* **Value**  
   The value part of the condition expression.
  + For String type values, use single quotation mark (') to quote the values, for example, 'Absolute Java';
  + For Boolean type values, use 0 (false) or 1 (true).
  + For Date type values, make sure the format of the value you enter is consistent with that of your database.

    **Note:** In the Record Level Security Information dialog, the date values provided on the drop-down list may not be valid for your actual database, because they are date values that have already been reformatted using your date format settings in Logi JReport. For detailed information on how to set the date format in Logi JReport Designer, see [Date Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog#DateFormat).
  + For the values of other types, type them in their original form.
* **E-mail**  
   The e-mail address of the user.
* **Title**  
   The title for the user.

**Import Text**

Imports record level security settings from an external .txt file.

**Add**

Inserts a new row of user condition after the selected row.

**Remove**

Removes the selected row of user condition.

**Clear All**

Clears all the rows in the list.

**OK**

Accepts the changes and closes this dialog.

**Cancel**

Closes this dialog, leaving any changes unsaved.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032262-Receive-Message-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067561-Reference-Table-Configuration-Dialog)
