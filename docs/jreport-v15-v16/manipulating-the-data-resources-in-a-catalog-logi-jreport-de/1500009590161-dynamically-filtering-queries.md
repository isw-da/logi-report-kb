---
title: "Dynamically Filtering Queries"
id: 1500009590161
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590161-Dynamically-Filtering-Queries
updated_at: 2021-07-24T05:54:28Z
---

# Dynamically Filtering Queries

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590221-Referencing-Parameters-in-a-Formula)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590241-Supplementing-WHERE-Portions)

# Dynamically Filtering Queries

You can use a parameter in a WHERE clause so that the query result can vary each time according to the entered parameter value. This works the same for [Logi JReport queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries) created with the Query Editor, [imported SQL files](https://devnet.logianalytics.com/hc/en-us/articles/1500009564042-Predefined-SQL-Files), [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) and [datasets](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets). When using imported SQL, simply put *@ParamterName* or *:ParameterName* directly into the SQL file to be imported. Logi JReport will provide the default values when you import the file so the database recognizes the syntax. This is the most common usage of parameters. See the following example.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source and create a type-in parameter named IDSet of Integer type with the default values 1, 10, and 20, and enable the Allow Multiple Values option.
3. In the same data source, [create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query) CustomersInfo on the table Customers. Select all the fields contained in the table.
4. In the Query Editor, select **Menu** > **Query** > **Filter**.
5. Filter the records of the query by adding a condition as follows in the Search Condition dialog (for details, see [Filtering with the Filter Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query#Filter)):

   ![Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404893826455/prmtr_app_fltrqry1.gif)
6. [Create a page report with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the query as follows: have the fields Customer ID, Customer Name, City and Phone displayed in the table and apply the Commercial style.
7. View the report. In the Enter Parameter Values dialog, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404889276567/btn_chsr.gif) next to the value field of IDSet.
8. In the Enter Values dialog, uncheck the **All** option, add the listed values 1, 10, and 20 to the right box, and then select **OK**. You will find that the records with Customer ID equal to 1, 10 and 20 have been retrieved.

   ![Filter Query with Customer ID](https://devnet.logianalytics.com/hc/article_attachments/4404889300503/prmtr_app_fltrqry2.gif)
9. View the report again. This time, in the Enter Values dialog, remove 1, 10, and 20 from the Selected Values box first. Enter the values 3, 7, 9, 11, 15, and 25 in the Enter Values field and add them into the Selected Values box one by one. Then select **OK**. Now, the records for the specified Customer IDs are displayed.

   ![Filter Query with User Defined Customer ID](https://devnet.logianalytics.com/hc/article_attachments/4404893826711/prmtr_app_fltrqry3.gif)

   To view the report with full data, select the **All** option and then select **OK** in the Enter Values dialog.

**Notes:**

* The parameter's data type must be set according to the field type and the manner in which you use the parameter. For example, if the field is a number, define a parameter to be Number type also.
* If you set the parameter format to be @ParameterName, to specify a String type value, your typed value should be without single quotations, for example, USA. Once you input a parameter value with single quotation marks, the quotation marks will be recognized as a part of the parameter value.

  However for the format :ParameterName, to specify a String type value, your typed value should be with single quotations, for example, 'USA'. If the data type is Number, the parameter value should be without quotes in both cases: 1234.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590221-Referencing-Parameters-in-a-Formula)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590241-Supplementing-WHERE-Portions)
