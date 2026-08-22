---
title: "Filtering a Parameter with Another Parameter"
id: 1500009568642
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568642-Filtering-a-Parameter-with-Another-Parameter
updated_at: 2021-07-24T05:54:29Z
---

# Filtering a Parameter with Another Parameter

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590061-Applying-RLS-to-a-Parameter)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590181-Dynamically-Grouping-Sorting-Report-Data)

# Filtering a Parameter with Another Parameter

You can use the value of one parameter to filter another one. In this way you can create your own cascading parameters such as using pCountry to filter the values returned by a parameter listing available states. The following examples show you the two methods that you can use to achieve this purpose.

**Method 1** (Use this method when the SQL needed to select the parameter values is very simple.)

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source node.
3. Right-click the **Parameters**  node and then select **New Parameter**. The New Parameter dialog appears.
4. Enter **CasParam** in the Name field, select **Bind with Cascading Columns** from the Value Setting drop-down list, and then select **Customers** of the Tables type from the Data Source drop-down list.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a parameter row, select **Region** as the Bind Column and Display Column, and then select in the Parameter cell to create the parameter in the cascading group.
6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add another parameter row, select **Country** as the Bind Column and Display Column, and then select in the Parameter cell.
7. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add one more parameter row, select **City** as the Bind Column and Display Column, select in the Parameter cell, and then select **OK** in the dialog.

   ![New Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404893826967/prmtr_app_fltrprm3.gif)
8. In the same data source, [create a query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592461-Creating-a-Query) CustomersInfo on the table Customers and select all the fields in the table.
9. Filter the records of the query by adding a condition as follows in the Search Condition dialog (for details, see [Filtering with the Filter Format](https://devnet.logianalytics.com/hc/en-us/articles/1500009570722-Filtering-the-Fields-of-a-Query#Filter)):

   ![Filter Condition](https://devnet.logianalytics.com/hc/article_attachments/4404893827223/prmtr_app_fltrprm1.gif)
10. [Create a page report with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the query, and have the fields Customer Name, City, Country and Region displayed in the report.
11. View the report and the Enter Parameter Values dialog appears.
12. From the region drop-down list, select a region, then only the countries in the selected region will be displayed in the country drop-down list. Choose a country from the list, and then only the cities in the selected country will be displayed in the city drop-down list.

    ![Enter Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4404893827479/prmtr_app_fltrprm2.gif)
13. Select **OK**. You will now find that only the specified records are shown.

**Method 2** (Use this method when you need more customized SQL to show the correct values.)

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the desired data source node.
3. Right-click the **Parameters**  node and then select **New Parameter**.
4. Create a parameter named ParamRegion, select **Bind with Single Column** from the Value Setting drop-down list, select **Tables and Views** from the Source drop-down list, select **Region** as the Bind Column and Display Column. Then in the value cell of the Import SQL option, you can see the following statement:

   `SELECT DISTINCT CUSTOMERS.REGION FROM CUSTOMERS`

   ![New Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404889301271/prmtr_app_fltrprm4.gif)
5. Create another parameter named ParamCountry. Bind it with the column Country, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell of Import SQL and edit its SQL statement as follows:

   `SELECT DISTINCT CUSTOMERS.COUNTRY FROM CUSTOMERS WHERE (Customers.Region=@ParamRegion and Customers.YTDSALES > 0 )`
6. Create one more parameter named ParamCity. Bind it with the column City, and then edit its SQL statement as follows:

   `SELECT DISTINCT CUSTOMERS.City FROM CUSTOMERS WHERE (Customers.Country=@ParamCountry and Customers.YTDSALES > 0 )`
7. In the same data source, create a query CustomersInfo on the table Customers and select all the fields in the table, and filter the records of the query by adding a condition as follows:

   `CUSTOMERS.CITY=@ParamCity`
8. [Create a page report with a table in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) based on the query, and have the fields Customer Name, City, Country and Region displayed in the report.
9. View the report. In the Enter Parameter Values dialog, you can use the value of ParamRegion to filter the value of ParamCounty, and use the value of ParamCounty to filter the value of ParamCity. You will not see any countries and cities where their are no sales.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590061-Applying-RLS-to-a-Parameter)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590181-Dynamically-Grouping-Sorting-Report-Data)
