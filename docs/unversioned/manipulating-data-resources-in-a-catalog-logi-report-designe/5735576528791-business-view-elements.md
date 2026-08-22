---
title: "Business View Elements"
id: 5735576528791
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735576528791-Business-View-Elements
updated_at: 2022-11-02T08:17:39Z
---

# Business View Elements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533912087-Benefits-of-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog)

# Business View Elements

A business view can contain the following elements: categories, group objects, detail objects, and aggregation objects (including custom aggregations). This topic introduces the usage of each element and the expression that a custom aggregation should follow.

You can add the following types of elements in a business view:

* **Category**  
  Categories are the main tool for organizing data. They are objects corresponding to particular collections of data in the data source. They are grouped in folders that are named to reflect information collections. A category can contain several subcategories.

  Organizing data into multiple categories or multiple levels of categories is meaningful. Users can use categories to find data elements they need, without having to know the underlying table names, although sometimes the table names are used as categories. Categories have no affect on the way reports get data at runtime. They are simply for users to find the data they need more easily.
* **Group**  
  Groups are view elements that are the basis for organizing data in a report. They present the availability and key performance of data, and characteristically return text data or dates, and answer the following questions: who, when, what, where, and which. You can insert a group object wherever you can insert a field: use it as a column or row field in a crosstab, as a group field or detail field in a table, or as a category or series field in a chart. Group objects may be based on DBFields such as region and country, or on formulas such as the year, quarter, or month portion of a date field. In order to create charts and crosstabs, at least one group element has to be in the business view since charts and crosstabs are all based on aggregating data into groups.
* **Detail**  
  Detail objects provide additional information. You can bind a detail object to a database field, formula, group object, or aggregation object, and use it to display detailed field values such as address and phone number for a customer in a table. However, you can neither use detail objects in crosstabs and charts nor use them for grouping in tables. If you have a question about an item being either a group or a detail element, make it a group element. You can use a group object in every case where a data object is allowed, but can only use detail objects in tables and banded objects.
* **Aggregation**  
  Aggregations (dynamic [summaries](https://devnet.logianalytics.com/hc/en-us/articles/5735532118039-Working-with-Summaries)) are numeric view elements that Logi Report Engine calculates at runtime based on the group elements in a report. You can use aggregations alone or with other fields. You can insert an aggregation wherever you can insert summaries. For example, you can insert aggregations in the group header or footer panel of a table, use them as aggregate fields in a crosstab or as the values in a chart. Logi Report Engine calculates aggregation values based on the group level at which you insert them such as total sales, average order size, and number of orders from a customer. You can also create custom aggregations for sophisticated mathematical and logic calculation purposes.

## Custom Aggregations

Custom aggregations are special aggregations used for sophisticated mathematical and logic calculation purposes. You can create custom aggregations using the Formula Editor and define them based on the elements in a business view and the built-in functions including aggregation functions, and other mathematical and logic calculation related functions. You can create a custom aggregation as an aggregation object or as a [dynamic formula](https://devnet.logianalytics.com/hc/en-us/articles/5735534296599-Using-Dynamic-Resources-and-Local-Parameters-in-a-Report#Formula) that is used as Aggregation in a business view.

When using a custom aggregation in a data component, you need to make sure that you also add the group elements referenced in the custom aggregation as table group-by field, crosstab column/row field, or chart category/series field in the data component.

**Custom aggregation expression**

The expression for a custom aggregation is defined by relative member set and aggregation. It returns a single value or an array.

The general expression structure of a custom aggregation is: *@(<Group Collection>, <Aggregation>)* or *@(<Group Collection>, <Detail>)*.

The following explains each segment in the expression.

* **<Group Collection>**  
  It contains "1-N" groups. For each group, you can declare a member. You can express <Group Collection> as *(<Group Exp>1, <Group Exp>2, … <Group Exp>N)*, and <Group Exp> as *<Group Name>:<member>*. Within <Group Collection>, <Group Name> cannot be duplicated. At runtime, if Logi Report Engine cannot calculate a <Group Name>, it ignores its <Group Exp>.
  + **<Group Name>**  
     It could be one of the following:
    - The qualified display name of a group, with the "@" symbol at the beginning. For example: *@"Customers.Country"*.
    - **CROSSTAB\_ROW**  
      A group used on crosstab row. You can use a custom aggregation containing this
      variable in the crosstab aggregation cell only.
      * Option: +/- N  
        The group used on current group inner/outer "N" level. "N" is an integer from 1.
    - **CROSSTAB\_COLUMN**  
      A group used on crosstab column. You can use a custom aggregation containing this
      variable in the crosstab aggregation cell only.
      * Option: +/- N  
        The group used on current group inner/outer "N" level. "N" is an integer from 1.

      In the following example, G1, G2, G3, G4, and G5 are group names.

      ![](https://devnet.logianalytics.com/hc/article_attachments/9898458593943/bv_elmnt_ca.gif)
    - **CHART\_CATEGORY**  
      The group used on chart category. You can use a custom aggregation containing this
      variable as Show Value of chart only.
    - **CHART\_SERIES**  
      The group used on chart series. You can use a custom aggregation containing this
      variable as Show Value of chart only.
    - **CURRENT**  
      The group used on current group level. When you use a custom aggregation containing this variable as Show Value of chart, it is the group used on the category axis; when you use it in the crosstab aggregation cell, if there is no group on the crosstab row, it is the same as CROSSTAB\_COLUMN, else the same as CROSSTAB\_ROW.
      * Option: +/- N  
        The group used on current group inner/outer "N" level. "N" is an integer from 1.
  + **<member>**  
     It could be one the following:
    - A variable.
    - A single value, such as "USA".
    - ALL means the "All" member of the group.
    - CHILDREN means all the other group members excluding the "All" member.
    - CURRENT means the current group member.
    - A member [navigation function](#Navigate): *nextMember()* or *prevMember()*.
    - Empty string means CURRENT.

      *@GroupName* means *@GroupName:CURRENT*  
      *@GroupName:* means *@GroupName:CURRENT*  
      *@GroupName:""* (zero length string) means *@GroupName:CURRENT*
* **<Aggregation>**  
   It could be one of the following:
  + Aggregation expressed using aggregate function such as *Sum(@ID)*.
  + The qualified display name of an aggregation, with the "@" symbol at the beginning. For example: *@"Orders Detail.Total Quantity"*.
  + The name of a dynamic aggregation or dynamic formula used as Aggregation, with the "@" symbol at the beginning.
  + The qualified display name of a group using CHILDREN as the member, with the "@" symbol at the beginning, such as *@Customers.Customer ID: CHILDREN*.

  Loop reference is not supported, for example:

  + CA2 is defined using *@(<Group Collection>, @CA1)* .
  + CA3 is defined using *@(<Group Collection>, @CA2)* .
  + CA1 is defined using *@(<Group Collection>, @CA3)* .
* **<Detail>**  
  It could be the qualified display name of a detail object or the name of a dynamic formula used as Detail, with the "@" symbol at the beginning. It returns an array for detail value.

**Navigation functions used in custom aggregation expressions**

When composing the expression of a custom aggregation, you can use a navigation function [nextMember()](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions#nextMember) or [prevMember()](https://devnet.logianalytics.com/hc/en-us/articles/5735511718167-Appendix-1-Formula-Functions#prevMember) to navigate to the next/previous member of a group or detail object. You can use the navigation function as the <member> argument in the expression of a custom aggregation.

The navigation functions do not actually return a member, because formulas do not have a member data type, instead, the functions only locate a specific member of a group or detail object when a custom aggregation expression is executed on a specific group node or on a crosstab cell. When the custom aggregation is executed on an ALL member, the functions always locate the ALL member itself.

The order of the members could be the following:

* If the group in the aggregation is used as a group in a data component with order, the members take the order in the data component, or else they are sorted in the ascending order.
* For a group used more than once in a data component, it is the highest group setting. If the group is used on both row header and column header of a crosstab, it is the highest group setting on the row header.
* The previous/next member of the "All" member is also "All".

Whether a navigation function can locate the members of a group or detail object depends on whether you define the range of members clearly. Logi Report Engine confines the range of members of a group or detail object to the current values of all the parent groups if there are any parent groups, and takes the hierarchy of the groups into consideration. For example, we have two groups: Country and City, with members as follows:

China

> Beijing  
> Shanghai

USA

> New York

When talking about city.FIRSTMEMBER, we first consider what the country is. If the current country is China, it is Beijing and city.LASTMEMBER is Shanghai; if the current country is USA, it is New York. In this way, Logi Report Engine can avoid inappropriate combinations such as the country China and the city New York.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) Since the combination of the country China and the city New York in a crosstab cell displays as blank, the navigation functions do not execute on such combination and therefore the corresponding crosstab cells are kept as blank.

**Examples of custom aggregation expressions**

* `@(@"Orders Detail.Sales Year":ALL,@"Customers.Country":"USA",Sum(@"Orders Detail.Quantity"))`
* `@(@"MonthOfOrderDate":CURRENT,@"Orders Detail.Total Quantity") - @(@"MonthOfOrderDate":PrevMember(),@"Orders Detail.Total Quantity")`
* `@(@"Customers.Country":"USA",@"Orders Detail.Total Quantity") / Sum(@"Orders Detail.Quantity")`
* `@"Orders Detail.Total Quantity" / Sum(@"Orders Detail.Quantity")`
* `Average(@(@"F_day":Children,@"Count_Order ID"))`. Here "F\_day" is a dynamic formula used as Group which is defined as: `ForeachDay(@"Orders Detail.Order Date")`
* `DATE[] dateArray = @(@"Orders Detail.Order Date": CHILDREN);  
  DATE maxDate = Maximum(dateArray);  
  NUMBER sumQuantityOfMaxDate = @(@"Orders Detail.Order Date": maxDate, Sum(@"Orders Detail.Quantity"));  
  RETURN sumQuantityOfMaxDate`
* Custom aggregation expression can reference [crosstab formula](https://devnet.logianalytics.com/hc/en-us/articles/5735520960151-Using-Crosstab-Formulas), for example, `@(@Country:"USA",@Year:CHILDREN, @@CTF1)`. Here "CTF1" is the name of a crosstab formula.

**Custom aggregation calculation logic**

The calculation of custom aggregations is based on data components. The following describes the calculation logic in a crosstab. Calculation on chart category and series is similar to that on crosstab. Logi Report Engine regards other data components with group structure as one-direction crosstabs.

1. Check whether the original custom aggregation expression includes every group of the crosstab. If a group is not included, Logi Report Engine adds *@Group:CURRENT* into the expression.

   For example, a custom aggregation is defined as `@(@Year:CURRENT, @Month:CURRENT, Sum(@Sales))`, which contains the two groups: @Year:CURRENT and @Month:CURRENT. When you use it in a crosstab with row field Country and column field Region, Country and Region also determine member combination, so the expression is `@(@Year:CURRENT, @Month:CURRENT, @Country:CURRENT, @Region:CURRENT, Sum(@Sales))`.

   If a custom aggregation uses the variable as <Group Name> in the expression, such as CURRENT, CROSSTAB\_ROW, CROSSTAB\_COLUMN, CHART\_CATEGORY, and CHART\_SERIES, during the calculation, Logi Report Engine needs to replace the variable by a group name in the data component, and which group name Logi Report Engine uses depends on the position where the custom aggregation is in the data component.
2. Replace every member value CURRENT using the member of the cell where the custom aggregation is, which could be a constant value or ALL.

   In the preceding example, Logi Report Engine knows Country and Region member values of the cells, but cannot know that of Year and Month, so Year and Month members are ALL, and the expression is `@(@Year:ALL, @Month:ALL, @Country:"USA", @Region:"CA", Sum(@Sales))`.
3. Return the aggregation value based on the member combination. If there is not any CHILDREN member/member set in the combination, the aggregation expression returns a single value, or else returns an array, and the order of the array elements should be according to the column and row order of the crosstab. When the aggregation expression cannot retrieve member, it returns the value "Null". When you use the Running functions in the custom aggregation expression, if the group member combination does not have relative cell in the crosstab, the aggregation expression returns "Null".

During the custom aggregation calculation, error may occur when any of the following happens:

* Logi Report Engine cannot replace the <Group Name> variable by a concrete <Group Name>.
* <Group Collection> has duplicated <Group Name>.

  For example, you define a custom aggregation "CusAgg1"as `@(CURRERT:CURRENT, @Year:"2014", Sum(@Sales))` and insert it into a data component's Year group. During calculation, <Group Collection> is `@Year:CURRENT, @Year:PrevMember()`, where group names are duplicated.
* The data component has no such group mentioned by <Group Name>.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735533912087-Benefits-of-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735576514071-Creating-Business-Views-in-a-Catalog)
