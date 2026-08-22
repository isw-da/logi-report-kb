---
title: "Using Dynamic Resources and Local Parameters in Reports"
id: 1500010070961
section: "Creating Datasets and Designing Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports
updated_at: 2021-07-24T10:37:43Z
---

# Using Dynamic Resources and Local Parameters in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034802-Changing-the-Display-Type-of-Objects-in-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034842-Delivering-Messages-Between-Library-Components-)

# Using Dynamic Resources and Local Parameters in Reports

When working with reports that are created using [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010070641-Business-Views), sometimes you may find the predefined view elements in the business views the reports use, or the predefined [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010068961-Parameters) in the current catalog cannot meet your requirements. In this case, you can create dynamic resources (including formulas and aggregations) and local parameters and use them in the reports to get the desired data. Then when you save the reports, the dynamic resources and local parameters will be saved along with the reports as their resources in the report files.

Dynamic resources and local parameters are report level resources, which means they are only available to the report for which they are created. Unless you need to use the formulas, aggregations or parameters in multiple reports, it is always better to create dynamic resources and local parameters rather than create them in the catalog.

Below is a list of the sections covered in this topic:

* [Creating and Using Dynamic Formulas](#Formula)
  + [Using User Defined Functions in Dynamic Formulas](#UDF)

* [Creating and Using Dynamic Aggregations](#Agg)
* [Creating and Using Local Parameters](#Param)

## Creating and Using Dynamic Formulas

**To create a dynamic formula:**

1. In the Data panel of the main window expand the **Dynamic Resources** > **Formulas** node and select **<New Formula…>**, or in the report wizard or dialog where a dynamic formula list is provided, select **<New Formula…>**.
2. In the displayed dialog, specify the name of the formula and select **OK**. The Formula Editor appears.

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901122455/fmlaedtr_dynmc.gif)
3. By default, Logi JReport will decide whether the formula can be used as an aggregation object, and if not the formula will be used as a detail object. You can specify to use the formula as a detail, group, or an aggregation object, by selecting the corresponding [view element type](https://devnet.logianalytics.com/hc/en-us/articles/1500010034582-Business-View-Elements) from the Use As drop-down list on the toolbar.

   Whether a dynamic formula can be used as a certain type depends on the following rules:

   * Any formula can be used as Detail.
   * Any formula that references a DBField and not an aggregation can be used as Group.
   * A formula that refers only to aggregations can be used as Aggregation. For example, there are two aggregations Sum\_Total and Sum\_Quantity, and you can create a formula `@"Sum_Total" / @"Sum_Quantity"` and use it as an aggregation.
   * A formula that follows the [custom aggregation expression](https://devnet.logianalytics.com/hc/en-us/articles/1500010034582-Business-View-Elements#CA) can be used as Aggregation.
4. [Create the formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010068541-Creating-Formulas-in-a-Catalog) by double-clicking the required fields, functions including Logi JReport built-in functions and [user defined functions](#UDF), and operators from the Fields, Functions and Operators panels respectively. You can also write the formula by yourself in the editing panel.
5. Save the formula and exit the Formula Editor.

Once a dynamic formula is created, you can then drag it from the Data panel to the desired position in the report, or add it as report field when working with the report wizard.

In the Data panel, you can make use of the shortcut menu of any existing dynamic formula to edit or delete the formula, or change the formula type as Group, Detail, or Aggregation if needed. Dynamic formulas that have been used in the report cannot be deleted.

### Using User Defined Functions in Dynamic Formulas

Logi JReport supports the [User Defined Formula Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions) feature which allows you to create any functions as you want and use them in your formulas. However, if you want to use user defined functions in dynamic formulas, you need to create them specifically for the current report via the dynamic resource list.

**To create a user defined function for a report:**

1. In the Data panel of the main window expand the **Dynamic Resources** > **User Defined Functions** node and select **<New Function…>**, or in the report wizard or dialog where a dynamic resource list is provided, select **<New Function…>**.
2. In the displayed dialog, specify the name of the function and select **OK**.
3. In the User Defined Function Editor, create the function according to your requirement.
4. Save the function and exit the editor.

   The function is then available under the User Defined Functions node in the Functions panel of the Formula Editor and User Defined Function Editor. You can then call it in a dynamic formula or another user defined function by double-clicking it.

In the case a user defined function named function1 is `arguments: integer age, string name;`, you can call it as follows:

* `@function1(25, "John Smith");`
* `@'function1'(25, "John Smith");`
* `@"function1"(25, "John Smith");`

If you want to further edit an existing user defined function or remove any that is not required, right-click the function in the Data panel of the main window and then select the corresponding command on the shortcut menu. Functions that have been used in the report cannot be deleted.

## Creating and Using Dynamic Aggregations

**To creating a dynamic aggregation:**

1. In the Data panel of the main window, or in the Resources box of the report wizard, expand the **Dynamic Resources** > **Aggregations** node, then select **<New Aggregation…>**. The [New Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010031782-New-Aggregation-Dialog) dialog appears.

   ![New Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404901122711/nwaggrgtn.gif)
2. In the Aggregation Name text box, specify the name of the dynamic aggregation.
3. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the Mapping Name text box to specify the field on which the dynamic aggregation is based.

   You can map dynamic aggregations to the available resources such as group objects and detail objects in the current business view, or the dynamic formulas that have been created in a web report.
4. From the Aggregate Function drop-down list, specify the [aggregate function](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Function). When DistinctSum is selected, you should select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif) next to the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010032562-Select-Fields-Dialog) dialog.
5. When done, select **OK** to create the dynamic aggregation.

Once a dynamic aggregation is created, you can then drag it from the Data panel to the desired position in the report, or add it as report field when working with the report wizard.

In the Data panel, you can make use of the shortcut menu of any existing dynamic aggregation to edit it in the [Edit Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500010065481-Edit-Aggregation-Dialog) dialog or delete it. Dynamic aggregations that have been used in the report cannot be deleted.

## Creating and Using Local Parameters

1. In the Data panel of the main window, or when specifying the value of a filter condition for a data component created using a business view with the Format Filter dialog, select **<New Parameter…>** in the **Local Parameters** node.
2. In the New Parameter dialog, [create the parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog) according to your requirement.
3. Select **OK** to create the parameter and exist the dialog.

Once a local parameter is created, you can then use it to [dynamically filter data](https://devnet.logianalytics.com/hc/en-us/articles/1500010070861-Filtering-Reports#EditFilter) of the data component in the report, add it to a [parameter control](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Param) or [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Form) in the report, or reference it in a dynamic record level pass one formula used in the report.

In the Data panel, you can also make use of the shortcut menu of any existing local parameter to edit or delete it. Local parameters that have been used in the report cannot be deleted.

**Notes:**

* You can only use JDK (not JRE) to compile formulas and user defined functions created in Logi JReport and save them with no errors into a report.
* Currently, global variables are not supported in dynamic formulas and user defined functions.
* When dynamic formulas and user defined functions reference display names or mapping names, the names should not contain any of the following characters if the names are not quoted by double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression @Customer#; will cause a syntax error. But @"Customer#" is ok.
  + If a field has the display name Category.Aggregation, quote it as "Category.Aggregation" or "Category"."Aggregation".

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034802-Changing-the-Display-Type-of-Objects-in-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034842-Delivering-Messages-Between-Library-Components-)
