---
title: "Query Options Dialog Box"
id: 28898227161357
section: "References - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28898227161357-Query-Options-Dialog-Box
updated_at: 2024-09-30T09:09:02Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Query Options Dialog Box

You can use the Query Options dialog box to specify the settings for a query. This topic describes the options in the dialog box.
    

Designer displays the Query Options dialog box when you navigate to Menu > Query > Current Query Options in the Query Editor dialog box.

Designer displays these options:

Auto Join Defaults

You can specify the criteria based on which to join the tables automatically in the query in this box.

- 
Join on Foreign Keys
Select to automatically join tables in a query through a reference from Table A to a primary key in Table B. For example, an order form in Table A shows information on purchases that are made by a customer with a primary key of CustomerID. The customer ID # refers to a record in Table B which lists a specific address, phone number, name, and so on for the customer. CustomerID in Table A is a foreign key because it links the customer's ordering information in Table A to the customer's information in Table B using the CustomerID field.

- 
Join on Primary Keys with Same Names
Select to automatically join tables in a query through a field or a combination of fields that uniquely and specifically identifies a record. For example, OrderID may be the primary key in a table for Orders and also for Payments. 

- 
Join on Same Name
Select to automatically join tables in a query through a link between two columns of the same name in two different tables. This often creates many invalid joins such as Amount that appears in both tables.

Show Mapping Names

Select to display the full names of the columns in the criteria panel of the Query Editor dialog box.

Show Table Names

Select to display the name of the table that each column belongs to in the criteria panel of the Query Editor dialog box.

Warn When Cartesian Exists

Select to let Designer display a warning message when a Cartesian product exists. A Cartesian product is used when you add tables to the query with no join specifications.

OK

Select to apply your settings and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

Previous Topic  Next Topic
