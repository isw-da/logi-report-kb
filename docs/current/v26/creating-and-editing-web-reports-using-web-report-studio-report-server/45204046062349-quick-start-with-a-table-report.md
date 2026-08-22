---
title: "Quick Start with a Table Report"
id: 45204046062349
section: "Creating and Editing Web Reports Using Web Report Studio Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45204046062349-Quick-Start-with-a-Table-Report
updated_at: 2026-04-30T14:11:04Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Quick Start With a Table Report 

This topic describes how you can create a web report using the quick start method. You just need to select data fields in a business view, and then Server generates a table report based on the fields. This saves time compared to typical report design with the report wizard. 

You can select a default page template in the Web Report Studio profile in advance, to apply it to the web reports that you create using the quick start method.

To create a web report using the quick start method:

- Do either of the following:
    
- In the Start Page of the Server Console, select Web Report in the Create category.

- On the Server Console, open the Resources page and select New > Web Report on the task bar.

Server displays Web Report Studio in a new tab or window, prompting you to select data for the new report.

- In the Select Catalog dialog box, select the catalog published to the server resource tree, which contains the data you want to use for the report. 

- Select OK.

- In the Select Data Source dialog box, select the required data source or dataset in the specified catalog from the Data Source drop-down list, or select Change Catalog to choose another catalog to use. Server lists all the business views in the selected data source or the business view of the dataset in the Resources box. 

- Select the business view for the report.

- In the right box, select the data fields you want to display in the report. You can select the Sort button  and the Search button  to sort and search for the required resources.
    

- Select OK. Server generates a table using the selected fields and opens it in Web Report Studio.
    

You can then manipulate the table and convert the table to a crosstab, chart, banded object, or another table. When inserting a summary column into the table, it inherits the properties of the nearest existing summary column (the summary column on its left has the higher priority). When there are not any existing summary columns in the table, Server applies the default properties to the newly added summary column.

You can also use URL command to directly create a web report using the quick start method.
