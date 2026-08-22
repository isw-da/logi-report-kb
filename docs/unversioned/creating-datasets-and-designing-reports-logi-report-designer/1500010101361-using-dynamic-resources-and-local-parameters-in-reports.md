---
title: "Using Dynamic Resources and Local Parameters in Reports"
id: 1500010101361
section: "Creating Datasets and Designing Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports
updated_at: 2021-07-23T19:16:50Z
---

# Using Dynamic Resources and Local Parameters in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components)

# Using Dynamic Resources and Local Parameters in Reports

When working with reports that use [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views), sometimes you may find the predefined view elements in the business views the reports use, or the predefined [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters) in the current catalog cannot meet your requirements. In this case, you can create dynamic resources (including formulas and aggregations) and local parameters and use them in the reports to get the desired data. Then when you save the reports, Designer saves the dynamic resources and local parameters along with the reports as their resources in the report files. This topic describes how you can create and use dynamic resources and local parameters in a report.

Dynamic resources and local parameters are report level resources, which means they are only available to the report for which they are created. Unless you need to use the formulas, aggregations, or parameters in multiple reports, it is always better to create dynamic resources and local parameters rather than create them in the catalog.

This topic contains the following sections:

* [Creating and Using Dynamic Formulas](#Formula)
  + [Using User-Defined Functions in Dynamic Formulas](#UDF)

* [Creating and Using Dynamic Aggregations](#Agg)
* [Creating and Using Local Parameters](#Param)

## Creating and Using Dynamic Formulas

**To create a dynamic formula:**

1. In the **Data** panel of the main window, expand the **Dynamic Resources** > **Formulas** node and select **<New Formula…>**, or in the report wizard or dialog box which contains a dynamic formula list, select **<New Formula…>**.
2. In the displayed dialog box, specify the name of the formula and select **OK**. Designer displays the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096921-Formula-Editor-Dialog-Box).

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404848397079/fmlaedtr_dynmc.gif)
3. By default, Designer decides whether the formula can be used as an aggregation object, and if not, the formula is used as a detail object. You can specify to use the formula as a detail, group, or an aggregation object, by selecting the corresponding [view element type](https://devnet.logianalytics.com/hc/en-us/articles/1500010101081-Business-View-Elements) from the **Use As** drop-down list on the toolbar.

   Whether a dynamic formula can be used as a certain type depends on the following rules:

   * Any formula can be used as Detail.
   * Any formula that references a DBField and not an aggregation can be used as Group.
   * A formula that refers only to aggregations can be used as Aggregation. For example, there are two aggregations "Sum\_Total" and "Sum\_Quantity", and you can create a formula `@"Sum_Total" / @"Sum_Quantity"` and use it as an aggregation.
   * A formula that follows the [custom aggregation expression](https://devnet.logianalytics.com/hc/en-us/articles/1500010101081-Business-View-Elements#CA) can be used as Aggregation.
4. [Create the formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog) by double-clicking the required fields, functions including Logi Report built-in functions and [user-defined functions](#UDF), and operators from the **Fields**, **Functions**, and **Operators** panels respectively. You can also write the formula by yourself in the editing panel.
5. Save the formula and exit editor.

Once you have created a dynamic formula, you can drag it from the Data panel to the desired position in the report, or add it as report field when working with the report wizard.

In the Data panel, you can make use of the shortcut menu of any existing dynamic formula to edit or delete the formula, or change the formula type as Group, Detail, or Aggregation. You cannot delete dynamic formulas that you have used in the report.

### Using User-Defined Functions in Dynamic Formulas

Logi Report supports the [User-Defined Formula Function](https://devnet.logianalytics.com/hc/en-us/articles/1500010099441-Using-User-Defined-Formula-Functions) feature which enables you to create any functions as you want and use them in your formulas. However, if you want to use user-defined functions in dynamic formulas, you need to create them specifically for the current report via the dynamic resource list.

**To create a user-defined function for a report:**

1. In the **Data** panel of the main window, expand the **Dynamic Resources** > **User Defined Functions** node and select **<New Function…>**, or in the report wizard or dialog box which contains a dynamic resource list, select **<New Function…>**.
2. In the displayed dialog box, specify the name of the function and select **OK**.
3. In the [User Defined Function Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099101-User-Defined-Function-Editor-Dialog-Box), create the function according to your requirement.
4. Save the function.

   The function is then available under the **User Defined Functions** node in the **Functions** panel of the Formula Editor and User Defined Function Editor. You can then call it in a dynamic formula or another user-defined function by double-clicking it.

In the case a user-defined function named "function1" is `arguments: integer age, string name;`, you can call it as follows:

* `@function1(25, "John Smith");`
* `@'function1'(25, "John Smith");`
* `@"function1"(25, "John Smith");`

If you want to further edit an existing user-defined function or remove any that is not required, right-click the function in the Data panel of the main window and then select the corresponding command on the shortcut menu. You cannot delete functions that you have used in the report.

## Creating and Using Dynamic Aggregations

**To creating a dynamic aggregation:**

1. In the **Data** panel of the main window, or in the Resources box of the report wizard, expand the **Dynamic Resources** > **Aggregations** node, then select **<New Aggregation…>**. Designer displays the [New Aggregation dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010059902-New-Aggregation-Dialog-Box).

   ![New Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404856820247/nwaggrgtn.gif)
2. In the **Aggregation Name** text box, specify the name of the dynamic aggregation.
3. Select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) to specify the field on which the dynamic aggregation is based.

   You can map dynamic aggregations to the available resources such as group objects and detail objects in the current business view, or the dynamic formulas that you have created in the report.
4. From the **Aggregate Function** drop-down list, select the [function](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Function) to calculate the mapping field. If you select **DistinctSum**, you should select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848397591/btn_ellipsis.gif) next to the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010060462-Select-Fields-Dialog-Box) dialog box.
5. Select **OK** to create the dynamic aggregation.

Once you have created a dynamic aggregation, you can drag it from the Data panel to the desired position in the report, or add it as report field when working with the report wizard.

In the Data panel, you can make use of the shortcut menu of any existing dynamic aggregation to edit it in the [Edit Aggregation dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096161-Edit-Aggregation-Dialog-Box) or delete it. You cannot delete dynamic aggregations that you have used in the report.

## Creating and Using Local Parameters

1. In the **Data** panel of the main window, or when specifying the value of a filter condition for a data component using a business view with the Format Filter dialog box, select **<New Parameter…>** in the **Local Parameters** node.
2. In the New Parameter dialog box, [create the parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog) according to your requirement.
3. Select **OK** to create the parameter.

Once you have created a local parameter, you can then use it to [dynamically filter data](https://devnet.logianalytics.com/hc/en-us/articles/1500010101241-Filtering-Reports#EditFilter) of the data component in the report, add it to a [parameter control](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Param) or [parameter form control](https://devnet.logianalytics.com/hc/en-us/articles/1500010095041-Using-Advanced-Web-Controls#Form) in the report, or reference it in a dynamic record level pass one formula used in the report.

In the Data panel, you can also make use of the shortcut menu of any existing local parameter to edit or delete it. You cannot delete local parameters that you have used in the report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* You can only use JDK (not JRE) to compile dynamic formulas created in Logi Report.
* Currently, you cannot use global variables in dynamic formulas and user-defined functions.
* When dynamic formulas and user-defined functions reference display names or mapping names, the names should not contain any of the following characters if you do not quote the names with the double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression *@Customer#;* causes a syntax error, but *@"Customer#"* is ok.
  + If a field has the display name Category.Aggregation, quote it as "Category.Aggregation" or "Category"."Aggregation".

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101201-Changing-the-Display-Type-of-Objects-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101301-Delivering-Messages-Between-Library-Components)
