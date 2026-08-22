---
title: "Track 1: Self-service Dashboard with Logi Report"
id: 1500010056482
section: "Logi Report Tutorial v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056482-Track-1-Self-service-Dashboard-with-Logi-Report
updated_at: 2021-07-23T19:14:26Z
---

# Track 1: Self-service Dashboard with Logi Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093601-Part-IV-End-User-Experience)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093641-Track-2-Performing-Visual-Analysis-)

# Track 1: Self-service Dashboard with Logi Report

Dashboard is a new way of information delivery. You can create, edit, and browse dashboards from the Server Console using JDashboard. With pre-built library components, you can freely choose the objects you want to display in a dashboard, without having to know how these objects were created, what data sources to use, what styles to set, and so on. A dashboard can hold multiple library components so that when browsing the dashboard, you are able to see multiple data aspects. Within a dashboard, library components are able to communicate with each other via the message mechanism. This enables actions such as common filters to be applied to all the components of a dashboard even when coming from different data sources so as to achieve data synchronization. Furthermore, you can run reports and Visual Analysis templates directly by invoking Web Report Studio/Page Report Studio and Visual Analysis inside JDashboard without having to switch to the Server Console, which enables analyzing with different tools in just one JDashboard window.

This track contains the following tasks:

* [Task 1: Create a Dashboard and Insert Library Components](#Task1)
* [Task 2: Insert a KPI](#Task2)
* [Task 3: Insert a Report Component](#Task3)
* [Task 4: Synchronize the Components](#Task4)
* [Task 5: Use a Slider to Filter on Quantity](#Task5)
* [Task 6: Insert a Third-Party Gadget (Stock Widget)](#Task6)
* [Task 7: Export the Library Components](#Task7)
* [Task 8: Use the Configuration Panel to Change Parameter Values](#Task8)
* [Task 9: Share Parameters Among Components](#Task9)
* [Task 10: Run a Report in JDashboard](#Task10)
* [Task 11: Set a Dashboard as the Server Home Page](#Task11)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) A JDashboard license for Server is required in order to perform this track. If you do not have the license, please contact your Logi Analytics account manager to obtain it first.

## Task 1: Create a Dashboard and Insert Library Components

1. In the [Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500010093101-Lesson-1-Starting-Server) of the Server Console, select **Dashboard** in the **Create** category.

   Server creates a blank dashboard in JDashboard in a new window tab.

   ![Create Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404857094039/dshbd_nw.gif)
2. In the **Resources** panel, expand the **Component Library** > **Public Components** > **SampleReports** folder. Drag **Sales by Category.lc** and **Crosstab.lc** to the dashboard body as follows:

   ![Insert Library Components to Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404857094423/dshbd_lc.gif)
3. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404857094679/btn_sv.gif) on the toolbar.
4. In the Save As dialog box, replace Dashboard 1 with **Products** in the **File Name** text box, then select **OK** to save the dashboard into the My Reports folder in the server resource tree.

## Task 2: Insert a KPI

KPIs (Key Performance Indicators) help in business performance management. They are based on predefined functions and can be further enriched with trend charts. You can create KPIs in Designer or Web Report Studio and use them for deeper data insights in dashboards.

In this task, we insert a pre-built KPI to the dashboard.

1. From the Component Library > Public Components > SampleReports folder in the Resources panel, drag **Sales YTD.lc** to the dashboard body and place it on the right of the chart.

   ![Insert KPI to Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404857094935/dshbd_kpi.gif)
2. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404857094679/btn_sv.gif) to save the dashboard.

## Task 3: Insert a Report Component

You can also insert report components that use business views in dashboards directly.

1. In the Resources panel, go to the **Reports** > **Public Reports** > **SampleReports** folder, expand **Shipment Status Report.wls** and drag **TableComp** to the dashboard body below the crosstab.

   ![Insert Report Component to Dashboard](https://devnet.logianalytics.com/hc/article_attachments/4404848717463/dshbd_rptcom.gif)
2. Select the **Close** button ![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404848717847/btn_cls.gif) on the top right of the Resources panel to close the panel.
3. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404857094679/btn_sv.gif) on the toolbar to save the dashboard.

## Task 4: Synchronize the Components

In this task, we want to select any value of the Category field in the crosstab to automatically update the chart. This is achieved by delivering a filter synchronization message between the two library components.

1. Right-click on any **Category** value in the crosstab row header, **Blends** for example, and select **Send Sync** > **Filter** from the shortcut menu.

   ![Define Send Sync](https://devnet.logianalytics.com/hc/article_attachments/4404857095703/dshbd_snd.gif)
2. The chart automatically receives the synchronization message because it uses the same business view as the crosstab and contains the field Category too. To view details of the message, right-click the chart and select **Receive Sync**. JDashboard displays the filter message in the Receive Sync dialog box. Close the dialog box.

   ![Define Receive Sync](https://devnet.logianalytics.com/hc/article_attachments/4404857096087/dshbd_rcv.gif)
3. Select any value in the crosstab row header, for example **Bold**. JDashboard filters the chart to show data of the Bold category only after it receives the synchronization message.

   You may find that JDashboard filters the crosstab at the same time. This is because at report design time, the library component designer has predefined to make it receive a filter message too. You can right-click on the crosstab and select **Receive Sync** to view the details if you want.

   ![Synchronize Components](https://devnet.logianalytics.com/hc/article_attachments/4404848718359/dshbd_sync.gif)
4. We want to remove the filter from the chart. Select the **Clear Filters** button ![Clear Filters button](https://devnet.logianalytics.com/hc/article_attachments/4404848718871/btn_clrfltr.gif) on the toolbar.
5. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404857094679/btn_sv.gif) on the toolbar to save the dashboard.

## Task 5: Use a Slider to Filter on Quantity

1. Select the **Show Resources** button ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404848719383/btn_show.gif) on the toolbar to display the Resources panel, then from the **Toolbox** node, drag **Filter Control** to the dashboard body on the right of the crosstab.
2. In the Insert Filter Control dialog box, type **Sales Quantity** in the **Title** text box and select **Range Slider** as the control type.
3. Expand the **Select Fields** drop-down list. It contains the business views that the data components in the dashboard use. Here we only want to filter data components which use WorldWideSalesBV. Select **Quantity** in WorldWideSalesBV, then select **OK** to insert the slider.

   ![Insert Slider Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404857096471/dshbd_sldrdlg.gif)
4. Close the Resources panel.

Next, we use the slider to show the data for Quantity between 2000 and 8000 only.

1. Drag the left arrow to set a minimum range 1973 and the right arrow to set a maximum range 8031. JDashboard filters the chart and crosstab. The other components use different business views so JDashboard does not filter them.

   ![Filter by Silder](https://devnet.logianalytics.com/hc/article_attachments/4404857096727/dshbd_sldr.gif)
2. Save the dashboard.

## Task 6: Insert a Third-Party Gadget (Stock Widget)

1. Select the **Show Resources** button ![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404848719383/btn_show.gif) on the toolbar to display the Resources panel, then drag **URL Frame** from the Toolbox node to the dashboard body beside the KPI. JDashboard displays the Insert URL Frame dialog box.
2. In the **Title** text box, type **My Stocks**, and in the **URL** text box, type **http://edulifeline.com/includes/stocks\_widget/**.

   ![Insert URL Frame](https://devnet.logianalytics.com/hc/article_attachments/4404857096983/dshbd_url.gif)
3. Select **OK** to insert the specified web page into the dashboard.

   ![Insert Web Page](https://devnet.logianalytics.com/hc/article_attachments/4404848719767/dshbd_urlrst.gif)
4. Close the Resources panel and save the dashboard.

## Task 7: Export the Library Components

1. Select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404857097367/btn_expt.gif) on the toolbar. JDashboard displays the Export dialog box.
2. Select **Customize Layout** from the **Layout** drop-down list.

By default, JDashboard arranges all the exportable library components using a tabular style according to their positions in the dashboard in the Design tab on the right. Each tabular cell can hold at most one component. Sliders and gadgets cannot be exported so they are not available here.
Next, we change the layout of the components a little bit by moving the KPI closer to the left.

1. Select in the tabular cell containing the chart to select the cell.
2. Select the **Vertical Split** button ![Vertical Split button](https://devnet.logianalytics.com/hc/article_attachments/4404857097751/btn_vtclsplt.gif) on the toolbar to split the cell into two. JDashboard places the chart in the left cell.
3. Right-click anywhere in the cell containing the KPI, select **Remove** from the shortcut menu.

   ![Remove KPI](https://devnet.logianalytics.com/hc/article_attachments/4404848720023/dshbd_exptrmv.gif)
4. Drag **Sales YTD** (the KPI) from the Resources box to the blank cell right to the chart and move it closer to the chart.

   ![Add KPI right to the chart](https://devnet.logianalytics.com/hc/article_attachments/4404857098007/dshbd_exptaddkpi.gif)

When exporting tables and crosstabs, by default JDashboard only exports the data currently displayed in the dashboard. In our dashboard, the table contains several pages and we can view only one page at a time, that is to say, we get only the currently displayed page in the exported result. However, we want to get the full data of the table in the exported result, so we need a further setting.

1. Right-click in the cell holding the table and select **Filter** from the shortcut menu.
2. In the Filter dialog box, select the **All** option and select **OK**.
3. Select the **Export** button ![Export button](https://devnet.logianalytics.com/hc/article_attachments/4404857097367/btn_expt.gif) on the toolbar.
4. In the Export dialog box,
   keep the default settings to export the dashboard to a PDF file.

   ![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/4404848720279/dshbd_expt.gif)
5. Select **OK**. The exporting process begins. When it finishes, you can open the PDF file to view the result.
6. Close the Export dialog box and save the dashboard.

## Task 8: Use the Configuration Panel to Change Parameter Values

When a library component uses parameters and its configuration panel is enabled, you can make use of the configuration panel to change its parameter values.

1. On the table, place the mouse anywhere on the title bar, then select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404848720791/btn_more.gif) that JDashboard displays on the title bar and select **Edit Setting** from the drop-down list to display the configuration panel.

   ![Display Configuration Panel](https://devnet.logianalytics.com/hc/article_attachments/4404848721047/dshbd_cnfg.gif)
2. Select in the value combo box of the Shipper parameter. JDashboard displays the Enter Values dialog box.
3. Clear the **All Values** checkbox, select **UBS Uniform Logistics** in the left box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404857098263/btn_add.gif) to add it to the right box, then select **OK**.

   ![Enter Parameter Values](https://devnet.logianalytics.com/hc/article_attachments/4404857098519/dshbd_entrvlue.gif)
4. Select **OK** in the configuration panel. The table now shows records of this shipper only.

   ![Apply Parameter Values to Table](https://devnet.logianalytics.com/hc/article_attachments/4404857098775/dshbd_chgprm.gif)
5. Save the dashboard.

## Task 9: Share Parameters Among Components

When two or more library components in a dashboard contain parameters that meet the following cases, you can share the parameters among them. After sharing parameters, you just need to provide values to one group of the parameters and all related components are able to receive them.

* The numbers of the parameters in each library component are the same.
* According to the parameter order in each library component, the orders of the parameter data types are the same. For example, the parameter data types in a component are String, Number, and Boolean. If there is another component in which the parameter data types are also String, Number, and Boolean, the two components fulfill the condition of the same parameter data types.
* It is up to users to make sure the to-be-shared parameters contain some common values.

In this task, we insert two library components having similar parameters and see the difference between before and after sharing the parameters.

1. Select the **Add** button ![Add Dashboard button](https://devnet.logianalytics.com/hc/article_attachments/4404848721303/btn_adddsh.gif) on the dashboard title bar to add a new dashboard. JDashboard creates a new tab and labels it Dashboard 2.
2. Expand **Component Library** > **Public Components** > **SampleReports** and drag **Shipment Status Overview.lc**  and **Shipments by Status.lc** one by one to the dashboard body.
3. Close the Resources panel.
4. Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404848721559/btn_menu.gif) on the toolbar and select **Share Parameter**.
5. JDashboard displays the Share Parameters Setting dialog box, showing that the two library components have shared parameters. Close the dialog box.

   ![Set Share Parameters](https://devnet.logianalytics.com/hc/article_attachments/4404848721815/dshbd_prmshare.gif)
6. Select the **Enter Parameter Values** button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404857099031/btn_prm.gif) on the toolbar. The Enter Parameter Values dialog box lists the following parameters. Close the dialog box.

   ![Shared Parameters](https://devnet.logianalytics.com/hc/article_attachments/4404848722071/dshbd_prmsharevlu.gif)

Next we will remove the parameter share between the two components to see how many parameters we need to specify.

1. Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404848721559/btn_menu.gif) on the toolbar and select **Share Parameter**. JDashboard displays the Share Parameters Setting dialog box.
2. Select either component and select the **Cancel Share** button, then select **OK**.
3. Select the **Enter Parameter Values** button ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404857099031/btn_prm.gif) on the toolbar to access the Enter Parameter Values dialog box again. Now it lists separate pairs of the Start Date, End Date, and Territory/Shipper parameters that the two library components apply. Close the dialog box.

   ![Separated Parameters](https://devnet.logianalytics.com/hc/article_attachments/4404857099287/dshbd_prmunsharevlu.gif)
4. Select the **Save** button ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404857094679/btn_sv.gif) on the toolbar to save the dashboard as **Shipment**.

## Task 10: Run a Report in JDashboard

You can run a report in Web Report Studio or Page Report Studio within JDashboard. In this task, we run a web report inside JDashboard without going to the resource tree in the Server Console.

1. Keep the Shipment dashboard active.
2. From the Resources panel, drag **Sales Detail Report.wls** in the Reports > Public Reports > SampleReports folder to the dashboard body, then close the panel.
3. JDashboard loads the report into a separate tab via Web Report Studio.

   ![Run Report in JDashboard](https://devnet.logianalytics.com/hc/article_attachments/4404848722327/dshbd_runrpt.gif)

## Task 11: Set a Dashboard as the Server Home Page

1. In the web browser, change from the JDashboard tab to the Logi Report Start Page tab.
2. Select **My Profile** in the **Manage** category.
3. In the My Profile > Customize Server Preferences > General tab, select the **Use a Dashboard** checkbox for the **Home Page** option, then select **OK**.

   ![Set Home Page](https://devnet.logianalytics.com/hc/article_attachments/4404848722583/dshbd_dshhm.gif)
4. Select **OK** in the prompt message.
5. Select **Resources** on the system toolbar, then go to the **My Reports** folder.
6. Select **Shipment.dsh** in the folder and Server loads the dashboard into a new JDashboard window.
7. Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404848721559/btn_menu.gif) on the toolbar and you can see **Set as Server Home** is enabled on the menu list. Select the option to set the Shipment dashboard as the Server home page.
8. Refresh the Server Console page. You can find that Server adds a Home label beside Resources on the system toolbar.
9. Select **Home** and you can access the Shipment dashboard immediately.

   ![Use Dashboard as Home Page](https://devnet.logianalytics.com/hc/article_attachments/4404857099927/dshbd_srvhome.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093601-Part-IV-End-User-Experience)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093641-Track-2-Performing-Visual-Analysis-)
