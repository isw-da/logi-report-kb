---
title: "Automatic Drilling Page Report Data"
id: 5741438817175
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741438817175-Automatic-Drilling-Page-Report-Data
updated_at: 2022-10-31T17:18:15Z
---

# Automatic Drilling Page Report Data

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741482750999-Drill-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741474913047-Going-Through-Page-Report-Data)

# Automatic Drilling Page Report Data

Automatic drilling enables you to switch from the current group to another group using system-defined commands on the shortcut menu. This topic describes how you can drill to, drill to by value, drill up, and drill down groups in page reports.

Drilling is only available when a data component bases on a business view or has been converted to use a business view. Otherwise you will see [Going](https://devnet.logianalytics.com/hc/en-us/articles/5741474913047-Going-Through-Page-Report-Data) instead of Drilling actions.

You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/5741452341143-Logi-Report-Licenses#ServerLive) to perform drilling on data components in Page Report Studio. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

Automatic drilling is divided into four types:

* [Drill-To](#Drill-to)  
  It enables you to obtain a different view of data by switching among groups.
* [Drill-to-by-Value](#Drill-to-by-value)  
  It enables you to filter data based on a drill-to action so as to obtain a more detailed view of the data.
* [Drill-Down](#Drill-down)  
  It enables you to drill data to lower groups according to predefined hierarchies. For more information about hierarchies, refer to Defining Hierarchies in a Business View in the *Logi Report Designer Guide*.
* [Drill-Up](#Drill-up)  
  It enables you to drill data to higher groups according to predefined hierarchies.

You can perform these drill actions on crosstabs, charts, grouped tables, and banded objects, whose data bases on business views or if on queries, data fields of which can be converted to corresponding view elements. After drilling, you can analyze the new component in the same way as you do to the original one.

Assume [you have created a crosstab report](https://devnet.logianalytics.com/hc/en-us/articles/5741469017879-Creating-Page-Reports#Crosstab) on the business view WorldWideSalesBV in Data Source 1 of the SampleReports catalog showing product sales information with Region as the column field, Sales Year as the row field, and Total Sales as the summary field, and applied the Classic style to the crosstab. The crosstab shows as follows:

![Create Crosstab](https://devnet.logianalytics.com/hc/article_attachments/9905662409495/pgrpt_edit_drl_auto0.gif)

We will now take the crosstab as an instance to illustrate the automatic drilling functions.

## Drill-To

1. Right-click any value of Region, Asia-Pacific for example, and choose **Drill To** from the shortcut menu. The list of groups available for Drill To will appear on the submenu.

   ![Drill To](https://devnet.logianalytics.com/hc/article_attachments/9905674336151/pgrpt_edit_drl_auto1.gif)
2. Select **Product Type**  on the submenu, then in the regenerated report, we can see that Sales Year remains the group for rows and Product Type becomes the group for columns.

   ![Drill to Product Type](https://devnet.logianalytics.com/hc/article_attachments/9905674381207/pgrpt_edit_drl_auto2.gif)
3. Repeat Steps 1 and 2 to drill the data to other groups. Row field can also be drilled freely.
4. To go back to the original report, right-click any value of Product Type, choose **Drill To** > **Region** from the shortcut menu.

## Drill-to-by-Value

1. Go back to the original report in the preceding example.
2. Right-click the value **Asia-Pacific** of the Region group, and select **Drill to by Value** on the shortcut menu. Server displays a submenu for the command and lists the same items as those of **Drill To**.
3. Select **Product Type**  too. Server regenerates the report.

   ![Drill to by Value - Product Type](https://devnet.logianalytics.com/hc/article_attachments/9905674397079/pgrpt_edit_drl_auto3.gif)

   We can see that the report is different from that of drill-to. This is because that, for the drill-to-by-value action, the group of columns changes to Product Type by the Region value Asia-Pacific. That is, on the basis of the drill-to action, Server further performs a filtering action where Region = Asia-Pacific, and thus generates the report of drill-to-by-value.

   In addition, when you perform a drill-to-by-value action, Server displays the Drill Filter panel on the left of the Page Report Studio, which shows the group and the value the filter is based on.

   ![Drill Filter Panel](https://devnet.logianalytics.com/hc/article_attachments/9905662550551/pgrpt_edit_drl_auto7.gif)
4. To go back to the original report, first delete the drill filter in the Drill Filter panel by selecting **X** next to the group name, then right-click any value of Product Type and select **Drill To** > **Region** from the shortcut menu.

## Drill-Down

Drill-down actions are based on predefined business view hierarchies. The WorldWideSalesBV contains a hierarchy Geography, which enables you to drill a group (corresponding to a high level) down to the one-level-lower group.

1. Go back to the original report in the preceding example, right-click the value **North America**, then select **Drill Down** on the shortcut menu. We can see that **Country** is the submenu item.

   ![Drill Down](https://devnet.logianalytics.com/hc/article_attachments/9905712931607/pgrpt_edit_drl_auto4.gif)
2. Select **Country** to see the report. It displays the data about countries in the North America region.

   ![Drill Down to Country](https://devnet.logianalytics.com/hc/article_attachments/9905712992791/pgrpt_edit_drl_auto5.gif)
3. The one-level-lower group for Country defined in the hierarchy is State. Now select **Canada** directly and Server also drills it down to **State**.

   ![Drill Down to State](https://devnet.logianalytics.com/hc/article_attachments/9905674586263/pgrpt_edit_drl_auto6.gif)

   After these two drill-down actions, we can see two filters in the Drill Filter panel, Region = North America and Country = Canada.

   ![Drill Filter Panel](https://devnet.logianalytics.com/hc/article_attachments/9905674616727/pgrpt_edit_drl_auto8.gif)

   This is because, when you perform a drill-down action, Server creates a filter based on the value you select on. In this example, we first select the North America region, so Server drills this region to the lower level to display countries in North America, and thus creates the filter Region = North America. If you want to display all data in the one-level-lower group when you drill down a group, you can remove the corresponding filter from the **Drill Filter** panel.

## Drill-Up

Drill-up actions enable you to drill a group (corresponding to a low level) up to the one-level-higher group.

1. Based on the report after drill-down, right-click any value of State, BC for example, then select **Drill Up** on the shortcut menu. We can see that Country is the submenu item.

   ![Drill Up](https://devnet.logianalytics.com/hc/article_attachments/9905674643351/pgrpt_edit_drl_auto9.gif)
2. Select **Country** to see the report. The group goes to the higher level. Country is now the group for columns.

   ![Drill Up to Country](https://devnet.logianalytics.com/hc/article_attachments/9905674664343/pgrpt_edit_drl_auto10.gif)
3. The one-level-higher group for Country defined in the hierarchy is Region. Now right-click any value of Country, Canada for example, then select **Drill Up** > **Region** on the shortcut menu. Server drills it up to Region.

   ![Drill Up to Region](https://devnet.logianalytics.com/hc/article_attachments/9905674692375/pgrpt_edit_drl_auto11.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg)

* For a banded object or table, you can right-click its group header/footer to show the shortcut menu so as to use the automatic drilling functions. You can also right-click field values in the group header/footer to achieve this.
* For group objects that are not used as group fields in a banded object or table, automatic drilling does not take effect.
* For page reports created in Logi Report Designer, if you want to directly select the group objects to perform the drill-down action, the report designer must have given the "Drill-down" action the highest Click Priority at report design time. Otherwise, you have to use the Drill Down command on the objects' shortcut menu to perform the action.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741482750999-Drill-Page-Report-Data)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741474913047-Going-Through-Page-Report-Data)
