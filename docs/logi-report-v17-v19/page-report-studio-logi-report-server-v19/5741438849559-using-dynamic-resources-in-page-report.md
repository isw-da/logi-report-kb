---
title: "Using Dynamic Resources in Page Report"
id: 5741438849559
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741438849559-Using-Dynamic-Resources-in-Page-Report
updated_at: 2022-10-31T17:18:13Z
---

# Using Dynamic Resources in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/7985371620375-Managing-Datasets-in-Page-Report)

# Using Dynamic Resources in Page Report

When the view elements in a business view cannot meet your requirements, you can create dynamic resources including dynamic formulas, dynamic aggregations, and crosstab formulas, and use them in a report to get the data you want. This topic describes how you can create and use dynamic resources in page reports.

When you save a report, Server saves the dynamic resources along with the report as its resources.

Dynamic resources are report tab level resources. They are only available to the report tab for which you created them.

In addition, when there are changes in a business view, Server administrators can [recompile the dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/5741482130199-Automatically-Recompiling-Dynamic-Resources-in-Reports) in reports that use the business view as the data source so that the dynamic resources can work normally.

You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/5741452341143-Logi-Report-Licenses#ServerLive) to use this feature. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

This topic contains the following sections:

* [Creating and Using Dynamic Formulas](#Formula)

+ [Using User Defined Functions](#UDF)

* [Creating and Using Dynamic Aggregation Objects](#Agg)
* [Creating and Using Crosstab Formulas](#CrosstabFormula)

## Creating and Using Dynamic Formulas

You should have some knowledge of the formula syntax before you can successfully compose a formula without errors. To learn about the syntax, see Formula Syntax in the *Logi Report Designer Guide*.

**To create a dynamic formula:**

1. In the Resource View panel, expand the **Dynamic Resources** > **Formulas** node, then select **<Add Formula…>**. Server displays the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5741410542999-Formula-Editor-Properties).

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/9905661970199/fmlaedtr.gif)
2. Type a name for the formula in Formula Name text box.
3. By default, Server will decide whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object. You can specify to use the formula as a detail, group, or an aggregation object, by selecting the corresponding [view element type](https://devnet.logianalytics.com/hc/en-us/articles/5741484450455-An-Introduction-to-Business-Views) from the Use As drop-down list on the toolbar.

   Whether you can use a dynamic formula as a certain type depends on the following rules:

   * You can use any formula as Detail.
   * You can use any formula that references a DBField excluding an aggregation as Group.
   * You can use a formula that refers only to aggregations as Aggregation. For example, there are two aggregations Sum\_Total and Sum\_Quantity, and you can create a formula `@"Sum_Total" / @"Sum_Quantity"` and use it as an aggregation.
   * You can use a formula that follows the custom aggregation expression as Aggregation. For more information, see Custom Aggregation in the *Logi Report Designer Guide*.
4. Compose the formula by selecting the required fields, functions including built-in functions and [user defined functions](#UDF), and operators from the Fields, Functions, and Operators boxes, respectively. You can also write the formula by yourself in the editing box.

   For more information about the built-in functions and operators Page Report Studio supports, see Appendix 1: Formula Functions and Appendix 2: Formula Operators in the *Logi Report Designer Guide*.
5. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/9905613668631/btn_pgrpt_check.gif) to check whether the syntax of your formula is correct.
6. Select the **OK** button to create the formula.

Once a dynamic formula is created, you can then drag it from the Resource View panel to the position you want in the report for data analyzing. The formulas can also be used to [control object properties](https://devnet.logianalytics.com/hc/en-us/articles/5741469351191-Making-Simple-Modifications-to-Page-Report-Objects#Property) if you are an [advanced user](https://devnet.logianalytics.com/hc/en-us/articles/5741427459479-Page-Report-Studio-Profile-Properties#AdvUser) and provided that the Use Dynamic Formula in Property is selected on the Report menu.

If you want to further edit an existing dynamic formula, remove any that is not required, or change the formula type as Group, Detail, or Aggregation if possible, right-click the formula and then select the corresponding command on the shortcut menu. Dynamic formulas that have been used in the report cannot be deleted.

### Using User Defined Functions

When you create dynamic formulas to use in a report, if the built-in functions do not satisfy your requirements, you can make use of the User Defined Function feature to create any functions as you want. Then when you save the report tab, the functions will be saved into the report tab as its resources the same as dynamic formulas. User defined functions can also call other user defined functions.

**To create a user defined function:**

1. In the Resource View panel, navigate to **Dynamic Resources** > **User Defined Functions**, then select **<Add Function…>**. Server displays the [User Defined Function Editor](https://devnet.logianalytics.com/hc/en-us/articles/5741419160855-User-Defined-Function-Editor-Properties).

   ![User Defined Function Editor](https://devnet.logianalytics.com/hc/article_attachments/9905662014999/udfedtr.gif)
2. Type a name for the function in the **Function Name** text box.
3. Compose the function by double-clicking the required fields, functions including built-in functions and other user defined functions, and operators from the Fields, Functions, and Operators boxes respectively. You can also write the function by yourself in the editing box.

   The function syntax is:

   *arguments: VariableType1 VariableName1, VariableType2 VariableName2, ...;*

   For example, `arguments: integer age, string name;`

   An argument works the same as a local variable except that you cannot assign any value to it, like `arguments: integer age=10;`.
4. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/9905613668631/btn_pgrpt_check.gif) to check whether the syntax of your function is correct.
5. Select **OK** to create the function.

   The function is then available under the User Defined Functions node in the Functions box of the Formula Editor, Crosstab Formula Editor, and User Defined Function Editor. You can call it in a dynamic formula, a crosstab formula, or another user defined function by double-clicking it.

Suppose a user defined function named function1 is `arguments: integer age, string name;`, you can call it as follows:

* `@function1(25, "John Smith");`
* `@'function1'(25, "John Smith");`
* `@"function1"(25, "John Smith");`

If you want to further edit or remove an existing user defined function, right-click the function in the Resource View panel, and then select the corresponding command on the shortcut menu. You cannot delete user defined functions when you have used them in the report.

## Creating and Using Dynamic Aggregation Objects

In Page Report Studio, you can also create dynamic aggregation objects by mapping them to the available resources which include group objects, detail objects in the current business view, and the dynamic formulas that you have created in the report.

**To create a dynamic aggregation object:**

1. In the Resource View panel, navigate to **Dynamic Resources** > **Aggregations**, then select **<Add Aggregation…>**. Server displays the [Add Aggregation dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741396640407-Add-Aggregation-Dialog-Box-Properties).

   ![Add Aggregation dialog](https://devnet.logianalytics.com/hc/article_attachments/9905662077975/addaggrgtn.gif)
2. In the **Aggregation Name** text box, specify the display name of the aggregation object.
3. Select the ellipsis button ![Select Source](https://devnet.logianalytics.com/hc/article_attachments/9905577763991/btn_chsr2.gif) next to the Mapping Name text box. Server displays the [Select Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741440630295-Select-Resource-Dialog-Box-Properties).
4. Specify a field or a formula on which the aggregation object is based.

   ![Select Source dialog](https://devnet.logianalytics.com/hc/article_attachments/9905662108311/slctrsc.gif)
5. Select **OK**.
6. From the **Aggregate Function** drop-down list, specify the aggregate function for the aggregation object. When you selected **DistinctSum**, you should select the ellipsis button ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/9905577763991/btn_chsr2.gif) next to the **Distinct On** text box. Server displays the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741440574103-Select-Fields-Dialog-Box-Properties).
   Select one or more group and detail objects according to whose unique values you want to calculate DistinctSum.

   For the usage about each function, refer to Aggregate Functions in the *Logi Report Designer Guide*.
7. Select **OK** to create the aggregation object.

You can also create a dynamic aggregation object on a dynamic formula. To do this:

1. In the Resource View panel, right-click the formula in the Dynamic Resources > Formulas node, then select **Add Aggregation** from the shortcut menu.
2. In the Add Aggregation dialog box, specify the display name of the aggregation object and the aggregate function.
3. Select **OK**.

Once you create a dynamic aggregation object, you can then drag it from the Resource View panel to the position you want in the report for data analyzing.

You can further modify any dynamic aggregation object. To do this, right-click the aggregation object and select **Edit** from the shortcut menu. Then in the [Edit Aggregation dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741396640407-Add-Aggregation-Dialog-Box-Properties), edit the aggregation object.

For dynamic aggregation objects that you don't need, you can remove them. To delete an aggregation object, right-click it and select **Delete** on the shortcut menu. You cannot remove aggregation objects when you have used them in the report.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* You can only use JDK (not JRE) to compile formulas and user defined functions created in Page Report Studio and save them with no errors into a report.
* Currently, you cannot use global variables in dynamic formulas and user defined functions.
* If you refer to any field in a formula or user defined function, you should add a prefix @ before the reference name for that field. If the field name contains spaces, quote the reference name with double-quotation marks (""). For example, if the field name is Customer Name, then the reference name will be @"Customer Name".
* When formulas and user defined functions reference display names or mapping names, the names should not contain any of the following characters if you do not quote the names by double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression @Customer#; will cause a syntax error. But @"Customer#" is ok.
  + If a field has the display name Category.Measure, quote it as "Category.Measure" or "Category"."Measure".

## Creating and Using Crosstab Formulas

Crosstab formulas are a type of extended formulas. You can insert crosstab formulas into crosstabs as aggregations and use them to control the property values of crosstab fields. Crosstab formulas are private resources on the crosstab level, which you cannot use beyond their crosstabs.

To support more powerful and flexible calculation logic in crosstabs, crosstab formula extends the basic Formula Syntax in the following aspects:

* A crosstab formula can reference another crosstab formula within the same crosstab. The format is `@@<Crosstab_Formula_Name>`, for example, `@@CTF1`, where *CTF1* is the name of a crosstab formula. In this case, you can write the crosstab formula expression as `@(@@CTF1)`.
* A crosstab formula can reference summary expression that follows the syntax of custom aggregation expression. For example,

  `@(Sum(@Sales))`  
  `@(@Country:"USA",@Year:CHILDREN, Sum(@Sales))`  
  `@(@Country:"USA",@Year:CHILDREN, @@CTF1)`

  For more information, see Custom Aggregation in the *Logi Report Designer Guide*.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* You cannot use global variables in crosstab formulas.
* You cannot reference detail fields and record level pass one formulas in crosstab formulas, except for referencing them in summary expression.
* You cannot use the Array functions as `array_function (field_variable, groupby)` in crosstab formulas (*array\_function* here refers to any Array function defined in Logi Report). For example, Logi Report does not allow `Maximum(@dbfield, "group_field")` and `Average(@formula, @parameter)` in crosstab formulas.

**To create a crosstab formula:**

1. In the Resource View panel of Page Report Studio, navigate to **Dynamic Resources** > **Crosstab Formulas**. Then, select **<Add Crosstab Formula…>**, or right-click a crosstab formula and select **Edit** from the shortcut menu.
   Server displays the [Crosstab Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5741450053911-Formula-Editor-Properties).

   ![Crosstab Formula Editor dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905575657495/crstbfmledtr.gif)
2. Type a name for the crosstab formula in the **Formula Name** text box.
3. Compose the formula by selecting the required fields, functions including built-in functions, [user defined functions](#UDF), and crosstab formulas, and operators from the Fields, Functions, and Operators boxes respectively. You can also write the formula by yourself in the editing box.

   For more information, see Appendix 1: Formula Functions and Appendix 2: Formula Operators in the *Logi Report Designer Guide*.
4. To insert an operator into your formula, you can also select the Add Operators button ![Operator button](https://devnet.logianalytics.com/hc/article_attachments/9905613365783/btn_wbrpt_oprtr.gif) and then select an operator.
5. To insert the HEX code of a color into your formula, select the Color Converter button ![Operator button](https://devnet.logianalytics.com/hc/article_attachments/9905613365783/btn_wbrpt_oprtr.gif), and then select a color in the [Select Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741389405847-Select-Color-Dialog-Box-Properties).
6. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/9905613668631/btn_pgrpt_check.gif) to check whether the syntax of your formula is correct.
7. Select **OK** to create the crosstab formula.

Once you create the crosstab formula, you can then add it in the crosstab as an aggregation, use it to control property values of the fields in the crosstab in a dialog box, and use it to [perform conditional formatting](https://devnet.logianalytics.com/hc/en-us/articles/5741454332311-Adding-Conditional-Formats-to-Fields-in-Page-Report) on the fields in the crosstab.

If you want to further edit or remove an existing crosstab formula, right-click it in the Resource View panel of Page Report Studio and then select the corresponding command on the shortcut menu. You cannot edit or remove crosstab formulas when you have used them in the report.

![Edit and Remove Crosstab Formula](https://devnet.logianalytics.com/hc/article_attachments/9905655388567/wbrpt_edt_dynrsc_edtcrstbfml.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741469268887-Applying-Filters-to-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/7985371620375-Managing-Datasets-in-Page-Report)
