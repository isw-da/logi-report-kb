---
title: "Automatic Drilling"
id: 1500009691562
section: "Drilling Through the Report Data"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691562-Automatic-Drilling
updated_at: 2021-11-03T06:56:49Z
---

# Automatic Drilling

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691542-Drilling-Through-the-Report-Data)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718141-Going)

# Automatic Drilling

Automatic drilling enables you to switch from the current group to another group using system-defined commands on the shortcut menu. Drilling is only available when a data component is created on a business view or has been converted to use a business view. Otherwise you will see [Going](https://devnet.logianalytics.com/hc/en-us/articles/1500009718141-Going) instead of Drilling actions.

It is divided into four types:

* [Drill-To](#Drill-to)  
   It enables you to obtain a different view of data by switching among groups.
* [Drill-to-by-Value](#Drill-to-by-value)  
   It enables you to filter data based on a drill-to action so as to obtain a more detailed view of the data.
* [Drill-Down](#Drill-down)  
   It enables you to drill data to lower groups according to predefined hierarchies. For more information about hierarchies, see Defining hierarchies in a business view in the *Logi JReport Designer User's Guide*.
* [Drill-Up](#Drill-up)  
  It enables you to drill data to higher groups according to predefined hierarchies.

These drill actions can be performed on crosstabs, charts, grouped tables and banded objects, whose data are based on business views or if on queries, data fields of which can be converted to corresponding view elements. After drilling, the new component can be analyzed in the same way as the original one.

Assume [you have created a crosstab report](https://devnet.logianalytics.com/hc/en-us/articles/1500009718121-Creating-Page-Reports#Crosstab) on the business view WorldWideSalesBV in Data Source 1 of the SampleReports catalog showing product sales information with Region as the column field, Sales Year as the row field, and Total Sales as the summary field, and applied the Classic style to the crosstab. The crosstab shows as follows:

![Create Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4412139528599/pgrpt_edit_drl_auto0.gif)

We will now take the crosstab as an instance to illustrate the automatic drilling functions.

## Drill-To

1. Right-click any value of Region, Asia-Pacific for example, and choose **Drill To** from the shortcut menu. The list of groups available for Drill To will appear on the submenu.

   ![Drill To](https://devnet.logianalytics.com/hc/article_attachments/4412131429399/pgrpt_edit_drl_auto1.gif)
2. Select **Product Type**  on the submenu, then in the regenerated result, we can see that Sales Year remains the group for rows and Product Type becomes the group for columns.

   ![Drill to Product Type](https://devnet.logianalytics.com/hc/article_attachments/4412112553367/pgrpt_edit_drl_auto2.gif)
3. Repeat Steps 1 and 2 to drill the data to other groups. Row field can also be drilled freely.
4. To go back to the original report, right-click any value of Product Type, choose **Drill To** > **Region** from the shortcut menu.

## Drill-to-by-Value

1. Go back to the original report in the above example.
2. Right-click the value **Asia-Pacific** of the Region group, and point to **Drill to by Value** on the shortcut menu. A submenu for the command is displayed, which lists the same items as those of Drill To.
3. Select **Product Type**  too and the result will be regenerated.

   ![Drill to by Value - Product Type](https://devnet.logianalytics.com/hc/article_attachments/4412112553623/pgrpt_edit_drl_auto3.gif)

   We can see that the result is different from that of drill-to. This is because that, for the drill-to-by-value action, the group of columns changes to Product Type by the Region value Asia-Pacific. That is, on the basis of the drill-to action, a filtering action where Region = Asia-Pacific is further performed, and thus the result of drill-to-by-value is generated.

   In addition, when a drill-to-by-value action is performed, the Drill Filter panel will be displayed on the left of the Page Report Studio window, which shows the group and the value the filter is based on.

   ![Drill Filter Panel](https://devnet.logianalytics.com/hc/article_attachments/4412139529623/pgrpt_edit_drl_auto7.gif)
4. To go back to the original report, first delete the drill filter in the Drill Filter panel by selecting **X** next to the group name, then right-click any value of Product Type and select **Drill To** > **Region** from the shortcut menu.

## Drill-Down

Drill-down actions are based on predefined business view hierarchies. The WorldWideSalesBV contains a hierarchy Geography, which allows you to drill a group (corresponding to a high level) down to the one-level-lower group.

1. Go back to the original report in the above example, right-click the value **North America** , on the shortcut menu, point to **Drill Down**, and we can see that Country is listed as the submenu item.

   ![Drill Down](https://devnet.logianalytics.com/hc/article_attachments/4412112553879/pgrpt_edit_drl_auto4.gif)
2. Select **Country**  to see the result. It displays the data about countries in the North America region.

   ![Drill Down to Country](https://devnet.logianalytics.com/hc/article_attachments/4412112554135/pgrpt_edit_drl_auto5.gif)
3. The one-level-lower group for Country defined in the hierarchy is State. Now click **Canada** directly and Logi JReport will also drill it down to State.

   ![Drill Down to State](https://devnet.logianalytics.com/hc/article_attachments/4412131429911/pgrpt_edit_drl_auto6.gif)

   After these two drill-down actions, we can see two filters are added in the Drill Filter panel, Region = North America and Country = Canada.

   ![Drill Filter Panel](https://devnet.logianalytics.com/hc/article_attachments/4412112554391/pgrpt_edit_drl_auto8.gif)

   This is because, when you perform a drill-down action, a filter will be created based on the value you select on. In this example, we first select on the North America region, so Logi JReport drills this region one-level down to display countries in North America, and thus the filter Region = North America is created. If you want all data in the one-level-lower group to be displayed when you drill down a group, you can remove the corresponding filter from the Drill Filter panel.

## Drill-Up

Drill-up actions allow you to drill a group (corresponding to a low level) up to the one-level-higher group.

1. Based on the report result after drill-down, right-click any value of State, BC for example, on the shortcut menu, point to **Drill Up**, and we can see that Country is listed as the submenu item.

   ![Drill Up](https://devnet.logianalytics.com/hc/article_attachments/4412131430295/pgrpt_edit_drl_auto9.gif)
2. Select **Country** to see the result. The group is drilled one level up. Country is now the group for columns.

   ![Drill Up to Country](https://devnet.logianalytics.com/hc/article_attachments/4412131430551/pgrpt_edit_drl_auto10.gif)
3. The one-level-higher group for Country defined in the hierarchy is Region. Now right-click any value of Country, Canada for example, on the shortcut menu, point to **Drill Up** and select **Region**, Logi JReport will drill it up to Region.

   ![Drill Up to Region](https://devnet.logianalytics.com/hc/article_attachments/4412112554647/pgrpt_edit_drl_auto11.gif)

**Notes:**

* A [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009691022-Logi-JReport-licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.
* For banded object and table, you can right-click its group header/footer to show the shortcut menu so as to use the automatic drilling functions, you can also right-click field values in the group header/footer to achieve this.
* For group objects that not used as group fields in a banded object or table, automatic drilling doesn't take effect.
* For page reports created in Logi JReport Designer, if you want to directly select the group objects to perform the drill-down action, the select priority of the drill-down action must have been specified to be the highest at report design time. Otherwise, you have to use the Drill Down command on the objects' shortcut menu to perform the action.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691542-Drilling-Through-the-Report-Data)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718141-Going)
