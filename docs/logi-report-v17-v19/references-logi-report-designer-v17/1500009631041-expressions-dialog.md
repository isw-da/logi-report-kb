---
title: "Expressions Dialog"
id: 1500009631041
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009631041-Expressions-Dialog
updated_at: 2021-07-24T16:04:42Z
---

# Expressions Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631061-Expression-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631741-Fetch-Data-Dialog)

# Expressions Dialog

The Expressions dialog helps you compose the filter conditions for a query dataset. It appears when you select **![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904178967/btn_chsr.gif)** to compose a condition.

The dialog varies for defining [filter condition](#Filter) or [record level security condition](#RLS).

---

When the dialog is used to compose the filter conditions for a query or a dataset created from a query, it contains three tabs: [Real Name](#Name), [Subquery](#Subquery), and [Field Value](#FieldValue). The Subquery tab is available only when defining filter for a query.

## Real Name

![Expressions dialog - Real Name tab](https://devnet.logianalytics.com/hc/article_attachments/4404904341911/exprsn_name.gif)

* When defining a query filter, this tab lists the tables added in the query with all their columns, as well as the parameters and valid formulas of these columns in the same catalog data source as the query.
* When defining a dataset filter, this tab lists the tables added in the data resource on which the dataset is created with all their columns, as well as the parameters and valid formulas of these columns in the same catalog data source as the data resource.

Double-click the required field to create the filter on it.

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

![Expressiongs dialog - Subquery tab](https://devnet.logianalytics.com/hc/article_attachments/4404916805655/exprsn_query.gif)

This tab allows you to create a [subquery](https://devnet.logianalytics.com/hc/en-us/articles/1500009635981-Creating-Queries-in-a-Catalog#Subquery) to use in the query filter by editing a query or creating a new query.

* **Edit Subquery**  
  Opens the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009609882-Query-Editor-Dialog) to edit the query.
* **New Subquery**  
  Creates a new subquery here.

## Field Value

![Expressions dialog - Field Value tab](https://devnet.logianalytics.com/hc/article_attachments/4404904342167/exprsn_fldvlu.gif)

This tab is disabled when the Expressions dialog is opened while setting the filter field. It lists all column names of the related table, in which the field to be filtered is. Select the column name of the field to be filtered, select OK, then the values of the field will be displayed. Choose the required value and select Set to use it to filter the field.

---

When the dialog is used to compose the conditions for a record level security policy, it contains two tabs: [Mapping Name](#MapName) and [Value](#Value).

## Mapping Name

![Expressions dialog - Mapping Name tab for record level security](https://devnet.logianalytics.com/hc/article_attachments/4404904342423/exprsn_mpnm.gif)

This tab lists the tables/views/synonyms, queries and hierarchical data sources in the current catalog data source with all their columns, as well as the parameters and valid formulas of these columns in the catalog data source, and the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName).

Double-click the required field to add it to the condition.

## Value

![Expressions dialog - Value tab for record level security](https://devnet.logianalytics.com/hc/article_attachments/4404904342679/exprsn_value.gif)

This tab is disabled when the Expressions dialog is opened while setting the field on which to build the condition. When a column is used for a condition, you can obtain the values of the column as follows: select the column in the Mapping Name tab, select the Value tab and the values of the selected column will be listed. double-click a value to set it as the value of the condition.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009631061-Expression-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631741-Fetch-Data-Dialog)
