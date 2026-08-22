---
title: "Specifying the Select N Condition"
id: 1500009584381
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584381-Specifying-the-Select-N-Condition
updated_at: 2021-07-24T05:55:56Z
---

# Specifying the Select N Condition

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584401-Setting-the-Sort-Manner)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584361-Filtering-the-Groups)

# Specifying the Select N Condition

Sometimes, you may want to show data from a range in a group or some groups in a table. To achieve this, you can use the Select N feature. By specifying a Select N condition, you can decide how many records or groups will be displayed in the table. You can also use an Integer-typed parameter to control the value of Select N.

* **To display the top or bottom N records in a table:**
  1. Right-click the table and select **Table Wizard**  from the shortcut menu.
  2. In the Group screen of the Table Wizard, select the **Table** node in the group by box, and then select the **Select N** button.
  3. In the [Select N](https://devnet.logianalytics.com/hc/en-us/articles/1500009567482-Select-N-Dialog) dialog, you will see that The whole object is displayed in the In text field. Select an item from the Select N drop-down list.

     ![Select N dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893980183/cmpnt_table_grp_slctn3.gif)

     By default, All is selected, which means that all records will be displayed.

     If you select Top N or Bottom N, then you can further specify a number in the combo box below. You can also use an Integer-typed parameter to define the Top/Bottom N condition dynamically. Supposing the number or the value you will specify for the parameter is N, when you view the result, you will find that only the first or last N records in the whole table or in each group (if any group has been defined) are retrieved.
  4. Select **OK** to go back to the Table Wizard.
  5. When done, select **Finish** to apply the settings.

* **To display the top or bottom N groups in certain group level of a table:**
  1. Right-click the table and select **Table Wizard**  from the shortcut menu.
  2. In the Group screen of the Table Wizard, select the group by field in the group by box, and then select the **Select N** button.
  3. In the Select N dialog, you will see that the field you have just selected is displayed in the In text field. From the Select N drop-down list, select **Top N**  or **Bottom N**, and then further specify a number or an Integer-typed parameter. If the number or the parameter value is N, then the first or last N groups in that group level will be displayed.
  4. To display all the other groups that do not match the Select N condition (which are by default hidden) in an additional group, check the **Other** box and type a name for the additional group.
  5. Select **OK** to go back to the Table Wizard.
  6. Upon finishing, select **Finish** to apply the settings.

**Notes:**

* The Select N conditions for the whole object and each group are not mutually exclusive, so you can set them individually.
* If you use an Integer-typed parameter to define the Top/Bottom N condition dynamically at runtime, you should make sure that the parameter has at least one default value that is larger than 0, otherwise you will get exceptions when viewing the report.

## Example of applying Select N conditions

The following example shows how to set the Select N conditions, both for the whole table and the groups in the table in detail.

1. Create a table based on the query EmployeeInformation in the catalog file SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports` as follows: add the fields Name, Hire Date, Employee Position and Notes to be displayed in the table, set the field Assigned Region as the group by field and Descend as the sort order, and apply the Neutral style to the table.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893980439/cmpnt_table_grp_slctn1.gif)
2. Right-click the table and select **Table Wizard**  from the shortcut menu.
3. In the Group screen of the Table Wizard, select the **Table** node in the group by box, and then select the **Select N** button.
4. In the Select N dialog, select **Top** from the Select N drop-down list and enter **2** in the combo box.
5. Select **OK** to go back to the Table Wizard.
6. Select the group by field **Assigned Region**  in the group by box and select the **Select N** button again.
7. In the Select N dialog, select **Top**, enter **2**, check the **Other** box and enter **Others** in the text field.
8. Select **OK** to close the Select N dialog, then select **Finish** in the Table Wizard to accept all settings.
9. View the table again.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889403927/cmpnt_table_grp_slctn2.gif)

   You can find that the first 2 records in each group (the group Latin America has only one record) have been retrieved, and then the first 2 groups (North America, and Latin America) are displayed, with the records in the rest group combined into an additional Others group.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584401-Setting-the-Sort-Manner)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584361-Filtering-the-Groups)
