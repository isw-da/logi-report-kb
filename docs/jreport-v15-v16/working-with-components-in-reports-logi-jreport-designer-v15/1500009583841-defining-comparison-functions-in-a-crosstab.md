---
title: "Defining Comparison Functions in a Crosstab"
id: 1500009583841
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583841-Defining-Comparison-Functions-in-a-Crosstab
updated_at: 2021-07-24T05:56:03Z
---

# Defining Comparison Functions in a Crosstab

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583801-Managing-the-Aggregate-Fields-in-a-Crosstab)

# Defining Comparison Functions in a Crosstab

A comparison function refers to calculations of percentage, permillage, or difference between:

* subtotal and grand total
* subtotal of inner group and subtotal of outer group
* values of aggregate field and subtotal
* values of aggregate field and grand total

**To define comparison functions in a crosstab:**

1. Right-click the crosstab and select **Crosstab Wizard** from the shortcut menu to open the Crosstab Wizard.
2. In the Display screen, select an aggregate field in the Summaries box and then select the **Comparison Function** button. The [Comparison Function](https://devnet.logianalytics.com/hc/en-us/articles/1500009585881-Comparison-Function-Dialog) dialog appears.

   ![Comparison Function dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893949207/cmprsnfctn.gif)
3. From the Function drop-down list, select the required function: Percentage, Permillage or Difference.
4. Specify a position for the comparison function.
   * **Comparison Function Spans on Row Direction**  
      The comparison function will be placed into the column total cell of the crosstab.
   * **Comparison Function Spans on Column Direction**  
      The comparison function will be placed into the row total cell of the crosstab.
5. Numbers that form the calculation of the comparison function are determined by the Break by and Refer to drop-down lists.

   Items in the Break by drop-down list vary with the position of the comparison function. It specifies the first parameter of the comparison function: the aggregate field or a subtotal.

   All available items are displayed in the Refer to drop-down list according to what you have selected from the Break by drop-down list. These items are outer group subtotals and the grand total. Select one as the other parameter of the comparison function.
6. Select **OK** and you can see that a new field is added into the Summaries box. Set the display name for the field in the Label column as required.
7. Repeat the above steps to define more comparison functions.
8. When done, select **Finish** in the Crosstab Wizard to apply the settings.
9. View the report. You will get the values of the comparison function.

## Example of using the comparison function

Assume that you have [created a web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Create) and [inserted a crosstab in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009583881-Inserting-a-Crosstab#Web) based on the business view WorldWideSalesBV in Data Source 1 of the catalog file SampleReports.cat saved in `<install_root>\Demo\Reports\SampleReports` as follows: added Product Type and Category in the Products table as the column fields, Country and State in the Customers table as the row fields, Quantity in the Orders Detail table as the aggregate field and specified Sum as the aggregate function, applied a filter "Country = Canada OR Country = France", set the crosstab to be Vertical Layout (Number of Rows: 1), and applied the style Classic. With these settings, the crosstab shows information about product sales volume in each state of Canada and France as follows:

![Crosstab Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404893988631/cmpnt_crstb_cmprsnfctn1.gif)

Now, you want to define a comparison function in the crosstab to show the percentage of each state's sales volume to the grand total. To do this:

1. Right-click the crosstab and select **Crosstab Wizard** on the shortcut menu.
2. In the Display screen of the Crosstab Wizard, select **Quantity** in the Summaries box, then select the **Comparison Function** button.
3. In the Comparison Function dialog, select **Percentage** from the Function drop-down list, check **Comparison Function Spans on Row Direction**, specify **Product Type** as the break by field and choose **Grand Total** from the Refer to list.
4. Select **OK** in the Comparison Function dialog to return to the Crosstab Wizard, then select **Finish** in the wizard to accept the settings.
5. In the Report Inspector, modify the value of the Format property of the fields corresponding to the percentage to **#,###.##%** (the fields are represented as QUANTITY9, QUANTITY10 and QUANTITY11 respectively in the Report Inspector).
6. View the crosstab again and you will find that a percentage is added to the right of each state's sales volume.

   ![Crosstab in Web Report](https://devnet.logianalytics.com/hc/article_attachments/4404889412247/cmpnt_crstb_cmprsnfctn2.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563322-Customizing-the-Crosstab-Layout)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583801-Managing-the-Aggregate-Fields-in-a-Crosstab)
