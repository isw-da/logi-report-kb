---
title: "Grouping the Data in Tables"
id: 1500010094941
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094941-Grouping-the-Data-in-Tables
updated_at: 2021-07-23T19:14:49Z
---

# Grouping the Data in Tables

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057402-Using-Customized-Controls-in-Tables)

# Grouping the Data in Tables

Data in a table is usually organized into groups based on certain criteria. You can define multi-level groups in your table either when creating it or after you have generated the table. This topic introduces how you can add groups in a table and use the other group features.

This topic contains the following sections:

* [Adding Groups](#Add)
* [Setting the Sort Manner of the Groups](#Sort)
* [Specifying Select N Conditions for the Groups](#SelectN)
* [Applying Special Functions for the Groups](#Function)
* [Filtering the Groups](#Filter)

## Adding Groups

1. When creating or editing a table with the table wizard, select the **Group** screen (for a summary table in a web report and library component, the **Columns** screen).

   For a table in a page report, you can also select **Insert** > **Group** to add groups in the table.

   See a sample UI below.

   ![Create Table wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404848595863/crttbl_grp.gif)
2. Specify the position of the new group by selecting **Table** or an existing group in the right box, then:
   * For a table using a business view, select a group object in the business view as the group-by field and select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box. You can also use a [dynamic formula used as Group](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) you have created for the business view in the current report as the group-by field.
   * For a table using a query resource, select a DBField in the query resource, or a formula or parameter valid to these DBFields in the current catalog as the group-by field and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif) or drag and drop it to the right box. For the usage about parameters as group-by fields, see [Grouping Data Dynamically](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#Group).
3. In the **Sort** column, set the [sort manner](#Sort) of groups at this group level.
4. Specify the [Select N condition](#SelectN) for groups at this group level.
5. If the table uses a query resource, you can also specify the following:
   * If the group-by field is of the Numeric/String/Date/Time type, you can select a [special function](#Function) for it in the **Special Function** drop-down list.
   * If you want to [filter groups](#Filter) at a group level, select the group level and select the **Group Filter** button to specify the filter conditions.
6. Repeat the above steps to add more groups. To adjust the group levels, select a group and select the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) or **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) button. To remove a group, select it and select the **Remove** button ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404848391831/btn_rmvarrow.gif) or drag and drop it to the Resources box.
7. Select **Finish** to apply the settings.

Designer displays one or more GH-GF (group header and group footer) row pairs with the selected group-by fields in the table.

You can also add groups to a table by means of [inserting group columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables#GroupColumn) in the table.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You cannot group the following SQL type of data: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY, and Db.SQL\_OTHER.

## Setting the Sort Manner of the Groups

After you add a group, you need to specify in which manner to sort the groups at the group level.

![Sort Manner List](https://devnet.logianalytics.com/hc/article_attachments/4404848665111/cmpnt_table_grp_srt1.gif)

**Ascend**

Sorts the groups in ascending order.

**Descend**

Sorts the groups in descending order.

**No Sort**

Arranges the groups in their original order.

**Special Group**

When you select this item, Designer displays the [User Defined Group dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060782-User-Defined-Group-Dialog-Box) for you to define how to group your information. This option is only available to tables that use query resources.

![User Defined Group dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848484375/udg.gif)

For example, if you place a field named "Score" for grouping which contains student scores that range from 0 to 100, and you want to group the students in 5 ranks, namely rank A: 90~100, B: 80~89, C: 70~79, D: 60~69, and E: 0~59. You can set the following in the User Defined Group dialog box.

| Group Name | Operator | Operand |
| --- | --- | --- |
| A | between | Op1: 90, Op2: 100 |
| B | between | Op1: 80, Op2: 89 |
| C | between | Op1: 70, Op2: 79 |
| D | between | Op2: 60, Op2: 69 |
| F | <= | 59 |

There are five groups in the order from A to F. If you want to change the order of the groups, you can also achieve it via the User Defined Group dialog box.

**Custom Sort**

When you select this item, Designer displays the [Custom Sort dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095981-Custom-Sort-Dialog-Box) for you to define how to sort the groups at current group level. You can specify some fields in the dialog box as the sort-by fields, then Designer sorts the groups by the values of the first record in each group on the related fields.

The following example shows how to sort groups by a specific field.

Suppose that you have created a table of Group Above type in a page report in the catalog SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports`. The table uses the query EmployeeInformation in Data Source 1 of the catalog, displays Name, Hire Date, Employee Position, and Notes, is grouped by Assigned Region in Descend order, and applies the Logi Report demo style. The table shows as follows in view mode.

![Initial Table](https://devnet.logianalytics.com/hc/article_attachments/4404848665623/cmpnt_table_grp_srt2.gif)

Now you want to sort the groups based on the hire date information. You can specify the sort manner as follows:

1. Right-click the table and select **Table Wizard** from the shortcut menu. Designer displays the Table Wizard dialog box.
2. In the **Group** screen, select **Custom Sort** from the drop-down list in the **Sort** column for the group-by field **Assigned Region**.
3. In the Custom Sort dialog box, add the field **Hire Date** as the sort-by field for the group, keep the default sort order **Ascend**, then select **OK**.

   ![Select Sort-by Field](https://devnet.logianalytics.com/hc/article_attachments/4404848665879/cmpnt_table_grp_srt3.gif)
4. Select **Finish** in the Table Wizard dialog box to apply the settings.
5. Select the **View** tab to preview the table. You can find that the groups are sorted based on their first record's Hire Date values.

   ![Preview the Table](https://devnet.logianalytics.com/hc/article_attachments/4404857038231/cmpnt_table_grp_srt4.gif)

## Specifying Select N Conditions for the Groups

Sometimes, you may want to show data from a range in a group or some groups. To achieve this, you can use the Select N feature. By specifying a Select N condition, you can decide how many records or groups you want to display. You can also use an Integer-typed parameter to control the value of Select N.

* **To display the top or bottom N records in a table:**
  1. In the Group screen of the table wizard, select the **Table** node in the right box, then select the **Select N** button.
  2. In the [Select N dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098701-Select-N-Dialog-Box), you can see the text "The whole object" in the **In** text box. Select an item from the **Select N** drop-down list.

     ![Select N dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848666647/cmpnt_table_grp_slctn3.gif)

     By default, Designer selects "All", which means that all records are displayed.

     If you select **Top N** or **Bottom N**, you can further specify a number in the combo box below. You can also use an Integer-typed parameter in the current catalog to define the Top/Bottom N condition dynamically. Supposing the number or the value you specify for the parameter is N, when you preview the table, you can find that Designer only retrieves the first or last N records in the whole table.
  3. Select **OK** to go back to the table wizard.
  4. Select **Finish** in the table wizard to apply the settings.

* **To display the top or bottom N groups in certain group level of a table:**
  1. In the Group screen of the table wizard, select the group-by field in the right box, and then select the **Select N** button.
  2. In the Select N dialog box, you can see that Designer displays the field you have just selected in the **In** text box. From the Select N drop-down list, select **Top N** or **Bottom N**, then specify a number or an Integer-typed parameter to retrieve the first or last N groups in the specified group level.
  3. To display all the other groups that do not match the Select N condition in an additional group (these groups are hidden by default), select the **Other** box and type a name for the additional group.
  4. Select **OK** to go back to the table wizard.
  5. Select **Finish** in the table wizard to apply the settings.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* The Select N conditions for the whole data component and each group are not mutually exclusive, so you can set them individually.
* If you use an Integer-typed parameter to define the Top/Bottom N condition dynamically, you should make sure that the parameter has at least one default value that is larger than 0; otherwise, the report users will get exceptions at runtime.

**Example: Applying Select N conditions in a table**

Based on the table result in the [above example](#Example), we set two Select N conditions in the table, one for the whole table and the other for the groups in the table.

1. Right-click the table and select **Table Wizard** from the shortcut menu. Designer displays the Table Wizard dialog box.
2. In the **Group** screen, select the **Table** node in the right box, and then select the **Select N** button.
3. In the Select N dialog box, select **Top N** from the Select N drop-down list and type **2** in the combo box, then select **OK**.

   ![Specify Select N Condition on Table](https://devnet.logianalytics.com/hc/article_attachments/4404848667031/cmpnt_table_grp_slctn1.gif)
4. In the Table Wizard dialog box, select the group-by field **Assigned Region** and select the **Select N** button again.
5. In the Select N dialog box, select **Top N**, type **2**, select the **Other** checkbox and type **Others** in the text box, then select **OK**.
6. Select **Finish** in the Table Wizard dialog box to accept all settings.
7. Preview the table again. The table now displays only the first 2 records in each group (the group Latin America has only one record), shows the first 2 groups (Latin America and Europe, Middle East, Africa), and combines the records in the rest group into an additional Others group.

   ![View table based on query](https://devnet.logianalytics.com/hc/article_attachments/4404857038487/cmpnt_table_grp_slctn2.gif)

## Applying Special Functions for the Groups

If a group-by field is of the Numeric, String, or Date/Time type, you can select a special function for it in the Special Function column. This is called "grouping data by intervals" in Logi Report. It enables you to group data more clearly and logically, and to summarize data more effectively. However, you can apply this feature to page reports created using query resources only.

The following is a short description of each special function.

**Special functions for Numeric type**

| Function | Description |
| --- | --- |
| None | Displays all the records that have the same field value together as a group. |
| Up to 5 | Groups the records by intervals of 5. |
| Up to 10 | Groups the records by intervals of 10. |
| Up to 50 | Groups the records by intervals of 50. |
| Up to 100 | Groups the records by intervals of 100. |
| Up to 500 | Groups the records by intervals of 500. |
| Up to 1000 | Groups the records by intervals of 1000. |
| Up to 5000 | Groups the records by intervals of 5000. |
| Up to 10000 | Groups the records by intervals of 10000. |

**Special functions for String type**

| Function | Description |
| --- | --- |
| None | Displays all the records that have the same field value together as a group. |
| For 1st letter | Groups the records, of which the field values' first letter is the same together. |
| For first 2 letters | Groups the records, of which the field values' first two letters are the same together. |
| For first 3 letters | Groups the records, of which the field values' first three letters are the same together. |
| For first 4 letters | Groups the records, of which the field values' first four letters are the same together. |
| For first 5 letters | Groups the records, of which the field values' first five letters are the same together. |
| For last 1 letter | Groups the records, of which the field values' last letter is the same together. |
| For last 2 letters | Groups the records, of which the field values' last two letters are the same together. |
| For last 3 letters | Groups the records, of which the field values' last three letters are the same together. |
| For last 4 letters | Groups the records, of which the field values' last four letters are the same together. |
| For last 5 letters | Groups the records, of which the field values' last five letters are the same together. |

**Special functions for Date/Time type**

| Function | Description |
| --- | --- |
| None | Displays all the records that have the same field value together as a group. |
| For each second | Groups the records, of which the field values are in the same second together. |
| For each minute | Groups the records, of which the field values are in the same minute together. |
| For each hour | Groups the records, of which the field values are in the same hour together. |
| For each day | Groups the records, of which the field values are in the same day together. |
| For each week | Groups the records, of which the field values are in the same week together. |
| For each bi-week | Groups the records, of which the field values are in the same bi-week together. |
| For each half month | Groups the records, of which the field values are in the same half month together. |
| For each month | Groups the records, of which the field values are in the same month together. |
| For each quarter | Groups the records, of which the field values are in the same quarter together. |
| For each half year | Groups the records, of which the field values are in the same half year together. |
| For each year | Groups the records, of which the field values are in the same year together. |

**Customized Function**

In the special function list for all the above data types, there is an item called "Customize". By selecting this item, you can define a special function by yourself.

* **Customizing a special function for Numeric type group-by field**
  1. Select a group-by field of the Numeric type and then select **Customize** in the Special Function drop-down list. Designer displays the [Customized Function dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096021-Customized-Function-Dialog-Box).

     ![Customized Function dialog box for Numeric type](https://devnet.logianalytics.com/hc/article_attachments/4404856984727/cstmzdfctn_nmrc.gif)
  2. Specify the way in which you want to group the data.

     If you want to group the data by intervals, select the **By Intervals** radio button, then define the interval in the **Numerical Value** text box.

     If you want to group data by a range, select the **Within Range** radio button, specify the range in the **Within** text box and select how to apply the range: apply to increasing data or decreasing data.
  3. Select **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval or range in a new group, then give a name for the group in the **Special Group Name** text box.
  4. Select **OK** to save the settings.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When grouping Numeric-typed data by intervals, Designer follows this rule: all values in each range are >= the minimum value in the range and < the maximum value in the range, and 0 is the offset for the intervals.

  For example, if you specify to group the following values by intervals of 5: -8, -6, -5, -3, -1, 0, 1, 3, 4, 5, 8, the result is as follows:

  | Ranges | Values |
  | --- | --- |
  | -10 to -5 | -8, -6 |
  | -5 to 0 | -5, -3, -1 |
  | 0 to 5 | 0, 1, 3, 4 |
  | 5 to 10 | 5, 8 |
* **Customizing a special function for String type group-by field**
  1. Select a group-by field of the String type and then select **Customize** in the Special Function drop-down list to display the Customized Function dialog box.

     ![Customized Function dialog box for String type](https://devnet.logianalytics.com/hc/article_attachments/4404856985111/cstmzdfctn_strg.gif)
  2. Specify the group intervals as required.

     For example, to group records by the first N letters of the group-by field values, select **First** from the drop-down list and then type **N** in the text box. Note that the number of letters should be an integer no larger than 255.
  3. If you want to distinguish between uppercase and lowercase characters when grouping, select **Case sensitive when grouping**; otherwise, select in which way you want to convert the group names: Uppercase, Lowercase or No Conversion.

     ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you select **Case sensitive when grouping**, Designer selects **No Conversion** as the default converting method.
  4. Select **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval in a new group, then give a name for the group in the **Special Group Name** text box.
  5. Select **OK** to save the settings.
* **Customizing a special function for Date/Time type group-by field**
  1. Select a group-by field of the Date/Time type and then select **Customize** in the Special Function drop-down list to display the Customized Function dialog box.

     ![Customized Function dialog box for Date and Time type](https://devnet.logianalytics.com/hc/article_attachments/4404856985495/cstmzdfctn_dttm.gif)
  2. Specify the group intervals by inputting a value in the **Time** text box and then selecting the required item from the drop-down list behind.
  3. Define the offset with which you want to group the data.

     By default, Logi Report takes "1/1/1970 00:00:00" as the offset. If you want to define the offset by yourself, select the **Customized Value** radio button and then select the **calendar** button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404848444439/btn_clndr.gif) to choose the required offset from the calendar.
  4. Specify which day you want to use as the first day of a week.
  5. Select **Keep values outside of the range in special group** if you want to put values that do not fall within the specified interval in a new group, then give a name for the group in the **Special Group Name** text box.
  6. Select **OK** to save the settings.

## Filtering the Groups

By applying a filter condition to the groups, you can specify the groups you want to display: if a group satisfies the filter condition, you can get all the records in this group; if a group doesn't satisfy the condition, the whole group does not display.

The Group Filter feature applies to page reports using query resources only.

Suppose that you have created a table of Group Above type in a page report in the catalog SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports`. The table uses the query EmployeeInformation in Data Source 1 of the catalog, displays Name, Hire Date, Home Phone, and Salary, is grouped by Employee Position in Ascend order, and applies the Logi Report demo style. Since you do not set any group filter condition, there are three groups in the table: Marketing, Sales Representative, and Vice President.

![Initial Table](https://devnet.logianalytics.com/hc/article_attachments/4404857038743/cmpnt_table_grp_fltr1.gif)

**Example 1: Showing groups where the lowest employee salary is less than 50000**

1. Right-click the table and select **Table Wizard** from the shortcut menu. Designer displays the Table Wizard dialog box.
2. In the **Group** screen, select the group-by field **Employee Position** and Designer enables the **Group Filter** button. Select the button to display the [Group Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010097461-Group-Filter-Dialog-Box).
3. Fill in the following information in the dialog box:

   | Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
   | --- | --- | --- | --- | --- | --- | --- |
   | Unselected | Min | Salary | Salary | < | 50000 | End |

   ![Define Group Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404848667287/cmpnt_table_grp_fltr2.gif)
4. Select **OK** to close the dialog box and then **Finish** in the Table Wizard dialog box to apply the settings.
5. Select the **View** tab to preview the tab. The table only shows the two groups "Marketing" and "Sales Representative". The "Vice President" group that does not fit this condition is ignored.

   ![Group Filter Result](https://devnet.logianalytics.com/hc/article_attachments/4404848667543/cmpnt_table_grp_fltr3.gif)

**Example 2: Showing groups in which the highest-salary employee was hired before Jan. 1, 1989**

In this example, you need to set the Group Filter dialog box as follows:

| Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
| --- | --- | --- | --- | --- | --- | --- |
| Unselected | Max | Salary | Hire Date | < | 1989-01-01 00:00:00.000 | End |

When you preview the table, it displays the "Vice President" group only.

![Group Filter Result](https://devnet.logianalytics.com/hc/article_attachments/4404848667927/cmpnt_table_grp_fltr4.gif)

**Example 3: Showing groups where at least one "not highest" employee salary is larger than or equal to 50000**

In this example, you need to set the Group Filter dialog box as follows:

| Logic | Function | Field Name (before Occurs With) | Field Name (after Occurs With) | Operator | Value | More |
| --- | --- | --- | --- | --- | --- | --- |
| Selected | Max | Salary | Salary | > | 50000 | End |

When you preview the table, it shows the two groups "Sales Representative" and "Vice President".

![View report](https://devnet.logianalytics.com/hc/article_attachments/4404857039255/cmpnt_table_grp_fltr5.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* In the Value text box of the Group Filter dialog box, you can specify a constant or parameter.
* For String type constants, you can type the string without quotation marks; for Date/Time type constants, you have to follow the Date/Time format specified in the [Date Format](https://devnet.logianalytics.com/hc/en-us/articles/1500010097761-Get-JDBC-Connection-Information-Dialog-Box#DateFormat) tab of the Get JDBC Connection Information dialog box.
* You should make sure that the report result contains at least one record; otherwise, Designer throws out an error message.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057442-Modifying-Tables)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057402-Using-Customized-Controls-in-Tables)
