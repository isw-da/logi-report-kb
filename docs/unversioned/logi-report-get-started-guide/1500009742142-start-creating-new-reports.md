---
title: "Start Creating New Reports"
id: 1500009742142
section: "Logi Report Get Started Guide"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009742142-Start-Creating-New-Reports
updated_at: 2021-07-24T00:49:55Z
---

# Start Creating New Reports

[![](https://devnet.logianalytics.com/hc/article_attachments/4404880314007/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009769821-Open-Sample-Report-Templates)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404880314519/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009769801-Online-Help)

# Start Creating New Reports

Logi Report supports three types of reports: Page Report, Web Report, and Library Component. This topic introduces how you can create reports of each type in Designer.

In Logi Report, different report type serves different reporting requirements.

* Page reports are composed of one or more report tabs that are designed for the same or related purposes. Report developers can design, maintain, run and schedule these report tabs together or separately. Page reports are designed for paginated result sets as well as more complex reporting techniques such as pixel-perfect reporting.
* Web reports provide easier and faster report creation and design, faster report execution, streamlined customization and interactive presentation style using the latest Web technology.
* Library components or widgets, are charts, tables, crosstabs, control components and others, that are created and edited in Designer for use in dashboards.

## Enabling Data Sources

Designer requires access to your data sources to retrieve data for reports, so before you can create reports in Designer you need to set up connections to your data sources. Currently Designer provides you with the following methods to achieve this goal: via JDBC Connection, XML Connection, SOAP Web Service Connection, MongoDB Connection, HIVE Connection, JSON Connection, or Elasticsearch Connection, or by creating Hierarchical Data Source and User-Defined Data Source.

* After you set up a connection, you can create queries and business views based on data resources from the connection, and then use the queries and business views to create reports.
* You can use hierarchical data sources (HDS) and user-defined data sources (UDS) to create page reports directly.

## Creating a Page Report

1. Select **Logi Report Designer** in the Logi Report folder on the Start menu to start Designer.

   Designer displays the main window.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404880722455/newrpt_start.gif)
2. Select **Page Report** in the **Create** category of the Start Page.
3. In the Select Component for Page Report dialog box, decide whether to create the page report using business views (by default page reports are query-based).

   Since a page report cannot be empty, you also need to create a report tab in it when creating the page report.

   ![New Page Report dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404880722711/newrpt_page.gif)

   Designer provides you with the following component types to start a page report tab:

   * **Banded**  
     Select to create a report containing a vertical banded object.
   * **Table (Group Above)**  
     Select to create a report containing a table with group information above the detail panel.
   * **Table (Group Left)**  
     Select to create a report containing a table with group information left to the detail panel.
   * **Table (Group Left Above)**  
     Select to create a report containing a table with group information left above the detail panel.
   * **Summary Table**  
     Select to create a report containing a table with only group and summary information.
   * **Chart**  
     Select to create a report containing a chart.
   * **Crosstab**  
     Select to create a report containing a crosstab.
   * **Horizontal Banded**  
     Select to create a report containing a horizontal banded object.
   * **Mailing Label**  
     Select to create a report containing a banded object in the form of a mailing label layout.
   * **Tabular**  
     Select to create a report containing a tabular component.
   * **Blank**  
     Select to create a report with nothing in it.
4. Select the required component type and select **OK** to create the page report with its first report tab.

## Creating a Web Report

1. In Designer, select **File** > **New** > **Web Report**. Designer displays a blank web report with a tabular of one cell.
2. Select **Insert** > **Chart**. Designer displays the Create Chart dialog box.
3. In the **Data** screen, select a business view.

   ![Create Chart wizard - Data](https://devnet.logianalytics.com/hc/article_attachments/4404880722967/newrpt_wbrpt_bv.gif)
4. We use the default chart type and skip the **Type** screen.
5. Select **Next** twice to access the **Display** screen, then define the data in the chart.

   ![Create Chart wizard - Display](https://devnet.logianalytics.com/hc/article_attachments/4404885702935/newrpt_wbrpt_data.gif)
6. Select **Finish** to create the chart.

   ![Chart](https://devnet.logianalytics.com/hc/article_attachments/4404885703191/newrpt_wbrpt_rst.gif)
7. Select the **View** tab to preview the web report.

   ![Preview Chart](https://devnet.logianalytics.com/hc/article_attachments/4404880723223/newrpt_wbrpt_view.gif)

## Creating a Library Component

1. In Designer, select **File** > **New** > **Library Component**.
2. In the Select Component for Library Component dialog box, type a title for the library component and select the component you want to create in the library component.

   ![New Library Component dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404885703447/newrpt_lc.gif)
3. Select **OK**.
   * If you select **Blank**, Designer creates a blank library component. You can then use the Components and the Data panels to add components to the library component.
   * If you select a component type, Designer displays the corresponding wizard. Specify the data to display in the component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880314007/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009769821-Open-Sample-Report-Templates)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404880314519/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009769801-Online-Help)
