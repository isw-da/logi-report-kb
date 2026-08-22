---
title: "Using Pre-joins in Queries"
id: 1500009592581
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592581-Using-Pre-joins-in-Queries
updated_at: 2021-07-24T05:53:52Z
---

# Using Pre-joins in Queries

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570662-Editing-a-Query)

# Using Pre-joins in Queries

Logi JReport Designer provides you with the option of choosing whether or not to use the [Pre-join](https://devnet.logianalytics.com/hc/en-us/articles/1500009583161-Defining-the-Join-Relationships-Between-Resources) feature when creating queries. If you want to use it, you must have this option enabled.

**To turn on the Pre-join feature:**

1. Make sure Forbid editing data object properties in the Catalog category of the Options dialog is unchecked.
2. In the Catalog Manager, select the data source in which you want to create queries, then select **Show Properties**  to expand the Properties sheet.
3. Set the Pre-join property of the data source to **true**.

Then, when you add tables contained in the data source to queries in the same data source, the pre-joins defined on the data source will be automatically applied to the tables.

Below is a list of the sections covered in this topic:

> * [Creating Queries Using Pre-join](#Create)
> * [Editing Queries Using Pre-join](#Edit)

## Creating Queries Using Pre-join

When you create a query using the pre-join feature, the following cases may appear:

* If Logi JReport Designer needs other tables to bridge the tables you have added, you will be prompted to decide whether to add another table to the query. For example,

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404893820951/qury_prjn1.gif)

  Suppose you've added table A and C to your query, a message box will then appear asking you whether you want to add table D in order to create links between tables A and C.

  **Note:** The prompt message appears only when the option "Show warning message when adding tables" is selected in the Query Editor category of the Options dialog. Otherwise, Logi JReport will add the bridged table automatically without any prompt.
* If there is more than one path available in the pre-join, as with this case,

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404893821207/qury_prjn2.gif)

  You've added table A and C to the query, and there are two paths available - ABC and ADC. Logi JReport Designer will ask you for the path ABC or ADC.

  Logi JReport Designer provides two methods for seeing the path information of a query:

  + In the Catalog Manager, expand the Properties sheet and select the query that uses the pre-join path. You will then see a property called Path Name which shows the name of the path used.
  + In the Query Editor, select the **Show Paths** button.

## Editing Queries Using Pre-join

One query is bound with at most one path. Once a path has been specified for a query, when you modify the relationships among the tables, you can make changes to a specific query based on that path, but the path itself will not be changed. When you edit a query, the following cases may appear:

* Adding tables to a query that has already been specified a path - If more than one path is suitable after the tables have been added, the specific path will still be used. That is, you cannot choose another path to replace the original one.
* If the path specified for a query is deleted - In the Query Editor, the Show Paths button will be disabled.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009570662-Editing-a-Query)
