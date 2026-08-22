---
title: "Using Crosstab Formulas"
id: 1500010094701
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094701-Using-Crosstab-Formulas
updated_at: 2021-07-23T19:14:44Z
---

# Using Crosstab Formulas

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094281-Working-with-Banded-Objects)

# Using Crosstab Formulas

Crosstab formulas are a type of extended [formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010060962-Working-with-Formulas) that you can apply in crosstabs using query resources. By using crosstab formulas, you can create custom aggregate functions in a crosstab to get the desired results. This topic introduces the syntax of crosstab formulas and how you can create and manage crosstab formulas in your crosstabs.

Crosstab formulas are private resources on the crosstab level, which means you cannot use them beyond its crosstab.

This topic contains the following sections:

* [Crosstab Formula Syntax](#Syntax)
* [Using Crosstab Formulas to Apply Custom Aggregate Functions](#Apply)
* [Managing Crosstab Formulas](#Manage)

## Crosstab Formula Syntax

To support more powerful and flexible calculation logic in crosstabs, crosstab formula extends the basic formula syntax in the following aspects:

* A crosstab formula can reference another crosstab formula within the same crosstab. The format is `@@<Crosstab_Formula_Name>`, for example, `@@CTF1`, here *CTF1* is a crosstab formula name. In this case, you can write the crosstab formula as `@(@@CTF1)`.
* A crosstab formula can reference summary expression which follows the syntax of [custom aggregation expression](https://devnet.logianalytics.com/hc/en-us/articles/1500010101081-Business-View-Elements#Expression). The following shows some summary expression examples:

  `@(Sum(@Sales))`  
  `@(@Country:"USA",@Year:CHILDREN, Sum(@Sales))`  
  `@(@Country:"USA",@Year:CHILDREN, @@CTF1)`

## Using Crosstab Formulas to Apply Custom Aggregate Functions

The following example shows how to apply custom aggregate function in a crosstab by creating a crosstab formula:

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog box, select **Crosstab** and select **OK**. Designer displays the Crosstab Wizard dialog box.
4. In the **Data** screen, select the query **WorldWideSales** in Data Source 1 of the catalog.
5. In the **Display** screen, add **Country** as the row field and **Region** as the column field.
6. In the **Resources** box, select **<New Crosstab Formula...>** in the **Crosstab Formulas** node .

   ![Add Fields to the Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404848676631/cmpnt_crstb_fmla1.gif)
7. In the Enter Crosstab Formula Name dialog box, type **CustomAgg** and select **OK**. Designer displays the [Crosstab Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095821-Crosstab-Formula-Editor-Dialog-Box).

   ![Create a Crosstab Formula](https://devnet.logianalytics.com/hc/article_attachments/4404848677015/cmpnt_crstb_fmla2.gif)
8. Define the formula as follows:

   `currency ctsv1 = @(Sum(@Price));  
   currency ctsv2 = @(@Country:ALL,@Region:ALL,Sum(@Price));  
   if(ctsv1/ctsv2 >0.005)  
   return ToText(ctsv1)  
   else  
   return "N/A"`
9. Save the crosstab formula and add it to the **Summaries** box as the aggregate field. You can find that Designer shows **Custom** as the aggregate function of the aggregate field and you cannot edit the function.
10. Switch to the **Style** screen and select **Classic** as the report style.
11. Select **Finish** to create the crosstab and preview it. Designer displays the crosstab somewhat as follows:

    ![Crosstab Result with Custom Aggregate Funtion](https://devnet.logianalytics.com/hc/article_attachments/4404848677271/cmpnt_crstb_fmla.gif)

    You can see that in the aggregate cell, based on the formula expression, the crosstab shows "N/A" if the price value equals to or is less than 5‰ of the grand total price "$16,337.85"; the crosstab displays the actual price if the price is more than 5‰ of the grand total price.

## Managing Crosstab Formulas

You can manage the crosstab formulas of a crosstab under the Crosstab Formulas node in the Data panel as follows:

* **Creating crosstab formulas**  
  Select **<New Crosstab Formula...>**, type a name for the crosstab formula in the Enter Crosstab Formula Name dialog box and select **OK**, then in the Crosstab Formula Editor dialog box, compose the formula as required. You can then [insert the crosstab formula as aggregate field](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs#InsertAgg) to the crosstab or use it to [control the properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties) of objects in the crosstab.
* **Editing a crosstab formula**  
  Select the crosstab formula, then right-click it and select **Edit Formula** on the shortcut menu. In the Crosstab Formula Editor dialog box, edit the formula expression as required.
* **Deleting a crosstab formula**  
  Right-click the crosstab formula and select **Delete** from the shortcut menu.
* **Renaming a crosstab formula**  
  Right-click the crosstab formula and select **Rename** from the shortcut menu. Type a new name in the Enter Crosstab Formula Name dialog box and select **OK** to confirm the change.
* **Viewing properties of a crosstab formula**  
  Right-click the crosstab formula and select **Properties**. Designer then lists its [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010061402-Formula-Properties) in the Properties dialog box.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* You can only use crosstab formulas as the aggregate fields in a crosstab.
* Crosstab formulas do not support global variables.
* Crosstab formulas cannot reference detail fields and record level pass one formulas, except for referencing them in summary expression.
* You cannot use the Array functions as `array_function (field_variable, groupby)` in crosstab formulas (*array\_function* here refers to any Array function defined in Designer). For example, Designer does not allow `Maximum(@dbfield, "group_field")` and `Average(@formula, @parameter)` in crosstab formulas.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094721-Modifying-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010094281-Working-with-Banded-Objects)
