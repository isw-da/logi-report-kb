---
title: "Sorting the Data"
id: 1500009563722
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563722-Sorting-the-Data
updated_at: 2021-07-24T05:55:55Z
---

# Sorting the Data

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584341-Grouping-Data-Dynamically)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data)

# Sorting the Data

By default, the records in a table are displayed randomly; they are displayed in the order they are returned from the fetch operation. You can specify that Logi JReport sort the records in a table, and also within the groups in the table, if any.

The following example shows how to set the sorting criteria in a table.

Suppose that you have created a table based on the query EmployeeInformation in the catalog file SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports` as follows: added the fields Hire Date, Name, Home Phone and Salary to be displayed in the table, set the field Employee Position as the group by field and Ascend as the sort order, then applied the Neutral style to the table.

![](https://devnet.logianalytics.com/hc/article_attachments/4404893978775/cmpnt_table_grp_srtmnr1.gif)

For the example, specify the sorting criteria as follows:

1. Right-click the table and select **Table Wizard** from the shortcut menu.
2. In the Table Wizard, select the **Display** screen, then select the **Sort Fields By** button.
3. In the [Sort Fields By](https://devnet.logianalytics.com/hc/en-us/articles/1500009588961-Sort-Fields-By-Dialog) dialog, select the field **Hire Date** as the sort by field from the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the sort fields by box on the right, select **Ascend** from the Sort column, then select **OK** to accept the changes.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893979031/cmpnt_table_srt4.gif)
4. Select **Finish** in the Table Wizard to apply the settings.
5. View the table again and you will find that the records in each group are displayed in ascending order by Hire Date.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893979287/cmpnt_table_srt1.gif)

## Sorting Data Dynamically

Similar to [dynamic grouping](https://devnet.logianalytics.com/hc/en-us/articles/1500009584341-Grouping-Data-Dynamically), sorting can also be defined at runtime. Using the table in the above example, you can apply a dynamic sort on it as follows:

1. Right-click the table and select **Table Wizard** from the shortcut menu.
2. In the Table Wizard, select the **Display** screen, then select the **Sort Fields By** button.
3. In the Sort Fields By dialog, remove the sort by field **Hire Date** set in the above example.
4. In the Resources box, select **<New Parameter...>** in the Parameters node.
5. In the New Parameter dialog, [create a type-in parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter) named SortBy of String type (leave the other settings to their default), then select **OK**.
6. Add the just created parameter **SortBy** as the sort by field.
7. Select **Dynamic Sort** in the sort order drop-down list of the Sort column.
8. In the Specify Sort Order for dialog, input **SortBy Order**, then select **OK** to close the dialog.
9. Select **OK** in the Sort Fields By dialog to accept the changes.
10. Select **Finish** in the Table Wizard to apply the settings.
11. View the report result. In the Enter Parameter Values dialog, select a field from the SortBy drop-down list and specify the sorting manner in the SortBy Order drop-down list.

    ![Entrer Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893979543/cmpnt_table_srt2.gif)

    Here, we choose **Salary** from the SortBy list and **DESCENDING** from the SortBy Order list. The records within each group are displayed in descending order according to their salary values.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4404893979799/cmpnt_table_srt3.gif)

**Note:** The following SQL type of data cannot be sorted: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584341-Grouping-Data-Dynamically)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584321-Filtering-the-Data)
