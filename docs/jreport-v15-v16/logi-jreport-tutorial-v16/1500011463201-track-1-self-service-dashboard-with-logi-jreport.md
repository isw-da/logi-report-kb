---
title: "Track 1: Self-service Dashboard with Logi JReport"
id: 1500011463201
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011463201-Track-1-Self-service-Dashboard-with-Logi-JReport
updated_at: 2021-07-24T10:39:36Z
---

# Track 1: Self-service Dashboard with Logi JReport

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463301-Part-III-End-User-Experience) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431282-Track-2-Performing-Visual-Analysis-)

# Track 1: Self-service Dashboard with Logi JReport

Dashboard is a new way of information delivery. Users can create, edit and browse dashboards from the Logi JReport Server console using JDashboard. With pre-built library components, users can freely choose the objects they want to display in a dashboard, without having to know how these objects were created, what data sources to use, what styles to set, etc. Report data components and Visual Analysis templates can also be inserted in dashboards directly. A dashboard can hold multiple library components so that when browsing the dashboard users are able to see multiple data aspects. Within a dashboard, library components are able to communicate with each other via the message mechanism. This allows actions such as common filters to be applied to all the components of a dashboard even when coming from different data sources so as to achieve data synchronization. Furthermore, users can run reports and Visual Analysis templates directly by invoking Web/Page Report Studio and Visual Analysis inside JDashboard, without having to switch to the server console. This allows analyzing with different tools in just one JDashboard window.

This track contains the following tasks:

* [Task 1: Create a Dashboard and Insert Library Components](#Task1)
* [Task 2: Insert a KPI](#Task2)
* [Task 3: Insert a Report Component](#Task3)
* [Task 4: Synchronize the Components](#Task4)
* [Task 5: Use a Slider to Filter on Quantity](#Task5)
* [Task 6: Insert a Third Party Gadget (Stock Widget)](#Task6)
* [Task 7: Export the Library Components](#Task7)
* [Task 8: Use the Configuration Panel to Change Parameter Values](#Task8)
* [Task 9: Share Parameters Among Components](#Task9)
* [Task 10: Run a Report in JDashboard](#Task10)
* [Task 11: Set a Dashboard as the Server Home Page](#Task11)

**Note:** A JDashboard license for Logi JReport Server is required in order to perform this track. If you do not have the license, please contact your Logi Analytics account manager to obtain it first.

## Task 1: Create a Dashboard and Insert Library Components

1. In the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011431562-Lesson-1-Starting-Logi-JReport-Server), select **Dashboard** in the Create category. JDashboard is then displayed in a new window tab, with a blank dashboard created.

   ![Create Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404901043863/dshbd_nw.gif)
2. In the Resources panel, expand the **Component Library** > **Public Components** > **SampleReports** folder. Drag **Sales by Category.lc** and **Crosstab.lc** to the dashboard body as follows:

   ![Insert Library Components to Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404901044119/dshbd_lc.gif)
3. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404909066647/btn_sv.gif) on the toolbar.
4. In the Save As dialog, replace Dashboard 1 with **Products** in the File Name text box, then select **OK** to save the dashboard into the My Reports folder in the server resource tree.

## Task 2: Insert a KPI

KPIs (Key Performance Indicators) help in business performance management. They are based on predefined functions and can be further enriched with trend charts. You can create KPIs in Logi JReport Designer or Web Report Studio and use them for deeper data insights in dashboards.

In this task, we will insert a pre-built KPI to the dashboard.

1. From the Component Library > Public Components > SampleReports folder of the Resources panel, drag **Sales YTD.lc** to the dashboard body and place it on the right of the chart.

   ![Insert KPI to Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404909066903/dshbd_kpi.gif)
2. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404909066647/btn_sv.gif) to save the dashboard.

## Task 3: Insert a Report Component into Dashboard

Report components created from business views can also be inserted in dashboards directly.

1. In the Resources panel, go to the **Reports** > **Public Reports** > **SampleReports** folder, expand **Shipment Status Report.wls** and drag **TableComp** to the dashboard body below the crosstab.

   ![Insert Report Component to Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404901044503/dshbd_rptcom.gif)
2. Select ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404901044759/btn_cls.gif) on the top right of the Resources panel to close the panel.
3. Select ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404909066647/btn_sv.gif) on the toolbar to save the dashboard.

## Task 4: Synchronize the Components

In this task, we want to select any value of the Category field in the crosstab to automatically update the chart. This is achieved by delivering a filter synchronization message between the two library components.

1. Right-click on any Category value in the crosstab column header, Blends for example, and select **Send Sync** > **Filter** from the shortcut menu.

   ![Define Send Sync](https://devnet.logianalytics.com/hc/article_attachments/4404901045015/dshbd_snd.gif)
2. The chart automatically receives the synchronization message because it is created based on the same business view as the crosstab and contains the field Category too. To view details of the message, right-click the chart and select **Receive Sync**. The filter message is shown in the Receive Sync dialog. Close the dialog.

   ![Define Receive Sync](https://devnet.logianalytics.com/hc/article_attachments/4404901045271/dshbd_rcv.gif)
3. Select any value in the crosstab column header, for example Bold. The chart is filtered to show data of the Bold category only after it receives the synchronization message.

   You may find that the crosstab is also filtered. This is because at report design time, the library component designer has predefined to make it receive a filter message too. You can right-click on the crosstab and select **Receive Sync** to view the details if you want.

   ![Synchronize Components](https://devnet.logianalytics.com/hc/article_attachments/4404909067159/dshbd_sync.gif)
4. We will remove the filters from the components. Select the **Clear Filters** button ![Clear Filters button](https://devnet.logianalytics.com/hc/article_attachments/4404909067415/btn_clrfltr.gif) on the toolbar.
5. Select ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404909066647/btn_sv.gif) on the toolbar to save the dashboard.

## Task 5: Use a Slider to Filter on Quantity

1. Select ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404901045527/btn_show.gif) on the toolbar to display the Resources panel, then from the Toolbox node, drag **Filter Control** to the dashboard body on the right of the crosstab.
2. In the Insert Filter Control dialog, input **Sales Quantity** in the Title text box and select **Range Slider** as the control type.
3. Expand the Select Fields drop-down list. The business views used by the data components in the dashboard are listed. Here we only want to filter data components that use WorldWideSalesBV. Check **Quantity** in WorldWideSalesBV. Then select **OK** to insert the slider.

   ![Insert Slider Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404909067671/dshbd_sldrdlg.gif)
4. Close the Resources panel.

Next, we will use the slider to show the data for Quantity between 2000 and 8000 only.

1. Drag the left arrow to set a minimum range 1973 and the right
   arrow to set a maximum range 8031. The
   chart and crosstab are filtered. The other components use different business views so they are not changed.

   ![Filter by Silder](https://devnet.logianalytics.com/hc/article_attachments/4404901045783/dshbd_sldr.gif)
2. Save the dashboard.

## Task 6: Insert a Third Party Gadget (Stock Widget)

1. Select ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404901045527/btn_show.gif) on the toolbar to display the Resources panel, then drag **URL Frame** from the Toolbox node to the dashboard body beside the KPI. The Insert URL Frame dialog is displayed.
2. In the Title text field, input **My Stocks**, and in the URL text box, type in **http://edulifeline.com/includes/stocks\_widget/**.

   ![Insert URL Frame](https://devnet.logianalytics.com/hc/article_attachments/4404901046039/dshbd_url.gif)
3. Select **OK**. The specified web page is then inserted into the dashboard.

   ![Insert Web Page](https://devnet.logianalytics.com/hc/article_attachments/4404909067927/dshbd_urlrst.gif)
4. Close the Resources panel and save the dashboard.

## Task 7: Export the Library Components

1. Select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404901046295/btn_expt.gif) on the toolbar. The Export dialog appears.
2. Select **Customize Layout** from the Layout drop-down list.

By default, all the exportable library components are arranged using a tabular style according to their positions in the dashboard in the Design tab on the right. Each tabular cell can hold at most one component. Sliders and gadgets cannot be exported so they are not available here.
Next, we will change the layout of the components a little bit by moving the KPI closer to the left.

1. Select in the tabular cell containing the chart to select the cell. Then select the **Vertical Split** button ![Vertical Split button](https://devnet.logianalytics.com/hc/article_attachments/4404901046551/btn_vtclsplt.gif) on the toolbar to split the cell into two. The chart is positioned in the left cell.
2. Right-click anywhere in the cell containing the KPI, select **Remove** from the shortcut menu.

   ![Remove KPI](https://devnet.logianalytics.com/hc/article_attachments/4404909068183/dshbd_exptrmv.gif)
3. Drag **Sales YTD** (the KPI) from the Resources box to the blank cell right to the chart. The KPI will be moved closer to the chart.

   ![Add KPI right to the chart](https://devnet.logianalytics.com/hc/article_attachments/4404909068439/dshbd_exptaddkpi.gif)

When exporting tables and crosstabs, by default only the data currently displayed in the dashboard will be exported. In our dashboard the table contains several pages and we can view only one page at a time, that is to say only the currently displayed page will be exported. We want to get the full data of the table in the exported result so we need a further setting.

1. Right-click in the cell holding the table, select **Filter** from the shortcut menu, then choose the **All** option and select **OK**.
2. Select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404901046295/btn_expt.gif) on the toolbar. In the Export dialog,
   keep the default settings to export the dashboard to a PDF file.

   ![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909068695/dshbd_expt.gif)
3. Select **OK**. The exporting process begins. When finished, you can open the PDF file to view the result.
4. Close the Export dialog and save the dashboard.

## Task 8: Use the Configuration Panel to Change Parameter Values

When a library component uses parameters and its configuration panel is enabled, you can make use of the configuration panel to change its parameter values.

1. On the table, place the mouse anywhere on the title bar, then select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404909068951/btn_more.gif) that appears on the title bar and select **Edit Setting** from the drop-down list to display the configuration panel.

   ![Display Configuration Panel](https://devnet.logianalytics.com/hc/article_attachments/4404909069207/dshbd_cnfg.gif)
2. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901046807/btn_entrvlu.gif) in the value box for the Shipper parameter. The Enter Values dialog appears.
3. Check the **Custom** radio button, select **UBS Uniform Logistics** and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901047063/btn_add.gif) to add it to the right box, then select **OK**.

   ![Enter Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4404901047319/dshbd_entrvlue.gif)
4. Select **OK** in the configuration panel. The table now shows records of this shipper only.

   ![Apply Parameter Values to Table](https://devnet.logianalytics.com/hc/article_attachments/4404901047575/dshbd_chgprm.gif)
5. Save the dashboard.

## Task 9: Share Parameters Among Components

When two or more library components in a dashboard contain parameters that meet the following cases, the parameters can be shared among them. After sharing parameters, you just need to provide values to one group of the parameters and all related components will be able to receive them.

* The numbers of the parameters in each library component are the same.
* According to the parameter order in each library component, the orders of the parameter data types are the same. For example, the parameter data types in a component are String, Number, and Boolean. If there is another component in which the parameter data types are also String, Number, and Boolean, the two components fulfill the condition of the same parameter data types.
* It is up to users to make sure the to-be-shared parameters contain some common values.

In this task, we will insert two library components having similar parameters and see the difference between before and after the parameters are shared.

1. Select ![Add Dashboard button](https://devnet.logianalytics.com/hc/article_attachments/4404909069463/btn_adddsh.gif) on the dashboard title bar to add a new dashboard. A new tab is created, labeled Dashboard 2.
2. Expand **Component Library** > **Public Components** > **SampleReports** and drag **Shipment Status Overview.lc**  and **Shipments by Status.lc** one by one to the dashboard body. Close the Resources panel.
3. Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404901047831/btn_menu.gif) on the toolbar and select **Share Parameter**. The displayed dialog shows that the two library components have shared parameters. Close the dialog.

   ![Set Share Parameters](https://devnet.logianalytics.com/hc/article_attachments/4404901048087/dshbd_prmshare.gif)
4. Select the **Enter Parameter Values** button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404909069719/btn_prm.gif) on the toolbar. The Enter Parameter Values dialog lists the following parameters. Close the dialog.

   ![Shared Parameters](https://devnet.logianalytics.com/hc/article_attachments/4404901048343/dshbd_prmsharevlu.gif)

Next we will remove the parameter share between the two components to see how many parameters we need to specify.

1. Select ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404901047831/btn_menu.gif) on the toolbar and select **Share Parameter**. In the displayed dialog, select either component and select the **Cancel Share** button on the top right, then select **OK**.
2. Select ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404909069719/btn_prm.gif) on the toolbar to access the Enter Parameter Values dialog again. Now it lists separate pairs of the Start Date, End Date, and Territory/Shipper parameters used by the two library components. Close the dialog.

   ![Separated Parameters](https://devnet.logianalytics.com/hc/article_attachments/4404901048599/dshbd_prmunsharevlu.gif)
3. Select ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404909066647/btn_sv.gif) on the toolbar to save the dashboard as **Shipment**.

## Task 10: Run a Report in JDashboard

A report can run in the corresponding Web/Page Report Studio within JDashboard. In this task we will run a web report inside JDashboard without going to the server resource tree on the server console.

1. Keep the Shipment dashboard active.
2. From the Resources panel, drag **Sales Detail Report.wls** in the Reports > Public Reports > SampleReports folder to the dashboard body, then hide the panel.
3. The report is loaded into a separate tab via Web Report Studio within JDashboard.

   ![Run Report in JDashboard](https://devnet.logianalytics.com/hc/article_attachments/4404909069975/dshbd_runrpt.gif)

## Task 11: Set a Dashboard as the Server Home Page

1. In the web browser, change from the JDashboard tab to the Logi JReport Start Page tab.
2. Select **My Profile** in the Manage category.
3. In the My Profile > Customize Server Preferences > General tab, check the **Use a Dashboard** checkbox for the Home Page option, then select **OK**. Select **OK** in the prompt message.

   ![Set Home Page](https://devnet.logianalytics.com/hc/article_attachments/4404901048855/dshbd_dshhm.gif)
4. Select **Resources** on the system toolbar, then go to the **My Reports** folder.
5. Select **Shipment.dsh** in the folder, the dashboard is loaded into a new JDashboard window.
6. Select ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404901047831/btn_menu.gif) on the toolbar and you can see Set as Server Home is enabled on the menu list. Select the option to set the Shipment dashboard as the server home page.
7. Refresh the Logi JReport Server console page and a Home label is added beside Resources on the system toolbar. Select it and you can access the Shipment dashboard immediately.

   ![Use Dashboard as Home Page](https://devnet.logianalytics.com/hc/article_attachments/4404901049111/dshbd_srvhome.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500011463301-Part-III-End-User-Experience) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011431282-Track-2-Performing-Visual-Analysis-)
