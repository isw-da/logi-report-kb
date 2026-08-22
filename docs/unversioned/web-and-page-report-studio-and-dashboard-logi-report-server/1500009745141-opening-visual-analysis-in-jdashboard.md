---
title: "Opening Visual Analysis in JDashboard"
id: 1500009745141
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745141-Opening-Visual-Analysis-in-JDashboard
updated_at: 2021-07-25T07:20:12Z
---

# Opening Visual Analysis in JDashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745121-Running-and-Editing-Reports-in-JDashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718962-Customizing-JDashboard-Profile)

# Opening Visual Analysis in JDashboard

If your Logi Report Server is enabled with [Visual Analysis](https://devnet.logianalytics.com/hc/en-us/articles/1500009718222-Using-Visual-Analysis-to-Analyze-Data-Intuitively-and-Instantly-Logi-Report-Server-v17), you can access Visual Analysis directly from JDashboard without having to switch to the resource tree in the server console. Visual Analysis is loaded in JDashboard as a tab with full functionality for you to perform data analysis with.

There are several ways to access Visual Analysis:

* On the dashboard title bar, leave the mouse pointer on the **+** button beside the rightmost tab for one second until a drop-down menu displays, then select **New Analysis** from the menu.
* On the toolbar, select the **New** button ![New button](https://devnet.logianalytics.com/hc/article_attachments/4404936714519/btn_newobj.gif) and then select **New Analysis**.
* On the toolbar, select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936890647/btn_dshbrd_optn.gif) and then select **New** > **Analysis**.

You can also take the following ways to access Visual Analysis for a specific analysis template:

**Using dialog box**

1. In JDashboard, select the **Open** button ![Open button](https://devnet.logianalytics.com/hc/article_attachments/4404942445591/btn_open.gif) on the toolbar or select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936890647/btn_dshbrd_optn.gif) and select **Open** from the option list. Report Server displays the Open Document dialog box.

   ![Open Document dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936895255/opendoc.gif)
2. Browse to the desired folder, select the analysis template you want to open and then select **OK**, or simply double-click the analysis template to open it.

**Using the Resources panel**

1. In the Resources panel of JDashboard, expand the **Reports** node (select **Show Resources**![Show Resources button](https://devnet.logianalytics.com/hc/article_attachments/4404942565655/btn_dshbrd_show.gif) on the toolbar to display the Resources panel if it is closed).
2. Browse to the target analysis template with .va as the suffix and drag it to the editing area.

   Visual Analysis is then loaded in a new dashboard tab with the selected analysis template displayed.

**Using component title bar**

After [an analysis template is inserted in a dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009745021-Creating-and-Saving-Dashboards#VA) as its component, select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4404942444951/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#TitleBar), focus on **Analyze** on the drop-down menu, and then choose an option:

* **In New Tab**  
   Loads the specified analysis template in Visual Analysis in a new dashboard tab.
* **In New Window**  
   Loads the specified analysis template in Visual Analysis in a new web browser window.

Note that the changes made on the analysis template in Visual Analysis will be saved to the server resource tree, however they will not be reflected on the one inserted as component in the dashboard.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745121-Running-and-Editing-Reports-in-JDashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718962-Customizing-JDashboard-Profile)
