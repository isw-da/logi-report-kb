---
title: "Sorting Report Data"
id: 1500009675281
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009675281-Sorting-Report-Data
updated_at: 2021-07-24T20:53:34Z
---

# Sorting Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650342-Applying-Parameters)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675301-Applying-CSS-Styles)

# Sorting Report Data

You can make the data displayed in either descending or ascending alphabetical order in a report.

Below is a list of the sections covered in this topic:

* [Sorting Data in Charts](#Chart)
* [Sorting Data in Crosstabs](#Crosstab)
* [Sorting Data in Tables](#Table)

## Sorting Data in Charts

Data labels on the category or series axes of a chart (including KPI charts in KPI components) can be sorted alphabetically. To do this, select the chart, right-click the icon ![](https://devnet.logianalytics.com/hc/article_attachments/4404920371095/btn_pgrpt_drag.gif) of the chart or right-click on the chart platform or paper, then on the shortcut menu, select **Ascend** or **Descend** from the Sort Category or Sort Series submenu.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920371735/wbrpt_edt_sort_cht.gif)

To remove the sort condition, select **No Sort** on the Sort Category or Sort Series submenu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Sorting Data in Crosstabs

You can make the records in a crosstab sorted based on any column or row field. To do this, right-click on any value on the column or row header, then choose the command **Sort** > **Ascend**  or **Sort** > **Descend**  from the shortcut menu. To remove the sort condition, select **Sort** > **No Sort** from the shortcut menu.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920371991/wbrpt_edt_sort_crstb.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Sorting Data in Tables

To sort the data in a table you can use either shortcut menu, column headers or labels.

### Sorting a Group Table

You can take the following ways to sort data in a group table. When you sort data in a group table by a detail field and then by another detail field, data in the table will be sorted by the later sort condition first and then by the former sort condition.

* **Using shortcut menu**Right-select on any value in the table, then on the shortcut menu select **Ascend** or **Descend** from the Sort submenu. If a detail/summary field value is selected on, the sorting will affect the order of detail/summary records in the table; if it is a group field value, the order of groups in the group level represented by the group field will be rearranged. To remove the sort condition, select **No Sort**.

* **Using the sort button on table column header**You can use the sort button on any table column header to sort values in the column if the feature is enabled in the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#ColumnHeader). By default the feature is enabled.
  1. On the Profile > Customize Profile > Common tab, make sure the option Sort on Column Headers is checked.
  2. Check **Show Sort/Filter Status on Column Headers** if you want the sort button to be displayed with the current sort status on the table column headers after the columns are applied with sort orders.
  3. Select **OK** to save the profile setting.
  4. Run a web report containing a table in Web Report Studio.
  5. Put the mouse pointer on any column header and you can find the sort button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920372247/btn_lblsort.gif).

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404926634519/wbrpt_edt_sort_tbl.gif)
  6. To sort data in the column ascending, select the upward triangle; to sort the values descending, select the downward triangle. When a sort order is applied, the corresponding triangle will be highlighted. To remove the sort order, select the highlighted triangle.

     A summary column that contains multiple summary fields cannot be sorted using this way. Moreover a group header in a table created in Web Report Studio is always merged as a table cell. If a summary column contains only one aggregation field which is in a merged group header, you cannot use this way to sort it either.
* **Using labels**With Logi JReport Designer, you can bind a label in a table with a field used in the table to enable sorting on the label by setting the label's Bind Column and Sortable properties. Then when running the table in Web Report Studio you can select the sort button beside the label to sort values of the bound field. This functions the same as via the [table column headers](#Header).

  When a label is bound with a field, if the Sort on Column Header feature is also enabled, the former has higher priority. For example, if you bind the label in column A header with the field in column B, when selecting the sort button on column A header, values in column B are sorted.

### Sorting a Summary Table

You can use the [same methods on group tables](#Group) to sort the group and aggregation fields in summary tables. However for summary tables, you can define whether to use major sort or minor sort via the [server profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#Sort) (Profile > Customize Server Preferences > General > Use Major Sort as Default). By default, major sort is applied which is to sort data in a summary table by the last sort condition only, that is to say the later sort condition always replaces the former one. When minor sort is used, sort of a lower group is always based on the sort result of all its higher level groups.

For example, a summary table contains group fields G1, G2 and G3 (G1 the highest group level and G3 the lowest) and the aggregation fields A1 and A2. When minor sort is applied, after sorting group G1 column ascending, if you apply a sort on group G2 column descending, the table will be sorted based on group G1 ascending first and then group G2 descending, then you further sort group G3 descending and the sort result is G1 ascending, G2 descending and G3 descending. Based on this sort result, you apply the ascending order on the aggregation field A1, and the table is now sorted based on G1 ascending, G2 descending and A1 ascending. Sort order on G3 is removed, this is because all aggregation fields calculate data based on the lowest group in a summary table and they are considered as one group, so on the lowest group and the aggregation fields only one sort order can take effect. Therefore based on the former sort result, if you apply a sort order on G3 again the sort on A1 will be removed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650342-Applying-Parameters)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009675301-Applying-CSS-Styles)
