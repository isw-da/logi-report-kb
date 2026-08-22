---
title: "Start Creating New Reports"
id: 1500010028362
section: "Logi JReport Get Started Guide v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028362-Start-Creating-New-Reports
updated_at: 2021-07-24T10:39:36Z
---

# Start Creating New Reports

[![](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062941-Open-Sample-Report-Templates)

# Start Creating New Reports

Logi JReport supports three types of reports: Page Report, Web Report, and Library Component. All serve different reporting requirements:

* Page reports are composed of one or more report tabs that are designed for the same or related purposes. Report developers can design, maintain, run and schedule these report tabs together or separately. Page reports are designed for paginated result sets as well as more complex reporting techniques such as pixel-perfect reporting.
* Web reports provide easier and faster report creation and design, faster report execution, streamlined customization and interactive presentation style using the latest Web technology.
* Library components or widgets, are charts, tables, crosstabs, control components and others, that are created and edited in Logi JReport Designer for use in dashboards.

[More information about each report type >>](https://devnet.logianalytics.com/hc/en-us/articles/1500010070781-Designing-Your-Reports)

## Enabling Data Sources

Logi JReport Designer requires access to your data sources to retrieve data for reports, so before you can create reports in Logi JReport Designer you need to set up connections to your data sources. Currently the following methods are provided for you to achieve this goal: via JDBC Connection, XML Connection, SOAP Web Service Connection, MongoDB Connection, HIVE Connection, JSON Connection, Elasticsearch Connection, or by creating Hierarchical Data Source and User Defined Data Source.

* When a connection is set up, you can create queries and business views based data resources from the connection, and then use the queries and business views to create reports.
* Hierarchical data sources (HDS) and user defined data sources (UDS) can be used to create page reports directly.

[More information about data source connections >>](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections)

## Creating a Page Report

1. Select **JReport Designer** in the JReport folder on the Start menu to start Logi JReport Designer.
2. On the Start Page, select **Page Report** in the Create category.
3. In the Select Component for Page Report dialog, decide whether to create the page report using business views (by default page reports are query based).

   Since a page report cannot be empty, you will also need to create a report tab in it when creating the page report.

   ![New Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901351959/newrpt_page.gif)

   Logi JReport provides you with the following component types to start a page report tab:

   * **Banded**  
      Creates a report containing a vertical banded object.
   * **Table (Group Above)**  
      Creates a report containing a table with group information above the detail panel.
   * **Table (Group Left)**  
     Creates a report containing a table with group information left to the detail panel.
   * **Table (Group Left Above)**  
     Creates a report containing a table with group information left above the detail panel.
   * **Summary Table**  
     Creates a report containing a table with only group and summary information.
   * **Chart**  
     Creates a report containing a chart.
   * **Crosstab**  
     Creates a report containing a crosstab.
   * **Horizontal Banded**  
     Creates a report containing a horizontal banded object.
   * **Mailing Label**  
     Creates a report containing a banded object in the form of a mailing label layout.
   * **Tabular**  
     Creates a report containing a tabular component.
   * **Blank**  
     Creates a report with nothing in it.
4. Select the required component type and select **OK** to create the page report with its first report tab.

## Creating a Web Report

1. In Logi JReport Designer, select **File** > **New** > **Web Report**. A blank web report with a tabular of one cell is displayed.
2. Select **Insert** > **Chart**. The Create Chart wizard is displayed.
3. Select a business view in the Data screen.

   ![Create Chart wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404909298071/newrpt_wbrpt_bv.gif)
4. We will use the default chart type and skip the Type screen. Select **Next** twice to access the Display screen. Define the data in the chart.

   ![Create Chart wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404909298327/newrpt_wbrpt_data.gif)
5. Select **Finish** to create the chart.

   ![Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901352215/newrpt_wbrpt_rst.gif)
6. Select the **View** tab to preview the web report.

   ![Preview Chart](https://devnet.logianalytics.com/hc/article_attachments/4404901352471/newrpt_wbrpt_view.gif)

## Creating a Library Component

1. In Logi JReport Designer, select **File** > **New** > **Library Component**.
2. In the Select Component for Library Component dialog, input a title for the library component and select the component you want to create in the library component.

   ![New Library Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901352727/newrpt_lc.gif)
3. Select **OK**.
   * If Blank is selected as the layout, a library component which is blank will be created. You can then use the Components and the Data panels to add components to the library component.
   * If you select a component type, the corresponding wizard is displayed. Specify the settings according to your requirements.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010062941-Open-Sample-Report-Templates)
