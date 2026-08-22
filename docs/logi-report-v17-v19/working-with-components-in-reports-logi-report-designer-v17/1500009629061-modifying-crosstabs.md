---
title: "Modifying Crosstabs"
id: 1500009629061
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs
updated_at: 2021-07-24T16:05:16Z
---

# Modifying Crosstabs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629041-Inserting-Crosstabs-in-a-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606222-Using-Crosstab-Formulas)

# Modifying Crosstabs

Once users create a crosstab, it can be further modified.

This topic introduces modifying a crosstab as follows:

* [Editing a Crosstab with Wizard](#Edit)
* [Adding More Column/Row Headers and Aggregations](#Add)
* [Defining Comparison Functions](#Comparison)
* [Customizing the Crosstab Layout](#Layout)

## Editing a Crosstab with Wizard

After a crosstab is created, you can further modify it by accessing its shortcut menu wizard which is composed by a set of screens that are similar to the wizard screens used to create the crosstab. For example, you can change the data used by the crosstab, reset the layout and style of the crosstab.

1. Right-click the crosstab and select **Crosstab Wizard** from the shortcut menu to display the [Crosstab Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009630181-Crosstab-Wizard-Dialog).
2. In the Data screen, you can specify a new data source for the crosstab.
3. In the Display screen, specify the fields you want to display in the crosstab.
4. In the Layout screen, specify the layout of the crosstab.
5. In the Style screen, set a style for the crosstab.
6. Select **Finish** to accept the changes.

For more detailed information about defining a crosstab, see [Inserting Crosstabs in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009629041-Inserting-Crosstabs-in-a-Report).

## Adding More Column/Row Headers and Aggregations

Besides using the wizard, you can drag and drop fields from the Data panel of the main window to add column/row headers and aggregations in a crosstab.

**To add a column/row header in a crosstab:**

1. From the resource tree in the Data panel, select a group objects ![Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828567/bv_grp.gif) or [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009636201-Using-Dynamic-Resources-and-Local-Parameters-in-Reports) used as Group ![Dynamic Formula as Group icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425879/bv_dynfmla_grp.gif) if the crosstab is business view based, or a DBField or formula if query based.
2. Drag the selected field to an existing column/row header until a blue line appears (for a blank crosstab, drag to the Total label to create the first column or row header), then release the mouse button. A new column/row header is then added above/on the left of the column/row.

After you have added a column/row header using the drag method, when you open the crosstab wizard, in the Display screen you can find the new fields in the corresponding box.

**To add an aggregation in a crosstab:**

You can add detail aggregations, subtotals and grand totals in a crosstab by dragging an aggregate field to the crosstab. The following fields can be used as aggregate fields in crosstabs: aggregation objects ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif), detail objects ![Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404904425495/bv_detail.gif), dynamic formulas used as Aggregation ![Dynamic Formula as Aggregation icon](https://devnet.logianalytics.com/hc/article_attachments/4404904427799/bv_dynfmla_agg.gif), dynamic formulas used as Detail ![Dynamic Formula as Detail icon](https://devnet.logianalytics.com/hc/article_attachments/4404916828823/bv_dynfmla_dtl.gif) and dynamic aggregations ![Aggregation cion](https://devnet.logianalytics.com/hc/article_attachments/4404904427287/bv_agg.gif) in a business view; DBFields, formulas and [crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009606222-Using-Crosstab-Formulas) in a query resource.

1. From the resource tree in the Data panel, select a field that can be used as crosstab aggregate field.
2. Drag the selected field to the aggregation area in the crosstab until a blue line appears, then release the mouse button. The position determines whether detail aggregations, subtotals or grand totals will be created in the crosstab.

   The [Insert Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009632081-Insert-Aggregation-Dialog) dialog appears.

   ![Insert Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404904267799/instaggrgt.gif)
3. From the Aggregate Function drop-down list, specify the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500009611182-Summaries#Function) used for the selected field. When DistinctSum is selected, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif) next to the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog.

   If the selected field has been predefined with an aggregate function, you cannot edit the function any more, and the drop-down list is changed to the Aggregation text box with the name of the field displayed in it.
4. In the Label text box, You can specify the label text for the aggregate field, which will label the newly created aggregations in the crosstab. If the crosstab is created using a business view, you can use the Auto Map Field Name checkbox to specify whether to automatically map the label text to the dynamic display name of the field at runtime. However whether the label would be displayed depends on if you have added any labels to label the column headers/row headers/aggregations in the crosstab while creating or editing the crosstab with the crosstab wizard. If no label is defined in the wizard, the label you add in the Insert Aggregation dialog will be ignored.
5. Select **OK** and a new aggregation is added in the crosstab.

After you have added an aggregation using the drag method, when you open the crosstab wizard, in the Display screen you can find the new fields in the corresponding box.

For the aggregations in a crosstab:

* If the aggregate field from which the aggregations are created has no predefined aggregate function, you can change the function of the aggregations at any time. To do this, select one or more aggregations, right-click and on the shortcut menu point to **Switch Aggregate Function**, then select the required function from the submenu. If DistinctSum is selected as the function, the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009633521-Select-Fields-Dialog) dialog will be displayed for you to specify the fields according to whose unique values to calculate DistinctSum. The new function only applies to the specified aggregations and does not affect the functions that the corresponding aggregate fields use. In this way you can make the detail aggregations, subtotals and grand totals calculated from the same aggregate field apply different aggregate functions.
* Remove them if not required. To remove an aggregation, right-click it and select **Remove Aggregation** on the shortcut menu.

## Defining Comparison Functions

A comparison function refers to calculations of percentage, permillage, or difference between:

* subtotal and grand total
* subtotal of inner group and subtotal of outer group
* values of aggregate field and subtotal
* values of aggregate field and grand total

**To define comparison functions in a crosstab:**

1. When creating or editing a crosstab with the crosstab wizard, select an aggregate field in the Summaries box of the Display screen and select the **Comparison Function** button. The [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009607422-Comparison-Function-Dialog) dialog appears.

   ![Comparison Function](https://devnet.logianalytics.com/hc/article_attachments/4404904386583/cmprsnfctn.gif)
2. From the Function drop-down list, select the required function: Percentage, Permillage or Difference.
3. Specify a position for the comparison function.
   * **Comparison Function Spans on Row Direction**  
      The comparison function will be placed into the column total cell of the crosstab.
   * **Comparison Function Spans on Column Direction**  
      The comparison function will be placed into the row total cell of the crosstab.
4. Numbers that form the calculation of the comparison function are determined by the Break By and Refer To drop-down lists.

   Items in the Break By drop-down list vary based on the position of the comparison function. It specifies the first parameter of the comparison function: the detail aggregation in the crosstab (Aggregate) or the subtotal of a specified row/column group.

   Items in the Refer To drop-down list also vary according to what you have selected from the Break By drop-down list. It specifies the other parameter of the comparison function: the grand total or subtotal for an outer row/column group.
5. Select **OK** and you can see that a new field is added into the Summaries box. You can set the display name for the field in the Label column.
6. Repeat the above steps to define comparison functions for other aggregate fields in the crosstab.
7. Select **Finish** in the Crosstab Wizard to apply the settings.

The following presents an example of using comparison function in a crosstab. It assumes that you have a web report with a crosstab in it in the catalog SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports`. The crosstab contains the following information:

* Uses business view WorldWideSalesBV in Data Source 1 of the catalog as the data source.
* Displays the group objects Product Type and Category as the column fields, Country and State as the row fields, the detail object Quantity as the aggregate field and apply Sum as the aggregate function.
* Applies the filter "Country = Canada OR Country = France".
* Uses vertical layout with Number of Rows as 1.
* Takes the Classic style.

The crosstab shows information about product sales volume in each state of Canada and France like below:

![Initial Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404916832407/cmpnt_crstb_mdfy_cmprsn1.gif)

Now, you want to define a comparison function in the crosstab to show the percentage of each state's sales volume to the grand total.

1. Right-click the crosstab and select **Crosstab Wizard** on the shortcut menu.
2. In the Display screen of the Crosstab Wizard, select **Quantity** in the Summaries box, then select the **Comparison Function** button.
3. In the Comparison Function dialog, select **Percentage** from the Function drop-down list, select **Comparison Function Spans on Row Direction**, specify **Product Type** as the break by field and choose **Grand Total** from the Refer to list.
4. Select **OK** in the Comparison Function dialog to return to the Crosstab Wizard.
5. Select **Finish** in the wizard to accept the settings.
6. In the Report Inspector, modify the value of the Format property of the fields corresponding to the percentage to **#,###.##%** (the fields are represented as QUANTITY9, QUANTITY10 and QUANTITY11 respectively in the Report Inspector).
7. Preview the crosstab again and you will find that a percentage is added to the right of each state's sales volume.

   ![Crosstab Result with Comparison Function](https://devnet.logianalytics.com/hc/article_attachments/4404916832663/cmpnt_crstb_mdfy_cmprsn2.gif)

## Customizing the Crosstab Layout

When you create or edit a crosstab, you can use the Layout screen of the crosstab wizard to customize the layout of the crosstab according to specific data displayed in the crosstab so as to make the data more intuitive and readable. You can also customize the layout of a crosstab by setting [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009635301-Crosstab-Properties#Property) in the Report Inspector.

![Crosstab Wizard - Layout](https://devnet.logianalytics.com/hc/article_attachments/4404904384407/crstbwzd_layout.gif)

The following are properties that are provided in the Layout screen.

**Aggregate**

Specifies properties of the aggregate fields.

* **Vertical Layout**  
   If selected, the aggregate fields will be arranged vertically.
  + **Number of Rows**  
     Specifies the number of rows to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a row so that the aggregate fields are positioned in one column vertically. 0 and a number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of rows (3 for example) less than the number of aggregate fields (6 for example), there will be 3 rows to hold the 6 fields with each row containing 2 fields.
* **Horizontal Layout**  
   If selected, the aggregate fields will be arranged horizontally. When you have multiple aggregate fields in the crosstab, using horizontal layout can make the report more readable.
  + **Number of Columns**   
     Specifies the number of columns to hold the aggregate fields in the crosstab. By default, it is -1 which means that each aggregate field is placed in a column so that the aggregate fields are positioned in one row horizontally. 0 and a number equal to or larger than the number of aggregate fields in the crosstab are treated as -1. If you set the number of columns (3 for example) less than the number of aggregate fields (6 for example), there will be 3 columns to hold the 6 fields with each column containing 2 fields.
* **Repeat Aggregate**  
   Specifies whether or not to repeat the crosstab for different aggregate fields. If the option is selected, one aggregate cell contains only one aggregate field value, while for the other aggregate fields, the crosstab will repeat; if unselected, one aggregate cell accommodates the values of all aggregate fields.
  When the option is selected, the value set for Number of Rows or Number of Columns will be ignored.

  The following sample shows the difference:

  + Repeat Aggregate selected:  
    ![Crosstab with Repeated Aggregate Fileds](https://devnet.logianalytics.com/hc/article_attachments/4404916832919/dlg_crstab1.gif)
  + Repeat Aggregate unselected:  
    ![Crosstab without Unrepeated Aggregate Fields](https://devnet.logianalytics.com/hc/article_attachments/4404916833175/dlg_crstab2.gif)
* **Outside Aggregate Title**  
   Specifies whether to place the aggregate field labels on the leftmost column when the aggregate layout is vertical, or on the topmost row of the crosstab when the aggregate layout is horizontal. Selecting this option would make the labels of the aggregate fields far from their values.

**Suppress Row Grand Totals**

Specifies whether or not to show the grand total row in the crosstab. For a compound crosstab, you can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) to customize the grand totals of which column compound groups will be suppressed and which will be shown in the [Suppress Row Grand Totals](https://devnet.logianalytics.com/hc/en-us/articles/1500009633741-Suppress-Row-Grand-Totals-Dialog) dialog

**Suppress Column Grand Totals**

Specifies whether or not to show the grand total column in the crosstab. For a compound crosstab, you can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) to customize the grand totals of which row compound groups will be suppressed and which will be shown in the [Suppress Column Grand Totals](https://devnet.logianalytics.com/hc/en-us/articles/1500009610502-Suppress-Column-Grand-Totals-Dialog) dialog.

**Suppress Row Subtotals**

Specifies whether or not to show the subtotals of the row fields in the crosstab. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) to customize which subtotals of the row fields will be suppressed and which will be shown in the [Suppress Row Subtotals](https://devnet.logianalytics.com/hc/en-us/articles/1500009610522-Suppress-Row-Subtotals-Dialog) dialog.

**Suppress Column Subtotals**

Specifies whether or not to show the subtotals of the column fields in the crosstab. You can select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) to customize which subtotals of the column fields will be suppressed and which will be shown in the [Suppress Column Subtotals](https://devnet.logianalytics.com/hc/en-us/articles/1500009633721-Suppress-Column-Subtotals-Dialog) dialog.

**Repeat Column Header**

Specifies whether or not the column headers appear on every page when the crosstab spans more than one page.

**Use Table Style**

Specifies whether to add labels to the Total rows and columns. If the option is selected, you may find the row and column labels will be repeated too much.

**Column Totals On**

Specifies the position of subtotal and grand total columns on the left or right of the detail aggregations.

**Row Totals On**

Specifies the position of subtotal and grand total rows on the top or bottom of the detail aggregations.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629041-Inserting-Crosstabs-in-a-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606222-Using-Crosstab-Formulas)
