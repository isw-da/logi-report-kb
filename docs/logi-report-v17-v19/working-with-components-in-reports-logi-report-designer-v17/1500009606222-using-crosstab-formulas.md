---
title: "Using Crosstab Formulas"
id: 1500009606222
section: "Working with Components in Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606222-Using-Crosstab-Formulas
updated_at: 2021-07-24T16:05:17Z
---

# Using Crosstab Formulas

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628361-Banded-Objects)

# Using Crosstab Formulas

Crosstab formulas are a type of extended [formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009611122-Formulas) used only in crosstabs that are created using query resources. By using crosstab formulas, you can create custom aggregate functions in a crosstab to get the desired results. Crosstab formulas are private resources on the crosstab level. They cannot be used beyond its crosstab.

This topic includes the following sections:

* [Crosstab Formula Syntax](#Syntax)
* [Using Crosstab Formulas to Apply Custom Aggregate Functions](#Apply)
* [Managing Crosstab Formulas](#Manage)

## Crosstab Formula Syntax

To support more powerful and flexible calculation logic in crosstabs, crosstab formula extends the basic formula syntax in the following aspects:

* A crosstab formula can reference another crosstab formula within the same crosstab. The format is `@@<Crosstab_Formula_Name>`, for example, `@@CTF1`, here CTF1 is a crosstab formula name. In this case, a crosstab formula can be written as `@(@@CTF1)`.
* A crosstab formula can reference summary expression which follows the syntax of [custom aggregation expression](https://devnet.logianalytics.com/hc/en-us/articles/1500009613122-Business-View-Elements#Expression). See some summary expression examples below:

  `@(Sum(@Sales))`  
  `@(@Country:"USA",@Year:CHILDREN, Sum(@Sales))`  
  `@(@Country:"USA",@Year:CHILDREN, @@CTF1)`

## Using Crosstab Formulas to Apply Custom Aggregate Functions

The following example shows how to apply custom aggregate function in a crosstab by creating a crosstab formula:

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Page Report**.
3. In the Select Component for Page Report dialog, select **Crosstab** and select **OK**.
4. In the Data screen of the Crosstab Wizard, select the query **WorldWideSales** in Data Source 1 of the catalog.
5. In the Display screen, add **Country** as the row field and **Region** as the column field.
6. Select **<New Crosstab Formula...>** in the Crosstab Formulas node in the Resources box.

   ![Add Fields to the Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404916833815/cmpnt_crstb_fmla1.gif)
7. In the Enter Crosstab Formula Name dialog, type **CustomAgg** and select **OK**. The [Crosstab Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009607482-Crosstab-Formula-Editor-Dialog) is displayed.

   ![Create a Crosstab Formula](https://devnet.logianalytics.com/hc/article_attachments/4404916834071/cmpnt_crstb_fmla2.gif)
8. Define the formula as follows:

   `currency ctsv1 = @(Sum(@Price));  
   currency ctsv2 = @(@Country:ALL,@Region:ALL,Sum(@Price));  
   if(ctsv1/ctsv2 >0.005)  
   return ToText(ctsv1)  
   else  
   return "N/A"`
9. Save the crosstab formula and add it to the Summaries box as the aggregate field. You can find the aggregate function of the aggregate field is displayed as Custom and cannot be edited.
10. Switch to the Style screen and select **Classic** as the report style from the Style box.
11. Select **Finish** to create the crosstab and preview it. The crosstab is shown somewhat as follows. You can see that in the aggregate cell, based on the formula expression, "N/A" is displayed if the price value equals to or is less than 5‰ of the grand total price $16,337.85, while the actual price is displayed if the price is more than 5‰ of the grand total price.

    ![Crosstab Result with Custom Aggregate Funtion](https://devnet.logianalytics.com/hc/article_attachments/4404904438807/cmpnt_crstb_fmla.gif)

## Managing Crosstab Formulas

You can manage the crosstab formulas of a crosstab in the Data panel as follows:

* **Creating crosstab formulas**  
  To create a crosstab formula, select **<New Crosstab Formula...>** in the Crosstab Formulas node, type a name for the crosstab formula in the Enter Crosstab Formula Name dialog and select **OK**, then in the Crosstab Formula Editor, compose the formula as required. You can then [insert the crosstab formula as aggregate field](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs#InsertAgg) to the crosstab or use it to [control the properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties) of objects in the crosstab.
* **Editing a crosstab formula**  
  To edit a crosstab formula, select it from the Crosstab Formulas node, then right-click the crosstab formula and select **Edit Formula** on the shortcut menu. In the Crosstab Formula Editor, edit the formula expression as required.
* **Deleting a crosstab formula**  
  To delete a crosstab formula, right-click the crosstab formula and select **Delete** from the shortcut menu.
* **Renaming a crosstab formula**  
  To rename a crosstab formula, right-click the crosstab formula and select **Rename** from the shortcut menu. Type a new name in the Enter Crosstab Formula Name dialog and select **OK** to confirm the change.
* **Viewing properties of a****crosstab formula**  
  To view the properties of a crosstab formula, right-click the crosstab formula and select **Properties**. The [properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009611622-Formula-Properties) are then displayed in the Properties dialog.

**Notes:**

* Crosstab formulas can only be used as aggregate fields in a crosstab.
* Global variables are not supported in crosstab formulas.
* Crosstab formulas cannot reference detail fields and record level pass one formulas, except for referencing them in summary expression.
* In crosstab formulas, the Array functions cannot be used as array\_function (field\_variable, groupby). Here array\_function refers to any Array function defined in Logi Report. For example, Maximum(@dbfield, "group\_field") and Average(@formula, @parameter) are not allowed in crosstab formulas.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629061-Modifying-Crosstabs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009628361-Banded-Objects)
