---
title: "Record Level Security Information Dialog Box"
id: 1500010098461
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010098461-Record-Level-Security-Information-Dialog-Box
updated_at: 2021-07-23T19:15:53Z
---

# Record Level Security Information Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098401-Reference-Table-Configuration-Dialog-Box)

# Record Level Security Information Dialog Box

You can use the Record Level Security Information dialog box to edit the [record level security](https://devnet.logianalytics.com/hc/en-us/articles/1500010094241-Applying-RLS-at-Report-Scope) for a query-based page report. This topic describes the options in the dialog box.

Designer displays the Record Level Security Information dialog box when you select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the Report Inspector to specify the property Record Security of a dataset.

![Record Level Security Information dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856899223/rlsinfo.gif)

You see the following options in the dialog box:

**User**

The column shows the user IDs to whom you add to apply the security settings.

**Role**

The column shows the roles to which you add to apply the security settings. More than one user can share one role; for one role, you only need to define once, and other users can share this role.

**Column**

The column shows the fields on which you specify to define the security conditions.

**Operator**

The column shows the operators you select for the conditions. You can use the following operators:

* **=**  
  Equal to
* **<>**  
  Not equal to
* **<**  
  Less than
* **>**  
  Greater than
* **<=**  
  Less than or equal to
* **>=**  
  Greater than or equal to
* **[NOT] IN**  
  The operator causes an enumerated list of values to appear in the WHERE clause predicate, and is used for evaluating for a true condition. For the operator "IN" or "NOT IN", you can use multiple values separated by comma (,).

**Value**

The column shows the values that you specify for the conditions.

**E-mail**

The column shows the e-mail addresses that you specify for the users.

**Title**

The column shows the titles that you specify for the users.

**Import Text**

Select to import the record level security settings from an external ".txt" file.

**Add**

Select to add a new line of security condition after the specified line.

**Remove**

Select to remove the specified security condition.

**Clear All**

Select to clear all the security settings in the dialog box.

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010098381-Receive-Message-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010098401-Reference-Table-Configuration-Dialog-Box)
