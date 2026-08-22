---
title: "Filtering the Groups"
id: 1500009584361
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584361-Filtering-the-Groups
updated_at: 2021-07-24T05:55:56Z
---

# Filtering the Groups

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584381-Specifying-the-Select-N-Condition)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584341-Grouping-Data-Dynamically)

# Filtering the Groups

As the name suggests, the Group Filter feature is based on groups. If a group satisfies the filter condition, all the records in this group will be shown. If the group doesn't satisfy the condition, then the whole group will not be displayed in the table.

Suppose that you have created a table based on the query EmployeeInformation in the catalog file SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports` as follows: added the fields Hire Date, Name, Home Phone and Salary to be displayed in the table, set the field Employee Position as the group by field and applied the Neutral style to the table. Since no group filter condition has been set, there are three groups in the table: Marketing, Sales Representative and Vice President.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893978775/cmpnt_table_grp_srtmnr1.gif)

**Example 1: Show groups where the lowest employee salary is less than 50000**

1. Right-click the table and select **Table Wizard** from the shortcut menu.
2. In the Group screen of the Table Wizard, select the group by field **Employee Position**, the Group Filter button will then become available. Select it to display the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009566302-Group-Filter-Dialog) dialog.

   ![Group Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893878039/grpfltr.gif)
3. Fill in the following information in the dialog:

   | Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
   | --- | --- | --- | --- | --- | --- | --- |
   | Unchecked | Min | Salary | Salary | < | 50000 | End |
4. Select **OK** to close the dialog and then **Finish** in the Table Wizard to apply the settings.
5. View the report result. You will find that only the two groups Marketing and Sales Representative are displayed, while the group Vice President that does not fit this condition is ignored.

   ![View report](https://devnet.logianalytics.com/hc/article_attachments/4404889404183/cmpnt_table_grp_fltr1.gif)

**Example 2: Show groups in which the highest-salary employee was hired before Jan. 1, 1989**

In this example, you need to set the Group Filter dialog as follows:

| Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
| --- | --- | --- | --- | --- | --- | --- |
| Unchecked | Max | Salary | Hire Date | < | 1989-01-01 00:00:00.000 | End |

When you view the report result, you will find that this time only the group Vice President is displayed.

![View report](https://devnet.logianalytics.com/hc/article_attachments/4404893980695/cmpnt_table_grp_fltr2.gif)

**Example 3: Show groups where at least one "not highest" employee salary is larger than 60000**

In this example, you need to set the Group Filter dialog as follows:

| Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
| --- | --- | --- | --- | --- | --- | --- |
| Checked | Max | Salary | Salary | > | 60000 | End |

When you view the report result, you will find that this time only the group Vice President is displayed.

![View report](https://devnet.logianalytics.com/hc/article_attachments/4404889404439/cmpnt_table_grp_fltr3.gif)

**Notes:**

* In the Value field of the Group Filter dialog, you can input a constant or parameter.
* For String type constants, you can type the string without quotation marks. For Date/Time type constants, you have to follow the Date/Time format specified in the [Date Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog#DateFormat) tab of the Get JDBC Connection Information dialog.
* Ensure that the report result contains at least one record; otherwise Logi JReport Designer will throw out an error message.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584381-Specifying-the-Select-N-Condition)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584341-Grouping-Data-Dynamically)
