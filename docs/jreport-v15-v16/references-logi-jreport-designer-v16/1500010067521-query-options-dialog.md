---
title: "Query Options Dialog"
id: 1500010067521
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010067521-Query-Options-Dialog
updated_at: 2021-07-24T10:38:29Z
---

# Query Options Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032242-Query-Modifier-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067541-Rank-Expert-Dialog)

# Query Options Dialog

The Query Options dialog helps you to specify the settings for a query. It appears when you select Menu > Query > Current Query Options in the [Query Editor](https://devnet.logianalytics.com/hc/en-us/articles/1500010067501-Query-Editor-Dialog).

![Query Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901185943/qryoptn.gif)

The following are details about options in the dialog:

**Auto Join Defaults:**

Specifies the options for auto joins.

* **Join on foreign keys**  
   Specifies to automatically join tables in a query through a reference from Table A to a primary key in Table B. For example, an order form in Table A shows information on purchases that are made by a customer with a primary key of CustomerID. The customer ID # refers to a record in Table B which lists a specific address, phone number, name, and so on for the customer. The CustomerID in Table A is a foreign key because it links the customer's ordering information in Table A to the customer's information in Table B using the CustomerID field.
* **Join on primary keys with same names**  
   Specifies to automatically join tables in a query through a field or a combination of fields that uniquely and specifically identifies a record. For example, the OrderID may be the primary key in a table for Orders and also for Payments.
* **Join on same name**  
   Specifies to automatically join tables in a query through a link between two columns of the same name in two different tables. This often creates many invalid joins such as Amount that appears in both tables.

**Show Mapping Names**

If selected, the full names of the columns in the tables will be displayed in the criteria panel of the Query Editor.

**Show Table Names**

If selected, the table that each column belongs to will be displayed in the criteria panel of the Query Editor.

**Warn When Cartesian Exists**

Specifies whether or not to display a warning when a Cartesian exists. A Cartesian product is used when tables are added to the query with no join specifications.

For example, Table A has three values: A, B and C and Table B has three values: 1, 2 and 3. Value A matches value 1, value B matches value 2, and so on. This is a specific match.

A Cartesian product would have value A matching with 1, 2 and 3, and value B matching with 1, 2 and 3, and so on. Depending on the data values Cartesian products can produce large datasets since each record in Table A matches every record in Table B.

**OK**

Applies the settings for the query and leaves the dialog.

**Cancel**

Does not retain the settings for the query and leaves the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010032242-Query-Modifier-Editor-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010067541-Rank-Expert-Dialog)
