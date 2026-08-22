---
title: "Grouping the Data"
id: 1500009563642
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data
updated_at: 2021-07-24T05:55:56Z
---

# Grouping the Data

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584421-Modifying-a-Table)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field)

# Grouping the Data

Data in a table is usually organized into groups based on certain criteria. You can define multi-level groups in your table either when creating it or after the table has been built. In this topic, you will be shown how to define groups in an existing table.

**To group data of an existing table:**

1. Select the table and do one of the following:
   * Select **Insert** > **Group**.
   * Right-click the table and select **Table Wizard**  from the shortcut menu.
2. In the Group screen of the Table Wizard, select the field in the Resources box as the group by field and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the group by box on the right.

   ![Table Wizard - Group](https://devnet.logianalytics.com/hc/article_attachments/4404893980951/cmpnt_table_grp.gif)
3. Set the sorting manner of groups at this group level in the Sort column.
4. Select the **Select N** button to specify the Select N condition.
5. If the table is in a page report based on query resource, you can also specify the following:
   * If the group by field is of Numeric/String/Date/Time type, you can select a special function for the it from the Special Function drop-down list.
   * If you want to filter groups at this group level, select the **Group Filter** button, and then specify the filter conditions.
6. To add another group to the table,
   specify the position of the group by selecting Table or the existing group in the group by box,
   then select the field in the Resources box as the group by field and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the group by box. The new group is then added below the selected group level. Define the group settings as described in steps 3 to 5.
7. Repeat the above step to add more groups.

   To adjust the order of the groups, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) above the group by box.

   To remove a group, select it in the group by box and select **![](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box.
8. Select **Finish** to apply the settings.

One or more GH-GF (group header and group footer) row pairs with the selected group fields will have been added to the table.

**Note:** The following SQL type of data cannot be grouped: Db.SQL\_BINARY, Db.SQL\_BLOB, Db.SQL\_CLOB, Db.SQL\_LONGVARCHAR, Db.SQL\_LONGVARBINARY, Db.SQL\_VARBINARY and Db.SQL\_OTHER.

The following topics provide additional information about grouping:

> * [Specifying Special Function for Group by Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field)
> * [Setting the Sort Manner](https://devnet.logianalytics.com/hc/en-us/articles/1500009584401-Setting-the-Sort-Manner)
> * [Specifying the Select N Condition](https://devnet.logianalytics.com/hc/en-us/articles/1500009584381-Specifying-the-Select-N-Condition)
> * [Filtering the Groups](https://devnet.logianalytics.com/hc/en-us/articles/1500009584361-Filtering-the-Groups)
> * [Grouping Data Dynamically](https://devnet.logianalytics.com/hc/en-us/articles/1500009584341-Grouping-Data-Dynamically)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584421-Modifying-a-Table)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field)
