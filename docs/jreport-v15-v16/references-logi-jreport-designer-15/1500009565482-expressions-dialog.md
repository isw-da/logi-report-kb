---
title: "Expressions Dialog"
id: 1500009565482
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565482-Expressions-Dialog
updated_at: 2021-07-24T05:55:21Z
---

# Expressions Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565502-Expression-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587481-Fetch-Data-Dialog)

# Expressions Dialog

The Expressions dialog appears when you select **![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif)** to compose the filter conditions for a query or dataset.

This dialog consists of three tabs. The Subquery tab is available only when defining a query filter.

* [Real Name](#Name)
* [Subquery](#Subquery)
* [Field Value](#Value)

## Real Name

[See the tab](javascript:%20void(null)).

![Expressions dialog - Real Name](https://devnet.logianalytics.com/hc/article_attachments/4404889363735/dlg_exprsn_name.gif)

* When defining a query filter, this tab lists the tables added in the query with all their columns, as well as the parameters and valid formulas in the catalog data source where the query is added.
* When defining a dataset filter, this tab lists the tables added in the data resource on which the dataset is created with all their columns, as well as the parameters and valid formulas in the catalog data source where the data resource is added.

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

[See the tab](javascript:%20void(null)).

![Expressiongs dialog - Subquery](https://devnet.logianalytics.com/hc/article_attachments/4404889363991/dlg_exprsn_query.gif)

This tab allows you to create a [subquery](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query#Subquery) to use in the query filter by editing a query or creating a new query.

* **Edit Subquery**  
   Opens the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500009567142-Query-Editor-Dialog) to edit the query.
* **New Subquery**  
   Creates a new subquery here.

## Field Value

[See the tab](javascript:%20void(null)).

![Expressions dialog - Field Value](https://devnet.logianalytics.com/hc/article_attachments/4404889364247/dlg_exprsn_value.gif)

This tab is disabled when the Expressions dialog is opened while setting the filter field. It lists all column names of the related table, in which the field to be filtered is. Check the column name of the field to be filtered, select OK, then the values of the field will be displayed. Choose the required value and select Set to use it to filter the field.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565502-Expression-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009587481-Fetch-Data-Dialog)
