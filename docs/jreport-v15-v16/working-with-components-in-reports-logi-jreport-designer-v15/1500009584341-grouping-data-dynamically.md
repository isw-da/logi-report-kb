---
title: "Grouping Data Dynamically"
id: 1500009584341
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584341-Grouping-Data-Dynamically
updated_at: 2021-07-24T05:55:56Z
---

# Grouping Data Dynamically

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584361-Filtering-the-Groups)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data)

# Grouping Data Dynamically

You can make a multi-level group report by selecting a field as grouping criterion for the report. However, because the grouping criteria are definite, if you want to group several times according to different grouping criteria but based on the same table in the database it is cumbersome. For example, you want to make three employee list reports with different grouping criteria, the first one is grouped by their first name, the second one is by the hire date and the third one is by their salary, then you have to repeat the steps of setting query, selecting fields as grouping criteria, and so on, which is not efficient.

For this case, you can use the Dynamic Grouping feature of Logi JReport Designer, which means grouping criteria is a dynamic process. You don't need to repeat the same steps to make multiple reports with different grouping criteria. You can just predefine a parameter using String value type and add it to the group list. Then when you run the report, the parameter dialog prompts the end user to select a field to group by. All the acceptable group by fields are listed in a drop-down list. You can select any of them as grouping criterion.

## Example of Using Dynamic Grouping

Assume that you have created a table based on the EmployeeInformation query in the catalog file SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports`, which displays the fields Name, Home Phone, Employee Position and Salary, and applies the Neutral style.

![Table in Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404889404695/cmpnt_table_grp_dynmc1.gif)

To apply the dynamic grouping conditions, follow the steps below:

1. Right-click the table and select **Table Wizard** from the shortcut menu to display the Table Wizard.
2. In the Resources box of the Group screen, select **<New Parameter...>** in the Parameters node.
3. In the New Parameter dialog, [create a type-in parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter) named GroupBy of String type (leave the other settings to their default), then select **OK**.
4. Specify to group the report on the just created parameter **GroupBy** and use **Ascend** as the sorting order.
5. Select **Finish** in the Table Wizard to accept the settings.
6. Select the **View** tab to view the report. You will then be prompted to specify the parameter value. The parameter value drop-down list will show all available fields (including the DBFields in the query EmployeeInformation and formulas which are related to these DBFields).

   ![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889404951/cmpnt_table_grp_dynmc3.gif)
7. Select **Employee Position**  from the value drop-down list and data in the table is then grouped by positions of the employees.

   ![Dynamic Grouped Table in Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404889405207/cmpnt_table_grp_dynmc2.gif)

   To group the data by hire date or salary, the end user would need to select Hire Date or Salary from the drop-down list.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584361-Filtering-the-Groups)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data)
