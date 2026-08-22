---
title: "Managing the Aggregate Fields in a Crosstab"
id: 1500009583801
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583801-Managing-the-Aggregate-Fields-in-a-Crosstab
updated_at: 2021-07-24T05:56:03Z
---

# Managing the Aggregate Fields in a Crosstab

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583841-Defining-Comparison-Functions-in-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563342-Expanding-and-Collapsing-a-Crosstab)

# Managing the Aggregate Fields in a Crosstab

The following fields can be used as aggregate fields to summarize data in crosstabs:

* Query fields, formulas or [crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas) in query resources
* Detail fields, aggregation fields, or [dynamic formulas/aggregations](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) in business views

Logi JReport provides you with the following methods to manage the aggregate fields in crosstabs easily:

> * [Inserting an Aggregate Field by Dragging and Dropping](#Insert)
> * [Switching the Aggregate Function of an Aggregate Field](#Switch)
> * [Removing an Aggregate Feld](#Remove)

## Inserting an Aggregate Field by Dragging and Dropping

When a crosstab is created, you can further drag and drop fields from the Data panel to the crosstab to add more aggregate fields to summarize data in the crosstab.

1. Select **View** > **Data** to display the Data panel if it is not displayed.
2. In the Data panel, select a field that can be used as an aggregate field and drag it above or under the desired subtotal or grand total cell until a blue line appears, then release the mouse button. The [Insert Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009587561-Insert-Aggregation-Dialog) dialog appears.

   ![Insert Aggrefation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893874839/instaggrgt.gif)
3. From the Aggregate Function drop-down list, specify the function to summarize the selected field.

   If the selected field has been predefined with an aggregate function, you cannot edit the function any more, and the drop-down list is changed to the Aggregation text box with the name of the field displayed in it.
4. In the Label text field, specify a display name for the aggregate field if needed, which will label the newly created summaries. However, whether the label you specify would be displayed depends on if you have added any labels to label the columns/rows/summaries in the crosstab while creating it with the report wizard. If no label is defined in the report wizard, the label you add in the Insert Aggregation dialog will be ignored.
5. Select **OK** and a new aggregate cell is added to the crosstab.

When you have added an aggregate field using this way, in the Display screen of the Crosstab Wizard, you can find the new aggregate field in the Summaries box along with the specified function and display name.

## Switching the Aggregate Function of an Aggregate Field

For the aggregate field that has no predefined aggregate function in a crosstab, you can switch the function it uses at anytime. To do this:

1. Right-click the aggregate field and select **Switch Aggregate Function** from the shortcut menu.
2. Choose a new function from the submenu.
3. View the crosstab and the values are recalculated based on the new function.

## Removing an Aggregate Field

To remove an aggregate field from a crosstab, right-click the field and select **Remove Aggregation** on the shortcut menu.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009583841-Defining-Comparison-Functions-in-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009563342-Expanding-and-Collapsing-a-Crosstab)
