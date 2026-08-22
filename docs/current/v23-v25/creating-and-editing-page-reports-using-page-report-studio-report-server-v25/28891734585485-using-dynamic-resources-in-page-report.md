---
title: "Using Dynamic Resources in Page Report"
id: 28891734585485
section: "Creating and Editing Page Reports Using Page Report Studio Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891734585485-Using-Dynamic-Resources-in-Page-Report
updated_at: 2026-02-26T02:13:38Z
source_host: docs-report.zendesk.com
---
# 
Using Dynamic Resources in Page Report 

When the view elements in a business view cannot meet your requirements, you can create dynamic resources including dynamic formulas, dynamic aggregations, and crosstab formulas, and use them in a report to get the data you want. This topic describes how you can create and use dynamic resources in page reports.

When you save a report, Server saves the dynamic resources along with the report as its resources.

Dynamic resources are report tab level resources. They are only available to the report tab for which you created them.

In addition, when there are changes in a business view, Server administrators can recompile the dynamic resources in reports that use the business view as the data source so that the dynamic resources can work normally.

You need a Report Live license for Server to use this feature. For more product information, including new purchases and upgrades, contact US Sales or UK Sales.
    

This topic contains the following sections:

- 
                    Creating and Using Dynamic Formulas
                

- 
                        Using User Defined Functions
                    

- 
                    Creating and Using Dynamic Aggregation Objects

- Creating and Using Crosstab Formulas 
                

## 
Creating and Using Dynamic Formulas

You should have some knowledge of the formula syntax before you can successfully compose a formula without errors. To learn about the syntax, see Formula Syntax in the Report Designer Guide.

To create a dynamic formula:

- In the Resource View panel, expand the Dynamic Resources > Formulas node, then select <Add Formula…>. Server displays the Formula Editor.
    

- Type a name for the formula in Formula Name text box.

- By default, Server will decide whether the formula can be used as an aggregation object, and if not, the formula will be used as a detail object. You can specify to use the formula as a detail, group, or an aggregation object, by selecting the corresponding view element type from the Use As drop-down list on the toolbar.
    Whether you can use a dynamic formula as a certain type depends on the following rules: 

- You can use any formula as Detail.

- You can use any formula that references a DBField excluding an aggregation as Group. 

- You can use a formula that refers only to aggregations as Aggregation. For example, there are two aggregations Sum_Total and Sum_Quantity, and you can create a formula @"Sum_Total" / @"Sum_Quantity" and use it as an aggregation. 

- You can use a formula that follows the custom aggregation expression as Aggregation. For more information, see Custom Aggregation in the Report Designer Guide.

- Compose the formula by selecting the required fields, functions including built-in functions and user defined functions, and operators from the Fields, Functions, and Operators boxes, respectively. You can also write the formula by yourself in the editing box.
			For more information about the built-in functions and operators Page Report Studio supports, see Appendix 1: Formula Functions and Appendix 2: Formula Operators in the Report Designer Guide.

- Select the Check button  to check whether the syntax of your formula is correct.

- Select the OK button to create the formula.

Once a dynamic formula is created, you can then drag it from the Resource View panel to the position you want in the report for data analyzing. The formulas can also be used to control object properties if you are an advanced user and provided that the Use Dynamic Formula in Property is selected on the Report menu.

If you want to further edit an existing dynamic formula, remove any that is not required, or change the formula type as Group, Detail, or Aggregation if possible, right-click the formula and then select the corresponding command on the shortcut menu. Dynamic formulas that have been used in the report cannot be deleted.

### 
Using User Defined Functions

When you create dynamic formulas to use in a report, if the built-in functions do not satisfy your requirements, you can make use of the User Defined Function feature to create any functions as you want. Then when you save the report tab, the functions will be saved into the report tab as its resources the same as dynamic formulas. User defined functions can also call other user defined functions.

To create a user defined function:

- In the Resource View panel, navigate to Dynamic Resources > User Defined Functions, then select <Add Function…>. Server displays the User Defined Function Editor.

- Type a name for the function in the Function Name text box.

- Compose the function by double-clicking the required fields, functions including built-in functions and other user defined functions, and operators from the Fields, Functions, and Operators boxes respectively. You can also write the function by yourself in the editing box.
    The function syntax is:

arguments: VariableType1 VariableName1, VariableType2 VariableName2, ...;

For example, arguments: integer age, string name;

An argument works the same as a local variable except that you cannot assign any value to it, like arguments: integer age=10;.

- Select the Check button  to check whether the syntax of your function is correct.

- Select OK to create the function.
    The function is then available under the User Defined Functions node in the Functions box of the Formula Editor, Crosstab Formula Editor, and User Defined Function Editor. You can call it in a dynamic formula, a crosstab formula, or another user defined function by double-clicking it. 

Suppose a user defined function named function1 is arguments: integer age, string name;, you can call it as follows:

- @function1(25, "John Smith");

- @'function1'(25, "John Smith");

- @"function1"(25, "John Smith");

If you want to further edit or remove an existing user defined function, right-click the function in the Resource View panel, and then select the corresponding command on the shortcut menu. You cannot delete user defined functions when you have used them in the report.

## 
Creating and Using Dynamic Aggregation Objects 

In Page Report Studio, you can also create dynamic aggregation objects by mapping them to the available resources which include group objects, detail objects in the current business view, and the dynamic formulas that you have created in the report.

To create a dynamic aggregation object:

- In the Resource View panel, navigate to Dynamic Resources > Aggregations, then select <Add Aggregation…>. Server displays the Add Aggregation dialog box.
    

- In the Aggregation Name text box, specify the display name of the aggregation object.

- Select the ellipsis button  next to the Mapping Name text box. Server displays the  Select Source dialog box.

-  Specify a field or a formula on which the aggregation object is based.
    

- Select OK.
            

- From the Aggregate Function drop-down list, specify the aggregate function for the aggregation object. When you selected DistinctSum, you should select the ellipsis button  next to the Distinct On text box. Server displays the Select Fields dialog box.
Select one or more group and detail objects according to whose unique values you want to calculate DistinctSum.
   For the usage about each function, refer to Aggregate Functions in the Report Designer Guide.

- Select OK to create the aggregation object.

You can also create a dynamic aggregation object on a dynamic formula. To do this:

- In the Resource View panel, right-click the formula in the Dynamic Resources > Formulas node, then select Add Aggregation from the shortcut menu.

- In the Add Aggregation dialog box, specify the display name of the aggregation object and the aggregate function.

- Select OK.

Once you create a dynamic aggregation object, you can then drag it from the Resource View panel to the position you want in the report for data analyzing.

You can further modify any dynamic aggregation object. To do this, right-click the aggregation object and select Edit from the shortcut menu. Then in the Edit Aggregation dialog box, edit the aggregation object. 

 For dynamic aggregation objects that you don't need, you can remove them. To delete an aggregation object, right-click it and select Delete on the shortcut menu. You cannot remove aggregation objects when you have used them in the report.

- You can only use JDK (not JRE) to compile formulas and user defined functions created in Page Report Studio and save them with no errors into a report.

- Currently, you cannot use global variables in dynamic formulas and user defined functions.

- If you refer to any field in a formula or user defined function, you should add a prefix @ before the reference name for that field. If the field name contains spaces, quote the reference name with double-quotation marks (""). For example, if the field name is Customer Name, then the reference name will be @"Customer Name".

- When formulas and user defined functions reference display names or mapping names, the names should not contain any of the following characters if you do not quote the names by double-quotation marks "":
      "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

Examples: 
      

- Expression @Customer#; will cause a syntax error. But @"Customer#" is ok. 

- If a field has the display name Category.Measure, quote it as "Category.Measure" or "Category"."Measure".

## 
Creating and Using Crosstab Formulas

Crosstab formulas are a type of extended formulas. You can insert crosstab formulas into crosstabs as aggregations and use them to control the property values of crosstab fields. Crosstab formulas are private resources on the crosstab level, which you cannot use beyond their crosstabs.

To support more powerful and flexible calculation logic in crosstabs, crosstab formula extends the basic Formula Syntax in the following aspects: 

- A crosstab formula can reference another crosstab formula within the same crosstab. The format is @@<Crosstab_Formula_Name>, for example, @@CTF1, where CTF1 is the name of a crosstab formula. In this case, you can write the crosstab formula expression as @(@@CTF1).

- A crosstab formula can reference summary expression that follows the syntax of custom aggregation expression. For example,    @(Sum(@Sales))
@(@Country:"USA",@Year:CHILDREN, Sum(@Sales))
@(@Country:"USA",@Year:CHILDREN, @@CTF1)

For more information, see Custom Aggregation in the Report Designer Guide.

- You cannot use global variables in crosstab formulas.

- You cannot reference detail fields and record level pass one formulas in crosstab formulas, except for referencing them in summary expression. 

- You cannot use the Array functions as array_function (field_variable, groupby) in crosstab formulas (array_function here refers to any Array function defined in Report). For example, Report does not allow Maximum(@dbfield, "group_field") and Average(@formula, @parameter) in crosstab formulas. 

To create a crosstab formula:

- In the Resource View panel of Page Report Studio, navigate to Dynamic Resources > Crosstab Formulas. Then, select <Add Crosstab Formula…>, or right-click a crosstab  formula and select Edit from the shortcut menu.
Server displays the Crosstab Formula Editor.

- Type a name for the crosstab formula in the Formula Name text box.

- Compose the formula by selecting the required fields, functions including built-in functions, user defined functions, and crosstab formulas, and operators from the Fields, Functions, and Operators boxes respectively. You can also write the formula by yourself in the editing box.
			For more information, see Appendix 1: Formula Functions and Appendix 2: Formula Operators in the Report Designer Guide.

- To insert an operator into your formula, you can also select the Add Operators button  and then select an operator.

- To insert the HEX code of a color into your formula, select the Color Converter button , and then select a color in the Select Color dialog box.

- Select the Check button  to check whether the syntax of your formula is correct.

- Select OK to create the crosstab formula.

Once you create the crosstab formula, you can then add it in the crosstab as an aggregation, use it to control property values of the fields in the crosstab in a dialog box, and use it to perform conditional formatting on the fields in the crosstab. 

If you want to further edit or remove an existing crosstab formula, right-click it in the Resource View panel of Page Report Studio and then select the corresponding command on the shortcut menu. You cannot edit or remove crosstab formulas when you have used them in the report.
