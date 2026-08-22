---
title: "Applying All Values to a Parameter in SQL Statement"
id: 1500009590041
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590041-Applying-All-Values-to-a-Parameter-in-SQL-Statement
updated_at: 2021-07-24T05:54:30Z
---

# Applying All Values to a Parameter in SQL Statement

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590201-Importing-Parameter-Values)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589641-Formulas)

# Applying All Values to a Parameter in SQL Statement

If a parameter allows multiple values and is enabled to use one single value "All" to represent all its values (the way to enable the "All" value is to set [Enable the "All" Option](https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog#All) to true when creating or editing the parameter), when you use the parameter in an imported SQL, you should embed each IN condition in parenthesis to enable the "All" value to work properly.

For example, there are two parameters: @pCountry and @pID. Suppose that they both can allow multiple values and have enabled the "All" option and you would like to reference them in an imported SQL query, you should embed each IN condition in parenthesis as follows:

`select... from ... where ... and ... and (country in @pCountry) and (customerid in @pID)`

There is another case in which you should also embed each IN condition in parenthesis when using such parameters for the same purpose: when you create or edit a Logi JReport query via the Query Editor, you choose to [modify its SQL statement manually](https://devnet.logianalytics.com/hc/en-us/articles/1500009570742-Editing-the-SQL-Statements-of-a-Query). If the customized statement fails to be parsed by Logi JReport and you would like to save the statement anyway, then it is up to you to guarantee the statement correctness. In this case, you should embed each IN condition in parenthesis. The reason for this is that when "All" is selected the in condition is replaced with (1 = 1), unless it is in parenthesis the substitution will create a syntax error. Another consideration when using "All" is the ( 1 = 1 ) may return more values than the user sees in the multi-value parameter dialog if you have customized the SQL to not return all distinct values.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590201-Importing-Parameter-Values)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589641-Formulas)
