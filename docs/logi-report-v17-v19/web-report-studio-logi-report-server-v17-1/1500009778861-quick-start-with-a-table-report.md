---
title: "Quick Start with a Table Report"
id: 1500009778861
section: "Web Report Studio Logi Report Server v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778861-Quick-Start-with-a-Table-Report
updated_at: 2021-07-24T00:47:28Z
---

# Quick Start with a Table Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749982-An-Introduction-to-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750022-Creating-Web-Reports-Using-the-Wizard)

# Quick Start With a Table Report

This topic describes how you can [create a web report quickly](https://devnet.logianalytics.com/hc/en-us/articles/1500009778701-Web-Report-Studio#Way). You just need to select data fields and then Server generates a table report based on the fields. This saves a lot of time compared to typical report design with the [report wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009750022-Creating-Web-Reports-Using-the-Wizard).

After Server opens a report in Web Report Studio, you can make use of the visualization toolbar to convert between data components and add more data components easily.

1. Do either of the following:
   * In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009777061-Accessing-Logi-Report-Server-via-a-Web-Browser#Start) of the Server Console, select **Web Report** in the **Create** category.
   * In the Server Console, open the **Resources** page and select **New** > **Web Report** on the task bar.

   Server displays Web Report Studio in a new tab or window, prompting you to select data for the new report.

   ![Select Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404885305623/wbrpt_qckstrt_slctcat.gif)
2. In the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009748002-Select-Catalog-Dialog-Box-Properties) dialog box, select the catalog published to the server resource tree, which contains the data you want to use for the report.
3. Select **OK**.
4. In the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009776221-Select-Data-Source-Dialog-Box-Properties#Report) dialog box, select the required data source in the specified catalog from the **Data Source** drop-down list, or select **Change Catalog** to select another catalog to use. Server lists all the business views in the selected data source in the **Resources** box.
5. Select the business view for the report.
6. In the right box select the data fields you want to display in the report. You can select the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880135447/btn_sort.gif) and the Search button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404880135831/btn_srch.gif) to sort and search for the required resources.

   ![Select Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885306135/slctdtsrc.gif)
7. Select **OK**. Server generates a table using the selected fields and opens it in Web Report Studio.

   ![Summary Table](https://devnet.logianalytics.com/hc/article_attachments/4404885306391/wbrpt_qckstrt_tbl.gif)

You can then [manipulate the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report#Table) and [convert the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009750142-Manipulating-Data-Components-in-Web-Report#ConvertVT) to a crosstab, chart, banded object, or another table. When inserting a summary column into the table, it inherits the properties of the nearest existing summary column (the summary column on its left has the higher priority). When there are not any existing summary columns in the table, Server applies the default properties to the newly added summary column.

You can also use URL command to directly [create a web report in the quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009750322-Creating-Reports-via-URL#Quickstart).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749982-An-Introduction-to-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009750022-Creating-Web-Reports-Using-the-Wizard)
