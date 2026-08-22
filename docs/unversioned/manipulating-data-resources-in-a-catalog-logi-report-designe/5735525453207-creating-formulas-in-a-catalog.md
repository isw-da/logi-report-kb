---
title: "Creating Formulas in a Catalog"
id: 5735525453207
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735525453207-Creating-Formulas-in-a-Catalog
updated_at: 2022-11-02T07:57:59Z
---

# Creating Formulas in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532056855-Formula-Syntax)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions)

# Creating Formulas in a Catalog

This topic describes how you can create formulas in a catalog, reference parameters and special fields in formulas, and use DBArray in formulas. It also provides some formula examples for your reference.

In addition to creating formulas in the catalog, you can create [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Formula) to use in a business-based report specifically and use [crosstab formulas](https://devnet.logianalytics.com/hc/en-us/articles/5735520960151-Using-Crosstab-Formulas) to apply custom aggregate functions in a crosstab.

This topic contains the following sections:

* [Predefining Formulas in a Catalog](#Predefine)
* [Creating Formulas in a Catalog on Demand](#Create)
* [Referencing Parameters in Formulas](#RefParam)
* [Referencing Special Fields in Formulas](#RefSpecial)
* [Using DBArray in Formulas](#DBArray)
* [Formula Examples](#Example)

See also [Formula Fields](https://devnet.logianalytics.com/hc/en-us/articles/5735507254295-Working-with-Formula-Fields) for how to work with formulas as component in a report.

## Predefining Formulas in a Catalog

You can predefine formulas in a catalog, so you can use them directly when designing reports.

1. [Open the catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, expand the data source to create the formula, then do either of the following:
   * Select the **Formulas** node or any existing formula in the data source and select **New Formula** on the Catalog Manager toolbar.
   * Right-click the **Formulas** node in the data source and select **New Formula** on the shortcut menu.
3. In the Enter Formula Name dialog box, provide a name for the formula and select **OK**. Designer displays the [Formula Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565964055-Formula-Editor-Dialog-Box).

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/9898459791639/fmlaedtr.gif)
4. Compose the formula by selecting the required fields from the **Fields** panel (including DBFields, other formulas, [summaries](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Predefine), and [parameters](#RefParam) in the current catalog data source, and [some special fields](#RefSpecial)), functions from the **Functions** panel (including [built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions) and [user-defined functions)](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions), and [operators](https://devnet.logianalytics.com/hc/en-us/articles/5735511732247-Appendix-2-Formula-Operators) from the **Operators** panel. You can also write the formula by yourself. When the predefined formulas, summaries, and parameters cannot meet you requirement, you can create new formula, [summary](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries#Predefine), and [parameter](https://devnet.logianalytics.com/hc/en-us/articles/5735516481047-Creating-Parameters-in-a-Catalog) using the New XXX option on the toolbar. Designer saves the newly created objects into the same catalog data source as the formula. You should have some knowledge of the [formula syntax](https://devnet.logianalytics.com/hc/en-us/articles/5735532056855-Formula-Syntax) before you can successfully compose a formula with no errors.
5. Save the formula and close the editor. Designer adds the formula in the catalog resource tree.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* When you refer to any field in a formula, you need to add the "@" symbol as the prefix of the field's reference name. If the field name contains spaces, you need to quote the reference name with double quotation marks (""). For example, if the field name is Customer Name, the reference name is @"Customer Name".
* When formulas reference display names or mapping names, the names should not contain any of the following characters if you do not quote the names using double quotation marks:

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression `@Customer#;` causes a syntax error, but `@"Customer#"` is correct.
  + If a field has the display name Category.Measure, when you add it to a formula, quote it as
    "Category.Measure" or "Category"."Measure".

## Creating Formulas in a Catalog on Demand

Besides predefining formulas in a catalog via the Catalog Manager, Designer also provides you quick access to create formulas from the UI where a formula list is available, for example, in the Resources box of the component wizard. In this formula list, you can find the option **<New Formula...>** on the top. Select the option and you can create a formula in the catalog and use it for the current scenario.

## Referencing Parameters in Formulas

A formula which references parameters returns values according to the parameter values. To reference a parameter in a formula, follow the syntax: *@ParameterName*.

Assume you have created a String type-in parameter, pCompany. You can reference it in a formula to display the URL for a company dynamically.

1. Create a formula in the Formula Editor dialog box.

   `"http://www." + @pCompany + ".com"`

   Here, you can either manually type **@pCompany**, or you can select it from the Parameters node in the Fields panel (if you choose this way, Designer adds the "@" symbol automatically).
2. Insert the formula into a report.
3. Select the **View** tab to preview the report and Designer prompts you to specify the parameter value.
4. Type the string **logianalytics** as the value for pCompany. You can then find that the value of the formula becomes **http://www.logianalytics.com**.

In the case when you need to display the value of a multivalued parameter, you can apply the built-in function [join()](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions#join). For example, the following expression can show a list of selected states separated by commas:

`"Selected States : " +  trim(join (@pStates,",")) + "\r\n"`

## Referencing Special Fields in Formulas

You can also reference some [special fields](https://devnet.logianalytics.com/hc/en-us/articles/5735564398999-Working-with-Special-Fields) in formulas in the format *fieldname*. These special fields include: User Name, Print Date, Print Time, Fetch Date, Fetch Time, Modified Date, Modified Time, Record Number, Page Number, Global Page Number, Total Records, and Total Fetched Records. All these special field have two types when you use them in formulas, page level and constant level, according to the time when their values are ready.

**Page level**

The value of this special field is ready at the time when Logi Report Engine generates the report. A formula that references a page level special field is a [page level formula](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#Page). Logi Report Engine calculates a page level formula more than once.

Page level special fields include: Fetch Date, Fetch Time, Print Date, Print Time, Record Number, Page Number, Global Page Number, Total Records, and Total Fetched Records.

**Constant level**

The value of this special field is ready at any time before Logi Report Engine runs. A formula that references a constant level special field is a constant level formula. Logi Report Engine calculates a constant level formula only once.

Constant level special fields include: User Name, Modified Date, and Modified Time.

## Using DBArray in Formulas

Designer supports a multivalued field in a formula, which contains a set of values in a single field. Using a multivalued field is the same as using an array in a formula. You can refer to a field with multiple values the same as with a normal field in a formula, such as *@FIELDNAME*, and then use the array functions that Logi Report provides to manipulate the values in it. Logi Report Engine first converts this field into a normal array, and then manipulates it in the usual way.

For example, normally you may define an array in a formula as follows:

`Integer myArray[4]=[1, 2, 3, 4]; //Datatype ArrayName[ArraySize]=[ArrayContent];`

And you may refer to the array in this way:

`integer myInt=3;  
 myInt in myArray;`

If a field, myField for example, contains a similar array value, you can refer to it similarly:

`integer myInt=3;  
 myInt in @myField;`

If you want to display all values of an array, you can use the [*join()*](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions#join)function to return a string of all the values.

## Formula Examples

**Example 1: TerritoryUSA**

In your sales report, you want to print out which territory the customer belongs to according to the abbreviated state names stored in the State field. You can write the formula as follows:

`if (@State in ["CT", "ME", "MA", "NH", "NY", "RI", "VT"]) {  
    "NorthEast, USA";}  
else if ( @State in ["DC", "DE", "MD", "NJ", "PA", "VA"]) {  
    "MidAtlantic, USA";}  
else if ( @State in ["CO", "ID", "KS", "MT", "NE", "NV", "NM", "ND", "SD", "UT"]) {  
    "Rockies, USA";}  
else if ( @State in ["AZ", "AR", "LA", "MO", "OK", "TX"]) {  
    "South, USA";}  
else if ( @State in ["AL", "FL", "GA", "MS", "NC", "SC"]) {  
    "SouthEast, USA";}  
else if ( @State in ["AK", "CA", "HI", "OR", "WA"]) {  
    "West, USA";}  
else if ( @State in ["IL", "IN", "LA", "KY", "MI", "MN", "OH", "TN", "WI", "WV", "WY"]) {  
    "MidWest, USA";}`

In the "else-if" statements, Logi Report Engine retrieves the value of the State field, and compares it with the values in brackets "[]". When a value matches the value in brackets, the formula returns the territory name.

**Example 2: DateToMonth**

In your sales report, you want to print out the month name of the orders, so that you can compare the orders of each month in a year. You can write the formula as follows:

`Number m = Month ( @"Order Date" ) ;  
String str = "";  
if ( m == 1 ) {  
    str = " January Sales";}  
else if ( m == 2 ) {  
    str = " February Sales";}  
else if ( m == 3 ) {  
    str = " March Sales";}  
else if( m == 4 ) {  
    str = " April Sales";}  
else if( m == 5 ) {  
    str = " May Sales";}  
else if ( m == 6 ) {  
    str = " June Sales";}  
else if ( m == 7 ) {  
    str = " July Sales";}  
else if( m == 8 ) {  
    str = " August Sales";}  
else if ( m == 9 ) {  
    str = " September Sales";}  
else if( m == 10 ) {  
    str = " October Sales";}  
else if ( m == 11 ) {  
    str = " November Sales";}  
else if ( m == 12 ) {  
    str = " December Sales";}`

Since the Order Date DBField is TimeStamp data type, Logi Report Engine first uses the built-in function *Month (DateTime)* to extract the month portion of Order Date. Then, it applies the "else-if" statement to decide the month according to the return value of the function, and assigns a String value which contains a relative month name to the predeclared string variable "str".

**Example 3: SectionInvisible**

When you set the Suppressed property of a panel such as Page Header to "true" in the Report Inspector, the panel is suppressed on every page. You can write a formula as follows to control the property, so that the panel is suppressed only on the first page of the report.

`boolean s;  
if (PageNumber==1){  
    s=true;}  
else {  
    s=false;}`

This formula first declares a Boolean type variable, then uses an "if-else" statement to determine whether the page is the first page. If the statement is true, it assigns "true" to "s"; otherwise, it assigns "false" to "s". In this formula, [PageNumber](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#Page) is a special field.

**Example 4: Running total of page**

You can use the running total function to calculate the sum of one page. However, in order to use the running total function, you have to create a set of formulas.

1. Create a formula as follows to initialize a global variable as the sum variable. Insert the formula into the banded page header panel. The reference to [PageNumber](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels#Page) forces the calculation to run after the page break.

   `PageNumber;  
   global number pagetotal;  
   pagetotal=0;`
2. Create another formula to accumulate the value. Insert it into the detail panel.

   `pagetotal=pagetotal+@"YTD Sales";`
3. Create one more formula to display the sum of one page. Insert it into the banded page footer panel.

   `return pagetotal;`

**Example 5: Running total of group**

This example accumulates the total of the successful and failed shipments for each group.

1. Create a formula as follows to initialize the value. Insert the formula into the group header panel.

   `global integer iFail;  
   global integer iSuccess;  
   iFail=0;  
   iSuccess=0;`
2. Create another formula to accumulate the value of the successful and failed shipments. Insert it into the detail panel.

   `if(@Shipped) {  
       iSuccess=iSuccess+1;  
       iFail=iFail;   
   }  
   else {  
       iSuccess=iSuccess;   
       iFail=iFail+1;  
   }`
3. Create one more formula to return the successful shipments and the failed shipments. Insert it into the group footer panel.

   `return "Total successful shipments is "+ iSuccess +" and total failed shipments is "+ iFail;`

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)Logi Report does not support global variables in dynamic formulas, so an alternate way to do this is using two formulas, fShipped and fNotShipped, to return either 1 or 0 based on Shipped.

`if(@Shipped) return 1 else return 0;  
 if(@Shipped) return 0 else return 1;`

You can then add [dynamic aggregations](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Agg) to sum on fShipped and fNotShipped. The result is the same as using the global variables.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735532056855-Formula-Syntax)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735545091095-Using-User-Defined-Formula-Functions)
