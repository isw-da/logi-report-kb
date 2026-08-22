---
title: "Creating a Formula"
id: 1500009589661
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula
updated_at: 2021-07-24T05:54:36Z
---

# Creating a Formula

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589721-User-Defined-Formula-Functions)

# Creating a Formula

To create a formula in a catalog, follow the steps below:

1. [Open the requied catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog).
2. In the Catalog Manager, expand the data source in which to create the formula, then:
   * Select the **Formulas** node or any existing formula in the data source and select **New Formula** on the Catalog Manager toolbar.
   * Right-click the **Formulas** node in the data source and select **New Formulas** on the shortcut menu.
3. In the Enter Formula Name dialog, provide a name for the formula and select **OK**. The [Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009586941-Formula-Editor-Dialog) appears.

   ![Formula Editor](https://devnet.logianalytics.com/hc/article_attachments/4404889308567/fmlaedtr.gif)
4. Compose the formula by selecting the required fields, including DBFields, other formulas, summaries and [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009590221-Referencing-Parameters-in-a-Formula) in the current catalog data source and some [special fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009584241-Special-Fields#Ref) from the Fields panel, and [functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009568182-Built-in-Functions) and [operators](https://devnet.logianalytics.com/hc/en-us/articles/1500009589581-Operators) from the Functions and Operators panels. When the predefined formulas, summaries and parameters cannot meet you requirement, you can create new formula, [summary](https://devnet.logianalytics.com/hc/en-us/articles/1500009589741-Creating-a-Summary) and [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter) to be referenced by the formula using the New XXX option on the toolbar. The newly created objects are saved into the same catalog data source as the formula. You can also write the formula by yourself in the editing panel.
   You should have some knowledge of the [formula syntax](https://devnet.logianalytics.com/hc/en-us/articles/1500009568322-Formula-Syntax) before you can successfully compose a formula with no errors.

   Make use of the buttons on the toolbar above the editing panel to edit the formula. To comment a line, select the **Comment/Uncomment** button ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404893837975/btn_cmtuncmnt.gif) on the toolbar. If you want to bookmark a line so that it can be searched easily later, select the **Add Bookmark** button ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404893838231/btn_bkmrk.gif). To check whether or not the syntax of your formula is correct, select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404893838487/btn_check.gif).
5. When done, select the **OK** button to add the formula.

**Notes:**

* If you refer to any field in the formula, the reference name for that field will be prefixed with an @ sign. If the field name contains spaces, the reference name in formula will be quoted with double-quotation marks (""). For example, if the field name is Customer Name, then the reference name will be @"Customer Name".
* When formulas refer to display names or mapping names, the names should not contain any of following characters if the names are not quoted by double-quotation marks "":

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression @Customer#; will cause a syntax error. But @"Customer#" is ok.
  + If a field has the display name Category.Measure, when adding it to a formula, quote it as
    "Category.Measure" or "Category"."Measure".
* The number of the "if-else" statements in a formula is limited to 190. When this number is reached, you should use the "select-case" statement instead.

Below are some formula examples:

**Example 1: TerritoryUSA**

|  |
| --- |
| ``` if (@State in ["CT", "ME", "MA", "NH", "NY", "RI", "VT"]) {   "NorthEast, USA";} else if ( @State in ["DC", "DE", "MD", "NJ", "PA", "VA"]) {   "MidAtlantic, USA";} else if ( @State in ["CO", "ID", "KS", "MT", "NE", "NV", "NM", "ND", "SD", "UT"]) {   "Rockies, USA";} else if ( @State in ["AZ", "AR", "LA", "MO", "OK", "TX"]) {   "South, USA";} else if ( @State in ["AL", "FL", "GA", "MS", "NC", "SC"]) {   "SouthEast, USA";} else if ( @State in ["AK", "CA", "HI", "OR", "WA"]) {   "West, USA";} else if ( @State in ["IL", "IN", "LA", "KY", "MI", "MN", "OH", "TN", "WI", "WV", "WY"]) {   "MidWest, USA";} ``` |

* **Purpose**: In your sales report, you want Logi JReport to print out which territory the customer belongs to according to the abbreviated state names stored in the State field.
* **Explanation**: In the six else-if statements, Logi JReport will retrieve the value of the State field, and compare it with the values in brackets []. If a value matches the value in brackets, the formula will return the territory name.

**Example 2: DateToMonth**

|  |
| --- |
| ``` Number m = Month ( @"Order Date" ) ; String str = ""; if ( m == 1 ) {   str = " January Sales";} else if ( m == 2 ) {   str = " February Sales";} else if ( m == 3 ) {   str = " March Sales";} else if( m == 4 ) {   str = " April Sales";} else if( m == 5 ) {   str = " May Sales";} else if ( m == 6 ) {   str = " June Sales";} else if ( m == 7 ) {   str = " July Sales";} else if( m == 8 ) {   str = " August Sales";} else if ( m == 9 ) {   str = " September Sales";} else if( m == 10 ) {   str = " October Sales";} else if ( m == 11 ) {   str = " November Sales";} else if ( m == 12 ) {   str = " December Sales";} ``` |

* **Purpose**: In your sales report, you want Logi JReport to print out the month name of the orders, so that you can compare the orders of each month in a year.
* **Explanation**: Since the database field Order Date is of the TimeStamp data type, the built-in function Month (DateTime) is first used to extract the month portion of Order Date. Then, the else-if statement is used to decide the month according to the return value of the function, and assigns a String value which contains a relative month name to the pre-declared string variable str.

**Example 3: SectionInvisible**

|  |
| --- |
| ``` boolean s; if (pagenumber==1){   s=true;} else {   s=false;} ``` |

* **Purpose**: This formula is used to control the Suppressed property of a certain section such as Page Header, so that the section will be suppressed on the first page of the report.
* **Explanation**: Since it is only required to suppress the section on the first page, if only the Suppressed property of the section is set to true in the Report Inspector, then it will be suppressed on every page. In this formula, a Boolean type variable is first declared. Then, an else-if statement is used to decide whether or not the page is the first page. If the statement is true, true is assigned to "s". If the statement is false, false is assigned false to "s". In this formula, pagenumber is a special field.

**Example 4: Running total of page**

You can use the running total function to calculate the sum of one page. And to use the running total function, you have to create a set of formulas.

1. Create a formula named Formula1 as follows to initialize a global variable as the sum variable. And insert it into the BandedPageHeader panel. The reference to PageNumber forces the calculation to run after the page break. For more information, see [Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels).

   |  |
   | --- |
   | ``` pagenumber; global number pagetotal; pagetotal=0; ``` |
2. Create a formula named Formula2 as follows to accumulate the value. And insert it into the Detail panel.

   |  |
   | --- |
   | ``` pagetotal=pagetotal+@"YTD Sales"; ``` |
3. Create a formula named Formula3 as follows to display the sum of one page. And insert it into the BandedPageFooter panel.

   |  |
   | --- |
   | ``` return pagetotal; ``` |

**Example 5: Running total of group**

This example will accumulate the total of the successful and failed shipments for each group.

1. Create a formula named Formula1 as follows to initialize the value. And insert it into the group header.

   |  |
   | --- |
   | ``` global integer iFail; global integer iSuccess; iFail=0; iSuccess=0; ``` |
2. Create a formula named Formula2 as follows to accumulate the value of the successful and failed shipments, and insert it into the Detail panel.

   |  |
   | --- |
   | ``` if(@Shipped) {   iSuccess=iSuccess+1;    iFail=iFail;  } else {   iSuccess=iSuccess;    iFail=iFail+1; } ``` |
3. Create a formula named Formula3 as follows to return the successful shipments and the failed shipments, and insert it into the group footer.

   |  |
   | --- |
   | ``` return "Total successful shipments is "+ iSuccess +" and total failed shipments is "+ iFail; ``` |

**Note:**  Global variables are not supported in dynamic formulas so an alternate way to do this is using two formulas (fShipped and fNotShipped) to return either 1 or 0 based on @Shipped:

`if(@Shipped) return 1 else return 0;  
 if(@Shipped) return 0 else return 1;`

Then add dynamic aggregations to sum on fShipped and fNotShipped. The result will be the same as using the global variables.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589721-User-Defined-Formula-Functions)
