---
title: "Quick Start with a Table Report"
id: 1500009751621
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009751621-Quick-Start-with-a-Table-Report
updated_at: 2021-07-25T07:18:32Z
---

# Quick Start with a Table Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751441-An-Introduction-to-Business-Views)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard)

# Quick Start With a Table Report

You can [create a web report quickly](https://devnet.logianalytics.com/hc/en-us/articles/1500009724642-Web-Report-Studio#Way): you just need to select data fields and then Web Report Studio generates a table report based on the fields. This saves a lot of time compared to typical report design with the [report wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard). After the report is opened in Web Report Studio, you can make use of the visualization toolbar to convert between data components and add more data components easily.

1. Do either of the following:
   * In the [Logi Report Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009749881-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Web Report** in the Create category.
   * In the Logi Report Server console, open the Resources page and select **New** > **Web Report** on the task bar.

   Web Report Studio is then displayed in a new tab or window, prompting you to select data for the new report.

   ![Select Catalog](https://devnet.logianalytics.com/hc/article_attachments/4404936713111/wbrpt_qckstrt_slctcat.gif)
2. In the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009722202-Select-Catalog) dialog box, select the catalog published to the server resource tree, which contains the data you want to use for the report. Select **OK**.
3. In the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009722222-Select-Data-Source#Report) dialog box, select the required data source in the specified catalog from the Data Source drop-down list (you can select the **Change Catalog** button to select another catalog to use). All the business views in the selected data source are then listed in the Resources box.
4. Select the business view for the report, then in the right box select the data fields you want to display in the report. You can select ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404936713367/btn_sort.gif) and ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404936713623/btn_srch.gif) to sort and search for the required resources.

   ![Select Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936713879/slctdtsrc.gif)
5. Select **OK**. A table is generated using the selected fields.

   ![Summary Table](https://devnet.logianalytics.com/hc/article_attachments/4404942445335/wbrpt_qckstrt_tbl.gif)

You can then [manipulate the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components#Table) and [convert the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components#ConvertVT) to a crosstab, chart, banded object or another table as required. However tables created in the quick start way have some special characteristics:

* If a summary column contains only one aggregate field, when you remove the aggregate field from the column, the whole column will be deleted.
* When inserting a summary column, it inherits the properties of the nearest existing summary column (the summary column on its left has the higher priority). When there aren't any existing summary columns, the default properties will be applied to the newly added summary column.

You can also use URL command to directly [create a web report in the quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009751681-Creating-Reports#Quickstart).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009751441-An-Introduction-to-Business-Views)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard)
