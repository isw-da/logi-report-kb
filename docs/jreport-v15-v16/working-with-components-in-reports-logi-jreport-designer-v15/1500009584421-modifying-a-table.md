---
title: "Modifying a Table"
id: 1500009584421
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584421-Modifying-a-Table
updated_at: 2021-07-24T05:55:55Z
---

# Modifying a Table

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data)

# Modifying a Table

This topic introduces how to modify a table.

Below is a list of the sections covered in this topic:

> * [Editing a Table with Wizard](#Edit)
> * [Aggregating on a Detail Column](#Aggregate)
> * [Showing/Hiding Summary Fields](#Show)

## Editing a Table with Wizard

Once a table has been created, you can further modify it by accessing its shortcut menu wizard which is composed by a set of screens that are similar to the wizard screens used to create the table. For example, you can change the data used by the table, apply grouping, sorting criteria to the table, and so on.

1. Right-click the table and select **Table Wizard** from the shortcut menu to display the Table Wizard.
2. In the Data screen, specify a new data source for the table if required.
3. Define the data displayed in the table using the Display and Group screens.
   Use the button ![Replace button](https://devnet.logianalytics.com/hc/article_attachments/4404889314711/btn_replace.gif) to replace a current field or ![Add botton](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add a field.
4. In the Style screen, select the style you want to apply to the table.
5. When done, select **Finish** to accept the changes.

**See also:**

* [Inserting a Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table) for details about how to define a table.
* Table Wizard for [page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009589121-Table-Wizard-Dialog-for-Page-Report-), [web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009589101-Table-Wizard-Dialog-for-Web-Report-), or [library component](https://devnet.logianalytics.com/hc/en-us/articles/1500009589081-Table-Wizard-Dialog-for-Library-Component-) for detailed information about options in the wizard.

## Aggregating on a Detail Column

You can summarize the data in a detail column if required. To do this:

1. Right-click the detail column and select **Aggregate On** from the shortcut menu. The [Aggregate On](https://devnet.logianalytics.com/hc/en-us/articles/1500009564542-Aggregate-On-Dialog) dialog appears.

   ![Aggregate On dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893956119/agrgton.gif)
2. From the Aggregate Function drop-down list, specify a function to summarize the field in the detail column.
3. Specify the Group By option.
   * If the table has groups and you want the summary to be applied on certain group level, check **Group By** and select the corresponding group by field from the drop-down list below.
   * If you want the summary to be applied on the whole dataset, check **Group By** and do not select any field from the drop-down list below.
   * If you want to create a dynamic summary, keep **Group By** unchecked. Then the summary will be applied on every group level and the whole dataset at the same time.
4. When done, select **OK**. Data in the detail column will be summarized based on the group by setting using the specified function.

In addition:

* For a page report that is created using query resources, a [summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009568382-Summaries) which is given a default name Function\_DetailFieldName will be created and saved in the current catalog. You can use it in other page reports if required.
* For a report that is created using business views, a [dynamic aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) which is given a default name Function\_DetailFieldName will be created and saved along with the report as a dynamic resource. You can use it in this report only.

## Showing/Hiding Summary Fields

When creating or editing a summary table via the table wizard in a web report or library component, once you have placed any aggregation field on its table header/footer or group header/footer, after the table is generated the Show Summary Field command is activated on the shortcut menu of all the summary columns in the table. You can use the menu command to show or hide the aggregation fields in the header/footer rows. To do this:

1. Right-click the summary column that contains the required aggregation field.
2. From the Show Summary Field submenu select/deselect the corresponding table/group header/footer to show/hide the aggregation field on the specified locations.

   The aggregation field will be placed in the intersection of its summary column and the table/group header/footer rows.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563642-Grouping-the-Data)
