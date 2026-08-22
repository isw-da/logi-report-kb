---
title: "RLS at Report Scope"
id: 1500009593201
section: "Defining Report Security - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593201-RLS-at-Report-Scope
updated_at: 2021-07-24T05:53:42Z
---

# RLS at Report Scope

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593181-RLS-and-CLS-at-Data-Source-Scope)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593121-Business-View-Security)

# RLS at Report Scope

The record-level security (RLS) can also be of report scope, that is, you can create different record-level security policies for different reports. When a report is applied RLS of both the report and data source scopes, the report-scope RLS will override that of the data source scope. Column-level security (CLS) is not supported at report scope.

RLS at report scope cannot be applied to reports that use business view as the data source, that is it is only supported on a query based page report.

**To set up a record-level security policy for a query based page report:**

1. [Open the page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009571002-Opening-a-Page-Report).
2. In the Report Inspector, select the node in the Datasets node.
3. In the Security section of the Properties sheet, select in the value cell of the Record Security property, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif).

   ![Set Record Security Property](https://devnet.logianalytics.com/hc/article_attachments/4404889275543/scrty_rlscls_rpt.gif)

   The Record Level Security Information dialog appears.

   ![Record Level Security Information dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889275799/rlsinfo.gif)
4. Select the **Add** button to add a condition line and edit the security information by selecting corresponding cells.

   If you want to use more values in one cell, use "|" to separate them (applies to the User, E-mail, and Title cells). This is useful when you want to apply the same conditions to multiple users. For example, if you want user1, user2, and user3 to share the same security setting, input **user1|user2|user3** in the User cell, and then define the security condition.
5. Add more condition lines as required. If you want to apply more than one condition expression to a user, you can edit the condition expressions in several individual lines, typing in the same user name for each line. For such compound conditions, the relationship among them is logical OR.

   You can also create a text file, add the security settings, and then select **Import Text** to import the security information from the text file into the Record Level Security Information dialog. After importing, you can select the cells to further edit the security settings if required. Note that when you create the text file to include the security information, you should use TAB to separate each item, and always keep the headings (User, Role, Column, and so on) on the first line of the text file. For example,

   | User | Role | Column | Operator | Value | E-mail | Title |
   | --- | --- | --- | --- | --- | --- | --- |
   | admin | admin |  |  |  |  |  |
   | user1 |  | Customer ID | >= | 10 | user1@yoursite.com | Mr. |
   | user1 |  | Customer Name | = | 'Absolute Java' |  |  |
   | user2 |  | Customer Name | IN | ('Absolute Java','American Coffee Inc.') | user2@yoursite.com | Miss |
   | user3 |  | Phone | IN | ('(212) 555-3462','(317) 555-1274') | user3@yoursite.com | Mrs. |
6. Select **OK** to finish defining the security information and close the dialog.
7. If necessary, you can also use a formula to specify the security condition and set it as value of the Function property on the dataset of the report to control the RLS conditions on the report.

   For example, if user1 should only see records which satisfy the condition State = 'CO' and Customer ID >= 10, you can create a formula as follows:

   `if ( @State == 'CO' && @"Customer ID">= 10 ) return "user1"`

   Then from the value list of the Function property, select the formula.

   When the Record Security and Function properties have been set to control the record-level security on a report, both will take effect, and the relationship between them is logical OR.

After the report is [published to Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Remotely), when different users log onto the server and run it, they will only see the data they are supposed to see.

**Note:** In the Record Level Security Information dialog, the date values provided in the drop-down list may not be valid for your database, because they are date values that have already been reformatted using your date format settings in Logi JReport. For detailed information on how to set the date format in Logi JReport Designer, see the [Date Format explanation](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog#DateFormat) of the document Get JDBC Connection Information dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593181-RLS-and-CLS-at-Data-Source-Scope)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593121-Business-View-Security)
