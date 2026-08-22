---
title: "Using Dynamic Resources and Local Parameters in Web Report "
id: 1500009750082
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009750082-Using-Dynamic-Resources-and-Local-Parameters-in-Web-Report
updated_at: 2021-07-24T00:47:30Z
---

# Using Dynamic Resources and Local Parameters in Web Report 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778801-Adding-Links-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778781-Going-Through-Web-Report-Data)

# Using Dynamic Resources and Local Parameters in Web Report

This topic describes how you can create dynamic formulas, user defined functions, dynamic aggregations, and local parameters in web reports.

When you add fields to a report or use parameters to define filter conditions in a report, sometimes you may find that the predefined view elements in the business view or the given parameters in the current catalog cannot meet your requirements. In those cases, you can create dynamic resources (including formulas and aggregations) and local parameters in the report and use them to get the desired data. Then when you save the report, Server saves the dynamic resources and local parameters along with the report as its resources.

Dynamic resources and local parameters are report level resources, which means they are only available to the report for which you created them.

In addition, when there are changes in a business view, Logi Report Server administrators can [recompile the dynamic resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009748722-Automatically-Recompiling-Dynamic-Resources-in-Reports) in reports that use the business view as the data source so that the dynamic resources can work normally.

You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009776661-Logi-Report-Licenses#ServerLive) to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

This topic contains the following sections:

* [Creating and Using Dynamic Formulas](#DynamicFormula)

+ [Using User Defined Functions](#UDF)

* [Creating and Using Dynamic Aggregations](#Agg)
* [Creating and Using Local Parameters](#Param)

## Creating and Using Dynamic Formulas

You should have some knowledge of the formula syntax before you can successfully compose a formula without errors. To learn about the syntax, see Formula Syntax in the *Logi Report Designer Guide*.

**To create a dynamic formula:**

1. In the Resources panel of Web Report Studio or the Resources box in the Web Report Wizard, expand the **Dynamic Resources** > **Formulas** node, then select **<Add Formula…>**. Server displays the [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009775341-Formula-Editor-Properties).

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404885343383/fmlaedtr.gif)
2. Type a name for the formula in the **Formula Name** text box.
3. By default, Logi Report decides whether it can use the formula as an aggregation object, and if not, uses it as a detail object. You can specify to use the formula as a detail, group, or an aggregation object, by selecting the corresponding [view element type](https://devnet.logianalytics.com/hc/en-us/articles/1500009749982-An-Introduction-to-Business-Views) from the **Use As** drop-down list on the toolbar.

   Whether you can use a dynamic formula as a certain type depends on the following rules:

   * You can use any formula as Detail.
   * You can use any formula that references a DBField and not an aggregation as Group.
   * You can use a formula that refers only to aggregations as Aggregation. For example, there are two aggregations Sum\_Total and Sum\_Quantity, and you can create a formula `@"Sum_Total" / @"Sum_Quantity"` and use it as an aggregation.
   * You can use a formula that follows the custom aggregation expression as Aggregation. For more information, see Custom Aggregation in the *Logi Report Designer Guide*.
4. Compose the formula by selecting the required fields, functions including built-in functions and [user defined functions](#UDF), and operators from the Fields, Functions, and Operators boxes respectively. You can also write the formula by yourself in the editing box.

   For more information, see Appendix 1: Formula Functions and Appendix 2: Formula Operators in the *Logi Report Designer Guide*.
5. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404880193559/btn_pgrpt_check.gif) to check whether the syntax of your formula is correct.
6. Select **OK** to create the formula.

Once you created a dynamic formula, you can then drag it from the Resources panel to the desired position in the report for data analyzing, add it as a report field when working with the report wizard, or use it to create expressions in the Formula Editor.

If you want to further edit an existing dynamic formula, remove any that you do not want any longer, or change the formula type as Group, Detail, or Aggregation, right-click the formula in the Resources panel of Web Report Studio and then select the corresponding command on the shortcut menu. You cannot delete dynamic formulas when you have used them in the report.

### Using User Defined Functions

When you create dynamic formulas to use in a report, if the built-in functions do not satisfy your requirements, you can make use of the User Defined Function feature to create any functions as you want. Then when you save the report, Logi Report saves the functions into the report as its resources the same as dynamic formulas. User defined functions can also call other user defined functions.

**To create a user defined function:**

1. In the Resources panel of Web Report Studio or the Resources box in the Web Report Wizard, expand the **Dynamic Resources** > **User Defined Functions** node, then select **<Add Function…>**. Server displays the [User Defined Function Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009776561-User-Defined-Function-Editor-Properties).

   ![User Defined Function Editor](https://devnet.logianalytics.com/hc/article_attachments/4404880193943/udfedtr.gif)
2. Type a name for the function in the **Function Name** text box.
3. Compose the function by double-clicking the required fields, functions including built-in functions and other user defined functions, and operators from the Fields, Functions, and Operators boxes. You can also write the function by yourself in the editing box.

   The function syntax is as follows:

   *arguments: VariableType1 VariableName1, VariableType2 VariableName2, ...;*

   For example, `arguments: integer age, string name;`

   An argument works the same as a local variable except that you cannot assign any value to it, like `arguments: integer age=10;`.
4. Select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404880193559/btn_pgrpt_check.gif) to check whether the syntax of your function is correct.
5. Select **OK** to create the function.

   Server displays the function under the **User Defined Functions** node in the Functions box of the Formula Editor and User Defined Function Editor. You can call it in a dynamic formula or another user defined function by double-clicking it.

Suppose a user defined function named function1 is written as: `arguments: integer age, string name;`, you can call it as follows:

* `@function1(25, "John Smith");`
* `@'function1'(25, "John Smith");`
* `@"function1"(25, "John Smith");`

If you want to further edit an existing user defined function or remove any that you no longer want, right-click the function in the Resources panel of Web Report Studio and then select the corresponding command on the shortcut menu. You cannot delete functions when you have used them in the report.

## Creating and Using Dynamic Aggregations

In Web Report Studio, you can also create dynamic aggregations by mapping them to the available resources such as group objects, detail objects in the current business view, and the dynamic formulas that you have created in the report.

**To create a dynamic aggregation:**

1. In the Resources panel of Web Report Studio or the Resources box of the Web Report Wizard, expand the **Dynamic Resource** > **Aggregations** node, then select **<Add Aggregation…>**. Server displays the [Add Aggregation](https://devnet.logianalytics.com/hc/en-us/articles/1500009746682-Add-Aggregation-Dialog-Box-Properties) dialog box.

   ![Add Aggregation dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880194455/addaggrgtn.gif)
2. In the **Aggregation Name** text box, type the display name of then dynamic aggregation. Or you can leave the name blank. Then when you finish selecting the mapping name and the aggregate function, Server automatically provides a name here.
3. Select the button ![Select Source](https://devnet.logianalytics.com/hc/article_attachments/4404885320983/btn_chsr.gif) next to the Mapping Name text box. Server displays the [Select Resource](https://devnet.logianalytics.com/hc/en-us/articles/1500009748022-Select-Resource-Dialog-Box-Properties) dialog box.
4. Select the field on which the dynamic aggregation is based.
5. From the **Aggregate Function** drop-down list, select the aggregate function. When you selected **DistinctSum**, you should select the button ![Select Resource](https://devnet.logianalytics.com/hc/article_attachments/4404885320983/btn_chsr.gif) next to the **Distinct On** text box. Server displays the [Select Fields dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500009776261-Select-Fields-Dialog-Box-Properties).
   Select one or more group and detail objects according to whose unique values to calculate DistinctSum.

   For more information, see Aggregate Functions in the *Logi Report Designer Guide*.
6. Select **OK** to create the dynamic aggregation.

Server adds the dynamic aggregation in the Resources panel. You can then drag it from to the desired position in the report for data analyzing, add it as a report field when working with the report wizard, or use it to create expressions in the Formula Editor. And if you want to edit any dynamic aggregation or delete it, right-click the aggregation and select **Edit** or **Delete** on the shortcut menu.

## Creating and Using Local Parameters

When you use parameters to compose the filter conditions to apply to a report, if the given parameters in the current catalog cannot meet your requirements, you can create local parameters to use in the report. You can also add the local parameters to the [parameter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009750222-Using-Web-Controls-in-Web-Report#Parameter) and [parameter form controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009750222-Using-Web-Controls-in-Web-Report#Form), or reference them in [dynamic formulas](#DynamicFormula) in the report.

**To create a local parameter and use it in a filter:**

1. When you filter [a business view in the Query Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500009778741-Applying-Filters-in-Web-Report#BV), or [a data component using the Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500009778741-Applying-Filters-in-Web-Report#Dialog), select the button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404880189463/btn_dshbrd_prm.gif) and then select **<Add Parameter…>** from the **Local Parameters** node of the value drop-down list.

   Server displays the [Add Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009774861-Add-Parameter-Dialog-Box-Properties) dialog box.

   ![Add Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404880194967/addprm.gif)
2. In the **Name** field, type a name for the parameter.
3. Select a parameter type from the **Value Setting** drop-down list.
4. In the value section, specify the parameter values as required. The section varies with the type you select from the Value Setting drop-down list.
   * **For Type-in Parameter:**
     1. Select the data type of the parameter values from the **Value Type** drop-down list.
     2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif) to add a value line, double-click in it and then type a value of the specified data type.

        If the parameter is of Date, DateTime, or Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404885317143/btn_clndr.gif) to set a date and time value using the calendar.
     3. Repeat the above step to add more values.
     4. To adjust the order of the values, select the **Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Down** button![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
     5. To remove any unwanted value, select it in the list and then select the **Remove** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif).
     6. To make a value the default selected value for the parameter, select it from the list.
   * **For Bind with Single Column**  
     Logi Report provides a mechanism that links each value of the display field with the exact value of the bound field for a parameter, thus when you select a value of the display field, Logi Report actually sends the value of the bound field to the query and filters the query result. This can help you bind the parameter to a data field in order to provide a list of values for report users to select which probably makes more sense. Logi Report uses the selected value of the bound field as the parameter value. For example, it might be confusing if you provide a list of customer ID numbers for the report users to select at runtime, since the ID numbers would probably mean nothing to them. In cases like this, it is better for you to display values of other fields, which would make more sense. For this case, you might prefer to display customer names instead of ID numbers. When the report user selects a customer name from the list, Logi Report passes its ID number to the query as the parameter value so that the search criteria can be fulfilled.
     1. From the **Source** drop-down list, select the required business view in the current data source from which to get data for the parameter. All the group and detail objects in the specified business view will be available for retrieving values for the parameter.
     2. Select a field from the **Bind Column** drop-down list, to filter the query when running a report with the parameter.
     3. If you want the values of another field to display for the report users to choose from, select that field from the **Display Column** drop-down list.
   * **For Bind with Cascading Columns:**
     1. From the **Data Source** drop-down list, select the required business view in the current data source from which to get data for the parameter. All the group and detail objects in the specified business view will be available for retrieving values for the parameter.
     2. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404880163351/btn_add1.gif) to add a parameter row.
     3. Select the arrow button ![Drop-down button](https://devnet.logianalytics.com/hc/article_attachments/4404880195479/btn_dropdown.gif) in the Bind Column cell and then select a field from the drop-down list.
     4. If you want the values of another field to display for the report users to choose from, select the arrow button ![Drop-down button](https://devnet.logianalytics.com/hc/article_attachments/4404880195479/btn_dropdown.gif) in the **Display Column** cell and select that field from the drop-down list.
     5. Select in the **Parameter** cell to create the parameter. Logi Report automatically adds a name for the parameter.
     6. Repeat steps b to e to create more parameters. Make sure that the selected Bind Column fields are of cascading relationship one level by one level down. In this way, you can create a group of cascading parameters.
     7. To adjust the order of the parameters, select the **Up** button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif) or the **Down** button![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif).
     8. To remove any unwanted parameter from the cascading group, select it and then select the **Remove** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404885309335/btn_delete.gif).
5. In the **Options** box, set [options](https://devnet.logianalytics.com/hc/en-us/articles/1500009774861-Add-Parameter-Dialog-Box-Properties#Options) for the parameter according to your requirements.
6. When done, select **OK** to create the parameter. Server adds the parameter to the **Local Parameters** node in the Parameters list.
7. To further edit the parameter, right-click it in the list and select **Edit** from the shortcut menu. Then in the [Edit Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009775201-Edit-Parameter-Dialog-Box-Properties) dialog box, edit the parameter as required.
8. To remove the parameter, right-click it in the list and select **Delete** on the shortcut menu.
9. Finish defining the filter condition using the parameter.
10. Select **OK** to apply the settings. Server lists the parameter in the [Parameters panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009750162-Applying-Parameters-to-Web-Report). You can specify the parameter value in the panel to dynamically set the filter condition.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* You can only use JDK (not JRE) to compile formulas and user defined functions that you created in Web Report Studio and save them with no errors into a web report.
* Currently, you cannot use global variables in dynamic formulas and user defined functions.
* If you refer to any field in a formula or user defined function, add a prefix @ before the reference name for that field. If the field name contains spaces, quote the reference name with double-quotation marks (""). For example, if the field name is **Customer Name**, then the reference name will be **@"Customer Name"**.
* When formulas and user defined functions reference display names or mapping names, the names should not contain any of the following characters if you do not quote the names by double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression **@Customer#;** will cause a syntax error. But **@"Customer#"** is OK.
  + If a field has the display name Category.Aggregation, quote it as "Category.Aggregation" or "Category"."Aggregation".

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778801-Adding-Links-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778781-Going-Through-Web-Report-Data)
