---
title: "Record Level Security Information Dialog Box"
id: 5735531031575
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735531031575-Record-Level-Security-Information-Dialog-Box
updated_at: 2022-11-02T04:40:12Z
---

# Record Level Security Information Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567115287-Receive-Message-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735544168599-Reference-Table-Configuration-Dialog-Box)

# Record Level Security Information Dialog Box

You can use the Record Level Security Information dialog box to edit the [record level security](https://devnet.logianalytics.com/hc/en-us/articles/5735511843479-Applying-RLS-at-Report-Scope) for a query-based page report. This topic describes the options in the dialog box.

Designer displays the Record Level Security Information dialog box when you select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898423153431/btn_ellipsis1.gif) in the Report Inspector to specify the Record Security property of a dataset.

![Record Level Security Information dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898478167063/rlsinfo.gif)

Designer displays these options:

**User**

This column shows the user IDs to whom you add to apply the security settings.

**Role**

This column shows the roles to which you add to apply the security settings. More than one user can share one role; for one role, you only need to define once, and other users can share this role.

**Column**

This column shows the fields on which you specify to define the security conditions.

**Operator**

This column shows the operators you select for the conditions. You can use the following operators:

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

This column shows the values that you specify for the conditions.

**E-mail**

This column shows the email addresses that you specify for the users.

**Title**

This column shows the titles that you specify for the users.

**Import Text**

Select to import the record level security settings from an external .txt file.

**Add**

Select to add a new line of security condition after the specified line.

**Remove**

Select to remove the specified security condition.

**Clear All**

Select to clear all the security settings in the dialog box.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735567115287-Receive-Message-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735544168599-Reference-Table-Configuration-Dialog-Box)
