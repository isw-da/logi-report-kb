---
title: "Opening Visual Analysis in JDashboard"
id: 1500009686962
section: "JDashboard Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009686962-Opening-Visual-Analysis-in-JDashboard
updated_at: 2021-11-03T06:58:22Z
---

# Opening Visual Analysis in JDashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686922-Running-and-Editing-Reports-in-JDashboard)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712641-Customizing-JDashboard-Profile)

# Opening Visual Analysis in JDashboard

If your Logi JReport Server is enabled with [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009686042-Visual-Analysis), you can access Visual Analysis directly from JDashboard without having to switch to the resource tree in the server console. Visual Analysis is loaded in JDashboard as a tab with full functionality for you to perform data analysis with.

There are several ways to access Visual Analysis:

* On the dashboard title bar, leave the mouse pointer on the **+** button beside the rightmost tab for one second until a drop-down menu displays, then select **New Analysis** from the menu.
* On the toolbar, select the **New** button ![New button](https://devnet.logianalytics.com/hc/article_attachments/4412139483159/btn_newobj.gif) and then select **New Analysis**.
* On the toolbar, select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) and then select **New** > **Analysis**.

You can also take the following ways to access Visual Analysis for a specific analysis template:

**Using dialog**

1. In JDashboard, select the **Open** button ![Open button](https://devnet.logianalytics.com/hc/article_attachments/4412139483415/btn_open.gif) on the toolbar or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4412131478039/btn_dshbrd_optn.gif) and select **Open** from the option list. The Open Document dialog appears.

   ![Open Document dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131481495/opendoc.gif)
2. Browse to the desired folder, select the analysis template you want to open and then select **OK**, or simply double-click the analysis template to open it.

**Using the Resources panel**

1. In the Resources panel of JDashboard, expand the **Reports** node (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4412139568151/btn_dshbrd_show.gif) on the toolbar to display the Resources panel if it is closed).
2. Browse to the target analysis template with .va as the suffix and drag it to the editing area.

   Visual Analysis is then loaded in a new dashboard tab with the selected analysis template displayed.

**Using component title bar**

After [an analysis template is inserted in a dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009712541-Creating-and-Saving-Dashboards#VA) as its component, select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4412139482135/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009712601-General-Operations-in-JDashboard#TitleBar), focus on **Analyze** on the drop-down menu, and then choose an option:

* **In New Tab**  
   Loads the specified analysis template in Visual Analysis in a new dashboard tab.
* **In New Window**  
   Loads the specified analysis template in Visual Analysis in a new web browser window.

Note that the changes made on the analysis template in Visual Analysis will be saved to the server resource tree, however they will not be reflected on the one inserted as component in the dashboard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009686922-Running-and-Editing-Reports-in-JDashboard)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009712641-Customizing-JDashboard-Profile)
