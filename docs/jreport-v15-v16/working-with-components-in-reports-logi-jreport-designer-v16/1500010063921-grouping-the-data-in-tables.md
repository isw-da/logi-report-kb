---
title: "Grouping the Data in Tables"
id: 1500010063921
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063921-Grouping-the-Data-in-Tables
updated_at: 2021-07-24T10:39:19Z
---

# Grouping the Data in Tables

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029302-Modifying-Tables) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029282-Using-Customized-Controls-in-Tables)

# Grouping the Data in Tables

Data in a table is usually organized into groups based on certain criteria. You can define multi-level groups in your table either when creating it or after the table is generated.

Below is a list of the sections covered in this topic:

* [Adding Groups](#Add)
* [Setting the Sort Manner of the Groups](#Sort)
* [Specifying Select N Conditions for the Groups](#SelectN)
* [Applying Special Functions for the Groups](#Function)
* [Filtering the Groups](#Filter)

## Adding Groups

1. When creating or editing a table with the table wizard, select the **Group** screen (for a summary table in a web report and library component, the **Columns** screen).

   For a table in a page report, you can also select **Insert** > **Group** to add groups in the table.

   Below is a sample UI.

   ![Create Table wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404909231511/crttbl_grp.gif)
2. Specify the position of the new group by selecting Table or an existing group in the right box, then:
   * For a table created using a business view, select a group object in the business view as the group-by field and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or drag and drop it to the right box. You can also use a [dynamic formula used as Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) created for the business view in the current report as the group-by field.
   * For a table created using a query resource, select a DBField in the query resource or a formula or parameter valid to these DBFields in the current catalog as the group-by field and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) or drag and drop it to the right box. For the usage about parameters as group-by fields, see [Grouping Data Dynamically](https://devnet.logianalytics.com/hc/en-us/articles/1500010068981-Parameter-Application-Cases#Group).
3. In the Sort column, set the [sort manner](#Sort) of groups at this group level.
4. Specify the [Select N condition](#SelectN) for groups at this group level.
5. If the table is created using a query resource in a page report, you can also specify the following:
   * If the group-by field is of Numeric/String/Date/Time type, you can select a [special function](#Function) for it in the Special Function drop-down list.
   * If you want to [filter groups](#Filter) at a group level, select the group level and select the **Group Filter** button to specify the filter conditions.
6. Repeat the above steps to add more groups. To adjust the group levels, select a group and select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif). To remove a group, select it and select **![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404901121047/btn_rmvarrow.gif)** or drag and drop it to the Resources box.
7. Select **Finish** to apply the settings.

One or more GH-GF (group header and group footer) row pairs with the selected group-by fields are now displayed in the table.

You can also add groups to a table by means of [inserting group columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010029302-Modifying-Tables#GroupColumn) in the table.

**Note:** The following SQL type of data cannot be grouped: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.

## Setting the Sort Manner of the Groups

After a group is added in a table, you need to specify in which manner groups at the group level will be sorted.

![Sort Manner List](https://devnet.logianalytics.com/hc/article_attachments/4404909272983/cmpnt_table_grp_srt1.gif)

**Ascend**

Groups will be sorted in ascending order.

**Descend**

Groups will be sorted in descending order.

**No Sort**

Groups will be arranged in their original order.

**Special Group**

Selecting this item will bring out the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010068301-User-Defined-Group-Dialog) dialog for you to define how to group your information. This option is only available for tables created using query resources.

![User Defined Group dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909151639/udg.gif)

For example, if you place a field named Score for grouping which contains student scores that range from 0 to 100, and you want to group the students in 5 ranks, namely rank A: 90~100, B: 80~89, C: 70~79, D: 60~69, and E: 0~59. You can set the following with the User Defined Group dialog.

| Group Name | Operator | Operand |
| --- | --- | --- |
| A | between | Op1: 90, Op2: 100 |
| B | between | Op1: 80, Op2: 89 |
| C | between | Op1: 70, Op2: 79 |
| D | between | Op2: 60, Op2: 69 |
| F | <= | 59 |

There will be five groups in the order from A to F. If you want to change the order of the groups, you can also do so via the User Defined Group dialog.

**Custom Sort**

Selecting this item will bring out the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500010065201-Custom-Sort-Dialog) dialog for you to define how to sort the groups at current group level. You can specify some fields in the dialog as the sort-by fields, then the groups will be sorted by the values of the first record in each group on the related fields.

The following example shows how to sort groups by a specific field.

Suppose that you have created a table of Group Above type in a page report in the catalog SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports`. The table uses the query EmployeeInformation in Data Source 1 of the catalog, displays Name, Hire Date, Employee Position and Notes, is grouped by Assigned Region in Descend order, and applies the Logi JReport demo style.

![Initial Table](https://devnet.logianalytics.com/hc/article_attachments/4404909273239/cmpnt_table_grp_srt2.gif)

Now you want to sort the groups based on the hire date information. You can specify the sort manner as follows:

1. Right-click the table and select **Table Wizard** from the shortcut menu.
2. In the Group screen of the Table Wizard, select **Custom Sort** from the drop-down list in the Sort column for the group-by field Assigned Region.
3. In the Custom Sort dialog, add the field **Hire Date** as the sort-by field for the group, set the sort order as **Ascend**, then select **OK**.

   ![Select Sort-by Field](https://devnet.logianalytics.com/hc/article_attachments/4404901316247/cmpnt_table_grp_srt3.gif)
4. Select **Finish** in the Table Wizard to apply the settings.
5. Select the **View** tab to preview the table. You can find that the groups are sorted based on their first record's Hire Date values.

   ![Preview the Table](https://devnet.logianalytics.com/hc/article_attachments/4404901316503/cmpnt_table_grp_srt4.gif)

## Specifying Select N Conditions for the Groups

Sometimes, you may want to show data from a range in a group or some groups in a table. To achieve this, you can use the Select N feature. By specifying a Select N condition, you can decide how many records or groups will be displayed in the table. You can also use an Integer-typed parameter to control the value of Select N.

* **To display the top or bottom N records in a table:**
  1. In the Group screen of the table wizard, select the **Table** node in the right box, then select the **Select N** button.
  2. In the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500010067821-Select-N-Dialog) dialog, you will see that "The whole object" is displayed in the In text box. Select an item from the Select N drop-down list.

     ![Select N dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901316759/cmpnt_table_grp_slctn3.gif)

     By default, All is selected, which means that all records will be displayed.

     If you select Top N or Bottom N, then you can further specify a number in the combo box below. You can also use an Integer-typed parameter in the current catalog to define the Top/Bottom N condition dynamically. Supposing the number or the value you will specify for the parameter is N, when you view the result, you will find that only the first or last N records in the whole table or in each group (if any group has been defined) are retrieved.
  3. Select **OK** to go back to the Table Wizard.
  4. Select **Finish** in the wizard to apply the settings.

* **To display the top or bottom N groups in certain group level of a table:**
  1. In the Group screen of the table wizard, select the group-by field in the right box, and then select the **Select N** button.
  2. In the Select N dialog, you will see that the field you have just selected is displayed in the In text box. From the Select N drop-down list, select **Top N**  or **Bottom N**, and then further specify a number or an Integer-typed parameter. If the number or the parameter value is N, then the first or last N groups in the specified group level will be displayed.
  3. To display all the other groups that do not match the Select N condition (which are by default hidden) in an additional group, check the **Other** box and type a name for the additional group.
  4. Select **OK** to go back to the Table Wizard.
  5. Select **Finish** in the wizard to apply the settings.

**Notes:**

* The Select N conditions for the whole data component and each group are not mutually exclusive, so you can set them individually.
* If you use an Integer-typed parameter to define the Top/Bottom N condition dynamically at runtime, you should make sure that the parameter has at least one default value that is larger than 0, otherwise you will get exceptions when running the report.

**Example: Applying Select N conditions in a table**

Based on the table result in the [above example](#Example), we will set two Select N conditions in the table, one for the whole table and the other for the groups in the table.

1. Right-click the table and select **Table Wizard**  from the shortcut menu.
2. In the Group screen of the Table Wizard, select the **Table** node in the right box, and then select the **Select N** button.
3. In the Select N dialog, select **Top N**  from the Select N drop-down list and enter **2** in the combo box.

   ![Specify Select N Condition on Table](https://devnet.logianalytics.com/hc/article_attachments/4404901317015/cmpnt_table_grp_slctn1.gif)
4. Select **OK** to go back to the Table Wizard.
5. Select the group-by field **Assigned Region**  and select the **Select N** button again.
6. In the Select N dialog, select **Top N** , enter **2**, check the **Other** box and enter **Others** in the text box.
7. Select **OK** to close the Select N dialog, then select **Finish** in the Table Wizard to accept all settings.
8. Preview the table again. You can find that the first 2 records in each group (the group Latin America has only one record) have been retrieved, and then the first 2 groups (Latin America and Europe, Middle East, Africa) are displayed, with the records in the rest group combined into an additional Others group.

   ![View table based on query](https://devnet.logianalytics.com/hc/article_attachments/4404909273495/cmpnt_table_grp_slctn2.gif)

## Applying Special Functions for the Groups

If a group-by field is of Numeric, String or Date/Time type in a table, you can select a special function for it in the Special Function column. This is called "grouping data by intervals" in Logi JReport. It enables you to group data more clearly and logically, and to summarize data more effectively. However this feature is supported in page reports created using query resources only.

The following is a short description of each special function.

**Special functions for Numeric type**

| Function | Description |
| --- | --- |
| None | All the records that have the same field value will be displayed together as a group. |
| Up to 5 | The records will be grouped by intervals of 5. |
| Up to 10 | The records will be grouped by intervals of 10. |
| Up to 50 | The records will be grouped by intervals of 50. |
| Up to 100 | The records will be grouped by intervals of 100. |
| Up to 500 | The records will be grouped by intervals of 500. |
| Up to 1000 | The records will be grouped by intervals of 1000. |
| Up to 5000 | The records will be grouped by intervals of 5000. |
| Up to 10000 | The records will be grouped by intervals of 10000. |

**Special functions for** **String type**

| Function | Description |
| --- | --- |
| None | All the records that have the same field value will be displayed together as a group. |
| For 1st letter | The records, of which the field values' first letter is the same, will be grouped together. |
| For first 2 letters | The records, of which the field values' first two letters are the same, will be grouped together. |
| For first 3 letters | The records, of which the field values' first three letters are the same, will be grouped together. |
| For first 4 letters | The records, of which the field values' first four letters are the same, will be grouped together. |
| For first 5 letters | The records, of which the field values' first five letters are the same, will be grouped together. |
| For last 1 letter | The records, of which the field values' last letter is the same, will be grouped together. |
| For last 2 letters | The records, of which the field values' last two letters are the same, will be grouped together. |
| For last 3 letters | The records, of which the field values' last three letters are the same, will be grouped together. |
| For last 4 letters | The records, of which the field values' last four letters are the same, will be grouped together. |
| For last 5 letters | The records, of which the field values' last five letters are the same, will be grouped together. |

**Special functions for Date/Time type**

| Function | Description |
| --- | --- |
| None | All the records that have the same field value will be displayed together as a group. |
| For each second | The records, of which the field values are in the same second, will be grouped together. |
| For each minute | The records, of which the field values are in the same minute, will be grouped together. |
| For each hour | The records, of which the field values are in the same hour, will be grouped together. |
| For each day | The records, of which the field values are in the same day, will be grouped together. |
| For each week | The records, of which the field values are in the same week, will be grouped together. |
| For each bi-week | The records, of which the field values are in the same bi-week, will be grouped together. |
| For each half month | The records, of which the field values are in the same half month, will be grouped together. |
| For each month | The records, of which the field values are in the same month, will be grouped together. |
| For each quarter | The records, of which the field values are in the same quarter, will be grouped together. |
| For each half year | The records, of which the field values are in the same half year, will be grouped together. |
| For each year | The records, of which the field values are in the same year, will be grouped together. |

**Customized Function**

In the special function list for all the above data types, there is an item called Customize. By selecting this item, you can define a special function by yourself.

* **Customizing a special function for Numeric type group-by field**
  1. Select a group-by field of the Numeric type and then select **Customize** in the Special Function drop-down list. The [Customized Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010065221-Customized-Function-Dialog) dialog appears.

     ![Customized Function dialog for Numeric type](https://devnet.logianalytics.com/hc/article_attachments/4404901274903/cstmzdfctn_nmrc.gif)
  2. Specify the way in which you want to group the data.

     If you want to group the data by intervals, check the **By Intervals** radio button, then define the interval in the Numerical Value text box.

     If you want to group data by a range, check the **Within Range** radio button, specify the range in the Within text box and select how to apply the range: apply to increasing data or decreasing data.
  3. Check **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval or range in a new group, then give a name for the group in the Special Group Name text box.
  4. Select **OK** to save the settings.

  **Note:** When grouping Numeric typed data by intervals, Logi JReport follows this rule: all values in each range are >= the minimum value in the range and < the maximum value in the range, and 0 is the offset for the intervals.

  For example, if you specify to group the following values by intervals of 5: -8, -6, -5, -3, -1, 0, 1, 3, 4, 5, 8, the results will be as follows:

  | Ranges | Values |
  | --- | --- |
  | -10 to -5 | -8, -6 |
  | -5 to 0 | -5, -3, -1 |
  | 0 to 5 | 0, 1, 3, 4 |
  | 5 to 10 | 5, 8 |
* **Customizing a special function for String type group-by field**
  1. Select a group-by field of the String type and then select **Customize** in the Special Function drop-down list to display the Customized Function dialog.

     ![Customized Function dialog for String type](https://devnet.logianalytics.com/hc/article_attachments/4404901275159/cstmzdfctn_strg.gif)
  2. Specify the group intervals as required.

     For example, to group records by the first N letters of the group-by field values, select **First** from the drop-down list and then enter **N** in the text box. Note that the number of letters should be an integer no larger than 255.
  3. If you want to distinguish between uppercase and lowercase characters when grouping, check **Case sensitive when grouping**; otherwise, check in which way you want to convert the group names: Uppercase, Lowercase or No Conversion.

     **Note:** If you check Case sensitive when grouping, No Conversion will be checked as the default converting method.
  4. Check **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval in a new group, then give a name for the group in the Special Group Name text box.
  5. Select **OK** to save the settings.
* **Customizing a special function for Date/Time type group-by field**
  1. Select a group-by field of the Date/Time type and then select **Customize** in the Special Function drop-down list to display the Customized Function dialog.

     ![Customized Function dialog for Date and Time type](https://devnet.logianalytics.com/hc/article_attachments/4404901275415/cstmzdfctn_dttm.gif)
  2. Specify the group intervals by inputting a value in the Time text box and then selecting the required item from the drop-down list behind.
  3. Define the offset with which you want to group the data.

     By default, Logi JReport takes 1/1/1970 00:00:00 as the offset. If you want to define the offset by yourself, check the **Customized Value** radio button and then select the calendar button to choose the required offset.
  4. Specify which day will be used as the first day of a week as required.
  5. Check **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval in a new group, then give a name for the group in the Special Group Name text box.
  6. Select **OK** to save the settings.

## Filtering the Groups

By applying a filter condition to the groups in table, you can specify the groups to display in the table: if a group satisfies the filter condition, all the records in this group will be shown; if a group doesn't satisfy the condition, then the whole group will not be displayed in the table.

The Group Filter feature is supported in page reports created using query resources only.

Suppose that you have created a table of Group Above type in a page report in the catalog SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports`. The table uses the query EmployeeInformation in Data Source 1 of the catalog, displays Name, Hire Date, Home Phone and Salary, is grouped by Employee Position in Ascend order, and applies the Logi JReport demo style. Since no group filter condition has been set, there are three groups in the table: Marketing, Sales Representative and Vice President.

![Initial Table](https://devnet.logianalytics.com/hc/article_attachments/4404901317271/cmpnt_table_grp_fltr1.gif)

**Example 1: Showing groups where the lowest employee salary is less than 50000**

1. Right-click the table and select **Table Wizard** from the shortcut menu.
2. In the Group screen of the Table Wizard, select the group-by field **Employee Position**, the Group Filter button is then activated. Select it to display the [Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500010031302-Group-Filter-Dialog) dialog.
3. Fill in the following information in the dialog:

   | Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
   | --- | --- | --- | --- | --- | --- | --- |
   | Unchecked | Min | Salary | Salary | < | 50000 | End |

   ![Define Group Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404901317527/cmpnt_table_grp_fltr2.gif)
4. Select **OK** to close the dialog and then **Finish** in the Table Wizard to apply the settings.
5. Select the **View** tab to preview the tab. You can find that only the two groups Marketing and Sales Representative are displayed, while the group Vice President that does not fit this condition is ignored.

   ![Group Filter Result](https://devnet.logianalytics.com/hc/article_attachments/4404909273751/cmpnt_table_grp_fltr3.gif)

**Example 2: Showing groups in which the highest-salary employee was hired before Jan. 1, 1989**

In this example, you need to set the Group Filter dialog as follows:

| Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
| --- | --- | --- | --- | --- | --- | --- |
| Unchecked | Max | Salary | Hire Date | < | 1989-01-01 00:00:00.000 | End |

When you preview the tab, you will find that this time only the group Vice President is displayed.

![Group Filter Result](https://devnet.logianalytics.com/hc/article_attachments/4404909274007/cmpnt_table_grp_fltr4.gif)

**Example 3: Showing groups where at least one "not highest" employee salary is larger than or equal to 50000**

In this example, you need to set the Group Filter dialog as follows:

| Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
| --- | --- | --- | --- | --- | --- | --- |
| Checked | Max | Salary | Salary | > | 50000 | End |

When you view the report result, you will find that this time only the two groups Sales Representative and Vice President are displayed.

![View report](https://devnet.logianalytics.com/hc/article_attachments/4404909274263/cmpnt_table_grp_fltr5.gif)

**Notes:**

* In the Value field of the Group Filter dialog, you can input a constant or parameter.
* For String type constants, you can type the string without quotation marks. For Date/Time type constants, you have to follow the Date/Time format specified in the [Date Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010031562-Get-JDBC-Connection-Information-Dialog#DateFormat) tab of the Get JDBC Connection Information dialog.
* Ensure that the report result contains at least one record; otherwise Logi JReport Designer will throw out an error message.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010029302-Modifying-Tables) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029282-Using-Customized-Controls-in-Tables)
