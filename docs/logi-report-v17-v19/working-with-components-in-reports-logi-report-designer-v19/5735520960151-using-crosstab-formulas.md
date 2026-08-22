---
title: "Using Crosstab Formulas"
id: 5735520960151
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735520960151-Using-Crosstab-Formulas
updated_at: 2022-11-02T04:28:12Z
---

# Using Crosstab Formulas

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects)

# Using Crosstab Formulas

Crosstab formulas are a type of extended [formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735525439511-Working-with-Formulas) that you can apply in crosstabs specifically in page and ![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898419617559/___newv19.1.png "New for version 19.1.")web reports. You can use crosstab formulas to create custom aggregate functions in a crosstab to get the data you need, and control properties of the objects in a crosstab. Crosstab formulas are private resources on the crosstab level that you cannot use beyond its crosstab. ![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898419617559/___newv19.1.png "New for version 19.1.")In a business view-based report, crosstab formulas are also [dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report) of the report. Designer saves the crosstab formulas you create for a crosstab in the report file when you save the report containing the crosstab. This topic introduces the syntax of crosstab formulas and how you can create and manage crosstab formulas in your crosstabs.

This topic contains the following sections:

* [Crosstab Formula Syntax](#Syntax)
* [Using Crosstab Formulas to Apply Custom Aggregate Functions](#Apply)
* [Managing Crosstab Formulas](#Manage)

## Crosstab Formula Syntax

To support more powerful and flexible calculation logic in crosstabs, crosstab formula extends the basic [formula syntax](https://devnet.logianalytics.com/hc/en-us/articles/5735532056855-Formula-Syntax) in the following aspects:

* A crosstab formula can reference another crosstab formula within the same crosstab. The format is `@@<Crosstab_Formula_Name>`, for example, `@@CTF1`, where *CTF1* is the name of a crosstab formula. In this case, you can write the crosstab formula expression as `@(@@CTF1)`.
* A crosstab formula can reference summary expression that follows the syntax of [custom aggregation expression](https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements#Expression). For example,

  `@(Sum(@Sales))`  
  `@(@Country:"USA",@Year:CHILDREN, Sum(@Sales))`  
  `@(@Country:"USA",@Year:CHILDREN, @@CTF1)`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* You cannot use global variables in crosstab formulas.
* You cannot reference detail fields and record level pass one formulas in crosstab formulas, except for referencing them in summary expression.
* You cannot use the Array functions as `array_function (field_variable, groupby)` in crosstab formulas (*array\_function* here refers to any Array function defined in Designer). For example, Designer does not allow `Maximum(@dbfield, "group_field")` and `Average(@formula, @parameter)` in crosstab formulas.

## Using Crosstab Formulas to Apply Custom Aggregate Functions

The following example shows how you can apply custom aggregate function in a crosstab by creating a crosstab formula.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Navigate to **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog box, select **Crosstab** and select **OK**. Designer displays the Crosstab Wizard dialog box.
4. In the **Data** screen, select the query **WorldWideSales** in Data Source 1 of the catalog.
5. In the **Display** screen, add **Country** as the row field and **Region** as the column field.
6. In the **Resources** box, select **<New Crosstab Formula...>** in the **Crosstab Formulas** node.

   ![Add Fields to the Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9898518540951/cmpnt_crstb_fmla1.gif)
7. In the Enter Crosstab Formula Name dialog box, type **CustomAgg** and select **OK**. Designer displays the [Crosstab Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522106391-Crosstab-Formula-Editor-Dialog-Box).

   ![Create a Crosstab Formula](https://devnet.logianalytics.com/hc/article_attachments/9898534830615/cmpnt_crstb_fmla2.gif)
8. Define the formula.

   `currency ctsv1 = @(Sum(@Price));  
   currency ctsv2 = @(@Country:ALL,@Region:ALL,Sum(@Price));  
   if(ctsv1/ctsv2 >0.005)  
   return ToText(ctsv1)  
   else  
   return "N/A"`
9. Save the crosstab formula and add it to the **Summaries** box as the aggregate field. You can find that Designer shows **Custom** as the aggregate function of the aggregate field and you cannot edit the function.
10. Switch to the **Style** screen and select **Classic** as the report style.
11. Select **Finish** to create the crosstab.
12. Select the **View** tab to preview the crosstab. Based on the formula expression, when the price value equals to or is less than 5‰ of the grand total price "$16,337.85", Designer displays "N/A" for the aggregation. Designer displays the actual price when the price is more than 5‰ of the grand total price.

    ![Crosstab Result with Custom Aggregate Funtion](https://devnet.logianalytics.com/hc/article_attachments/9898518550807/cmpnt_crstb_fmla.gif)

## Managing Crosstab Formulas

To manage the crosstab formulas of a crosstab, first select the crosstab in the design area, then go to the **Crosstab Formulas** node in the Data panel.

You can perform the following management tasks:

* **Creating crosstab formulas**  
  Select **<New Crosstab Formula...>**, type a name for the crosstab formula in the Enter Crosstab Formula Name dialog box and select **OK**, then in the Crosstab Formula Editor dialog box, compose the formula as required. You can then [insert the crosstab formula as aggregate field](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs#InsertAgg) to the crosstab, or use it to [control the properties](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties) of objects in the crosstab.
* **Editing a crosstab formula**  
  Select the crosstab formula, then right-click it and select **Edit Formula** on the shortcut menu. In the Crosstab Formula Editor dialog box, edit the formula expression.
* **Deleting a crosstab formula**  
  Right-click the crosstab formula and select **Delete** from the shortcut menu.
* **Renaming a crosstab formula**  
  Right-click the crosstab formula and select **Rename** from the shortcut menu. Type a new name in the Enter Crosstab Formula Name dialog box and select **OK** to confirm the change.
* **Viewing properties of a crosstab formula**  
  Right-click the crosstab formula and select **Properties**. Designer then lists its [properties](https://devnet.logianalytics.com/hc/en-us/articles/5735568430103-Formula-Properties) in the Properties dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527527447-Modifying-Crosstabs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735527064599-Working-with-Banded-Objects)
