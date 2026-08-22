---
title: "Business View Elements"
id: 1500009562702
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562702-Business-View-Elements
updated_at: 2021-07-24T05:56:15Z
---

# Business View Elements

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562602-Creating-a-Business-View)

# Business View Elements

The following are elements contained in business views:

* **Category**  
   Categories are the main tools for organizing data. They are components which correspond to particular collections of data in the data source. They are grouped in folders that are named to reflect information collections. A category can contain several subcategories.

  Organizing data required by a user into multiple categories or multiple levels of categories is meaningful, and makes it easy to use. End users can use categories to find data elements they need to use without knowing the underlying table names although sometimes the table names are used as categories.

  Categories have no affect on the way reports get data at runtime. They are simply for the end users to more easily find the data they need.
* **Group**  
   Groups are view elements that are the basis for organizing data in a report. They present the availability and key performance of data, and characteristically return text data or dates, and answer the following question: who, when, what, where and which. A group element can be inserted wherever a field can be inserted, as a column or row in a crosstab, or as a group field or detail field in a table or as a category or series in a chart. Group elements may be based on DBFields such as region and country or based on formulas such as the year, quarter, or month portion of a date field. In order to create charts and crosstabs, at least one group element has to be in the business view since charts and crosstabs are all based on aggregating data into groups.
* **Detail**Detail elements provide additional information. They can be bound to a database field, formula, group element or aggregation element, and are used for displaying detailed field values such as address and phone number for a customer in a table. Detail elements cannot be used in crosstabs and charts and cannot be used for grouping in tables. If you have a question about an item being either a group or a detail element, make it a group element. A group element can be used in every case of using a data object but detail elements can only be used in tables and banded objects.
* **Aggregation**  
   Aggregations (dynamic summaries) are numeric view elements that are calculated at runtime based on the group elements in the report. Aggregations can be used alone or calculated with other fields. An aggregation can be inserted wherever summaries can be inserted. For example, aggregations can be inserted in the group header or footer panel of a table, as an aggregate field in a crosstab, or as the value in a chart. Logi JReport calculates values based on the group level at which the aggregation is inserted such as total sales, average order size and number of orders from a customer. Logi JReport also supports custom aggregations.

## Custom aggregations

Custom aggregations are special aggregations used for sophisticated mathematic and logic calculation purposes. They are created using the Formula Editor and are defined based on the elements in a business view and the built-in functions including aggregation functions, mathematic and logic calculation related functions. Custom aggregations can be created as [aggregation objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009562642-Adding-and-Modifying-Elements#CustomAgg) or as [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Dynamic) that are used as aggregations in a business view.

When using a custom aggregation in a data component, you need to make sure the group elements referenced in the custom aggregation are also added as table group by field, crosstab column/row field or chart category/series field in the data component.

**Custom aggregation expression**

The expression for a custom aggregation is defined by relative member set and aggregation. It returns a single value or an array.

The general expression structure of a custom aggregation is @(<Group Collection>, <Aggregation>) or @(<Group Collection>, <Detail>).

The following details each segment in the expression.

* **<Group Collection>**It contains 1-N groups. For each group you can declare a member. <Group Collection> can be expressed as (<Group Exp>1, <Group Exp>2, … <Group Exp>N), enclosed in parentheses. <Group Exp> can be expressed as <Group Name>:<member>. Within <Group Collection>, <Group Name> cannot be duplicated. If a <Group Name> cannot be calculated, its <Group Exp> will be ignored.
  + **<Group Name>**  
     It could be one of the following:
    - The qualified display name of a group, with @ at the beginning. For example: `@"Customers.Country"`.
    - **CROSSTAB\_ROW**  
       A group used on crosstab row. A custom aggregation containing this
      variable can be used in crosstab aggregation cell only.
      * Option: +/- N  
         The group used on current group inner/outer N level. N is an integer from 1.
    - **CROSSTAB\_COLUMN**  
       A group used on crosstab column. A custom aggregation containing this
      variable can be used in crosstab aggregation cell only.
      * Option: +/- N  
         The group used on current group inner/outer N level. N is an integer from 1.

      In the following example, G1, G2, G3, G4, and G5 are group names.

      ![](https://devnet.logianalytics.com/hc/article_attachments/4404889430807/bv_elmnt_ca.gif)
    - **CHART\_CATEGORY**  
       The group used on chart category. A custom aggregation containing this
      variable can be used as Show Value of chart only.
    - **CHART\_SERIES**The group used on chart series. A custom aggregation containing this
      variable can be used as Show Value of chart only.
    - **CURRENT**The group used on current group level. When a custom aggregation containing this
      variable is used as Show Value of chart, it is the group used on the category axis; when used in crosstab aggregation cell, if there is no group on the crosstab row, it is the same as CROSSTAB\_COLUMN, else the same as CROSSTAB\_ROW.
      * Option: +/- N  
         The group used on current group inner/outer N level. N is an integer from 1.
  + **<member>**  
     It could be one the following:
    - A single value, such as "USA".
    - ALL means the "All" member of the group.
    - CHILDREN means all the other group members excluding the "All" member.
    - CURRENT means the current group member.
    - A member navigation function: [nextMember()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#nextMember) or [prevMember()](https://devnet.logianalytics.com/hc/en-us/articles/1500009589561-Other-Functions#prevMember).
    - Empty string means CURRENT.

      @dim means @dim:CURRENT   
       @dim: means @dim:CURRENT  
       @dim:"" zero length string, means @dim:CURRENT
* **<Aggregation>**  
   It could be one of the following:
  + Aggregation expressed using aggregation function, like Sum(@ID).
  + The qualified display name of an aggregation, with @ at the beginning. For example: `@"Orders Detail.Total Quantity".`
  + The name of a dynamic aggregation or dynamic formula used as Aggregation, with @ at the beginning.

  Loop reference is not supported, for example:

  + CA2 is defined using @(<Group Collection>, @CA1)
  + CA3 is defined using @(<Group Collection>, @CA2)
  + CA1 is defined using @(<Group Collection>, @CA3)
* **<Detail>**  
   It could be the qualified display name of a detail element or the name of a dynamic formula used as Detail, with @ at the beginning. It returns an array for detail value.

Here are some custom aggregation expression examples:

* `@(@"Orders Detail.Sales Year":ALL,@"Customers.Country":"USA",Sum(@"Orders Detail.Quantity"))`
* `@(@"MonthOfOrderDate":CURRENT,@"Orders Detail.Total Quantity") - @(@"MonthOfOrderDate":PrevMember(),@"Orders Detail.Total Quantity")`
* `@(@"Customers.Country":"USA",@"Orders Detail.Total Quantity") / Sum(@"Orders Detail.Quantity")`
* `@"Orders Detail.Total Quantity" / Sum(@"Orders Detail.Quantity")`
* `Average(@(@"F_day":Children,@"Count_Order ID"))`. Here F\_day is a dynamic formula used as group which is defined as: `ForeachDay(@"Orders Detail.Order Date")`

**Calculation logic**

The calculation of custom aggregations is based on data components. The following introduces the calculation logic in a crosstab. Calculation on chart category and series is similar to that on crosstab. Other components with group structure can be regarded as one-direction crosstabs.

1. Check whether every group of the crosstab is included in the original custom aggregation expression. If a group is not included, Logi JReport adds @Group:CURRENT into the expression.

   For exmaple, a custom aggregation is defined as `@(@Year:CURRENT, @Month:CURRENT, Sum(@Sales))`, which contains the two groups @Year:CURRENT and @Month:CURRENT, when it is used in a crosstab with row header Country and column header Region, Country and Region will also determine member combination, so the expression will be `@(@Year:CURRENT, @Month:CURRENT, @Country:CURRENT, @Region:CURRENT, Sum(@Sales))`.

   If a custom aggregation uses variable as <Group Name> in the expression, such as CURRENT, CROSSTAB\_ROW, CROSSTAB\_COLUMN, CHART\_CATEGORY, and CHART\_SERIES, during the calculation the variable need to be replaced by a group name in the data component, and which group name will be used depends on the position where the custom aggregation is inserted in the data component.
2. Replace every member value CURRENT using the member of the cell where the custom aggregation is inserted, which could be a constant value or ALL.

   In the above example, Logi JReport knows Country and Region member values of the cells, but cannot know that of Year and Month, so Year and Month members are ALL, and the expression will be `@(@Year:ALL, @Month:ALL, @Country:"USA", @Region:"CA", Sum(@Sales))`.
3. Return the aggregation value based on the member combination. If there is not any CHILDREN member/member set in the combination, it returns a single value, or else returns an array, and the order of the array elements should be according to column and row order of the crosstab. When member cannot be gotten, the aggregation expression will return the value "Null".

> When the Running functions are used in the custom aggregation expression, if the group member combination does not have relative cell in the crosstab, it returns Null.

During the custom aggregation calculation, error may occur when any of the following happens:

* <Group Name> variable cannot be replaced by a concrete <Group Name>.
* <Group Collection> has duplicated <Group Name>.

  For example: CusAgg1 is defined as `@(CURRERT:CURRENT, @Year:"2014", Sum(@Sales))` and is inserted into a data component's Year group. During calculation, <Group Collection> is `@Year:CURRENT, @Year:PrevMember()`, where group names are duplicated.
* The data component has no such group mentioned by <Group Name>.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562602-Creating-a-Business-View)
