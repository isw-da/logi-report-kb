---
title: "Using Crosstab Formulas"
id: 1500009583861
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583861-Using-Crosstab-Formulas
updated_at: 2021-07-24T05:56:03Z
---

# Using Crosstab Formulas

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563342-Expanding-and-Collapsing-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583821-Creating-a-Compound-Crosstab)

# Using Crosstab Formulas

Crosstab formula is a type of extended [formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009589641-Formulas) used only in crosstabs in page reports based on query resources. By using crosstab formulas, you can create custom aggregate functions in a crosstab to get the desired results. Crosstab formulas are private resources on the crosstab level. They cannot be used beyond its crosstab.

Below is a list of the sections covered in this topic:

> * [Applying Custom Aggregate Functions](#Apply)
> * [Managing Crosstab Formulas](#Manage)

## Applying Custom Aggregate Functions

The following example shows how to apply custom aggregate function in a crosstab simply by creating a crosstab formula:

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog, select **Crosstab** and select **OK**. The Crosstab Wizard appears.
4. In the Data screen, select the query **WorldWideSales** in Data Source 1 of the catalog.
5. In the Display screen, add **Country** as the row field and **Region** as the column field.
6. Select **<New Crosstab Formula...>** in the Crosstab Formulas node in the Resources box.

   ![Create Crosstab wizard](https://devnet.logianalytics.com/hc/article_attachments/4404889411607/cmpnt_crstb_fmla1.gif)
7. In the Enter Crosstab Formula Name dialog, input **CustomAggregate** and select **OK**. The [Crosstab Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009564842-Crosstab-Formula-Editor-Dialog) is displayed.

   ![Crosstab Formula Editor window](https://devnet.logianalytics.com/hc/article_attachments/4404889411863/cmpnt_crstb_fmla2.gif)
8. Define the formula as follows:

   |  |
   | --- |
   | ``` currency ctsv1 = @(Sum(@Price)); currency ctsv2 = @(@Country:ALL,@Region:ALL,Sum(@Price)); if(ctsv1/ctsv2 >0.005) return ToText(ctsv1) else return "N/A" ``` |
9. Save the crosstab formula and add it to the Summaries box as the aggregate field.
10. Switch to the **Style** screen and select **Neutral** as the report style from the Style list.
11. Select **Finish** to create the crosstab and preview it. The crosstab is shown somewhat as follows. You can see that in the aggregate cell, based on the formula expression, "N/A" is displayed if the price value equals to or is less than 5‰ of the grand total price $16,337.85, while the actual price is displayed if the price is more than 5‰ of the grand total price.

    ![Crosstab in Page Report](https://devnet.logianalytics.com/hc/article_attachments/4404893988375/cmpnt_crstb_fmla.gif)

## Managing Crosstab Formulas

You can manage the crosstab formulas of a crosstab in the Data panel as follows:

* **Creating crosstab formulas**  
   To create a crosstab formula, select **<New Crosstab Formula...>** in the Crosstab Formulas node, enter a name for the crosstab formula in the Enter Crosstab Formula Name dialog and select **OK**, then in the Crosstab Formula Editor, compose the formula as required. You can then insert the crosstab formula as aggregate field to the crosstab or use it to [control the properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009568362-Using-Formulas-to-Control-Object-Properties) of objects in the crosstab.
* **Editing a crosstab formula**  
   To edit a crosstab formula, select it from the Crosstab Formulas node, then right-click the crosstab formula and select **Edit Formula** on the shortcut menu. In the Crosstab Formula Editor, edit the crosstab formula as required.
* **Deleting a crosstab formula**  
   To delete a crosstab formula, right-click the crosstab formula and select **Delete** from the shortcut menu.
* **Renaming a crosstab formula**  
   To rename a crosstab formula, right-click the crosstab formula and select **Rename** from the shortcut menu. Input a new name in the Enter Crosstab Formula Name dialog and select **OK** to confirm the change.
* **Viewing properties of a****crosstab formula**  
   To view the properties of a crosstab formula, right-click the crosstab formula and select **Properties** to show the Properties table.

**Notes:**

* Crosstab formulas can only be used as aggregate fields in a crosstab.
* Global variables are not supported in crosstab formulas.
* Crosstab formulas cannot reference detail fields and record level pass one formulas, except for referencing them in simple Sum expression.
* In crosstab formulas, the Array functions cannot be used as array\_function (field\_variable, groupby). Here array\_function refers to any Array function defined in Logi JReport. For example, Maximum(@dbfield, "group\_field") and Average(@formula, @parameter) are not allowed in crosstab formulas.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563342-Expanding-and-Collapsing-a-Crosstab)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009583821-Creating-a-Compound-Crosstab)
