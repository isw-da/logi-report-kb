---
title: "Track 1: Self-service Dashboard with Logi JReport"
id: 1500009571382
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009571382-Track-1-Self-service-Dashboard-with-Logi-JReport
updated_at: 2021-07-24T05:53:40Z
---

# Track 1: Self-service Dashboard with Logi JReport

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009593401-Part-II-Quick-Start) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571402-Track-2-Performing-Visual-Analysis)

# Track 1: Self-service Dashboard with Logi JReport

Dashboard is a new way of information delivery. Users can create, edit and browse dashboards from the Logi JReport Server user console using JDashboard. With pre-built library components, users can freely choose the objects they want to display in a dashboard, without having to know how these objects were created, what data sources to use, what styles to set, etc. Report data components and Visual Analysis templates can also be inserted in dashboards directly. A dashboard can hold multiple library components so that when browsing the dashboard users are able to see multiple data aspects. Within a dashboard, library components are able to communicate with each other via the message mechanism. This allows actions such as common filters to be applied to all the components of a dashboard even when coming from different data sources so as to achieve data synchronization.

* [Task 1: Create a Dashboard and Insert Library Components](#Task1)
* [Task 2: Insert a Report Component into Dashboard](#Task2)
* [Task 3: Synchronize the Components](#Task3)
* [Task 4: Use a Slider to Filter on Quantity](#Task4)
* [Task 5: Insert a Third-Party Gadget (Stock Widget)](#Task5)
* [Task 6: Export the Library Components](#Task6)
* [Task 7: Use the Configuration Panel to Change Parameters](#Task7)
* [Task 8: Share Parameters Among Components](#Task8)
* [Task 9: Insert an Analysis Template into Dashboard](#Task9)
* [Task 10: Run a Report in JDashboard](#Task10)
* [Task 11: Set a Dashboard as the Server Home Page](#Task11)

**Note:** A JDashboard license for Logi JReport Server is required in order to perform this track. If you do not have the license, please contact your Jinfonet Software account manager to obtain it first.

## Task 1: Create a Dashboard and Insert Library Components

1. On the [Logi JReport Server Start Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009582241-Lesson-1-Starting-Logi-JReport-Server), select **Dashboards** in the Create category.

   The JDashboard window is displayed with a blank dashboard created.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889253783/dshbd_nw.gif)
2. Select the **Resources** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254039/btn_show.gif) on the toolbar to display the Resources panel, which lists all the data resources and components that can be inserted in dashboards.
3. Expand the **Component Library** > **Public Components** > **SampleReports** folder and drag **Sales by Category.lc** to the dashboard body.
4. Drag **Crosstab.lc** in the same folder to the right of the first component.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893766039/btn_cls.gif) on the top right of the Resources panel to hide the panel.
6. Select the **Arrange** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254295/btn_arg.gif) on the toolbar to align the two library components.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893766551/dshbd_dshbrd.gif)
7. Select the **Save** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893766807/btn_sv.gif) on the toolbar.
8. In the Save As dialog, replace Dashboard 1 with **Products** in the File Name text box, then select **OK** to save the dashboard into the My Reports folder in the server resource tree.

## Task 2: Insert a Report Component into Dashboard

Report components created from business views can be inserted in dashboards directly.

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254039/btn_show.gif) on the toolbar to display the Resources panel.
2. Go to the **Reports** > **Public Reports** > **SampleReports** folder, expand **ShipmentStatus.wls** and drag **TableComp** to the dashboard body below the existing components. Hide the Resources panel.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254295/btn_arg.gif) on the toolbar to align the three library components.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893767063/dshbd_rptcom.gif)
4. Save the dashboard.

## Task 3: Synchronize the Components

In this task, we want to select any value of the Category field in the crosstab to automatically update the chart. This is achieved by delivering a filter synchronization message between the two library components.

1. Right-click on any Category value in the crosstab column header, Blends for example, and select **Send Sync** > **Filter** from the shortcut menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254551/dshbd_snd.gif)
2. The chart automatically receives the synchronization message because it is created based on the same business view as the crosstab and contains the field Category too. To view details of the message, right-click the chart and select **Receive Sync**. The filter message is shown in the Receive Sync dialog. Close the dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254807/dshbd_rcv.gif)
3. Select any value in the crosstab column header, for example Bold. The chart is filtered to show data of the Bold category only after it receives the synchronization message.

   You may find that the crosstab is also filtered. This is because at report design time, the library component designer has predefined to make it receive a filter message too. You can right-click on the crosstab and select **Receive Sync** to view the details if you want.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893767319/dshbd_sync.gif)
4. We will remove the filters from the components. Select the **Clear Filters** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889255063/btn_clrfltr.gif) on the toolbar.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893766807/btn_sv.gif) on the toolbar to save the dashboard.

## Task 4: Use a Slider to Filter on Quantity

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254039/btn_show.gif) on the toolbar to display the Resources panel, then from the Toolbox node, drag **Filter Control** to the dashboard body below the table.
2. In the Insert Filter Control dialog, input **Sales Quantity** in the Title text box and select **Range Slider** as the control type.
3. Expand the Select Fields drop-down list. The two business views used by the three data components in the dashboard are listed. You can select a common field in both business views to filter the three data component at the same time via the slider. Here we only want to filter data components that use WorldWideSalesBV.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893767575/dshbd_bvlist.gif)
4. Check **Quantity** in WorldWideSalesBV, then select outside of the drop-down list to close it. Select **OK** to insert the slider.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893767831/dshbd_sldrdlg.gif)
5. Hide the Resources panel.

Next, we will use the slider to show the data for Quantity between 5000 and 8000 only.

1. Uncheck the **All** checkbox on the slider. Drag the left arrow to set a minimum range 4983 and the right
   arrow to set a maximum range 8031. The
   chart and crosstab are filtered. The table uses the other business view so it is not changed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893768087/dshbd_sldr.gif)
2. Save the dashboard.

## Task 5: Insert a Third-Party Gadget (Stock Widget)

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254039/btn_show.gif) on the toolbar to display the Resources panel, then drag **URL Frame** from the Toolbox node to the dashboard body on the right of the slider. The Insert URL Frame dialog is displayed.
2. In the Title text field, input **My Stocks**, and in the URL text box, type in **http://edulifeline.com/includes/stocks\_widget/**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893768343/dshbd_url.gif)
3. Select  **OK**. The specified web page is then inserted into the dashboard.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889255447/dshbd_urlrst.gif)
4. Hide the Resources panel and save the dashboard.

## Task 6: Export the Library Components

1. Select the **Export** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893768727/btn_expt.gif) on the toolbar. The Export dialog appears.
2. Select **Customize Layout** from the Layout drop-down list.

By default, all the exportable library components are arranged using a tabular style according to their positions in the dashboard in the Design tab on the right. Each tabular cell can hold no more than one component. Sliders and gadgets cannot be exported so they are not available here.
Next, we will change the layout of the components a little bit by removing the crosstab on the right of the chart and adding it below the table.

1. Right-click anywhere in the cell containing the crosstab, select **Remove** from the shortcut menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893768983/dshbd_exptrmv.gif)
2. Scroll down to the blank cell below the table. Drag **Crosstab** from the Resources box to the cell.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893769239/dshbd_exptcrstb.gif)

When exporting tables and crosstabs, by default only the data currently displayed in the dashboard will be exported. In our dashboard the table contains several pages and we can view only one page at a time, that is to say only the currently displayed page will be exported. We want to get the full data of the table in the exported result so we need a further setting.

1. Right-click in the cell holding the table, select **Filter** from the shortcut menu, then choose the **All** option and select **OK**.
2. Select the **Export** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893768727/btn_expt.gif) on the toolbar. In the Export dialog,
   keep the default settings to export the dashboard to a PDF file.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889255703/dshbd_expt.gif)
3. Select **OK**. The exporting process begins. When finished, you can open the PDF file to view the result.
4. Close the Export dialog and save the dashboard.

## Task 7: Use the Configuration Panel to Change Parameters

When a library component uses parameters and its configuration panel is enabled, you can make use of the configuration panel to change its parameter values.

1. On the table, place the mouse anywhere on the title bar, then select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889255959/btn_more.gif) that appears on the title bar and select **Edit Setting** from the drop-down list to display the configuration panel.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893769495/dshbd_cnfg.gif)
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893769751/btn_entrvlu.gif) in the value box for the Shipper parameter. The Enter Values dialog appears.
3. Check the **Custom** radio button, select **UBS Uniform Logistics** and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893770007/btn_add.gif) to add it to the right box, then select **OK**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893770519/dshbd_entrvlue.gif)
4. Select **OK** in the configuration panel. The table result is then changed based on the parameter value.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889256343/dshbd_chgprm.gif)
5. Save the dashboard.

## Task 8: Share Parameters Among Components

When two or more library components in a dashboard contain parameters that meet the following cases, the parameters can be shared among them. After sharing parameters, you just need to provide values to one group of the parameters and all related components will be able to receive them.

* The numbers of the parameters in each library component are the same.
* According to the parameter order in each library component, the orders of the parameter data types are the same. For example, the parameter data types in a component are String, Number, and Boolean. If there is another component in which the parameter data types are also String, Number, and Boolean, the two components fulfill the condition of the same parameter data types.
* It is up to users to make sure the to-be-shared parameters contain some common values.

In this task, we will insert two library components having similar parameters and see the difference between before and after the parameters are shared.

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889256599/btn_adddsh.gif) on the dashboard title bar to add a new dashboard. A new tab is created, labeled Dashboard 2.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254039/btn_show.gif) on the toolbar to display the Resources panel.
3. Expand **Component Library** > **Public Components** > **SampleReports** and drag **Count Shipment by Ship Type.lc** and **Count Shipment by Territory.lc** one by one to the dashboard body. Hide the Resources panel.
4. Select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404889256855/btn_menu.gif) on the toolbar and select **Share Parameter**. The displayed dialog shows that the two library components have shared parameters. Close the dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889257111/dshbd_prmshare.gif)
5. Select the **Enter Parameter Values** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893770775/btn_prm.gif) on the toolbar. The Enter Parameter Values dialog lists the following parameters. Close the dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893771031/dshbd_prmsharevlu.gif)

Next we will remove the parameter share between the two components to see how many parameters we need to specify.

1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889256855/btn_menu.gif) on the toolbar and select **Share Parameter**. In the displayed dialog, select either component and select the **Cancel Share** button on the top right, then select **OK**.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893770775/btn_prm.gif) on the toolbar to access the Enter Parameter Values dialog again. Now it lists separate pairs of the Start Date, End Date, and Territory/Shipper parameters used by the two library components. Close the dialog.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889257367/dshbd_prmunsharevlu.gif)
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893766807/btn_sv.gif) on the toolbar to save the dashboard as **Shipment**.

## Task 9: Insert an Analysis Template into Dashboard

1. Keep the Shipment dashboard active.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889254039/btn_show.gif) on the toolbar to display the Resources panel.
3. Go to the **Reports** > **Public Reports** > **SampleReports** folder, expand **VA Analysis.va** and you can find a VCTObject under it. Drag **VCTObject** into the dashboard body.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893771287/dshbd_va.gif)
4. Save the dashboard.

## Task 10: Run a Report in JDashboard

1. Keep the Shipment dashboard active.
2. From the Resources panel, drag **Coffee Sales.wls** in the Reports > Public Reports > SampleReports folder to the dashboard body, then hide the panel.
3. The report is loaded into a separate tab via Web Report Studio.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893771543/dshbd_runrpt.gif)

## Task 11: Set a Dashboard as the Server Home Page

1. In the web browser, change from the JDashboard tab to the Logi JReport Server Start Page tab.
2. Select **Profile** in the Manage category.
3. In the General tab of the Profile page, check the **Use a Dashboard** checkbox for the Home Page option, then select **OK**. Select **OK** in the prompt message.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889257623/dshbd_dshhm.gif)
4. Select **Resources** on the system toolbar, then go to the **My Reports** folder.
5. Select **Shipment.dsh** in the folder, the dashboard is loaded into a new JDashboard window.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404889256855/btn_menu.gif) on the toolbar and you can see Set as Server Home is enabled on the menu list. Select the option to set the Shipment dashboard as the server home page.
7. Refresh the Logi JReport Console page and a Home label is added beside Resources on the system toolbar. Select it and you can access the Shipment dashboard immediately.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893771799/dshbd_srvhome.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Page](https://devnet.logianalytics.com/hc/en-us/articles/1500009593401-Part-II-Quick-Start) [Next Page![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571402-Track-2-Performing-Visual-Analysis)
