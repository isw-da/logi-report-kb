---
title: "Sorting Page Report Data"
id: 28891735121293
section: "Creating and Editing Page Reports Using Page Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891735121293-Sorting-Page-Report-Data
updated_at: 2026-02-26T02:13:40Z
source_host: docs-report.zendesk.com
---
# 
Sorting Page Report Data 

You can sort the records, and the groups at a certain group level if you have defined one or more group levels, in a banded object or table. This topic describes how you can sort data using the Sort dialog box or shortcut menu.

- 
Sorting records: Changing the order of records in the whole banded object or table, or in each group if there exist one or more group levels. The sorting scope is the whole banded object or table.

- 
Sorting groups at a group level: Changing the order of groups at the specified group level, that is, the groups will be sorted by value of the first record in each group on the related field. The sorting scope is the group level.

You can achieve the above using the Sort dialog box or shortcut menu. However, you cannot sort the data by a global level formula.

To sort a banded object/table using the Sort dialog box:

- Select Menu > Report > Sort, or the Sort button  on the toolbar. 
    

- From the Sort in Scope drop-down list, select a banded object/table or a group field on which the sort condition will be based.

- From the field drop-down list, select the field on which to sort the data, then set the sort order to Ascend or Descend.

- If you select a banded object/table in step 2, you can select  to add new rows of sorting conditions. When a group field is selected, only one sort condition can be composed.
    Select  or  to move a row up or down so as to set the sorting priority, and  to delete the corresponding sorting condition if it is unwanted.

- To retrieve the opening status of this dialog box, select Reset.

- Select OK to accept the settings and reload the report.

To sort a banded object/table using shortcut menu:

- Right-click any value of a field, by which you want to sort the data in the banded object/table.

- Choose the command Sort > Ascend or Sort > Descend from the shortcut menu.
    If you right-click a detail/summary field value in step 1, the sorting will affect the order of detail/summary records in the banded object or table. If it is a group field value, Server rearranges the order of groups in the group level represented by the group field.

To remove the sort condition, select Sort > No Sort.

When you use the shortcut menu to sort the report data by a field and then by another field, the later sort condition always replaces the former one. And after applying a sort using the shortcut menu, if you open the Sort dialog box you can find the corresponding sort expression displays in the dialog box.

Tips:

- Administrators can customize the buffer size for sorting of each report to improve performance.

- Using Report Designer, you can set the Bind Column property for labels in banded objects and tables to enable the Sort shortcut menu on the labels, and show the sort button beside the labels for easy sorting.
