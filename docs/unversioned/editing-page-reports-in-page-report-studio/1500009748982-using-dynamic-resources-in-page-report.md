---
title: "Using Dynamic Resources in Page Report"
id: 1500009748982
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748982-Using-Dynamic-Resources-in-Page-Report
updated_at: 2021-07-24T00:47:52Z
---

# Using Dynamic Resources in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777561-Applying-Filters-to-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777621-Sorting-Page-Report-Data)

# Using Dynamic Resources in Page Report

When the view elements in a business view cannot meet your requirements, you can create dynamic resources including formulas and aggregations and use them in a report to get the desired data. This topic describes how you can create and use dynamic formulas and aggregations in page reports.

When you save a report, Server saves the dynamic resources along with the report as its resources.

Dynamic resources are report tab level resources. They are only available to the report tab for which you created them.

In addition, when there are changes in a business view, Logi Report Server administrators can [recompile the dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009748722-Automatically-Recompiling-Dynamic-Resources-in-Reports) in reports that use the business view as the data source so that the dynamic resources can work normally.

You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009776661-Logi-Report-Licenses#ServerLive) to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

This topic contains the following sections:

* [Creating and Using Dynamic Formulas](#Formula)

+ [Using User Defined Functions](#UDF)

* [Creating and Using Dynamic Aggregation Objects](#Agg)

## Creating and Using Dynamic Formulas

You should have some knowledge of the formula syntax before you can successfully compose a formula without errors. To learn about the syntax, see Formula Syntax in the *Logi Report Designer Guide*.

**To create a dynamic formula:**

1. In the Resource View panel, expand the **Dynamic Resources** > **Formulas** node, then select **<Add Formula…>**. Server displays the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009772221-Formula-Editor-Properties).

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404880266263/fmlaedtr.gif)
2. Type a name for the formula in Formula Name text box.
3. By default, Page Report Studio will decide whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object. You can specify to use the formula as a detail, group, or an aggregation object, by selecting the corresponding [view element type](https://devnet.logianalytics.com/hc/en-us/articles/1500009749982-An-Introduction-to-Business-Views) from the Use As drop-down list on the toolbar.

   Whether a dynamic formula can be used as a certain type depends on the following rules:

   * Any formula can be used as Detail.
   * Any formula that references a DBField and not an aggregation can be used as Group.
   * A formula that refers only to aggregations can be used as Aggregation. For example, there are two aggregations Sum\_Total and Sum\_Quantity, and you can create a formula `@"Sum_Total" / @"Sum_Quantity"` and use it as an aggregation.
   * A formula that follows the custom aggregation expression can be used as Aggregation. For more information, see Custom Aggregation in the *Logi Report Designer Guide*.
4. Compose the formula by selecting the required fields, functions including built-in functions and [user defined functions](#UDF), and operators from the Fields, Functions, and Operators boxes, respectively. You can also write the formula by yourself in the editing box.

   For more information about the built-in functions and operators Page Report Studio supports, see Appendix 1: Formula Functions and Appendix 2: Formula Operators in the *Logi Report Designer Guide*.
5. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404880193559/btn_pgrpt_check.gif) to check whether the syntax of your formula is correct.
6. Select the **OK** button to create the formula.

Once a dynamic formula is created, you can then drag it from the Resource View panel to the desired position in the report for data analyzing. The formulas can also be used to [control object properties](https://devnet.logianalytics.com/hc/en-us/articles/1500009749042-Making-Simple-Modifications-to-Page-Report-Objects#Property) if you are an [advanced user](https://devnet.logianalytics.com/hc/en-us/articles/1500009777681-Customizing-Page-Report-Studio-Profile#AdvUser) and provided that the Use Dynamic Formula in Property is selected on the Report menu.

If you want to further edit an existing dynamic formula, remove any that is not required, or change the formula type as Group, Detail, or Aggregation if possible, right-click the formula and then select the corresponding command on the shortcut menu. Dynamic formulas that have been used in the report cannot be deleted.

### Using User Defined Functions

When you create dynamic formulas to use in a report, if the built-in functions do not satisfy your requirements, you can make use of the User Defined Function feature to create any functions as you want. Then when you save the report tab, the functions will be saved into the report tab as its resources the same as dynamic formulas. User defined functions can also call other user defined functions.

**To create a user defined function:**

1. In the Resource View panel, expand the **Dynamic Resources** > **User Defined Functions** node, then select **<Add Function…>**. The [User Defined Function Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009745302-User-Defined-Function-Editor-Properties) appears.

   ![User Defined Function Editor](https://devnet.logianalytics.com/hc/article_attachments/4404885397143/udfedtr.gif)
2. Type a name for the function in the Function Name text box.
3. Compose the function by double-clicking the required fields, functions including built-in functions and other user defined functions, and operators from the Fields, Functions and Operators boxes respectively. You can also write the function by yourself in the editing box.

   The function syntax is as follows:

   *arguments: VariableType1 VariableName1, VariableType2 VariableName2, ...;*

   For example, `arguments: integer age, string name;`

   An argument works the same as a local variable except that it is not allowed to assign any value to it, like `arguments: integer age=10;`.
4. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404880193559/btn_pgrpt_check.gif) to check whether the syntax of your function is correct.
5. Select the **OK** button to create the function.

   The function is then available under the User Defined Functions node in the Functions box of the Formula Editor and User Defined Function Editor. You can call it in a dynamic formula or another user defined function by double-clicking it.

Suppose a user defined function named function1 is written as: `arguments: integer age, string name;`, you can call it as follows:

* `@function1(25, "John Smith");`
* `@'function1'(25, "John Smith");`
* `@"function1"(25, "John Smith");`

If you want to further edit an existing user defined function or remove any that is not required, right-click the function in the Resource View panel and then select the corresponding command on the shortcut menu. Functions that have been used in the report cannot be deleted.

## Creating and Using Dynamic Aggregation Objects

In Page Report Studio, you can also create dynamic aggregation objects by mapping them to the available resources which include group objects, detail objects in the current business view and the dynamic formulas that have been created in the report.

**To create a dynamic aggregation object:**

1. In the Resource View panel, expand the **Dynamic Resources** > **Aggregations** node, then select **<Add Aggregation…>**. Server displays the [Add Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009771921-Add-Aggregation-Dialog-Box-Properties) dialog box.

   ![Add Aggregation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885397783/addaggrgtn.gif)
2. In the Aggregation Name text box, specify the display name of the aggregation object.
3. Select ![Select Source](https://devnet.logianalytics.com/hc/article_attachments/4404880145687/btn_chsr2.gif) next to the Mapping Name text box. In the [Select Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009773021-Select-Resource-Dialog-Box-Properties) dialog box, specify a field or a formula on which the aggregation object is based.

   ![Select Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880266775/slctrsc.gif)
4. From the Aggregate Function drop-down list, specify the aggregate function for the aggregation object. When DistinctSum is selected, you should select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404880145687/btn_chsr2.gif) next to the Distinct On text box to specify one or more group and detail objects according to whose unique values to calculate DistinctSumin using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009745042-Select-Fields-Dialog-Box-Properties) dialog box.

   For the usage about each function, refer to Aggregate Functions in the *Logi Report Designer Guide*.
5. When done, select **OK** to create the aggregation object.

You can also create a dynamic aggregation object on a dynamic formula. To do this:

1. In the Resource View panel, right-click the formula in the Dynamic Resources > Formulas node, then select **Add Aggregation** from the shortcut menu.
2. In the Add Aggregation dialog box, specify the display name of the aggregation object and the aggregate function as required.
3. When done, select **OK**.

Once a dynamic aggregation object is created, you can then drag it from the Resource View panel to the desired position in the report for data analyzing.

You can further modify any dynamic aggregation object. To do this, right-click the aggregation object and select **Edit** from the shortcut menu. Then in the [Edit Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009771921-Add-Aggregation-Dialog-Box-Properties) dialog box, edit the aggregation object as required.

For dynamic aggregation objects that are on longer required, you can remove them. To delete an aggregation object, right-click it and select **Delete** on the shortcut menu. Aggregation objects that have been used in the report cannot be deleted.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* You can only use JDK (not JRE) to compile formulas and user defined functions created in Page Report Studio and save them with no errors into a report.
* Currently, you cannot use global variables in dynamic formulas and user defined functions.
* If you refer to any field in a formula or user defined function, you should add a prefix @ before the reference name for that field. If the field name contains spaces, quote the reference name with double-quotation marks (""). For example, if the field name is Customer Name, then the reference name will be @"Customer Name".
* When formulas and user defined functions reference display names or mapping names, the names should not contain any of below characters if you do not quote the names by double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression @Customer#; will cause a syntax error. But @"Customer#" is ok.
  + If a field has the display name Category.Measure, quote it as "Category.Measure" or "Category"."Measure".

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009777561-Applying-Filters-to-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009777621-Sorting-Page-Report-Data)
