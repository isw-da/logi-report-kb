---
title: "Creating Formulas in a Catalog"
id: 1500010068541
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068541-Creating-Formulas-in-a-Catalog
updated_at: 2021-07-24T10:38:14Z
---

# Creating Formulas in a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033222-Formula-Syntax) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions)

# Creating Formulas in a Catalog

This section introduces creating formulas in a catalog. In a report that uses business view as the data source, you can also create [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010070961-Using-Dynamic-Resources-and-Local-Parameters-in-Reports#Formula) to use in the report specifically.

Below is a list of the sections covered in this topic:

* [Predefining Formulas in a Catalog](#Predefine)
* [Creating Formulas in a Catalog When Needed](#Create)
* [Referencing Parameters in Formulas](#RefParam)
* [Referencing Special Fields in Formulas](#RefSpecial)
* [Using DBArray in Formulas](#DBArray)
* [Formula Examples](#Example)

See also [Formula Fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010063801-Formula-Fields) for how to work with formulas as component in a report.

## Predefining Formulas in a Catalog

You can predefine formulas in a catalog so as to use them directly in reports.

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010063141-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, expand the data source in which to create the formula, then:
   * Select the **Formulas** node or any existing formula in the data source and select **New Formula** on the Catalog Manager toolbar.
   * Right-click the **Formulas** node in the data source and select **New Formula** on the shortcut menu.
3. In the Enter Formula Name dialog, provide a name for the formula and select **OK**. The [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010066181-Formula-Editor-Dialog) appears.

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901162647/fmlaedtr.gif)
4. Compose the formula by selecting the required fields from the Fields panel (including DBFields, other formulas, summaries and [parameters](#RefParam) in the current catalog data source and [some special fields](#RefSpecial)), functions from the Functions panel (including [the built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010028442-Appendix-1-Formula-Functions) and [user defined functions)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions), and [operators](https://devnet.logianalytics.com/hc/en-us/articles/1500010063101-Appendix-2-Formula-Operators) from the Operators panel. When the predefined formulas, summaries and parameters cannot meet you requirement, you can create new formula, [summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010068581-Summaries#Predefine) and [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010069001-Creating-Parameters-in-a-Catalog) to be referenced by the formula using the New XXX option on the toolbar. The newly created objects are saved into the same catalog data source as the formula. You can also write the formula by yourself in the editing panel. You should have some knowledge of the [formula syntax](https://devnet.logianalytics.com/hc/en-us/articles/1500010033222-Formula-Syntax) before you can successfully compose a formula with no errors.
5. Make use of the buttons on the toolbar above the editing panel to edit the formula. To comment a line, select the **Comment/Uncomment** button ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404901161367/btn_cmtuncmnt.gif) on the toolbar. If you want to bookmark a line so that it can be searched easily later, select the **Add Bookmark** button ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404909145879/btn_bkmrk.gif). To check whether or not the syntax of your formula is correct, select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404901161623/btn_check.gif).
6. Select **OK** to add the formula.

**Notes:**

* If you refer to any field in the formula, the reference name for that field will be prefixed with an @ sign. If the field name contains spaces, the reference name in formula will be quoted with double-quotation marks (""). For example, if the field name is Customer Name, then the reference name will be @"Customer Name".
* When formulas reference display names or mapping names, the names should not contain any of following characters if the names are not quoted by double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression `@Customer#;` will cause a syntax error. But `@"Customer#"` is ok.
  + If a field has the display name Category.Measure, when adding it to a formula, quote it as
    "Category.Measure" or "Category"."Measure".
* The number of the "if-else" statements in a formula is limited to 190. When this number is reached, you should use the "select-case" statement instead.

## Creating Formulas in a Catalog When Needed

Besides predefining formulas in a catalog via the Catalog Manager, Logi JReport Designer also provides you quick access to create formulas in a catalog from the UI where a formula list is available, for example in the Resources box of the component wizard. In this formula list, the <New Formula...> item is provided on the top. By selecting the item, you can create any formulas you want with the Formula Editor, which are then added into the current catalog.

## Referencing Parameters in Formulas

A formula which references parameters will return values according to the parameter values. To reference a parameter in a formula, follow the syntax: *@ParameterName*.

Assume there is a type-in parameter pCompany of String type, you can reference it in a formula to display the URL for a company dynamically.

1. Create a formula named CompanyURL in the Formula Editor as follows:

   `"http://www." + @pCompany + ".com"`

   Here, you can either manually type @pCompany, or you can select it from the Parameters node in the Fields panel (if you choose this way, the @ sign will be automatically inserted).
2. Insert the formula into a report.
3. View the report result, and type the string **Jinfonet** when prompted to enter the parameter value for pCompany. You will then find that the value of the formula becomes http://www.jinfonet.com.

There may be times you need to display the value of a multi-valued parameter. The built-in function [join()](https://devnet.logianalytics.com/hc/en-us/articles/1500010028442-Appendix-1-Formula-Functions#join) assists with that. For example, the following expression will show a list of selected states separated by commas:

`"Selected States : " +  trim(join (@pStates,",")) + "\r\n"`

## Referencing Special Fields in Formulas

You can also reference some [special fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010029242-Special-Fields) in formulas in the format *fieldname*. These special fields include: User Name, Print Date, Print Time, Fetch Date, Fetch Time, Modified Date, Modified Time, Record Number, Page Number, Global Page Number, Total Records and Total Fetched Records. They can all be divided into two types (page level and constant level) according to the time when their values are ready.

**Page level**

The value of this special field is ready at the time when the report result is generated. A formula which references a page-level special field is treated as a page-level formula. In which, the formula is calculated more than once.

The special fields of this type are: Fetch Date, Fetch Time, Print Date, Print Time, Record Number, Page Number, Global Page Number, Total Records and Total Fetched Records.

**Constant level**

The value of this special field is ready at any time before the engine runs. A formula which references a constant-level special field is treated as a constant-level formula, and is calculated only once.

The special fields of this type are: User Name, Modified Date and Modified Time.

## Using DBArray in Formulas

Logi JReport Designer supports a multiple-value field, which contains a set of values in a single field, in a formula. Using the multiple value field is the same as using an array in a formula. You can refer to a field with multiple values as with a normal field in a formula, such as @FIELDNAME, and then use the array functions that Logi JReport Designer provides in the Formula Editor to manipulate the values in it. Logi JReport Designer first converts this field into a normal array, and then manipulates it in the usual way.

For example, normally an array in a formula is manually defined as follows:

`Integer myArray[4]=[1, 2, 3, 4]; //Datatype ArrayName[ArraySize]=[ArrayContent];`

The array may be referred to in this way:

`integer myInt=3;  
 myInt in myArray;`

If a field, named myField for example, contains a similar array value, it can be referred to similarly:

`integer myInt=3;  
 myInt in @myField;`

If you want to display all the values of an array, you can use the [join()](https://devnet.logianalytics.com/hc/en-us/articles/1500010028442-Appendix-1-Formula-Functions#join) function to return a string of all the values.

## Formula Examples

**Example 1: TerritoryUSA**

In your sales report, you want Logi JReport to print out which territory the customer belongs to according to the abbreviated state names stored in the State field. You can write the formula as follows:

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

In the six else-if statements, Logi JReport will retrieve the value of the State field, and compare it with the values in brackets []. If a value matches the value in brackets, the formula will return the territory name.

**Example 2: DateToMonth**

In your sales report, you want Logi JReport to print out the month name of the orders, so that you can compare the orders of each month in a year. You can write the formula as follows:

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

Since the database field Order Date is of the TimeStamp data type, the built-in function Month (DateTime) is first used to extract the month portion of Order Date. Then, the else-if statement is used to decide the month according to the return value of the function, and assigns a String value which contains a relative month name to the pre-declared string variable str.

**Example 3: SectionInvisible**

You can write a formula as follows to control the Suppressed property of a certain section such as Page Header, so that the section will be suppressed on the first page of the report.

`boolean s;  
if (pagenumber==1){  
    s=true;}  
else {  
    s=false;}`

Since it is only required to suppress the section on the first page, if only the Suppressed property of the section is set to true in the Report Inspector, then it will be suppressed on every page. In this formula, a Boolean type variable is first declared. Then, an else-if statement is used to decide whether or not the page is the first page. If the statement is true, true is assigned to "s". If the statement is false, false is assigned false to "s". In this formula, pagenumber is a special field.

**Example 4: Running total of page**

You can use the running total function to calculate the sum of one page. And to use the running total function, you have to create a set of formulas.

1. Create a formula named Formula1 as follows to initialize a global variable as the sum variable. And insert it into the Banded Page Header panel. The reference to PageNumber forces the calculation to run after the page break. For more information, see [Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/1500010068561-Formula-Levels).

   `pagenumber;  
   global number pagetotal;  
   pagetotal=0;`
2. Create a formula named Formula2 as follows to accumulate the value. And insert it into the Detail panel.

   `pagetotal=pagetotal+@"YTD Sales";`
3. Create a formula named Formula3 as follows to display the sum of one page. And insert it into the Banded Page Footer panel.

   `return pagetotal;`

**Example 5: Running total of group**

This example will accumulate the total of the successful and failed shipments for each group.

1. Create a formula named Formula1 as follows to initialize the value. And insert it into the group header.

   `global integer iFail;  
   global integer iSuccess;  
   iFail=0;  
   iSuccess=0;`
2. Create a formula named Formula2 as follows to accumulate the value of the successful and failed shipments, and insert it into the Detail panel.

   `if(@Shipped) {  
       iSuccess=iSuccess+1;  
       iFail=iFail;   
   }  
   else {  
       iSuccess=iSuccess;   
       iFail=iFail+1;  
   }`
3. Create a formula named Formula3 as follows to return the successful shipments and the failed shipments, and insert it into the group footer.

   `return "Total successful shipments is "+ iSuccess +" and total failed shipments is "+ iFail;`

**Note:**  Global variables are not supported in dynamic formulas so an alternate way to do this is using two formulas (fShipped and fNotShipped) to return either 1 or 0 based on @Shipped:

`if(@Shipped) return 1 else return 0;  
 if(@Shipped) return 0 else return 1;`

Then add dynamic aggregations to sum on fShipped and fNotShipped. The result will be the same as using the global variables.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033222-Formula-Syntax) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033242-User-Defined-Formula-Functions)
