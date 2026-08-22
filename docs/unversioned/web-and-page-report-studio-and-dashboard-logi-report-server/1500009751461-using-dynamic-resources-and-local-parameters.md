---
title: "Using Dynamic Resources and Local Parameters "
id: 1500009751461
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters
updated_at: 2021-07-25T07:18:35Z
---

# Using Dynamic Resources and Local Parameters 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724822-Adding-Links-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data)

# Using Dynamic Resources and Local Parameters

When you add fields to a report or use parameters to define filter conditions in a report, sometimes you may find that the view elements that have been predefined in the business view or the given parameters in the current catalog cannot meet your requirements. In those cases, you can create dynamic resources (including formulas and aggregations) and local parameters in the report and use them to get the desired data. Then when you save the report, the dynamic resources and local parameters will be saved along with the report as its resources.

Dynamic resources and local parameters are report level resources, which means they are only available to the report for which they are created.

![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")In addition, when there are changes in a business view, Logi Report Server administrators can [recompile the dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009750121-Automatically-Recompiling-Dynamic-Resources-in-Reports) in reports that use the business view as the data source so that the dynamic resources can work normally.

A [Logi Report Live license for Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009749561-Logi-Report-licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

Select the following links to view the topics:

* [Creating and Using Dynamic Formulas](#DynamicFormula)

+ [Using User Defined Functions](#UDF)

* [Creating and Using Dynamic Aggregations](#Agg)
* [Creating and Using Local Parameters](#Param)

## Creating and Using Dynamic Formulas

You should have some knowledge of the formula syntax before you can successfully compose a formula with no errors. To learn about the syntax, refer to Formula Syntax in the *Logi Report Designer Guide*.

**To create a dynamic formula:**

1. In the Resources panel of Web Report Studio or the Resources box in the Web Report Wizard, expand the **Dynamic Resources** > **Formulas** node, then select **<Add Formula…>**. The [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009748461-Formula-Editor) appears.

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404942468247/fmlaedtr.gif)
2. Type a name for the formula in the Formula Name text box.
3. By default, Web Report Studio will decide whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object. You can specify to use the formula as a detail, group, or an aggregation object, by selecting the corresponding [view element type](https://devnet.logianalytics.com/hc/en-us/articles/1500009751441-An-Introduction-to-Business-Views) from the Use As drop-down list on the toolbar.

   Whether a dynamic formula can be used as a certain type depends on the following rules:

   * Any formula can be used as Detail.
   * Any formula that references a DBField and not an aggregation can be used as Group.
   * A formula that refers only to aggregations can be used as Aggregation. For example, there are two aggregations Sum\_Total and Sum\_Quantity, and you can create a formula `@"Sum_Total" / @"Sum_Quantity"` and use it as an aggregation.
   * A formula that follows the custom aggregation expression can be used as Aggregation. For details about the expression, refer to Custom Aggregation in the *Logi Report Designer Guide*.
4. Compose the formula by selecting the required fields, functions including built-in functions and [user defined functions](#UDF), and operators from the Fields, Functions and Operators boxes respectively. You can also write the formula by yourself in the editing box.

   For detailed information about the built-in functions and operators Web Report Studio supports, refer to Appendix 1: Formula Functions and Appendix 2: Formula Operators in the *Logi Report Designer Guide*.
5. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404936750359/btn_pgrpt_check.gif) to check whether or not the syntax of your formula is correct.
6. When done, select the **OK** button to create the formula.

Once a dynamic formula is created, you can then drag it from the Resources panel to the desired position in the report for data analyzing, add it as report field when working with the report wizard, or use it to create expressions in the Formula Editor.

If you want to further edit an existing dynamic formula, remove any that is not required, or change the formula type as Group, Detail, or Aggregation if possible, right-click the formula in the Resources panel of Web Report Studio and then select the corresponding command on the shortcut menu. Dynamic formulas that have been used in the report cannot be deleted.

### Using User Defined Functions

When you create dynamic formulas to use in a report, if the built-in functions do not satisfy your requirements, you can make use of the User Defined Function feature to create any functions as you want. Then when you save the report, the functions will be saved into the report as its resources the same as dynamic formulas. User defined functions can also call other user defined functions.

**To create a user defined function:**

1. In the Resources panel of Web Report Studio or the Resources box in the Web Report Wizard, expand the **Dynamic Resources** > **User Defined Functions** node, then select **<Add Function…>**. The [User Defined Function Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009749521-User-Defined-Function-Editor) appears.

   ![User Defined Function Editor](https://devnet.logianalytics.com/hc/article_attachments/4404942468503/udfedtr.gif)
2. Type a name for the function in the Function Name text box.
3. Compose the function by double-clicking the required fields, functions including built-in functions and other user defined functions, and operators from the Fields, Functions and Operators boxes. You can also write the function by yourself in the editing box.

   The function syntax is as follows:

   *arguments: VariableType1 VariableName1, VariableType2 VariableName2, ...;*

   For example, `arguments: integer age, string name;`

   An argument works the same as a local variable except that it is not allowed to assign any value to it, like `arguments: integer age=10;`.
4. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404936750359/btn_pgrpt_check.gif) to check whether or not the syntax of your function is correct.
5. Select the **OK** button to create the function.

   The function is then available under the User Defined Functions node in the Functions box of the Formula Editor and User Defined Function Editor. You can call it in a dynamic formula or another user defined function by double-clicking it.

Suppose a user defined function named function1 is written as: `arguments: integer age, string name;`, you can call it as follows:

* `@function1(25, "John Smith");`
* `@'function1'(25, "John Smith");`
* `@"function1"(25, "John Smith");`

If you want to further edit an existing user defined function or remove any that is not required, right-click the function in the Resources panel of Web Report Studio and then select the corresponding command on the shortcut menu. Functions that have been used in the report cannot be deleted.

## Creating and Using Dynamic Aggregations

In Web Report Studio, you can also create dynamic aggregations by mapping them to the available resources such as group objects, detail objects in the current business view and the dynamic formulas that have been created in the report.

**To create a dynamic aggregation:**

1. In the Resources panel of Web Report Studio or the Resources box of the Web Report Wizard, expand the **Dynamic Resource** > **Aggregations** node, then select **<Add Aggregation…>**. Report Server displays the [Add Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009721182-Add-Aggregation) dialog box.

   ![Add Aggregation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404942468759/addaggrgtn.gif)
2. In the Aggregation Name text box, specify the display name of the dynamic aggregation.
3. Select ![Select Source](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) next to the Mapping Name text box. In the [Select Resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009722242-Select-Resource) dialog box, specify the field on which the dynamic aggregation is based.
4. From the Aggregate Function drop-down list, specify the aggregate function. When DistinctSum is selected, you should select ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) next to the Distinct On text box to specify one or more group and detail objects according to whose unique values to calculate DistinctSum using the [Select Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009749361-Select-Fields).

   For the usage about each function, refer to Aggregate Functions in the *Logi Report Designer Guide*.
5. Select **OK** to create the dynamic aggregation.

Once a dynamic aggregation is created, you can then drag it from the Resources panel to the desired position in the report for data analyzing, add it as report field when working with the report wizard, or use it to create expressions in the Formula Editor. And if you want to edit any dynamic aggregation or delete it, right-click the aggregation and select **Edit** or **Delete** on the shortcut menu.

## Creating and Using Local Parameters

When you use parameters to compose the filter conditions applied to a report, if the given parameters in the current catalog cannot meet your requirements, you can create local parameters to use in the report. The local parameters created for a report can also be added to the [parameter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009751581-Using-Web-Controls#Parameter) and [parameter form controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009751581-Using-Web-Controls#Form) in the report, or referenced in [dynamic formulas](#DynamicFormula) used in the report.

**To create a local parameter and use it in a filter:**

1. When filtering [a business view in the Query Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters#BV) dialog box, or [a data component using the Filter](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters#Dialog) dialog box, select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404936748567/btn_dshbrd_prm.gif) and select **<Add Parameter…>** from the **Local Parameters** node of the value drop-down list.

   Report Server displays the [Add Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009721202-Add-Parameter) dialog box.

   ![Add Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936750615/addprm.gif)
2. In the Name field, type a name for the parameter.
3. Select a parameter type from the Value Setting drop-down list.
4. In the value section, specify the parameter values as required. The section varies with the type you select from the Value Setting drop-down list.
   * **For Type-in Parameter:**
     1. Specify the data type of the parameter value from the Value Type drop-down list.
     2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add a value line, double-click in it and then type a value of the specified data type.

        If the parameter is of Date, DateTime, or Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) to set a date and time value using the calendar.
     3. Repeat the above step to add more values.

        To adjust the order of the values, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif); to remove any unwanted value, select it in the list and then select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).
     4. To make a value the default selected value for the parameter, select it from the list.
   * **For Bind with Single Column**  
     Logi Report provides a mechanism that links each value of the display DBField with the exact value of the bound DBField, so that when you select a value of the display field, the value of the bound field is actually sent to the query and filters the query result. This can help you bind the parameter to a DBField in order to provide a list of values for the report users to select which probably makes more sense. The selected value of the bound field will be used as the parameter value. For example, it might be confusing if you provide a list of customer ID numbers for the report users to select, since the ID numbers would probably mean nothing to them. In cases like this, it is better for you to display values of other fields, which would make more sense. For this case, you might prefer to display customer names instead of ID numbers. When the report users select a customer name from the list, its ID number is passed to the query as the parameter value so that the search criteria can be fulfilled.
     1. From the Source drop-down list, select the required business view in the current data source from which to get data for the parameter. All the group and detail objects in the specified business view will be available for retrieving values for the parameter.
     2. Select a field from the Bind Column drop-down list. This field is used to filter the query when running a report with the parameter.
     3. If you want the values of another field to be displayed for the report users to choose from, select that field from the Display Column drop-down list.

        Logi Report provides a mechanism that links each value of the display field with the exact value of the bound field for a parameter, thus when you select a value of the display field, the value of the bound field is actually sent to the query and filters the query result. This can help you bind the parameter to a DBField in order to provide a list of values for report users to select which probably makes more sense. The selected value of the bound field will be used as the parameter value. For example, it might be confusing if you provide a list of customer ID numbers for users to select at runtime, since the ID numbers would probably mean nothing to them. In cases like this, it is better for you to display values of other fields, which would make more sense. For this case, you might prefer to display customer names instead of ID numbers. When the report users select a customer name from the list, its ID number is passed to the query as the parameter value so that the search criteria can be fulfilled.
   * **For Bind with Cascading Columns:**
     1. From the Data Source drop-down list, select the required business view in the current data source from which to get data for the parameter. All the group and detail objects in the specified business view will be available for retrieving values for the parameter.
     2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add a parameter row.
     3. Select in the Bind Column cell and select a field from the drop-down list.
     4. If you want the values of another field to be displayed for the report users to choose from, select in the Display Column cell and select that field from the drop-down list.
     5. Select in the Parameter cell to create the parameter. A name for the parameter will then be automatically added by Logi Report.
     6. Repeat steps b to e to create more parameters. Make sure that the selected Bind Column fields are of cascading relationship one level by one level down. In this way, a group of cascading parameters are created.

        To adjust the order of the parameters, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif); to remove any unwanted parameter from the cascading group, select it and then select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).
5. In the Options box, set [options](https://devnet.logianalytics.com/hc/en-us/articles/1500009721202-Add-Parameter#Options) for the parameter according to your requirements.
6. When done, select **OK** to create the parameter. The parameter is added to the Local Parameters node in the Parameters list.

   To further edit the parameter, right-click it in the list and select **Edit** from the shortcut menu. Then in the [Edit Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009721562-Edit-Parameter) dialog box, edit the parameter as required.

   To remove the parameter, right-click it in the list and select **Delete** on the shortcut menu.
7. Finish defining the filter condition using the parameter.
8. Select **OK** to apply the settings. The parameter is then listed in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009724862-Applying-Parameters) and you can specify the parameter value in the panel to dynamically set the filter condition.

**Notes:**

* You can only use JDK (not JRE) to compile formulas and user defined functions created in Web Report Studio and save them with no errors into a web report.
* Currently, global variables are not supported in dynamic formulas and user defined functions.
* If you refer to any field in a formula or user defined function, the reference name for that field will be prefixed with an @ sign. If the field name contains spaces, the reference name will be quoted with double-quotation marks (""). For example, if the field name is Customer Name, then the reference name will be @"Customer Name".
* When formulas and user defined functions reference display names or mapping names, the names should not contain any of the following characters if the names are not quoted by double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression @Customer#; will cause a syntax error. But @"Customer#" is ok.
  + If a field has the display name Category.Aggregation, quote it as "Category.Aggregation" or "Category"."Aggregation".

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724822-Adding-Links-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data)
