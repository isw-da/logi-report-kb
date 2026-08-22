---
title: "Using Dynamic Resources and Local Parameters in a Report"
id: 45190686667149
section: "Designing Your Reports - Report Designer"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45190686667149-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report
updated_at: 2026-04-30T15:16:08Z
source_host: logi-report-v26.insightsoftware.com
---
# Using Dynamic Resources and Local Parameters in a Report

When working with a business view-based report, sometimes you may find the predefined view elements in the business views the report applies, or the predefined parameters in the current catalog cannot meet your requirements. In this case, you can create dynamic resources, including dynamic formulas, dynamic aggregations, and crosstab formulas, and local parameters and use them in the report to get the data you need. When you save the report, Designer saves the dynamic resources and local parameters as resources of the report in the report file. This topic describes how you can create and use dynamic resources and local parameters in a report.

 Dynamic resources and local parameters are report level resources, meaning, they are only available to the report for which you create them. Unless you need to use the formulas, aggregations, or parameters in multiple reports, you should create dynamic resources and local parameters rather than create them in the catalog.

This topic contains the following sections:

- 
Creating and Using Dynamic Formulas- Using User-Defined Functions in Dynamic Formulas

- Creating and Using Dynamic Aggregations

- Creating and Using Crosstab Formulas

- Creating and Using Local Parameters

## 
Creating and Using Dynamic Formulas

To create a dynamic formula

- Do one of the following:
- In the Data panel of the main window, expand the Dynamic Resources > Formulas node and select <New Formula…>.

- In the component wizard or dialog box that contains a dynamic formula list, select <New Formula…>.

- In the value drop-down list for some object properties or dialog box options, select <New Formula…>.

- In the Enter Formula Name dialog box, specify the name of the formula and select OK. Designer displays the Formula Editor dialog box.
			

- Compose the formula by selecting the required fields from the Fields panel (including view elements in the current business view, parameters in the current catalog data source (global parameters), some special fields, and dynamic resources and local parameters in the current report), functions from the Functions panel (including built-in functions and user-defined functions), and operators from the Operators panel. You can also write the formula by yourself. You should have some knowledge of the formula syntax before you can successfully compose a formula with no errors.
  

- Specify how you want to use the formula, as a detail, group, or an aggregation object, by selecting the corresponding view element type from the Use As drop-down list on the toolbar. 
If you leave Use As empty (the default behavior), when you save the formula, Designer determines whether  the formula  can be used as an aggregation object; if it cannot, Designer applies it as a detail object. 
- You can use any formula as Detail.

- You can use a formula that references a DBField and does not reference an aggregation as Group. 

- You can use a formula that only references aggregations  as Aggregation. For example, there are two aggregations "Sum_Total" and "Sum_Quantity", and you can create a formula @"Sum_Total" / @"Sum_Quantity" and use it as an aggregation. 

- You can use a formula that follows the custom aggregation expression as Aggregation.

- Save the formula and close the editor. Designer adds the formula to the dynamic formula resource tree.

Once you have created a dynamic formula in a report, you can then drag it from the Data panel to insert it in the report, add it as report field when working with the component wizard, or use it to control property or option values.

In the Data panel, you can use the shortcut menu of any existing dynamic formula to edit or delete the formula, or change the formula type as Group, Detail, or Aggregation. You cannot delete dynamic formulas that you have used in the report.

### 
Using User-Defined Functions in Dynamic Formulas 

Using Report's User-Defined Formula Function feature, you can create any functions as you want and apply them in your formulas. However, if you want to use user-defined functions in dynamic formulas, you need to create them specifically for the current report via the dynamic resource list.

To create a user-defined function for a report

- In the Data panel of the main window, expand the Dynamic Resources > User Defined Functions node and select <New Function…>, or in the component wizard or dialog box that contains a dynamic resource list, select <New Function…>.

- In the displayed dialog box, specify the name of the function and select OK.

- In the User Defined Function Editor dialog box, create the function according to your requirement.

- Save the function. The function is then available under the User Defined Functions node in the Functions panel of the Formula Editor and User Defined Function Editor. You can then call it in a dynamic formula or another user-defined function by double-clicking it.

In the case a user-defined function named "function1" is arguments: integer age, string name;, you can call it as follows:

- @function1(25, "John Smith");

- @'function1'(25, "John Smith");

- @"function1"(25, "John Smith");

If you want to further edit an existing user-defined function or remove any that you do not need, right-click the function in the Data panel of the main window and then select the corresponding command on the shortcut menu. You cannot delete functions that you have used in the report.

- You can only use JDK (not JRE) to compile dynamic formulas created in Report.

- When you refer to any field in a formula, you need to add the "@" symbol as the prefix of the field's reference name. If the field name contains spaces, you need to quote the reference name with double quotation marks (""). For example, if the field name is Customer Name, the reference name is @"Customer Name".

- 
Report limits the number of the "if-else" statements to 190. When this number is reached, you should use the "select-case" statement instead.

- You cannot use global variables in dynamic formulas and user-defined functions.

- When dynamic formulas and user-defined functions reference display names or mapping names, the names should not contain any of the following characters if you do not quote the names  with the double-quotation marks (""):
					"~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

Examples: 
				

- Expression @Customer#; causes a syntax error, but @"Customer#" is ok. 

- If a field has the display name Category.Measure, when you add it to a formula, you should quote it as 
 "Category.Measure" or "Category"."Measure".

 

## 
Creating and Using Dynamic Aggregations

To creating a dynamic aggregation

- In the Data panel of the main window, or in the Resources box of the component wizard, expand the Dynamic Resources > Aggregations node, then select <New Aggregation…>. Designer displays the New Aggregation dialog box.
			

- In the Aggregation Name text box, specify the name of the dynamic aggregation.

- Select the ellipsis to specify the field on which the dynamic aggregation is based. You can map dynamic aggregations to the available resources such as group objects and detail objects in the current business view, or the dynamic formulas that you have created in the report.	

- From the Aggregate Function drop-down list, select the function to calculate the mapping field. If you select DistinctSum, you should select the ellipsis next  to the Distinct On text box to specify one or more fields according to whose unique values to calculate DistinctSum using the Select Fields dialog box.

- Select OK to create the dynamic aggregation.

Once you have created a dynamic aggregation in a report, you can then drag it from the Data panel to  insert it in the report, or add it as report field when working with the component wizard.

In the Data panel, you can use the shortcut menu of any existing dynamic aggregation to edit it in the Edit Aggregation dialog box or delete it. You cannot delete dynamic aggregations that you have used in the report.

 

## 
Creating and Using Crosstab Formulas

You can use crosstab formulas to apply custom aggregate functions in a business view-based crosstab, and control the properties of objects in the crosstab. See  Using Crosstab Formulas.

 

## 
Creating and Using Local Parameters 

- Select <New Parameter…> in the Local Parameters node in one of the following cases:
- In the Data panel of the main window when working with a business view-based report.

- In the Fields panel of the Formula Editor dialog box when creating or editing a dynamic formula.

- When specifying the value of a filter condition for a business view-based dataset.

- In the New Parameter dialog box, create the parameter according to your requirement.

- Select OK to create the parameter.

Once you have created a local parameter in a report, you can then use it to dynamically filter data components in the report, add it to  parameter controls or parameter form controls in the report, or reference it in dynamic record level pass one formulas in the report.

In the Data panel, you can also use the shortcut menu of any existing local parameter to edit or delete it. You cannot delete local parameters that you have used in the report.
