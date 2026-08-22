---
title: "Using Dynamic Resources and Local Parameters in a Report"
id: 5735534296599
section: "Designing Your Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report
updated_at: 2022-11-02T08:23:02Z
---

# Using Dynamic Resources and Local Parameters in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components)

# Using Dynamic Resources and Local Parameters in a Report

When working with a [business view](https://devnet.logianalytics.com/hc/en-us/articles/5735547021975-Working-with-Business-Views)-based report, sometimes you may find the predefined view elements in the business views the report applies, or the predefined [parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735532413719-Working-with-Parameters) in the current catalog cannot meet your requirements. In this case, you can create dynamic resources, including dynamic formulas, dynamic aggregations, and ![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898419617559/___newv19.1.png "New for version 19.1.")crosstab formulas, and local parameters and use them in the report to get the data you need. When you save the report, Designer saves the dynamic resources and local parameters as resources of the report in the report file. This topic describes how you can create and use dynamic resources and local parameters in a report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Dynamic resources and local parameters are report level resources, meaning, they are only available to the report for which you create them. Unless you need to use the formulas, aggregations, or parameters in multiple reports, you should create dynamic resources and local parameters rather than create them in the catalog.

This topic contains the following sections:

* [Creating and Using Dynamic Formulas](#Formula)
  + [Using User-Defined Functions in Dynamic Formulas](#UDF)
* [Creating and Using Dynamic Aggregations](#Agg)
* ![This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/9898419617559/___newv19.1.png "New for version 19.1.")[Creating and Using Crosstab Formulas](#CTFormula)
* [Creating and Using Local Parameters](#Param)

## Creating and Using Dynamic Formulas

**To create a dynamic formula**

1. Do one of the following:
   * In the **Data** panel of the main window, expand the **Dynamic Resources** > **Formulas** node and select **<New Formula…>**.
   * In the component wizard or dialog box that contains a dynamic formula list, select **<New Formula…>**.
   * In the value drop-down list for some object properties or dialog box options, select **<New Formula…>**.
2. In the Enter Formula Name dialog box, specify the name of the formula and select **OK**. Designer displays the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565964055-Formula-Editor-Dialog-Box).

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/9898405934871/fmlaedtr_dynmc.gif)
3. Compose the formula by selecting the required fields from the **Fields** panel (including view elements in the current business view, [parameters](https://devnet.logianalytics.com/hc/en-us/articles/5735525453207-Creating-Formulas-in-a-Catalog#RefParam) in the current catalog data source (global parameters), some [special fields](https://devnet.logianalytics.com/hc/en-us/articles/5735525453207-Creating-Formulas-in-a-Catalog#RefSpecial), and dynamic resources and [local parameters](#Param) in the current report), functions from the **Functions** panel (including [built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions) and [user-defined functions)](#UDF), and [operators](https://devnet.logianalytics.com/hc/en-us/articles/5735511732247-Appendix-2-Formula-Operators) from the **Operators** panel. You can also write the formula by yourself. You should have some knowledge of the [formula syntax](https://devnet.logianalytics.com/hc/en-us/articles/5735532056855-Formula-Syntax) before you can successfully compose a formula with no errors.
4. Specify how you want to use the formula, as a detail, group, or an aggregation object, by selecting the corresponding [view element type](https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements) from the **Use As** drop-down list on the toolbar.
   If you leave Use As empty (the default behavior), when you save the formula, Designer determines whether the formula can be used as an aggregation object; if it cannot, Designer applies it as a detail object.
   * You can use any formula as Detail.
   * You can use a formula that references a DBField and does not reference an aggregation as Group.
   * You can use a formula that only references aggregations as Aggregation. For example, there are two aggregations "Sum\_Total" and "Sum\_Quantity", and you can create a formula `@"Sum_Total" / @"Sum_Quantity"` and use it as an aggregation.
   * You can use a formula that follows the [custom aggregation expression](https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements#CA) as Aggregation.
5. Save the formula and close the editor. Designer adds the formula to the dynamic formula resource tree.

Once you have created a dynamic formula in a report, you can then [drag it from the Data panel](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields) to insert it in the report, add it as report field when working with the component wizard, or use it to [control property or option values](https://devnet.logianalytics.com/hc/en-us/articles/5735545031703-Using-Formulas-to-Control-Object-Properties).

In the Data panel, you can use the shortcut menu of any existing dynamic formula to edit or delete the formula, or change the formula type as Group, Detail, or Aggregation. You cannot delete dynamic formulas that you have used in the report.

### Using User-Defined Functions in Dynamic Formulas

Using Logi Report's [User-Defined Formula Function](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions) feature, you can create any functions as you want and apply them in your formulas. However, if you want to use user-defined functions in dynamic formulas, you need to create them specifically for the current report via the dynamic resource list.

**To create a user-defined function for a report**

1. In the **Data** panel of the main window, expand the **Dynamic Resources** > **User Defined Functions** node and select **<New Function…>**, or in the component wizard or dialog box that contains a dynamic resource list, select **<New Function…>**.
2. In the displayed dialog box, specify the name of the function and select **OK**.
3. In the [User Defined Function Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735553198231-User-Defined-Function-Editor-Dialog-Box), create the function according to your requirement.
4. Save the function. The function is then available under the **User Defined Functions** node in the **Functions** panel of the Formula Editor and User Defined Function Editor. You can then call it in a dynamic formula or another user-defined function by double-clicking it.

In the case a user-defined function named "function1" is `arguments: integer age, string name;`, you can call it as follows:

* `@function1(25, "John Smith");`
* `@'function1'(25, "John Smith");`
* `@"function1"(25, "John Smith");`

If you want to further edit an existing user-defined function or remove any that you do not need, right-click the function in the Data panel of the main window and then select the corresponding command on the shortcut menu. You cannot delete functions that you have used in the report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* You can only use JDK (not JRE) to compile dynamic formulas created in Logi Report.
* When you refer to any field in a formula, you need to add the "@" symbol as the prefix of the field's reference name. If the field name contains spaces, you need to quote the reference name with double quotation marks (""). For example, if the field name is Customer Name, the reference name is @"Customer Name".
* Logi Report limits the number of the "if-else" statements to 190. When this number is reached, you should use the "select-case" statement instead.
* You cannot use global variables in dynamic formulas and user-defined functions.
* When dynamic formulas and user-defined functions reference display names or mapping names, the names should not contain any of the following characters if you do not quote the names with the double-quotation marks (""):

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression *@Customer#;* causes a syntax error, but *@"Customer#"* is ok.
  + If a field has the display name Category.Measure, when you add it to a formula, you should quote it as
    "Category.Measure" or "Category"."Measure".

## Creating and Using Dynamic Aggregations

**To creating a dynamic aggregation**

1. In the **Data** panel of the main window, or in the Resources box of the component wizard, expand the **Dynamic Resources** > **Aggregations** node, then select **<New Aggregation…>**. Designer displays the [New Aggregation dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735514877719-New-Aggregation-Dialog-Box).

   ![New Aggregation](https://devnet.logianalytics.com/hc/article_attachments/9898405947415/nwaggrgtn.gif)
2. In the **Aggregation Name** text box, specify the name of the dynamic aggregation.
3. Select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) to specify the field on which the dynamic aggregation is based. You can map dynamic aggregations to the available resources such as group objects and detail objects in the current business view, or the dynamic formulas that you have created in the report.
4. From the **Aggregate Function** drop-down list, select the [function](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Function) to calculate the mapping field. If you select **DistinctSum**, you should select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898422868887/btn_ellipsis2.gif) next to the **Distinct On** text box to specify one or more fields according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735524767255-Select-Fields-Dialog-Box) dialog box.
5. Select **OK** to create the dynamic aggregation.

Once you have created a dynamic aggregation in a report, you can then [drag it from the Data panel](https://devnet.logianalytics.com/hc/en-us/articles/5735507390615-Working-with-Summary-Fields) to insert it in the report, or add it as report field when working with the component wizard.

In the Data panel, you can use the shortcut menu of any existing dynamic aggregation to edit it in the [Edit Aggregation dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513687703-Edit-Aggregation-Dialog-Box) or delete it. You cannot delete dynamic aggregations that you have used in the report.

## This image notes any new content for version 19.1 of the product. For more information please see the Release Notes or What's New topics.Creating and Using Crosstab Formulas

You can use crosstab formulas to apply custom aggregate functions in a business view-based crosstab, and control the properties of objects in the crosstab. See [Using Crosstab Formulas.](https://devnet.logianalytics.com/hc/en-us/articles/5735520960151-Using-Crosstab-Formulas)

## Creating and Using Local Parameters

1. Select **<New Parameter…>** in the **Local Parameters** node in one of the following cases:
   * In the Data panel of the main window when working with a business view-based report.
   * In the Fields panel of the Formula Editor dialog box when creating or editing a [dynamic formula](#Formula).
   * When specifying the value of a [filter condition for a business view-based dataset](https://devnet.logianalytics.com/hc/en-us/articles/5735555312279-Filtering-Datasets-in-a-Report).
2. In the New Parameter dialog box, [create the parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735516481047-Creating-Parameters-in-a-Catalog) according to your requirement.
3. Select **OK** to create the parameter.

Once you have created a local parameter in a report, you can then use it to [dynamically filter data components](https://devnet.logianalytics.com/hc/en-us/articles/5735534181911-Filtering-Reports#EditFilter) in the report, add it to [parameter controls](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Param) or [parameter form controls](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Form) in the report, or reference it in dynamic [record level pass one formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#PassOne) in the report.

In the Data panel, you can also use the shortcut menu of any existing local parameter to edit or delete it. You cannot delete local parameters that you have used in the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576827671-Delivering-Messages-Between-Library-Components)
