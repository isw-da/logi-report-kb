---
title: "Expressions Dialog"
id: 1500010065881
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010065881-Expressions-Dialog
updated_at: 2021-07-24T10:38:53Z
---

# Expressions Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065901-Expression-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066721-Fetch-Data-Dialog)

# Expressions Dialog

The Expressions dialog helps you compose the filter conditions for a query dataset. It appears when you select **![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901122967/btn_chsr.gif)** to compose a condition and differs for [filter condition](#Filter) and [record level security condition](#RLS).

When the dialog is used to compose the filter conditions for a query or a dataset created from a query, it contains three tabs: [Real Name](#Name), [Subquery](#Subquery) and [Field Value](#FieldValue). The Subquery tab is available only when defining filter for a query.

## Real Name

![Expressions dialog - Real Name tab](https://devnet.logianalytics.com/hc/article_attachments/4404901262359/exprsn_name.gif)

* When defining a query filter, this tab lists the tables added in the query with all their columns, as well as the parameters and valid formulas of these columns in the same catalog data source as the query.
* When defining a dataset filter, this tab lists the tables added in the data resource on which the dataset is created with all their columns, as well as the parameters and valid formulas of these columns in the same catalog data source as the data resource.

double-click the required field to create the filter on it.

The following symbols at the bottom allow you to modify the expression according to your requirements.

* **+**  
   Adds numbers or fields together in the Expression menu.
* **-**  
   Subtracts numbers or fields together in the Expression menu.
* **\***  
   Multiplies numbers or fields together in the Expression menu.
* **/**  
   Divides numbers or fields together in the Expression menu.
* **=**  
   Equates fields together
* **"**  
   Places quotations on long character strings or name that have blanks in them. For example, you should place quotes on values such as "New York" or "Washington DC")
* **||**  
   Allows you to place fields together in the same Expression menu. For example, "New York" || "Washington DC")
* **( )**  
   Places your fields in parentheses

## Subquery

![Expressiongs dialog - Subquery tab](https://devnet.logianalytics.com/hc/article_attachments/4404909221527/exprsn_query.gif)

This tab allows you to create a [subquery](https://devnet.logianalytics.com/hc/en-us/articles/1500010034642-Creating-Queries-in-a-Catalog#Subquery) to use in the query filter by editing a query or creating a new query.

* **Edit Subquery**  
   Opens the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog) to edit the query.
* **New Subquery**  
   Creates a new subquery here.

## Field Value

![Expressions dialog - Field Value tab](https://devnet.logianalytics.com/hc/article_attachments/4404909221783/exprsn_fldvlu.gif)

This tab is disabled when the Expressions dialog is opened while setting the filter field. It lists all column names of the related table, in which the field to be filtered is. Check the column name of the field to be filtered, select OK, then the values of the field will be displayed. Choose the required value and select Set to use it to filter the field.

---

When the dialog is used to compose the conditions for a record level security policy, it contains two tabs: [Mapping Name](#MapName) and [Value](#Value).

## Mapping Name

![Expressions dialog - Mapping Name tab for record level security](https://devnet.logianalytics.com/hc/article_attachments/4404901262615/exprsn_mpnm.gif)

This tab lists the tables/views/synonyms, queries and hierarchical data sources in the current catalog data source with all their columns, as well as the parameters and valid formulas of these columns in the catalog data source, and the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010029242-Special-Fields#UserName).

Double-click the required field to add it to the condition.

## Value

![Expressions dialog - Value tab for record level security](https://devnet.logianalytics.com/hc/article_attachments/4404901262871/exprsn_value.gif)

This tab is disabled when the Expressions dialog is opened while setting the field on which to build the condition. When a column is used for a condition, you can obtain the values of the column as follows: select the column in the Mapping Name tab, select the Value tab and the values of the selected column will be listed. double-click a value to set it as the value of the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010065901-Expression-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010066721-Fetch-Data-Dialog)
