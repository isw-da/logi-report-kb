---
title: "Going Through the Report Data"
id: 1500009692802
section: "Editing Web Reports in Web Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009692802-Going-Through-the-Report-Data
updated_at: 2021-11-03T06:56:28Z
---

# Going Through the Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719141-Applying-Filters)

# Going Through the Report Data

In a web report, you can switch from the current group to another group to see the data you want, and view the detail information of the summary values with the following going actions. This feature is not supported on org charts.

* [Go-To](#Go-to)  
   Enables you to obtain a different view of data by switching between the groups.
* [Go-to-by-Value](#Go-to-by-value)  
   Enables you to filter data based on a go-to action to obtain a more detailed view of the data.
* [Go-Down](#Go-down)  
   Enables you to drill data to lower-level groups according to predefined hierarchies. For more information about hierarchies, see Defining hierarchies in a business view in the *Logi JReport Designer User's Guide*.
* [Go-Up](#Go-up)  
   Enables you to drill data to higher-level groups according to predefined hierarchies.
* [Go-to-Detail](#Go-to-detail)  
   Enables you to concentrate on the detail information of summaries.

After a going action is performed, the data presented in the component will be reloaded from the data buffer, showing only the requested data. The new component can be viewed, printed, and exported to other formats in the same way as the original one.

Assume [you have created a chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009719181-Inserting-Components#Chart) of Clustered Bar 2-D type on the business view WorldWideSalesBV in Data Source 1 of the SampleReports catalog in the SampleReports folder, which shows product sales information with Region as the field on the category axis, Sales Year as the field on the series axis, and Total Sales as the field on the value axis, and applies the Classic style. The chart shows as follows:

![Create Chart](https://devnet.logianalytics.com/hc/article_attachments/4412139506583/wbrpt_edt_go.gif)

The business view WorldWideSalesBV has been defined with the following hierarchical group levels: Region > Country > State > City.

We will now take the chart as an instance to illustrate the going actions.

## Go-To

The go-to action enables jumping to a different group by replacing the current. It is performed on chart categories and series.

1. Right-click any region on the category axis, Asia-Pacific for example, and choose **Go To** from the shortcut menu. The groups available for the action are listed on the submenu, which are all the other group objects in the business view used by the chart.

   ![Go To Submenu](https://devnet.logianalytics.com/hc/article_attachments/4412139506839/wbrpt_edt_go1.gif)
2. Select **State** on the submenu. In the regenerated result, we can see that State becomes the group for categories and Sales Year remains the group for series.

   ![Go To State](https://devnet.logianalytics.com/hc/article_attachments/4412112509847/wbrpt_edt_go2.gif)

## Go-to-by-Value

The go-to-by-value action allows showing the information of another group while applying the current value being clicked on as a filter condition. It is performed on crosstab column/row headers, table/banded object groups, and chart categories and series.

1. Go back to the original chart in the above example by selecting the **Undo** button ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4412139484183/btn_undo.gif) on the toolbar.
2. Right-click **Asia-Pacific** on the category axis, and point to **Go to By Value** on the shortcut menu. A submenu for the command is displayed, which lists the same items as those of Go To.
3. Select **State** too and the result is regenerated as follows:

   ![Go To By State](https://devnet.logianalytics.com/hc/article_attachments/4412139507095/wbrpt_edt_go3.gif)

   We can see that the result is different from that of go-to. This is because that, for the go-to-by-value action, the group of categories changes to State while being filtered by the Region value Asia-Pacific. That is, on the basis of the go-to action, a filtering action where Region = Asia-Pacific is performed at the same time. In addition, when a go-to-by-value action is performed, the "Go To" Filter panel will be displayed on the left of the Web Report Studio window, showing the group and the value that the filter is based on.

   ![Go To Filter](https://devnet.logianalytics.com/hc/article_attachments/4412112510103/wbrpt_edt_go4.gif)

## Go-Down

The go-down action allows going from a non-bottom level group to the one-level-lower group while applying the currently selected value as a filter condition. It is performed on table/banded object groups, crosstab column/row headers, and chart categories and series.

1. Go back to the original chart in the above example by selecting the **Undo** button ![Undo button](https://devnet.logianalytics.com/hc/article_attachments/4412139484183/btn_undo.gif) on the toolbar.
2. Right-click the value **Asia-Pacific**, on the shortcut menu, point to **Go Down**. Country is listed as the submenu item.

   ![Go Down Submenu](https://devnet.logianalytics.com/hc/article_attachments/4412112510359/wbrpt_edt_godwn1.gif)
3. Select **Country**. The chart now displays the data about countries in the Asia Pacific region.

   ![Go Down to Country](https://devnet.logianalytics.com/hc/article_attachments/4412112510615/wbrpt_edt_godwn2.gif)
4. The one-level-lower group for Country defined in the hierarchy is State. Right-click on **China** and select **Go Down** > **State**. The chart now shows states in China.

   ![Go Down to State](https://devnet.logianalytics.com/hc/article_attachments/4412131396375/wbrpt_edt_godwn3.gif)

   After these two go-down actions, we can see two filters are added in the "Go To" Filter panel, "Region : Asia-Pacific" and "Country : China".

   ![Go To Filter](https://devnet.logianalytics.com/hc/article_attachments/4412131396631/wbrpt_edt_godwn4.gif)

   This is because, when you perform a go-down action, a filter will be created based on the value you select on. In this example, we first select on the Asia-Pacific region, so Logi JReport drills this region one-level down to display countries in Asia Pacific, and thus the filter Region = Asia-Pacific is created. If you want all data in the one-level-lower group to be displayed when you drill down a group, you can remove the corresponding filter from the "Go To" Filter panel, by selecting **X** beside the filter condition.

## Go-Up

The go-up action allows going from a group which is non-top level in a predefined hierarchy to the one-level-higher group. It is performed on table/banded object groups, crosstab column/row headers, and chart categories and series.

1. Based on the report result after go-down, right-click any value of State, Beijing for example, on the shortcut menu, point to **Go Up**, and we can see that Country is listed as the submenu item.

   ![Go Up Submenu](https://devnet.logianalytics.com/hc/article_attachments/4412112510871/wbrpt_edt_goup.gif)
2. Select **Country** to update the chart. Country is now the group for categories and the filter condition Country = China is removed from the "Go To" Filter panel.

   ![Go Up to Country](https://devnet.logianalytics.com/hc/article_attachments/4412112510615/wbrpt_edt_godwn2.gif)
3. The one-level-higher group for Country defined in the hierarchy is Region. Now right-click any value of Country, Australia for example, on the shortcut menu, select **Go Up** > **Region**, the chart restores to the original state.

   ![Go Up to Region](https://devnet.logianalytics.com/hc/article_attachments/4412139506583/wbrpt_edt_go.gif)

## Go-to-Detail

The go-to-detail action enables you to concentrate on the detail information of each summary value. It is performed on summaries in tables, crosstabs, banded objects and the chart data markers.

1. Right-click the bar represents the total sales of Asia-Pacific in 2016 and select **Go to Detail** on the shortcut menu.

   ![Go To Detail](https://devnet.logianalytics.com/hc/article_attachments/4412139507351/wbrpt_edt_gotodtl1.gif)
2. The detail table of the summary value is displayed in the same frame or a new window according to the setting of [Target of Detail Table Report and Links](https://devnet.logianalytics.com/hc/en-us/articles/1500009719321-Customizing-Web-Report-Studio-Profile#Target) in the Web Report Studio profile. By default, the detail table contains all the group and detail objects in the same business view category as the aggregate object from which the summary value is generated.

   ![Detail Table](https://devnet.logianalytics.com/hc/article_attachments/4412112511127/wbrpt_edt_gotodtl2.gif)
3. If the detail table is displayed in the same frame as the original report, you can select ![Back button](https://devnet.logianalytics.com/hc/article_attachments/4412139499927/btn_back.gif) on the toolbar to go back to the original report.

In most cases, the default detail table may not well satisfy your requirements. Logi JReport provides you with the option to customize the detail table by your own.

**To edit the detail table for the go-to-detail action:**

1. Right-click any summary value (for a chart it is any data marker) and select **Edit Detail Table** from the shortcut menu. The [Edit Detail Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009715961-Edit-Detail-Table) dialog appears.

   ![Edit Detail Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131396887/edtdtltbl.gif)
2. The Resources box lists all the group and detail objects in the business view used by the current data component. Add the fields you want to display in the detail table to the right box. To adjust the order of the added fields, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4412112497431/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4412112497687/btn_mvdown.gif).
3. From the Target drop-down list, specify the window or frame in which to load the detail table.
   * **New Window**  
      Loads the detail table into a new window.
   * **Same Frame**  
      Loads the detail table into the same frame or window where the main report is.
   * **Other Frame**  
      Loads the detail table into some other available frame. Type the frame name into the text box to find the frame. If the frame does not exist, the detail table report will be loaded into a new window.
   * **<Server Setting>****[Target of Detail Table Report and Links](https://devnet.logianalytics.com/hc/en-us/articles/1500009719321-Customizing-Web-Report-Studio-Profile#Target) Loads the detail table according to setting of the** option in the Web Report Studio profile.
4. Select **OK** to finish defining the detail table.
5. Perform the go-to-detail action on a summary value and the detail table displays the information you define.

**Notes:**

* If the table type is Group Above, you can right-click its group header to show the shortcut menu so as to use the going function. For other table types, you have to right-click the group name in group column to perform going.
* For a web report created in Logi JReport Designer, if the select priority of the go-down action is specified to be the highest at report design time, you can also select the group object directly to go down to the next level in View Mode of Web Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009719121-Using-Dynamic-Resources-and-Local-Parameters-)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009719141-Applying-Filters)
