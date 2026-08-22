---
title: "Creating Union Queries"
id: 12480387029005
section: "Manipulating Data Resources in a Catalog - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480387029005-Creating-Union-Queries
updated_at: 2026-02-25T23:47:38Z
source_host: docs-report.zendesk.com
---
# Creating Union Queries

You can combine specified records from more than one query into a result set by creating a union query. Unlike a join which creates one record with multiple columns from two queries, UNION appends the results of one query to the results of the second query, so the number of records is the sum of the two queries. This topic describes how you can create union queries in a catalog.

When creating a union query, you should make sure that in all the queries you are combining, you have added the same number of columns in the same order. You should also pay careful attention to the data type of the columns, and make sure that each column resides in the same position in all queries, as well as having compatible data types. The column names do not need to match. For example, if the first query has five columns, the first of which contains DateTime data, you should make sure that each of the other queries you are combining also has five columns, the first of which contains DateTime data, and so on. A common  union query usage is combining a query from one instance of a database to a second instance of the database. For example, you want all records of the Customers table from one database appended to all records of the Customers table from a second database. The two Customers tables must match exactly the number of columns, the SQL type, and sequence. 

 A union query does not support formulas and parameters.

To create a union query

- In the Catalog Manager, right-click a query (the primary query) and select Edit Query. 

- In the Query Editor dialog box, navigate to Menu > Query > Union > Select. Designer displays the Union dialog box.
  

- The Queries box contains all valid queries in the current catalog that you can combine to the primary query. Select a query and select Add to add it to the Union box. If no valid query is available, close the Union dialog box and go to the next step.

- In the Query Editor dialog box of the primary query, navigate to Menu > Query > Union > New.

- In the Enter Query Name dialog box, specify a name for the query and select OK. Designer displays a new Query Editor dialog box. 

- 
Define the new query.  The selecting order of the columns to include in the new query should refer to the order in the primary query. The SQL type and the number of the columns should also match those in the primary query. For example, when you select two columns in the primary query, the first one is  Integer data type and the second String,  then in the new query, you should also first select an Integer column and then a String column.

- Select OK to create the new query.

- Repeat steps 4 through 7 until you have created all the queries you want to combine to the primary query.

- Add the queries you just created from the Queries box to the Union box. To remove a query, select it in the Union box and select Remove.

- In the Union box, select in the Attribute column of each query to specify its attribute in the union.  
    
- 
: Select it if you do not want to return duplicate records from the query.

- 
: Select it if you want to return all records from the query.

- Select OK. The primary query now functions as a union query.
