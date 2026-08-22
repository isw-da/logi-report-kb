---
title: "Going Through the Report Data"
id: 1500009650302
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data
updated_at: 2021-07-24T20:53:36Z
---

# Going Through the Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters)

# Going Through the Report Data

In a web report, you can choose to show certain groups of records according to your requirements (not supported on org charts), and switch among the groups to see the data you want.

* [Go-to](#Go-to)  
   Enables you to obtain a different view of data by switching among groups.
* [Go-to-by-value](#Go-to-by-value)  
   Enables you to filter data based on a go-to action to obtain a more detailed view of the data.
* [Go-down](#Go-down)  
   Enables you to drill data to a lower-level group according to predefined hierarchies. For more information about hierarchies, refer to "Defining Hierarchies" in the *Logi JReport Designer User's Guide*.
* [Go-up](#Go-up)  
   Enables you to drill data to a higher-level group according to predefined hierarchies.
* [Go-to-detail](#Go-to-detail)   
   Enables you to concentrate on the details of a group.

After a "going" action has been performed, the data presented in the component will be re-loaded from the data buffer, showing only the records in the selected group, and the new report created can be viewed, printed, and exported to other formats in the same way as the original report.

Assume [you have created a chart report](https://devnet.logianalytics.com/hc/en-us/articles/1500009675141-Standard-Way-of-Report-Creation-Using-Wizard) of Clustered Bar 2-D type on the business view WorldWideSalesBV in Data Source 1 of the SampleReports catalog in the SampleReports folder, which  shows product sales information with Region as the field on the category axis, Sales Year as the field on the series axis, and Total Sales as the field on the value axis, and applies the Neutral style to the chart. The chart shows as follows:

![](https://devnet.logianalytics.com/hc/article_attachments/4404920394263/wbrpt_edt_go0.gif)

The business view WorldWideSalesBV has defined the following hierarchical relationship: Region > Country > State > City.

We will now take the chart as an instance to illustrate the going functions.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Go-To

The go-to action enables jumping to a different group by replacing the current. It is performed on chart categories and series.

1. Right-select any value of Region, Asia-Pacific for example, and choose **Go To** from the shortcut menu. The list of groups available for "Go to" will appear on the submenu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920394519/wbrpt_edt_go1.gif)
2. Select **State** on the submenu, then in the regenerated result, we can see that State becomes the group for categories and Sales Year remains the group for series.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920394775/wbrpt_edt_go2.gif)
3. To return to the original status, select the Undo button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920359447/btn_undo.gif) on the toolbar.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Go-to-by-Value

The go-to-by-value action allows showing the information of another group while applying the current value being selected on as a filter condition. It is performed on crosstab column/row headers, table groups, and chart categories and series.

1. Go back to the original report in the above example.
2. Right-select the value **Asia-Pacific** of the Region group, and point to **Go to By Value** on the shortcut menu. A submenu for the command is displayed, which lists the same items as those of Go To.
3. Select **State** too and the result will be regenerated.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920395031/wbrpt_edt_go3.gif)

   We can see that the result is different from that of go-to. This is because that, for the go-to-by-value action, the group of categories changes to State while being filtered by the Region value Asia-Pacific. That is, on the basis of the go-to action, a filtering action where Region = Asia-Pacific is performed at the same time, and thus the result of go-to-by-value is generated.

   In addition, when a go-to-by-value action is performed, the "Go To" Filter panel will be displayed on the left of the Web Report Studio window, showing the group and the value that the filter is based on.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920395287/wbrpt_edt_go4.gif)
4. To go back to the original report, select the Undo button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920359447/btn_undo.gif) on the toolbar.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Go-Down

The go-down action allows going from a non-bottom level group to the one-level-lower group while applying the current selected value as a filter condition. It is performed on table groups, crosstab column/row headers, and chart categories and series.

1. Go back to the original report in the above example, right-click the value **Asia-Pacific**, on the shortcut menu, point to **Go Down**, and we can see that Country is listed as the submenu item.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920395543/wbrpt_edt_godwn1.gif)
2. Select **Country** to see the result. It displays the data about countries in the Asia Pacific region.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926647063/wbrpt_edt_godwn2.gif)
3. The one-level-lower group for Country defined in the hierarchy is State. Right-select on **China** and select **Go Down** > **State**. The chart now shows states in China.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920395799/wbrpt_edt_godwn3.gif)

   After these two go-down actions, we can see two filters are added in the "Go To" Filter panel, Region = Asia-Pacific and Country = China.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926647319/wbrpt_edt_godwn4.gif)

   This is because, when you perform a go-down action, a filter will be created based on the value you select on. In this example, we first select on the Asia-Pacific region, so Logi JReport drills this region one-level down to display countries in Asia Pacific, and thus the filter Region = Asia-Pacific is created. If you want all data in the one-level-lower group to be displayed when you drill down a group, you can remove the corresponding filter from the "Go To" Filter panel, by selecting **X** beside the filter condition.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Go-Up

The go-up action allows jumping from a group which is non-top level in a predefined hierarchy to the one-level-higher group. It is performed on table groups, crosstab column/row headers, and chart categories and series.

1. Based on the report result after go-down, right-click any value of State, Beijing for example, on the shortcut menu, point to **Go Up**, and we can see that Country is listed as the submenu item.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920396183/wbrpt_edt_goup.gif)
2. Select **Country** to see the result. Country is now the group for categories and the filter condition Country = China is removed from the "Go To" Filter panel.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926647063/wbrpt_edt_godwn2.gif)
3. The one-level-higher group for Country defined in the hierarchy is Region. Now right-click any value of Country, Singapore for example, on the shortcut menu, point to **Go Up** and select **Region**, the chart restores to the original state.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920394263/wbrpt_edt_go0.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Go-to-Detail

The go-to-detail action is performed on the summary of the tables, crosstabs and charts. First define a table and make it contain the information you would like to view about the summary values. Suppose that the summary is total sales in different countries. Then when you perform go-to-detail action on the value of total sales in France, you will get the table displaying the fields you defined and having applied the filter condition Country=France. When you go to detail of the total sales in another country, the table will display the data of that country.

**To define the detail table for a summary and perform the go-to-detail action on it:**

1. Right-select any summary value (for a chart it is any data marker) and select **Edit Detail Table** from the shortcut menu. The [Edit Detail Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009671661-Edit-Detail-Table) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926648215/edtdtltbl.gif)
2. From the Resources box, add the fields you want to display in the detail table of the summary. To adjust the order of the added fields, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).
3. From the Target drop-down list, specify the window or frame in which to load the detail table.
4. Select **OK** to finish defining the detail table.
5. Right-select a summary value of which you would like to view the detailed information, then select **Go to Detail** on the shortcut menu. The detail table for the summary value is then displayed in the window or frame as you specified, which shows the fields you have defined.

   If the detail table is displayed in the same frame as the original report, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920386327/btn_back.gif) on the toolbar to go back to the original report.

**Notes:**

* If the table type is Group Above, you can right-click its group header to show the shortcut menu so as to use the going function. For other table types, you have to right-click the group name in group column to perform going.
* For a web report created in Logi JReport Designer, if the select priority of the go-down action is specified to be the highest at report design time, you can also select the group object directly to go down to the next level in the View Mode of Web Report Studio.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters)
