---
title: "Quick Start with a Table Report"
id: 1500009692882
section: "Web Report Studio Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692882-Quick-Start-with-a-Table-Report
updated_at: 2021-11-03T06:56:25Z
---

# Quick Start with a Table Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719021-An-Introduction-to-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719061-Creating-Web-Reports-Using-Wizard)

# Quick Start With a Table Report

There is a [quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009719001-Web-Report-Studio#Way) to create a web report: you just need to select data fields and then Logi JReport generates a table report based on the fields. This saves a lot of time compared to typical report design with the [report wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009719061-Creating-Web-Reports-Using-Wizard). After the report is opened in Web Report Studio, you can make use of the visualization toolbar to convert between data components and add more data components easily.

1. Do either of the following:
   * In the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009717601-Accessing-Logi-Report-Server-via-a-Web-Browser#Start), select **Web Report** in the Create category.
   * In the Logi JReport Server console, open the Resources page and select **New** > **Web Report** on the task bar.

   Web Report Studio is then displayed in a new tab or window, prompting you to select data for the new report.

   ![Select Catalog](https://devnet.logianalytics.com/hc/article_attachments/4412131375127/wbrpt_qckstrt_slctcat.gif)
2. In the [Select Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009716941-Select-Catalog) dialog, select the catalog published to the server resource tree, which contains the data you want to use for the report. Select **OK**.
3. In the [Select Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009690662-Select-Data-Source#Report) dialog, select the required data source in the specified catalog from the Data Source drop-down list (if necessary you can select the **Change Catalog** button to select another catalog to use). All the business views in the selected data source are then listed in the Resources box. Select the business view for the report, then in the right box check the checkboxes ahead of the data fields you want to display in the report. You can select ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4412112481943/btn_sort.gif) and ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4412131375383/btn_srch.gif) to sort and search the required resources.

   ![Select Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131375639/slctdtsrc.gif)
4. Select **OK**. A table is generated using the selected fields.

   ![Summary Table](https://devnet.logianalytics.com/hc/article_attachments/4412139482647/wbrpt_qckstrt_tbl.gif)

You can then [manipulate the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009692842-Manipulating-Data-Components#Table) and [convert the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009692842-Manipulating-Data-Components#ConvertVT) to a crosstab, chart, banded object or another table as required. However tables created in the quick start way have some special characteristics:

* If a summary column contains only one aggregate field, when you remove the aggregate field from the column, the whole column will be deleted.
* When inserting a summary column, it inherits the properties of the nearest existing summary column (the summary column on its left has the higher priority). When there aren't any existing summary columns, the default properties will be applied to the newly added summary column.

You can also use URL command to directly [create a web report in the quick start way](https://devnet.logianalytics.com/hc/en-us/articles/1500009719361-Creating-Reports#Quickstart).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719021-An-Introduction-to-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719061-Creating-Web-Reports-Using-Wizard)
