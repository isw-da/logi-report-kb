---
title: "Setting the Sort Manner"
id: 1500009584401
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584401-Setting-the-Sort-Manner
updated_at: 2021-07-24T05:55:56Z
---

# Setting the Sort Manner

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584381-Specifying-the-Select-N-Condition)

# Setting the Sort Manner

After a group has been added, you need to specify in which manner groups at the current group level will be sorted.

* **Ascend**  
   Groups will be sorted in ascending order.
* **Descend**  
   Groups will be sorted in descending order.
* **No Sort**  
   Groups will be arranged in their original order.
* **Special Group**  
   Selecting this item will bring out the [User Defined Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009589181-User-Defined-Group-Dialog) dialog for you to define how to group your information.

  ![User Defined Group](https://devnet.logianalytics.com/hc/article_attachments/4404893845783/udg.gif)

  For example, if you place a field named Score for grouping which contains student scores that range from 0 to 100, and you want to group the students in 5 ranks, namely rank A: 90~100, B: 80~89, C: 70~79, D: 60~69, and E: 0~59. You can set the following with the User Defined Group dialog.

  | Group Name | Operator | Operand |
  | --- | --- | --- |
  | A | between | Op1: 90, Op2: 100 |
  | B | between | Op1: 80, Op2: 89 |
  | C | between | Op1: 70, Op2: 79 |
  | D | between | Op2: 60, Op2: 69 |
  | F | <= | 59 |

  There will be five groups in the order from A to F. If you want to change the order of the groups, you can also do so via the User Defined Group dialog.
* **Custom Sort**  
   Selecting this item will bring out the [Custom Sort](https://devnet.logianalytics.com/hc/en-us/articles/1500009586161-Custom-Sort-Dialog) dialog for you to define how to sort the groups. You can specify some fields in the dialog, then the groups will be sorted by the values of the first record in each group on the related fields. To add a field, select it in the Resources box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) or drag and drop it to the sort group by box on the right. You can add only one field at a time. If a field is not required, select it and select **![](https://devnet.logianalytics.com/hc/article_attachments/4404893789975/btn_rmvarrow.gif)** or drag and drop it to the Resources box.

  ![Custom Sort](https://devnet.logianalytics.com/hc/article_attachments/4404893933719/cstmsrt.gif)

  The following example shows how to sort groups by a specific field.

  Suppose that you have created a group above table based on the query EmployeeInformation in the catalog file SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports` as follows: added the fields Hire Date, Name, Home Phone and Salary to be displayed in the table, set the field Employee Position as the group by field and Ascend as the sort order, then applied the Neutral style to the table.

  ![Table in Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404893978775/cmpnt_table_grp_srtmnr1.gif)

  For the example, specify the sorting criteria as follows:

  1. Right-click the table and select **Table Wizard** from the shortcut menu.
  2. In the Group screen of the Table Wizard, select the group by field **Employee Position** in the group by box, then select **Custom Sort** from the Sort column.
  3. In the Custom Sort dialog, add the field **Hire Date**  to the sort by box, set the sorting manner as **Descend**, then select **OK**.
  4. Select **Finish** in the Table Wizard to apply the settings.
  5. View the table again and you will find that the groups are sorted based on their first record's Salary values.

     ![Table in Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404889403671/cmpnt_table_grp_srtmnr2.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563662-Specifying-Special-Function-for-Group-by-Field)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584381-Specifying-the-Select-N-Condition)
